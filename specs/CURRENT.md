# Current specification

Active: Spec 006 / v1 Public Publication

Status: `PLANNING_CANDIDATE`

Spec 006 becomes active canonical publication authority only after its planning record is merged to canonical `main` and the required exact post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`.

Spec 005 / v1 Release Polish is `COMPLETE_CANONICAL` at terminal canonical `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`. Its terminal post-merge `ci` `33398836802`, `skills-compat` `33398836751`, and `release` `33398836807` all completed `SUCCESS`; the trusted release run built all three native binaries, verified deterministic checksum closure, created signed Sigstore provenance, preserved the attestation bundle, and verified every native-binary subject.

## Active frontier

Spec 006 is a publication-only authority derived from live terminal Spec 005 truth. It authorizes no new product feature.

The immediate gate is T603: make the publication planning record canonical and prove exact post-merge `ci`, `skills-compat`, and `release` before any version bump, tag, draft release, or publication implementation begins.

## Publication boundary

Until T603 is canonical, version `1.0.0`, tag `v1.0.0`, draft staging, publication, and published-asset verification remain unauthorized.

Even after publication implementation is canonical, repository automation must not publish the draft. Independent repository-administrator confirmation that GitHub release immutability is enabled is required before publication through the administrative release surface.
