# Study 002 Final Report — Exact-First Screening of Compact Games

_Date closed: 2026-07-18 (Asia/Tokyo)_  
_Disposition: **partial / incomplete methodological result**_

## Abstract

Study 002 tested whether an exact-analysis pipeline could reveal opening structure that aggregate random play misrepresented in a frozen family of autonomously generated compact deterministic placement games.

The study generated and froze eighteen candidates before outcome inspection, validated a memoized exact solver against an independently written retrograde oracle on hand-audited fixtures, solved fifteen candidates under precommitted resource caps, and ran 36,000 fixed-seed random games. Six candidates met a pre-defined false-reassurance condition: random first-participant win rates fell between 40% and 60%, while exact analysis found either a decisive forced result within eight plies or no non-losing opening for the first participant.

This supports the claims that random aggregate rates can conceal short forced results and concentrated opening structure, and that exact opening analysis can provide clearer structural rejection reasons. However, the study failed to freeze its shallow-search heuristic before exact outcomes were inspected. The required depth-1/2/3 comparison therefore could not be conducted honestly, leaving H2 unresolved and preventing a fully successful methodological disposition.

The final result is consequently **partial / incomplete**: H1 and H3 are supported by valid precommitted evidence; H2 was not evaluated because of a protocol-design sequencing failure.

## 1. Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluated a screening method. It did not attempt to certify a publishable game and did not treat exact solvability, random balance, or short rules as evidence of fun, fairness, elegance, strategic depth, teachability, accessibility, or originality.

## 2. Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

Failure to support a hypothesis was permitted. A result of zero false-reassurance cases would also have been valid.

## 3. Frozen candidate family

The candidate family was fixed before any candidate outcome was inspected.

- Eighteen deterministic placement games.
- Nine on 3×3 boards and nine on 4×4 boards.
- Three mechanism families: adjacency-constrained growth, component expansion or merger, and local blocking or pattern completion.
- Exactly three candidates in every board-size × mechanism-family cell.
- No movement, capture, swap, chance, hidden information, scoring, repetition, or pass.
- At most sixteen placements.
- Core generated rules at or below 250 words.

The grammar, generation seed `2026071602`, canonical serialization, SHA-256 ordering, and all selected tuples were frozen before evaluation. No candidate was manually ranked, replaced, repaired, or polished.

Frozen manifest compact-entry SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## 4. Exact instrument

### 4.1 Solver

The primary instrument was a standard-library-only, full-width memoized solver without symmetry reduction. It returned:

- exact outcome from the participant-to-move perspective;
- outcome-preserving terminal distance;
- the value of every legal opening;
- winning, drawing, and losing opening counts;
- expanded-state count;
- explicit state-cap or time-cap status.

Outcome order was `win > draw > loss`. Among outcome-preserving choices, wins selected the shortest distance, losses the longest, and draws the shortest as a deterministic convention. A capped solve published no partial root or opening value.

### 4.2 Correctness gate

Before any frozen candidate was solved, the memoized solver was compared with an independently written instrument that first constructed the reachable graph with a queue and then performed retrograde evaluation in descending ply order.

The two implementations agreed on every reachable state and legal action of four frozen hand-audited fixtures: twelve states in total. They also agreed on terminal distances, state counts, cap behavior, and the two retained symmetry claims.

This gate established correctness evidence on the fixture domain. It did not prove correctness for all larger candidates.

## 5. Exact candidate screen

The formal exact experiment was committed before candidate outcomes were inspected:

`9a453ccc2a2e1f30691d23028b12b3296ebb4f13`

Frozen limits were:

- 2,000,000 expanded states per candidate;
- 30 measured seconds per candidate;
- 25,000,000 expanded states across the study;
- manifest-order execution;
- at least twelve exact solutions required for continuation;
- capped candidates remained unsolved and caps could not be raised.

### 5.1 Exact result

| Measure | Result |
|---|---:|
| Frozen candidates | 18 |
| Exactly solved | 15 |
| Time-capped | 3 |
| 3×3 solved | 9 / 9 |
| 4×4 solved | 6 / 9 |
| First-participant exact wins | 9 |
| First-participant exact losses | 6 |
| Exact draws | 0 |
| Decisive within 2 optimal plies | 4 / 15 |
| Decisive within 8 optimal plies | 14 / 15 |
| Zero non-losing openings | 6 / 15 |

The minimum of twelve exact solutions passed. The precommitted degenerate-grammar condition did not trigger because only four of fifteen solved candidates terminated within two optimal plies.

The three unsolved candidates were:

- `S2-4-CE-02`;
- `S2-4-LB-01`;
- `S2-4-LB-03`.

All three reached the 30-second wall-clock cap rather than the state cap.

### 5.2 Opening structure

Six candidates were exact first-participant losses with no non-losing opening:

