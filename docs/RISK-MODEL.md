# Risk model

Diffcipline separates minimality from rigor. A small diff can still be high risk.

## R0 — Non-behavioral

Examples: documentation, comments, formatting, metadata.

Expected proof: scope check and syntax/build checks when relevant.

## R1 — Local behavior

Examples: isolated feature behavior, local bug fix, internal helper.

Expected proof: focused regression or behavior test plus normal static checks.

## R2 — Shared behavior

Examples: persistence, concurrency, shared library contract, public API, serialization, infrastructure behavior.

Expected proof: focused regression, dependent-surface tests, static checks, and contract compatibility evidence.

## R3 — Critical boundary

Examples: authentication, authorization, security controls, payments, destructive data changes, schema migrations, secrets, cryptography.

Expected proof: R2 evidence plus adversarial/negative-path coverage and explicit review. Passing a small test suite alone is insufficient.
