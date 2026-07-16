"""Participant-aware deterministic baseline agents for Span v0.2."""
from __future__ import annotations

import heapq
import random
from collections.abc import Callable
from functools import lru_cache

from templex_zero.games import span, span_v0_2 as game

SpanV02Agent = Callable[[game.State, random.Random], game.Action]
WIN_SCORE = 1_000_000.0
BLOCKED_COST = game.BOARD_SIZE**2 + 1


def random_agent(state: game.State, rng: random.Random) -> game.Action:
    actions = game.legal_actions(state)
    if not actions:
        raise ValueError("Agent asked to move in a terminal state")
    return rng.choice(actions)


@lru_cache(maxsize=None)
def _connection_cost(board: tuple[int, ...], color: game.Color) -> int:
    """Minimum empty cells on an orthogonal edge-to-edge path for ``color``."""
    opponent = 1 - color
    distances = [BLOCKED_COST] * len(board)
    frontier: list[tuple[int, int]] = []
    starts = (
        (span._index(0, column) for column in range(game.BOARD_SIZE))
        if color == 0
        else (span._index(row, 0) for row in range(game.BOARD_SIZE))
    )
    for index in starts:
        if board[index] == opponent:
            continue
        cost = 0 if board[index] == color else 1
        distances[index] = cost
        heapq.heappush(frontier, (cost, index))

    while frontier:
        cost, current = heapq.heappop(frontier)
        if cost != distances[current]:
            continue
        row, column = span._rc(current)
        if (color == 0 and row == game.BOARD_SIZE - 1) or (
            color == 1 and column == game.BOARD_SIZE - 1
        ):
            return cost
        for neighbor in span._orthogonal_neighbors(current):
            if board[neighbor] == opponent:
                continue
            step = 0 if board[neighbor] == color else 1
            candidate = cost + step
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(frontier, (candidate, neighbor))
    return BLOCKED_COST


@lru_cache(maxsize=None)
def _maximum_component_span(board: tuple[int, ...], color: game.Color) -> int:
    spans: list[int] = []
    for component in span._components(board, color):
        rows, columns = zip(*(span._rc(index) for index in component), strict=True)
        spans.append(
            max(rows) - min(rows) if color == 0 else max(columns) - min(columns)
        )
    return max(spans, default=0)


def evaluate(state: game.State, root: game.Participant) -> float:
    """Evaluate a state from a participant's perspective, independent of color."""
    outcome = game.winner(state)
    if outcome != "ongoing":
        return WIN_SCORE - state.ply if outcome == root else -WIN_SCORE + state.ply

    root_color = state.participant_colors[root]
    opponent_color: game.Color = 1 - root_color  # type: ignore[assignment]
    root_cost = _connection_cost(state.board, root_color)
    opponent_cost = _connection_cost(state.board, opponent_color)
    root_span = _maximum_component_span(state.board, root_color)
    opponent_span = _maximum_component_span(state.board, opponent_color)
    root_mobility = len(span._legal_moves(state.board, root_color))
    opponent_mobility = len(span._legal_moves(state.board, opponent_color))
    root_components = len(span._components(state.board, root_color))
    opponent_components = len(span._components(state.board, opponent_color))

    return (
        100.0 * (opponent_cost - root_cost)
        + 12.0 * (root_span - opponent_span)
        + 2.0 * (root_mobility - opponent_mobility)
        + 3.0 * (opponent_components - root_components)
    )


@lru_cache(maxsize=None)
def _minimax_value(
    state: game.State, depth: int, root: game.Participant
) -> float:
    outcome = game.winner(state)
    if outcome != "ongoing" or depth == 0:
        return evaluate(state, root)
    values = tuple(
        _minimax_value(game.apply_action(state, action), depth - 1, root)
        for action in game.legal_actions(state)
    )
    return max(values) if state.participant == root else min(values)


def minimax_agent(depth: int) -> SpanV02Agent:
    if depth < 1:
        raise ValueError("depth must be at least 1")

    def choose(state: game.State, rng: random.Random) -> game.Action:
        actions = game.legal_actions(state)
        if not actions:
            raise ValueError("Agent asked to move in a terminal state")
        root = state.participant
        scored = [
            (_minimax_value(game.apply_action(state, action), depth - 1, root), action)
            for action in actions
        ]
        best = max(score for score, _ in scored)
        return rng.choice([action for score, action in scored if score == best])

    return choose
