use super::*;

pub(super) fn run_check(args: Vec<String>) -> Result<Verdict, String> {
    let mut base = None;
    let mut risk = None;
    let mut execute = false;
    let mut json = false;
    let mut enterprise_policy = None;
    let mut index = 0;

    while index < args.len() {
        match args[index].as_str() {
            "--base" => {
                index += 1;
                base = Some(args.get(index).ok_or("--base requires a ref")?.to_string());
            }
            "--risk" => {
                index += 1;
                risk = Some(Risk::parse(
                    args.get(index).ok_or("--risk requires R0, R1, R2, or R3")?,
                )?);
            }
            "--enterprise-policy" => {
                if enterprise_policy.is_some() {
                    return Err("--enterprise-policy may be specified only once".into());
                }
                index += 1;
                enterprise_policy = Some(
                    args.get(index)
                        .ok_or("--enterprise-policy requires a local file path")?
                        .to_string(),
                );
            }
            "--run" => execute = true,
            "--json" => json = true,
            other => return Err(format!("unknown check option: {other}")),
        }
        index += 1;
    }

    let source = enterprise_policy.ok_or("--enterprise-policy requires a local file path")?;
    let (result, sources) = check_enterprise(base.as_deref(), execute, risk, &source)?;
    if json {
        println!(
            "{}",
            to_json(&result, base.as_deref(), "enterprise", &sources)
        );
    } else {
        print_result(&result, base.as_deref());
    }
    Ok(result.verdict)
}

fn check_enterprise(
    base: Option<&str>,
    execute: bool,
    risk: Option<Risk>,
    enterprise_source: &str,
) -> Result<(CheckResult, Vec<String>), String> {
    let root = git_root()?;
    let repository_path = root.join(POLICY_FILE);
    let repository_exists = repository_path.exists();
    let repository = if repository_exists {
        read_policy(&repository_path, POLICY_FILE)?
    } else {
        Policy::default()
    };

    let requested = Path::new(enterprise_source);
    let enterprise_path = if requested.is_absolute() {
        requested.to_path_buf()
    } else {
        root.join(requested)
    };
    let enterprise = read_policy(&enterprise_path, enterprise_source)?;

    if repository_exists {
        let repository_real = fs::canonicalize(&repository_path)
            .map_err(|error| format!("resolve {POLICY_FILE}: {error}"))?;
        let enterprise_real = fs::canonicalize(&enterprise_path)
            .map_err(|error| format!("resolve enterprise policy {enterprise_source}: {error}"))?;
        if repository_real == enterprise_real {
            return Err("enterprise policy must be distinct from .diffcipline.toml".into());
        }
    }

    let effective = merge_policies(&enterprise, &repository);
    let commands = verification_commands(&effective, risk)?.to_vec();
    let stats = collect_stats(&root, base)?;
    let mut verdict = Verdict::Pass;
    let mut reasons = Vec::new();

    if stats.files.len() > effective.max_changed_files {
        verdict = Verdict::Fail;
        reasons.push(format!(
            "changed files {} exceed maximum {}",
            stats.files.len(),
            effective.max_changed_files
        ));
    }
    if stats.added > effective.max_added_lines {
        verdict = Verdict::Fail;
        reasons.push(format!(
            "added lines {} exceed maximum {}",
            stats.added, effective.max_added_lines
        ));
    }
    for (condition, decision, reason) in [
        (
            !stats.manifests.is_empty(),
            effective.dependency_manifest_changes,
            format!(
                "dependency manifest changed: {}",
                stats.manifests.join(", ")
            ),
        ),
        (
            !stats.lockfiles.is_empty(),
            effective.lockfile_changes,
            format!("lockfile changed: {}", stats.lockfiles.join(", ")),
        ),
        (
            !stats.untracked.is_empty(),
            effective.untracked_files,
            format!("untracked files remain: {}", stats.untracked.join(", ")),
        ),
    ] {
        apply_decision(condition, decision, reason, &mut verdict, &mut reasons);
    }

    let scope_violations = layered_scope_violations(
        &enterprise.expected_files,
        &repository.expected_files,
        &effective.forbidden_surfaces,
        &changed_paths(&stats),
    );
    for reason in &scope_violations {
        verdict = Verdict::Fail;
        reasons.push(reason.clone());
    }

    let mut verification = Vec::new();
    if commands.is_empty() {
        verdict = verdict.max(Verdict::Review);
        reasons.push("no verification commands configured".into());
    } else if execute {
        for command in commands {
            let success = run_shell(&root, &command)?;
            verification.push((command.clone(), Some(success)));
            if !success {
                verdict = Verdict::Fail;
                reasons.push(format!("verification failed: {command}"));
            }
        }
    } else {
        verdict = verdict.max(Verdict::Review);
        reasons.push("verification configured but NOT RUN".into());
        verification.extend(commands.into_iter().map(|command| (command, None)));
    }
    if stats.files.is_empty() && stats.untracked.is_empty() {
        verdict = verdict.max(Verdict::Review);
        reasons.push("no change detected".into());
    }

    let mut sources = vec![enterprise_source.to_string()];
    if repository_exists {
        sources.push(POLICY_FILE.into());
    }
    Ok((
        CheckResult {
            verdict,
            risk,
            expected_files: effective.expected_files,
            forbidden_surfaces: effective.forbidden_surfaces,
            scope_violations,
            stats,
            reasons,
            verification,
        },
        sources,
    ))
}

