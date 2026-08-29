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
13. `.github/workflows/tag-v0.1.0.yml`
14. `.github/workflows/verify-v0.1.0-release.yml`
15. `docs/RELEASES.md`

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
9. Validation of the guarded tag authority and immutable release verifier.
10. On trusted canonical `main`, successful Sigstore provenance creation plus GitHub attestation verification for every native binary.

If the candidate head changes, all exact-head PR gates must be re-established before merge.

## Change-size policy

The canonical `.diffcipline.toml` sets `max_added_lines = 400` and `max_changed_files = 12`. The original combined closeout PR exceeded that policy. Release/CI workflow hardening is therefore landed as a separate prerequisite PR rather than weakening the policy. After that prerequisite becomes canonical, the remaining closeout diff must be re-proven against the updated `main` and must independently satisfy the same policy.

## Tag authority

T063 is not authorized until T062 succeeds on the exact canonical post-merge release commit and the crate version is exactly `0.1.0`.

The `v0.1.0` tag must point to that exact verified canonical `main` SHA. Never tag a branch head, merge preview, stale commit, or unverified commit.

Because the connected GitHub tooling cannot create a tag directly, `.github/workflows/tag-v0.1.0.yml` is the reviewed repository-native authority. It:

- accepts an explicit 40-character canonical SHA;
- proves that SHA is current `main`;
- proves the required post-merge T062 workflows succeeded for that same SHA;
- proves the crate version is `0.1.0` and therefore the tag is `v0.1.0`;
- refuses an existing or mismatched tag;
- creates a lightweight tag directly at the verified canonical SHA only after all checks pass.

## Immutable release authority

The tag-triggered `release.yml` workflow must build and attest the exact tagged source, then create a **draft** GitHub Release containing exactly five assets:

- Linux, macOS, and Windows native binaries;
- `SHA256SUMS`;
- preserved `PROVENANCE.sigstore.json`.

The workflow must verify the checksum manifest, GitHub artifact attestations, tag/version equality, draft state, asset list, and byte-for-byte round-trip download before it succeeds.

The draft is intentionally not published by repository automation. GitHub's repository immutable-release setting requires repository Administration access to inspect or change, while the ordinary workflow `GITHUB_TOKEN` does not receive that permission. A `403 Resource not accessible by integration` therefore cannot be interpreted as evidence that immutability is enabled or disabled.

Before final T064 publication, a repository administrator must independently confirm that **Enable release immutability** is active and publish the already-verified draft through GitHub's administrative release surface. This is a genuine external administrative prerequisite.

Publication triggers `.github/workflows/verify-v0.1.0-release.yml`. That exact release-event workflow must machine-prove:

- the published tag still resolves to canonical `main` and crate version `0.1.0`;
- `isDraft=false` and `isImmutable=true`;
- a valid GitHub Release attestation via `gh release verify`;
- exactly five release assets;
- `SHA256SUMS` validates all three native binaries;
- each native binary verifies with `gh attestation verify`;
- every published asset verifies with `gh release verify-asset`;
- a durable `v0.1.0-release-verification` Actions artifact records the release metadata, tag SHA, run ID, and published asset digests.

T064 is not complete if any of those post-publication checks fail or are absent.

T065 remains open until exact post-tag and post-publication evidence is committed and merged to canonical `main`. Only then may `specs/CURRENT.md` and the task ledger record `COMPLETE_CANONICAL`.

## Stop conditions

Stop instead of weakening governance if:

- any required exact-head or post-merge gate is missing or failing;
- a valid review finding remains unresolved;
- the tag cannot be constrained to the verified canonical SHA;
- repository release immutability cannot be independently confirmed before publication;
- provenance, attestations, checksums, or published assets cannot be verified;
- post-tag evidence cannot be made canonical without bypassing repository rules.

No benchmark fixture, preparer, scorer, treatment, or result may be selectively changed or rerun to improve the published v0.1 outcome.
