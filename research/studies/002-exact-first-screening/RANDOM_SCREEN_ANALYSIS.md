# Study 002 Random Screen and Exact Comparison

_Date: 2026-07-17 (Asia/Tokyo)_  
_Status: **Random cycle 5 of at most 6 complete; six pre-defined false-reassurance cases**_

## Scope

This cycle ran only the frozen random screen. It did not implement or run shallow search, alter any candidate, or use exact values in move selection.

The experiment was committed before play:

- experiment commit: `970b5a7b35b40806b8962c4a73d3841804a95e7a`;
- targeted-test commit: `62cdbb8efd7edc39424396d74b7a00c2cbdad890`;
- frozen manifest SHA-256: `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`;
- games: exactly 2,000 per candidate, 36,000 total;
- move choice: uniform among the current legal actions;
- game seed: first unsigned 64 bits of SHA-256 over the frozen namespace, manifest hash, manifest index, and game index.

The complete aggregate result is `data/random_screen_v1.json`.

## Reproducibility

The GitHub-stored experiment file had Git blob SHA `051ab0fa3de409c38adf35d327ade8111ae597d8`, which matched the locally executed file exactly.

Two complete executions agreed on every deterministic field and produced the same SHA-256:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

Measured run times were approximately 52.92 and 52.98 seconds.

## Aggregate random result

| Measure | Result |
|---|---:|
| Candidates | 18 |
| Games | 36,000 |
| First-participant wins | 17,656 |
| Second-participant wins | 18,344 |
| Draws | 0 |
| Goal endings | 19,715 |
| No-legal-action endings | 16,285 |
| Mean plies over all games | 6.8161 |
| Mean legal actions over all decision points | 5.1395 |

Every random game terminated. This follows from the finite placement-only design as well as the observed runs; it is not evidence of balance.

## Candidate-level comparison

The exact comparison was performed only after both random outputs were complete.

| Candidate | Random first rate | Exact root | Exact distance | Non-losing openings | False reassurance |
|---|---:|---|---:|---:|---|
| `S2-3-AG-01` | 0.0000 | loss | 2 | 0 / 9 | no |
| `S2-3-AG-02` | 0.5490 | loss | 6 | 0 / 9 | **yes** |
| `S2-3-AG-03` | 0.5960 | win | 5 | 3 / 3 | **yes** |
| `S2-3-CE-01` | 1.0000 | win | 5 | 3 / 3 | no |
| `S2-3-CE-02` | 0.0000 | loss | 2 | 0 / 3 | no |
| `S2-3-CE-03` | 0.5615 | loss | 6 | 0 / 9 | **yes** |
| `S2-3-LB-01` | 0.7285 | win | 5 | 5 / 9 | no |
| `S2-3-LB-02` | 0.7200 | win | 5 | 5 / 9 | no |
| `S2-3-LB-03` | 0.7575 | win | 5 | 3 / 3 | no |
| `S2-4-AG-01` | 0.5155 | win | 7 | 1 / 4 | **yes** |
| `S2-4-AG-02` | 0.5885 | win | 7 | 4 / 4 | **yes** |
| `S2-4-AG-03` | 0.0000 | loss | 2 | 0 / 4 | no |
| `S2-4-CE-01` | 0.5250 | win | 7 | 1 / 4 | **yes** |
| `S2-4-CE-02` | 0.6070 | unsolved | — | — | unavailable |
| `S2-4-CE-03` | 0.0000 | loss | 2 | 0 / 16 | no |
| `S2-4-LB-01` | 0.5705 | unsolved | — | — | unavailable |
| `S2-4-LB-02` | 0.5330 | win | 9 | 12 / 16 | no |
| `S2-4-LB-03` | 0.5760 | unsolved | — | — | unavailable |

The frozen definition labels an exactly solved candidate as false reassurance when random play gives a 40–60% first-participant decisive rate while exact analysis finds either a forced decisive result within eight plies or zero non-losing openings.

Six candidates meet that definition:

- `S2-3-AG-02`;
- `S2-3-AG-03`;
- `S2-3-CE-03`;
- `S2-4-AG-01`;
- `S2-4-AG-02`;
- `S2-4-CE-01`.

Nine candidates had random first-participant rates between 40% and 60%. Seven of those were exactly solved; six of the seven were false-reassurance cases. The remaining solved case, `S2-4-LB-02`, was an exact first-participant win in nine plies with twelve non-losing openings out of sixteen, so it did not meet the frozen diagnostic definition.

The three exact-unsolved candidates cannot be classified as false reassurance even when their random rates appear near the interval. Solver failure is not treated as evidence of balance or pathology.

## Strong examples

`S2-3-AG-02` looked nearly balanced under random play at 54.9% first-participant wins, but exact analysis found a second-participant forced win in six plies after every one of the nine legal openings.

`S2-3-CE-03` similarly produced 56.15% random first-participant wins while exact analysis found a loss in six with zero non-losing openings.

`S2-4-AG-01` produced 51.55% random first-participant wins, yet only one of its four openings was winning and the exact root was a forced first-participant win in seven. Random aggregate balance concealed both the forced outcome and the concentration of viable openings.

These examples demonstrate distinct ways that random aggregate rates can misrepresent opening structure: they can hide which participant has a forced result, and they can hide extreme concentration among opening choices.

## Hypotheses after valid evidence

- **H1 supported.** The study precommitted that some approximately balanced random results would contain short exact forced outcomes or highly concentrated optimal openings. Six pre-defined false-reassurance cases were observed.
- **H3 supported.** Exact analysis supplied clearer rejection or structural reasons than aggregate random rates for multiple candidates, including complete opening loss and one-opening-only survival.
- **H2 unresolved.** The shallow heuristic was not frozen before exact inspection, so no formal depth-1/2/3 evidence exists and no post-result substitute will be created.

These classifications remain subject to final synthesis in cycle 6.

## Limits

- Random play is not a model of competent human or machine play.
- The 40–60% interval is a diagnostic trigger, not proof of fairness outside the labelled cases.
- Three 4×4 candidates remain exact-unsolved under the frozen time cap.
- The local execution used a functionally reconstructed schema and manifest whose manifest hash matched the live repository. The experiment script itself was byte-identical to the GitHub blob, but byte-identical identity of every reconstructed dependency is not claimed.
- Fresh clone remained unavailable because the environment could not resolve `github.com`.
- The repository has no recorded GitHub Actions workflow.

## Decision

The valid random-versus-exact comparison is complete. Do not add shallow search, another grammar, candidate repair, human playtesting, or prior-art work.

Cycle 6 must synthesize the exact instrument, fifteen exact solutions, random evidence, six false-reassurance cases, H1 and H3 support, H2 non-evaluation, reproducibility corrections, and the heuristic sequencing defect. Then close Study 002 as partial/incomplete rather than fully successful.
