# Execution frontier — Spec 001

This document is the canonical continuation handoff for `001-proof-before-done`.

Live GitHub/repository truth always overrides this snapshot. Re-verify `main`, open pull requests, Actions runs, tags, releases, and the files in the read order below before acting.

## Canonical read order

1. `AGENTS.md`
2. `specs/CURRENT.md`
3. `specs/001-proof-before-done/spec.md`
4. `specs/001-proof-before-done/plan.md`
5. `specs/001-proof-before-done/tasks.md`
6. this file
7. `benchmarks/PROTOCOL.md`
8. `benchmarks/results/v0.1/REPORT.md`
9. `benchmarks/results/v0.1/MANIFEST.json`
10. `.github/workflows/ci.yml`
11. `.github/workflows/skills-compat.yml`
12. `.github/workflows/release.yml`

## Last verified canonical state

Canonical `main` at closeout start:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

T001–T055 are complete through that commit. PR #24 squash-merged the durable v0.1 benchmark publication.

The valid matched benchmark is `benchmark-arms` run `33200332207`, executed from canonical revision:

`b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`

The repaired frozen fixture/preparer/scorer boundary is:

`cde4d0058ce522ddd9863457c29560679fac53dd`

Run `33195457215` is invalid comparative evidence because the old preparer produced different ephemeral fixture base commits across arms. It must never be counted as comparative benchmark evidence.

## Canonical benchmark result

| Arm | Correct | Scorer pass | Changed files | Total seconds |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 |

The evidence does **not** show a correctness advantage for Diffcipline. Diffcipline was the slowest arm by observed total wall-clock time. The only correct fixture was the already-minimal no-op fixture `f06`. Preserve this losing result exactly.

Durable evidence is published under `benchmarks/results/v0.1/`:

- `MANIFEST.json`
- `REPORT.md`
- `SHA256SUMS`
- `raw-canonical-evidence.tar.gz`

## Active closeout state

T060 and T061 are implemented by the v0.1 closeout branch. T062 remains open until all required machine gates pass on one exact release-candidate head and then again on the exact post-merge canonical release commit.

Required T062 evidence:

1. `cargo fmt --all -- --check` on Linux, macOS, and Windows CI surfaces as defined by repository workflows.
2. `cargo clippy --workspace --all-targets --locked -- -D warnings`.
3. `cargo test --workspace --all-targets --locked`.
4. Diffcipline proof gate on Ubuntu, macOS, and Windows.
5. Agent Skills installation compatibility for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI from the exact candidate checkout.
6. Canonical v0.1 benchmark archive checksum and manifest assertions.
7. Locked release builds for Linux, macOS, and Windows.
8. A three-subject SHA-256 release manifest and checksum verification.
9. On trusted canonical `main`, successful Sigstore provenance creation plus GitHub attestation verification for every native binary.

If the candidate head changes, all exact-head PR gates must be re-established before merge.

## Tag and release authority

T063 is not authorized until T062 succeeds on the exact canonical post-merge release commit and the crate version is exactly `0.1.0`.

The `v0.1.0` tag must point to that exact verified canonical `main` SHA. Never tag a branch head, merge preview, stale commit, or unverified commit.

If the connected GitHub tooling cannot create a tag directly, use only a reviewed repository-native mechanism that:

- accepts an explicit canonical SHA;
- proves that SHA is current `main`;
- proves the required post-merge T062 workflows succeeded for that same SHA;
- proves the crate version is `0.1.0` and therefore the tag is `v0.1.0`;
- refuses an existing or mismatched tag;
- creates no tag until all checks pass.

T064 then requires the tag-triggered `release` workflow to publish and verify:

- Linux, macOS, and Windows native binaries;
- `SHA256SUMS`;
- checksum verification;
- Sigstore provenance;
- GitHub attestations;
- preserved `PROVENANCE.sigstore.json`;
- immutable GitHub Release state;
- tag/version equality.

T065 remains open until exact post-tag evidence is committed and merged to canonical `main`. Only then may `specs/CURRENT.md` and the task ledger record `COMPLETE_CANONICAL`.

## Stop conditions

Stop instead of weakening governance if:

- any required exact-head or post-merge gate is missing or failing;
- a valid review finding remains unresolved;
- the tag cannot be constrained to the verified canonical SHA;
- provenance, attestations, checksums, or published assets cannot be verified;
- post-tag evidence cannot be made canonical without bypassing repository rules.

No benchmark fixture, preparer, scorer, treatment, or result may be selectively changed or rerun to improve the published v0.1 outcome.
