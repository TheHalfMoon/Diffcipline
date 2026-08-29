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

T120–T125 are canonical at `ef6b66a94029c102d5c798fdc8e71c68eeab61be` after PR #36 exact head `a744174a1337a94e9ac0c90d0798dae63df2da01` passed `ci` `33251448181` and `release` `33251448146`, followed by successful post-merge `ci` `33251565005` and `release` `33251564986`.

## Phase D canonical evidence

PR #38 implemented T130–T132 on exact head:

`73de8af1ae368432d0ccfb29c7db31a354bd99cd`

Exact-head evidence:

- `ci` run `33254922245`: SUCCESS, including formatting, clippy with warnings denied, locked tests, and cross-platform Diffcipline proof gates;
- `release` run `33254922255`: SUCCESS;
- no submitted review or review thread remained; automated comments contained no valid code finding.

PR #38 was squash-merged to canonical `main` as:

`fb231e21bc8e6ff0435e4056b196057ffc39d042`

Exact post-merge push evidence:

- `ci` run `33254995550`: SUCCESS;
- `release` run `33254995552`: SUCCESS.

T130–T132 are complete.

## Immediate frontier

T140–T144 are now eligible and must be implemented as one coherent GitHub Action annotation unit:

1. add an optional `risk` Action input where empty means the existing default verification path and non-empty values are strictly limited to `R0`, `R1`, `R2`, or `R3`;
2. forward a valid non-empty risk value to the same `diffcipline check --risk ...` CLI contract used locally;
3. capture deterministic proof output without changing the CLI's verdict/exit semantics;
4. write a concise Markdown proof to `$GITHUB_STEP_SUMMARY` and do not add repository write permissions, PR comments, or checkout mutation;
5. add CI dogfood that executes and validates the Action annotation path on supported runners.

Do not begin T150 until T140–T144 are merged canonical and exact post-merge gates succeed.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly during candidate evaluation, a required exact-head workflow is missing or failing, a valid review finding remains unresolved, a runtime dependency becomes necessary without demonstrated benefit, v0.1 compatibility cannot be preserved without a spec amendment, Action annotation would require repository write access or PR comments, or requested behavior requires semantic/LLM judging rather than deterministic repository evidence.
