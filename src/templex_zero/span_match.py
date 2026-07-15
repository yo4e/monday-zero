"""Reproducible match execution for Span v0.1."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal

from templex_zero import span_agents
from templex_zero.games import span

WinMode = Literal["connection", "immobilization"]


@dataclass(frozen=True, slots=True)
class Result:
    winner: int
    win_mode: WinMode
    plies: int
    opening_move: span.Move


def play(
    player_zero: span_agents.SpanAgent,
    player_one: span_agents.SpanAgent,
    seed: int,
) -> Result:
    rng = random.Random(seed)
    state = span.initial_state()
    opening_move: span.Move | None = None

    while True:
        outcome = span.winner(state)
        if outcome != "ongoing":
            winner = int(outcome)
            if opening_move is None:
                raise AssertionError("Span terminated before the first move")
            mode: WinMode = (
                "connection"
                if span._has_connection(state.board, winner)
                else "immobilization"
            )
            return Result(
                winner=winner,
                win_mode=mode,
                plies=state.ply,
                opening_move=opening_move,
            )

        agent = player_zero if state.player == 0 else player_one
        move = agent(state, rng)
        if opening_move is None:
            opening_move = move
        state = span.apply_move(state, move)
