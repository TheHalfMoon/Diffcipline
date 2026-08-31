# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

Spec 006 planning authority is `ACTIVE_CANONICAL` at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577` after exact post-merge `ci` `33399584260`, `skills-compat` `33399584290`, and `release` `33399584278` all completed `SUCCESS`.

The final Spec 006 publication implementation is canonical through PR #72. Expected-head merge produced the sole authorized release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`, whose exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` all completed `SUCCESS`, including three locked native builds, deterministic checksum closure, signed Sigstore provenance, and attestation-subject verification.

## Guarded tag and verified draft

Owner-only tag authority run `33403681664` created `v1.0.0` exactly at `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

Owner-only recovery staging run `33403855005` verified the exact canonical signed release candidate, created release `379824838` as a draft, and round-trip byte-verified exactly five assets:

1. `diffcipline-aarch64-apple-darwin`;
2. `diffcipline-x86_64-pc-windows-msvc.exe`;
3. `diffcipline-x86_64-unknown-linux-gnu`;
4. `SHA256SUMS`;
5. `PROVENANCE.sigstore.json`.

PR #73 canonically recorded T620–T622 evidence at `e42bdccd7a97089fd986d478fadaf92b406d873d`. PR #74 canonically recorded the independent T630 administrator confirmation at `2444671549cb22fc664e6f3476dcb43cd964d28f`; its exact post-merge `ci`, `skills-compat`, and `release` gates all completed `SUCCESS`.

## T631 published immutable v1.0.0

On 2026-08-31 the repository administrator published the already-verified draft through GitHub's administrative release surface.

Live GitHub release `379824838` now reports:

- `tag_name=v1.0.0`;
- `draft=false`;
- `immutable=true`;
- `prerelease=false`;
- `published_at=2026-08-31T18:17:06Z`;
- the same five staged assets;
- fixed tag target `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

T631 is complete. Publication did not move the tag, replace the release, or mutate the staged asset set.

## Initial T632 verifier failure

The `release.published` event correctly triggered `verify-v1.0.0-release` run `33424164688` on the fixed release SHA.

Its lineage step succeeded. The next step, `Verify tag and staging authority evidence`, failed before any immutable-release or asset-verification step could run. Job `99593546041` recorded:

```text
accepts 1 arg(s), received 4
```

The failure is a verifier implementation defect: `gh api --jq` accepts one jq expression, but the workflow attempted to pass `--arg sha ...` as additional `gh --jq` arguments. This is not evidence of release corruption and must not be hidden or relabeled as success.

## Current frontier — T632 recovery verification

Branch `fix/006-v1-published-verifier-recovery` replaces the invalid `gh api --jq --arg` composition with a plain `gh api` JSON stream piped into `jq -r --arg sha ...`. The exact successful issue-comment run selection semantics remain unchanged.

The recovery unit must:

1. qualify the exact verifier-fix head through all required pull-request workflows;
2. reconcile reviews, threads, comments, mergeability, and canonical `main`;
3. merge only the expected head;
4. require exact post-merge `ci`, `skills-compat`, and `release` success;
5. trigger the guarded owner-only recovery command:

```text
/verify-release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

6. require the recovery verifier to prove fixed tag lineage, successful tag/staging authority evidence, `isDraft=false`, `isImmutable=true`, GitHub release attestation, exact five-asset closure, checksum closure, native-binary attestations, every `gh release verify-asset`, and durable uploaded evidence.

Spec 006 remains `ACTIVE_CANONICAL`, not `COMPLETE_CANONICAL`, until T632 succeeds and T633 terminal evidence becomes canonical.
