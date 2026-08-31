# Discoverability audit

Audit date: 2026-08-31.

This document records a bounded observation of how easily Diffcipline can be found from public discovery surfaces. It is **not** a quality ranking, adoption benchmark, endorsement, search-engine guarantee, or completion gate based on third-party ranking.

Search results are volatile. The observations below are valid only for the named query, surface, result bound, and audit date.

## Interpretation rules

- `OBSERVED` means the named surface returned a directly relevant Diffcipline result in the bounded observation.
- `NOT OBSERVED` means the bounded observation did not return a directly relevant Diffcipline result. It does not prove global absence.
- `NOT TESTED` means this execution environment did not expose an independent query surface suitable for the observation.
- Search position, stars, installs, forks, citations, and model recommendations are adoption/discovery signals, not correctness evidence.

## GitHub repository search

Surface: authenticated GitHub repository search. Result bound: first 20 repositories returned for each query.

| Exact query | Observation |
| --- | --- |
| `Diffcipline` | **OBSERVED.** `TheHalfMoon/Diffcipline` is returned by exact-name repository search. |
| `coding agent verification` | **NOT OBSERVED** in the first 20 results. |
| `coding agent discipline` | **NOT OBSERVED** in the first 20 results. |
| `agent verification guardrails` | **NOT OBSERVED** in the first 20 results. |

This establishes a useful distinction: exact-name discovery works on GitHub, but the repository is not yet surfaced by the bounded category queries above.

## External GitHub references

Surface: GitHub code, issue, and pull-request lexical search, excluding `TheHalfMoon/Diffcipline` itself.

| Exact query | Observation |
| --- | --- |
| `Diffcipline -repo:TheHalfMoon/Diffcipline` in code search | One external lexical hit. Inspection shows an unrelated text occurrence in `lmccalman/baroque`, so it is not counted as a project reference. |
| `"TheHalfMoon/Diffcipline" -repo:TheHalfMoon/Diffcipline` in code search | **0** external hits. |
| `"Diffcipline" is:issue -repo:TheHalfMoon/Diffcipline` | **0** external issues. |
| `"Diffcipline" is:pr -repo:TheHalfMoon/Diffcipline` | **0** external pull requests. |

The bounded GitHub search therefore establishes no meaningful external repository reference yet. It does not prove that no reference exists outside GitHub search coverage.

## Public web search

Surface: public web search available to the repository executor. Observation bound: returned search results for the exact query on 2026-08-31.

Project-name queries:

- `"TheHalfMoon Diffcipline" coding agent` — **NOT OBSERVED**.
- `"Diffcipline" "coding agent" verification` — **NOT OBSERVED**.
- `"Diffcipline" github` — **NOT OBSERVED**.
- `"Diffcipline" skills.sh` — **NOT OBSERVED**.
- `site:skills.sh "Diffcipline"` — **NOT OBSERVED**.

Category queries:

- `"best coding agent verification" github` — Diffcipline **NOT OBSERVED** in the returned results.
- `"coding agent discipline" github` — Diffcipline **NOT OBSERVED**; current results include adjacent projects such as `frontier-infra/adl` and `kiloloop/kiloloop-skills`.
- `"proof before done" "coding agent"` — Diffcipline **NOT OBSERVED**; current results include tools/projects using similar proof-before-done language.

These category observations are discovery evidence only. They do not modify the frozen Phase E comparator set and do not establish that any returned project is better or worse than Diffcipline.

## skills.sh

Surface: `https://www.skills.sh/`, described by the site as the Open Agent Skills Ecosystem.

- The crawled leaderboard/index snapshot contains no `Diffcipline` text match: **NOT OBSERVED**.
- The same snapshot contains no `TheHalfMoon` text match: **NOT OBSERVED**.
- Public web search with `site:skills.sh "Diffcipline"` returns no Diffcipline result: **NOT OBSERVED**.
- Public install telemetry attributable to Diffcipline was not established by the available surface: **NOT ESTABLISHED**.

`NOT ESTABLISHED` must not be rewritten as zero installs. The available page snapshot is not proof of the complete skills.sh database or private telemetry.

## Independent LLM recommendation observations

Spec 007 requires only independent systems that are actually accessible to this execution environment. This session does not expose separate GLM, Claude, Gemini, Grok, or other independent model query surfaces whose outputs can be preserved as third-party observations.

| System | Observation |
| --- | --- |
| GLM | **NOT TESTED** — no independent GLM query surface is available here. |
| Claude | **NOT TESTED** — no independent Claude query surface is available here. |
| Gemini | **NOT TESTED** — no independent Gemini query surface is available here. |
| Grok | **NOT TESTED** — no independent Grok query surface is available here. |
| This ChatGPT execution session | **EXCLUDED** — the executor performing the repository work is not treated as independent recommendation evidence about its own work. |

No inference is made about what an unavailable model would recommend.

## Current bounded conclusion

Diffcipline now has strong first-party engineering, release, comparison, citation, and machine-readable evidence surfaces, but public discovery/adoption remains an open gap:

1. exact-name GitHub repository search finds it;
2. bounded category-oriented GitHub searches do not yet surface it in the first 20 results;
3. the bounded public web queries do not yet surface the project;
4. meaningful external GitHub references were not observed;
5. skills.sh indexing/install telemetry was not established;
6. independent LLM recommendation status is unknown because those systems were not available for observation.

These are honest adoption/discoverability findings, not failed engineering gates. Future work may improve distribution, metadata, integrations, citations, independent references, and category visibility, then repeat this audit as a new dated snapshot. Do not silently rewrite this one when rankings change.
