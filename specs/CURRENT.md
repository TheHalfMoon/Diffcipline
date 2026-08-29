# Current specification

Active: [`001-proof-before-done`](001-proof-before-done/spec.md)

Status: `V0_1_TAGGED_RELEASE_STAGING`

## Canonical continuation

Read in this order before acting:

1. `AGENTS.md`
2. this file
3. `specs/001-proof-before-done/spec.md`
4. `specs/001-proof-before-done/plan.md`
5. `specs/001-proof-before-done/tasks.md`
6. `specs/001-proof-before-done/execution-frontier.md`
7. `benchmarks/PROTOCOL.md`
8. `benchmarks/results/v0.1/REPORT.md`
9. `benchmarks/results/v0.1/MANIFEST.json`
10. `.github/workflows/ci.yml`
11. `.github/workflows/skills-compat.yml`
12. `.github/workflows/release.yml`
13. `.github/workflows/tag-v0.1.0.yml`
14. `.github/workflows/stage-v0.1.0-release.yml`
15. `.github/workflows/verify-v0.1.0-release.yml`
16. `docs/RELEASES.md`

Live GitHub/repository truth overrides every recorded SHA below.

## Verified benchmark state

T001–T055 are complete through canonical benchmark-publication commit:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

The valid matched benchmark is `benchmark-arms` run `33200332207`, executed from canonical revision:

`b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`

The repaired frozen fixture/preparer/scorer boundary is:

`cde4d0058ce522ddd9863457c29560679fac53dd`

Baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6` correct. The result does not show a Diffcipline correctness advantage. Diffcipline was the slowest arm by observed total wall-clock time. Durable raw evidence, checksums, provenance, the invalidated run `33195457215`, earlier exclusions, and limitations are published under `benchmarks/results/v0.1/`.

## Verified release commit and tag

The canonical v0.1 release commit is:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

T062 is complete on that exact commit:

- `ci` push run `33237553577`: SUCCESS, including Rust and Diffcipline proof gates on Ubuntu, macOS, and Windows;
- `skills-compat` push run `33237553599`: SUCCESS for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- `release` push run `33237553641`: SUCCESS, including canonical benchmark validation, three locked native builds, SHA-256 aggregation, Sigstore provenance creation, and GitHub attestation verification.

T063 is complete. Guarded tag-authority run `33237861972` succeeded and created lightweight `v0.1.0` directly at the release commit above. The tag must never be moved or replaced.

## Active release gate

T064 remains open. The repository-native tag was pushed by a workflow using `GITHUB_TOKEN`; GitHub's workflow-recursion guard therefore did not create a second tag-push workflow run. No draft release was created, and the tag remains valid.

The authorized recovery is `.github/workflows/stage-v0.1.0-release.yml`. It must recover the already-signed `signed-release-candidate` artifact from exact T062 release run `33237553641`, verify the tag lineage, checksums, binary attestations, T062/T063 evidence, and exact five-asset round trip, and create a draft release without rebuilding or moving the tag.

After the verified draft exists, a repository administrator must independently confirm **Enable release immutability** and publish that draft. Publication must trigger `.github/workflows/verify-v0.1.0-release.yml`, which requires the fixed tag to remain an ancestor of canonical `main`, `isImmutable=true`, release verification, all five asset verifications, binary provenance verification, and durable verification evidence.

T065 remains open until the exact post-tag and post-publication evidence is committed and merged to canonical `main`. `COMPLETE_CANONICAL` must not be claimed before that merge.
