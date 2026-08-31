# Tasks — 008 Integration & Adoption Readiness

## Gate A — Activation

- [x] T800 Reverify live `main`, repository governance, Spec 007 closeout, README, current discoverability evidence, repository metadata, and exact post-merge gates from the Spec 007 terminal commit.
- [x] T801 Record bounded research and design constraints for repository-controlled adoption work.
- [ ] T802 Merge this Spec 008 planning authority by expected head after exact-head qualification and clean reconciliation.
- [ ] T803 Require exact post-merge `ci`, `skills-compat`, and `release` success on the resulting canonical activation commit.

## Phase B — Validated ecosystem examples

- [ ] T810 Add `examples/README.md` explaining supported example semantics and limitations.
- [ ] T811 Add a Rust `.diffcipline.toml` example.
- [ ] T812 Add a Node `.diffcipline.toml` example.
- [ ] T813 Add a Python `.diffcipline.toml` example.
- [ ] T814 Add a Go `.diffcipline.toml` example.
- [ ] T815 Add a repository test that parses the exact checked-in example files and asserts the intended verification commands.
- [ ] T816 Qualify, reconcile, expected-head merge, and exact post-merge verify the example unit.

## Phase C — Adoption and independent validation

- [ ] T820 Publish `docs/ADOPTION.md` covering Agent Skills installation, supported agent layouts, CLI, risk profiles, and the immutable GitHub Action path without vendor-endorsement language.
- [ ] T821 Publish `docs/INDEPENDENT-VALIDATION.md` with exact environment facts, commands, expected semantics, evidence-retention requirements, and `NOT RUN` rules.
- [ ] T822 Link adoption/examples/validation from `README.md` and `llms.txt` without keyword stuffing.
- [ ] T823 Qualify, reconcile, expected-head merge, and exact post-merge verify the adoption unit.

## Phase D — Metadata handoff and discovery observation

- [ ] T830 Publish `docs/GITHUB-METADATA.md` with exact recommended description/topics, source rationale, and live application status.
- [ ] T831 If the authenticated execution surface exposes a repository-metadata mutation by then, apply the exact approved values and verify live state; otherwise record `NOT APPLIED — TOOLING UNAVAILABLE` without fabricating success.
- [ ] T832 Publish a new dated post-change discovery snapshot while preserving `docs/DISCOVERABILITY.md` unchanged.
- [ ] T833 Qualify, reconcile, expected-head merge, and exact post-merge verify the metadata/discovery unit.

## Phase E — Terminal closeout

- [ ] T840 Reconcile all Spec 008 public surfaces and preserved evidence against live canonical `main`.
- [ ] T841 Qualify the exact terminal candidate and reconcile reviews, threads, comments, mergeability, and canonical main.
- [ ] T842 Merge only the expected head and require exact post-merge `ci`, `skills-compat`, and `release` success.
- [ ] T843 Record `COMPLETE_CANONICAL` only after T842 is machine-observed, then qualify that completion record under the same proof-before-done discipline.

## Ordering

Do not perform Phase B implementation until Gate A is canonical. Do not declare external metadata live from a recommendation document. Do not rewrite historical Spec 007 discovery or benchmark evidence. T843 is last and cannot be pre-recorded as complete.
