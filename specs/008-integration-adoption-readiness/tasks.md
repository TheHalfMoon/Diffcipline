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
- [x] T815 Add a repository integration test that loads the exact checked-in example files through the CLI contract and asserts the intended verification commands are exposed as `NOT RUN` without `--run`.
- [x] T816 Qualify, reconcile, expected-head merge, and exact post-merge verify the example unit. PR #89 exact head `015c0196b646d7eafd231de6607e57d5d633f23a`; all nine pull-request workflows `SUCCESS`; canonical Phase B `b31d891427b5ddbd43fc24c2ad2e1dc7adc6bd39`; post-merge `ci` `33440059674`, `skills-compat` `33440059726`, and `release` `33440059755` all `SUCCESS`.

## Phase C — Adoption and independent validation

- [x] T820 Publish `docs/ADOPTION.md` covering Agent Skills installation, qualified installer layouts, CLI, risk profiles, and immutable GitHub Action usage without vendor-endorsement language.
- [x] T821 Publish `docs/INDEPENDENT-VALIDATION.md` with fixed release identity, exact release/attestation/CLI checks, evidence-retention requirements, and explicit `NOT RUN` / `NOT AVAILABLE` semantics. This is a protocol, not an external validation result.
- [x] T822 Link adoption, examples, and independent validation from human and machine-readable entry points without keyword stuffing.
- [x] T823 Qualify, reconcile, expected-head merge, and exact post-merge verify the adoption unit. PR #90 exact head `9a7096abd2ec00541b8f521538cb41dbbf0268bb`; all nine pull-request workflows `SUCCESS`; no submitted reviews or inline threads; no substantive comments; canonical `main` remained `b31d891427b5ddbd43fc24c2ad2e1dc7adc6bd39` before expected-head squash merge. Canonical Phase C `498df9f4c0260f6deb87861f4e27f882f16a14ab`; post-merge `ci` `33441120552`, `skills-compat` `33441120459`, and `release` `33441120450` all `SUCCESS`.

## Phase D — Metadata handoff and discovery observation

- [x] T830 Publish `docs/GITHUB-METADATA.md` with exact recommended description/topics, source rationale, and live application status.
- [x] T831 Re-check repository metadata mutation support. The authenticated execution surface still exposes no repository description/topics mutation action, so the required status is `NOT APPLIED — TOOLING UNAVAILABLE`; live GitHub remains description unset, topics empty, homepage unset.
- [x] T832 Publish `docs/DISCOVERABILITY-2026-09-01.md` as a new bounded post-change snapshot while preserving historical `docs/DISCOVERABILITY.md` unchanged.
- [x] T833 Qualify, reconcile, expected-head merge, and exact post-merge verify the metadata/discovery unit. PR #91 exact head `128e2b711a725f79b788ce67151ce590fa940a06`; all nine pull-request workflows `SUCCESS`; no submitted reviews or inline review threads; only non-substantive automated comments; canonical `main` remained `498df9f4c0260f6deb87861f4e27f882f16a14ab` before expected-head squash merge. Canonical Phase D `cc52f2c95e67eca1458549b6639c6080c0feb533`; post-merge `ci` `33441805035`, `skills-compat` `33441805026`, and `release` `33441805093` all `SUCCESS`.

## Phase E — Terminal closeout

- [x] T840 Reconcile all Spec 008 public surfaces and preserved evidence against live canonical `main`. `terminal-reconciliation.md` records canonical Phase D proof, immutable `v1.0.0`, unchanged historical discoverability blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`, exact metadata status `NOT APPLIED — TOOLING UNAVAILABLE`, preserved benchmark limitations, and bounded public-surface corrections.
- [x] T841 Qualify the exact terminal candidate and reconcile reviews, threads, comments, mergeability, and canonical main. PR #92 exact head `c7e60b1b5f4c63311655215ef172c8de565e11e2`; all nine pull-request workflows `SUCCESS`: `tag-v1.0.0` `33442164512`, `tag-v0.1.0` `33442164582`, `stage-v1.0.0-release` `33442164514`, `stage-v0.1.0-release` `33442164484`, `verify-v0.1.0-release` `33442164545`, `verify-v1.0.0-release` `33442164580`, `release` `33442164488`, `ci` `33442164621`, and `skills-compat` `33442164604`. No submitted reviews or inline review threads; only non-substantive automated comments; mergeability `true`; canonical `main` remained `cc52f2c95e67eca1458549b6639c6080c0feb533` before merge.
- [x] T842 Merge only the expected head and require exact post-merge `ci`, `skills-compat`, and `release` success. PR #92 was squash-merged with expected head `c7e60b1b5f4c63311655215ef172c8de565e11e2` to canonical terminal reconciliation `f8314f34135afab2bd7801afb0658d40441f598e`; exact post-merge `ci` `33442409478`, `skills-compat` `33442409398`, and `release` `33442409380` all `SUCCESS`.
- [x] T843 Record `COMPLETE_CANONICAL` only after T842 is machine-observed. `t843-complete-canonical.md` records the terminal proof and completion criteria. This checkbox records the completion candidate; the status becomes effective only after this exact T843 record unit itself passes all nine pull-request workflows, clean reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success.

## Ordering

Phases A through E are machine-observed through T842. T843 is now the sole final evidence-record unit. Repository metadata remains `NOT APPLIED — TOOLING UNAVAILABLE`; historical discovery, release, and benchmark evidence remain preserved. `COMPLETE_CANONICAL` becomes effective only when the exact T843 record candidate itself completes the same proof-before-done qualification and post-merge gates.