fn read_policy(path: &Path, source: &str) -> Result<Policy, String> {
    let text = fs::read_to_string(path).map_err(|error| format!("read {source}: {error}"))?;
    let policy = parse_policy(&text)?;
    if policy.version != 1 {
        return Err(format!(
            "unsupported policy version in {source}: {}",
            policy.version
        ));
    }
    Ok(policy)
}

fn merge_policies(enterprise: &Policy, repository: &Policy) -> Policy {
    Policy {
        version: 1,
        max_changed_files: enterprise
            .max_changed_files
            .min(repository.max_changed_files),
        max_added_lines: enterprise.max_added_lines.min(repository.max_added_lines),
        dependency_manifest_changes: stricter(
            enterprise.dependency_manifest_changes,
            repository.dependency_manifest_changes,
        ),
        lockfile_changes: stricter(enterprise.lockfile_changes, repository.lockfile_changes),
        untracked_files: stricter(enterprise.untracked_files, repository.untracked_files),
        expected_files: merged(&enterprise.expected_files, &repository.expected_files),
        forbidden_surfaces: merged(
            &enterprise.forbidden_surfaces,
            &repository.forbidden_surfaces,
        ),
        commands: merged(&enterprise.commands, &repository.commands),
        r0_commands: merged(&enterprise.r0_commands, &repository.r0_commands),
        r1_commands: merged(&enterprise.r1_commands, &repository.r1_commands),
        r2_commands: merged(&enterprise.r2_commands, &repository.r2_commands),
        r3_commands: merged(&enterprise.r3_commands, &repository.r3_commands),
    }
}

fn stricter(left: Decision, right: Decision) -> Decision {
    match (left, right) {
        (Decision::Fail, _) | (_, Decision::Fail) => Decision::Fail,
        (Decision::Review, _) | (_, Decision::Review) => Decision::Review,
        _ => Decision::Allow,
    }
}

fn merged(first: &[String], second: &[String]) -> Vec<String> {
    let mut values = Vec::new();
    for value in first.iter().chain(second) {
        if !values.contains(value) {
            values.push(value.clone());
        }
    }
    values
}

fn layered_scope_violations(
    enterprise_expected: &[String],
    repository_expected: &[String],
    forbidden: &[String],
    paths: &[String],
) -> Vec<String> {
    let mut reasons = Vec::new();
    for path in paths {
        for (label, patterns) in [
            ("enterprise", enterprise_expected),
            ("repository", repository_expected),
        ] {
            if !patterns.is_empty()
                && !patterns
                    .iter()
                    .any(|pattern| path_pattern_matches(pattern, path))
            {
                reasons.push(format!("{label} expected-files contract rejected: {path}"));
            }
        }
        if forbidden
            .iter()
            .any(|pattern| path_pattern_matches(pattern, path))
        {
            reasons.push(format!("forbidden surface changed: {path}"));
        }
    }
    reasons
}
