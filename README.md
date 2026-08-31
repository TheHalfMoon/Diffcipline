# Diffcipline

**Discipline for coding agents.**
Smaller diffs. Fewer assumptions. Proof before done.

> Your coding agent should not be allowed to say “done” just because it wrote code.

Diffcipline is an open Agent Skill plus a deterministic CLI that gives coding agents a closed-loop engineering discipline:

**Think → Challenge → Minimize → Change → Prove**

It is inspired by the best ideas behind cautious, surgical agent behavior and minimal senior-engineer code, but it adds the missing layer: **machine-observed proof over the exact diff**.

## v1 capability milestone

The Universal Engineering Governor capability set is implemented on canonical `main`:

- stable machine proof schema `diffcipline.proof/v1` / `1.0` with deterministic policy provenance;
- explicit local enterprise-policy input with monotonic, fail-closed layering over repository policy;
- one canonical Agent Skills behavior qualified byte-identically for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI, plus the generic Agent Skills layout;
- locked Linux, macOS, and Windows release-candidate builds with deterministic `SHA256SUMS`, keyless GitHub/Sigstore provenance, and attestation-subject verification on trusted canonical pushes.

See [`docs/PROOF-CONTRACT.md`](docs/PROOF-CONTRACT.md), [`docs/INSTALLATION.md`](docs/INSTALLATION.md), and [`docs/RELEASES.md`](docs/RELEASES.md) for the machine, portability, and release-candidate contracts.

This capability milestone does **not** create or authorize a public `v1.0` tag or GitHub release.

## Why Diffcipline

Coding agents are fast at producing plausible changes. The expensive failures happen when they silently assume, over-build, touch unrelated files, add dependencies too early, or declare success without enough evidence.

Diffcipline attacks that failure mode from both sides:

- **Skill:** changes how the agent reasons before and during implementation.
- **CLI:** inspects the actual Git diff and verification evidence before allowing a clean PASS.

## The loop

### 1. Intent
Define what is actually changing. Surface only assumptions that can alter implementation.

### 2. Need
Stop at the first rung that solves the problem safely:

1. No change needed
2. Existing code or pattern
3. Standard library
4. Native platform capability
5. Already-installed dependency
6. Tiny local implementation
7. New dependency or abstraction only with evidence

### 3. Scope
Every changed file needs a reason. No drive-by cleanup. No “while I’m here” refactor.

### 4. Risk
Rigor scales with blast radius:

- **R0** — docs, formatting, trivial non-behavioral changes
- **R1** — localized behavior
- **R2** — shared contracts, persistence, concurrency, public interfaces
- **R3** — auth, security, payments, migrations, destructive operations

Minimalism never deletes safety.

### 5. Proof
Run `diffcipline check` to produce a proof card from repository facts.

```text
DIFFCIPLINE PROOF

Verdict       REVIEW
Changed       3 files
Diff          +71 / -18
Dependencies  unchanged
Lockfiles     unchanged
Verification  NOT RUN

REVIEW — verification evidence is still missing.
```

No opaque “AI quality score.” Diffcipline uses **PASS / REVIEW / FAIL** with reasons.

## Install the skill

Diffcipline follows the open Agent Skills layout. With a compatible skill installer:

```bash
npx skills add TheHalfMoon/Diffcipline
```

The repository ships two initial skills:

- `diffcipline` — implementation discipline for coding tasks
- `diffcipline-review` — scope, minimality, and proof-focused review

## CLI

The CLI is written in dependency-free Rust.

```bash
cargo install --path crates/diffcipline-cli
```

Then:

```bash
diffcipline init
diffcipline check
diffcipline check --base origin/main
diffcipline check --base origin/main --run
diffcipline check --base origin/main --risk R2 --run
diffcipline check --enterprise-policy ./enterprise.diffcipline.toml --base origin/main --risk R2 --run --json
```

`--run` executes the verification commands declared in `.diffcipline.toml`. Without `--run`, configured verification is reported as NOT RUN rather than silently treated as passing.

`--risk R0|R1|R2|R3` selects the matching repository-configured verification profile. An explicitly requested profile must exist and contain at least one command; Diffcipline fails closed instead of silently falling back to weaker verification. Omitting `--risk` preserves the default `commands` behavior.

`--enterprise-policy <path>` explicitly adds a local enterprise baseline. The repository layer may tighten that baseline but cannot weaken its limits, decisions, scope restrictions, or required verification. No network discovery, credential exchange, or remote policy service is used.

When intent contracts are configured, every changed repository-relative path is checked against `expected_files` and `forbidden_surfaces`. A path outside all expected patterns or inside a forbidden surface produces FAIL. Human and JSON proof output expose the selected risk, configured intent contract, scope violations, verification command state, and policy provenance.

## GitHub Action

Diffcipline can gate pull requests with the same CLI and repository policy. Pin the immutable `v0.1.0` release or an exact commit for production workflows; `@main` tracks current development behavior.

