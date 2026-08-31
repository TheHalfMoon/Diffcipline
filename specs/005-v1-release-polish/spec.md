# Spec 005 — v1 Release Polish

## Status

`PLANNING_CANDIDATE`

This specification becomes implementation authority only after its planning record is merged to canonical `main` and the required exact post-merge gates succeed on that resulting canonical SHA.

Spec 004 remains `COMPLETE_CANONICAL`. This specification does not reopen, amend, or reinterpret Spec 004.

## Authority and purpose

Canonical Spec 004 completed the v1 Universal Engineering Governor capability set while preserving a separate public-release authority boundary. Before any public `v1.0.0` publication is considered, Diffcipline needs one deliberately small release-polish unit derived from live repository truth.

The unit is limited to:

1. fixing the verified hand-written TOML array parsing defect that prevents quoted verification commands containing commas from being expressed correctly;
2. documenting the exact enterprise-enforcement boundary around `--enterprise-policy <path>`;
3. reviewing repository hygiene without inventing process bureaucracy.

A public v1 tag, draft release, or published release remains outside this specification.

## Parser contract

The dependency-free policy parser must accept comma characters inside quoted array string elements instead of treating those commas as element separators.

The change must remain surgical and preserve existing policy version 1 behavior:

- array elements remain quoted strings;
- commas separate elements only when outside a quoted string;
- existing escaped quote and escaped backslash handling remains supported;
- malformed arrays, malformed quoted elements, unsupported policy keys/sections, and unsupported policy versions continue to fail closed;
- `expected_files`, `forbidden_surfaces`, default verification commands, and R0/R1/R2/R3 command arrays share the same corrected parsing behavior;
- no runtime dependency is added unless repository evidence proves the standard library cannot support a safe narrow fix.

Focused regression coverage must include at least one verification command whose quoted value contains a comma and negative coverage that preserves fail-closed parsing.

## Enterprise-enforcement documentation contract

Documentation must state explicitly that `--enterprise-policy <path>` activates the monotonic enterprise layer only when that argument is supplied.

A repository-controlled workflow can omit that argument. Therefore a genuinely mandatory organizational baseline requires organization-controlled enforcement such as a required workflow, reusable workflow, ruleset-integrated workflow, or equivalent externally controlled CI policy that supplies the enterprise policy input.

The local-file mechanism is not an identity, RBAC, credential-distribution, or remote policy-control system. This specification must not add such a system.

## Repository-hygiene contract

Review live repository metadata and contributor entry surfaces. Improve only low-cost, clearly useful hygiene that is available through authorized repository tooling.

Repository description/topics are desirable where supported. New issue templates are optional and must not be added merely to create process. Metadata limitations in the available execution tooling are not a product-release blocker.

## Preservation and non-goals

Preserve:

- dependency-free Rust CLI core;
- PASS / REVIEW / FAIL / usage exit semantics 0 / 1 / 2 / 64;
- stable proof schema `diffcipline.proof/v1` / `1.0`;
- monotonic enterprise/repository policy layering;
- Agent Skills portability and GitHub Action behavior;
- signed release-candidate contract and all immutable historical release evidence;
- frozen v0.3 benchmark evidence and its negative/null findings.

Do not add:

- new agent adapters;
- dashboards, SaaS, telemetry, AI scoring, RBAC, or remote policy distribution;
- a new benchmark before public v1;
- release-binary consumption changes for the GitHub Action;
- architecture redesign or parser rewrite unrelated to the verified defect.

## Qualification

The implementation candidate must:

1. stay within `.diffcipline.toml` repository policy;
2. pass focused parser regression tests plus the repository-required Rust checks;
3. pass exact-head `ci`, `skills-compat`, and `release` qualification on one final candidate head;
4. preserve historical immutable-release guards and release workflow behavior;
5. reconcile submitted reviews, inline threads, technical PR comments, mergeability, and canonical `main` immediately before merge;
6. merge only with an expected-head SHA guard;
7. pass exact post-merge `ci`, `skills-compat`, and `release` gates on the resulting canonical SHA.

## Completion and next authority boundary

Spec 005 is complete only after the parser fix, regression coverage, enterprise-enforcement documentation, hygiene review, exact-head qualification, expected-head merge, and exact post-merge verification are canonical and a terminal completion record is merged.

Only after Spec 005 is `COMPLETE_CANONICAL` may a separate canonical publication specification authorize version `1.0.0`, tag `v1.0.0`, release staging/publication, and published-asset verification.
