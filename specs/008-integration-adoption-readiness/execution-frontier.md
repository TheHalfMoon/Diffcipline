# Execution Frontier — Spec 008

Live GitHub/repository truth overrides this snapshot.

## Canonical prerequisite

Spec 007 closeout:

`108ed30e9d8fd00b7d0a6202cba5c433476c9ea9`

Exact post-merge:

- `ci` `33436852275` — `SUCCESS`;
- `skills-compat` `33436852135` — `SUCCESS`;
- `release` `33436852085` — `SUCCESS`.

Public `v1.0.0` remains immutable at `5cb1c77340b75649f6168e0e8f66479ea047ea96`.

## Canonical activation

Spec 008 planning PR #88 exact head:

`693e1bc81af394e77c96e7a373be8118ca301bb3`

All nine required pull-request workflows completed `SUCCESS`; no submitted reviews or inline review threads existed; automated comments were non-substantive; canonical `main` remained `108ed30e9d8fd00b7d0a6202cba5c433476c9ea9` before expected-head squash merge.

Canonical activation:

`60fb2643c2710f0e262c2b007ca4192f039d30c3`

Exact post-merge:

- `ci` `33439088987` — `SUCCESS`;
- `skills-compat` `33439088957` — `SUCCESS`;
- `release` `33439088976` — `SUCCESS`.

Spec 008 is therefore `ACTIVE_CANONICAL` by its activation contract.

## Phase B candidate

Branch: `feat/008-validated-policy-examples`.

The candidate publishes four copyable policy examples under `examples/policies/` for Rust, Node, Python, and Go, plus `examples/README.md` explaining semantics and limitations.

`crates/diffcipline-cli/tests/policy_examples.rs` loads the exact checked-in example files with `include_str!`, installs each as `.diffcipline.toml` in an isolated Git fixture, invokes the compiled CLI with `check --json`, and requires:

- proof schema `diffcipline.proof/v1`;
- repository policy provenance;
- `REVIEW` when verification is deliberately not run;
- every documented verification command to appear with state `NOT RUN`.

No ecosystem toolchain is executed by this test. It validates the published policy contract without pretending that a generic example proves each downstream project's test suite.

## Current limitations carried forward

- repository description is unset;
- topics are empty;
- homepage is unset;
- broad public discovery/adoption remains weak in the bounded Spec 007 audit;
- unavailable independent model recommendation surfaces remain untested;
- the authenticated execution surface currently exposes no repository-metadata mutation action.

## Next gate

T816 requires exact-head qualification of this Phase B candidate, clean review/thread/comment and canonical-main reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success before Phase C begins.
