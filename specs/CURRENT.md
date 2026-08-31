# Current specification

Active: [`004-universal-engineering-governor`](004-universal-engineering-governor/spec.md)

Status: `IMPLEMENTATION`

Live GitHub/repository truth overrides this file.

## Canonical read order

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `README.md` roadmap
4. this file
5. `specs/004-universal-engineering-governor/spec.md`
6. `specs/004-universal-engineering-governor/plan.md`
7. `specs/004-universal-engineering-governor/tasks.md`
8. `specs/004-universal-engineering-governor/execution-frontier.md`
9. current proof/policy/skills/release contracts relevant to the active task.

## Completed roadmap history

Spec 001 / v0.1 is `COMPLETE_CANONICAL`; immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`.

Spec 002 / v0.2 is `COMPLETE_CANONICAL` at `0a6513aa17c90840a5024c62684d042571d431ed`. No v0.2 tag was created.

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted one-shot experiment and published negative findings remain frozen.

## Spec 004 canonical progress

Planning/T403 is canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.

Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161`.

Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011`.

Broad portability/T435 is canonical at `066c0138e5e2970781cc91abba38797654f92c77`.

Signed release-artifact capability/T447 is canonical at `b20b2671c75c5076fcf66397ee4a3f7c308bdfba`. PR #62 final head `4dbc751e09808999df61383092c2720f289c34d8` passed exact-head `ci` `33361112731` and `release` `33361112742`. Exact post-merge `ci` `33361219139` and `release` `33361219144` also completed `SUCCESS`. The trusted canonical release run built all three locked native binaries, generated and verified the three-entry `SHA256SUMS`, created keyless GitHub/Sigstore provenance, preserved the attestation bundle, verified every native binary subject, and intentionally skipped release drafting because no v1 tag is authorized.

## Immediate frontier

Phase F integrated qualification and closeout is next: T450–T455.

Update public documentation only with capabilities that are now implemented and canonical: proof-v1 schema/provenance, explicit monotonic enterprise policy, generic six-client Agent Skills portability, and the signed release-candidate capability. One final candidate must then pass exact-head `ci`, `skills-compat`, and `release`, reconcile reviews and canonical `main`, merge with an expected-head guard, and pass the exact post-merge repository/portability/schema-policy/signed-release gates.

T455 is a separate terminal governance record and must not claim `COMPLETE_CANONICAL` until T454 is machine-observed and the terminal record itself becomes canonical with successful required post-merge gates.

No public v1 tag or release is authorized by integrated closeout.
