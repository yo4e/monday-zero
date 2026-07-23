"""Black-box execution primitives for Study 004 testing methods.

The comparison code uses a reference model for expected behavior and interacts
with the implementation under test only through reset and step operations.
It performs no paired-state equivalence or shortest-counterexample search.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

from .schema import ACTIONS, MealyModel

Trace = tuple[str, ...]
TransitionKey = tuple[int, str]
TransitionPairKey = tuple[int, str, int, str]


@runtime_checkable
class BlackBoxSystem(Protocol):
    """Minimal interface exposed to testing methods and the reducer."""

    def reset(self) -> None:
        """Return the implementation to its reset state."""

    def step(self, action: str) -> str:
        """Apply one action and return the observable output label."""


@dataclass
class ModelBlackBox:
    """Executable adapter for a frozen Mealy model.

    Formal testing methods accept only the BlackBoxSystem protocol; this adapter
    exists so later benchmark code can execute frozen mutant models without
    exposing transition data through the method implementation itself.
    """

    model: MealyModel
    _state: int = field(init=False)

    def __post_init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._state = self.model.reset_state

    def step(self, action: str) -> str:
        try:
            action_index = ACTIONS.index(action)
        except ValueError as exc:
            raise ValueError(f"unknown action: {action}") from exc
        transition = self.model.transitions[self._state][action_index]
        self._state = transition.target
        return transition.output


@dataclass(frozen=True)
class TraceExecution:
    """Observed execution of one reset-delimited test trace."""

    requested_trace: Trace
    executed_trace: Trace
    expected_outputs: tuple[str, ...]
    observed_outputs: tuple[str, ...]
    transitions: tuple[TransitionKey, ...]
    transition_pairs: tuple[TransitionPairKey, ...]
    mismatch_index: int | None
    expected_output: str | None
    observed_output: str | None

    @property
    def detected(self) -> bool:
        return self.mismatch_index is not None

    @property
    def actions_executed(self) -> int:
        return len(self.executed_trace)

    @property
    def failing_trace(self) -> Trace | None:
        if self.mismatch_index is None:
            return None
        return self.executed_trace[: self.mismatch_index + 1]


def validate_trace(trace: Trace) -> None:
    for action in trace:
        if action not in ACTIONS:
            raise ValueError(f"unknown action in trace: {action}")


def execute_trace(
    reference: MealyModel,
    system: BlackBoxSystem,
    trace: Trace,
) -> TraceExecution:
    """Reset and compare one trace, stopping at the first output mismatch."""

    validate_trace(trace)
    system.reset()
    reference_state = reference.reset_state
    expected_outputs: list[str] = []
    observed_outputs: list[str] = []
    executed: list[str] = []
    transitions: list[TransitionKey] = []
    pairs: list[TransitionPairKey] = []
    previous: tuple[int, str, int] | None = None

    mismatch_index: int | None = None
    expected_mismatch: str | None = None
    observed_mismatch: str | None = None

    for index, action in enumerate(trace):
        action_index = ACTIONS.index(action)
        source_state = reference_state
        transition = reference.transitions[source_state][action_index]
        expected = transition.output
        observed = system.step(action)

        executed.append(action)
        expected_outputs.append(expected)
        observed_outputs.append(observed)
        transitions.append((source_state, action))
        if previous is not None:
            previous_state, previous_action, middle_state = previous
            pairs.append((previous_state, previous_action, middle_state, action))
        previous = (source_state, action, transition.target)
        reference_state = transition.target

        if observed != expected:
            mismatch_index = index
            expected_mismatch = expected
            observed_mismatch = observed
            break

    return TraceExecution(
        requested_trace=trace,
        executed_trace=tuple(executed),
        expected_outputs=tuple(expected_outputs),
        observed_outputs=tuple(observed_outputs),
        transitions=tuple(transitions),
        transition_pairs=tuple(pairs),
        mismatch_index=mismatch_index,
        expected_output=expected_mismatch,
        observed_output=observed_mismatch,
    )
