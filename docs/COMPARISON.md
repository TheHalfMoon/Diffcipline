# Bounded comparison: coding-agent discipline and verification

Snapshot date: 2026-08-31.

This comparison is intentionally narrow. It compares observable repository structures at the exact commits frozen in `specs/007-category-leadership/comparator-snapshot.md`. It is **not** a universal quality ranking, benchmark result, vendor endorsement, or claim that a missing public feature cannot exist elsewhere.

`Not established` means only that the reviewed frozen source did not establish the capability.

## Structural comparison

| Dimension | Diffcipline | obra/superpowers | Aurite Agent Verifier | skillgate | Agent Task Contract |
| --- | --- | --- | --- | --- | --- |
| Deterministic enforcement outside model self-report | **Yes.** Dependency-free Rust CLI computes PASS / REVIEW / FAIL from repository facts, policy, and executed checks. | **Partial.** Strong verification discipline is encoded as agent skills; the reviewed source does not establish a standalone deterministic finish-line verdict engine. | **Partial.** Verification is delivered as coding-agent skills with structured findings; the reviewed source does not establish an independent exact-diff verdict engine. | **Yes.** README explicitly describes a model-independent deterministic evaluator that can block finish-line actions. | **Partial.** Skill defines task/verification discipline and deterministic helper scripts, but the reviewed source does not establish an independent finish-line verdict engine. |
| Model / harness independence | **Yes.** CLI behavior is separate from the coding model; Agent Skills are an adapter. | **Partial.** Skills are portable across multiple agent harnesses, but execution remains agent-workflow driven. | **Partial.** README documents 30+ coding-agent targets; verification remains skill-mediated. | **Yes.** Public positioning explicitly states model independence and CI/pre-commit/server use. | **Partial.** Skill is usable with multiple coding agents; the task discipline remains agent-mediated. |
| Agent Skills / coding-agent portability | **Yes.** One canonical behavior is compatibility-qualified across generic Agent Skills plus Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI layouts. | **Yes.** Repository is an agentic skills framework with multiple harness integrations. | **Yes.** README documents Agent Skills installation and 30+ supported agents. | **Partial.** Integrates with agent hooks plus CI/pre-commit; it is primarily an evaluator rather than a portable Agent Skill contract. | **Yes.** Repository is explicitly a coding-agent skill and documents Codex/Claude/OpenClaw-style installation. |
| Machine-enforced exact-diff scope controls | **Yes.** Policy covers changed-file count, added lines, manifests, lockfiles, untracked files, expected paths, and forbidden surfaces. | **Not established.** | **Not established.** | **Partial.** Evaluates configured definition-of-done and instruction drift, but the reviewed source does not establish Diffcipline-style expected-path / forbidden-surface exact-diff policy. | **Partial.** Scope/non-goals are first-class workflow concepts, but the reviewed source does not establish equivalent machine-enforced exact-diff path contracts. |
| Risk-aware verification selection | **Yes.** Explicit R0–R3 profiles select repository-declared commands and fail closed when a requested profile is absent. | **Not established** as a named machine-enforced risk-profile contract. | **Partial.** Domain-focused security/quality/pattern/language checks exist, but not the same risk-profile selection contract. | **Not established** in the reviewed frozen source. | **Partial.** README explicitly asks agents to choose verification matching change risk; this is workflow guidance rather than the same CLI profile contract. |
| Machine-readable proof output | **Yes.** Stable `diffcipline.proof/v1` JSON schema includes verdict, scope, policy provenance, reasons, and verification states. | **Not established.** | **Partial.** README shows structured human-readable verification reports; a stable machine proof schema was not established in the reviewed source. | **Partial.** README documents JSON output for instruction-drift inspection; an equivalent universal finish-line proof schema was not established in the reviewed source. | **Not established** as a stable verdict/proof schema. |
| Runtime dependency posture | **Yes.** Core Rust CLI declares no runtime dependencies. | **Different scope.** Primarily skills, hooks, shell tooling, and harness integration rather than a comparable standalone Rust CLI. | **Different scope.** Agent Skills package; README emphasizes local analysis but is not a directly comparable CLI dependency surface. | **Different scope.** TypeScript/npm evaluator with a package dependency/toolchain model. | **Different scope.** TypeScript helper tooling uses an npm toolchain. |
| Release integrity / provenance evidence | **Yes.** Public `v1.0.0` is immutable; Linux/macOS/Windows binaries, SHA256SUMS, Sigstore provenance, release attestation, and every-asset verification are preserved. | **Not established** at the same artifact/provenance level in the reviewed source. | **Not established** at the same artifact/provenance level in the reviewed source. | **Not established** at the same artifact/provenance level in the reviewed source. | **Not established** at the same artifact/provenance level in the reviewed source. |
| Benchmark and failure transparency | **Yes, with negative results.** v0.1 and v0.3 reports publish losses/limitations; the initial v1 publication verifier failure is also preserved. These results do **not** establish a correctness advantage. | **Partial.** Repository contains extensive skills testing/evaluation work, but this snapshot is not a comparable public treatment benchmark against Diffcipline. | **Not established** as a comparable public benchmark in the reviewed source. | **Partial.** README cites a separate empirical compliance study; Phase E did not independently audit it as a like-for-like benchmark. | **Not established** as a comparable public benchmark in the reviewed source. |
| Organization / enterprise policy behavior | **Yes.** Local enterprise baseline can be tightened by repository policy but not weakened; provenance is exposed in proof. | **Different scope.** Workflow methodology rather than the same monotonic enterprise-policy layer. | **Partial / different scope.** README documents organization-specific rules through Kahuna-enhanced mode. | **Partial / different scope.** Definition-of-done policy can run in CI/server-side enforcement, but the reviewed source does not establish the same monotonic two-layer policy contract. | **Partial.** Task contract carries scope/risk/verification requirements, but not the same monotonic enterprise-policy merge semantics. |

