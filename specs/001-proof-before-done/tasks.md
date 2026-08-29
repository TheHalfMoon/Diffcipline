# Tasks — 001 Proof Before Done

## Phase A — Repository foundation

- [x] T001 Create product README and positioning.
- [x] T002 Add constitution and repository instructions.
- [x] T003 Add clean-room acknowledgments and MIT license.
- [x] T004 Add security and contribution policies.

## Phase B — Portable behavioral skills

- [x] T010 Add `diffcipline` skill.
- [x] T011 Add `diffcipline-review` skill.
- [x] T012 Document risk model and proof contract.

## Phase C — CLI v0.1 implementation

- [x] T020 Create dependency-free Rust workspace.
- [x] T021 Implement `diffcipline init`.
- [x] T022 Implement Git diff/stat collection.
- [x] T023 Implement dependency/lockfile/untracked policy checks.
- [x] T024 Implement explicit verification execution with `--run`.
- [x] T025 Implement human proof card.
- [x] T026 Implement JSON output.
- [x] T027 Add unit tests for parser/classification/verdict helpers.
- [x] T028 Compile with stable Rust.
- [x] T029 Pass rustfmt.
- [x] T030 Pass clippy with warnings denied.
- [x] T031 Pass unit tests.
- [x] T032 Add fixture-repository integration tests for PASS/REVIEW/FAIL.

Verification evidence for T028–T032: GitHub Actions `ci` run #4 on commit `fbbd42637c58a72f7fd3e9d928eec299b94227b5` completed successfully with format, clippy, and tests green.

## Phase D — Distribution

- [x] T040 Create public `TheHalfMoon/Diffcipline` GitHub repository.
- [x] T041 Push verified baseline through a feature branch and PR.
- [x] T042 Add GitHub Action after CLI contract is verified.
- [x] T043 Add release workflow and signed/checksummed binaries.
- [x] T044 Verify installation through compatible Agent Skills installers.

T042 repair and exact-head cross-platform evidence closed through PR #4. T043 release-candidate build/checksum/Sigstore evidence closed through PR #5 and canonical release run #2. T044 installer compatibility closed through PR #7 and canonical `skills-compat` run #2 for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI.

## Phase E — Benchmark

- [x] T050 Publish benchmark protocol before claims.
- [x] T051 Build public task fixtures.
- [x] T052 Run unassisted-agent baseline.
- [x] T053 Run comparison skill baselines under matching conditions.
- [x] T054 Run Diffcipline arm.
- [x] T055 Publish raw outputs, scorer, limitations, and results.

### Frozen and repaired boundary

The original six-task corpus/scorer/preparer boundary was frozen at `4f796058bddd840be31d3fbf7d74b34a5403c49c`. Canonical run #25 later exposed a preparer defect: fixture commits used unpinned timestamps, yielding different ephemeral base commit SHAs across arms. PR #23 repaired only that defect, added deterministic-revision regression checks, invalidated run #25 as comparative evidence, and established the repaired boundary:

`cde4d0058ce522ddd9863457c29560679fac53dd`

### T052–T054 canonical execution

Valid whole-experiment restart:

- workflow: `benchmark-arms` #27
- run: `33200332207`
- repository revision: `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`
- model: `diffcipline-llama3.2-3b-q4km`
- arm order: baseline → Karpathy → Ponytail → Diffcipline
- six matched tasks per arm
- one identical fixture base commit per task across all four arms
- no individual task retries

Observed aggregate outcome:

| Arm | Correct | Scorer pass | Changed files | Total seconds | Clean agent exits |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 | 4/6 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 | 4/6 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 | 1/6 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 | 3/6 |

The result does not show a correctness advantage for Diffcipline. Diffcipline was the slowest arm by observed total wall-clock time. The tested local 3B Q4 model/agent showed provider/tool-parser errors, timeouts, max-step exhaustion, and assistant output without repository edits, so the six-task result does not support a treatment-effect inference.

### T055 durable publication

PR #24 published canonical evidence and was squash-merged to `main` as:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

Published under `benchmarks/results/v0.1/`:

- `REPORT.md`
- `MANIFEST.json`
- `SHA256SUMS`
- `raw-canonical-evidence.tar.gz`

The durable archive contains all 24 canonical transcripts, stdout/stderr, scorer JSON, metadata, patches, status files, arm summaries, runtime provenance, accepted preflight evidence, matched-base audit, and the excluded/invalidated-run ledger. The publication records tokens and monetary cost as `NOT AVAILABLE` rather than inventing values and preserves losing metrics.

## Phase F — v0.1 canonical closeout

These gates are intentionally after T055.

- [x] T060 Update README with only benchmark claims supported by canonical published evidence.
- [x] T061 Update CHANGELOG and final Spec 001 ledger/status.
- [ ] T062 Pass all required canonical Rust, Diffcipline, skills compatibility, benchmark-evidence, and release-candidate gates on the exact release commit.
- [ ] T063 Create `v0.1.0` tag only from that exact verified canonical `main` commit with matching crate version.
- [ ] T064 Verify tag-triggered binaries, SHA-256 manifest, signatures/provenance/attestations, and published release assets.
- [ ] T065 Mark Spec 001 / v0.1 `COMPLETE_CANONICAL` only after post-tag evidence is recorded in the repository.

T062 release-candidate validation must include exact-head Rust and Diffcipline CI, all six Agent Skills installer targets, canonical benchmark archive/manifest verification, cross-platform locked release builds, and post-merge signed provenance before T063 is authorized.
