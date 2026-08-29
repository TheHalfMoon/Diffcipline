# Current specification

Active: [`001-proof-before-done`](001-proof-before-done/spec.md)

Status: `V0_1_RELEASE_CANDIDATE`

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
10. `.github/workflows/release.yml`

Live GitHub/repository truth overrides every recorded SHA below.

## Verified benchmark state

T001–T055 are complete through canonical `main` commit:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

The valid matched benchmark is `benchmark-arms` run `33200332207`, executed from canonical revision:

`b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`

The repaired frozen fixture/preparer/scorer boundary is:

`cde4d0058ce522ddd9863457c29560679fac53dd`

Baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6` correct. The result does not show a Diffcipline correctness advantage. Diffcipline was the slowest arm by observed total wall-clock time. Durable raw evidence, checksums, provenance, the invalidated run #25, earlier exclusions, and limitations are published under `benchmarks/results/v0.1/`.

## Active release gate

T060 and T061 are implemented by the v0.1 closeout change. T062 must pass on the exact release candidate head before merge and again on the exact canonical release commit after merge:

- Rust fmt, clippy with warnings denied, and locked tests on Ubuntu, macOS, and Windows;
- Diffcipline proof gate on Ubuntu, macOS, and Windows;
- Agent Skills installer compatibility for all six supported agents;
- canonical benchmark archive/manifest checksum and provenance assertions;
- cross-platform locked release binary builds and three-subject SHA-256 manifest;
- post-merge Sigstore provenance/attestation verification.

Only after those exact-commit gates succeed may T063 create `v0.1.0`. T064 then verifies the tag-triggered release and T065 records post-tag evidence before `COMPLETE_CANONICAL` can be claimed.
