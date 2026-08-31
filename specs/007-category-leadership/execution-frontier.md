# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical chain

- planning authority: `768a3980e99c4dac4e49b55d39f1d66366025ae8`;
- Phase B: `f3bcf163466feb853d3d441f326b758c5b9bce8e`;
- Phase C: `91ab45bc729b578cda37aed159bb4dbdd8e2f545`;
- Phase D: `41adfcd3d2ca6e16c85bddff8d976239f9d97d67`;
- Phase E: `92ad064b954182fe2082ac0a5c873ad0d740d811`.

Phase E exact post-merge gates:

- `ci` `33432375777` — `SUCCESS`;
- `skills-compat` `33432375615` — `SUCCESS`;
- `release` `33432375709` — `SUCCESS`.

T700–T744 are complete.

## Phase F candidate

Branch: `docs/007-stronger-evaluation-not-run`.

Decision: a new stronger comparative coding-agent experiment is `NOT_RUN` in the current environment. The repository execution surface can mutate/observe GitHub and public sources, but it does not expose a separate controlled set of comparable coding-agent/model executors plus a preregisterable harness/scorer suitable for a defensible treatment comparison.

The conversational repository executor is not substituted as an experimental treatment. Missing experimental infrastructure is not converted into a benchmark result.

`stronger-evaluation.md` records the decision, preserves existing negative v0.1/v0.3 evidence unchanged, and lists the controls required before any future run.

T750 and T753 become complete only after this exact candidate qualifies, reconciles, merges by expected head, and exact post-merge `ci`, `skills-compat`, and `release` succeed. T751/T752 remain not activated because the T750 condition is false for this environment.

## Next unit

After T753, execute the timestamped discoverability audit. Record GitHub/web/skills.sh observations exactly. Independent LLM systems unavailable to this execution environment must be recorded `NOT OBSERVED`, not simulated or inferred.