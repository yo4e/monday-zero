# Keystone — Candidate Recovery and Ambiguity Decisions

_Date: 2026-07-15 (Asia/Tokyo)_

## Recovered candidate

The genesis mechanism set in commit `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e` described Keystone as a 5×5 game in which players place or shift stones, win by occupying the center and connecting it to two distinct board edges, and use orthogonal custodian capture to remove one bracketed enemy stone.

The initial screening selected Keystone because it combines a visible structural objective with reversible local tactics. It also recorded two risks before implementation: the rules could become too busy, and the center objective could dominate play.

No Keystone implementation, play result, or search result existed when the decisions below were made.

## Ambiguities in the original brief

The candidate description did not define:

- the starting position or number of stones;
- whether placement and shifting are both always available;
- shift distance and direction;
- whether captured stones return to reserve;
- whether capture is mandatory, optional, or multi-capture;
- whether only the newly arrived stone can complete a capture;
- the exact meaning of connecting the center to two edges;
- whether one corner stone may count as both edge contacts;
- the order of capture and victory checks;
- what happens when no move exists;
- how repetition or indefinite shifting is handled;
- whether a swap rule is present.

## Frozen v0.1 decisions

### Empty board and eight stones each

The board begins empty and each player owns eight stones. Sixteen total stones leave room for movement and tactical vacancies while allowing several plausible center-to-edge structures.

### One action per turn

A player either places one reserve stone on any empty cell or shifts one board stone by one orthogonal step into an empty cell. Placement does not require support. Shifting may break a component.

### Captures are local, mandatory, and singular

Only the stone that just arrived may complete a custodian bracket. If several enemy stones become bracketed, exactly one must be chosen and removed. Captured stones leave the game rather than returning to reserve.

This preserves the original phrase “remove a single enemy stone” and limits tactical volatility without making capture optional.

### Victory requires a center component and two separate edge contacts

One orthogonally connected component must contain C3 and two different friendly edge stones touching two different edges. Adjacent and opposite edge pairs are both valid. A corner cannot alone certify both edges; another edge stone is required.

### Resolution order

The action occurs, one mandatory capture is resolved if available, victory is checked, and only then is repetition checked for the next player-to-move position.

### Termination

A player with no legal placement or shift loses. The third occurrence of the same complete position is a draw. Board contents, reserve counts, and player to move define the position.

### No balancing rule in the baseline

Black moves first. Keystone v0.1 has no swap or pie rule. First-player advantage is a known risk to measure rather than repair before evidence.

## Pre-result sanity observations

- The core rules are under the study's 400-word limit.
- An uninterrupted win requires at least five stones: C3 plus two separate orthogonal routes to different edges. Black therefore cannot win before ply 9 by placement alone.
- Eight stones per player permit that minimum structure but do not fill the board.
- Captures and shifts create reversibility, unlike Span, while the repetition rule gives cyclic play a defined result.

These observations are design checks, not evidence of balance, depth, originality, or play quality.