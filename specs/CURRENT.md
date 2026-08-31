# Current specification

Active: Spec 006 / v1 Public Publication

Status: `ACTIVE_CANONICAL`

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`. Its final publication implementation is canonical through PR #72, whose expected-head merge produced the sole authorized `v1.0.0` release target `5cb1c77340b75649f6168e0e8f66479ea047ea96`. Exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` all completed `SUCCESS` on that release SHA.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`.

Spec 005 / v1 Release Polish is `COMPLETE_CANONICAL` at terminal canonical `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

## Completed Spec 006 publication prerequisites

T620 created `v1.0.0` exactly at `5cb1c77340b75649f6168e0e8f66479ea047ea96` through owner-only tag authority run `33403681664`.

T621 staged and byte-verified release `379824838` through owner-only recovery run `33403855005` with exactly three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`.

T622 became canonical through PR #73 at `e42bdccd7a97089fd986d478fadaf92b406d873d` with successful exact post-merge `ci`, `skills-compat`, and `release` gates.

T630 became canonical through PR #74 at `2444671549cb22fc664e6f3476dcb43cd964d28f` after independent GitHub Settings evidence showed release immutability enabled; its exact post-merge `ci`, `skills-compat`, and `release` gates all completed `SUCCESS`.

T631 is complete: existing release `379824838` was published through GitHub's administrative release surface at `2026-08-31T18:17:06Z`. Live GitHub now reports `draft=false`, `immutable=true`, `prerelease=false`, tag `v1.0.0`, with the same fixed five assets and release target.

## Active Spec 006 frontier — T632 recovery verification

The automatic `release.published` verifier ran as `verify-v1.0.0-release` run `33424164688` on exact release SHA `5cb1c77340b75649f6168e0e8f66479ea047ea96` and failed in job `99593546041` before immutable-release verification.

The lineage step succeeded. `Verify tag and staging authority evidence` failed with:

```text
accepts 1 arg(s), received 4
```

The defect is in verifier command composition: it attempted to combine `gh api --jq` with jq variable arguments that `gh --jq` does not accept. The immutable release itself remains published and unchanged.

The active recovery unit is `fix/006-v1-published-verifier-recovery`. It preserves the same issue-comment evidence-selection semantics while piping the `gh api` JSON response into standalone `jq -r --arg sha ...`.

After canonical qualification and merge of that recovery unit, the repository owner must trigger:

```text
/verify-release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

T632 requires that recovery run to prove fixed tag lineage, successful tag/staging authority evidence, `isDraft=false`, `isImmutable=true`, release attestation, exact five-asset closure, checksums, binary attestations, every release-asset verification, and durable evidence. T632 then gates terminal T633.

Spec 006 remains incomplete until T632 succeeds and T633 becomes canonical. The prepared Spec 007 Category Leadership candidate remains noncanonical and blocked until that terminal closeout.
