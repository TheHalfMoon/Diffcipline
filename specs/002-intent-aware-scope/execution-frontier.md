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

Spec 001 / v0.1 reached `COMPLETE_CANONICAL` at `d74ed5f8789fb255e24f124e3283939cdc080cd0`. Published immutable `v0.1.0` remains fixed at `ab434ae114b5f11ea9eb882bf572831dc7634531`; do not move or replace that tag or mutate Release ID `378936458`.

The v0.1 benchmark conclusion remains canonical and must not be rewritten: all four arms scored `1/6`, all changed zero files, Diffcipline was slowest by observed wall-clock time, and no correctness advantage is supported.

## Spec 002 planning authority

PR #32 planning head `2936f00420b8fa3cd8444812a05e736a2ecc0cc7` passed all six exact-head workflows and merged canonical as `43aaf35c7a6b07b632e4707999cc664089f911ac`. Post-merge `ci` `33249914994`, `skills-compat` `33249915085`, and `release` `33249915039` all succeeded. T103 is complete.

## Phase B canonical evidence

PR #34 implemented T110–T115 on exact head:

`e0214a75a2e65319618d9b4b4529ac280843bc86`

Exact-head evidence:

- `ci` run `33250895497`: SUCCESS, including formatting, clippy with warnings denied, locked tests, and cross-platform proof gates;
- `release` run `33250895562`: SUCCESS;
- no submitted review or review thread remained; automated comments contained no valid code finding.

PR #34 was squash-merged to canonical `main` as:

`b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779`

Exact post-merge push evidence:

- `ci` run `33250973190`: SUCCESS;
- `release` run `33250973214`: SUCCESS.

T110–T115 are therefore complete.

## Immediate frontier

T120–T125 are now eligible and must be implemented as one coherent risk-profile unit:

1. accept only explicit `check --risk R0|R1|R2|R3` values;
2. parse `r0_commands`, `r1_commands`, `r2_commands`, and `r3_commands` under `[verification]`;
3. execute only the explicitly selected profile when risk is supplied;
4. fail closed with execution/configuration error if that selected profile is absent or empty;
5. preserve the existing `commands` path exactly when `--risk` is omitted;
6. cover selection, invalid risk, absent/empty profile, and backward compatibility in unit and fixture-repository integration tests.

Do not begin T130 until T120–T125 are merged canonical and exact post-merge gates succeed.

## Stop conditions

Stop rather than weaken governance if canonical `main` changes unexpectedly during candidate evaluation, an exact-head required workflow is missing or failing, a valid review finding remains unresolved, a runtime dependency becomes necessary without demonstrated benefit, v0.1 compatibility cannot be preserved without a spec amendment, or requested behavior requires semantic/LLM judging rather than deterministic repository evidence.
