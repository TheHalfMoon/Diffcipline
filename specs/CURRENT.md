# Current specification

Active: Spec 006 / v1 Public Publication

Status: `COMPLETE_CANONICAL`

This terminal status is effective only after the exact terminal closeout record is merged to canonical `main` and its resulting canonical SHA passes exact post-merge `ci`, `skills-compat`, and `release`. Until then, this branch is only the terminal completion candidate and live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`.

Spec 005 / v1 Release Polish is `COMPLETE_CANONICAL` at terminal canonical `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

## Spec 006 terminal evidence

The sole authorized `v1.0.0` release commit is `5cb1c77340b75649f6168e0e8f66479ea047ea96`. Its exact post-merge `ci` `33403468465`, `skills-compat` `33403468547`, and `release` `33403468550` completed `SUCCESS` before tag creation.

Owner-only tag authority run `33403681664` created `v1.0.0` exactly at that release SHA. Owner-only staging run `33403855005` created release `379824838` from the exact canonical signed candidate and byte-verified exactly five staged assets.

T630 administrator evidence became canonical through PR #74 at `2444671549cb22fc664e6f3476dcb43cd964d28f`.

The administrator published existing release `379824838` through GitHub's administrative surface at `2026-08-31T18:17:06Z`. GitHub reports `draft=false`, `immutable=true`, `prerelease=false`, tag `v1.0.0`, and the unchanged five-asset set.

The first automatic published-release verifier run `33424164688` failed before immutable verification because of a verifier command-composition defect. That failure remains preserved evidence.

PR #76 corrected only the verifier mechanics. Expected-head merge produced canonical recovery SHA `95efb154b93a4745e0265bb4e2b94b60cd1d0463`; exact post-merge `ci` `33424737598`, `skills-compat` `33424737542`, and `release` `33424737688` completed `SUCCESS`.

Owner-triggered recovery verifier run `33424987600`, job `99596275866`, completed `SUCCESS` and machine-proved:

- fixed tag lineage and crate version `1.0.0`;
- successful tag/staging authority evidence;
- `isDraft=false` and `isImmutable=true`;
- GitHub release attestation;
- exact five-asset closure;
- three-entry checksum closure;
- native-binary attestations;
- verification of every published release asset;
- durable evidence artifact `9770386235` with digest `sha256:1ecfe4b8e1bac7f66c56d14602ac655514b05b2b87816d2efe683867d6053db0`.

T632 is machine-observed complete. `specs/006-v1-publication/t632-published-verification.md` preserves the detailed evidence.

## Terminal frontier

T633 is the only remaining effectiveness gate: this terminal record itself must pass exact-head qualification, clean reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` on the resulting canonical SHA.

Once those conditions hold, Spec 006 is `COMPLETE_CANONICAL` with no remaining publication frontier.

Only then may the prepared noncanonical Spec 007 Category Leadership candidate be reconciled against the new canonical `main`, refreshed from current public ecosystem truth, and activated through its own canonical planning-authority merge.
