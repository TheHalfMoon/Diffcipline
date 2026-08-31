# Spec 008 — Integration & Adoption Readiness

## Status

`ACTIVE_CANDIDATE`

This authority becomes `ACTIVE_CANONICAL` only after this planning unit passes exact-head qualification, clean reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` on the resulting canonical commit.

## Purpose

Make Diffcipline easier to adopt correctly without weakening its proof-before-done contract.

Spec 007 established truthful positioning, immutable release evidence, machine-readable discovery surfaces, comparison evidence, contribution/security entry points, and a bounded discoverability audit. Its closeout also preserved a real gap: public discovery/adoption remains weak and the available authenticated execution surface cannot mutate GitHub description/topics.

Spec 008 addresses repository-controlled adoption friction. It does not reopen Spec 007, rewrite frozen benchmark evidence, or convert popularity into a quality gate.

## Canonical prerequisite

Spec 007 is `COMPLETE_CANONICAL` at `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9` after exact post-merge:

- `ci` `33436852275` — `SUCCESS`;
- `skills-compat` `33436852135` — `SUCCESS`;
- `release` `33436852085` — `SUCCESS`.

Public `v1.0.0` remains immutable at release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

## Principles

1. **Adoption must preserve rigor.** Examples may simplify setup, never verification semantics.
2. **Examples are executable claims.** Published policy examples must be parsed by repository tests from their actual checked-in files.
3. **No vendor endorsement claims.** Agent-specific recipes describe file/layout interoperability only.
4. **Independent validation is reproducible, not theatrical.** Publish a bounded protocol others can run; do not invent external results.
5. **Distribution signals stay observational.** Stars, installs, rankings, mentions, and model recommendations are not engineering pass gates.
6. **External admin gaps stay explicit.** If repository metadata cannot be changed through the available authenticated surface, publish the exact recommended values and record the limitation rather than pretending it was applied.

## Authorized work

### A. Validated ecosystem examples

Publish repository policy examples for Rust, Node, Python, and Go. Each example must use only currently supported policy keys and verification semantics. Add a test that parses the exact checked-in example files so documentation drift fails CI.

### B. Agent and CI adoption recipes

Publish a compact adoption guide covering the canonical Agent Skills install path, major supported agent layouts already qualified by the repository, CLI usage, and the immutable GitHub Action path. Link the guide and examples from first-screen and machine-readable discovery surfaces.

### C. Independent validation protocol

Publish a reproducible protocol that a maintainer, evaluator, or independent model operator can run against immutable `v1.0.0`. It must define environment facts, exact commands, expected PASS/REVIEW/FAIL semantics, evidence to retain, and a rule that missing execution is `NOT RUN`, never PASS.

### D. GitHub metadata handoff

Publish exact proposed repository description and focused topics grounded in the project’s actual capabilities. Cite GitHub’s own documentation that topics help people find and contribute to projects. Do not claim the metadata is live unless GitHub live state proves it.

### E. Post-change discovery observation

After repository-controlled work is canonical, repeat bounded GitHub/public-web discovery observations as a new dated snapshot. Preserve the Spec 007 audit unchanged. Indexing latency or unchanged rankings are valid findings, not failures to hide.

## Completion criteria

Spec 008 is complete only when:

- four checked-in ecosystem policy examples exist and the exact files are parsed by tests;
- adoption recipes are linked from human and machine-readable entry points;
- an independent validation protocol exists and contains no fabricated result;
- exact recommended GitHub description/topics and live-application status are recorded truthfully;
- a new dated discovery snapshot is published after repository-controlled changes;
- frozen benchmarks and immutable release evidence remain unchanged;
- every implementation unit passes exact-head qualification, clean reconciliation, expected-head merge, and exact post-merge repository gates;
- terminal closeout is itself canonically qualified.

## Non-goals

Do not buy or solicit fake engagement, claim endorsement by agent vendors, rewrite search results, manufacture external references, alter proof semantics for marketing, silently edit Spec 007 evidence, or run a weaker substitute benchmark and call it independent validation.
