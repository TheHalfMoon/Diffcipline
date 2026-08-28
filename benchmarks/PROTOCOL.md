# Diffcipline benchmark protocol

The benchmark exists to falsify our claims, not decorate the README.

## Arms

At minimum:

1. agent baseline with no behavioral skill
2. agent + comparison skill when license and installation permit
3. agent + Diffcipline

Use the same task, repository revision, model, harness configuration, tool permissions, and resource limits for each arm.

## Task classes

Include tasks where minimal solutions help and tasks where they should not dominate:

- bug fixes with a shared root cause
- small features with a native or standard-library solution
- dependency temptation
- refactors with explicit behavior preservation
- validation/security boundaries
- tasks that are already minimal

## Metrics

Primary:
- task correctness
- regression rate
- changed files
- added/deleted LOC
- unrelated churn
- dependency additions
- verification quality

Secondary when reliably available:
- tokens
- cost
- wall-clock time

## Publication requirements

Publish raw run artifacts, exact revisions, model/harness versions, scoring code, and every excluded run with the exclusion reason. Report confidence intervals when sample sizes support them. Never flatten a per-task ceiling into an overall average.
