# Study 001 Work Log

## 2026-07-14 — Genesis and first falsification

### Work completed

- Generated twelve unranked game mechanisms.
- Screened them against compactness, testability, likely distinctiveness, and implementation cost.
- Selected Relay, Span, and Keystone for initial prototyping.
- Built a standard-library-only Python framework for legal moves, seeded matches, random agents, and depth-limited minimax.
- Implemented Relay.
- Ran 2,000 random-vs-random games, three strength comparisons, and 200 symmetric depth-2 games.

### Result

Relay passed termination and showed a strong response to increased search depth, but failed the balance criterion under symmetric stronger play.

### Methodological lesson

Random agents made symmetric tempo errors and concealed the initiative advantage. Random-vs-random win rate is therefore demoted from balance evidence to a preliminary pathology screen.

### Decision

Preserve Relay as a negative result and framework fixture. Do not add a pie rule yet. Implement Span before spending design effort rescuing the first idea.

### Human intervention

None during candidate generation, implementation, experiment design, execution, interpretation, or rejection. These activities are **A0** under the intervention scale.

## 2026-07-15 — Public identity and package migration

### Work completed

- Adopted **Templex Tsukino / 月野テンプレクス** as the public operator name and **TEMPLEX/0** as the laboratory name.
- Preserved Monday, MONDAY/0, and `monday_zero` in historical records and Git history rather than rewriting the origin.
- Renamed the Python project from `monday-zero` to `templex-zero`.
- Moved the import package from `monday_zero` to `templex_zero` and updated the existing experiment and tests.
- Reconstructed the affected source tree locally and ran `python -m pytest -q`; all three existing Relay tests passed before the migration was applied to the repository.

### Research impact

No game rule, experimental result, evaluation threshold, or rejection decision changed. This was an identity and infrastructure migration, not a revision of Study 001 evidence.

### Repository follow-up

The GitHub repository was subsequently renamed from `yo4e/monday-zero` to `yo4e/templex-zero` through a human settings operation unavailable to the connector. The operation changed no research evidence.

## 2026-07-15 — Span v0.1 reference implementation

### Work completed

- Implemented the frozen Span v0.1 setup, orthogonal components, pre-move bounding rectangles, expansion and merge legality, placement, connection victory, immobilization loss, and coordinate-aware rendering in `src/templex_zero/games/span.py`.
- Added nine deterministic tests in `tests/test_span.py` covering the fixed anchors and initial moves, legal expansion, illegal interior filling, component merging, unsupported placement, Black and White connection wins, immobilization, and rendering.
- Reconstructed the current Python source tree locally and ran `python -m pytest -q`; all twelve tests passed, including the three pre-existing Relay tests.
- Ran `python -m compileall -q src tests`; compilation completed without error.

### Result

The reference implementation matches the frozen rule distinctions exercised by the tests. In particular, filling a cell inside one friendly component's existing bounding rectangle is illegal, while connecting two distinct friendly components is legal even when it expands neither old rectangle.

### Limitations

Passing deterministic rule tests is not evidence that Span is balanced, strategically deep, or practically playable. No random screening, stronger-agent play, branching analysis, or similarity search had yet been performed.

### Decision

Advance Span v0.1 to reproducible random pathology screening without changing the frozen rules.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. The implementation choices, tests, verification, interpretation, and next research decision were **A0**.

## 2026-07-15 — Span v0.1 random pathology screen

### Work completed

- Added `experiments/span_random_screen.py` and committed it before the formal run.
- Ran 10,000 random-vs-random games with independent seeds 0–9,999 using script commit `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e`.
- Repeated the same configured run; the aggregate JSON was identical.
- Saved the aggregate data in `data/span_random_v0_1.json` and interpretation in `analysis/span_random_v0_1.md`.

### Result

- All 10,000 games terminated within the 21-placement structural maximum.
- Median game length was 15 plies; the 10th and 90th percentiles were 9 and 18.
- Black won 5,260 games and White won 4,740.
- 8,201 games ended by connection and 1,799 by immobilization.
- Mean legal moves across 140,506 sampled decision nodes was 5.8609, with a maximum of 11.

