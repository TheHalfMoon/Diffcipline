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

Verification evidence for T028–T032: GitHub Actions `ci` run #4 on commit `fbbd42637c58a72f7fd3e9d928eec299b94227b5` completed successfully with `cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets -- -D warnings`, and `cargo test --workspace --all-targets` all green.

## Phase D — Distribution

- [x] T040 Create public `TheHalfMoon/Diffcipline` GitHub repository.
- [x] T041 Push verified baseline through a feature branch and PR.
- [x] T042 Add GitHub Action after CLI contract is verified.
- [x] T043 Add release workflow and signed/checksummed binaries.
- [x] T044 Verify installation through compatible Agent Skills installers.

Verification evidence for T042: run #11 established the initial cross-platform Action behavior on `a12089f8eb01a5e54d9ae786509ffe8db75dc443`; run #12 then exposed a macOS fixture-directory collision and T042 was reopened. Commit `db80d1801e6a650c599c05f3a76e80d4d0359e86` replaced clock-derived fixture names with process-local atomic IDs. Run #13 passed the repaired implementation on Ubuntu, macOS, and Windows, and final ledger head `7029021a3066bd26ff30c67c3fc4a6e95b92a801` passed all six jobs in `ci` run #14 before PR #4 merged.

Verification evidence for T043: PR #5 head `518200a6cd639d7fd9db994eebd84507a71b950d` passed normal `ci` run #16 and release workflow run #1. Release run #1 built and smoke-tested host-native Linux, macOS, and Windows binaries and generated a verified three-subject `SHA256SUMS`; signing and publishing were intentionally unavailable on the pull request. After merge, canonical `main` commit `4348b40049d64f5b5eb5dbe060953caa3c90fdc4` passed `ci` run #17 and trusted release run #2. Run #2 created build provenance for all three binary subjects with `actions/attest`, signed it with the Public Good Sigstore instance, uploaded it to the Rekor transparency log and GitHub Attestations (attestation `43657557`), verified every subject with `gh attestation verify`, preserved `PROVENANCE.sigstore.json`, and uploaded signed-release-candidate artifact `9686520987`. Tag publication remains NOT RUN because no release tag has been created; the workflow will publish only a matching `v<crate version>` tag.

Verification evidence for T044: PR #7 exact head `e15f84e3241e487cbe2c4df3e03dcbf4b7680adb` passed `skills-compat` run #1 and normal `ci` run #20. The pinned `skills@1.5.23` installer discovered and installed both Diffcipline skills successfully for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI from the exact local candidate head. After squash merge, canonical `main` commit `2e56990d3e4f31d48e57ab7f0ac01e31cf21d988` passed `skills-compat` run #2 with all six jobs installing from public GitHub shorthand `TheHalfMoon/Diffcipline`; post-merge `ci` run #21 also passed on Ubuntu, macOS, and Windows.

## Phase E — Benchmark

- [x] T050 Publish benchmark protocol before claims.
- [x] T051 Build public task fixtures.
- [ ] T052 Run unassisted-agent baseline.
- [ ] T053 Run comparison skill baselines under matching conditions.
- [ ] T054 Run Diffcipline arm.
- [ ] T055 Publish raw outputs, scorer, limitations, and results.

Verification evidence for T051: the six frozen task fixtures landed without any model execution through PRs #9–#11. The first all-at-once candidate was rejected by Diffcipline because it exceeded repository change-size policy, so the corpus was split with forward commits rather than weakening the policy. PR #12 exact head `8606c8dabbdf1f20becbdfc365eff988933fb3e5` added only the fixture validator, isolated preparer, scorer, and benchmark CI without modifying fixture bytes. `benchmark-fixtures` run #2 passed all six manifest/initial-state checks and the no-op scorer smoke contract, while normal `ci` run #31 passed Rust and Diffcipline gates on Ubuntu, macOS, and Windows. After squash merge, canonical `main` commit `4f796058bddd840be31d3fbf7d74b34a5403c49c` passed post-merge `benchmark-fixtures` run #3 and `ci` run #32; Rust fmt, clippy with warnings denied, and full locked tests passed on Ubuntu, macOS, and Windows. T052–T054 had not run before this frozen canonical revision.

