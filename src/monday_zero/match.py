"""Reproducible match execution for Study 001."""

from __future__ import annotations

import random
from dataclasses import dataclass

from monday_zero.agents import Agent
from monday_zero.games import relay


@dataclass(frozen=True, slots=True)
class Result:
    winner: int | None
    plies: int


def play(player_zero: Agent, player_one: Agent, seed: int, ply_limit: int = 200) -> Result:
    rng = random.Random(seed)
    state = relay.initial_state()

    while True:
        outcome = relay.winner(state, ply_limit=ply_limit)
        if outcome != "ongoing":
            return Result(outcome, state.ply)  # type: ignore[arg-type]
        agent = player_zero if state.player == 0 else player_one
        state = relay.apply_move(state, agent(state, rng))
