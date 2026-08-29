# Current specification

Active: [`001-proof-before-done`](001-proof-before-done/spec.md)

Status: `COMPLETE_CANONICAL`

## Canonical read order

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
18. `docs/v0.1.0-release-evidence.md`

Live GitHub/repository truth overrides every recorded SHA below.

## Canonical benchmark state

T001–T055 are complete through canonical benchmark-publication commit:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

The valid matched benchmark is `benchmark-arms` run `33200332207`, executed from canonical revision `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc` with repaired fixture/preparer/scorer boundary `cde4d0058ce522ddd9863457c29560679fac53dd`.

Baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6` correct and changed zero files. Diffcipline was the slowest arm by observed total wall-clock time. The evidence does not show a correctness advantage for Diffcipline. Run `33195457215` remains invalid comparative evidence. Durable raw evidence, checksums, provenance, exclusions, and limitations remain published under `benchmarks/results/v0.1/`.

## Canonical release commit and tag

The fixed v0.1 release commit is:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

T062 exact canonical evidence on that commit:

- `ci` push run `33237553577`: SUCCESS;
- `skills-compat` push run `33237553599`: SUCCESS;
- `release` push run `33237553641`: SUCCESS, including canonical benchmark validation, three locked native builds, SHA-256 aggregation, Sigstore provenance creation, and GitHub attestation verification.

T063 exact evidence:

- guarded tag-authority run `33237861972`: SUCCESS;
- lightweight `v0.1.0` resolves directly to `ab434ae114b5f11ea9eb882bf572831dc7634531`.

The tag must never be moved or replaced.

## Immutable publication and post-publication verification

Staging recovery run `33245697424` reused the exact signed T062 artifact and created GitHub Release ID `378936458` as a draft with exactly five byte-verified explicit assets. Draft evidence is preserved in `docs/v0.1.0-draft-staging-evidence.md` and artifact `9712760016` (`sha256:22f6606a28900558a3a79c8782f44d3807f615346d356fb5613fbdc1ece20d18`).

The release was published at `2026-08-29T10:35:12Z` with `draft=false` and `immutable=true` without moving the tag or replacing any asset.

The historical workflow definition at the tagged commit caused the first real `release.published` verifier run `33248168681` to fail before release/asset checks because it required canonical `main` to equal the tag SHA. PR #30 repaired only that obsolete verifier invariant and merged the owner-only recovery path to canonical `main` as:

`aa8dbe5f3d0e67355517c7d02f56a7e2d763b744`

Owner recovery command comment `5461857729` triggered verifier run `33248389195`. Verification job `99089706027` succeeded and machine-proved:

- fixed tag SHA and unchanged remote tag ref;
- tag ancestry to canonical `main`;
- crate version `0.1.0`;
- non-draft immutable release state;
- `gh release verify` success;
- exactly five explicit release assets;
- three native binary checksums;
- GitHub attestation verification for every binary;
- immutable release-asset verification for every explicit asset.

Durable verifier artifact `9713577320` has digest `sha256:59afe9908e14189b55d576f98fd81f7b9bd2c28341dcc42c9c4007c31fb85233`. Exact post-publication evidence is preserved in `docs/v0.1.0-release-evidence.md`.

## Completion

T064 is complete by exact post-publication machine evidence. T065 is satisfied by this completion ledger and the final evidence record being present on canonical `main` after this change is merged and its post-merge gates are verified.

Spec 001 / Diffcipline v0.1 has no remaining task in the canonical plan. `COMPLETE_CANONICAL` is valid only when this file, `tasks.md`, `execution-frontier.md`, and `docs/v0.1.0-release-evidence.md` are all present on canonical `main` and live GitHub truth still matches the fixed tag and immutable release evidence above.
