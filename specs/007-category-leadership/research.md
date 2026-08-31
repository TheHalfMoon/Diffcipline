# Research — 007 Category Leadership

## Snapshot

Research date: 2026-08-31.

Repository planning baseline: `2444671549cb22fc664e6f3476dcb43cd964d28f`.

This file records planning inputs, not endorsement or benchmark conclusions. Public sources can change; activation requires a fresh reconciliation after Spec 006 closes.

## Live Diffcipline baseline

Observed through GitHub repository APIs at the planning baseline:

- description: empty;
- topics: empty;
- homepage: empty;
- stars/forks: zero at this early repository age;
- Discussions: disabled;
- `.github/`: workflows only;
- README: strong technical depth and transparent negative benchmark reporting, but still contains pre-publication v1 wording while Spec 006 is active.

These are discovery/trust-surface gaps, not evidence that product behavior is weak.

## Public ecosystem signals

### Open Agent Skills ecosystem

Sources: https://agentskills.io, https://github.com/agentskills, https://skills.sh, and https://skills.sh/docs

Observed points:

- Agent Skills is an open format intended for portable agent capabilities;
- the ecosystem installs public skills with `npx skills add <owner/repo>`;
- skills.sh exposes install telemetry and an install-count badge;
- leaderboard/install position is an adoption observation, not an engineering-quality metric.

Implication for Diffcipline: use the open format and existing install path as the discovery spine, but never equate install count with correctness or superiority.

### obra/superpowers — verification-before-completion

Source: https://skills.sh/obra/superpowers/verification-before-completion

At this snapshot the skill showed roughly 193.8K installs and centers on the rule that completion claims require fresh verification evidence. That makes proof-before-completion a demonstrated high-demand category, not a unique phrase Diffcipline can own by messaging alone.

### agent-contracts/agent-task-contract

Source: https://github.com/agent-contracts/agent-task-contract

Observed positioning combines task definition, scope boundaries, risk-matched verification, failure context, and PR-ready evidence. This is a close conceptual comparator for scope-and-verification discipline, while its implementation model differs from Diffcipline's repository-native deterministic CLI and proof schema.

### Aurite-ai/agent-verifier

Source: https://github.com/Aurite-ai/agent-verifier

Observed positioning emphasizes cross-agent verification against policy, security, code-quality, and language-specific requirements. This reinforces that broad agent portability and verification alone are not sufficient differentiation claims.

### Repository discoverability

Source: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics

GitHub documents repository topics as a mechanism for helping people find projects by purpose and subject. Diffcipline currently has no topics or repository description, so metadata is a concrete discovery gap rather than cosmetic polish.

### Other adjacent signals

Public search surfaced additional repositories focused on deterministic finish-line gates, minimal-diff skills, agent governance, evidence ledgers, spec-driven workflows, and large multi-skill catalogs. Comparison must therefore use a timestamped comparator set rather than a cherry-picked rival.

## Differentiation hypothesis to verify

Diffcipline appears structurally differentiated by the combination of:

1. open Agent Skills behavior plus a deterministic external CLI;
2. exact-diff scope and policy evidence rather than model self-report;
3. explicit PASS / REVIEW / FAIL semantics and fail-closed verification;
4. risk-aware verification profiles and intent contracts;
5. local enterprise-policy layering without a remote policy service;
6. byte-qualified multi-agent skill compatibility;
7. signed cross-platform release candidates and attestation verification;
8. unusually explicit publication of negative benchmark results.

These are hypotheses until each row is linked to canonical repository evidence and compared against the frozen public comparator set.

## Recommendation-system reality

No repository can guarantee that GLM, GPT, Claude, Gemini, search engines, or other third-party systems will call it "the best." Their corpora, retrieval systems, ranking rules, and update schedules are external.

Repository-controlled work can improve recommendation likelihood by making facts easy to retrieve:

- concise identity and category wording;
- stable public release metadata;
- canonical install commands;
- source-cited comparison material;
- machine-readable evidence pointers;
- strong security/contribution surfaces;
- transparent benchmarks and limitations;
- public adoption signals that arise organically.

Spec 007 therefore optimizes verifiable public evidence and discoverability, not model manipulation.

## Research refresh rule

Before T703, re-check all named comparator URLs, skills.sh behavior, Diffcipline metadata, release state, README truth, and search visibility. Record changed facts explicitly; do not silently carry this snapshot forward.