# Diffcipline v0.1 benchmark evidence

## Result

The canonical matched run does **not** show a correctness advantage for Diffcipline or either comparison treatment. All four arms finished at **1/6 correct** and **1/6 scorer-pass**, with zero changed files across every arm. The only correct task was the already-minimal no-op fixture (`f06`). Diffcipline also had the largest observed total wall-clock time.

## Canonical execution

- Run: `33200332207` (`benchmark-arms` #27)
- Repository revision: `b640461cfdf08c25b8cf8b0404aa6b5a8ccae1bc`
- Repaired frozen fixture/preparer/scorer boundary: `cde4d0058ce522ddd9863457c29560679fac53dd`
- Results artifact SHA-256: `00751734da3428a1ce9c1c4b020bbf12264289782b12e82d24a781caf1506203`
- Durable archive SHA-256: `a60c0873738ac4e03b52df2f8512eed35d25f190efefbb68d0522c4f67c86274`
- Arm order: baseline -> Karpathy -> Ponytail -> Diffcipline

| Arm | Correct | Scorer pass | Changed files | Total seconds | Clean agent exits | Bash calls |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | 1/6 | 1/6 | 0 | 746.668 | 4/6 | 79 |
| Karpathy | 1/6 | 1/6 | 0 | 797.091 | 4/6 | 63 |
| Ponytail | 1/6 | 1/6 | 0 | 702.127 | 1/6 | 29 |
| Diffcipline | 1/6 | 1/6 | 0 | 981.263 | 3/6 | 76 |

For 1 success in 6 tasks, the Wilson 95% interval is approximately **3.0% to 56.4%** for every arm. Six tasks and a four-way tie do not support a treatment-effect inference.

## Interpretation and limitations

The pinned local 3B Q4 model/agent combination was not a reliable code-editing agent: sessions included provider/tool-parser HTTP 500 responses, internal timeouts, max-tool-step exhaustion, and assistant prose/code without repository edits. `f06` is a no-op task, so scorer correctness and clean agent exit are reported separately. These results do not establish how the treatments would behave with a stronger model or different runtime. Tokens and monetary cost are **NOT AVAILABLE**.

All arms made zero repository changes, so diff-size, dependency, and unrelated-churn metrics are tied at zero and do not demonstrate useful minimality. Diffcipline was slower than every other arm in this run.

## Raw evidence

`raw-canonical-evidence.tar.gz` contains all 24 task transcripts, stdout/stderr, scorer JSON, metadata, patches, status files, arm summaries, runtime provenance, accepted preflight output, matched-base audit, and the exclusion ledger. Duplicated fixture workspaces and `llama-server.log` are omitted; fixture source bytes remain versioned in the repository.

```sh
cd benchmarks/results/v0.1
sha256sum -c SHA256SUMS
tar -tzf raw-canonical-evidence.tar.gz
```

Run #25 (`33195457215`) is invalidated because the old preparer produced different ephemeral base commits across arms. Earlier hosted/local preflights are enumerated in `EXCLUSIONS.txt` inside the archive; none is counted as task evidence. Individual canonical tasks were not silently retried.