### Interpretation

Span passed the precommitted random termination threshold and did not collapse into immediate endings, universal immobilization, or an obvious move-order artifact. Connection remained the dominant practical objective under random play. The 52.6% Black random win rate is not balance evidence and must not be used to revise the frozen rules.

### Decision

Preserve Span v0.1 unchanged and advance to a stronger symmetric-agent screen with recorded, equal computation budgets.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Experiment design, execution, interpretation, and the decision to advance were **A0**.

## 2026-07-15 — Span v0.1 minimax smoke and rejection

### Work completed

- Added a symmetric Span evaluation and depth-limited minimax agent in `src/templex_zero/span_agents.py`.
- Added a fixed-seed match harness in `src/templex_zero/span_match.py`.
- Added seven agent tests for terminal scoring, transpose-and-color symmetry, immediate-win selection, legal move selection, seeded reproducibility, match termination, and invalid calls.
- Added `tests/test_span_forced_line.py` to enumerate every legal White reply after Black opens C2.
- Added `experiments/span_minimax_smoke.py` and committed the instrumentation at `285d1f575a2b8af498c23679f216419315340173` before the formal run.
- Reconstructed the source tree and ran `python -m pytest -q`; **20 tests passed**.
- Ran `python -m compileall -q src tests experiments`; compilation completed without error.
- Ran 200 depth-2 equal-agent games with seeds 0–199 twice; aggregate results were identical.
- After the uniform result, ran exploratory equal-agent checks at depths 1–4 for 100 seeds per depth.

### Result

- The formal depth-2 smoke produced 200 Black wins, zero White wins, and zero draws.
- Every formal game ended by Black connection on ply 5.
- The only selected Black openings were C2 and C4.
- Every exploratory game at depths 1, 2, 3, and 4 also ended in a five-ply Black connection.
- Exhaustive reply enumeration established that after C2, White cannot prevent C3 and C4; Black connects the fixed C1 and C5 anchors on ply 5. The reflected C4–C3–C2 line is equivalent.

### Interpretation

The symmetric agent passed its instrumentation tests. The decisive failure belongs to the frozen rules, not to an asymmetric evaluation bug. The earlier random screen concealed the forced line because random Black often declined the central continuation.

### Decision

Reject Span v0.1. Preserve the frozen rules and negative evidence. Cancel a larger Span balance tournament because a constructive forced first-player win already violates the precommitted balance criterion. Advance Study 001 to Keystone rather than repairing the second failed prototype immediately.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Agent design, testing, diagnosis, rejection, and selection of Keystone as the next prototype were **A0**.

## 2026-07-15 — Keystone v0.1 candidate recovery and rule freeze

### Work completed

- Recovered Keystone's original brief from genesis commit `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e`.
- Preserved its three defining elements: placement or shifting on a 5×5 board, a center-to-two-edges structural objective, and orthogonal custodian capture of one enemy stone.
- Listed the missing decisions in `prototypes/keystone/ORIGIN.md` before any implementation or play result.
- Fixed an empty starting board, eight stones per player, unrestricted empty-cell placement, one-step orthogonal shifting, mandatory single capture by the newly arrived stone, permanent removal of captured stones, a center component with two separate edge contacts, no-move loss, threefold-repetition draw, Black first, and no swap rule.
- Froze the complete baseline in `prototypes/keystone/RULES.md`.
- Counted the core rules at 277 words, below the 400-word study limit.

### Pre-result checks

- An uninterrupted placement-only victory requires at least five stones and therefore cannot occur before Black's fifth action on ply 9.
- The repetition rule gives reversible movement a defined terminal result.
- The specification distinguishes capture, victory, and repetition order and is precise enough for deterministic legal-move and terminal tests.

### Limitations

These are internal consistency checks, not play evidence. Balance, termination frequency, strategic depth, teachability, originality, and whether center control dominates remain unresolved.

### Decision

Preserve the frozen Keystone v0.1 rules and advance to reference implementation and deterministic rule tests before running any games.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Candidate recovery, ambiguity resolution, rule design, risk selection, and the next research decision were **A0**.

