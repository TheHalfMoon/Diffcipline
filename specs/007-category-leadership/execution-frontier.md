# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical chain

- planning authority: `768a3980e99c4dac4e49b55d39f1d66366025ae8`;
- Phase B: `f3bcf163466feb853d3d441f326b758c5b9bce8e`;
- Phase C: `91ab45bc729b578cda37aed159bb4dbdd8e2f545`;
- Phase D: `41adfcd3d2ca6e16c85bddff8d976239f9d97d67`;
- Phase E: `92ad064b954182fe2082ac0a5c873ad0d740d811`;
- Phase F: `c8068f89bb926d86c3fb305c6097a41da985a3d4`;
- Phase G: `735e61c5db24df45fdca4e6d80f3982f82abdf5d`.

Phase G exact post-merge gates:

- `ci` `33434796013` — `SUCCESS`;
- `skills-compat` `33434795922` — `SUCCESS`;
- `release` `33434795993` — `SUCCESS`.

T700–T763 are complete.

## Terminal qualification candidate

Branch: `spec/007-terminal-qualification`.

T770 reconciliation against canonical `735e61c5db24df45fdca4e6d80f3982f82abdf5d` is recorded in `terminal-reconciliation.md`.

The reconciliation re-read the human, machine-readable, trust, comparison, discovery, benchmark, release, and live repository metadata surfaces. It confirmed the immutable `v1.0.0` tag still resolves to `5cb1c77340b75649f6168e0e8f66479ea047ea96`, release `379824838` remains published and immutable with the expected five assets, and the previously recorded repository metadata limitations remain true.

Two documentation repairs are included before closeout:

1. `llms.txt` now links the canonical bounded comparison and discoverability audit added after the original machine-readable index.
2. `stronger-evaluation.md` now matches the frozen benchmark reports: v0.1 is `1/6 task-correct` and `1/6 scorer-pass` for every treatment; v0.3 is `1/6 task-correct` with frozen `0/6 scorer-pass` under the published generated-`__pycache__` confound.

No frozen benchmark result, raw evidence, release, tag, asset, product behavior, dependency, manifest, lockfile, or workflow semantics are changed.

T771 requires exact-head workflow qualification plus review/thread/comment, mergeability, and canonical-main reconciliation. T772 requires expected-head merge and exact post-merge `ci`, `skills-compat`, and `release` success.

This branch deliberately does **not** record `COMPLETE_CANONICAL`. After T772 is machine-observed, a final evidence-record unit may perform T773.
