# Terminal reconciliation — Spec 008

Date: 2026-09-01

Live GitHub/repository truth overrides this record.

## Canonical base inspected

Canonical Phase D: `cc52f2c95e67eca1458549b6639c6080c0feb533`.

Exact Phase D post-merge gates:

- `ci` `33441805035` — `SUCCESS`;
- `skills-compat` `33441805026` — `SUCCESS`;
- `release` `33441805093` — `SUCCESS`.

T833 is therefore machine-observed complete.

## Completion-criteria reconciliation

The canonical repository was reconciled against every Spec 008 completion criterion.

### Validated ecosystem examples

The checked-in Rust, Node, Python, and Go policy examples remain canonical from Phase B. The repository integration test loads the exact checked-in files through the real CLI contract. Phase B remains qualified at `b31d891427b5ddbd43fc24c2ad2e1dc7adc6bd39` with exact post-merge `ci`, `skills-compat`, and `release` success.

### Adoption and independent validation

`docs/ADOPTION.md`, `examples/README.md`, and `docs/INDEPENDENT-VALIDATION.md` remain canonical from Phase C and are linked from both `README.md` and `llms.txt`. The independent-validation document remains a protocol only; no external result, vendor endorsement, or independent execution is represented as observed.

### GitHub metadata handoff

`docs/GITHUB-METADATA.md` records the exact recommended description and topics. Live GitHub was re-read during terminal reconciliation and still reports:

- description: unset;
- topics: empty;
- homepage: unset.

The authenticated execution surface still exposes no repository description/topics mutation action. The exact application status remains:

`NOT APPLIED — TOOLING UNAVAILABLE`

No closeout surface may rewrite that status as applied.

### Discoverability observation

`docs/DISCOVERABILITY-2026-09-01.md` is canonical from Phase D and records the bounded post-change observation. It establishes exact-name GitHub discovery but no material broad-discovery improvement, no relevant external GitHub reference, no public-web or skills.sh observation of Diffcipline in the sampled results, and no independent model recommendation evidence.

Historical `docs/DISCOVERABILITY.md` remains unchanged at blob `013791e04fd30607f1f64f4a8218c000a8f0ab73`.

The terminal candidate adds direct human and machine-readable links to the metadata handoff and dated snapshot so the new canonical evidence is reachable without replacing the preserved historical audit.

### Immutable release and frozen evidence

Live GitHub still reports release `v1.0.0` as immutable, and tag `v1.0.0` still resolves to release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96` with the five published release assets intact.

Frozen benchmark evidence remains unchanged. The v0.1 and accepted v0.3 results do not establish a correctness advantage, failed runs and negative findings remain preserved, and no stronger experiment is represented as having run.

## Reconciliation findings

Two documentation-frontier discrepancies were identified after Phase D became canonical:

1. `specs/CURRENT.md` still described Phase D as a candidate and T833 as pending.
2. `README.md` and `llms.txt` did not directly index the new metadata recommendation and dated post-change discoverability snapshot.

This terminal candidate corrects those public/canonical surfaces only. No workflow, dependency, lockfile, release, tag, asset, benchmark result, proof semantic, or historical evidence is changed.

## Terminal qualification rule

This record does **not** mark Spec 008 `COMPLETE_CANONICAL`.

T841 must qualify the exact terminal candidate through all required pull-request workflows and reconcile reviews, review threads, comments, mergeability, and canonical `main`. T842 must then merge only the expected head and require exact post-merge `ci`, `skills-compat`, and `release` success.

Only after T842 is machine-observed may T843 record `COMPLETE_CANONICAL`. That completion record must itself pass the same exact-head qualification, reconciliation, expected-head merge, and exact post-merge proof discipline before completion becomes effective.
