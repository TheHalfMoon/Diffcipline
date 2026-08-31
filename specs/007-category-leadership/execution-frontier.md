# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical authority

Spec 006 is `COMPLETE_CANONICAL` at `91ba5389e26be2d8330fcc9c938d1f33bf120bec`.

Spec 007 planning authority is canonical at `768a3980e99c4dac4e49b55d39f1d66366025ae8`.

Phase B is canonical at `f3bcf163466feb853d3d441f326b758c5b9bce8e`; post-merge `ci` `33428154407`, `skills-compat` `33428154408`, and `release` `33428154493` completed `SUCCESS`.

Phase C is canonical at `91ab45bc729b578cda37aed159bb4dbdd8e2f545`; post-merge `ci` `33429154442`, `skills-compat` `33429154536`, and `release` `33429154544` completed `SUCCESS`.

T700–T725 are therefore complete.

## Phase D candidate

Branch: `docs/007-trust-contribution`.

This bounded unit:

1. strengthens `SECURITY.md` with private-reporting guidance, supported-version policy, executable-policy trust boundary, and a proof-before-disclosure fix standard;
2. adds a reproducible bug issue form that asks for exact version, environment, minimal reproduction, expected/actual behavior, and machine evidence without secrets;
3. adds a proof/evidence failure form that captures exact policy, command, Git state, observed verdict, and expected repository fact;
4. strengthens `CONTRIBUTING.md` around surgical scope, dependency restraint, exact-head proof, NOT RUN semantics, benchmark integrity, and security handling;
5. keeps GitHub Discussions disabled because no maintained discussion workflow or response commitment exists; an unattended channel is not treated as a leadership feature;
6. updates the canonical ledger to close Phase C and identify T734 as the qualification gate.

No product semantics, dependency, manifest, lockfile, release, tag, asset, or historical benchmark evidence is changed.

T730–T733 become canonical only after T734: exact-head workflow success, review/thread/comment and main reconciliation, expected-head merge, and exact post-merge `ci`, `skills-compat`, and `release` success.

## Next unit

After T734, Phase E freezes a timestamped comparator set and publishes bounded source-cited comparative evidence. Popularity and model recommendations remain observations, not engineering-quality proof.
