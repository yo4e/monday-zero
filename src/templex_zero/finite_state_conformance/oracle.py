"""Independent exact paired-state oracle for Study 004.

This module uses only the frozen Mealy schema. It does not import or call the
black-box testing methods, coverage planners, execution helper, reducer, or
corpus generator.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any

from .schema import ACTIONS, MealyModel, Transition

Trace = tuple[str, ...]
StatePair = tuple[int, int]


@dataclass(frozen=True)
class OracleResult:
    equivalent: bool
    shortest_trace: Trace | None
    visited_pairs: int

    def __post_init__(self) -> None:
        if self.equivalent != (self.shortest_trace is None):
            raise ValueError("equivalent and shortest_trace disagree")
        if self.visited_pairs <= 0:
            raise ValueError("visited_pairs must be positive")


def model_from_dict(data: dict[str, Any]) -> MealyModel:
    transitions = tuple(
        tuple(Transition(int(target), str(output)) for target, output in row)
        for row in data["transitions"]
    )
    return MealyModel(
        model_id=str(data["model_id"]),
        family=str(data["family"]),
        state_count=int(data["state_count"]),
        variant=int(data["variant"]),
        transitions=transitions,
        reset_state=int(data.get("reset_state", 0)),
    )


def exact_shortest_counterexample(
    reference: MealyModel,
    implementation: MealyModel,
) -> OracleResult:
    """Return the lexicographically first shortest output-distinguishing trace.

    Breadth-first search explores reachable pairs of hidden states. Action order
    is the frozen ACTIONS tuple, so the first found mismatch is shortest and is
    lexicographically first among traces of that length.
    """

    start: StatePair = (reference.reset_state, implementation.reset_state)
    queue: deque[tuple[StatePair, Trace]] = deque([(start, ())])
    visited: set[StatePair] = {start}

    while queue:
        (reference_state, implementation_state), prefix = queue.popleft()
        for action_index, action in enumerate(ACTIONS):
            reference_transition = reference.transitions[reference_state][action_index]
            implementation_transition = implementation.transitions[implementation_state][action_index]
            candidate = prefix + (action,)

            if reference_transition.output != implementation_transition.output:
                return OracleResult(
                    equivalent=False,
                    shortest_trace=candidate,
                    visited_pairs=len(visited),
                )

            target_pair = (
                reference_transition.target,
                implementation_transition.target,
            )
            if target_pair not in visited:
                visited.add(target_pair)
                queue.append((target_pair, candidate))

    return OracleResult(
        equivalent=True,
        shortest_trace=None,
        visited_pairs=len(visited),
    )
