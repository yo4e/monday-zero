"""Small, inspectable baseline agents for Study 001."""

from __future__ import annotations

import random
from collections.abc import Callable

from templex_zero.games import relay

Agent = Callable[[relay.State, random.Random], relay.Move]


def random_agent(state: relay.State, rng: random.Random) -> relay.Move:
    moves = relay.legal_moves(state)
    if not moves:
        raise ValueError("Agent asked to move in a terminal state")
    return rng.choice(moves)


def _heuristic(state: relay.State, root: relay.Player) -> float:
    result = relay.winner(state)
    if result != "ongoing":
        if result is None:
            return 0.0
        return 10_000.0 if result == root else -10_000.0

    opponent = 1 - root
    root_positions = [divmod(index, relay.BOARD_SIZE) for index, value in enumerate(state.board) if value == root]
    opponent_positions = [
        divmod(index, relay.BOARD_SIZE) for index, value in enumerate(state.board) if value == opponent
    ]

    def progress(player: int, positions: list[tuple[int, int]]) -> int:
        if player == 0:
            return max(row for row, _ in positions)
        return max(relay.BOARD_SIZE - 1 - row for row, _ in positions)

    progress_difference = progress(root, root_positions) - progress(opponent, opponent_positions)
    material_difference = len(root_positions) - len(opponent_positions)
    root_mobility = len(relay._legal_moves(state.board, root))
    opponent_mobility = len(relay._legal_moves(state.board, opponent))
    mobility_difference = root_mobility - opponent_mobility
    center_difference = sum(2 - abs(column - 2) for _, column in root_positions) - sum(
        2 - abs(column - 2) for _, column in opponent_positions
    )

    return (
        30.0 * progress_difference
        + 12.0 * material_difference
        + 1.5 * mobility_difference
        + 0.5 * center_difference
    )


def _minimax(
    state: relay.State,
    depth: int,
    root: relay.Player,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
) -> float:
    result = relay.winner(state)
    if result != "ongoing" or depth == 0:
        return _heuristic(state, root)

    if state.player == root:
        value = float("-inf")
        for move in relay.legal_moves(state):
            value = max(value, _minimax(relay.apply_move(state, move), depth - 1, root, alpha, beta))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    value = float("inf")
    for move in relay.legal_moves(state):
        value = min(value, _minimax(relay.apply_move(state, move), depth - 1, root, alpha, beta))
        beta = min(beta, value)
        if beta <= alpha:
            break
    return value


def minimax_agent(depth: int) -> Agent:
    if depth < 1:
        raise ValueError("depth must be at least 1")

    def choose(state: relay.State, rng: random.Random) -> relay.Move:
        scored = [
            (_minimax(relay.apply_move(state, move), depth - 1, state.player), move)
            for move in relay.legal_moves(state)
        ]
        best = max(score for score, _ in scored)
        return rng.choice([move for score, move in scored if score == best])

    return choose
