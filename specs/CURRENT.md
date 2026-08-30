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

Spec 003 / v0.3 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its terminal post-merge `ci` `33302411448`, `benchmark-v0.3-qualification` `33302411430`, `skills-compat` `33302411434`, and `release` `33302411442` all succeeded. Its accepted one-shot experiment and published negative findings remain frozen.

## Spec 004 canonical planning authority

PR #56 planning head `cb590fde5dc3bf76abee1ec3bd8b512607d63dcf` passed exact-head `ci` `33302675371`, `skills-compat` `33302675367`, and `release` `33302675373`, then merged as canonical `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.

Exact post-merge `ci` `33302752212`, `skills-compat` `33302752218`, and `release` `33302752209` all completed `SUCCESS`. T403 is therefore canonical and implementation is authorized in task order.

## Active Phase B candidate

Stable proof schema T410–T415 are implemented on the current candidate:

- repository schema `schemas/proof-v1.json` identifies `diffcipline.proof/v1` / `1.0`;
- `check --json` preserves existing fields and exit semantics while adding schema identity and policy provenance;
- policy mode is currently `default` or `repository`; `enterprise` is reserved in the v1 schema for Phase C;
- Rust tests and `scripts/validate-proof-v1.py` bind real CLI output to exact schema field order and reject an incompatible schema version;
- CI runs this contract validation with no new Rust runtime dependency.

## Immediate frontier

Only T416 remains for Phase B: the exact stable-schema candidate must pass required exact-head gates, reconcile reviews, merge with an expected-head guard, and pass exact post-merge verification. Enterprise policy implementation is blocked until T416 is canonical.

No public v1 tag/release is authorized by this phase.
