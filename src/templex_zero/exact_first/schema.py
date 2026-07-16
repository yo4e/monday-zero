"""Declarative, finite, placement-only game schema for Study 002.

The module intentionally contains no candidate generator and no exact solver.
It defines only validated rule data, deterministic state transitions, terminal
resolution, and a small graph enumerator used to audit fixtures before candidate
outcomes exist.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Literal

BLOCKED = -2
EMPTY = -1
Player = Literal[0, 1]
Action = int
Terminal = Literal["ongoing", "draw", "win:0", "win:1"]


class MechanismFamily(str, Enum):
    ADJACENCY_GROWTH = "adjacency_growth"
    COMPONENT_EXPANSION = "component_expansion"
    LOCAL_BLOCK_PATTERN = "local_block_pattern"
    FIXTURE = "fixture"


class Neighborhood(str, Enum):
    ORTHOGONAL = "orthogonal"
    KING = "king"


class FirstMoveScope(str, Enum):
    ANY = "any"
    HOME_EDGE = "home_edge"
    EXPLICIT = "explicit"


class PlacementKind(str, Enum):
    ANY = "any"
    FRIENDLY_ADJACENCY = "friendly_adjacency"
    EXPAND_OR_MERGE = "expand_or_merge"
    ENEMY_LIMIT = "enemy_limit"


class GoalKind(str, Enum):
    CONNECT_EDGES = "connect_edges"
    COMPONENT_SIZE = "component_size"
    LINE = "line"
    EXPLICIT_PATTERNS = "explicit_patterns"


class LineDirections(str, Enum):
    ORTHOGONAL = "orthogonal"
    ALL = "all"


class NoMoveOutcome(str, Enum):
    PREVIOUS_PLAYER_WINS = "previous_player_wins"
    DRAW = "draw"


@dataclass(frozen=True)
class PlacementRule:
    kind: PlacementKind
    neighborhood: Neighborhood = Neighborhood.ORTHOGONAL
    first_move_scope: FirstMoveScope = FirstMoveScope.ANY
    explicit_first_cells: tuple[tuple[int, ...], tuple[int, ...]] = ((), ())
    friendly_min: int = 0
    friendly_max: int | None = None
    enemy_max: int | None = None
    allow_expand: bool = False
    allow_merge: bool = False

    def __post_init__(self) -> None:
        if self.friendly_min < 0:
            raise ValueError("friendly_min must be non-negative")
        if self.friendly_max is not None and self.friendly_max < self.friendly_min:
            raise ValueError("friendly_max must be at least friendly_min")
        if self.enemy_max is not None and self.enemy_max < 0:
            raise ValueError("enemy_max must be non-negative")
        if self.first_move_scope is FirstMoveScope.EXPLICIT:
            if len(self.explicit_first_cells) != 2 or any(
                not cells for cells in self.explicit_first_cells
            ):
                raise ValueError("explicit first-move scope requires cells for both players")
        elif self.explicit_first_cells != ((), ()):
            raise ValueError("explicit_first_cells require EXPLICIT first-move scope")
        if self.kind is PlacementKind.EXPAND_OR_MERGE and not (
            self.allow_expand or self.allow_merge
        ):
            raise ValueError("expand-or-merge rule must allow expansion or merger")


@dataclass(frozen=True)
class GoalRule:
    kind: GoalKind
    neighborhood: Neighborhood = Neighborhood.ORTHOGONAL
    threshold: int = 1
    line_directions: LineDirections = LineDirections.ORTHOGONAL
    explicit_patterns: tuple[
        tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]
    ] = ((), ())

    def __post_init__(self) -> None:
        if self.threshold < 1:
            raise ValueError("goal threshold must be positive")
        if self.kind is GoalKind.EXPLICIT_PATTERNS:
            if len(self.explicit_patterns) != 2 or any(
                not patterns for patterns in self.explicit_patterns
            ):
                raise ValueError("explicit pattern goal requires patterns for both players")
        elif self.explicit_patterns != ((), ()):
            raise ValueError("explicit_patterns require EXPLICIT_PATTERNS goal")


@dataclass(frozen=True)
class GameSpec:
    name: str
    board_size: int
    family: MechanismFamily
    placement: PlacementRule
    goal: GoalRule
    playable_cells: tuple[int, ...] = ()
    no_move_outcome: NoMoveOutcome = NoMoveOutcome.PREVIOUS_PLAYER_WINS
    intended_symmetric: bool = True
    core_rule_words: int = 0

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("name must be non-empty")
        if not 1 <= self.board_size <= 4:
            raise ValueError("board_size must be between 1 and 4")
        cell_count = self.board_size**2
        cells = self.playable_cells or tuple(range(cell_count))
        if len(set(cells)) != len(cells):
            raise ValueError("playable_cells must be unique")
        if not cells or any(cell < 0 or cell >= cell_count for cell in cells):
            raise ValueError("playable_cells must be non-empty and in bounds")
        object.__setattr__(self, "playable_cells", tuple(sorted(cells)))
        if self.core_rule_words < 0 or self.core_rule_words > 250:
            raise ValueError("core_rule_words must be between 0 and 250")
        if self.family is not MechanismFamily.FIXTURE:
            if self.board_size not in (3, 4):
                raise ValueError("candidate games must use a 3x3 or 4x4 board")
            if self.playable_cells != tuple(range(cell_count)):
                raise ValueError("candidate games must use every board cell")
            if not self.intended_symmetric:
                raise ValueError("candidate games must state intended symmetry")
            if self.placement.first_move_scope is FirstMoveScope.EXPLICIT:
                raise ValueError("explicit openings are fixture-only")
            if self.goal.kind is GoalKind.EXPLICIT_PATTERNS:
                raise ValueError("explicit goal patterns are fixture-only")
        for cells_for_player in self.placement.explicit_first_cells:
            if any(cell not in self.playable_cells for cell in cells_for_player):
                raise ValueError("explicit first-move cells must be playable")
        for patterns in self.goal.explicit_patterns:
            for pattern in patterns:
                if not pattern or any(cell not in self.playable_cells for cell in pattern):
                    raise ValueError("explicit goal patterns must be non-empty and playable")


@dataclass(frozen=True)
class State:
    board: tuple[int, ...]
    player: Player
    ply: int = 0

    def __post_init__(self) -> None:
        if self.player not in (0, 1):
            raise ValueError("player must be 0 or 1")
        if self.ply < 0:
            raise ValueError("ply must be non-negative")
        if any(value not in (BLOCKED, EMPTY, 0, 1) for value in self.board):
            raise ValueError("board contains an invalid cell value")


def initial_state(spec: GameSpec) -> State:
    playable = set(spec.playable_cells)
    board = tuple(
        EMPTY if index in playable else BLOCKED
        for index in range(spec.board_size**2)
    )
    return State(board, 0, 0)


def _rc(spec: GameSpec, index: int) -> tuple[int, int]:
    return divmod(index, spec.board_size)


def _index(spec: GameSpec, row: int, column: int) -> int:
    return row * spec.board_size + column


def _neighbors(spec: GameSpec, index: int, mode: Neighborhood) -> tuple[int, ...]:
    row, column = _rc(spec, index)
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if mode is Neighborhood.KING:
        deltas += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    result = []
    playable = set(spec.playable_cells)
    for dr, dc in deltas:
        nr, nc = row + dr, column + dc
        if 0 <= nr < spec.board_size and 0 <= nc < spec.board_size:
            neighbor = _index(spec, nr, nc)
            if neighbor in playable:
                result.append(neighbor)
    return tuple(sorted(result))


def _player_cells(state: State, player: Player) -> tuple[int, ...]:
    return tuple(index for index, value in enumerate(state.board) if value == player)


def _first_move_allowed(spec: GameSpec, player: Player, cell: int) -> bool:
    scope = spec.placement.first_move_scope
    if scope is FirstMoveScope.ANY:
        return True
    if scope is FirstMoveScope.EXPLICIT:
        return cell in spec.placement.explicit_first_cells[player]
    row, column = _rc(spec, cell)
    return row == 0 if player == 0 else column == 0


def _components(
    spec: GameSpec, board: tuple[int, ...], player: Player, mode: Neighborhood
) -> list[set[int]]:
    remaining = {index for index, value in enumerate(board) if value == player}
    components: list[set[int]] = []
    while remaining:
        start = min(remaining)
        component = {start}
        stack = [start]
        remaining.remove(start)
        while stack:
            current = stack.pop()
            for neighbor in _neighbors(spec, current, mode):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    component.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    return components


def _adjacent_components(
    spec: GameSpec, state: State, cell: int, mode: Neighborhood
) -> list[set[int]]:
    adjacent = set(_neighbors(spec, cell, mode))
    return [
        component
        for component in _components(spec, state.board, state.player, mode)
        if component & adjacent
    ]


def _expands_component(spec: GameSpec, cell: int, component: set[int]) -> bool:
    rows = [_rc(spec, index)[0] for index in component]
    columns = [_rc(spec, index)[1] for index in component]
    row, column = _rc(spec, cell)
    return row < min(rows) or row > max(rows) or column < min(columns) or column > max(columns)


def _placement_allowed(spec: GameSpec, state: State, cell: int) -> bool:
    rule = spec.placement
    own_cells = _player_cells(state, state.player)
    if not own_cells and not _first_move_allowed(spec, state.player, cell):
        return False
    neighbors = _neighbors(spec, cell, rule.neighborhood)
    friendly = sum(state.board[index] == state.player for index in neighbors)
    enemy = sum(state.board[index] == 1 - state.player for index in neighbors)

    if rule.kind is PlacementKind.ANY:
        return True
    if rule.kind is PlacementKind.FRIENDLY_ADJACENCY:
        if not own_cells:
            return True
        if friendly < rule.friendly_min:
            return False
        return rule.friendly_max is None or friendly <= rule.friendly_max
    if rule.kind is PlacementKind.ENEMY_LIMIT:
        if friendly < rule.friendly_min:
            return False
        return rule.enemy_max is None or enemy <= rule.enemy_max
    if rule.kind is PlacementKind.EXPAND_OR_MERGE:
        if not own_cells:
            return True
        joined = _adjacent_components(spec, state, cell, rule.neighborhood)
        merge = rule.allow_merge and len(joined) >= 2
        expand = rule.allow_expand and any(
            _expands_component(spec, cell, component) for component in joined
        )
        return merge or expand
    raise AssertionError(f"unhandled placement kind: {rule.kind}")


def _raw_legal_actions(spec: GameSpec, state: State) -> tuple[Action, ...]:
    if len(state.board) != spec.board_size**2:
        raise ValueError("state board length does not match spec")
    return tuple(
        cell
        for cell in spec.playable_cells
        if state.board[cell] == EMPTY and _placement_allowed(spec, state, cell)
    )


def _has_connection(spec: GameSpec, state: State, player: Player) -> bool:
    for component in _components(spec, state.board, player, spec.goal.neighborhood):
        coordinates = {_rc(spec, index) for index in component}
        if player == 0:
            if any(row == 0 for row, _ in coordinates) and any(
                row == spec.board_size - 1 for row, _ in coordinates
            ):
                return True
        elif any(column == 0 for _, column in coordinates) and any(
            column == spec.board_size - 1 for _, column in coordinates
        ):
            return True
    return False


def _has_line(spec: GameSpec, state: State, player: Player) -> bool:
    target = spec.goal.threshold
    directions = [(0, 1), (1, 0)]
    if spec.goal.line_directions is LineDirections.ALL:
        directions += [(1, 1), (1, -1)]
    own = set(_player_cells(state, player))
    for start in own:
        row, column = _rc(spec, start)
        for dr, dc in directions:
            cells = []
            for offset in range(target):
                nr, nc = row + dr * offset, column + dc * offset
                if not (0 <= nr < spec.board_size and 0 <= nc < spec.board_size):
                    break
                cells.append(_index(spec, nr, nc))
            if len(cells) == target and all(cell in own for cell in cells):
                return True
    return False


def goal_satisfied(spec: GameSpec, state: State, player: Player) -> bool:
    goal = spec.goal
    if goal.kind is GoalKind.CONNECT_EDGES:
        return _has_connection(spec, state, player)
    if goal.kind is GoalKind.COMPONENT_SIZE:
        return any(
            len(component) >= goal.threshold
            for component in _components(spec, state.board, player, goal.neighborhood)
        )
    if goal.kind is GoalKind.LINE:
        return _has_line(spec, state, player)
    if goal.kind is GoalKind.EXPLICIT_PATTERNS:
        own = set(_player_cells(state, player))
        return any(set(pattern) <= own for pattern in goal.explicit_patterns[player])
    raise AssertionError(f"unhandled goal kind: {goal.kind}")


def terminal_result(spec: GameSpec, state: State) -> Terminal:
    if state.ply > 0:
        previous: Player = 1 - state.player  # type: ignore[assignment]
        if goal_satisfied(spec, state, previous):
            return f"win:{previous}"  # type: ignore[return-value]
    if not _raw_legal_actions(spec, state):
        if spec.no_move_outcome is NoMoveOutcome.DRAW or state.ply == 0:
            return "draw"
        previous = 1 - state.player
        return f"win:{previous}"  # type: ignore[return-value]
    return "ongoing"


def legal_actions(spec: GameSpec, state: State) -> tuple[Action, ...]:
    if terminal_result(spec, state) != "ongoing":
        return ()
    return _raw_legal_actions(spec, state)


def apply_action(spec: GameSpec, state: State, action: Action) -> State:
    if action not in legal_actions(spec, state):
        raise ValueError("illegal action")
    board = list(state.board)
    board[action] = state.player
    next_player: Player = 1 - state.player  # type: ignore[assignment]
    return State(tuple(board), next_player, state.ply + 1)


def coordinate(spec: GameSpec, action: Action) -> str:
    row, column = _rc(spec, action)
    return f"{chr(ord('A') + column)}{row + 1}"


def state_key(spec: GameSpec, state: State) -> str:
    symbols = {BLOCKED: "#", EMPTY: ".", 0: "X", 1: "O"}
    board = "".join(symbols[value] for value in state.board)
    return f"p{state.player}:{state.ply}:{board}"


def enumerate_state_graph(spec: GameSpec) -> dict[str, dict[str, object]]:
    """Enumerate a fixture's complete reachable graph in deterministic order."""

    root = initial_state(spec)
    queue = deque([root])
    seen: dict[str, State] = {state_key(spec, root): root}
    graph: dict[str, dict[str, object]] = {}
    while queue:
        state = queue.popleft()
        key = state_key(spec, state)
        actions: dict[str, str] = {}
        for action in legal_actions(spec, state):
            child = apply_action(spec, state, action)
            child_key = state_key(spec, child)
            actions[coordinate(spec, action)] = child_key
            if child_key not in seen:
                seen[child_key] = child
                queue.append(child)
        graph[key] = {
            "terminal": terminal_result(spec, state),
            "actions": actions,
        }
    return graph
