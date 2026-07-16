# Study 002 Exact-Instrument Correctness Audit

_Date: 2026-07-17 (Asia/Tokyo)_  
_Status: **Correctness gate passed before candidate solving**_

## Scope

This audit covers only the generic exact-analysis instrument and the four frozen pre-candidate fixtures. None of the eighteen frozen candidates was solved, enumerated, played, or assigned an outcome in this cycle.

## Instruments

### Memoized reference solver

`src/templex_zero/exact_first/solver.py` implements a standard-library-only, full-width, no-symmetry-reduction depth-first solver.

For every expanded state it records:

- outcome from the participant-to-move perspective: `win`, `draw`, or `loss`;
- terminal distance;
- every legal action's value from the acting participant's perspective;
- expanded-state count;
- state-cap or time-cap termination.

A capped solve does not publish a partial root value.

### Independent fixture oracle

`src/templex_zero/exact_first/bruteforce.py` does not call the memoized recursion. It:

1. constructs the complete reachable graph with a queue;
2. stores every edge explicitly;
3. processes states in descending ply order;
4. computes values retrogradely.

The two instruments share the frozen declarative game engine for legality and terminal resolution, but they do not share traversal, memoization, retrograde evaluation, or outcome-selection code.

## Frozen value convention

Values are from the participant-to-move perspective. An action value reverses the child participant's result and adds one ply.

Outcome order is:

`win > draw > loss`

Among actions preserving the best outcome:

- a win uses the shortest terminal distance;
- a loss uses the longest terminal distance;
- a draw uses the shortest terminal distance as a deterministic convention.

The draw distance convention is not a claim about player preference. It gives one reproducible distance where the game-theoretic outcome alone does not order draw lengths.

## Fixture results

| Fixture | Reachable states | Root value | Opening values |
|---|---:|---|---|
| immediate component win | 2 | win in 1 | A1: win in 1 |
| single-cell draw | 2 | draw in 1 | A1: draw in 1 |
| branching pattern | 4 | win in 1 | A1: win in 1; B1: loss in 2 |
| adjacency chain | 4 | win in 3 | A1: win in 3 |

The two implementations agreed on all twelve reachable states, including:

- state outcome;
- state distance;
- the value and distance of every legal action;
- reachable or expanded-state count.

The explicit hand-audited root and opening values also matched.

## Symmetry check

Only Fixtures 1 and 2 retain a frozen symmetry claim. For every reachable state in those fixtures, swapping participant-to-move and exchanging stone colors preserved:

- outcome;
- distance;
- legal action values.

Fixtures 3 and 4 were not subjected to a symmetry requirement because no such claim remains frozen for them.

## Cap behavior

Deterministic tests verified:

- a one-state cap interrupts the two-state immediate-win fixture after exactly one expansion;
- the capped result has no root or opening value;
- a two-state cap completes the same fixture;
- invalid non-positive caps are rejected;
- a controlled monotonic clock triggers the time-cap path after one expansion.

Candidate caps remain unchanged: 2,000,000 expanded states and 30 measured seconds per candidate, with 25,000,000 expanded states across the study in frozen manifest order.

## Verification

Using the final GitHub-stored solver, oracle, package export, and test contents in a local reconstruction:

- `tests/test_exact_first_solver.py`: **8 passed**;
- setup, fixture, and solver tests together: **18 passed**;
- `python -m compileall -q src tests`: completed without error;
- Git blob SHAs of the solver, oracle, package export, and final solver test matched the locally executed files exactly.

The earlier seven manifest tests were not rerun because the local reconstruction did not include the twenty-one committed manifest files. Their previous result remains a separate cycle record.

A fresh clone remained unavailable because the execution environment could not resolve `github.com`. The repository has no recorded GitHub Actions workflow.

## Decision

The precommitted exact-instrument correctness gate passed. The disagreement failure condition did not trigger, and the instrument may advance to frozen candidate solving.

This result establishes consistency on tiny audited fixtures. It does not prove that the solver is free of all defects on larger games, that any candidate will solve within caps, or that any candidate is balanced, deep, interesting, or original.

## Next gate

Solve the eighteen frozen candidates strictly in manifest order with the no-reduction memoized solver and the frozen per-candidate and total caps. Record capped entries as unsolved. Do not change the manifest, grammar, value convention, or caps, and do not run random or shallow screens in that same cycle.
