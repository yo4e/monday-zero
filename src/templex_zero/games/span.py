"""Reference implementation of the frozen Span v0.1 prototype."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Literal

BOARD_SIZE = 5
EMPTY = -1
Player = Literal[0, 1]
Move = tuple[int, int]


@dataclass(frozen=True, slots=True)
class State:
    board: tuple[int, ...]
    player: Player
    ply: int = 0


def _index(row: int, column: int) -> int:
    return row * BOARD_SIZE + column


def _rc(index: int) -> tuple[int, int]:
    return divmod(index, BOARD_SIZE)


def _orthogonal_neighbors(index: int) -> tuple[int, ...]:
    row, column = _rc(index)
    neighbors: list[int] = []
    for row_delta, column_delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row = row + row_delta
        next_column = column + column_delta
        if 0 <= next_row < BOARD_SIZE and 0 <= next_column < BOARD_SIZE:
            neighbors.append(_index(next_row, next_column))
    return tuple(neighbors)


def initial_state() -> State:
    board = [EMPTY] * (BOARD_SIZE * BOARD_SIZE)
    board[_index(0, 2)] = 0
    board[_index(4, 2)] = 0
    board[_index(2, 0)] = 1
    board[_index(2, 4)] = 1
    return State(tuple(board), 0, 0)


def _components(board: tuple[int, ...], player: Player) -> tuple[frozenset[int], ...]:
    remaining = {index for index, value in enumerate(board) if value == player}
    components: list[frozenset[int]] = []
    while remaining:
        start = remaining.pop()
        component = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbor in _orthogonal_neighbors(current):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(frozenset(component))
    return tuple(components)


def _bounding_rectangle(component: frozenset[int]) -> tuple[int, int, int, int]:
    rows, columns = zip(*(_rc(index) for index in component), strict=True)
    return min(rows), max(rows), min(columns), max(columns)


def _is_legal_placement(board: tuple[int, ...], player: Player, move: Move) -> bool:
    row, column = move
    if not (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE):
        return False
    destination = _index(row, column)
    if board[destination] != EMPTY:
        return False

    components = _components(board, player)
    component_by_stone = {
        stone: component_index
        for component_index, component in enumerate(components)
        for stone in component
    }
    adjacent_component_indexes = {
        component_by_stone[neighbor]
        for neighbor in _orthogonal_neighbors(destination)
        if board[neighbor] == player
    }

    if not adjacent_component_indexes:
        return False
    if len(adjacent_component_indexes) >= 2:
        return True

    component = components[next(iter(adjacent_component_indexes))]
    min_row, max_row, min_column, max_column = _bounding_rectangle(component)
    return row < min_row or row > max_row or column < min_column or column > max_column


@lru_cache(maxsize=None)
def _legal_moves(board: tuple[int, ...], player: Player) -> tuple[Move, ...]:
    return tuple(
        (row, column)
        for row in range(BOARD_SIZE)
        for column in range(BOARD_SIZE)
        if _is_legal_placement(board, player, (row, column))
    )


def legal_moves(state: State) -> tuple[Move, ...]:
    return _legal_moves(state.board, state.player)


def apply_move(state: State, move: Move) -> State:
    if move not in legal_moves(state):
        raise ValueError(f"Illegal Span move: {move}")
    row, column = move
    board = list(state.board)
    board[_index(row, column)] = state.player
    return State(tuple(board), 1 - state.player, state.ply + 1)  # type: ignore[arg-type]


def _has_connection(board: tuple[int, ...], player: Player) -> bool:
    for component in _components(board, player):
        positions = [_rc(index) for index in component]
        if player == 0:
            if any(row == 0 for row, _ in positions) and any(row == BOARD_SIZE - 1 for row, _ in positions):
                return True
        elif any(column == 0 for _, column in positions) and any(
            column == BOARD_SIZE - 1 for _, column in positions
        ):
            return True
    return False


def winner(state: State) -> Player | str:
    """Return 0/1 for a winner, or ``"ongoing"``."""
    for player in (0, 1):
        if _has_connection(state.board, player):
            return player
    if not legal_moves(state):
        return 1 - state.player  # type: ignore[return-value]
    return "ongoing"


def render(state: State) -> str:
    symbols = {EMPTY: ".", 0: "B", 1: "W"}
    rows = ["    A B C D E"]
    for row in range(BOARD_SIZE):
        cells = " ".join(symbols[state.board[_index(row, column)]] for column in range(BOARD_SIZE))
        rows.append(f"{row + 1:>2}  {cells}")
    return "\n".join(rows)
