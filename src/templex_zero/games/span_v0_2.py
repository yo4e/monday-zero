"""Reference implementation of the frozen Span v0.2 swap revision."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from templex_zero.games import span

BOARD_SIZE = span.BOARD_SIZE
EMPTY = span.EMPTY
Color = span.Player
Participant = Literal[0, 1]
Move = span.Move


@dataclass(frozen=True, slots=True)
class Action:
    """A normal placement, or the one-time opening swap when destination is None."""

    destination: Move | None

    @property
    def is_swap(self) -> bool:
        return self.destination is None


SWAP = Action(None)


@dataclass(frozen=True, slots=True)
class State:
    board: tuple[int, ...]
    participant: Participant
    participant_colors: tuple[Color, Color]
    swap_available: bool = False
    ply: int = 0
    placements: int = 0


def initial_state() -> State:
    baseline = span.initial_state()
    return State(
        board=baseline.board,
        participant=0,
        participant_colors=(0, 1),
        swap_available=False,
        ply=0,
        placements=0,
    )


def current_color(state: State) -> Color:
    return state.participant_colors[state.participant]


def participant_for_color(state: State, color: Color) -> Participant:
    return state.participant_colors.index(color)  # type: ignore[return-value]


def legal_placement_moves(state: State) -> tuple[Move, ...]:
    return span._legal_moves(state.board, current_color(state))


def legal_actions(state: State) -> tuple[Action, ...]:
    placements = tuple(Action(move) for move in legal_placement_moves(state))
    return placements + ((SWAP,) if state.swap_available else ())


def apply_action(state: State, action: Action) -> State:
    if action not in legal_actions(state):
        raise ValueError(f"Illegal Span v0.2 action: {action}")

    if action.is_swap:
        return State(
            board=state.board,
            participant=1 - state.participant,  # type: ignore[arg-type]
            participant_colors=(
                state.participant_colors[1],
                state.participant_colors[0],
            ),
            swap_available=False,
            ply=state.ply + 1,
            placements=state.placements,
        )

    if action.destination is None:
        raise AssertionError("Non-swap action requires a destination")

    color = current_color(state)
    row, column = action.destination
    board = list(state.board)
    board[span._index(row, column)] = color

    first_placement = state.placements == 0
    return State(
        board=tuple(board),
        participant=1 - state.participant,  # type: ignore[arg-type]
        participant_colors=state.participant_colors,
        swap_available=first_placement,
        ply=state.ply + 1,
        placements=state.placements + 1,
    )


def winning_color(state: State) -> Color | str:
    """Return the winning color, or ``"ongoing"``."""

    for color in (0, 1):
        if span._has_connection(state.board, color):
            return color
    if not legal_actions(state):
        return 1 - current_color(state)  # type: ignore[return-value]
    return "ongoing"


def winner(state: State) -> Participant | str:
    """Return the winning participant, or ``"ongoing"``."""

    color = winning_color(state)
    if color == "ongoing":
        return "ongoing"
    return participant_for_color(state, color)


def render(state: State) -> str:
    board = span.render(span.State(state.board, current_color(state), state.ply))
    color_name = {0: "Black", 1: "White"}
    return "\n".join(
        (
            board,
            f"Participant 1: {color_name[state.participant_colors[0]]}",
            f"Participant 2: {color_name[state.participant_colors[1]]}",
            (
                f"To move: Participant {state.participant + 1} "
                f"({color_name[current_color(state)]})"
            ),
            f"Swap available: {'yes' if state.swap_available else 'no'}",
        )
    )
