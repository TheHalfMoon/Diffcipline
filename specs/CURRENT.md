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

Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161`. The v1 proof contract is `diffcipline.proof/v1` / `1.0` with deterministic schema identity, legacy evidence semantics, and policy provenance.

Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011`. PR #58 final head `7ae53bfde368287a3a780fb591e7a3d21166856f` passed exact-head `ci` `33357573607` and `release` `33357573613`; post-merge `ci` `33357739486` and `release` `33357739507` also succeeded. Enterprise policy is explicit local-file input, monotonic over repository policy, fail-closed, and disclosed through the stable proof-v1 policy provenance object.

The post-merge release evidence on `f0198395f0a141048b272bfd495f585fb76f6011` also proves locked Linux/macOS/Windows builds, checksum-manifest closure, signed Sigstore provenance, and attestation-subject verification. Those observations may be reused as evidence in Phase E only where the release contract remains unchanged and later exact-head/final qualification requirements are still satisfied.

## Immediate frontier

Phase D broad agent portability is next: T430–T435. Preserve one canonical `diffcipline` and `diffcipline-review` skill behavior, qualify the existing six named clients from exact heads, add a generic Agent Skills layout/content qualification independent of any one client, and document platform-neutral boundaries and limitations.

Do not create platform-specific behavioral forks. No public v1 tag/release is authorized by this phase.
