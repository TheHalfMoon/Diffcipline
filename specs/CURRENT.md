# Current specification

Active: Spec 006 / v1 Public Publication

Status: `ACTIVE_CANONICAL`

Spec 006 planning authority is canonical at `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`. Its exact post-merge `ci` `33399584260`, `skills-compat` `33399584290`, and `release` `33399584278` all completed `SUCCESS`.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`.

Spec 005 / v1 Release Polish is `COMPLETE_CANONICAL` at terminal canonical `e64a6ae9ad50edc9e08a1392c23134f96d4d7587`.

## Active frontier

Phase B publication implementation is authorized. The current bounded candidate sets version `1.0.0`, adds guarded owner-only `v1.0.0` tag authority, wires release qualification for that authority, and preserves immutable v0.1 validation against the historical tag itself.

No v1 tag or release exists from this candidate. T615 still gates tag creation.

After this unit becomes canonical, the next bounded unit is recovery draft staging plus immutable published-release verification and detailed release documentation. That unit must become the final T614/T615 publication implementation candidate before any tag can be created.

## Publication boundary

Repository automation must not publish the v1 draft. Independent repository-administrator confirmation that GitHub release immutability is enabled is required before publication through the administrative release surface.
