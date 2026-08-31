use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_ID: AtomicU64 = AtomicU64::new(0);

struct Fixture {
    root: PathBuf,
}

impl Fixture {
    fn new(enterprise: &str, repository_expected: &str) -> Self {
        let id = NEXT_ID.fetch_add(1, Ordering::Relaxed);
        let root = std::env::temp_dir().join(format!(
            "diffcipline-enterprise-{}-{id}",
            std::process::id()
        ));
        fs::create_dir_all(&root).unwrap();
        git(&root, &["init"]);
        git(&root, &["config", "user.name", "Diffcipline Test"]);
        git(
            &root,
            &["config", "user.email", "diffcipline-test@example.invalid"],
        );
        fs::write(root.join("tracked.txt"), "before\n").unwrap();
        fs::write(root.join("package.json"), "{}\n").unwrap();
        fs::write(
            root.join(".diffcipline.toml"),
            format!(
                "version = 1\n[policy]\nmax_changed_files = 4\nmax_added_lines = 20\n\
dependency_manifest_changes = \"allow\"\nlockfile_changes = \"allow\"\nuntracked_files = \"allow\"\n{repository_expected}\n\
[verification]\ncommands = [\"git diff --check\"]\n"
            ),
        )
        .unwrap();
        fs::write(root.join("enterprise.toml"), enterprise).unwrap();
        git(&root, &["add", "."]);
        git(&root, &["commit", "-m", "fixture base"]);
        fs::write(root.join("tracked.txt"), "after\n").unwrap();
        Self { root }
    }

    fn run(&self, args: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_diffcipline"))
            .args(args)
            .current_dir(&self.root)
            .output()
            .unwrap()
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
        .unwrap();
    assert!(
        output.status.success(),
        "{}",
        String::from_utf8_lossy(&output.stderr)
    );
}

fn enterprise(max_files: usize, expected: &str) -> String {
    format!(
        "version = 1\n[policy]\nmax_changed_files = {max_files}\nmax_added_lines = 20\n\
dependency_manifest_changes = \"fail\"\nlockfile_changes = \"allow\"\nuntracked_files = \"allow\"\n{expected}\n\
[verification]\ncommands = [\"git status --short\"]\n"
    )
}

#[test]
fn enterprise_mode_is_explicit_cumulative_and_provenanced() {
    let fixture = Fixture::new(
        &enterprise(4, "expected_files = [\"tracked.txt\"]"),
        "expected_files = [\"*.txt\"]",
    );
    let output = fixture.run(&[
        "check",
        "--enterprise-policy",
        "enterprise.toml",
        "--run",
        "--json",
    ]);
    assert_eq!(output.status.code(), Some(0));
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("\"policy\":{\"mode\":\"enterprise\",\"sources\":[\"enterprise.toml\",\".diffcipline.toml\"]}"));
    assert!(stdout.contains("\"command\":\"git status --short\",\"state\":\"PASS\""));
    assert!(stdout.contains("\"command\":\"git diff --check\",\"state\":\"PASS\""));
}

#[test]
fn enterprise_hardening_cannot_be_weakened_by_repository() {
    let fixture = Fixture::new(&enterprise(0, "expected_files = [\"src/**\"]"), "");
    fs::write(fixture.root.join("package.json"), "{\"changed\":true}\n").unwrap();
    let output = fixture.run(&["check", "--enterprise-policy", "enterprise.toml", "--run"]);
    assert_eq!(output.status.code(), Some(2));
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("exceed maximum 0"));
    assert!(stdout.contains("dependency manifest changed: package.json"));
    assert!(stdout.contains("enterprise expected-files contract rejected: tracked.txt"));
}

#[test]
fn missing_or_unsupported_enterprise_policy_fails_closed() {
    let fixture = Fixture::new(&enterprise(4, ""), "");
    let missing = fixture.run(&["check", "--enterprise-policy", "missing.toml"]);
    assert_eq!(missing.status.code(), Some(64));
    fs::write(fixture.root.join("enterprise.toml"), "version = 2\n").unwrap();
    let unsupported = fixture.run(&["check", "--enterprise-policy", "enterprise.toml"]);
    assert!(String::from_utf8_lossy(&unsupported.stderr).contains("unsupported policy version"));
}
