use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_FIXTURE_ID: AtomicU64 = AtomicU64::new(0);

const RUST_POLICY: &str = include_str!("../../../examples/policies/rust.toml");
const NODE_POLICY: &str = include_str!("../../../examples/policies/node.toml");
const PYTHON_POLICY: &str = include_str!("../../../examples/policies/python.toml");
const GO_POLICY: &str = include_str!("../../../examples/policies/go.toml");

const RUST_COMMANDS: &[&str] = &[
    "cargo fmt --all -- --check",
    "cargo clippy --workspace --all-targets --locked -- -D warnings",
    "cargo test --workspace --all-targets --locked",
];
const NODE_COMMANDS: &[&str] = &["npm test"];
const PYTHON_COMMANDS: &[&str] = &["python -m pytest"];
const GO_COMMANDS: &[&str] = &["go test ./..."];

struct Fixture {
    root: PathBuf,
}

impl Fixture {
    fn new(name: &str, policy: &str) -> Self {
        let unique = NEXT_FIXTURE_ID.fetch_add(1, Ordering::Relaxed);
        let root = std::env::temp_dir().join(format!(
            "diffcipline-policy-example-{name}-{}-{unique}",
            std::process::id()
        ));
        fs::create_dir_all(&root).expect("create example fixture");

        git(&root, &["init"]);
        git(&root, &["config", "user.name", "Diffcipline Test"]);
        git(
            &root,
            &["config", "user.email", "diffcipline-test@example.invalid"],
        );

        fs::write(root.join("tracked.txt"), "before\n").expect("write tracked file");
        git(&root, &["add", "tracked.txt"]);
        git(&root, &["commit", "-m", "fixture base"]);

        fs::write(root.join(".diffcipline.toml"), policy).expect("write published policy");
        git(&root, &["add", ".diffcipline.toml"]);
        git(&root, &["commit", "-m", "add published policy"]);

        fs::write(root.join("tracked.txt"), "after\n").expect("modify tracked file");

        Self { root }
    }

    fn run(&self, args: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_diffcipline"))
            .args(args)
            .current_dir(&self.root)
            .output()
            .expect("run diffcipline")
    }
}

impl Drop for Fixture {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.root);
    }
}

fn git(root: &Path, args: &[&str]) {
    let output = Command::new("git")
        .args(args)
        .current_dir(root)
        .output()
        .expect("run git");
    assert!(
        output.status.success(),
        "git {} failed: {}",
        args.join(" "),
        String::from_utf8_lossy(&output.stderr)
    );
}

#[test]
fn published_policy_examples_are_accepted_by_the_cli_contract() {
    let examples = [
        ("rust", RUST_POLICY, RUST_COMMANDS),
        ("node", NODE_POLICY, NODE_COMMANDS),
        ("python", PYTHON_POLICY, PYTHON_COMMANDS),
        ("go", GO_POLICY, GO_COMMANDS),
    ];

    for (name, policy, expected_commands) in examples {
        let fixture = Fixture::new(name, policy);
        let output = fixture.run(&["check", "--json"]);

        assert_eq!(
            output.status.code(),
            Some(1),
            "{name} example should require REVIEW when verification is not run: {}",
            String::from_utf8_lossy(&output.stderr)
        );

        let stdout = String::from_utf8_lossy(&output.stdout);
        assert!(
            stdout.contains("\"schema\":\"diffcipline.proof/v1\""),
            "{name} example did not produce proof-v1 JSON: {stdout}"
        );
        assert!(
            stdout.contains("\"policy\":{\"mode\":\"repository\",\"sources\":[\".diffcipline.toml\"]}"),
            "{name} example did not load as repository policy: {stdout}"
        );
        assert!(
            stdout.contains("\"verdict\":\"REVIEW\""),
            "{name} example should be REVIEW without --run: {stdout}"
        );

        for command in expected_commands {
            let expected = format!("\"command\":\"{command}\",\"state\":\"NOT RUN\"");
            assert!(
                stdout.contains(&expected),
                "{name} example did not expose expected command {command}: {stdout}"
            );
        }
    }
}
