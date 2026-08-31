# Current specification

Active: Spec 005 / v1 Release Polish

Status: `PLANNING_CANDIDATE`

Spec 005 planning authority is candidate-only until T503 is merged to canonical `main` and the required exact post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA. No Spec 005 implementation begins before that boundary.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`. Its final capability boundary is canonical at `2ff687c038f72a3b747e85ad907d2400955cb649`, where `ci` `33365950241`, `skills-compat` `33365950200`, and `release` `33365950214` all completed `SUCCESS`; the trusted release run created signed Sigstore provenance and verified every native binary subject. The terminal completion record itself then passed canonical `ci` `33366320014`, `skills-compat` `33366320027`, and `release` `33366320048`.

## Active frontier

Spec 005 is a narrow pre-v1 polish unit only:

- correct the verified quoted-array comma parsing defect without adding a runtime dependency;
- add focused regression coverage while preserving fail-closed policy behavior;
- document the actual enforcement boundary of explicit `--enterprise-policy <path>` input;
- review low-cost repository hygiene where supported by authorized tooling;
- qualify and close the unit with exact-head, expected-head merge, and post-merge machine evidence.

## Publication boundary

Spec 005 does not authorize version `1.0.0`, tag `v1.0.0`, a draft release, public publication, or published-asset verification.

Those irreversible actions require a separate explicit canonical publication specification after Spec 005 is `COMPLETE_CANONICAL`.