## What the matrix supports

The strongest bounded Diffcipline differentiators in this frozen comparison are the **combination** of exact-diff policy, fail-closed risk-specific verification, stable machine proof, a dependency-free model-independent CLI, portable Agent Skills, and immutable signed release evidence.

That statement is structural, not a claim that Diffcipline produces better code than every alternative. Diffcipline's own public benchmark history currently does **not** prove a correctness advantage.

## Where alternatives are stronger or broader

- **obra/superpowers** has dramatically greater public adoption and a broader end-to-end software-development skills methodology. Diffcipline does not match that ecosystem scale or workflow breadth.
- **Aurite Agent Verifier** exposes a broader catalog of security, code-quality, agent-pattern, and language-specific review checks and documents support across 30+ agents. Diffcipline is deliberately narrower: it governs scope and executable proof rather than replacing domain-specific static/review expertise.
- **skillgate** has direct finish-line blocking integrations across agent hooks, pre-commit/CI, and documented server-side enforcement patterns. Diffcipline currently focuses on explicit proof evaluation and CI/Action integration rather than claiming an unbypassable remote gate.
- **Agent Task Contract** is lighter-weight and may be easier to adopt when a team wants process guidance without a separate compiled CLI or policy file.

## Popularity is separate evidence

GitHub stars, forks, install counts, search ranking, and model recommendations describe adoption/discoverability. They are not included in capability scoring and are not evidence that one engineering method is more correct.

Diffcipline is a very new repository and currently has far less public adoption than the largest comparator. Spec 007 treats that as a discoverability/adoption gap, not something to conceal or relabel.

## Sources

Frozen commit links and source-selection rules are recorded in `specs/007-category-leadership/comparator-snapshot.md`. Diffcipline capability links are additionally indexed in `docs/EVIDENCE.md`.

Re-run this comparison only by creating a new dated snapshot; do not silently rewrite the frozen source commits when upstream projects change.