- `S2-3-AG-01` — loss in 2, 0 / 9 non-losing openings;
- `S2-3-AG-02` — loss in 6, 0 / 9;
- `S2-3-CE-02` — loss in 2, 0 / 3;
- `S2-3-CE-03` — loss in 6, 0 / 9;
- `S2-4-AG-03` — loss in 2, 0 / 4;
- `S2-4-CE-03` — loss in 2, 0 / 16.

Among exact first-participant wins, opening concentration varied substantially. Four candidates had every opening winning. `S2-3-LB-01` and `S2-3-LB-02` had five winning openings out of nine. `S2-4-AG-01` and `S2-4-CE-01` had only one winning opening out of four. `S2-4-LB-02` had twelve winning openings out of sixteen and was the only solved candidate with an optimal root distance greater than eight plies.

### 5.3 Exact repeated execution

Two configured runs agreed on:

- every solved root outcome and distance;
- every solved opening value;
- every solved reachable-state count;
- solved and unsolved classification;
- every cap reason.

The original report projection incorrectly classified the number of states expanded before a wall-clock time cap as deterministic. Those counts varied slightly for the three time-capped candidates. A separately committed comparator excluded only wall-clock-dependent fields from the reproducibility projection while preserving the raw measurements.

Corrected normalized SHA-256 for both runs:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

This was a post-run correction to reproducibility classification, not a change to candidate rules, caps, exact values, or dispositions.

## 6. Random screen

The random experiment was specified and committed before play:

`970b5a7b35b40806b8962c4a73d3841804a95e7a`

For each candidate, exactly 2,000 independent games were played. Each game used a seed derived from the frozen manifest hash, manifest index, and game index. Every move was selected uniformly from the current legal actions. The experiment imported neither exact results nor shallow-search code and used no candidate-specific policy.

### 6.1 Aggregate random result

| Measure | Result |
|---|---:|
| Candidates | 18 |
| Games | 36,000 |
| First-participant wins | 17,656 |
| Second-participant wins | 18,344 |
| Draws | 0 |
| Goal endings | 19,715 |
| No-legal-action endings | 16,285 |
| Mean plies | 6.8161 |
| Mean legal actions per decision point | 5.1395 |

Every random game terminated. Because these were finite placement-only games with at most sixteen placements, termination is not evidence of balance or strategic quality.

### 6.2 Random repeated execution

The experiment file used for the final executions was byte-identical to live GitHub blob:

`051ab0fa3de409c38adf35d327ade8111ae597d8`

Two complete runs agreed on every deterministic field and produced:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

Measured run times were approximately 52.92 and 52.98 seconds.

## 7. Exact-versus-random comparison

The comparison was performed only after both random outputs were complete.

The frozen false-reassurance definition required:

1. a random first-participant decisive win rate between 40% and 60%; and
2. either an exact decisive result within eight plies or zero non-losing openings.

### 7.1 False-reassurance cases

| Candidate | Random first rate | Exact root | Exact distance | Non-losing openings |
|---|---:|---|---:|---:|
| `S2-3-AG-02` | 54.90% | loss | 6 | 0 / 9 |
| `S2-3-AG-03` | 59.60% | win | 5 | 3 / 3 |
| `S2-3-CE-03` | 56.15% | loss | 6 | 0 / 9 |
| `S2-4-AG-01` | 51.55% | win | 7 | 1 / 4 |
| `S2-4-AG-02` | 58.85% | win | 7 | 4 / 4 |
| `S2-4-CE-01` | 52.50% | win | 7 | 1 / 4 |

Nine candidates appeared in the 40–60% interval under random play. Seven of those were exactly solved. Six of the seven met the pre-defined false-reassurance condition.

The remaining solved candidate in that interval, `S2-4-LB-02`, was an exact first-participant win in nine plies with twelve non-losing openings out of sixteen. It did not meet the frozen diagnostic threshold. The three exact-unsolved candidates were not classified; failure to solve was not converted into evidence of balance or pathology.

### 7.2 Strong examples

`S2-3-AG-02` produced 54.9% random first-participant wins but was an exact second-participant win in six plies after every one of the nine legal openings. Random second participants frequently failed to continue the winning structure, allowing the losing side to win a majority of random games.

`S2-4-AG-01` produced 51.55% random first-participant wins but had only one winning opening among four. The aggregate rate concealed both the forced root result and extreme concentration of viable first moves.

These are two distinct forms of misrepresentation: random rates can obscure which participant has the forced result, and they can obscure how narrowly optimal play is concentrated among openings.

## 8. Hypothesis disposition

### H1 — supported

Six candidates met the exact pre-defined false-reassurance condition. Random aggregate rates near 50% coexisted with short exact forced outcomes, complete opening losses, or sharply concentrated viable openings.

### H2 — unresolved

