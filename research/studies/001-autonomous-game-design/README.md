# Study 001 — Autonomous Game Design

_Status: **Closed — negative research conclusion**_  
_Final report: [`REPORT.md`](REPORT.md)_

## Research question

Can Templex Tsukino independently design a compact, deterministic, two-player abstract strategy game whose rules are teachable in under three minutes and whose automated play provides evidence of nontrivial strategy and reasonable balance?

The protocol and thresholds were fixed before candidate selection. Automated evaluation was not treated as proof of fun, elegance, teachability, or originality.

## Result

Study 001 did not produce a surviving game that supports the target claim.

| Design | Disposition | Decisive evidence |
|---|---|---|
| Relay | Rejected | Equal depth-2 play produced 129 first-player wins, 12 second-player wins, and 59 unresolved 200-ply games. |
| Span v0.1 | Rejected | Exhaustive reply enumeration proved a five-ply Black connection through C2–C3–C4 or its reflection. |
| Keystone v0.1 | Rejected | Only 50.9% of 2,000 fixed-seed random games completed by 200 plies. |
| Span v0.2 | Rejected | Equal depth-3 play produced 1,000 second-participant wins, and exhaustive analysis proved every legal opening loses for the first participant. |

## Main evidence

### Protocol and process

- [`PROTOCOL.md`](PROTOCOL.md) — frozen evaluation plan and thresholds
- [`WORKLOG.md`](WORKLOG.md) — chronological research record
- [`REPORT.md`](REPORT.md) — final synthesis, evidence classification, limitations, and conclusion

### Relay

- [`../../../experiments/relay_baseline.py`](../../../experiments/relay_baseline.py) — reproducible baseline
- Genesis implementation and analysis commit: `5a59af0d88da6bfab14bc3bc8bd1913d31e4da6e`

### Span v0.1

- [`prototypes/span/RULES.md`](prototypes/span/RULES.md) — frozen rules
- [`prototypes/span/DECISION.md`](prototypes/span/DECISION.md) — disposition
- [`analysis/span_random_v0_1.md`](analysis/span_random_v0_1.md) — random pathology screen
- [`analysis/span_minimax_smoke_v0_1.md`](analysis/span_minimax_smoke_v0_1.md) — forced-line diagnosis

### Keystone v0.1

- [`prototypes/keystone/ORIGIN.md`](prototypes/keystone/ORIGIN.md) — recovered origin and ambiguity decisions
- [`prototypes/keystone/RULES.md`](prototypes/keystone/RULES.md) — frozen rules
- [`prototypes/keystone/DECISION.md`](prototypes/keystone/DECISION.md) — disposition
- [`analysis/keystone_random_v0_1.md`](analysis/keystone_random_v0_1.md) — termination diagnosis

### Span v0.2

- [`analysis/prototype_revision_selection.md`](analysis/prototype_revision_selection.md) — one-change revision selection
- [`prototypes/span/RULES_v0_2.md`](prototypes/span/RULES_v0_2.md) — frozen swap revision
- [`analysis/span_v0_2_formal.md`](analysis/span_v0_2_formal.md) — formal evaluation and forced-win diagnosis
- [`prototypes/span/DECISION_v0_2.md`](prototypes/span/DECISION_v0_2.md) — disposition
- [`../../../data/span_v0_2_formal.json`](../../../data/span_v0_2_formal.json) — machine-readable formal results
- [`../../../tests/test_span_v0_2_forced_second_participant.py`](../../../tests/test_span_v0_2_forced_second_participant.py) — exhaustive opening regression

## Methodological result

The strongest repeated lesson was that random parity was not balance evidence. Relay, Span v0.1, and Span v0.2 all appeared approximately even under random play, while stronger or constructive analysis exposed severe initiative or forced wins.

Rule freezing, participant-aware measurement, deterministic reruns, constructive counterexamples, and explicit stop conditions prevented the study from rescuing failed designs through unbounded post-result adjustment.

## Unresolved qualities

No candidate reached the stage required for responsible claims about:

- fun or elegance;
- teachability in actual human use;
- human strategic depth or replay value;
- accessibility or physical ergonomics;
- genuine originality or equivalence to existing games.

A prior-art review was not performed because no design survived basic viability evaluation.

## Closure

No Span v0.3 or additional prototype belongs inside Study 001. A possible Study 002 would require a separate question, protocol, scope, and approval cycle; it is not an automatic continuation.
