from collections import deque

import pytest

from templex_zero.exact_first.bruteforce import solve_bruteforce
from templex_zero.exact_first.fixtures import (
    ADJACENCY_CHAIN,
    AUDITED_FIXTURES,
    BRANCHING_PATTERN,
    IMMEDIATE_COMPONENT_WIN,
    SINGLE_CELL_DRAW,
)
from templex_zero.exact_first.schema import (
    State,
    apply_action,
    initial_state,
    legal_actions,
)
from templex_zero.exact_first.solver import (
    ActionValue,
    ExactValue,
    _choose,
    solve_exact,
)


def reachable_states(spec):
    root = initial_state(spec)
    queue = deque([root])
    seen = {root}
    while queue:
        state = queue.popleft()
        for action in legal_actions(spec, state):
            child = apply_action(spec, state, action)
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return seen


def simple(value):
    return value.outcome, value.distance


def actions(values):
    return {item.action: simple(item.value) for item in values}


def test_memoized_and_bruteforce_agree_on_every_reachable_fixture_state():
    for fixture in AUDITED_FIXTURES:
        exact = solve_exact(fixture.spec)
        brute = solve_bruteforce(fixture.spec)
        states = reachable_states(fixture.spec)

        assert exact.cap_reached is False
        assert exact.expanded_states == brute.reachable_states == len(states)
        assert set(exact.values) == set(brute.values) == states
        for state in states:
            assert simple(exact.values[state]) == simple(brute.values[state])
            assert actions(exact.action_values[state]) == actions(
                brute.action_values[state]
            )


def test_hand_audited_root_values_and_openings():
    expected = {
        IMMEDIATE_COMPONENT_WIN.name: (("win", 1), {0: ("win", 1)}),
        SINGLE_CELL_DRAW.name: (("draw", 1), {0: ("draw", 1)}),
        BRANCHING_PATTERN.name: (
            ("win", 1),
            {0: ("win", 1), 1: ("loss", 2)},
        ),
        ADJACENCY_CHAIN.name: (("win", 3), {0: ("win", 3)}),
    }

    for fixture in AUDITED_FIXTURES:
        result = solve_exact(fixture.spec)
        root, opening = expected[fixture.name]
        assert simple(result.root) == root
        assert actions(result.opening_values) == opening


def swap_roles(state: State) -> State:
    board = tuple(1 - value if value in (0, 1) else value for value in state.board)
    return State(board, 1 - state.player, state.ply)


def test_claimed_fixture_symmetry_preserves_values_and_actions():
    claimed = [fixture for fixture in AUDITED_FIXTURES if fixture.symmetry_claim]
    assert [fixture.name for fixture in claimed] == [
        IMMEDIATE_COMPONENT_WIN.name,
        SINGLE_CELL_DRAW.name,
    ]

    for fixture in claimed:
        result = solve_exact(fixture.spec)
        for state in reachable_states(fixture.spec):
            mirrored = solve_exact(fixture.spec, swap_roles(state))
            assert simple(mirrored.root) == simple(result.values[state])
            assert actions(mirrored.opening_values) == actions(
                result.action_values[state]
            )


def test_state_cap_is_deterministic_and_does_not_publish_partial_root():
    spec = IMMEDIATE_COMPONENT_WIN.spec
    capped = solve_exact(spec, state_cap=1)
    assert capped.root is None
    assert capped.opening_values == ()
    assert capped.expanded_states == 1
    assert capped.cap_reached is True
    assert capped.cap_reason == "state"

    complete = solve_exact(spec, state_cap=2)
    assert complete.root == ExactValue("win", 1)
    assert complete.expanded_states == 2
    assert complete.cap_reached is False


def test_invalid_caps_are_rejected():
    with pytest.raises(ValueError, match="state_cap"):
        solve_exact(IMMEDIATE_COMPONENT_WIN.spec, state_cap=0)
    with pytest.raises(ValueError, match="time_limit"):
        solve_exact(IMMEDIATE_COMPONENT_WIN.spec, time_limit_seconds=0)


def test_terminal_state_solves_without_actions():
    spec = IMMEDIATE_COMPONENT_WIN.spec
    terminal = apply_action(spec, initial_state(spec), 0)
    exact = solve_exact(spec, terminal)
    brute = solve_bruteforce(spec, terminal)

    assert simple(exact.root) == simple(brute.root) == ("loss", 0)
    assert exact.opening_values == brute.opening_values == ()


def test_outcome_preserving_distance_policy_is_explicit():
    assert _choose(
        (
            ActionValue(0, ExactValue("win", 3)),
            ActionValue(1, ExactValue("win", 1)),
        )
    ) == ExactValue("win", 1)
    assert _choose(
        (
            ActionValue(0, ExactValue("draw", 4)),
            ActionValue(1, ExactValue("draw", 2)),
        )
    ) == ExactValue("draw", 2)
    assert _choose(
        (
            ActionValue(0, ExactValue("loss", 1)),
            ActionValue(1, ExactValue("loss", 5)),
        )
    ) == ExactValue("loss", 5)
