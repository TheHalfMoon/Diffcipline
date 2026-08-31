use std::fs;
use std::path::{Path, PathBuf};
use std::process::{Command, Output};
use std::sync::atomic::{AtomicU64, Ordering};

static NEXT_ID: AtomicU64 = AtomicU64::new(0);

struct DemoRepo {
    root: PathBuf,
}

impl DemoRepo {
    fn new() -> Self {
        let id = NEXT_ID.fetch_add(1, Ordering::Relaxed);
        let root = std::env::temp_dir().join(format!(
            "diffcipline-quickstart-{}-{id}",
            std::process::id()
        ));
        fs::create_dir_all(root.join("src")).expect("create quickstart repository");

        git(&root, &["init", "-q"]);
        git(&root, &["config", "user.name", "Diffcipline Demo"]);
        git(
            &root,
            &["config", "user.email", "diffcipline-demo@example.invalid"],
        );

        fs::write(
            root.join("Cargo.toml"),
            "[package]\nname = \"diffcipline-demo\"\nversion = \"0.1.0\"\nedition = \"2024\"\n",
        )
        .expect("write demo manifest");
        fs::write(root.join("src/main.rs"), "fn main() {}\n").expect("write demo source");
        command(&root, "cargo", &["generate-lockfile", "-q"]);
        git(&root, &["add", "."]);
        git(&root, &["commit", "-qm", "demo base"]);

        Self { root }
    }

    fn diffcipline(&self, args: &[&str]) -> Output {
        Command::new(env!("CARGO_BIN_EXE_diffcipline"))
            .args(args)
            .current_dir(&self.root)
            .output()
            .expect("run diffcipline")
    }
}

impl Drop for DemoRepo {
    fn drop(&mut self) {
        let _ = fs::remove_dir_all(&self.root);
    }
}

fn git(root: &Path, args: &[&str]) {
    command(root, "git", args);
}

fn command(root: &Path, program: &str, args: &[&str]) {
    let output = Command::new(program)
        .args(args)
        .current_dir(root)
        .output()
        .unwrap_or_else(|error| panic!("run {program}: {error}"));
    assert!(
        output.status.success(),
        "{program} {} failed: {}",
        args.join(" "),
        String::from_utf8_lossy(&output.stderr)
    );
}

#[test]
fn readme_quickstart_reaches_a_real_pass() {
    let demo = DemoRepo::new();

    let init = demo.diffcipline(&["init"]);
    assert_eq!(init.status.code(), Some(0));
    assert!(demo.root.join(".diffcipline.toml").exists());
    let policy = fs::read_to_string(demo.root.join(".diffcipline.toml")).expect("read policy");
    assert!(policy.contains("cargo fmt --all -- --check"));
    assert!(policy.contains("cargo clippy --workspace --all-targets -- -D warnings"));
    assert!(policy.contains("cargo test --workspace --all-targets"));

    git(&demo.root, &["add", ".diffcipline.toml"]);
    git(&demo.root, &["commit", "-qm", "add diffcipline policy"]);
    fs::write(
        demo.root.join("src/main.rs"),
        "fn main() {}\n\n// Bounded demo change.\n",
    )
    .expect("write bounded demo change");

    let proof = demo.diffcipline(&["check", "--run"]);
    assert_eq!(
        proof.status.code(),
        Some(0),
        "{}\n{}",
        String::from_utf8_lossy(&proof.stdout),
        String::from_utf8_lossy(&proof.stderr)
    );
    let stdout = String::from_utf8_lossy(&proof.stdout);
    assert!(stdout.contains("Verdict       PASS"));
    assert!(stdout.contains("Verification  PASS — cargo fmt --all -- --check"));
    assert!(
        stdout
            .contains("Verification  PASS — cargo clippy --workspace --all-targets -- -D warnings")
    );
    assert!(stdout.contains("Verification  PASS — cargo test --workspace --all-targets"));
}
