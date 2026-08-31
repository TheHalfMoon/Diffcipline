# Spec 007 — Category Leadership

## Status

`DRAFT_BLOCKED_NONCANONICAL`

This specification is a planning candidate only. It MUST NOT become canonical, update `specs/CURRENT.md`, or authorize implementation until Spec 006 is `COMPLETE_CANONICAL` after immutable `v1.0.0` publication verification and terminal closeout.

## Purpose

Diffcipline should become the most credible, discoverable, and easiest-to-verify repository in its category: deterministic engineering discipline and finish-line proof for coding agents.

The goal is not to manufacture a subjective "best repository" claim or manipulate model rankings. The goal is to maximize the probability that developers, search engines, and LLM-based recommendation systems can independently discover Diffcipline, understand its differentiation, verify its claims, install it quickly, and compare it fairly with alternatives.

## Baseline at planning time

Planning baseline: canonical `main` `2444671549cb22fc664e6f3476dcb43cd964d28f` on 2026-08-31.

Observed repository truth:

- repository description is empty;
- repository topics are empty;
- repository homepage is empty;
- GitHub Discussions are disabled;
- `.github/` contains workflows only;
- README already documents Agent Skills installation, the dependency-free Rust CLI, deterministic proof, policy layering, multi-agent compatibility, signed release construction, and the preserved negative benchmark evidence;
- README still contains pre-publication wording while Spec 006 remains active;
- `skills.sh` documents install telemetry as the basis of its leaderboard and supports an install-count badge;
- public search did not surface Diffcipline by name during this planning pass.

Adjacent public projects already compete on evidence-first review, portable coding-agent skills, deterministic finish-line gates, or workflow discipline. Diffcipline must differentiate through externally verifiable product structure rather than slogans.

## Leadership principles

1. **Truth before positioning.** Every public claim must map to repository facts, machine evidence, or a cited external source.
2. **No universal-best claim.** "Best" may be used only when a defined comparison method and observed result support it for a bounded criterion.
3. **Fast comprehension.** A new visitor should understand what Diffcipline is, why it is different, and how to try it within the first screen and first two minutes.
4. **Machine-readable discovery.** Important identity, install, capability, evidence, and comparison facts should be easy for search/indexing systems and LLM retrieval pipelines to extract.
5. **Proof remains the moat.** Public positioning must emphasize deterministic proof, exact-diff policy, fail-closed behavior, portable Agent Skills, and signed release evidence.
6. **Negative evidence stays visible.** Existing benchmark losses and limitations must not be hidden, rewritten, or selectively summarized.
7. **Adoption is observed, not fabricated.** Stars, installs, mentions, recommendations, and benchmark wins are outcomes to measure, never repository acceptance criteria that can be gamed.

## Authorized work after activation

### A. Public truth and first-screen clarity

- update README only after Spec 006 completion so release language reflects the immutable public `v1.0.0` truth;
- place a concise category statement, proof-oriented differentiation, install path, and evidence links above the fold;
- provide a copy/paste quickstart that reaches a real proof verdict in approximately two minutes on a compatible environment;
- add only badges backed by live public systems and avoid decorative badge walls;
- keep exact limitations and benchmark caveats linked from the primary narrative.

### B. Repository discovery metadata

- set a factual repository description;
- set a focused topic set covering coding agents, agent skills, AI engineering, code review, verification, developer tools, Rust, and CI where GitHub permits;
- set a useful homepage only if a stable canonical destination exists;
- add the `skills.sh` badge only after confirming the repository is accepted/indexable by the public skills ecosystem;
- record any administrator-only metadata mutation as an explicit external action rather than bypassing it with repository code.

### C. Machine-readable identity and evidence

Create small, maintainable public surfaces where justified:

- `llms.txt` with factual product identity, install commands, canonical documentation, proof contract, release, benchmark evidence, limitations, and citation pointers;
- `CITATION.cff` if the repository can provide stable author/title/release metadata without inventing academic status;
- a concise capability/evidence matrix that links each differentiating claim to executable or immutable proof;
- no generated marketing corpus, keyword stuffing, hidden text, or model-specific prompt injection.

### D. Trust and community surface

Add only useful community files:

- `SECURITY.md` with a real disclosure path and supported-version policy;
- issue templates for bug reports and reproducibility/evidence reports if they reduce ambiguity;
- improve `CONTRIBUTING.md` around exact-head proof, benchmark integrity, and dependency restraint;
- enable Discussions only if there is a maintainer commitment to use it; otherwise leave it disabled and document the decision.

### E. Comparative evidence

Publish a bounded comparison document against a named, timestamped public comparator set.

The comparison MUST:

- compare observable capabilities, not inferred quality;
- cite source URLs and retrieval dates;
- separate product structure from benchmark outcomes;
- include disadvantages and missing features in Diffcipline;
- avoid star-count or popularity claims as evidence of engineering quality;
- remain reproducible enough that a maintainer can update it without subjective rewriting.

At minimum evaluate: deterministic enforcement, model independence, Agent Skills portability, exact-diff scope controls, risk-aware verification, machine-readable proof, dependency posture, signed release evidence, benchmark transparency, and enterprise-policy behavior.

### F. Evidence program

Existing v0.1 and v0.3 negative experiments remain frozen.

A stronger future evaluation may be designed only as a new, separately identified experiment with:

- a capable executor that can reliably edit repositories and call tools;
- exact prompts, models, harness versions, tasks, scorers, raw outputs, patches, costs/tokens when available, and limitations;
- preregistered success metrics before execution;
- no rerunning only losing rows;
- no hidden scorer or selective exclusion;
- a publication rule that reports losses as prominently as wins.

A new benchmark is not required to claim Spec 007 completion unless its execution environment is explicitly authorized and available. Unsupported superiority claims remain forbidden without it.

### G. Recommendation and discoverability audit

After public-surface implementation, run a timestamped observation audit across available public search engines, `skills.sh`, GitHub search, and accessible LLM recommendation systems.

The audit records whether Diffcipline is surfaced for bounded queries such as coding-agent verification, deterministic coding-agent governance, minimal-diff enforcement, and Agent Skills code review. Responses are evidence snapshots, not acceptance gates, because third-party rankings are external and unstable.

## Completion criteria

Spec 007 may become `COMPLETE_CANONICAL` only when all repository-controlled acceptance criteria are machine- or source-verified:

- public README reflects actual immutable v1 release truth and provides a tested quickstart;
- factual repository description/topics are set or an explicit administrator limitation is recorded;
- machine-readable identity/evidence surfaces are present and internally consistent;
- security/contribution entry points are usable;
- the comparative evidence document is source-cited and bounded;
- all existing negative benchmark evidence remains unchanged and prominent;
- exact-head and post-merge repository gates succeed for every implementation unit;
- a final discoverability audit is published without turning third-party popularity into a pass/fail criterion.

## Non-goals

Do not buy stars, automate fake engagement, mass-post promotional spam, hide negative benchmark evidence, create fake citations, claim endorsement by an LLM vendor, manipulate model prompts embedded in public files, or introduce product dependencies solely for marketing.

Do not change Diffcipline's proof semantics merely to improve positioning metrics.

## Activation rule

This planning candidate may be reviewed while Spec 006 is active, but it MUST remain unmerged and noncanonical until Spec 006 terminal closeout is canonical. Activation requires a fresh live-repository reconciliation after Spec 006 completion and a dedicated planning-authority merge whose exact head and exact post-merge gates succeed.