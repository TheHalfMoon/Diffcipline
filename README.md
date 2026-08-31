# Diffcipline

**Deterministic finish-line proof for coding agents.**

Diffcipline combines an open Agent Skill with a dependency-free Rust CLI so a coding agent cannot turn “I changed the code” into “done” without checking the actual diff and the repository’s verification policy.

**Think → Challenge → Minimize → Change → Prove**

The public `v1.0.0` release is published and immutable. Its Linux, macOS, and Windows binaries, `SHA256SUMS`, and Sigstore provenance were built from the exact authorized release commit and machine-verified after publication.

- **Install the skills:** `npx skills add TheHalfMoon/Diffcipline`
- **Install the immutable v1 CLI:** `cargo install --git https://github.com/TheHalfMoon/Diffcipline --tag v1.0.0 diffcipline`
- **Proof contract:** [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md)
- **Release verification:** [`docs/RELEASES.md`](docs/RELEASES.md)
- **Benchmark evidence and limitations:** [`benchmarks/PROTOCOL.md`](benchmarks/PROTOCOL.md)
- **Capability-to-evidence matrix:** [`docs/EVIDENCE.md`](docs/EVIDENCE.md)
- **Agent-readable index:** [`llms.txt`](llms.txt)
- **Citation metadata:** [`CITATION.cff`](CITATION.cff)

Diffcipline does not claim universal superiority. Its public benchmark record includes negative results, failed runs, limitations, and preserved verifier failures alongside successful release evidence.

## Two-minute proof

After installing the CLI, this copy/paste demo creates a disposable Rust repository, lets Diffcipline detect verification commands, makes one bounded change, and reaches a real `PASS` only after formatting, linting, and tests execute successfully.

```bash
DEMO="$(mktemp -d)"
cd "$DEMO"
git init -q
git config user.name "Diffcipline Demo"
git config user.email "diffcipline-demo@example.invalid"
mkdir -p src
printf '[package]\nname = "diffcipline-demo"\nversion = "0.1.0"\nedition = "2024"\n' > Cargo.toml
printf 'fn main() {}\n' > src/main.rs
cargo generate-lockfile -q
git add .
git commit -qm "demo base"

diffcipline init
git add .diffcipline.toml
git commit -qm "add diffcipline policy"

printf '\n// Bounded demo change.\n' >> src/main.rs
diffcipline check --run
```

Expected final proof includes:

```text
Verdict       PASS
Verification  PASS — cargo fmt --all -- --check
Verification  PASS — cargo clippy --workspace --all-targets -- -D warnings
Verification  PASS — cargo test --workspace --all-targets
```

The repository integration suite machine-executes the same quickstart path. If verification is configured but not run, Diffcipline returns `REVIEW`; if policy or verification fails, it returns `FAIL`.

## Why Diffcipline

Coding agents are good at producing plausible changes. The expensive failures happen when they silently assume, over-build, touch unrelated files, add dependencies too early, or declare success without enough evidence.

Diffcipline attacks that failure mode from both sides:

- **Agent Skill:** shapes implementation behavior toward explicit intent, need, scope, risk, and proof.
- **Deterministic CLI:** inspects repository facts, the exact Git diff, policy boundaries, and executed verification evidence.

There is no opaque AI quality score. The contract is explicit: **PASS / REVIEW / FAIL** with machine-readable reasons.

## What is verified

| Surface | Diffcipline behavior | Evidence |
| --- | --- | --- |
| Exact diff | Counts changed files and added lines; detects manifests, lockfiles, and untracked files | [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md) |
| Intent scope | Supports expected files and forbidden surfaces | [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md) |
| Risk | Selects explicit `R0`–`R3` verification profiles and fails closed when a requested profile is absent | [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md) |
| Verification | Executes repository-declared commands only when `--run` is explicit | [`crates/diffcipline-cli/tests/`](crates/diffcipline-cli/tests/) |
| Enterprise policy | Local enterprise baseline can be tightened by repository policy but not weakened | [`docs/ENTERPRISE-POLICY.md`](docs/ENTERPRISE-POLICY.md) |
| Agent portability | One canonical skill behavior is qualified across Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Gemini CLI, and generic Agent Skills layout | [`docs/INSTALLATION.md`](docs/INSTALLATION.md) |
| Release integrity | Immutable `v1.0.0`, cross-platform binaries, checksums, Sigstore provenance, release and asset verification | [`docs/RELEASES.md`](docs/RELEASES.md) |
| Benchmark integrity | Tasks, raw outputs, scoring, failures, negative findings, and limitations remain public | [`benchmarks/PROTOCOL.md`](benchmarks/PROTOCOL.md) |

## Install

### Agent Skills

```bash
npx skills add TheHalfMoon/Diffcipline
```

The repository ships:

- `diffcipline` — implementation discipline for coding tasks;
- `diffcipline-review` — scope, minimality, and proof-focused review.

### CLI from immutable v1.0.0

```bash
cargo install --git https://github.com/TheHalfMoon/Diffcipline --tag v1.0.0 diffcipline
```

For development from a clone:

```bash
cargo install --path crates/diffcipline-cli
```

