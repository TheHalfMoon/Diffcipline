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

T130–T132 are canonical at `fb231e21bc8e6ff0435e4056b196057ffc39d042` after PR #38 exact head `73de8af1ae368432d0ccfb29c7db31a354bd99cd` passed `ci` `33254922245` and `release` `33254922255`, followed by successful post-merge `ci` `33254995550` and `release` `33254995552`.

## Phase E canonical evidence

PR #40 implemented T140–T144 on exact head:

`ec87a121ddf1958f9b57f300699da0457e219b43`

Exact-head evidence:

- `ci` run `33255469452`: SUCCESS;
- Rust formatting, clippy with warnings denied, and locked tests succeeded;
- the default Action proof path succeeded on Ubuntu, macOS, and Windows;
- an isolated fixture exercised explicit `risk: R0` annotation successfully on Ubuntu, macOS, and Windows;
- invalid `risk: R4` was rejected successfully on Ubuntu, macOS, and Windows;
- no submitted reviews or review threads remained;
- Qodo and CodeRabbit top-level comments contained no code finding.

PR #40 was squash-merged to canonical `main` as:

`c059fc76e4d836e7f9e10ce4bb0465428791ed40`

Exact post-merge push evidence:

- `ci` run `33255652466`: SUCCESS with Rust and default/risk-aware Action dogfood across Ubuntu, macOS, and Windows.

`skills-compat` and `release` were not triggered by the Phase E implementation paths. T152 therefore requires both on the final v0.2 candidate rather than treating missing runs as PASS.

T140–T144 are complete.

## Immediate frontier

T150–T154 are the only remaining tasks.

The closeout must proceed in this order:

1. T150: update README with only the v0.2 behavior already implemented and machine-observed;
2. T151: reconcile `specs/CURRENT.md`, `tasks.md`, and this frontier with the exact Phase E canonical evidence above;
3. T152: on the resulting exact candidate head, require successful `ci` (Rust plus Action dogfood), `skills-compat`, and `release` workflows, plus any repository-governance validation workflows triggered by the changed paths;
4. before merge, verify the exact head is unchanged, canonical `main` is unchanged from the candidate base, mergeability is clean, and no valid review finding remains;
5. T153: squash-merge only that verified head, then verify canonical `main` and all triggered post-merge gates on the exact merge commit;
6. T154: only after T153 is machine-observed, record the exact closeout evidence and set Spec 002 to `COMPLETE_CANONICAL` in a separate canonical evidence change; do not claim completion before that evidence change itself is merged and its post-merge state is verified.

No `v0.2.0` tag is authorized by Spec 002. Do not create, move, delete, or replace a v0.2 tag during this closeout.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly during candidate evaluation, a required exact-head workflow is missing or failing, a valid review finding remains unresolved, a runtime dependency becomes necessary without demonstrated benefit, v0.1 compatibility cannot be preserved without a spec amendment, Action annotation would require repository write access or PR comments, requested behavior requires semantic/LLM judging rather than deterministic repository evidence, or any completion claim would require treating an untriggered workflow as PASS.
