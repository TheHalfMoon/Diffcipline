# Current specification

Active: none

Status: `COMPLETE_CANONICAL`

This terminal status is effective only after the Spec 004 completion record is merged to canonical `main` and its required exact post-merge gates succeed. Before those conditions hold, the completion branch is only a terminal candidate.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor has completed its capability implementation and integrated post-merge qualification. Its final capability boundary is canonical at `2ff687c038f72a3b747e85ad907d2400955cb649`, where `ci` `33365950241`, `skills-compat` `33365950200`, and `release` `33365950214` all completed `SUCCESS`; the trusted release run created signed Sigstore provenance and verified every native binary subject.

## Terminal frontier

No Spec 004 implementation task remains after T455.

No later roadmap item or specification becomes active implicitly. Any future implementation requires new canonical specification authority derived from live repository truth.

No public v1 tag or release is authorized by Spec 004 completion. That irreversible publication boundary requires separate explicit canonical authority.
