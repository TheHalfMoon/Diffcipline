# Current specification

Active: [`002-intent-aware-scope`](002-intent-aware-scope/spec.md)

Status: `PLANNING_CANDIDATE`

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

## Active gate

T103 is the only eligible task until this planning candidate is merged to canonical `main` with exact-head repository gates. `PLANNING_CANDIDATE` must not be represented as canonical Spec 002 authority before that merge.
