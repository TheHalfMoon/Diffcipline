# Diffcipline

**Discipline for coding agents.**
Smaller diffs. Fewer assumptions. Proof before done.

> Your coding agent should not be allowed to say “done” just because it wrote code.

Diffcipline is an open Agent Skill plus a deterministic CLI that gives coding agents a closed-loop engineering discipline:

**Think → Challenge → Minimize → Change → Prove**

It is inspired by the best ideas behind cautious, surgical agent behavior and minimal senior-engineer code, but it adds the missing layer: **machine-observed proof over the exact diff**.

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
```

`--run` executes the verification commands declared in `.diffcipline.toml`. Without `--run`, configured verification is reported as NOT RUN rather than silently treated as passing.

## GitHub Action

Diffcipline can gate pull requests using the same CLI and repository policy. Until a tagged release exists, `@main` is suitable for evaluation; pin a release or exact commit for production workflows.

```yaml
permissions:
  contents: read

steps:
  - uses: actions/checkout@v7
    with:
      fetch-depth: 0

  - uses: TheHalfMoon/Diffcipline@main
    with:
      base: ${{ github.event.pull_request.base.sha }}
      run-verification: "true"
```

The Action intentionally requires explicit `run-verification: "true"` before executing commands from `.diffcipline.toml`. Treat repository policy as executable code and review it before enabling this on untrusted changes.

A PASS exits `0`; REVIEW exits `1`; FAIL exits `2`. That makes incomplete evidence fail the GitHub job rather than silently becoming green.

## Policy

`diffcipline init` creates a small repository policy:

```toml
version = 1

[policy]
max_changed_files = 12
max_added_lines = 400
dependency_manifest_changes = "review"
lockfile_changes = "review"
untracked_files = "review"

[verification]
commands = ["cargo test --workspace --all-targets"]
```

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
- GitHub PR annotation

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