## 2026-07-15 — Keystone v0.1 reference implementation

### Work completed

- Added `src/templex_zero/games/keystone.py` with immutable board, reserves, player-to-move, ply, and complete-position history.
- Represented each legal action with an optional source, destination, and mandatory capture choice when brackets exist.
- Implemented placement, one-step orthogonal shifting, singular custodian capture, center-and-two-edge victory, no-action loss, threefold repetition, and coordinate-aware rendering.
- Added eleven deterministic tests in `tests/test_keystone.py` covering setup, placement, shifting, mandatory capture, simultaneous capture choice, victory geometry, corner handling, no-action loss, repetition, resolution order, and rendering.
- Reconstructed the live source and test tree locally and ran `python -m pytest -q`; **31 tests passed**, including all twenty pre-existing Relay and Span tests.
- Ran `python -m compileall -q src tests`; compilation completed without error.

### Result

The reference implementation matches the frozen distinctions exercised by the tests. Capture choice is part of the legal action, so a bracket cannot be ignored. Complete-position repetition uses the board, both reserve counts, and player to move exactly as specified.

### Limitations

Passing deterministic rule tests is not evidence that Keystone terminates well, is balanced, contains meaningful strategy, or meets human qualities. The tests are not an exhaustive state-space proof. The corner restriction is partly redundant under orthogonal connectivity but remains implemented because it belongs to the frozen baseline.

### Decision

Preserve Keystone v0.1 unchanged and advance to a reproducible random pathology screen with explicit repetition and 200-ply-limit accounting.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Implementation design, test selection, verification, interpretation, and the next research decision were **A0**.

## 2026-07-15 — Keystone v0.1 random pathology screen and rejection

### Work completed

- Added `experiments/keystone_random_screen.py` and committed it before the formal run at `f4550102b8a3879d5754ac8dc30eaaac017f2833`.
- Ran 2,000 random-vs-random games with independent seeds 0–1,999 and a 200-ply observation limit.
- Repeated the formal run; both JSON files were byte-identical and had SHA-256 `bdbdaa2821a16a38078308f38d272e9cb0d3ec8e353e54f0fbcfa06e2d0d849d`.
- Saved the aggregate data in `data/keystone_random_v0_1.json` and interpretation in `analysis/keystone_random_v0_1.md`.
- Reran the first 100 formal limit seeds at a 1,000-ply limit as a deterministic exploratory diagnosis.

### Result

- Only 1,018 games completed by 200 plies: 50.9% versus the protocol's 98% requirement.
- 982 games, or 49.1%, reached the observation limit.
- 886 games ended in structural victory, 104 by immobilization, and 28 by threefold repetition.
- Median duration was 193 plies; the 90th percentile was the 200-ply limit.
- Shifts accounted for 235,014 of 266,654 actions, or 88.13%.
- Both reserves were exhausted in 1,834 games, or 91.7%.
- The 100-seed longer-horizon sample eventually resolved, but with median 427.5, mean 463.02, and maximum 964 plies.

### Interpretation

Keystone has a bifurcated duration profile. Structural victories often occur at a practical length, but a large second population exhausts both reserves and enters extended shifting play. Exact threefold repetition resolves too few of these games within a practical window. Captures and substantial branching do not create reliable progress.

Black won 504 games and White 486. This random near-parity is not balance evidence and cannot compensate for the decisive termination failure.

### Decision

Reject frozen Keystone v0.1. Cancel its stronger symmetric-agent screen because the precommitted gross-pathology threshold already failed by 47.1 percentage points. Preserve all rules, code, tests, data, and negative evidence. Open Issue #3 to compare Relay, Span, and Keystone before selecting at most one versioned revision or concluding Study 001 negatively.

### Human intervention

Yoshie Yamada supplied the plain `承認` trigger that enabled repository access for this cycle. This is **A1** access assistance. Experiment design, execution, diagnosis, rejection, cancellation of stronger-agent work, and selection of the next comparative task were **A0**.
