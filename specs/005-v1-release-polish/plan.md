# Plan — 005 v1 Release Polish

## Delivery principles

- create new authority rather than reactivating completed Spec 004;
- keep the release-polish diff deliberately small;
- fix only the verified quoted-array comma defect in the dependency-free parser;
- document enterprise enforcement without pretending local policy input is organization identity or distribution;
- preserve all v1 capability and historical benchmark/release evidence;
- keep public `v1.0.0` publication outside this specification;
- use exact-head and post-merge machine evidence for every canonical boundary.

## Phase A — Canonical planning authority

Establish Spec 005 scope, task order, preservation rules, qualification requirements, and the continuing public-release boundary. No implementation begins before this planning authority becomes canonical.

## Phase B — Surgical parser and documentation polish

First reproduce the quoted-command comma defect against live source behavior. Replace only the simplistic top-level comma splitting needed to distinguish separators from commas inside quoted strings. Keep standard-library-only parsing and preserve fail-closed behavior.

Add focused regression tests covering comma-containing verification commands and malformed input. Apply the corrected array behavior uniformly through the existing shared parser used by repository and enterprise policy files.

Update the enterprise-policy documentation to make enforcement responsibility explicit: the local monotonic baseline is active only when `--enterprise-policy <path>` is supplied, and mandatory organizational enforcement requires an externally controlled required CI path that supplies it.

Review live repository metadata and issue-entry surfaces. Apply only supported, low-cost hygiene; do not add bureaucracy.

## Phase C — Integrated qualification and closeout

Run focused tests and the strongest repository checks, then exact-head `ci`, `skills-compat`, and `release` on one final candidate. Reconcile reviews and threads, verify canonical `main`, and merge with an expected-head guard.

Verify exact post-merge `ci`, `skills-compat`, and `release` evidence on the resulting canonical SHA. Record Spec 005 completion separately only after that evidence is machine-observed.

## Ordering

A → B → C.

Public `v1.0.0` publication remains a later independent authority unit after Spec 005 completion.
