# Spec 005 — v1 Release Polish

## Status

`COMPLETE_CANONICAL`

This terminal status is effective only after this completion record is merged to canonical `main` and the required exact post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA. Until those conditions hold, this branch is only the terminal completion candidate.

Spec 004 remains `COMPLETE_CANONICAL`. Spec 005 did not reopen, amend, or reinterpret Spec 004.

## Authority and purpose

Canonical Spec 004 completed the v1 Universal Engineering Governor capability set while preserving a separate public-release authority boundary. Spec 005 authorized one deliberately small release-polish unit derived from live repository truth.

The completed unit was limited to:

1. correcting the verified hand-written TOML array parsing defect that prevented quoted verification commands containing commas from being expressed correctly;
2. documenting the exact enterprise-enforcement boundary around `--enterprise-policy <path>`;
3. reviewing repository hygiene without inventing process bureaucracy.

A public v1 tag, draft release, or published release remains outside this specification.

## Parser contract

The dependency-free policy parser accepts comma characters inside quoted array string elements instead of treating those commas as element separators.

The surgical standard-library implementation preserves policy version 1 behavior:

- array elements remain quoted strings;
- commas separate elements only when outside a quoted string;
- existing escaped quote and escaped backslash handling remains supported;
- malformed arrays, malformed quoted elements, unsupported policy keys/sections, and unsupported policy versions continue to fail closed;
- `expected_files`, `forbidden_surfaces`, default verification commands, and R0/R1/R2/R3 command arrays share the corrected parsing behavior;
- no runtime dependency was added.

Focused regression coverage preserves at least one verification command whose quoted value contains a comma and negative coverage for malformed quoted arrays.

## Enterprise-enforcement documentation contract

Documentation states explicitly that `--enterprise-policy <path>` activates the monotonic enterprise layer only when that argument is supplied.

A repository-controlled workflow can omit that argument. Therefore a genuinely mandatory organizational baseline requires organization-controlled enforcement such as a required workflow, reusable workflow, ruleset-integrated workflow, or equivalent externally controlled CI policy that supplies the enterprise policy input.

The local-file mechanism is not an identity, RBAC, credential-distribution, or remote policy-control system. Spec 005 added no such system.

## Repository-hygiene review

Live repository review found an empty GitHub repository description and no `.github/ISSUE_TEMPLATE` directory. The authorized repository tooling available to this execution did not support mutating description/topics. Spec 005 treated that tooling limitation as non-blocking and did not add process-only issue templates merely to create ceremony.

## Preservation

Spec 005 preserved:

- dependency-free Rust CLI core;
- PASS / REVIEW / FAIL / usage exit semantics 0 / 1 / 2 / 64;
- stable proof schema `diffcipline.proof/v1` / `1.0`;
- monotonic enterprise/repository policy layering;
- Agent Skills portability and GitHub Action behavior;
- signed release-candidate contract and all immutable historical release evidence;
- frozen v0.3 benchmark evidence and its negative/null findings.

It did not add new agent adapters, dashboards, SaaS, telemetry, AI scoring, RBAC, remote policy distribution, a new benchmark, release-binary Action changes, or unrelated architecture work.

## Qualification evidence

The final implementation candidate was exact head `d95bbe4a17a3ad5bd779558be0ee3b09a2dda0b9` on PR #67.

On that exact head:

- `ci` `33397933733` completed `SUCCESS`;
- `skills-compat` `33397933822` completed `SUCCESS`;
- `release` `33397933738` completed `SUCCESS`;
- historical immutable-release guards `verify-v0.1.0-release` `33397933732`, `tag-v0.1.0` `33397933764`, and `stage-v0.1.0-release` `33397933755` completed `SUCCESS`;
- no submitted reviews or inline review threads remained;
- the only PR comments were nontechnical Qodo billing and CodeRabbit skipped-review notices;
- canonical `main` remained exactly `3e7abe3ca7c95fe327ef04ccb46fae89286ab8bc` immediately before merge;
- the PR remained mergeable and was merged with expected head `d95bbe4a17a3ad5bd779558be0ee3b09a2dda0b9`.

The expected-head squash merge produced canonical implementation SHA `035035485ced320b5184c8245f0fd1558d68ed60`.

On that exact post-merge SHA:

- `ci` `33398236413` completed `SUCCESS`;
- `skills-compat` `33398236347` completed `SUCCESS`;
- `release` `33398236441` completed `SUCCESS`;
- the trusted release path built locked Linux, macOS, and Windows binaries, generated and verified the SHA-256 manifest, created signed Sigstore provenance, preserved the attestation bundle, and verified every native-binary subject;
- `stage GitHub release draft` was intentionally skipped because no public v1 tag was authorized.

## Completion and next authority boundary

Spec 005 has no remaining implementation task after the terminal completion record becomes canonical with successful required post-merge gates.

Only after this `COMPLETE_CANONICAL` status becomes effective may a separate canonical publication specification authorize version `1.0.0`, tag `v1.0.0`, release staging/publication, and published-asset verification.
