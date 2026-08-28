---
name: diffcipline-review
description: Review a code change for unnecessary scope, hidden assumptions, dependency churn, weak proof, and risk-inappropriate verification. Use for pull requests, patches, diffs, or requests to simplify or verify agent-written code.
license: MIT
---

# Diffcipline Review

Review the exact diff, not the author's narrative.

## Review order

1. **Correct target** — does the change address the actual root cause and requested behavior?
2. **Scope** — does every changed file have a direct reason?
3. **Need** — was existing code, stdlib, native platform behavior, or an installed dependency ignored?
4. **Complexity** — are there speculative abstractions, configuration, wrappers, or dependencies?
5. **Risk** — is the verification level strong enough for the touched boundary?
6. **Proof** — what actually ran, and what remains unverified?

## Finding format

Use concise findings with evidence:

`<file>:<line/range> [scope|need|complexity|risk|proof] <problem>. <smallest correct remedy>.`

Do not flag security controls, trust-boundary validation, accessibility, data-integrity handling, or explicit requirements merely because removing them would shrink the diff.

Finish with one verdict:

- `PASS — scope and proof are sufficient.`
- `REVIEW — no hard failure, but evidence or judgment is incomplete.`
- `FAIL — a correctness/policy/verification requirement failed.`
