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

T622 is the current repository-governance unit: record this tag/staging evidence canonically without changing the release target. Its candidate record becomes effective only after merge and exact post-merge qualification.

After canonical T622, the active frontier is T630.

## Administrative publication boundary

Before publication, an independent repository administrator must confirm in GitHub repository settings that **Enable release immutability** is active.

The connected repository execution tooling does not expose that repository-level administration setting, so it must not infer or bypass it. Historical immutable `v0.1.0` does not substitute for the required current administrative confirmation.

No repository workflow may publish the draft. Only after T630 is independently satisfied may the existing verified `v1.0.0` draft be published through GitHub's administrative release surface. Publication must trigger the immutable published-release verifier, and Spec 006 remains incomplete until that verifier succeeds and terminal T633 evidence becomes canonical.
