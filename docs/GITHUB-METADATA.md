# GitHub metadata recommendation

Date: 2026-09-01

This document records the exact repository-metadata recommendation authorized by Spec 008. Live GitHub state remains canonical over this record.

## Observed live state

Observed from the authenticated GitHub repository surface after canonical Phase C (`498df9f4c0260f6deb87861f4e27f882f16a14ab`):

- description: unset;
- topics: empty;
- homepage: unset.

The authenticated execution surface was re-checked for repository metadata mutation after Phase C. It exposes repository/file/PR/issue/workflow operations but no action that can update repository description or topics.

Application status:

`NOT APPLIED — TOOLING UNAVAILABLE`

No document, task, or closeout record may represent the recommendation below as live until GitHub itself is observed with those exact values.

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

## Why these fields

GitHub documents repository descriptions and topics as repository-level discoverability/classification metadata. The recommended text names only the project's qualified interfaces and proof-before-done purpose; the topics are focused enough to describe those interfaces without keyword stuffing.

Official GitHub references:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository

## Application rule

A future authorized execution may apply these exact values only through a supported authenticated mutation surface and must verify the resulting live GitHub state. Until then, the application status remains exactly:

`NOT APPLIED — TOOLING UNAVAILABLE`
