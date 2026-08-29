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

## Spec 002 authority

The canonical README roadmap explicitly defines `v0.2 — Intent-aware scope` with:

- proof contract for expected files and forbidden surfaces;
- risk-aware verification profiles;
- GitHub PR annotation.

PR #32 narrowed only that roadmap scope into the Spec 002 authority chain. Exact planning head:

`2936f00420b8fa3cd8444812a05e736a2ecc0cc7`

All six exact-head workflows succeeded:

- `ci` `33249759142`;
- `skills-compat` `33249759124`;
- `release` `33249759126`;
- `tag-v0.1.0` validation `33249759105`;
- `stage-v0.1.0-release` validation `33249759106`;
- `verify-v0.1.0-release` validation `33249759179`.

No valid review finding remained. PR #32 was squash-merged to canonical `main` as:

`43aaf35c7a6b07b632e4707999cc664089f911ac`

Post-merge exact push gates:

- `ci` `33249914994`: SUCCESS;
- `skills-compat` `33249915085`: SUCCESS;
- `release` `33249915039`: SUCCESS.

T103 is therefore complete.

## Immediate frontier

T110–T115 are now eligible and must be executed as one coherent Phase B unit:

1. extend policy parsing with optional `expected_files` and `forbidden_surfaces`;
2. validate only the documented deterministic matcher grammar;
3. evaluate expected-file constraints against every changed repository-relative path;
4. evaluate forbidden-surface constraints against every changed repository-relative path;
5. add unit tests for exact, recursive-directory, suffix, invalid, expected, and forbidden behavior;
6. add fixture-repository integration coverage for PASS/FAIL behavior.

For intent evaluation, treat tracked diff paths and untracked repository-relative paths as changed paths. Preserve the existing independent untracked-file policy decision as well.

Do not start T120 until T110–T115 are merged canonical and their post-merge exact gates are successful.

## Stop conditions

Stop rather than weaken governance if:

- canonical `main` changes unexpectedly while a candidate is being evaluated;
- an exact-head required workflow is missing or failing;
- a valid review finding remains unresolved;
- implementation would require a runtime dependency without a demonstrated necessity;
- backward compatibility with v0.1 policy behavior cannot be preserved without an explicit spec amendment;
- the requested behavior requires semantic/LLM judging rather than deterministic repository evidence.
