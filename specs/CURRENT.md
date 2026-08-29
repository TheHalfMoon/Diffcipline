# Current specification

Active: [`001-proof-before-done`](001-proof-before-done/spec.md)

Status: `V0_1_DRAFT_STAGED_IMMUTABLE_PUBLICATION_PENDING_ADMIN`

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
17. `docs/v0.1.0-draft-staging-evidence.md`

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

## Verified draft staging

PR #28 merged the reviewed staging recovery to canonical `main` as:

`528a1fd5a722bcd4c40e05b7e54a293c287e14b7`

Staging recovery run `33245697424` completed successfully and recovered the exact signed T062 artifact rather than rebuilding a replacement candidate. It created GitHub Release ID `378936458` as a draft containing exactly five byte-verified assets.

Durable draft evidence is recorded in `docs/v0.1.0-draft-staging-evidence.md` and workflow artifact `9712760016` (`sha256:22f6606a28900558a3a79c8782f44d3807f615346d356fb5613fbdc1ece20d18`).

## Active release gate

T064 remains open solely at immutable publication and post-publication verification.

A repository administrator must independently confirm **Enable release immutability** and publish the already-verified draft. Publication must trigger `.github/workflows/verify-v0.1.0-release.yml`, which requires the fixed tag to remain an ancestor of canonical `main`, `isImmutable=true`, release verification, all five asset verifications, binary provenance verification, and durable verification evidence.

T065 remains open until the exact post-publication evidence is committed and merged to canonical `main`. `COMPLETE_CANONICAL` must not be claimed before that merge.
