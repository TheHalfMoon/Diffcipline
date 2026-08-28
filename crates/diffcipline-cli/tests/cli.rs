use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_FIXTURE_ID: AtomicU64 = AtomicU64::new(0);

struct Fixture {
    root: PathBuf,
}

impl Fixture {
    fn new(max_changed_files: usize) -> Self {
        let unique = NEXT_FIXTURE_ID.fetch_add(1, Ordering::Relaxed);
        let root = std::env::temp_dir().join(format!(
            "diffcipline-fixture-{}-{unique}",
            std::process::id()
        ));
        fs::create_dir_all(&root).expect("create fixture repository");

        git(&root, &["init"]);
        git(&root, &["config", "user.name", "Diffcipline Test"]);
        git(
            &root,
            &["config", "user.email", "diffcipline-test@example.invalid"],
        );

        fs::write(root.join("tracked.txt"), "before\n").expect("write fixture file");
        git(&root, &["add", "tracked.txt"]);
        git(&root, &["commit", "-m", "fixture base"]);

        fs::write(
            root.join(".diffcipline.toml"),
            format!(
                "version = 1\n\n[policy]\nmax_changed_files = {max_changed_files}\n\
max_added_lines = 20\ndependency_manifest_changes = \"allow\"\n\
lockfile_changes = \"allow\"\nuntracked_files = \"allow\"\n\n\
[verification]\ncommands = [\"git diff --check\"]\n"
            ),
        )
        .expect("write fixture policy");
        git(&root, &["add", ".diffcipline.toml"]);
        git(&root, &["commit", "-m", "add policy"]);

        fs::write(root.join("tracked.txt"), "after\n").expect("modify fixture file");

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
fn pass_requires_executed_verification() {
    let fixture = Fixture::new(4);
    let output = fixture.run(&["check", "--run"]);

    assert_eq!(output.status.code(), Some(0));
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("Verdict       PASS"));
    assert!(stdout.contains("Verification  PASS — git diff --check"));
}

#[test]
fn not_run_verification_requires_review() {
    let fixture = Fixture::new(4);
    let output = fixture.run(&["check"]);

    assert_eq!(output.status.code(), Some(1));
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("Verdict       REVIEW"));
    assert!(stdout.contains("Verification  NOT RUN — git diff --check"));
}

#[test]
fn hard_policy_violation_fails_even_when_verification_passes() {
    let fixture = Fixture::new(0);
    let output = fixture.run(&["check", "--run"]);

    assert_eq!(output.status.code(), Some(2));
    let stdout = String::from_utf8_lossy(&output.stdout);
    assert!(stdout.contains("Verdict       FAIL"));
    assert!(stdout.contains("changed files 1 exceed maximum 0"));
    assert!(stdout.contains("Verification  PASS — git diff --check"));
}
