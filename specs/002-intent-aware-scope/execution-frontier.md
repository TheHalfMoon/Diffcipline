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

## Spec 002 completed implementation

- T103 planning authority is canonical at `43aaf35c7a6b07b632e4707999cc664089f911ac`.
- T110–T115 intent-scope implementation is canonical at `b35ae01f7a83964ed1c5ab2431f8cf00f4fe3779`.
- T120–T125 risk-aware verification is canonical at `ef6b66a94029c102d5c798fdc8e71c68eeab61be`.
- T130–T132 proof output is canonical at `fb231e21bc8e6ff0435e4056b196057ffc39d042`.
- T140–T144 GitHub Action annotation is canonical at `c059fc76e4d836e7f9e10ce4bb0465428791ed40`.

## Phase F closeout evidence

PR #41 exact head:

`6e10466fb28687aba48ca363135dbff5253bd1db`

Exact-head gates:

- `ci` `33255846426`: SUCCESS, including Rust and default/risk-aware/invalid-risk Action dogfood across Ubuntu, macOS, and Windows;
- `skills-compat` `33255846412`: SUCCESS across all six supported installer targets;
- `release` `33255846514`: SUCCESS;
- `tag-v0.1.0` validation `33255846439`: SUCCESS;
- `stage-v0.1.0-release` validation `33255846449`: SUCCESS;
- `verify-v0.1.0-release` validation `33255846466`: SUCCESS;
- no submitted reviews or review threads remained; Qodo and CodeRabbit top-level notices contained no code finding;
- canonical `main` remained at candidate base `c059fc76e4d836e7f9e10ce4bb0465428791ed40` until merge.

PR #41 was squash-merged as canonical commit:

`246cac79d8c1a2774b8fa7aad60ccb9efb4b40cd`

Canonical tree:

`ca9bfabdb3e4ebccae2781862237344e2a9f1531`

Exact post-merge push evidence:

- `ci` `33255959784`: SUCCESS;
- `skills-compat` `33255959806`: SUCCESS;
- `release` `33255959768`: SUCCESS.

T153 was machine-observed before the T154 completion record was authored.

## Spec 002 terminal state

T150–T154 are complete in the task ledger and this evidence change records Spec 002 as `COMPLETE_CANONICAL`.

There is no remaining Spec 002 implementation or closeout task. The `COMPLETE_CANONICAL` status becomes canonical only when this evidence change itself is merged to `main` and the resulting post-merge state is verified.

No `v0.2.0` tag is authorized. Do not create, move, delete, or replace one under Spec 002.

Further roadmap work, including v0.3 Evidence benchmark, must proceed under a separate canonical authority chain. Do not extend Spec 002 to authorize v0.3 implicitly.

## Stop conditions

Stop rather than weaken governance if this completion evidence does not pass every exact-head workflow triggered by its paths, canonical `main` changes unexpectedly before merge, a valid review finding remains unresolved, the expected-head merge condition fails, post-merge gates do not succeed, or a future phase lacks its own canonical authority chain.