Published native binaries and verification assets are available from the immutable [`v1.0.0` release](https://github.com/TheHalfMoon/Diffcipline/releases/tag/v1.0.0).

## CLI

```bash
diffcipline init
diffcipline check
diffcipline check --base origin/main
diffcipline check --base origin/main --run
diffcipline check --base origin/main --risk R2 --run
diffcipline check --enterprise-policy ./enterprise.diffcipline.toml --base origin/main --risk R2 --run --json
```

`diffcipline init` creates `.diffcipline.toml` and detects common repository verification commands for Rust, Node, Python, and Go projects.

`--run` is explicit by design. Without it, configured verification is reported as `NOT RUN` and a clean `PASS` is impossible.

`--risk R0|R1|R2|R3` selects the matching configured profile. An explicitly requested missing or empty profile is a usage/execution error rather than a fallback to weaker checks.

`--enterprise-policy <path>` layers a local enterprise baseline under repository policy. The repository may tighten that baseline but cannot weaken it.

Exit codes:

| Code | Meaning |
| ---: | --- |
| `0` | `PASS` |
| `1` | `REVIEW` |
| `2` | `FAIL` |
| `64` | usage/execution error |

## GitHub Action

Pin the immutable `v1.0.0` tag for production workflows:

```yaml
permissions:
  contents: read

steps:
  - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
    with:
      fetch-depth: 0

  - uses: TheHalfMoon/Diffcipline@v1.0.0
    with:
      base: ${{ github.event.pull_request.base.sha }}
      risk: R2
      run-verification: "true"
```

The Action preserves the CLI exit status, writes the deterministic proof to the job summary, and requires explicit `run-verification: "true"` before executing commands from repository policy. Review repository policy before enabling verification on untrusted changes.

## Policy

A small policy can bound scope and verification:

```toml
version = 1

[policy]
max_changed_files = 12
max_added_lines = 400
dependency_manifest_changes = "review"
lockfile_changes = "review"
untracked_files = "review"
expected_files = ["crates/diffcipline-cli/**", "README.md"]
forbidden_surfaces = ["secrets/**", ".github/workflows/**"]

[verification]
commands = ["cargo test --workspace --all-targets"]
r0_commands = ["cargo fmt --all -- --check"]
r1_commands = ["cargo test --workspace --all-targets"]
r2_commands = ["cargo clippy --workspace --all-targets --locked -- -D warnings", "cargo test --workspace --all-targets --locked"]
r3_commands = ["cargo fmt --all -- --check", "cargo clippy --workspace --all-targets --locked -- -D warnings", "cargo test --workspace --all-targets --locked"]
```

Supported intent patterns are intentionally narrow: exact repository-relative paths, directory-recursive `/**` suffixes, and leading filename suffix patterns such as `*.md`. Unsupported wildcard placement fails policy parsing.

## Release integrity

`v1.0.0` is fixed at release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

The release contains exactly five assets:

1. `diffcipline-aarch64-apple-darwin`
2. `diffcipline-x86_64-pc-windows-msvc.exe`
3. `diffcipline-x86_64-unknown-linux-gnu`
4. `SHA256SUMS`
5. `PROVENANCE.sigstore.json`

GitHub reports the release as immutable. Repository verification checks the fixed tag lineage, release attestation, exact asset closure, checksums, native-binary attestations, and every published asset. The complete publication protocol and recovery history are preserved under [`specs/006-v1-publication/`](specs/006-v1-publication/).

## Benchmark truth

Diffcipline publishes negative evidence instead of hiding it.

### v0.1 canonical benchmark

The six-task v0.1 experiment did **not** show a correctness advantage for Diffcipline. Baseline, Karpathy, Ponytail, and Diffcipline each finished at `1/6` correct and `1/6` scorer-pass. The small pinned 3B Q4 model/agent also exhibited provider/tool-parser failures, timeouts, and sessions that produced text without repository edits.

Full evidence: [`benchmarks/results/v0.1/REPORT.md`](benchmarks/results/v0.1/REPORT.md).

### v0.3 accepted reference benchmark

The accepted 24-row v0.3 experiment also did **not** show a correctness advantage for Diffcipline. All four treatments finished at `1/6` task-correct. The scorer-pass signal was confounded by generated `__pycache__` files, and the run preserved provider/tool-parser failures and timeouts without selective reruns.

Full evidence: [`benchmarks/results/v0.3/REPORT.md`](benchmarks/results/v0.3/REPORT.md).

These experiments do not establish a treatment effect. A stronger future evaluation must be separately preregistered and must publish losses as prominently as wins.

## What Diffcipline is not

Diffcipline is not another coding agent, another chat UI, a benchmark-marketing wrapper, or an excuse to trade safety for smaller diffs. It does not reward fewer lines when those lines make the system less correct, secure, accessible, or maintainable.

## Project principles

- proof before done;
- repository truth over narrative;
- minimality subordinate to correctness;
- stronger rigor for higher risk;
- open, reproducible claims;
- portable Agent Skills core;
- dependency restraint.

See [`CONSTITUTION.md`](CONSTITUTION.md) and [`AGENTS.md`](AGENTS.md).

## Prior art and attribution

Diffcipline is a clean-room implementation informed by ideas from the wider agent-development ecosystem. See [`ACKNOWLEDGMENTS.md`](ACKNOWLEDGMENTS.md).

## License

MIT
