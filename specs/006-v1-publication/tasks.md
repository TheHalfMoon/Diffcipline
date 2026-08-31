# Tasks — 006 v1 Public Publication

## Phase A — Canonical publication authority

- [x] T600 Derive public-v1 publication scope from terminal Spec 005 and live release truth.
- [x] T601 Define exact `1.0.0` version, guarded tag, signed-candidate recovery staging, immutable publication, and published-release verification contracts.
- [x] T602 Preserve v0.1 immutability, dependency-free product behavior, signed-candidate semantics, and the external administrator immutability prerequisite.
- [x] T603 Merge Spec 006 planning authority to canonical `main` and verify exact post-merge `ci`, `skills-compat`, and `release` gates. Evidence: PR #69 exact head `2d633052e990b5ba852495eecb49d1b2a5d25ab6`; exact-head `ci` `33399447630`, `skills-compat` `33399447639`, `release` `33399447636`, `tag-v0.1.0` `33399447689`, `stage-v0.1.0-release` `33399447618`, and `verify-v0.1.0-release` `33399447643` all completed `SUCCESS`; expected-head squash merge produced canonical `ccdaa65b7ff48775ffa72e20f8d2dbf024ee3577`; exact post-merge `ci` `33399584260`, `skills-compat` `33399584290`, and `release` `33399584278` all completed `SUCCESS`, including three native builds, deterministic checksum closure, signed Sigstore provenance, and attestation-subject verification.

## Phase B — Publication implementation

- [ ] T610 Set crate and lockfile version to `1.0.0`; update changelog/release documentation without adding product behavior. Candidate progress: crate, lockfile, and changelog are updated on the current implementation branch; detailed release documentation remains for the staging/verifier unit.
- [x] T611 Add guarded repository-native `v1.0.0` tag authority with exact canonical-SHA and exact-SHA workflow qualification. The current candidate also preserves historical v0.1 PR validation by resolving the immutable v0.1 version from its fixed tag instead of the current crate version.
- [ ] T612 Add `v1.0.0` recovery staging that reuses the unique exact canonical `signed-release-candidate`, verifies its five-file closure, and creates a byte-verified draft only.
- [ ] T613 Add immutable published-release verification for `v1.0.0` covering tag lineage, version, immutable state, release attestation, checksums, binary attestations, and every release asset.
- [ ] T614 Qualify one exact publication-implementation head with `ci`, `skills-compat`, `release`, all historical v0.1 guards, review/thread/comment reconciliation, mergeability, and canonical-main reconciliation.
- [ ] T615 Merge only the exact qualified head and verify exact post-merge `ci`, `skills-compat`, and `release` on the resulting canonical release commit.

## Phase C — Guarded tag and verified draft

- [ ] T620 Trigger the guarded owner-only `v1.0.0` tag authority for the exact canonical release commit and verify the immutable tag target.
- [ ] T621 Trigger owner-only recovery staging for that same SHA; verify the exact signed canonical candidate and byte-identical five-asset draft.
- [ ] T622 Record tag/staging evidence on canonical `main` without changing the release target.

## Phase D — Immutable publication and terminal verification

- [ ] T630 Require independent repository-administrator confirmation that GitHub release immutability is enabled.
- [ ] T631 Publish the already-verified draft only through the administrative release surface.
- [ ] T632 Require the `release.published` verifier to succeed for immutable `v1.0.0` and preserve durable verification evidence.
- [ ] T633 Record terminal Spec 006 `COMPLETE_CANONICAL` only after T632 is machine-observed and the terminal record itself becomes canonical with required post-merge gates.

## Ordering

T603 gates publication implementation. T615 gates tag creation. T620 gates staging. T621 gates the administrative publication prerequisite. T632 gates terminal closeout.

No task authorizes bypassing the administrator immutability confirmation, replacing an existing tag or release, or publishing a draft through repository automation.
