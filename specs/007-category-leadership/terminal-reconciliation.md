# Terminal reconciliation — Spec 007

Date: 2026-08-31

Canonical base inspected: `735e61c5db24df45fdca4e6d80f3982f82abdf5d`.

This record is the T770 reconciliation evidence for the Spec 007 terminal qualification candidate. Live GitHub/repository truth overrides this snapshot.

## Phase G canonical proof

Phase G is canonical at `735e61c5db24df45fdca4e6d80f3982f82abdf5d` after exact post-merge:

- `ci` run `33434796013` — `SUCCESS`;
- `skills-compat` run `33434795922` — `SUCCESS`;
- `release` run `33434795993` — `SUCCESS`.

T760–T763 are therefore complete.

## Public-surface reconciliation

The following canonical surfaces were re-read from the exact base before this candidate was written:

- `README.md`;
- `llms.txt`;
- `CITATION.cff`;
- `docs/EVIDENCE.md`;
- `docs/COMPARISON.md`;
- `docs/DISCOVERABILITY.md`;
- `SECURITY.md`;
- `CONTRIBUTING.md`;
- `specs/007-category-leadership/stronger-evaluation.md`;
- frozen v0.1 and v0.3 benchmark reports;
- live repository metadata, `v1.0.0` tag, and `v1.0.0` release metadata.

## Live release truth

- `refs/tags/v1.0.0` still resolves exactly to `5cb1c77340b75649f6168e0e8f66479ea047ea96`.
- GitHub release `379824838` is `draft=false`, `prerelease=false`, and `immutable=true`.
- The release still exposes exactly the expected five assets: three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`.
- No release, tag, asset, checksum, provenance, or historical benchmark evidence is modified by this terminal candidate.

## Live repository metadata truth

The live repository still has:

- description: unset;
- topics: empty;
- homepage: unset;
- Discussions: disabled.

These states match the previously recorded Spec 007 decisions/limitations. The authenticated repository execution surface still exposes no repository-description/topic mutation action, no separate canonical homepage exists, and no maintained Discussions workflow exists. No mutation is fabricated.

No open pull request was present immediately before creating this terminal qualification branch.

## Reconciliation fixes

Two documentation issues were found and are repaired in this candidate before closeout:

1. `llms.txt` was created before Phases E/G and did not yet link the bounded comparison or discoverability audit. This candidate adds those canonical evidence pointers to the machine-readable index without changing product claims.
2. `stronger-evaluation.md` incorrectly summarized the v0.1 historical scorer-pass count as `0/6`. The frozen v0.1 report says every arm finished at `1/6 correct` and `1/6 scorer-pass`. The frozen v0.3 report says every treatment finished at `1/6 task-correct` while the frozen scorer reported `0/6 scorer-pass` under the published `__pycache__` confound. This candidate corrects only the summary; the historical reports and raw evidence remain unchanged.

## Completion-criteria reconciliation

After the fixes above, every Spec 007 completion criterion is represented by canonical or candidate evidence:

- immutable-v1 README truth and machine-qualified quickstart;
- unavailable repository metadata mutation explicitly recorded;
- machine-readable identity/evidence surfaces cross-linked to current evidence;
- security and contribution entry points present;
- bounded source-frozen comparison preserving weaknesses and unknowns;
- frozen negative benchmark evidence unchanged;
- timestamped discoverability audit published;
- every completed implementation unit has exact-head qualification, reconciliation, expected-head merge, and exact post-merge gates;
- terminal closeout remains pending T771/T772 proof and T773 recording.

This candidate does **not** mark Spec 007 `COMPLETE_CANONICAL`. T773 remains forbidden until T772 has been machine-observed after this terminal qualification unit merges.
