# Current specification

Active after this completion-record unit becomes canonical: none.

Status recorded by this unit: `COMPLETE_CANONICAL`

Live GitHub/repository truth overrides this file.

The status above becomes effective canonical truth only after the exact T843 completion-record candidate itself passes all nine required pull-request workflows, reconciles reviews/threads/comments/mergeability/exact head/canonical `main`, merges by expected head, and the resulting canonical commit passes exact post-merge `ci`, `skills-compat`, and `release`.

Until those conditions are machine-observed, canonical `main` remains the prior terminal-reconciliation state and Spec 008 must not be treated as effectively complete merely because this candidate records the status.

## Completed roadmap history

Specs 001–007 are `COMPLETE_CANONICAL`.

Spec 007 terminal closeout is canonical at `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9` after exact post-merge `ci` `33436852275`, `skills-compat` `33436852135`, and `release` `33436852085` all `SUCCESS`.

Public `v1.0.0` remains published immutable at release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`; published-release verification run `33424987600` completed `SUCCESS`.

## Spec 008 canonical units

Activation: `60fb2643c2710f0e262c2b007ca4192f039d30c3` — post-merge `ci` `33439088987`, `skills-compat` `33439088957`, `release` `33439088976` all `SUCCESS`.

Phase B / validated ecosystem examples: `b31d891427b5ddbd43fc24c2ad2e1dc7adc6bd39` — post-merge `ci` `33440059674`, `skills-compat` `33440059726`, `release` `33440059755` all `SUCCESS`.

Phase C / adoption and independent validation: `498df9f4c0260f6deb87861f4e27f882f16a14ab` — post-merge `ci` `33441120552`, `skills-compat` `33441120459`, `release` `33441120450` all `SUCCESS`.

Phase D / metadata handoff and discoverability observation: `cc52f2c95e67eca1458549b6639c6080c0feb533` — post-merge `ci` `33441805035`, `skills-compat` `33441805026`, `release` `33441805093` all `SUCCESS`.

Terminal reconciliation: `f8314f34135afab2bd7801afb0658d40441f598e` — post-merge `ci` `33442409478`, `skills-compat` `33442409398`, `release` `33442409380` all `SUCCESS`.

Terminal reconciliation PR #92 exact head `c7e60b1b5f4c63311655215ef172c8de565e11e2` passed all nine required pull-request workflows and reconciled with no submitted reviews or inline review threads, no substantive comments, mergeability `true`, exact head unchanged, and canonical `main` still `cc52f2c95e67eca1458549b6639c6080c0feb533` before expected-head squash merge.

T840, T841, and T842 are machine-observed complete.

## Completion-record frontier

Branch `docs/008-complete-canonical` is the sole remaining Spec 008 unit. It records T843 and `COMPLETE_CANONICAL` only after T842 machine proof exists.

The candidate is limited to the Spec 008 completion record and canonical status/frontier/task surfaces. It does not alter implementation, workflows, dependencies, lockfiles, releases, tags, assets, benchmark results, proof semantics, or historical evidence.

Effective completion requires exact-head qualification of this candidate through all nine pull-request workflows, clean review/thread/comment/mergeability/main reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success.

After that final proof is machine-observed, Specs 001–008 are `COMPLETE_CANONICAL`, there is no active authorized implementation specification, and any new repository-controlled work requires a new canonical specification or separately authorized maintenance unit.

## Preserved limitations

Frozen v0.1/v0.3 benchmark evidence does not establish a correctness advantage, no stronger experiment is represented as having run, broad discovery/adoption remains an explicit gap, and unavailable independent model recommendation systems remain `NOT TESTED` where no separately preserved third-party observation surface was available.

Repository metadata remains truthfully recorded as `NOT APPLIED — TOOLING UNAVAILABLE`; live GitHub was last reconciled with description unset, topics empty, and homepage unset because the authenticated execution surface exposes no supported repository metadata mutation action.

Historical `docs/DISCOVERABILITY.md` remains preserved at blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`.

Public `v1.0.0` remains immutable and tag `v1.0.0` resolves to release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`.
