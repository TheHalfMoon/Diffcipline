# Post-change discoverability snapshot — 2026-09-01

This is a bounded observation, not a ranking, endorsement, adoption measurement, or causal experiment. It is intentionally a new file: historical `docs/DISCOVERABILITY.md` remains unchanged.

Canonical repository base observed before this snapshot: `498df9f4c0260f6deb87861f4e27f882f16a14ab`.

## Repository metadata at observation time

GitHub reported:

- description: unset;
- topics: empty;
- homepage: unset;
- stars: 0;
- forks: 0;
- open issues: 0.

Spec 008's exact metadata recommendation is published in `docs/GITHUB-METADATA.md`, but the available authenticated execution surface cannot mutate repository description/topics. Therefore the recommendation was not applied before this snapshot.

Application status: `NOT APPLIED — TOOLING UNAVAILABLE`.

The counts above are repository metadata observations only. They are not converted into claims about total users, installs, readers, private forks, or adoption.

## GitHub repository-search observations

System: authenticated GitHub repository search.

Each category query inspected the returned first page with a maximum of 20 repositories.

| Query | Observation |
| --- | --- |
| `Diffcipline` | `TheHalfMoon/Diffcipline` observed as the exact-name result. |
| `coding agent verification` | Diffcipline not observed in the first 20 returned repositories. |
| `coding agent discipline` | Diffcipline not observed in the first 20 returned repositories. |
| `agent verification guardrails` | Diffcipline not observed in the first 20 returned repositories. |

These are bounded query observations, not a claim about all GitHub search orderings, users, locales, or future results.

## External GitHub-reference observations

Querying issues/PRs for `Diffcipline` while excluding `TheHalfMoon/Diffcipline` returned no results in the inspected set.

GitHub code search for `Diffcipline -repo:TheHalfMoon/Diffcipline` returned one result: `lmccalman/baroque/raw-output/SP 84.550/french_page_028.txt`. The match is an unrelated lexical occurrence, not a reference to this project.

No independent GitHub endorsement or adoption reference was established by these searches.

## Public web-search observations

A fresh public web-search sample used these queries:

- `"TheHalfMoon Diffcipline" coding agent`
- `"Diffcipline" "coding agent" verification`
- `"Diffcipline" github`
- `"Diffcipline" skills.sh`
- `site:skills.sh "Diffcipline"`
- `"best coding agent verification" github`
- `"coding agent discipline" github`
- `"proof before done" "coding agent"`

Diffcipline was not observed in the returned public-web sample. Category queries did surface other coding-agent discipline/verification projects and articles, which confirms that the query space itself returns relevant material but does not establish a ranking or a controlled comparison.

Search-engine results are dynamic, personalized/region-sensitive in some environments, and incomplete. This snapshot records only the observed sample on this date.

## skills.sh observation

Diffcipline/TheHalfMoon was not observed in the returned `skills.sh`-targeted public-web sample.

- indexing/visibility: `NOT OBSERVED`;
- install telemetry: `NOT ESTABLISHED`.

`NOT ESTABLISHED` must not be rewritten as zero installs.

## Independent recommendation surfaces

Independent GLM, Claude, Gemini, Grok, and similar recommendation systems were not available as separately preserved third-party observation surfaces in this execution.

Status: `NOT TESTED`.

This ChatGPT execution is excluded from independent-recommendation evidence because it is the repository executor for this snapshot.

## Comparison with the preserved historical audit

The historical Spec 007 audit remains unchanged at `docs/DISCOVERABILITY.md`.

This new observation does not establish a material discoverability improvement:

- exact-name GitHub discovery remains observable;
- the three bounded category queries still do not surface Diffcipline in their first 20 results;
- no relevant external GitHub reference was established;
- public-web and skills.sh-targeted samples did not surface Diffcipline;
- independent recommendation surfaces remain `NOT TESTED`;
- the recommended description/topics were not applied because the mutation tooling is unavailable.

Therefore broad public discovery/adoption remains an explicit limitation. No treatment effect is claimed because no repository metadata treatment was applied and this is not a controlled experiment.
