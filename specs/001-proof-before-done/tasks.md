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
- [ ] T042 Add GitHub Action after CLI contract is verified.
- [ ] T043 Add release workflow and signed/checksummed binaries.
- [ ] T044 Verify installation through compatible Agent Skills installers.

T042 implementation evidence: GitHub Actions `ci` run #11 on commit `a12089f8eb01a5e54d9ae786509ffe8db75dc443` completed successfully with the normal Rust suite and the `Diffcipline proof gate` itself green on Ubuntu, macOS, and Windows. T042 was reopened after run #12 exposed a macOS fixture-directory collision in the existing integration tests; completion now requires the collision fix and a new exact-head all-platform PASS.

## Phase E — Benchmark

- [x] T050 Publish benchmark protocol before claims.
- [ ] T051 Build public task fixtures.
- [ ] T052 Run unassisted-agent baseline.
- [ ] T053 Run comparison skill baselines under matching conditions.
- [ ] T054 Run Diffcipline arm.
- [ ] T055 Publish raw outputs, scorer, limitations, and results.
