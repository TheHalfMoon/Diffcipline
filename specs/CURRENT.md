# Current specification

Active: [`002-intent-aware-scope`](002-intent-aware-scope/spec.md)

Status: `ACTIVE_IMPLEMENTATION`

## Canonical read order

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. this file
4. `specs/002-intent-aware-scope/spec.md`
5. `specs/002-intent-aware-scope/plan.md`
6. `specs/002-intent-aware-scope/tasks.md`
7. `specs/002-intent-aware-scope/execution-frontier.md`
8. `.diffcipline.toml`
9. `crates/diffcipline-cli/src/main.rs`
10. `crates/diffcipline-cli/tests/cli.rs`
11. `action.yml`
12. `.github/workflows/ci.yml`

Live GitHub/repository truth overrides every recorded SHA below.

## Completed Spec 001 / v0.1

Spec 001 reached `COMPLETE_CANONICAL` on canonical `main`:

`d74ed5f8789fb255e24f124e3283939cdc080cd0`

The fixed `v0.1.0` tag remains directly at:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

Release ID `378936458` was published immutable at `2026-08-29T10:35:12Z`. Post-publication recovery verifier run `33248389195` succeeded; durable verifier artifact `9713577320` has digest `sha256:59afe9908e14189b55d576f98fd81f7b9bd2c28341dcc42c9c4007c31fb85233`.

The v0.1 benchmark remains intentionally unfavorable and unchanged: Baseline, Karpathy, Ponytail, and Diffcipline each scored `1/6`, all four arms changed zero files, Diffcipline was slowest by observed total wall-clock time, and the evidence does not support a Diffcipline correctness advantage.

## Spec 002 authority

The canonical README roadmap defines v0.2 as `Intent-aware scope` with exactly three product goals:

1. proof contract for expected files and forbidden surfaces;
2. risk-aware verification profiles;
3. GitHub PR annotation.

Spec 002 translates those roadmap goals into deterministic, dependency-free acceptance criteria. It does not authorize semantic AI judging, inferred risk, arbitrary glob semantics, PR write access, or unrelated roadmap work.

T103 planning authority is canonical at `43aaf35c7a6b07b632e4707999cc664089f911ac` with successful post-merge `ci` `33249914994`, `skills-compat` `33249915085`, and `release` `33249915039`.

## Completed Phase B

T110–T115 expected/forbidden scope implementation is canonical at:

`b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779`

Exact candidate evidence:

- PR #34 head `e0214a75a2e65319618d9b4b4529ac280843bc86`;
- `ci` `33250895497`: SUCCESS;
- `release` `33250895562`: SUCCESS;
- no submitted reviews or review threads and no valid automated finding.

Post-merge evidence:

- `ci` `33250973190`: SUCCESS;
- `release` `33250973214`: SUCCESS.

## Active frontier

T120–T125 are the next eligible unit: implement explicit `check --risk R0|R1|R2|R3`, corresponding verification profile keys, strict selected-profile execution, missing/empty-profile fail-closed behavior, v0.1 default-command compatibility when risk is omitted, and unit/integration coverage.

Do not begin proof-output work until T120–T125 are canonical with successful exact post-merge gates.
