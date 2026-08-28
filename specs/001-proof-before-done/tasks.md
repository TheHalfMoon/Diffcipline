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
- [ ] T044 Verify installation through compatible Agent Skills installers.

Verification evidence for T042: run #11 established the initial cross-platform Action behavior on `a12089f8eb01a5e54d9ae786509ffe8db75dc443`; run #12 then exposed a macOS fixture-directory collision and T042 was reopened. Commit `db80d1801e6a650c599c05f3a76e80d4d0359e86` replaced clock-derived fixture names with process-local atomic IDs. Run #13 passed the repaired implementation on Ubuntu, macOS, and Windows, and final ledger head `7029021a3066bd26ff30c67c3fc4a6e95b92a801` passed all six jobs in `ci` run #14 before PR #4 merged.

Verification evidence for T043: PR #5 head `518200a6cd639d7fd9db994eebd84507a71b950d` passed normal `ci` run #16 and release workflow run #1. Release run #1 built and smoke-tested host-native Linux, macOS, and Windows binaries and generated a verified three-subject `SHA256SUMS`; signing and publishing were intentionally unavailable on the pull request. After merge, canonical `main` commit `4348b40049d64f5b5eb5dbe060953caa3c90fdc4` passed `ci` run #17 and trusted release run #2. Run #2 created build provenance for all three binary subjects with `actions/attest`, signed it with the Public Good Sigstore instance, uploaded it to the Rekor transparency log and GitHub Attestations (attestation `43657557`), verified every subject with `gh attestation verify`, preserved `PROVENANCE.sigstore.json`, and uploaded signed-release-candidate artifact `9686520987`. Tag publication remains NOT RUN because no release tag has been created; the workflow will publish only a matching `v<crate version>` tag.

## Phase E — Benchmark

- [x] T050 Publish benchmark protocol before claims.
- [ ] T051 Build public task fixtures.
- [ ] T052 Run unassisted-agent baseline.
- [ ] T053 Run comparison skill baselines under matching conditions.
- [ ] T054 Run Diffcipline arm.
- [ ] T055 Publish raw outputs, scorer, limitations, and results.
