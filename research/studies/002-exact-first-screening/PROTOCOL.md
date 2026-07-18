# Study 002 Protocol — Exact-First Screening of Compact Games

_Date activated: 2026-07-16 (Asia/Tokyo)_  
_Date closed: 2026-07-18 (Asia/Tokyo)_  
_Status: **Closed — partial / incomplete methodological result**_

## Authority and frozen source

This protocol implemented the frozen proposal:

- `research/proposals/STUDY_002_EXACT_FIRST_SCREENING.md`
- final pre-result proposal commit: `68fc4c2edb93ca1363e7b7040221b5507cfeb171`

The research question, candidate family, exact caps, random-game count, false-reassurance definition, stopping boundaries, and six-cycle limit were frozen. Recorded defects did not authorize retroactive repair.

The final synthesis is:

- `research/studies/002-exact-first-screening/REPORT.md`

## Research question

> Can Templex Tsukino build and use an exact-analysis pipeline that measures when random and shallow symmetric play misrepresent the opening structure of autonomously generated compact deterministic placement games?

The study evaluated a screening method. It did not treat exact solvability or random rates as evidence of fun, elegance, fairness, strategic depth, teachability, accessibility, or originality.

## Precommitted hypotheses

- **H1:** Some candidates that appear approximately balanced under random play will contain short exact forced outcomes or highly concentrated optimal openings.
- **H2:** Increasing shallow search depth will reduce, but not necessarily eliminate, disagreement with exact opening analysis.
- **H3:** Exact-first analysis will provide a clearer rejection reason than aggregate win rates for at least some candidates.

## Frozen candidate family

- Eighteen deterministic placement games.
- Nine on 3×3 and nine on 4×4.
- Three mechanism families.
- Exactly three candidates in every board-size × family cell.
- No movement, capture, swap, chance, scoring, repetition, or pass.
- At most sixteen placements.
- Core rules at or below 250 words.
- No manual ranking, replacement, repair, or polishing after generation.

Frozen manifest compact-entry SHA-256:

`cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee`

## Exact-analysis instrument

The primary instrument was a full-width memoized solver without symmetry reduction. It returned participant-to-move outcome, outcome-preserving distance, every opening value, opening counts, expanded-state count, and cap status.

Outcome order was `win > draw > loss`. Wins selected the shortest outcome-preserving distance, losses the longest, and draws the shortest as a deterministic convention. Capped solves published no partial root value.

Before candidate solving, the solver agreed with an independently written queue-built retrograde oracle on all twelve reachable states of four frozen fixtures, all action values, state counts, cap behavior, and retained symmetry claims.

## Frozen exact resource boundaries

- Maximum 2,000,000 expanded states per candidate.
- Maximum 30 measured seconds per candidate.
- Maximum 25,000,000 expanded states across the study.
- Frozen manifest order.
- At least twelve exact solutions required.
- Capped candidates remained unsolved; caps could not be raised.

## Exact result

Formal experiment commit:

`9a453ccc2a2e1f30691d23028b12b3296ebb4f13`

- 15 of 18 candidates solved exactly.
- All nine 3×3 and six of nine 4×4 candidates solved.
- Nine first-participant exact wins, six losses, no draws.
- Four of fifteen decisive within two optimal plies.
- Fourteen of fifteen decisive within eight optimal plies.
- Six candidates had zero non-losing openings.
- Three candidates reached the 30-second time cap.
- The minimum-solved threshold passed.
- The degenerate-majority failure condition did not trigger.

Corrected repeated-run normalized SHA-256:

`9cc17bd02dee865d1e20c67d72a975a04ec36b131d9dfb8bf17de24e6f381eb1`

## Frozen random screen

- 2,000 games per candidate.
- Independent fixed seeds derived from manifest hash, manifest index, and game index.
- Uniform choice among current legal actions.
- Participant result, duration, terminal reason, opening distribution, and branching recorded.
- No exact value or candidate-specific policy used in move selection.

Formal experiment commit:

`970b5a7b35b40806b8962c4a73d3841804a95e7a`

- 36,000 games completed.
- 17,656 first-participant wins.
- 18,344 second-participant wins.
- No draws.
- 19,715 goal endings.
- 16,285 no-legal-action endings.
- Mean duration 6.8161 plies.

Repeated-run deterministic SHA-256:

`d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`

## Exact-versus-random definition and result

A false-reassurance case was an exactly solved candidate with a random first-participant decisive rate from 40% through 60% while exact analysis found either a decisive forced result within eight plies or zero non-losing openings.

Six candidates met the definition:

- `S2-3-AG-02`;
- `S2-3-AG-03`;
- `S2-3-CE-03`;
- `S2-4-AG-01`;
- `S2-4-AG-02`;
- `S2-4-CE-01`.

Nine candidates appeared 40–60% under random play. Seven were exactly solved, and six of those seven were false-reassurance cases.

## Shallow screen — formally unavailable

The frozen proposal required the shallow-search heuristic to be generated from declarative rule features before exact outcomes were inspected. No heuristic was frozen in cycles 1–3, and exact results were inspected in cycle 4.

Therefore:

- no post-result heuristic was represented as precommitted;
- the formal depth-1/2/3 screen was cancelled;
- H2 remained unresolved;
- the full methodological-success condition could not be met.

This was a protocol-design failure, not permission to change the proposal or extend the study.

## Final hypothesis disposition

- **H1: supported by valid evidence.** Six pre-defined false-reassurance cases were observed.
- **H2: unresolved.** The required pre-result heuristic did not exist.
- **H3: supported by valid evidence.** Exact opening analysis supplied clearer structural explanations than aggregate random rates.

## Cycle record

- Cycle 1: protocol, schema, fixtures, grammar, seed — complete.
- Cycle 2: deterministic manifest freeze — complete.
- Cycle 3: exact-instrument correctness gate — complete.
- Cycle 4: frozen exact candidate screen — complete.
- Cycle 5: frozen random screen and exact comparison — complete.
- Cycle 6: synthesis and closure — complete.

## Final disposition and boundaries

Study 002 closed as a **partial / incomplete methodological result**.

The study may not expand into a retroactive heuristic, second grammar, candidate replacement, symmetry rescue, game polishing, prior-art review, human playtesting, paid compute, external solver, or product development. Future factual or technical corrections must preserve the frozen evidence and disclose the correction.

Study 003 was not started in the closure cycle.

## Verification limitations

- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- Functional reconstructions reproduced the frozen manifest hash and expected fixture behavior, but byte-identical identity of every dependency is not claimed.
- The final random experiment script was byte-identical to its live GitHub blob.
- The repository had no recorded GitHub Actions workflow.

## Intervention model

A plain project-chat `承認` supplied A1 access assistance for each bounded cycle. Templex selected implementation details, interpretation, failure diagnosis, and stopping decisions. External communication, publication, spending, permission changes, third-party actions, and human-subject activity remained separately gated.
