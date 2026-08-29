# Execution frontier — Spec 001

This document is the canonical continuation and closeout handoff for `001-proof-before-done`.

Live GitHub/repository truth always overrides this snapshot. Re-verify `main`, pull requests, Actions runs, tags, releases, and the files below before making any future claim.

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
14. `.github/workflows/stage-v0.1.0-release.yml`
15. `.github/workflows/verify-v0.1.0-release.yml`
16. `docs/RELEASES.md`
17. `docs/v0.1.0-draft-staging-evidence.md`
18. `docs/v0.1.0-release-evidence.md`

## Canonical release lineage before final evidence merge

Canonical `main` containing the reviewed verifier-recovery path is:

`aa8dbe5f3d0e67355517c7d02f56a7e2d763b744`

The fixed v0.1 release commit and lightweight tag target remain:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

Never move, replace, delete, or recreate `v0.1.0`.

T062 exact canonical evidence on the release commit:

- `ci` push run `33237553577`: SUCCESS;
- `skills-compat` push run `33237553599`: SUCCESS;
- `release` push run `33237553641`: SUCCESS, including canonical benchmark evidence validation, three locked native builds, SHA-256 aggregation, Sigstore provenance creation, and GitHub attestation verification.

T063 exact evidence:

- guarded tag-authority run `33237861972`: SUCCESS;
- lightweight `refs/tags/v0.1.0` resolves directly to `ab434ae114b5f11ea9eb882bf572831dc7634531`.

## Canonical benchmark result

T001–T055 are complete through benchmark publication commit:

`78fcc432afcf0fabe2ed13800f7a9361570ab905`

Valid matched benchmark run `33200332207` used execution revision `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc` and repaired fixture/preparer/scorer boundary `cde4d0058ce522ddd9863457c29560679fac53dd`.

| Arm | Correct | Scorer pass | Changed files | Total seconds |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 |

The evidence does **not** show a correctness advantage for Diffcipline. Diffcipline was the slowest arm by observed total wall-clock time. The only correct fixture was the already-minimal no-op fixture `f06`. Run `33195457215` remains invalid comparative evidence. Never modify or selectively rerun benchmark evidence to improve the result.

## Draft staging evidence

The guarded tag workflow created `v0.1.0` with `GITHUB_TOKEN`, so GitHub's workflow-recursion guard did not emit the intended tag-push release workflow. The valid tag itself was unchanged.

PR #28 added the reviewed staging recovery. Owner command:

`/stage-release v0.1.0 ab434ae114b5f11ea9eb882bf572831dc7634531`

Staging run `33245697424`: SUCCESS.

The staging path reused signed release-candidate artifact `9710422207` with digest `sha256:586ebf4c711b1d746e7664a1a71f4f2dd4542ee3eff98df2dfeb1443e4021e7e`; it did not rebuild binaries or rerun the benchmark. GitHub Release ID `378936458` was created as a draft containing exactly five byte-verified explicit assets.

Durable draft staging evidence:

- repository record: `docs/v0.1.0-draft-staging-evidence.md`;
- workflow artifact: `9712760016`;
- artifact digest: `sha256:22f6606a28900558a3a79c8782f44d3807f615346d356fb5613fbdc1ece20d18`.

## Immutable publication

A repository administrator enabled release immutability and published the already-verified draft without changing the tag or assets.

Live publication identity:

- Release ID: `378936458`;
- URL: `https://github.com/TheHalfMoon/Diffcipline/releases/tag/v0.1.0`;
- published at: `2026-08-29T10:35:12Z`;
- `draft=false`;
- `immutable=true`.

The five explicit published assets remain the three native binaries, `PROVENANCE.sigstore.json`, and `SHA256SUMS` with the exact IDs and SHA-256 digests recorded in `docs/v0.1.0-release-evidence.md`.

## Post-publication verifier recovery and proof

The real `release.published` event triggered verifier run `33248168681` on the exact tagged commit. The historical workflow definition at that commit required `origin/main == tag SHA`. Because canonical post-tag evidence had legitimately advanced `main`, that obsolete invariant failed before any release-state or asset-verification step executed. Preserve this failed run as provenance; do not treat it as evidence against release integrity.

PR #30 repaired only the verifier execution path. Exact PR head `35911dc7a9273262a4cbb61366a12b9d26ed9451` passed its exact-head `ci`, `release`, staging-verifier validation, and immutable-verifier validation gates with no valid review finding. It was squash-merged as:

`aa8dbe5f3d0e67355517c7d02f56a7e2d763b744`

Post-merge push evidence on that exact canonical SHA:

- `ci` run `33248380028`: SUCCESS;
- `release` run `33248380047`: SUCCESS.

Owner recovery comment ID `5461857729` requested exactly:

`/verify-release v0.1.0 ab434ae114b5f11ea9eb882bf572831dc7634531`

Recovery verifier run `33248389195` executed from canonical `main` at `aa8dbe5f3d0e67355517c7d02f56a7e2d763b744`. Verification job `99089706027`: SUCCESS.

The machine proof succeeded for:

1. fixed tag SHA and unchanged remote tag ref;
2. tag ancestry to canonical `main`;
3. crate version `0.1.0`;
4. `isDraft=false` and `isImmutable=true`;
5. `gh release verify`;
6. exactly five explicit release assets;
7. the three native checksums in `SHA256SUMS`;
8. `gh attestation verify` for all native binaries;
9. `gh release verify-asset` for every explicit asset;
10. durable evidence recording and upload.

Durable verifier artifact:

- ID: `9713577320`;
- name: `v0.1.0-release-verification`;
- digest: `sha256:59afe9908e14189b55d576f98fd81f7b9bd2c28341dcc42c9c4007c31fb85233`;
- expires: `2026-11-27T10:41:03Z`;
- workflow run: `33248389195`;
- workflow head: `aa8dbe5f3d0e67355517c7d02f56a7e2d763b744`.

The artifact contains `release.json`, `published-assets.sha256`, and `verification.txt`. Exact contents and asset digests are preserved in `docs/v0.1.0-release-evidence.md`.

## Completion contract

T064 is complete by the successful immutable post-publication machine proof above.

T065 becomes canonical when this final evidence record, `specs/CURRENT.md`, and `tasks.md` are merged to canonical `main`, all exact-head PR gates are successful, and the exact post-merge canonical gates are successful.

After that merge, re-verify live GitHub truth before claiming completion:

- canonical `main` contains the final evidence ledger;
- `v0.1.0` still resolves directly to `ab434ae114b5f11ea9eb882bf572831dc7634531`;
- Release ID `378936458` remains `draft=false` and `immutable=true`;
- the five explicit assets remain unchanged;
- no required gate or valid review finding remains unresolved;
- no additional active Spec 001 task exists.

When all of those statements are machine-observed on the final canonical merge, Spec 001 / Diffcipline v0.1 is `COMPLETE_CANONICAL`.
