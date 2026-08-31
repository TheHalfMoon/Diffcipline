# Tasks — 008 Integration & Adoption Readiness

## Gate A — Activation

- [x] T800 Reverify live `main`, repository governance, Spec 007 closeout, README, current discoverability evidence, repository metadata, and exact post-merge gates from the Spec 007 terminal commit.
- [x] T801 Record bounded research and design constraints for repository-controlled adoption work.
- [x] T802 Merge the Spec 008 planning authority by expected head after exact-head qualification and clean reconciliation. PR #88 exact head `693e1bc81af394e77c96e7a373be8118ca301bb3`; all nine pull-request workflows `SUCCESS`; no submitted reviews or inline threads; only non-substantive automated comments; canonical `main` remained `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9` before merge.
- [x] T803 Require exact post-merge `ci`, `skills-compat`, and `release` success. Canonical activation `60fb2643c2710f0e262c2b007ca4192f039d30c3`; `ci` `33439088987`, `skills-compat` `33439088957`, and `release` `33439088976` all `SUCCESS`.

## Phase B — Validated ecosystem examples

- [x] T810 Add `examples/README.md` explaining supported example semantics and limitations.
- [x] T811 Add a Rust `.diffcipline.toml` example.
- [x] T812 Add a Node `.diffcipline.toml` example.
- [x] T813 Add a Python `.diffcipline.toml` example.
- [x] T814 Add a Go `.diffcipline.toml` example.
- [x] T815 Add a repository integration test that loads the exact checked-in example files through the CLI contract and asserts their intended verification commands are exposed as `NOT RUN` without `--run`.
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

Gate A is canonical. Phase B content is only an implementation candidate until T816 completes. Do not declare external metadata live from a recommendation document. Do not rewrite historical Spec 007 discovery or benchmark evidence. T843 is last and cannot be pre-recorded as complete.
