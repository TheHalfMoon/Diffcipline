# Tasks — 002 Intent-Aware Scope

## Phase A — Canonical planning

- [x] T100 Define v0.2 intent-aware scope contract from the repository roadmap.
- [x] T101 Define deterministic path-pattern semantics and non-goals.
- [x] T102 Define risk-profile and GitHub annotation contracts.
- [x] T103 Merge Spec 002 authority chain to canonical `main` with exact-head gates.

T103 exact evidence:

- planning PR #32 exact head `2936f00420b8fa3cd8444812a05e736a2ecc0cc7` passed `ci` run `33249759142`, `skills-compat` run `33249759124`, `release` run `33249759126`, tag validation run `33249759105`, staging validation run `33249759106`, and immutable-release verifier validation run `33249759179`;
- no submitted reviews or review threads remained; automated comments contained no valid code finding;
- PR #32 was squash-merged to canonical `main` as `43aaf35c7a6b07b632e4707999cc664089f911ac`;
- exact post-merge push runs `ci` `33249914994`, `skills-compat` `33249915085`, and `release` `33249915039` all completed successfully.

## Phase B — Expected and forbidden surfaces

- [ ] T110 Extend policy parsing with `expected_files` and `forbidden_surfaces`.
- [ ] T111 Validate the supported path-pattern grammar and fail closed on unsupported wildcard placement.
- [ ] T112 Evaluate expected-file scope against every changed path.
- [ ] T113 Evaluate forbidden-surface scope against every changed path.
- [ ] T114 Add unit coverage for exact, directory-recursive, filename-suffix, invalid, expected, and forbidden matching.
- [ ] T115 Add fixture-repository integration coverage for intent PASS/FAIL behavior.

## Phase C — Risk-aware verification

- [ ] T120 Add `check --risk R0|R1|R2|R3` parsing.
- [ ] T121 Add R0–R3 verification profile policy keys.
- [ ] T122 Select only the explicitly requested risk profile when `--risk` is supplied.
- [ ] T123 Fail closed when an explicitly requested risk profile is absent or empty.
- [ ] T124 Preserve v0.1 default `commands` behavior when `--risk` is omitted.
- [ ] T125 Add unit and integration coverage for profile selection and missing-profile failure.

## Phase D — Proof output

- [ ] T130 Add scope and risk evidence to human proof output.
- [ ] T131 Add risk, intent contract, scope violations, and verification states to JSON output.
- [ ] T132 Add regression tests for structured output escaping and compatibility.

## Phase E — GitHub Action annotation

- [ ] T140 Add optional Action `risk` input and strict validation.
- [ ] T141 Forward risk to the same CLI proof contract used locally.
- [ ] T142 Preserve CLI exit semantics while capturing deterministic proof output.
- [ ] T143 Write a concise Markdown proof to `$GITHUB_STEP_SUMMARY` without write permissions or PR comments.
- [ ] T144 Add CI dogfood coverage for the Action annotation path.

## Phase F — v0.2 canonical closeout

- [ ] T150 Update README with implemented v0.2 behavior only.
- [ ] T151 Reconcile `specs/CURRENT.md`, tasks, and execution frontier with exact canonical evidence.
- [ ] T152 Pass exact-head Rust, dogfood, skills compatibility, and release-candidate gates on the final v0.2 candidate.
- [ ] T153 Merge final v0.2 evidence to canonical `main` and verify post-merge gates.
- [ ] T154 Mark Spec 002 `COMPLETE_CANONICAL` only after T153 is machine-observed.

## Ordering

T103 gates all implementation. Phase B precedes Phase C because risk profiles must not obscure intent-scope failures. Phase D follows both core contracts. Phase E consumes the stable CLI proof shape. Phase F starts only after T110–T144 are canonical.
