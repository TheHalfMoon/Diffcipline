#[allow(dead_code)]
mod legacy {
    include!("main.rs");

    const PROOF_SCHEMA: &str = "diffcipline.proof/v1";
    const PROOF_SCHEMA_VERSION: &str = "1.0";
    const PROOF_SCHEMA_DOCUMENT: &str = include_str!("../../../schemas/proof-v1.json");

    pub fn main_v1() -> ExitCode {
        match run_v1() {
            Ok(verdict) => ExitCode::from(verdict.exit_code()),
            Err(error) => {
                eprintln!("diffcipline: {error}");
                ExitCode::from(64)
            }
        }
    }

    fn run_v1() -> Result<Verdict, String> {
        let mut args = env::args().skip(1);
        match args.next().as_deref() {
            Some("check") => run_check_v1(args.collect()),
            _ => run(),
        }
    }

    fn run_check_v1(args: Vec<String>) -> Result<Verdict, String> {
        let mut base = None;
        let mut risk = None;
        let mut execute = false;
        let mut json = false;
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
                "--run" => execute = true,
                "--json" => json = true,
                other => return Err(format!("unknown check option: {other}")),
            }
            index += 1;
        }

        let result = check(base.as_deref(), execute, risk)?;
        if json {
            let (mode, sources) = policy_provenance()?;
            println!("{}", to_json_v1(&result, base.as_deref(), mode, &sources));
        } else {
            print_result(&result, base.as_deref());
        }
        Ok(result.verdict)
    }

    fn policy_provenance() -> Result<(&'static str, Vec<String>), String> {
        let root = git_root()?;
        if root.join(POLICY_FILE).exists() {
            Ok(("repository", vec![POLICY_FILE.into()]))
        } else {
            Ok(("default", Vec::new()))
        }
    }

    fn to_json_v1(
        result: &CheckResult,
        base: Option<&str>,
        policy_mode: &str,
        policy_sources: &[String],
    ) -> String {
        let legacy = to_json(result, base);
        let tail = legacy
            .strip_prefix('{')
            .expect("legacy JSON is always an object");
        format!(
            "{{\"schema\":\"{}\",\"schema_version\":\"{}\",\"policy\":{{\"mode\":\"{}\",\"sources\":[{}]}},{}",
            PROOF_SCHEMA,
            PROOF_SCHEMA_VERSION,
            json_escape(policy_mode),
            json_string_array(policy_sources),
            tail
        )
    }

    #[cfg(test)]
    mod v1_tests {
        use super::*;

        #[test]
        fn schema_identity_and_legacy_fields_are_stable() {
            let result = CheckResult {
                verdict: Verdict::Review,
                risk: None,
                expected_files: Vec::new(),
                forbidden_surfaces: Vec::new(),
                scope_violations: Vec::new(),
                stats: Stats {
                    files: Vec::new(),
                    added: 0,
                    deleted: 0,
                    manifests: Vec::new(),
                    lockfiles: Vec::new(),
                    untracked: Vec::new(),
                },
                reasons: vec!["no change detected".into()],
                verification: vec![("cargo test".into(), None)],
            };

            let json = to_json_v1(&result, None, "repository", &[POLICY_FILE.into()]);
            assert!(json.starts_with(
                "{\"schema\":\"diffcipline.proof/v1\",\"schema_version\":\"1.0\",\"policy\":{"
            ));
            for field in [
                "verdict",
                "base",
                "changed_files",
                "added_lines",
                "deleted_lines",
                "files",
                "reasons",
                "risk",
                "expected_files",
                "forbidden_surfaces",
                "scope_violations",
                "verification",
            ] {
                assert!(json.contains(&format!("\"{field}\":")), "{field}");
            }
        }

        #[test]
        fn repository_schema_declares_v1_identity() {
            assert!(PROOF_SCHEMA_DOCUMENT.contains("\"$id\": \"diffcipline.proof/v1\""));
            assert!(PROOF_SCHEMA_DOCUMENT.contains("\"schema_version\""));
            assert!(PROOF_SCHEMA_DOCUMENT.contains("\"policy\""));
            assert!(PROOF_SCHEMA_DOCUMENT.contains("\"verification\""));
        }
    }
}

fn main() -> std::process::ExitCode {
    legacy::main_v1()
}
