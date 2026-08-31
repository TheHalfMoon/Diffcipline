# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical authority

Spec 006 is `COMPLETE_CANONICAL` at `91ba5389e26be2d8330fcc9c938d1f33bf120bec`.

Spec 007 planning authority is canonical at `768a3980e99c4dac4e49b55d39f1d66366025ae8`. Its exact post-merge gates completed `SUCCESS`:

- `ci` `33426507275`;
- `skills-compat` `33426507265`;
- `release` `33426507377`.

T700–T703 are therefore effective and Phase B is authorized.

## Phase B candidate

Branch: `docs/007-first-screen-quickstart`.

This unit:

1. replaces stale pre-publication README language with verified immutable `v1.0.0` truth;
2. rewrites the first screen around deterministic proof, installation, and evidence links;
3. adds a copy/paste Rust quickstart that reaches a real `PASS`;
4. adds an integration test that executes the same init/change/check path and asserts the exact verification lines;
5. preserves the negative v0.1 and v0.3 benchmark findings prominently;
6. records that public skills.sh search did not surface Diffcipline during the 2026-08-31 check, so no install-count badge is added yet.

T710–T713 become complete only after this exact candidate is qualified, reconciled, merged with expected-head protection, and its canonical SHA passes exact post-merge `ci`, `skills-compat`, and `release`. T714 is that qualification/merge gate.

## Next unit

After T714, execute Phase C discovery and machine-readable identity: repository metadata where tooling permits, `llms.txt`, truthful citation metadata, and a capability-to-evidence matrix.

Do not make comparative superiority claims before the Phase E source freeze and comparison method are complete.
