# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical chain

- planning authority: `768a3980e99c4dac4e49b55d39f1d66366025ae8`;
- Phase B: `f3bcf163466feb853d3d441f326b758c5b9bce8e`;
- Phase C: `91ab45bc729b578cda37aed159bb4dbdd8e2f545`;
- Phase D: `41adfcd3d2ca6e16c85bddff8d976239f9d97d67`;
- Phase E: `92ad064b954182fe2082ac0a5c873ad0d740d811`;
- Phase F: `c8068f89bb926d86c3fb305c6097a41da985a3d4`.

Phase F exact post-merge gates:

- `ci` `33433480729` — `SUCCESS`;
- `skills-compat` `33433480739` — `SUCCESS`;
- `release` `33433480733` — `SUCCESS`.

T700–T753 are complete. T751/T752 were satisfied by the T750 false condition: no stronger experiment was activated or executed, and `stronger-evaluation.md` records `NOT_RUN` without creating a result from missing infrastructure.

## Phase G candidate

Branch: `docs/007-discoverability-audit`.

`docs/DISCOVERABILITY.md` records a dated bounded audit with exact queries and explicit semantics:

1. exact-name GitHub repository search finds `TheHalfMoon/Diffcipline`;
2. the first 20 GitHub repository results for `coding agent verification`, `coding agent discipline`, and `agent verification guardrails` do not surface Diffcipline;
3. external GitHub code/issues/PR search establishes no meaningful project reference in the bounded search;
4. current public-web project-name and category searches do not surface Diffcipline in returned results;
5. the available skills.sh page snapshot contains no `Diffcipline` or `TheHalfMoon` match, while public install telemetry remains `NOT ESTABLISHED` rather than zero;
6. GLM, Claude, Gemini, Grok, and other independent model surfaces are unavailable to this execution environment and therefore `NOT TESTED`; this ChatGPT executor is excluded as non-independent evidence.

The audit is observational only. Search rank, install counts, citations, stars, and model recommendations are not quality proof or pass gates. The frozen Phase E comparator snapshot remains unchanged; newly observed adjacent search results are not silently promoted into comparator conclusions.

T760–T762 become canonical only after T763 exact-head qualification, clean reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success.

## Next unit

After T763, Phase H reconciles all public surfaces and evidence against canonical `main`, qualifies the terminal candidate, and records `COMPLETE_CANONICAL` only after the terminal merge has machine-observed post-merge proof.
