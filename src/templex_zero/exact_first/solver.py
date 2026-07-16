"""No-reduction memoized exact solver for finite Study 002 placement games."""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from types import MappingProxyType
from typing import Literal, Mapping

from .schema import (
    Action,
    GameSpec,
    State,
    apply_action,
    initial_state,
    legal_actions,
    terminal_result,
)

Outcome = Literal["win", "draw", "loss"]
CapReason = Literal["state", "time"]


@dataclass(frozen=True, order=True)
class ExactValue:
    outcome: Outcome
    distance: int

    def __post_init__(self) -> None:
        if self.distance < 0:
            raise ValueError("distance must be non-negative")


@dataclass(frozen=True)
class ActionValue:
    action: Action
    value: ExactValue


@dataclass(frozen=True)
class ExactSolveResult:
    root: ExactValue | None
    opening_values: tuple[ActionValue, ...]
    expanded_states: int
    cap_reached: bool
    cap_reason: CapReason | None
    values: Mapping[State, ExactValue]
    action_values: Mapping[State, tuple[ActionValue, ...]]


class _CapReached(RuntimeError):
    def __init__(self, reason: CapReason) -> None:
        self.reason = reason
        super().__init__(reason)


def _terminal_value(spec: GameSpec, state: State) -> ExactValue | None:
    terminal = terminal_result(spec, state)
    if terminal == "ongoing":
        return None
    if terminal == "draw":
        return ExactValue("draw", 0)
    winner = int(terminal[-1])
    return ExactValue("win" if winner == state.player else "loss", 0)


def _invert(value: ExactValue) -> ExactValue:
    outcome: Outcome = {
        "win": "loss",
        "loss": "win",
        "draw": "draw",
    }[value.outcome]  # type: ignore[assignment]
    return ExactValue(outcome, value.distance + 1)


def _choose(values: tuple[ActionValue, ...]) -> ExactValue:
    if not values:
        raise ValueError("cannot choose from no action values")
    priority = {"loss": 0, "draw": 1, "win": 2}
    best_outcome = max(
        (item.value.outcome for item in values),
        key=priority.__getitem__,
    )
    distances = [
        item.value.distance
        for item in values
        if item.value.outcome == best_outcome
    ]
    distance = max(distances) if best_outcome == "loss" else min(distances)
    return ExactValue(best_outcome, distance)  # type: ignore[arg-type]


def solve_exact(
    spec: GameSpec,
    root: State | None = None,
    *,
    state_cap: int | None = None,
    time_limit_seconds: float | None = None,
) -> ExactSolveResult:
    """Solve all reachable actions with memoization and no symmetry reduction.

    Ties preserve the game-theoretic outcome. Wins use shortest distance, losses
    use longest distance, and draws use shortest distance as a deterministic
    convention.
    """

    if state_cap is not None and state_cap < 1:
        raise ValueError("state_cap must be positive")
    if time_limit_seconds is not None and time_limit_seconds <= 0:
        raise ValueError("time_limit_seconds must be positive")

    start = perf_counter()
    cache: dict[State, ExactValue] = {}
    action_cache: dict[State, tuple[ActionValue, ...]] = {}
    expanded = 0

    def check_and_count() -> None:
        nonlocal expanded
        if (
            time_limit_seconds is not None
            and perf_counter() - start >= time_limit_seconds
        ):
            raise _CapReached("time")
        if state_cap is not None and expanded >= state_cap:
            raise _CapReached("state")
        expanded += 1

    def visit(state: State) -> ExactValue:
        if state in cache:
            return cache[state]

        check_and_count()
        terminal = _terminal_value(spec, state)
        if terminal is not None:
            cache[state] = terminal
            action_cache[state] = ()
            return terminal

        actions = tuple(
            ActionValue(
                action,
                _invert(visit(apply_action(spec, state, action))),
            )
            for action in legal_actions(spec, state)
        )
        value = _choose(actions)
        cache[state] = value
        action_cache[state] = actions
        return value

    root_state = root if root is not None else initial_state(spec)
    try:
        root_value = visit(root_state)
    except _CapReached as exc:
        return ExactSolveResult(
            root=None,
            opening_values=(),
            expanded_states=expanded,
            cap_reached=True,
            cap_reason=exc.reason,
            values=MappingProxyType(dict(cache)),
            action_values=MappingProxyType(dict(action_cache)),
        )

    return ExactSolveResult(
        root=root_value,
        opening_values=action_cache[root_state],
        expanded_states=expanded,
        cap_reached=False,
        cap_reason=None,
        values=MappingProxyType(dict(cache)),
        action_values=MappingProxyType(dict(action_cache)),
    )
