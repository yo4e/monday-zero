# Span v0.1 Random Pathology Screen

_Date: 2026-07-15 (Asia/Tokyo)_

## Question

Does the frozen Span v0.1 implementation terminate reliably under ordinary random legal play, and does it show an obvious gross pathology before stronger-agent evaluation?

This screen is deliberately limited. Random-play win rates are **not** evidence of strategic balance; Relay already demonstrated that random agents can conceal a severe initiative advantage.

## Method

- Script: `experiments/span_random_screen.py`
- Script/code version: `d1ed92b0a6ada87e8aef7c479ca4a38ab6d01f9e`
- Python: 3.13.5
- Games: 10,000
- Seeds: 0 through 9,999 inclusive
- One independent `random.Random(seed)` instance per game
- Both players selected uniformly from their current legal moves
- The same configured run was executed twice locally; the resulting aggregate JSON was identical
- Raw aggregate data: `../data/span_random_v0_1.json`

## Results

| Measure | Result |
|---|---:|
| Completed games | 10,000 / 10,000 |
| Games within 200 plies | 10,000 / 10,000 |
| Minimum plies | 5 |
| 10th percentile | 9 |
| Median plies | 15 |
| Mean plies | 14.0506 |
| 90th percentile | 18 |
| Maximum plies | 21 |
| Black wins | 5,260 (52.6%) |
| White wins | 4,740 (47.4%) |
| Connection endings | 8,201 (82.01%) |
| Immobilization endings | 1,799 (17.99%) |
| Mean legal moves per decision | 5.8609 |
| Median legal moves per decision | 6 |
| Maximum legal moves | 11 |

The six legal Black openings occurred between 1,586 and 1,735 times each. No single opening dominated the random sampler through an implementation or ordering accident.

## Interpretation

### Termination

Span passes the precommitted random termination threshold. Every game terminated, and the rules themselves cap play at 21 placements because four cells are occupied initially and no stone moves or leaves the board.

### Practical duration

The random sample is compact without collapsing almost immediately. Median play was 15 plies, with 80% of games between 9 and 18 plies. This sits inside the protocol's intended practical range of 8–80 plies for typical completed games.

### Outcome mode

Connection, not immobilization, produced the large majority of random outcomes. Immobilization is therefore relevant but does not appear to replace the nominal connection objective under random play.

### Branching

The mean branching factor was about 5.86 across 140,506 sampled decision nodes. It rose above seven in the early-middle game and then declined as the board filled. This is enough local choice to justify stronger search, but it does not establish strategic depth.

### Seat result

Black won 52.6% of random games. This is not interpreted as evidence that Span is balanced or nearly balanced. Random agents are only a pathology instrument here, and a stronger symmetric-agent screen remains mandatory.

## Decision

Span v0.1 shows no gross random-play pathology requiring immediate rejection or rule revision. Preserve the frozen rules and advance to a stronger symmetric-agent screen.

The next experiment should add a Span-specific evaluation and search agent, compare equal search budgets from both seats, and record decisive win rates, draws if any, computation budget, and reproducibility settings. The random results must not be used to tune or rewrite v0.1 before that test.

## Limitations

- Random legal play does not model competent strategy.
- Aggregate statistics do not reveal whether one or more openings are strategically forced.
- No exhaustive search or solved-state claim has been made.
- The current screen used a local reconstruction rather than GitHub Actions; no remote CI workflow exists.
- Fun, teachability, elegance, and originality remain untested.
