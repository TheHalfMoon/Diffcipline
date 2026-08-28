use std::env;
use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, ExitCode};

const POLICY_FILE: &str = ".diffcipline.toml";

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Verdict {
    Pass,
    Review,
    Fail,
}

impl Verdict {
    fn name(self) -> &'static str {
        match self {
            Self::Pass => "PASS",
            Self::Review => "REVIEW",
            Self::Fail => "FAIL",
        }
    }

    fn exit_code(self) -> u8 {
        match self {
            Self::Pass => 0,
            Self::Review => 1,
            Self::Fail => 2,
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Decision {
    Allow,
    Review,
    Fail,
}

impl Decision {
    fn parse(value: &str) -> Result<Self, String> {
        match value.trim().trim_matches('"') {
            "allow" => Ok(Self::Allow),
            "review" => Ok(Self::Review),
            "fail" => Ok(Self::Fail),
            other => Err(format!("unknown policy decision: {other}")),
        }
    }

    fn verdict(self) -> Verdict {
        match self {
            Self::Allow => Verdict::Pass,
            Self::Review => Verdict::Review,
            Self::Fail => Verdict::Fail,
        }
    }
}

#[derive(Debug)]
struct Policy {
    version: u32,
    max_changed_files: usize,
    max_added_lines: usize,
    dependency_manifest_changes: Decision,
    lockfile_changes: Decision,
    untracked_files: Decision,
    commands: Vec<String>,
}

impl Default for Policy {
    fn default() -> Self {
        Self {
            version: 1,
            max_changed_files: 12,
            max_added_lines: 400,
            dependency_manifest_changes: Decision::Review,
            lockfile_changes: Decision::Review,
            untracked_files: Decision::Review,
            commands: Vec::new(),
        }
    }
}

#[derive(Debug)]
struct Stats {
    files: Vec<String>,
    added: usize,
    deleted: usize,
    manifests: Vec<String>,
    lockfiles: Vec<String>,
    untracked: Vec<String>,
}

#[derive(Debug)]
struct CheckResult {
    verdict: Verdict,
    stats: Stats,
    reasons: Vec<String>,
    verification: Vec<(String, Option<bool>)>,
}

fn main() -> ExitCode {
    match run() {
        Ok(verdict) => ExitCode::from(verdict.exit_code()),
        Err(error) => {
            eprintln!("diffcipline: {error}");
            ExitCode::from(64)
        }
    }
}

fn run() -> Result<Verdict, String> {
    let mut args = env::args().skip(1);

    match args.next().as_deref() {
        None | Some("help") | Some("--help") | Some("-h") => {
            print_help();
            Ok(Verdict::Pass)
        }
        Some("init") => {
            if args.next().is_some() {
                return Err("usage: diffcipline init".into());
            }
            init_policy()?;
            Ok(Verdict::Pass)
        }
        Some("check") => run_check(args.collect()),
        Some(other) => Err(format!("unknown command: {other}")),
    }
}

fn run_check(args: Vec<String>) -> Result<Verdict, String> {
    let mut base = None;
    let mut execute = false;
    let mut json = false;
    let mut index = 0;

    while index < args.len() {
        match args[index].as_str() {
            "--base" => {
                index += 1;
                base = Some(args.get(index).ok_or("--base requires a ref")?.to_string());
            }
            "--run" => execute = true,
            "--json" => json = true,
            other => return Err(format!("unknown check option: {other}")),
        }
        index += 1;
    }

    let result = check(base.as_deref(), execute)?;
    if json {
        println!("{}", to_json(&result, base.as_deref()));
    } else {
        print_result(&result, base.as_deref());
    }
    Ok(result.verdict)
}

fn print_help() {
    println!(
        "Diffcipline — discipline for coding agents\n\n\
Usage:\n  diffcipline init\n  diffcipline check [--base <ref>] [--run] [--json]\n\n\
Exit codes:\n  0 PASS\n  1 REVIEW\n  2 FAIL\n  64 usage/execution error"
    );
}

fn init_policy() -> Result<(), String> {
    let root = git_root()?;
    let path = root.join(POLICY_FILE);
    if path.exists() {
        println!("{} already exists; left unchanged.", path.display());
        return Ok(());
    }

    let commands = detect_commands(&root);
    let rendered = commands
        .iter()
        .map(|value| format!("\"{}\"", toml_escape(value)))
        .collect::<Vec<_>>()
        .join(", ");
    let content = format!(
        "version = 1\n\n[policy]\nmax_changed_files = 12\nmax_added_lines = 400\n\
dependency_manifest_changes = \"review\"\nlockfile_changes = \"review\"\n\
untracked_files = \"review\"\n\n[verification]\ncommands = [{rendered}]\n"
    );

    fs::write(&path, content).map_err(|error| format!("write {}: {error}", path.display()))?;
    println!("Created {}.", path.display());
    Ok(())
}

fn detect_commands(root: &Path) -> Vec<String> {
    if root.join("Cargo.toml").exists() {
        vec![
            "cargo fmt --all -- --check".into(),
            "cargo clippy --workspace --all-targets -- -D warnings".into(),
            "cargo test --workspace --all-targets".into(),
        ]
    } else if root.join("package.json").exists() {
        vec!["npm test".into()]
    } else if root.join("pyproject.toml").exists() || root.join("pytest.ini").exists() {
        vec!["python -m pytest".into()]
    } else if root.join("go.mod").exists() {
        vec!["go test ./...".into()]
    } else {
        Vec::new()
    }
}

fn check(base: Option<&str>, execute: bool) -> Result<CheckResult, String> {
    let root = git_root()?;
    let policy_path = root.join(POLICY_FILE);
    let policy = if policy_path.exists() {
        let text = fs::read_to_string(&policy_path)
            .map_err(|error| format!("read {}: {error}", policy_path.display()))?;
        parse_policy(&text)?
    } else {
        Policy::default()
    };

    if policy.version != 1 {
        return Err(format!("unsupported policy version: {}", policy.version));
    }

    let stats = collect_stats(&root, base)?;
    let mut verdict = Verdict::Pass;
    let mut reasons = Vec::new();

    if stats.files.len() > policy.max_changed_files {
        verdict = Verdict::Fail;
        reasons.push(format!(
            "changed files {} exceed maximum {}",
            stats.files.len(),
            policy.max_changed_files
        ));
    }
    if stats.added > policy.max_added_lines {
        verdict = Verdict::Fail;
        reasons.push(format!(
            "added lines {} exceed maximum {}",
            stats.added, policy.max_added_lines
        ));
    }

    apply_decision(
        !stats.manifests.is_empty(),
        policy.dependency_manifest_changes,
        format!(
            "dependency manifest changed: {}",
            stats.manifests.join(", ")
        ),
        &mut verdict,
        &mut reasons,
    );
    apply_decision(
        !stats.lockfiles.is_empty(),
        policy.lockfile_changes,
        format!("lockfile changed: {}", stats.lockfiles.join(", ")),
        &mut verdict,
        &mut reasons,
    );
    apply_decision(
        !stats.untracked.is_empty(),
        policy.untracked_files,
        format!("untracked files remain: {}", stats.untracked.join(", ")),
        &mut verdict,
        &mut reasons,
    );

    let mut verification = Vec::new();
    if policy.commands.is_empty() {
        verdict = verdict.max(Verdict::Review);
        reasons.push("no verification commands configured".into());
    } else if execute {
        for command in policy.commands {
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
        verification.extend(policy.commands.into_iter().map(|command| (command, None)));
    }

    if stats.files.is_empty() && stats.untracked.is_empty() {
        verdict = verdict.max(Verdict::Review);
        reasons.push("no change detected".into());
    }

    Ok(CheckResult {
        verdict,
        stats,
        reasons,
        verification,
    })
}

fn apply_decision(
    condition: bool,
    decision: Decision,
    reason: String,
    verdict: &mut Verdict,
    reasons: &mut Vec<String>,
) {
    if condition {
        *verdict = (*verdict).max(decision.verdict());
        if decision != Decision::Allow {
            reasons.push(reason);
        }
    }
}

fn collect_stats(root: &Path, base: Option<&str>) -> Result<Stats, String> {
    let range = base.map(|value| format!("{value}...HEAD"));
    let mut numstat = vec!["diff".to_string(), "--numstat".to_string()];
    let mut names = vec!["diff".to_string(), "--name-only".to_string()];

    if let Some(range) = &range {
        numstat.push(range.clone());
        names.push(range.clone());
    } else {
        numstat.push("HEAD".into());
        names.push("HEAD".into());
    }

    let output = git(root, &numstat)?;
    let files_output = git(root, &names)?;
    let files = files_output
        .lines()
        .filter(|value| !value.is_empty())
        .map(str::to_owned)
        .collect::<Vec<_>>();

    let mut added = 0;
    let mut deleted = 0;
    for line in output.lines() {
        let mut fields = line.splitn(3, '\t');
        added += fields
            .next()
            .and_then(|value| value.parse::<usize>().ok())
            .unwrap_or(0);
        deleted += fields
            .next()
            .and_then(|value| value.parse::<usize>().ok())
            .unwrap_or(0);
    }

    let manifests = files
        .iter()
        .filter(|path| is_manifest(path))
        .cloned()
        .collect();
    let lockfiles = files
        .iter()
        .filter(|path| is_lockfile(path))
        .cloned()
        .collect();
    let untracked = git(
        root,
        &[
            "ls-files".into(),
            "--others".into(),
            "--exclude-standard".into(),
        ],
    )?
    .lines()
    .filter(|value| !value.is_empty())
    .map(str::to_owned)
    .collect();

    Ok(Stats {
        files,
        added,
        deleted,
        manifests,
        lockfiles,
        untracked,
    })
}

fn is_manifest(path: &str) -> bool {
    let name = path.rsplit('/').next().unwrap_or(path);
    matches!(
        name,
        "Cargo.toml" | "package.json" | "pyproject.toml" | "go.mod" | "Gemfile" | "composer.json"
    ) || name.starts_with("requirements") && name.ends_with(".txt")
}

fn is_lockfile(path: &str) -> bool {
    matches!(
        path.rsplit('/').next().unwrap_or(path),
        "Cargo.lock"
            | "package-lock.json"
            | "pnpm-lock.yaml"
            | "yarn.lock"
            | "uv.lock"
            | "poetry.lock"
            | "Gemfile.lock"
            | "composer.lock"
    )
}

fn git_root() -> Result<PathBuf, String> {
    let output = Command::new("git")
        .args(["rev-parse", "--show-toplevel"])
        .output()
        .map_err(|error| format!("run git: {error}"))?;
    if !output.status.success() {
        return Err("not inside a Git repository".into());
    }
    Ok(PathBuf::from(
        String::from_utf8_lossy(&output.stdout).trim(),
    ))
}

fn git(root: &Path, args: &[String]) -> Result<String, String> {
    let output = Command::new("git")
        .args(args)
        .current_dir(root)
        .output()
        .map_err(|error| format!("run git: {error}"))?;
    if !output.status.success() {
        return Err(format!(
            "git {} failed: {}",
            args.join(" "),
            String::from_utf8_lossy(&output.stderr).trim()
        ));
    }
    Ok(String::from_utf8_lossy(&output.stdout).into_owned())
}

fn run_shell(root: &Path, command: &str) -> Result<bool, String> {
    #[cfg(windows)]
    let status = Command::new("cmd")
        .args(["/C", command])
        .current_dir(root)
        .status();

    #[cfg(not(windows))]
    let status = Command::new("sh")
        .args(["-lc", command])
        .current_dir(root)
        .status();

    status
        .map(|value| value.success())
        .map_err(|error| format!("run verification: {error}"))
}

fn parse_policy(input: &str) -> Result<Policy, String> {
    let mut policy = Policy::default();
    let mut section = String::new();

    for (index, raw) in input.lines().enumerate() {
        let line = strip_comment(raw).trim();
        if line.is_empty() {
            continue;
        }
        if line.starts_with('[') && line.ends_with(']') {
            section = line[1..line.len() - 1].to_string();
            if section != "policy" && section != "verification" {
                return Err(format!(
                    "unsupported section at line {}: {section}",
                    index + 1
                ));
            }
            continue;
        }

        let (key, value) = line
            .split_once('=')
            .ok_or_else(|| format!("invalid policy line {}", index + 1))?;
        let key = key.trim();
        let value = value.trim();

        match (section.as_str(), key) {
            ("", "version") => {
                policy.version = value.parse().map_err(|_| "version must be an integer")?;
            }
            ("policy", "max_changed_files") => {
                policy.max_changed_files = value
                    .parse()
                    .map_err(|_| "max_changed_files must be an integer")?;
            }
            ("policy", "max_added_lines") => {
                policy.max_added_lines = value
                    .parse()
                    .map_err(|_| "max_added_lines must be an integer")?;
            }
            ("policy", "dependency_manifest_changes") => {
                policy.dependency_manifest_changes = Decision::parse(value)?;
            }
            ("policy", "lockfile_changes") => {
                policy.lockfile_changes = Decision::parse(value)?;
            }
            ("policy", "untracked_files") => {
                policy.untracked_files = Decision::parse(value)?;
            }
            ("verification", "commands") => {
                policy.commands = parse_array(value)?;
            }
            _ => {
                return Err(format!(
                    "unsupported policy key at line {}: {key}",
                    index + 1
                ));
            }
        }
    }

    Ok(policy)
}

fn strip_comment(line: &str) -> &str {
    let mut quoted = false;
    let mut escaped = false;
    for (index, character) in line.char_indices() {
        match character {
            '\\' if quoted => escaped = !escaped,
            '"' if !escaped => quoted = !quoted,
            '#' if !quoted => return &line[..index],
            _ => escaped = false,
        }
    }
    line
}

fn parse_array(value: &str) -> Result<Vec<String>, String> {
    let value = value.trim();
    if !value.starts_with('[') || !value.ends_with(']') {
        return Err("commands must be an array".into());
    }
    let inner = value[1..value.len() - 1].trim();
    if inner.is_empty() {
        return Ok(Vec::new());
    }

    inner
        .split(',')
        .map(|item| {
            let item = item.trim();
            if item.len() < 2 || !item.starts_with('"') || !item.ends_with('"') {
                return Err("commands must contain quoted strings".into());
            }
            Ok(item[1..item.len() - 1]
                .replace("\\\"", "\"")
                .replace("\\\\", "\\"))
        })
        .collect()
}

fn toml_escape(value: &str) -> String {
    value.replace('\\', "\\\\").replace('"', "\\\"")
}

fn print_result(result: &CheckResult, base: Option<&str>) {
    println!("DIFFCIPLINE PROOF\n");
    println!("Verdict       {}", result.verdict.name());
    println!(
        "Comparison    {}",
        base.map(|value| format!("{value}...HEAD"))
            .unwrap_or_else(|| "HEAD vs working tree".into())
    );
    println!("Changed       {} files", result.stats.files.len());
    println!(
        "Diff          +{} / -{}",
        result.stats.added, result.stats.deleted
    );
    println!(
        "Dependencies  {}",
        if result.stats.manifests.is_empty() {
            "unchanged".into()
        } else {
            result.stats.manifests.join(", ")
        }
    );
    println!(
        "Lockfiles     {}",
        if result.stats.lockfiles.is_empty() {
            "unchanged".into()
        } else {
            result.stats.lockfiles.join(", ")
        }
    );
    println!("Untracked     {}", result.stats.untracked.len());

    for (command, state) in &result.verification {
        let label = match state {
            Some(true) => "PASS",
            Some(false) => "FAIL",
            None => "NOT RUN",
        };
        println!("Verification  {label} — {command}");
    }

    if !result.reasons.is_empty() {
        println!("\nReasons:");
        for reason in &result.reasons {
            println!("- {reason}");
        }
    }
    println!("\n{}", result.verdict.name());
}

fn to_json(result: &CheckResult, base: Option<&str>) -> String {
    let files = result
        .stats
        .files
        .iter()
        .map(|value| format!("\"{}\"", json_escape(value)))
        .collect::<Vec<_>>()
        .join(",");
    let reasons = result
        .reasons
        .iter()
        .map(|value| format!("\"{}\"", json_escape(value)))
        .collect::<Vec<_>>()
        .join(",");
    let base = base
        .map(|value| format!("\"{}\"", json_escape(value)))
        .unwrap_or_else(|| "null".into());

    format!(
        "{{\"verdict\":\"{}\",\"base\":{},\"changed_files\":{},\"added_lines\":{},\"deleted_lines\":{},\"files\":[{}],\"reasons\":[{}]}}",
        result.verdict.name(),
        base,
        result.stats.files.len(),
        result.stats.added,
        result.stats.deleted,
        files,
        reasons
    )
}

fn json_escape(value: &str) -> String {
    value
        .replace('\\', "\\\\")
        .replace('"', "\\\"")
        .replace('\n', "\\n")
        .replace('\r', "\\r")
        .replace('\t', "\\t")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn policy_parses_and_fails_closed() {
        let policy = parse_policy(
            "version = 1\n[policy]\nmax_changed_files = 7\nmax_added_lines = 80\n\
dependency_manifest_changes = \"fail\"\nlockfile_changes = \"review\"\n\
untracked_files = \"allow\"\n[verification]\ncommands = [\"cargo test\"]\n",
        )
        .unwrap();

        assert_eq!(policy.max_changed_files, 7);
        assert_eq!(policy.dependency_manifest_changes, Decision::Fail);
        assert!(parse_policy("version = 1\n[policy]\nunknown = 1\n").is_err());
    }

    #[test]
    fn dependency_files_are_classified() {
        assert!(is_manifest("Cargo.toml"));
        assert!(is_manifest("apps/web/package.json"));
        assert!(is_manifest("requirements-dev.txt"));
        assert!(is_lockfile("nested/Cargo.lock"));
        assert!(!is_manifest("src/package.rs"));
    }

    #[test]
    fn comments_inside_strings_survive() {
        assert_eq!(
            strip_comment("commands = [\"echo # ok\"] # comment"),
            "commands = [\"echo # ok\"] "
        );
    }

    #[test]
    fn verdicts_only_escalate() {
        assert_eq!(Verdict::Pass.max(Verdict::Review), Verdict::Review);
        assert_eq!(Verdict::Review.max(Verdict::Fail), Verdict::Fail);
    }
}
