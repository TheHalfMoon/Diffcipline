# Diffcipline Constitution

## I. Proof before done

No workflow, agent, CLI, benchmark, or documentation may represent a check as passed unless the exact check ran successfully against the exact change being claimed.

## II. Minimality is subordinate to correctness

Diff size is a cost signal, not the objective function. Correctness, security, accessibility, data integrity, compatibility, and explicit requirements outrank line count.

## III. Repository truth outranks narrative

Git diff, repository policy, executable checks, and reproducible artifacts are canonical evidence. Agent summaries are claims to verify, not evidence to trust automatically.

## IV. Risk changes rigor

Verification must scale with blast radius. High-risk boundaries require negative-path and adversarial evidence even when the code change is small.

## V. Open, reproducible claims

Performance, quality, cost, and behavioral claims require enough public method and artifacts for an independent maintainer to reproduce or challenge them.

## VI. Portable core

The behavioral contract must remain usable through the open Agent Skills convention. Platform-specific adapters may improve experience but must not become the only way to use the core skill.

## VII. Dependency restraint

The core CLI starts dependency-free. A new runtime dependency requires a documented capability, security, maintenance, and portability justification.
