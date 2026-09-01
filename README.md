<div align="center">

# Diffcipline

### Make coding agents prove they're done.

**A proof-before-done layer for coding agents: Agent Skills + a dependency-free Rust CLI + a GitHub Action.**

[![CI](https://github.com/TheHalfMoon/Diffcipline/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/TheHalfMoon/Diffcipline/actions/workflows/ci.yml)
[![Release](https://img.shields.io/badge/release-v1.0.0-2ea44f)](https://github.com/TheHalfMoon/Diffcipline/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Rust](https://img.shields.io/badge/CLI-Rust-dea584)](crates/diffcipline-cli)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-portable-7c3aed)](docs/INSTALLATION.md)

**Think → Challenge → Minimize → Change → Prove**

[Quick start](#quick-start) · [How it works](#how-it-works) · [GitHub Action](#github-action) · [Policy](#policy) · [Evidence](#evidence-not-marketing) · [Contributing](CONTRIBUTING.md)

</div>

---

Coding agents can produce plausible changes quickly. The expensive part is knowing whether the change is actually in scope, appropriately verified, and safe to call complete.

Diffcipline makes that finish line explicit. It combines:

- **Agent Skills** that push implementation toward intent, scope, risk, and proof;
- a **dependency-free Rust CLI** that inspects repository facts, the exact Git diff, policy boundaries, and executed verification evidence;
- a **GitHub Action** that applies the same deterministic contract in CI.

There is no opaque AI quality score. Diffcipline returns an explainable **`PASS` / `REVIEW` / `FAIL`** verdict with machine-readable reasons.

> **Proof before done.** If a required check did not run successfully against the exact change, Diffcipline does not call it `PASS`.

## Quick start

### 1. Add the Agent Skills

```bash
npx skills add TheHalfMoon/Diffcipline
```

The repository ships two skills:

- `diffcipline` — implementation discipline for coding tasks;
- `diffcipline-review` — scope, minimality, and proof-focused review.

### 2. Install the immutable v1 CLI

```bash
cargo install --git https://github.com/TheHalfMoon/Diffcipline --tag v1.0.0 diffcipline
```

### 3. Initialize policy and prove a change

```bash
diffcipline init
diffcipline check --base origin/main --run
```

A successful proof ends with machine-observed verification, for example:

```text
Verdict       PASS
Verification  PASS — cargo fmt --all -- --check
Verification  PASS — cargo clippy --workspace --all-targets -- -D warnings
Verification  PASS — cargo test --workspace --all-targets
```

If verification is configured but not run, Diffcipline returns `REVIEW`. If policy or verification fails, it returns `FAIL`.

## Pick the integration you need

| Goal | Use | Start here |
| --- | --- | --- |
| Improve coding-agent behavior | Agent Skills | `npx skills add TheHalfMoon/Diffcipline` |
| Prove a local change | Rust CLI | `diffcipline check --base origin/main --run` |
| Enforce proof in pull requests | GitHub Action | [Action example](#github-action) |
| Integrate with tooling | JSON output | `diffcipline check --run --json` |
| Adopt incrementally | Policy examples | [`examples/README.md`](examples/README.md) |
| Validate independently | Reproduction protocol | [`docs/INDEPENDENT-VALIDATION.md`](docs/INDEPENDENT-VALIDATION.md) |

`diffcipline init` detects common verification commands for **Rust, Node, Python, and Go** repositories.

## How it works

Diffcipline checks the parts coding agents most often hand-wave at the finish line:

| Surface | What Diffcipline verifies |
| --- | --- |
| **Exact diff** | Changed files, added lines, manifests, lockfiles, and untracked files |
| **Intent scope** | Expected files and forbidden surfaces |
| **Risk** | Explicit `R0`–`R3` verification profiles; requested missing profiles fail closed |
| **Verification** | Repository-declared commands execute only when `--run` is explicit |
| **Enterprise policy** | Repository policy may tighten a local baseline but cannot weaken it |
| **Agent portability** | One canonical skill behavior across supported Agent Skills layouts |
| **Release integrity** | Immutable release, native binaries, checksums, and Sigstore provenance |

The full behavioral contract lives in [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md).

### The finish-line rule

Without `--run`, configured verification remains `NOT RUN` by design. A clean `PASS` is impossible until the required commands actually execute successfully.

```bash
# Inspect only: verification remains NOT RUN.
diffcipline check --base origin/main

# Execute repository-declared verification.
diffcipline check --base origin/main --run

# Require a risk profile.
diffcipline check --base origin/main --risk R2 --run

# Emit deterministic machine-readable output.
diffcipline check --base origin/main --risk R2 --run --json
```

Exit codes are stable and automation-friendly:

| Code | Meaning |
| ---: | --- |
| `0` | `PASS` |
| `1` | `REVIEW` |
| `2` | `FAIL` |
| `64` | usage/execution error |

## GitHub Action

Pin the immutable `v1.0.0` tag in production workflows:

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

The Action preserves the CLI exit status and writes the deterministic proof to the job summary. Verification is opt-in: `run-verification: "true"` is required before commands from repository policy execute. Review policy before enabling verification on untrusted changes.

## Policy

A small `.diffcipline.toml` can bound scope and verification:

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

More examples: [`examples/README.md`](examples/README.md) · [`docs/ADOPTION.md`](docs/ADOPTION.md) · [`docs/ENTERPRISE-POLICY.md`](docs/ENTERPRISE-POLICY.md)

## Portable across coding-agent workflows

The canonical skill behavior is qualified across **Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, Gemini CLI, and generic Agent Skills layout**. Platform adapters improve ergonomics without becoming the only way to use the core behavior.

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) and the compatibility evidence referenced there.

## Release integrity

Public `v1.0.0` is fixed at release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96` and GitHub reports the release as immutable.

Published assets include native Linux, macOS, and Windows binaries plus `SHA256SUMS` and Sigstore provenance. Repository verification checks tag lineage, release attestation, exact asset closure, checksums, native-binary attestations, and published assets.

- [Download / inspect `v1.0.0`](https://github.com/TheHalfMoon/Diffcipline/releases/tag/v1.0.0)
- [Release verification protocol](docs/RELEASES.md)
- [Capability-to-evidence matrix](docs/EVIDENCE.md)

## Evidence, not marketing

Diffcipline deliberately publishes negative evidence.

Its accepted v0.1 and v0.3 reference experiments **did not establish a correctness advantage** for Diffcipline. Failures, timeouts, tool-parser problems, scorer limitations, and losing results remain preserved rather than being selectively removed or rerun.

That is part of the product philosophy: evidence should constrain claims, not decorate them.

- [`benchmarks/results/v0.1/REPORT.md`](benchmarks/results/v0.1/REPORT.md)
- [`benchmarks/results/v0.3/REPORT.md`](benchmarks/results/v0.3/REPORT.md)
- [`benchmarks/PROTOCOL.md`](benchmarks/PROTOCOL.md)

Diffcipline does **not** claim universal superiority. A stronger comparative claim requires a separately preregistered, reproducible evaluation.

## What Diffcipline is not

Diffcipline is not another coding agent, another chat UI, or a benchmark-marketing wrapper. It does not reward smaller diffs when those diffs make a system less correct, secure, accessible, compatible, or maintainable.

It is a **discipline layer around the moment an agent says “done.”**

## For maintainers and contributors

Contributions are welcome when they make Diffcipline more correct, portable, verifiable, or simpler without weakening safety.

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and exact-head proof expectations
- [`SECURITY.md`](SECURITY.md) — private vulnerability reporting
- [`CONSTITUTION.md`](CONSTITUTION.md) — project principles
- [`AGENTS.md`](AGENTS.md) — repository engineering rules
- [`llms.txt`](llms.txt) — agent-readable repository index
- [`CITATION.cff`](CITATION.cff) — citation metadata

## Project principles

**Proof before done · Repository truth over narrative · Minimality subordinate to correctness · Stronger rigor for higher risk · Open reproducible claims · Portable Agent Skills core · Dependency restraint**

## Prior art and attribution

Diffcipline is a clean-room implementation informed by ideas from the wider agent-development ecosystem. See [`ACKNOWLEDGMENTS.md`](ACKNOWLEDGMENTS.md).

## License

[MIT](LICENSE)