```yaml
permissions:
  contents: read

steps:
  - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
    with:
      fetch-depth: 0

  - uses: TheHalfMoon/Diffcipline@main
    with:
      base: ${{ github.event.pull_request.base.sha }}
      risk: R2
      run-verification: "true"
```

The optional `risk` input accepts only `R0`, `R1`, `R2`, or `R3`; leaving it empty preserves default verification behavior. The Action forwards the value to the same CLI proof contract used locally.

The Action requires explicit `run-verification: "true"` before executing commands from `.diffcipline.toml`. Treat repository policy as executable code and review it before enabling verification on untrusted changes.

The Action preserves the CLI exit status, keeps full proof output in the job log, and writes the deterministic `DIFFCIPLINE PROOF` section to `$GITHUB_STEP_SUMMARY`. It requires only `contents: read` and does not post PR comments.

A PASS exits `0`; REVIEW exits `1`; FAIL exits `2`. Missing evidence therefore fails the GitHub job instead of silently becoming green.

The repository dogfoods the default and risk-aware Action paths on Ubuntu, macOS, and Windows, including rejection of an invalid risk input.

## Policy

`diffcipline init` creates a small repository policy. Teams can extend it with intent and risk contracts:

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

Supported intent patterns are deliberately narrow: exact repository-relative paths, directory-recursive `/**` suffixes, and leading filename suffix patterns such as `*.md`. Unsupported wildcard placement fails policy parsing.

Policies are deterministic and repository-native. Teams can tighten them as risk increases.

## What Diffcipline is not

Diffcipline is not another coding agent, another chat UI, a code-golf prompt, or an excuse to remove validation. It does not reward fewer lines when those lines make the system less correct, secure, accessible, or maintainable.

## Benchmark doctrine

A Diffcipline benchmark is publishable only when it includes:

- exact tasks and repositories
- model and harness versions
- prompts/skills used by every arm
- raw outputs and diffs
- correctness and regression checks
- LOC, file count, dependency churn, tokens, cost, and time when available
- judge/scoring code
- failures and losing metrics
- limitations

See [`benchmarks/PROTOCOL.md`](benchmarks/PROTOCOL.md).

### v0.1 canonical benchmark

The canonical six-task v0.1 experiment **did not show a correctness advantage for Diffcipline**. Baseline, Karpathy, Ponytail, and Diffcipline each finished at **1/6 correct** and **1/6 scorer-pass**. All four arms changed zero files; the only correct task was the already-minimal no-op fixture.

Observed total wall-clock time was 746.668s for baseline, 797.091s for Karpathy, 702.127s for Ponytail, and **981.263s for Diffcipline**, making Diffcipline the slowest arm in this run. The small pinned 3B Q4 model/agent also exhibited provider/tool-parser failures, timeouts, and sessions that produced assistant text without repository edits, so this experiment does not support a treatment-effect inference.

Raw transcripts, scorer JSON, patches, metadata, runtime provenance, checksums, invalidated/excluded runs, and limitations are published under [`benchmarks/results/v0.1/`](benchmarks/results/v0.1/REPORT.md). Tokens and monetary cost were not available and are reported as such.

### v0.3 accepted reference benchmark

The accepted 24-row v0.3 reference experiment also **does not show a correctness advantage for Diffcipline**. Under the same pinned executor contract, baseline, Karpathy, Ponytail, and Diffcipline each finished at **1/6 task-correct**. Diffcipline had the largest summed task duration: 939.839s versus 494.365s baseline, 902.187s Karpathy, and 700.243s Ponytail.

The frozen scorer reported **0/6 scorer-pass for every treatment**, but that signal is not usable as a treatment comparison in this run: fixture verification generated `__pycache__` files, and the unchanged scorer counted those bytecode caches as changed/unrelated/protected paths. All textual patches were empty and no source-text edit was observed. The run preserved 12 failed rows—nine provider/tool-parser HTTP 500 failures and three internal agent timeouts—with no selective rerun and no hidden exclusion.

The exact accepted run, artifact identity/digest, provenance, treatment revisions, limitations, and retention boundary are published under [`benchmarks/results/v0.3/`](benchmarks/results/v0.3/REPORT.md). Tokens and monetary cost were not available. These results do not support a treatment-effect inference and do not establish behavior with a stronger executor.

## Roadmap

**v0.1 — Proof before done**
- portable Agent Skills
- dependency-free Rust CLI
- diff size and scope policy
- dependency/lockfile awareness
- deterministic verification commands
- PASS / REVIEW / FAIL proof card
- GitHub Action proof gate

**v0.2 — Intent-aware scope**
- proof contract for expected files and forbidden surfaces
- risk-aware verification profiles
- GitHub job-summary annotation

**v0.3 — Evidence benchmark**
- public multi-agent benchmark harness
- reproducible baselines against unassisted agents and other skills

**v1.0 — Universal engineering governor**
- stable proof schema
- broad agent portability
- signed release artifacts
- enterprise policy mode

## Prior art and attribution

Diffcipline is a clean-room implementation informed by ideas from the wider agent-development ecosystem. See [`ACKNOWLEDGMENTS.md`](ACKNOWLEDGMENTS.md).

## License

MIT
