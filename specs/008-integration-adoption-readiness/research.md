# Research — Spec 008 Integration & Adoption Readiness

Research date: 2026-08-31.

## Canonical starting point

Live `main` was reverified at `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9`.

Spec 007 is closed `COMPLETE_CANONICAL`. Its final exact post-merge gates are:

- `ci` `33436852275` — `SUCCESS`;
- `skills-compat` `33436852135` — `SUCCESS`;
- `release` `33436852085` — `SUCCESS`.

The existing discoverability audit records exact-name GitHub discovery but weak category discovery, no meaningful bounded external GitHub references, no observed public-web project result, no established skills.sh install telemetry, and independent GLM/Claude/Gemini/Grok recommendation surfaces as `NOT TESTED`.

## Live repository metadata

GitHub live repository metadata currently reports:

- description: unset;
- topics: empty;
- homepage: unset;
- discussions: disabled;
- stars: 0;
- forks: 0;
- open issues: 0.

These are observations, not engineering-quality scores.

The currently available authenticated GitHub connector exposes repository reads and many repository/PR mutations, but no repository-metadata update action for description/topics/homepage. Spec 008 therefore treats metadata application as conditional on a real supported mutation surface and otherwise records the limitation explicitly.

## Discovery rationale

GitHub’s current documentation states that repository topics help people find and contribute to projects and recommends topics related to intended purpose, subject area, community, or language:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository

A fresh GitHub repository search for `coding agent verification` still does not return Diffcipline in the first 20 results. This is a distribution observation only and does not change the frozen Spec 007 comparator set.

## Repository-controlled leverage

The highest-confidence work available without external popularity manipulation is:

1. publish copyable ecosystem policies for common repositories;
2. make those published examples executable claims by parsing their exact files in tests;
3. reduce agent/CI onboarding ambiguity with one canonical adoption guide;
4. publish a protocol that independent evaluators can reproduce against immutable `v1.0.0`;
5. publish exact metadata recommendations without falsely claiming they were applied;
6. repeat discovery observations after the repository-controlled surfaces are canonical.

## Design constraints

- No runtime dependency is needed.
- Existing parser/test machinery can validate example policies directly.
- Example verification commands must match existing supported detection semantics: Rust, Node, Python, and Go.
- Agent recipes must reuse the already-qualified Agent Skills layouts rather than invent new platform-specific behavior.
- Immutable `v1.0.0` remains the stable public verification target.
- Historical benchmark losses, failed runs, release evidence, and Spec 007 audit remain immutable inputs, not marketing material to rewrite.
