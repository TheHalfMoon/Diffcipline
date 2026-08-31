# Current specification

Active: Spec 005 / v1 Release Polish

Status: `ACTIVE_CANONICAL`

Spec 005 planning authority is canonical at `3e7abe3ca7c95fe327ef04ccb46fae89286ab8bc`. Its exact post-merge gates completed successfully: `ci` `33397182736`, `skills-compat` `33397182730`, and `release` `33397182737`.

Live GitHub/repository truth overrides this file.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

Spec 004 / v1 Universal Engineering Governor is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7`. Its final capability boundary is canonical at `2ff687c038f72a3b747e85ad907d2400955cb649`, where `ci` `33365950241`, `skills-compat` `33365950200`, and `release` `33365950214` all completed `SUCCESS`; the trusted release run created signed Sigstore provenance and verified every native binary subject. The terminal completion record itself then passed canonical `ci` `33366320014`, `skills-compat` `33366320027`, and `release` `33366320048`.

## Active frontier

Spec 005 Phase B is active under the canonical planning authority:

- the quoted-array comma defect was machine-reproduced on red head `c20a81b9bf47ac3b7da55db6300385b8e25e706f` by `ci` `33397575574`, where Rust `cargo test --workspace --all-targets --locked` failed after format and clippy succeeded;
- a surgical dependency-free quote-aware separator scan now exists on the implementation branch with positive comma-preservation and negative fail-closed regression coverage;
- the proof contract now states that `--enterprise-policy <path>` is effective only when supplied and that mandatory organizational enforcement requires an externally controlled CI path that supplies it;
- live repository hygiene review found no issue-template directory and an empty GitHub repository description; available authorized tooling cannot mutate description/topics, and Spec 005 makes that tooling limitation non-blocking.

The next gate is T515: one final exact implementation head must pass `ci`, `skills-compat`, `release`, historical immutable-release guards, review/thread/comment reconciliation, mergeability, and canonical-main reconciliation.

## Publication boundary

Spec 005 does not authorize version `1.0.0`, tag `v1.0.0`, a draft release, public publication, or published-asset verification.

Those irreversible actions require a separate explicit canonical publication specification after Spec 005 is `COMPLETE_CANONICAL`.
