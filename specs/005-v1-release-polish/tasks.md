# Tasks — 005 v1 Release Polish

## Phase A — Canonical planning authority

- [x] T500 Derive the narrow pre-v1 release-polish scope from terminal Spec 004 and live repository truth.
- [x] T501 Define parser, enterprise-enforcement documentation, hygiene, preservation, and non-goal contracts.
- [x] T502 Define exact-head, review, expected-head merge, and post-merge qualification requirements while preserving the separate public-release boundary.
- [ ] T503 Merge Spec 005 planning authority to canonical `main` and verify exact post-merge `ci`, `skills-compat`, and `release` gates.

## Phase B — Surgical parser and documentation polish

- [ ] T510 Reproduce and record the current failure for a quoted verification command containing a comma.
- [ ] T511 Replace simplistic array comma splitting with a surgical quote-aware, dependency-free separator scan.
- [ ] T512 Add focused positive and fail-closed regression tests for quoted arrays, including comma-containing verification commands.
- [ ] T513 Document that enterprise layering is active only when `--enterprise-policy <path>` is supplied and that mandatory organizational enforcement requires an externally controlled required CI path.
- [ ] T514 Review repository description/topics and issue-entry hygiene; apply only supported low-cost improvements and record any tooling limitation without blocking release.
- [ ] T515 Qualify one exact implementation head with focused Rust tests plus `ci`, `skills-compat`, and `release`; reconcile reviews, threads, technical comments, mergeability, and canonical `main`.
- [ ] T516 Merge the implementation candidate only with its expected head SHA and verify exact post-merge `ci`, `skills-compat`, and `release` success.

## Phase C — Canonical closeout

- [ ] T520 Record Spec 005 `COMPLETE_CANONICAL` only after T516 evidence is machine-observed.
- [ ] T521 Merge the terminal completion record with an expected-head guard and verify its required exact post-merge gates.

## Ordering

T503 gates all implementation. T516 gates terminal closeout. T521 closes Spec 005.

No task in this specification authorizes version `1.0.0`, tag `v1.0.0`, a draft release, publication, or published-asset verification. Those require a separate later canonical publication specification.
