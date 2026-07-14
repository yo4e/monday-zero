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
