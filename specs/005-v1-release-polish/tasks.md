# Tasks — 005 v1 Release Polish

## Phase A — Canonical planning authority

- [x] T500 Derive the narrow pre-v1 release-polish scope from terminal Spec 004 and live repository truth.
- [x] T501 Define parser, enterprise-enforcement documentation, hygiene, preservation, and non-goal contracts.
- [x] T502 Define exact-head, review, expected-head merge, and post-merge qualification requirements while preserving the separate public-release boundary.
- [x] T503 Merge Spec 005 planning authority to canonical `main` and verify exact post-merge `ci`, `skills-compat`, and `release` gates. Evidence: planning head `d3c7019360fc8a28369bd6515f5546c6902968ab`; PR #66 exact-head `ci` `33396961978`, `skills-compat` `33396962159`, `release` `33396962148`; canonical merge `3e7abe3ca7c95fe327ef04ccb46fae89286ab8bc`; post-merge `ci` `33397182736`, `skills-compat` `33397182730`, `release` `33397182737` — all `SUCCESS`.

## Phase B — Surgical parser and documentation polish

- [x] T510 Reproduce and record the current failure for a quoted verification command containing a comma. Evidence: red regression head `c20a81b9bf47ac3b7da55db6300385b8e25e706f`; `ci` `33397575574` reached and failed `cargo test --workspace --all-targets --locked` on Ubuntu and macOS after format and clippy passed, while the dogfood proof gate also failed on the same head.
- [x] T511 Replace simplistic array comma splitting with a surgical quote-aware, dependency-free separator scan. Implementation commit: `a645f717e21d6465b8a0698ab04728972e2c02dd`.
- [x] T512 Add focused positive and fail-closed regression tests for quoted arrays, including comma-containing verification commands. Coverage was introduced by the T510 red regression and retained for final qualification.
- [x] T513 Document that enterprise layering is active only when `--enterprise-policy <path>` is supplied and that mandatory organizational enforcement requires an externally controlled required CI path. Proof-contract documentation commit: `efba132f2954807a0a839463df2317831a994c06`.
- [x] T514 Review repository description/topics and issue-entry hygiene; apply only supported low-cost improvements and record any tooling limitation without blocking release. Live review found an empty repository description and no `.github/ISSUE_TEMPLATE` directory; authorized repository tooling available to this execution cannot mutate description/topics, so no process-only template was added and the metadata limitation is recorded as non-blocking.
- [ ] T515 Qualify one exact implementation head with focused Rust tests plus `ci`, `skills-compat`, and `release`; reconcile reviews, threads, technical comments, mergeability, and canonical `main`.
- [ ] T516 Merge the implementation candidate only with its expected head SHA and verify exact post-merge `ci`, `skills-compat`, and `release` success.

## Phase C — Canonical closeout

- [ ] T520 Record Spec 005 `COMPLETE_CANONICAL` only after T516 evidence is machine-observed.
- [ ] T521 Merge the terminal completion record with an expected-head guard and verify its required exact post-merge gates.

## Ordering

T503 gates all implementation. T516 gates terminal closeout. T521 closes Spec 005.

No task in this specification authorizes version `1.0.0`, tag `v1.0.0`, a draft release, publication, or published-asset verification. Those require a separate later canonical publication specification.
