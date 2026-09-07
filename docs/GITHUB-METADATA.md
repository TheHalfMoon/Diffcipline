# GitHub metadata recommendation

Date: 2026-09-01

This document records the exact repository-metadata recommendation authorized by Spec 008. Live GitHub state remains canonical over this record.

## Historical Phase C observation

Observed from the authenticated GitHub repository surface after canonical Phase C (`498df9f4c0260f6deb87861f4e27f882f16a14ab`):

- description: unset;
- topics: empty;
- homepage: unset.

The authenticated execution surface available during Phase C exposed repository/file/PR/issue/workflow operations but no action that could update repository description or topics.

Historical application status at that time:

`NOT APPLIED — TOOLING UNAVAILABLE`

That status is preserved as historical evidence only. It must not be represented as the current live GitHub state after the later independently verified metadata application.

## Exact recommended description

```text
Proof-before-done verification for coding agents through Agent Skills, a dependency-free Rust CLI, and a pinned GitHub Action.
```

## Exact recommended topics

```text
coding-agents
ai-agents
agent-skills
verification
developer-tools
github-actions
rust
code-quality
```

The recommendation is intentionally bounded to capabilities already present in canonical repository evidence. It does not claim vendor endorsement, category leadership, universal superiority, benchmark advantage, adoption, popularity, or independent validation.

## Current live reconciliation

Reconciled on 2026-09-08 from the authenticated GitHub repository API after the metadata was applied through a separately available authenticated execution path.

Current live state:

- description: `Proof-before-done verification for coding agents through Agent Skills, a dependency-free Rust CLI, and a pinned GitHub Action.`;
- topics: `agent-skills`, `ai-agents`, `code-quality`, `coding-agents`, `developer-tools`, `github-actions`, `rust`, `verification`;
- homepage: unset.

Current application status:

`APPLIED AND VERIFIED`

The topic order returned by GitHub is not semantically significant. The live set matches the eight recommended topics exactly.

This reconciliation records repository metadata only. It does not alter runtime behavior, proof semantics, benchmark evidence, release artifacts, tags, completed specifications, or the preserved historical discoverability document.

## Why these fields

GitHub documents repository descriptions and topics as repository-level discoverability/classification metadata. The recommended text names only the project's qualified interfaces and proof-before-done purpose; the topics are focused enough to describe those interfaces without keyword stuffing.

Official GitHub references:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository

## Application rule

Live GitHub state remains authoritative. If the description, topics, or homepage change later, repository-controlled status documentation must be reconciled from the authenticated live API before making a current-state claim.