No formal shallow depth-1/2/3 evidence exists. The frozen proposal required the shallow-search heuristic to be generated from declarative rule features before exact results were inspected. Cycles 1–3 did not freeze a heuristic, and exact outcomes were then inspected in cycle 4.

A heuristic authored afterward could not honestly satisfy the pre-result requirement. No post-result substitute was created or represented as precommitted evidence. Consequently the study cannot determine whether increasing shallow depth reduces disagreement with exact opening analysis.

### H3 — supported

Exact opening analysis supplied clearer structural explanations than aggregate random rates for multiple candidates. It distinguished all-opening losses, short forced outcomes, one-opening-only survival, and broader winning-opening sets. Random win rates alone did not provide those rejection or structural reasons.

## 9. Procedural failures

### 9.1 Shallow-heuristic sequencing failure

The most consequential failure was in protocol sequencing. The proposal required a heuristic to be frozen before exact inspection, while the activation plan scheduled exact solving before approximate-screen implementation. No heuristic was frozen before exact results became known.

This defect did not invalidate the exact values or the already specified random experiment. It did invalidate the intended shallow-search component and prevented full methodological success.

The study was not extended to repair the defect. No retroactive heuristic, second grammar, candidate replacement, or additional cycle was authorized.

### 9.2 Exact reproducibility projection defect

The initial exact report projection included expanded-state counts observed before wall-clock time caps. These counts are timing-dependent and differed slightly between repeated runs. The error was isolated and corrected transparently without changing any result, rule, cap, or classification.

### 9.3 Repository write corrections

During cycle 4 synchronization, two connector calls intended as checks temporarily replaced the Study README and `STATE.md` with abbreviated content. Both files were immediately restored from their complete prior contents, and the erroneous and corrective commits remain visible. An unrelated-SHA update attempt was rejected by GitHub and made no change. No experiment, manifest, result, or interpretation was altered.

## 10. Verification and reproducibility limits

- The exact solver passed a small frozen-fixture correctness gate against an independent implementation; this does not prove universal correctness on larger games.
- Fifteen candidates were solved under frozen caps; three 4×4 candidates remained unsolved.
- The exact repeated-run comparison agreed on all exact and classification fields after excluding only wall-clock-dependent fields from the deterministic projection.
- The final random experiment source was byte-identical to its GitHub blob and produced identical deterministic output in two complete runs.
- Functional local reconstructions reproduced the frozen manifest hash and expected fixture behavior, but byte-identical identity of every reconstructed dependency is not claimed.
- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- The repository had no recorded GitHub Actions workflow.
- An initial combined random execution exceeded an outer command timeout and produced no complete output file; it was excluded from evidence.

## 11. Claims not supported

This study does not establish that any candidate is:

- fun or engaging;
- fair under competent play;
- strategically deep;
- elegant or teachable;
- accessible;
- original or distinct from prior games;
- suitable for publication or product development.

Random win rates are not balance evidence. Exact solvability is not game quality. A forced result does not by itself establish triviality for human players, although short forced results and concentrated openings are valid structural rejection evidence for the present screening question.

## 12. Methodological findings

1. **Aggregate random balance can be actively misleading.** In this sample, six of seven exactly solved candidates that appeared 40–60% under random play met the frozen false-reassurance definition.
2. **Opening values carry information hidden by root win rates.** A root win with one viable opening is materially different from a root win with every opening viable, even when random rates are similar.
3. **Exact-first screening can provide sharper rejection reasons.** Complete opening loss, short forced distance, and opening concentration are directly interpretable structural findings.
4. **Resource-capped exact analysis remains useful when partial.** Fifteen exact solutions were sufficient for valid comparisons, while unsolved candidates were left unclassified rather than inferred from random play.
5. **Precommitment dependencies must be ordered, not merely listed.** Requiring a pre-result heuristic is ineffective if the execution plan allows exact inspection before the heuristic is frozen.
6. **Reproducibility projections must distinguish computational outcomes from wall-clock traces.** Values and classifications may be deterministic even when work completed before a time cap is not.

## 13. Final disposition

Study 002 is closed as a **partial / incomplete methodological result**.

- **H1 supported** by six pre-defined false-reassurance cases.
- **H2 unresolved** because the required pre-result shallow heuristic was never frozen.
- **H3 supported** because exact opening analysis supplied structural explanations hidden by aggregate random rates.
- The exact instrument, frozen manifest, exact screen, random screen, and exact-versus-random comparison produced valid bounded evidence.
- The intended shallow-depth comparison was not performed and cannot be restored as precommitted evidence after exact inspection.

The study therefore answers a narrower question affirmatively: TEMPLEX/0 built and operated an exact-first pipeline that measured multiple cases where random play misrepresented opening structure. It did not complete the full planned comparison between random, shallow, and exact evaluation.

No candidate is advanced as a finished game. No active study follows automatically from this closure, and Study 003 is not started in this cycle.
