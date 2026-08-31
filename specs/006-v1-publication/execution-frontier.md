# Execution frontier — Spec 006

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 005 is `COMPLETE_CANONICAL` at `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

Spec 006 planning authority is `ACTIVE_CANONICAL` at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577` after exact post-merge `ci` `33399584260`, `skills-compat` `33399584290`, and `release` `33399584278` all completed `SUCCESS`.

The final Spec 006 publication implementation is canonical through PR #72. Its exact candidate head `b75c469e4fbbcac41ac43b849d621f5ae38fa075` passed all nine required pull-request workflows: `ci` `33403121745`, `skills-compat` `33403121769`, `release` `33403121862`, `tag-v1.0.0` `33403121753`, `stage-v1.0.0-release` `33403121718`, `verify-v1.0.0-release` `33403121792`, `tag-v0.1.0` `33403121587`, `stage-v0.1.0-release` `33403121609`, and `verify-v0.1.0-release` `33403121807`. Review/thread/comment, mergeability, and canonical-main reconciliation were clean before expected-head merge.

Expected-head merge of PR #72 produced canonical release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`. Exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` all completed `SUCCESS`. The canonical release run completed all three locked native builds, deterministic checksum closure, signed Sigstore provenance, and attestation-subject verification. This SHA is the sole authorized `v1.0.0` release target.

## Guarded tag

The repository owner requested:

```text
/release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

`tag-v1.0.0` run `33403681664` completed `SUCCESS` on the exact release SHA. `refs/tags/v1.0.0` resolves exactly to `5cb1c77340b75649f6168e0e8f66479ea047ea96`; the release target has not moved.

## Verified draft

The repository owner then requested:

```text
/stage-release v1.0.0 5cb1c77340b75649f6168e0e8f66479ea047ea96
```

`stage-v1.0.0-release` run `33403855005` completed `SUCCESS`. Its mutation job `99526451916` successfully:

- parsed the explicit owner request;
- verified the fixed tag, canonical release commit, and lineage;
- resolved exact successful canonical `ci`, `skills-compat`, `release`, and tag-authority evidence;
- downloaded and verified the exact non-expired canonical `signed-release-candidate`;
- verified its five-file closure, checksums, and native-binary attestations;
- created draft release `379824838`;
- downloaded the draft and round-trip byte-verified every staged asset against the canonical signed candidate;
- retained machine-readable staging evidence.

Live draft release `379824838` is `v1.0.0`, `draft=true`, `prerelease=false`, and unpublished. It contains exactly five assets:

1. `diffcipline-aarch64-apple-darwin`;
2. `diffcipline-x86_64-pc-windows-msvc.exe`;
3. `diffcipline-x86_64-unknown-linux-gnu`;
4. `SHA256SUMS`;
5. `PROVENANCE.sigstore.json`.

A verified draft is not a published release.

## T622 evidence-record candidate

Branch `docs/006-tag-staging-evidence` records T614 through T621 live evidence without changing the release target, tag, draft, product behavior, dependencies, or publication state.

This T622 record becomes canonical only after its exact qualified head is merged and the required exact post-merge gates succeed. Until then, live GitHub truth remains authoritative over this candidate wording.

## Current frontier — T630 external administrative prerequisite

After canonical T622, the next permitted step is T630: an independent repository administrator must confirm in GitHub repository settings that **Enable release immutability** is active.

The currently connected repository execution surface does not expose the repository-level release-immutability administration setting and therefore cannot independently inspect, infer, or change it. The existence of immutable historical `v0.1.0` is not evidence that the current repository setting is enabled for this publication boundary.

No repository workflow is authorized to publish the draft. Publication through the GitHub administrative release surface remains prohibited until T630 is independently satisfied. Only after T630 may T631 publish the already-verified draft. Publication must then trigger T632, whose verifier requires `isDraft=false`, `isImmutable=true`, fixed tag lineage, successful `gh release verify`, exactly five assets, checksum closure, binary attestations, and verification of every published release asset.

Spec 006 remains `ACTIVE_CANONICAL`, not `COMPLETE_CANONICAL`, until T632 succeeds and T633 terminal evidence becomes canonical.
