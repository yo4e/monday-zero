# Initial Screening

_Date: 2026-07-14_

## Selected for prototyping

### Relay

- Very short rules.
- Straightforward legal-move generation.
- Connectivity constraint may create nonlocal consequences.
- Main risk: resemblance to race/capture games and severe first-player advantage.

### Span

- Distinctive expansion restriction.
- Can share grid and search infrastructure with Relay.
- Easy to visualize and test.
- Main risk: the restriction may reduce rather than deepen meaningful choice.

### Keystone

- Combines structural victory with local tactics.
- Captures allow reversibility and interaction absent from pure placement games.
- Main risk: rules may become too busy, and the center objective may dominate all other play.

## Deferred

- **Echo Step:** elegant and easy to implement, but likely close to known constrained-geography games and may be shallow on a 5×5 board.
- **Ravel:** promising, but loop detection and branch-removal language need formal clarification before fair evaluation.
- **Counterweight:** conceptually interesting but currently too opaque to teach quickly.

## Rejected in current form

- **Tidepool:** row/column shifting creates bookkeeping and has strong family resemblance to existing shift-and-align games.
- **Pulse:** propagation rule is concise but likely produces excessive board volatility and difficult causal reading.
- **Hinge:** physical representation and move generation are cumbersome relative to expected payoff.
- **Mosaic:** separating player identity from color weakens intuitive ownership and complicates evaluation.
- **Rift:** scoring and shared-pawn movement create a larger design burden than appropriate for the first cycle.
- **Thread:** loop cutting and planar geometry exceed the compactness target.

## Prototype order

1. Relay — quickest falsification target.
2. Span — pure placement comparison.
3. Keystone — more complex fallback if simpler mechanisms prove shallow.
