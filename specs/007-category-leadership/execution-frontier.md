# Execution frontier — Spec 007

Live GitHub/repository truth overrides this snapshot.

## Canonical authority

Spec 006 is `COMPLETE_CANONICAL` at `91ba5389e26be2d8330fcc9c938d1f33bf120bec`.

Spec 007 planning authority is canonical at `768a3980e99c4dac4e49b55d39f1d66366025ae8`.

Phase B is canonical at `f3bcf163466feb853d3d441f326b758c5b9bce8e`. Exact post-merge gates completed `SUCCESS`:

- `ci` `33428154407`;
- `skills-compat` `33428154408`;
- `release` `33428154493`.

T700–T714 are therefore complete.

## Phase C candidate

Branch: `docs/007-machine-readable-discovery`.

Live GitHub metadata observed on 2026-08-31 still reports `description=null`, `topics=[]`, and `homepage=null`. The authenticated GitHub execution surface available to this program has repository read/admin visibility but exposes no mutation action for description, topics, or homepage. T720/T721 record that limitation rather than fabricate a change. T722 intentionally leaves homepage unset because no independent stable canonical site exists.

This unit adds:

1. root `llms.txt` following the current concise Markdown discovery structure, with factual identity, installation, proof, release, benchmark, governance, and citation links;
2. `CITATION.cff` using CFF 1.2.0, entity author `TheHalfMoon`, immutable version `1.0.0`, release date `2026-08-31`, and exact release commit `5cb1c77340b75649f6168e0e8f66479ea047ea96`;
3. `docs/EVIDENCE.md`, mapping public capabilities to repository or immutable machine evidence and listing limitations;
4. lightweight README links to the new machine-readable surfaces;
5. updated task/current-state records.

No DOI, academic publication status, vendor endorsement, universal-best claim, hidden prompt instruction, or popularity claim is introduced.

T723/T724 are candidate-complete. T725 requires this exact branch to pass all pull-request workflows, reconcile reviews/threads/comments/mergeability and canonical main, merge with expected-head protection, and pass exact post-merge `ci`, `skills-compat`, and `release`.

## Next unit

After T725, execute Phase D trust and contribution surfaces. Do not begin comparative conclusions before Phase E freezes and revalidates its source set.