### T052 current execution gate

Status: `BLOCKED_HOSTED_MODEL_ENTITLEMENT`.

The benchmark harness and runtime pinning were added through PR #14 and subsequent infrastructure-only repairs. No benchmark task has executed yet.

Excluded infrastructure preflights:

- `benchmark-arms` run #1 (`33177348082`) on canonical `f5f17b9d0fa025bbed436075c462ce48a5766151`: `gpt-5.3-codex` was unavailable; baseline, Karpathy, Ponytail, and Diffcipline all skipped.
- `benchmark-arms` run #2 (`33177729891`) on canonical `d20f6b615fc9c1285b01b74377aa6e53e7fa081a`: `claude-sonnet-4.6` was unavailable; all arms skipped.
- `benchmark-arms` run #3 (`33178142084`) on canonical `c71d3f81016ae6bc1d8516b47d1b3c5cb7258e45`: the predeclared nine-model explicit list was exhausted and every model was unavailable; all arms skipped.

Run #3 independently proved `CopilotRequests: write`, the frozen corpus, Copilot CLI `v1.0.81` checksum, and all pinned treatment skill blobs before model resolution failed. `auto` selection remains forbidden. Current valid benchmark task execution count: **0**.

T052 may proceed only after all of these pre-task gates are satisfied:

- [ ] Establish one pinned local reproducible inference runtime inside GitHub Actions.
- [ ] Pin exact runtime release/image plus checksum or digest.
- [ ] Select one exact open-weight coding-capable model before observing any benchmark task outcome.
- [ ] Record exact model artifact identity and digest where the distribution format permits it.
- [ ] Verify model/runtime license permits public reproducible benchmark evidence.
- [ ] Verify GitHub-hosted runner resource feasibility.
- [ ] Prove the required model/tool interface with a harmless preflight.
- [ ] Preserve selected runtime/model provenance for every downstream arm.
- [ ] Keep frozen fixtures, prompts, scorer/preparer, treatment blobs, timeout/tool/network policy, and runner class matched across arms.
- [ ] Pass exact-head repository CI and benchmark-infrastructure validation before the migration PR merges.
- [ ] Start benchmark tasks only from canonical `main` after that merge.

Then execute without skipping order:

- [ ] T052 baseline: six frozen tasks, no treatment skill.
- [ ] Validate six complete baseline result bundles before comparisons.
- [ ] T053 Karpathy: six frozen tasks under identical conditions with pinned Karpathy treatment blob.
- [ ] T053 Ponytail: six frozen tasks under identical conditions with pinned Ponytail treatment blob.
- [ ] Validate both comparison bundles before Diffcipline.
- [ ] T054 Diffcipline: six frozen tasks under identical conditions with pinned Diffcipline treatment blob.
- [ ] T055 commit durable results/manifest/checksums or publish oversized raw artifacts as immutable release assets referenced from the repository.
- [ ] T055 include raw transcripts where permitted, patches, test outputs, scorer JSON, aggregate tables, observed token/cost/time metrics or explicit `NOT AVAILABLE`, excluded runs #1–#3, limitations, and losing metrics.

Detailed execution and stop conditions: [`execution-frontier.md`](execution-frontier.md).

## Phase F — v0.1 canonical closeout

These gates are intentionally after T055.

- [ ] T060 Update README with only benchmark claims supported by canonical published evidence.
- [ ] T061 Update CHANGELOG and final Spec 001 ledger/status.
- [ ] T062 Pass all required canonical Rust, Diffcipline, skills compatibility, benchmark-evidence, and release-candidate gates on the exact release commit.
- [ ] T063 Create `v0.1.0` tag only from that exact verified canonical `main` commit with matching crate version.
- [ ] T064 Verify tag-triggered binaries, SHA-256 manifest, signatures/provenance/attestations, and published release assets.
- [ ] T065 Mark Spec 001 / v0.1 `COMPLETE_CANONICAL` only after post-tag evidence is recorded in the repository.
