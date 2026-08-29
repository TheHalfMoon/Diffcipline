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

## Preserved v0.1 truth

Spec 001 / v0.1 is `COMPLETE_CANONICAL` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`. Published immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`. Its benchmark remains unfavorable and unchanged: all four arms scored `1/6`, all changed zero files, Diffcipline was slowest, and no correctness advantage is supported.

## Spec 002 planning authority

T103 is canonical at `43aaf35c7a6b07b632e4707999cc664089f911ac` with successful post-merge `ci` `33249914994`, `skills-compat` `33249915085`, and `release` `33249915039`.

## Phase B canonical evidence

T110–T115 are canonical at `b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779` after PR #34 exact head `e0214a75a2e65319618d9b4b4529ac280843bc86` passed `ci` `33250895497` and `release` `33250895562`, followed by successful post-merge `ci` `33250973190` and `release` `33250973214`.

## Phase C canonical evidence

PR #36 implemented T120–T125 on exact head:

`a744174a1337a94e9ac0c90d0798dae63df2da01`

Exact-head evidence:

- `ci` run `33251448181`: SUCCESS;
- `release` run `33251448146`: SUCCESS;
- no submitted review or review thread remained.

PR #36 was squash-merged to canonical `main` as:

`ef6b66a94029c102d5c798fdc8e71c68eeab61be`

Exact post-merge push evidence:

- `ci` run `33251565005`: SUCCESS;
- `release` run `33251564986`: SUCCESS.

T120–T125 are complete.

## Immediate frontier

T130–T132 are now eligible and must be implemented as one coherent proof-output unit:

1. human proof explicitly identifies selected risk or default verification mode;
2. human proof identifies configured expected and forbidden contracts and resulting scope state;
3. JSON adds `risk`, `expected_files`, `forbidden_surfaces`, `scope_violations`, and verification command/state entries while preserving existing fields;
4. JSON remains dependency-free and correctly escapes strings;
5. existing v0.1 callers that consume existing fields remain compatible.

Do not begin T140 until T130–T132 are merged canonical and exact post-merge gates succeed.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly during candidate evaluation, a required exact-head workflow is missing or failing, a valid review finding remains unresolved, a runtime dependency becomes necessary without demonstrated benefit, v0.1 compatibility cannot be preserved without a spec amendment, or requested behavior requires semantic/LLM judging rather than deterministic repository evidence.
