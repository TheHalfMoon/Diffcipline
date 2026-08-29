# Execution frontier — Spec 002

Live GitHub/repository truth overrides this snapshot.

## Canonical authority chain

Read in this order before acting:

1. `AGENTS.md`
2. `CONSTITUTION.md`
3. `specs/CURRENT.md`
4. `specs/002-intent-aware-scope/spec.md`
5. `specs/002-intent-aware-scope/plan.md`
6. `specs/002-intent-aware-scope/tasks.md`
7. this file
8. `.diffcipline.toml`
9. `crates/diffcipline-cli/src/main.rs`
10. `crates/diffcipline-cli/tests/cli.rs`
11. `action.yml`
12. `.github/workflows/ci.yml`

## Starting canonical state

Spec 001 / v0.1 reached `COMPLETE_CANONICAL` at canonical `main`:

`d74ed5f8789fb255e24f124e3283939cdc080cd0`

Published immutable `v0.1.0` remains fixed at:

`ab434ae114b5f11ea9eb882bf572831dc7634531`

Do not move or replace that tag or mutate Release ID `378936458`.

The v0.1 benchmark conclusion remains canonical and must not be rewritten: all four arms scored `1/6`, all changed zero files, Diffcipline was slowest by observed wall-clock time, and no correctness advantage is supported.

## Why Spec 002 is authorized

The canonical README roadmap explicitly defines `v0.2 — Intent-aware scope` with:

- proof contract for expected files and forbidden surfaces;
- risk-aware verification profiles;
- GitHub PR annotation.

The user has authorized ordinary repository work through the canonical roadmap. This spec narrows that roadmap into deterministic acceptance criteria; it does not add unrelated product scope.

## Immediate frontier

T103 is first: merge this planning authority chain through a reviewed PR with exact-head repository gates. No implementation task is eligible until T103 is canonical.

After T103, execute in order:

1. T110–T115 expected/forbidden scope;
2. T120–T125 risk-aware verification;
3. T130–T132 proof output;
4. T140–T144 GitHub Action annotation;
5. T150–T154 canonical closeout.

## Stop conditions

Stop rather than weaken governance if:

- canonical `main` changes unexpectedly while a candidate is being evaluated;
- an exact-head required workflow is missing or failing;
- a valid review finding remains unresolved;
- implementation would require a runtime dependency without a demonstrated necessity;
- backward compatibility with v0.1 policy behavior cannot be preserved without an explicit spec amendment;
- the requested behavior requires semantic/LLM judging rather than deterministic repository evidence.
