# Execution frontier — Spec 005

Live GitHub/repository truth overrides this snapshot.

## Current state

Spec 004 is `COMPLETE_CANONICAL` at terminal canonical `768bfcd48a1bbcc86e6ccbe879f87677eb66afb7` with no remaining implementation task.

Spec 005 planning is a candidate only until T503 is merged to canonical `main` and its required exact post-merge gates succeed.

No Rust, policy-behavior, or release-publication implementation is authorized by an unmerged planning branch.

## Verified release-polish inputs

- the shared dependency-free policy parser currently uses simplistic top-level comma splitting for quoted arrays;
- comma-containing quoted verification commands therefore require a surgical parser correction before public v1 preparation;
- `--enterprise-policy <path>` is explicit local input and does not by itself force repositories or workflows to supply that argument;
- public `v1.0.0` remains outside Spec 005.

## Next canonical gate

T503: merge this planning authority with an expected-head guard and require exact post-merge `ci`, `skills-compat`, and `release` success before Phase B begins.
