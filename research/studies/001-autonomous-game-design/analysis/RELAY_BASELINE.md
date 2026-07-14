# Relay Baseline Analysis

_Date: 2026-07-14_

## Result

Relay is **rejected in its current form** before deeper investment.

## Evidence

### Random play appears deceptively healthy

Across 2,000 random-vs-random games:

- Player 0 wins: 1,003
- Player 1 wins: 997
- Mean duration: 31.5715 plies
- Maximum duration: 91 plies
- Draws at 200-ply limit: 0

This would pass a superficial balance and termination check.

### Search strength produces a clear strategic signal

Across 200 games per depth, split evenly between seats:

- Depth 1 beats random 131–69.
- Depth 2 beats random 154–46.
- Depth 3 beats random 184–16.

This indicates that choices matter and that the baseline heuristic can exploit nonrandom structure.

### Symmetric stronger play exposes a first-player defect

Across 200 depth-2-vs-depth-2 games with randomized tie-breaking:

- Player 0 wins: 129
- Player 1 wins: 12
- Draws at 200 plies: 59

Among decisive games, Player 0 wins approximately 91.5%. This fails the precommitted 40–60% balance target by a wide margin. The high draw rate also suggests cycling or blocked formations under stronger play.

## Interpretation

Random balance was not diagnostic. Both random players waste tempo symmetrically, masking the initiative advantage. Once agents value progress and mobility, the first move becomes disproportionately valuable.

The result also reveals a protocol issue: balance should not be screened only with random play, even at the earliest stage.

## Decision

Do not tune Relay immediately. A pie rule or opening restriction might repair balance, but adding a standard balancing device before comparing the other prototypes would spend effort rescuing the first implemented idea.

Relay remains preserved as:

- a failed prototype;
- a test fixture for the shared framework;
- evidence that the research loop can reject an attractive mechanism.

Proceed to Span.

## Limitations

- The minimax heuristic is hand-designed and may exaggerate or misread strategic value.
- Depth 2 is not strong enough to establish the game's true value.
- The design has not undergone a formal similarity search against existing race games.

These limitations weaken any global claim about Relay, but they do not rescue it under the study's own practical evaluation protocol.
