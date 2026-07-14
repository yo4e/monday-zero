"""Reference implementation of the Relay prototype.

Relay is deliberately implemented before it is endorsed. The purpose of this
module is to make the candidate falsifiable.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable, Literal

BOARD_SIZE = 5
EMPTY = -1
Player = Literal[0, 1]
Move = tuple[int, int, bool]  # source, destination, is_capture


@dataclass(frozen=True, slots=True)
class State:
    board: tuple[int, ...]
    player: Player
    ply: int = 0


def initial_state() -> State:
    board = [EMPTY] * (BOARD_SIZE * BOARD_SIZE)
    for column in range(BOARD_SIZE):
        board[column] = 0
        board[(BOARD_SIZE - 1) * BOARD_SIZE + column] = 1
    return State(tuple(board), 0, 0)


def _rc(index: int) -> tuple[int, int]:
    return divmod(index, BOARD_SIZE)


def _index(row: int, column: int) -> int:
    return row * BOARD_SIZE + column


def _connected_by_king_steps(board: tuple[int, ...], player: Player) -> bool:
    stones = [index for index, value in enumerate(board) if value == player]
    if not stones:
        return False

    seen = {stones[0]}
    stack = [stones[0]]
    while stack:
        current = stack.pop()
        row, column = _rc(current)
        for row_delta in (-1, 0, 1):
            for column_delta in (-1, 0, 1):
                if row_delta == 0 and column_delta == 0:
                    continue
                next_row = row + row_delta
                next_column = column + column_delta
                if not (0 <= next_row < BOARD_SIZE and 0 <= next_column < BOARD_SIZE):
                    continue
                candidate = _index(next_row, next_column)
                if board[candidate] == player and candidate not in seen:
                    seen.add(candidate)
                    stack.append(candidate)
    return len(seen) == len(stones)


@lru_cache(maxsize=None)
def _legal_moves(board: tuple[int, ...], player: Player) -> tuple[Move, ...]:
    moves: list[Move] = []
    forward = 1 if player == 0 else -1

    for source, value in enumerate(board):
        if value != player:
            continue
        row, column = _rc(source)

        # Noncapturing steps: forward or sideways, never backward.
        for row_delta, column_delta in ((forward, 0), (0, -1), (0, 1)):
            next_row = row + row_delta
            next_column = column + column_delta
            if not (0 <= next_row < BOARD_SIZE and 0 <= next_column < BOARD_SIZE):
                continue
            destination = _index(next_row, next_column)
            if board[destination] != EMPTY:
                continue
            candidate = list(board)
            candidate[source] = EMPTY
            candidate[destination] = player
            if _connected_by_king_steps(tuple(candidate), player):
                moves.append((source, destination, False))

        # Captures: one diagonal step forward into an opponent stone.
        for column_delta in (-1, 1):
            next_row = row + forward
            next_column = column + column_delta
            if not (0 <= next_row < BOARD_SIZE and 0 <= next_column < BOARD_SIZE):
                continue
            destination = _index(next_row, next_column)
            if board[destination] != 1 - player:
                continue
            candidate = list(board)
            candidate[source] = EMPTY
            candidate[destination] = player
            if _connected_by_king_steps(tuple(candidate), player):
                moves.append((source, destination, True))

    return tuple(moves)


def legal_moves(state: State) -> tuple[Move, ...]:
    return _legal_moves(state.board, state.player)


def apply_move(state: State, move: Move) -> State:
    if move not in legal_moves(state):
        raise ValueError(f"Illegal Relay move: {move}")
    source, destination, _ = move
    board = list(state.board)
    board[source] = EMPTY
    board[destination] = state.player
    return State(tuple(board), 1 - state.player, state.ply + 1)  # type: ignore[arg-type]


def winner(state: State, ply_limit: int = 200) -> Player | None | str:
    """Return 0/1 for a winner, None for a draw, or 'ongoing'."""

    for column in range(BOARD_SIZE):
        if state.board[_index(BOARD_SIZE - 1, column)] == 0:
            return 0
        if state.board[_index(0, column)] == 1:
            return 1

    if 0 not in state.board:
        return 1
    if 1 not in state.board:
        return 0
    if state.ply >= ply_limit:
        return None
    if not legal_moves(state):
        return 1 - state.player  # type: ignore[return-value]
    return "ongoing"


def render(state: State) -> str:
    symbols = {EMPTY: ".", 0: "A", 1: "B"}
    rows = []
    for row in range(BOARD_SIZE):
        rows.append(" ".join(symbols[state.board[_index(row, column)]] for column in range(BOARD_SIZE)))
    return "\n".join(rows)
