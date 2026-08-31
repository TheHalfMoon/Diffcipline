# Stronger evaluation decision — Spec 007 Phase F

Date: 2026-08-31

Status: `NOT_RUN`

## Decision

A new comparative coding-agent experiment is **not run** in this execution environment.

Spec 007 requires a stronger evaluation to be preregistered before execution and to use a sufficiently capable, authorized environment that can hold tasks, treatments, executors/models, harness versions, scorer behavior, raw outputs, patches, failures, and stopping rules fixed enough for a fair comparison.

The current repository execution surface can edit GitHub state, inspect public sources, and observe repository workflows. It does not expose a separate controlled multi-treatment coding-agent evaluation harness or a comparable set of external model executors suitable for the proposed experiment.

The conversational assistant executing repository work is not substituted as an experimental treatment. Doing so would collapse experiment design and execution into an uncontrolled condition and would not provide a defensible comparison against other agents or models.

## Consequence

T750 is answered **no for this environment**. Therefore T751 and T752 are not activated.

T753 is satisfied only by publishing this `NOT_RUN` record without weakening existing standards or converting missing evidence into a result.

No new correctness, quality, productivity, cost, or superiority claim follows from this decision.

## Preserved evidence

Existing accepted benchmark evidence remains unchanged:

- v0.1 reports **1/6 task-correct and 1/6 scorer-pass for every treatment** in the canonical matched run; all arms made zero repository changes, so the result does not establish a correctness or useful-minimality advantage;
- v0.3 reports **1/6 task-correct for every treatment**, while the frozen scorer reports **0/6 scorer-pass for every treatment** under the published generated-`__pycache__` confound;
- both experiments remain negative evidence, not a marketing asset;
- the bounded structural comparison in `docs/COMPARISON.md` is not reclassified as a benchmark.

## What would authorize a future run

A future specification or explicitly authorized experiment may run only after it records, before execution:

1. repository/task corpus and selection method;
2. treatment prompts and Diffcipline exposure;
3. named executor/model versions and access conditions;
4. harness and tool versions;
5. scorer implementation and visible/hidden boundaries;
6. primary and secondary metrics;
7. exclusions and invalidation criteria;
8. run count, retry policy, and stop rules;
9. raw-output, patch, token/cost, and failure-preservation rules;
10. publication rule requiring losses and null results to be reported as prominently as wins.

Until those conditions are available, `NOT_RUN` is the only evidence-consistent outcome.
