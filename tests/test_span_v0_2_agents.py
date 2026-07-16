import random

import pytest

from templex_zero import span_v0_2_agents as agents
from templex_zero import span_v0_2_match
from templex_zero.games import span, span_v0_2 as game


def make_state(
    *,
    black=(),
    white=(),
    participant=0,
    participant_colors=(0, 1),
    swap_available=False,
    ply=0,
    placements=0,
):
    board = [game.EMPTY] * (game.BOARD_SIZE**2)
    for row, column in black:
        board[span._index(row, column)] = 0
    for row, column in white:
        board[span._index(row, column)] = 1
    return game.State(
        tuple(board),
        participant,
        participant_colors,
        swap_available,
        ply,
        placements,
    )


def transpose_color_swap(state):
    board = [game.EMPTY] * len(state.board)
    for index, value in enumerate(state.board):
        row, column = span._rc(index)
        board[span._index(column, row)] = (
            game.EMPTY if value == game.EMPTY else 1 - value
        )
    colors = tuple(1 - color for color in state.participant_colors)
    return game.State(
        tuple(board),
        state.participant,
        colors,
        state.swap_available,
        state.ply,
        state.placements,
    )


def test_terminal_scoring_is_by_participant_after_swap():
    state = make_state(
        black=((0, 2), (1, 2), (2, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        participant=0,
        participant_colors=(1, 0),
        ply=9,
        placements=9,
    )
    assert agents.evaluate(state, 1) > 900_000
    assert agents.evaluate(state, 0) < -900_000


def test_evaluation_symmetric_under_transpose_color_swap():
    state = make_state(
        black=((0, 2), (1, 2), (3, 3), (4, 2)),
        white=((1, 4), (2, 0), (2, 1), (2, 4)),
        participant=0,
        participant_colors=(0, 1),
        ply=6,
        placements=6,
    )
    mirrored = transpose_color_swap(state)
    assert agents.evaluate(state, 0) == agents.evaluate(mirrored, 0)
    assert agents.evaluate(state, 1) == agents.evaluate(mirrored, 1)


def test_minimax_selects_immediate_participant_win():
    state = make_state(
        black=((0, 2), (1, 2), (3, 2), (4, 2)),
        white=((2, 0), (2, 4)),
        participant=1,
        participant_colors=(1, 0),
        ply=4,
        placements=4,
    )
    assert agents.minimax_agent(1)(state, random.Random(0)) == game.Action((2, 2))


def test_swap_window_choice_is_legal_and_seeded():
    state = game.apply_action(game.initial_state(), game.Action((1, 2)))
    agent = agents.minimax_agent(2)
    first = agent(state, random.Random(42))
    second = agent(state, random.Random(42))
    assert first == second
    assert first in game.legal_actions(state)


def test_random_agent_and_minimax_reject_terminal_state():
    terminal = make_state(
        black=((2, 2),),
        white=((1, 2), (2, 1), (2, 3), (3, 2)),
        participant=0,
        participant_colors=(0, 1),
        placements=5,
    )
    with pytest.raises(ValueError, match="terminal state"):
        agents.random_agent(terminal, random.Random(0))
    with pytest.raises(ValueError, match="terminal state"):
        agents.minimax_agent(1)(terminal, random.Random(0))


def test_invalid_depth_rejected():
    with pytest.raises(ValueError, match="depth must be at least 1"):
        agents.minimax_agent(0)


def test_match_reproducible_terminates_and_records_participants():
    agent = agents.minimax_agent(2)
    first = span_v0_2_match.play(agent, agent, 17)
    second = span_v0_2_match.play(agent, agent, 17)
    assert first == second
    assert first.winner_participant in (0, 1)
    assert first.winner_color in (0, 1)
    assert first.win_mode in ("connection", "immobilization")
    assert 1 <= first.placements <= 21
    assert first.placements <= first.plies <= first.placements + 1
    assert len(first.legal_action_counts) == first.plies
    assert first.max_legal_actions >= first.mean_legal_actions > 0
    assert first.final_participant_colors in ((0, 1), (1, 0))
