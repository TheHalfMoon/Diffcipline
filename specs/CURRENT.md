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

Spec 005 / v1 Release Polish is `COMPLETE_CANONICAL` at terminal canonical `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`. Its terminal post-merge `ci` `33398836802`, `skills-compat` `33398836751`, and `release` `33398836807` all completed `SUCCESS`.

## Active Spec 006 frontier

T614 and T615 are complete. The final implementation candidate `b75c469e4fbbcac41ac43b849d621f5ae38fa075` passed all required v1, historical v0.1, `ci`, `skills-compat`, and `release` workflows before expected-head merge. Canonical release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96` then passed exact post-merge qualification.

T620 is complete: owner-triggered `tag-v1.0.0` run `33403681664` completed `SUCCESS`, and `v1.0.0` resolves exactly to `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

T621 is complete: owner-triggered `stage-v1.0.0-release` run `33403855005` completed `SUCCESS`. It verified the exact canonical signed candidate, created draft release `379824838`, and round-trip byte-verified the five staged assets. The release remains a verified unpublished draft.

T622 is complete: PR #73 exact head `c4fdb7470aedd8249c202fd0d01a80d0149db692` passed all required exact-head workflows; expected-head merge produced canonical `e42bdccd7a97089fd986d478fadaf92b406d873d`; exact post-merge `ci` `33405800810`, `skills-compat` `33405800597`, and `release` `33405800938` all completed `SUCCESS`. The fixed release target did not move.

T630 has been independently satisfied: on 2026-08-31 a repository administrator supplied direct GitHub Settings evidence showing **Enable release immutability** selected and saved for `TheHalfMoon/Diffcipline`. The confirmation is recorded by the active T630 governance unit and live tag/draft state was rechecked afterward.

This T630 record becomes canonical only after its exact branch is qualified, merged, and required exact post-merge gates succeed.

After canonical T630, the active frontier is T631.

## Administrative publication boundary

The independent administrator confirmation required by T630 has been supplied. The already-verified `v1.0.0` draft may therefore be published through GitHub's administrative release surface once this T630 record is canonical.

No repository workflow may publish the draft. The connected repository execution tooling currently exposes no release-publication mutation, so it must not introduce repository automation as a bypass.

T631 must publish existing draft release `379824838` without changing the fixed tag or staged assets. Publication must trigger the immutable published-release verifier. T632 must prove `isDraft=false`, `isImmutable=true`, fixed tag lineage, release attestation, exact five-asset closure, checksums, binary attestations, and every release-asset verification. Spec 006 remains incomplete until that verifier succeeds and terminal T633 evidence becomes canonical.
