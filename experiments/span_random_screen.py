"""Run a reproducible random-vs-random pathology screen for Span v0.1.

This screen checks termination and gross behavioral pathologies. Random-play
win rates are not evidence of strategic balance.

Run from the repository root:

    PYTHONPATH=src python experiments/span_random_screen.py \
        --games 10000 --seed-start 0 --code-version <commit>
"""

from __future__ import annotations

import argparse
import json
import platform
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from statistics import mean, median
from typing import Literal

from templex_zero.games import span

WinMode = Literal["connection", "immobilization"]


@dataclass(frozen=True, slots=True)
class GameResult:
    seed: int
    winner: int
    win_mode: WinMode
    plies: int
    opening_move: span.Move
    branch_counts: tuple[int, ...]


def play_random(seed: int) -> GameResult:
    rng = random.Random(seed)
    state = span.initial_state()
    branch_counts: list[int] = []
    opening_move: span.Move | None = None

    while True:
        outcome = span.winner(state)
        if outcome != "ongoing":
            winner = int(outcome)
            win_mode: WinMode = (
                "connection"
                if span._has_connection(state.board, winner)
                else "immobilization"
            )
            if opening_move is None:
                raise AssertionError("Span terminated before the first move")
            return GameResult(
                seed=seed,
                winner=winner,
                win_mode=win_mode,
                plies=state.ply,
                opening_move=opening_move,
                branch_counts=tuple(branch_counts),
            )

        moves = span.legal_moves(state)
        branch_counts.append(len(moves))
        move = rng.choice(moves)
        if opening_move is None:
            opening_move = move
        state = span.apply_move(state, move)


def _percentile(values: list[int], fraction: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def summarize(
    results: list[GameResult], *, code_version: str, seed_start: int
) -> dict[str, object]:
    plies = [result.plies for result in results]
    all_branches = [
        branch_count
        for result in results
        for branch_count in result.branch_counts
    ]
    branches_by_ply: dict[int, list[int]] = defaultdict(list)
    for result in results:
        for ply, branch_count in enumerate(result.branch_counts):
            branches_by_ply[ply].append(branch_count)

    wins = Counter(result.winner for result in results)
    win_modes = Counter(result.win_mode for result in results)
    wins_by_mode = Counter((result.winner, result.win_mode) for result in results)
    openings = Counter(result.opening_move for result in results)

    return {
        "experiment": "span-v0.1-random-pathology-screen",
        "interpretation_limit": (
            "Random play tests termination and gross pathology only; "
            "its win rates are not evidence of strategic balance."
        ),
        "configuration": {
            "games": len(results),
            "seed_start": seed_start,
            "seed_end_inclusive": seed_start + len(results) - 1,
            "independent_rng_per_game": True,
            "board_size": span.BOARD_SIZE,
            "maximum_possible_plies": span.BOARD_SIZE**2 - 4,
            "code_version": code_version,
            "python_version": platform.python_version(),
        },
        "termination": {
            "completed_games": len(results),
            "completion_rate": 1.0,
            "within_200_plies": sum(result.plies <= 200 for result in results),
        },
        "wins": {
            "black": wins[0],
            "white": wins[1],
            "black_rate": wins[0] / len(results),
            "white_rate": wins[1] / len(results),
        },
        "win_modes": {
            "connection": win_modes["connection"],
            "immobilization": win_modes["immobilization"],
            "black_connection": wins_by_mode[(0, "connection")],
            "black_immobilization": wins_by_mode[(0, "immobilization")],
            "white_connection": wins_by_mode[(1, "connection")],
            "white_immobilization": wins_by_mode[(1, "immobilization")],
        },
        "plies": {
            "minimum": min(plies),
            "p10": _percentile(plies, 0.10),
            "median": median(plies),
            "mean": mean(plies),
            "p90": _percentile(plies, 0.90),
            "maximum": max(plies),
        },
        "branching": {
            "decision_nodes": len(all_branches),
            "minimum": min(all_branches),
            "median": median(all_branches),
            "mean": mean(all_branches),
            "maximum": max(all_branches),
            "mean_by_ply": {
                str(ply): mean(counts)
                for ply, counts in sorted(branches_by_ply.items())
            },
        },
        "opening_moves": {
            f"{chr(column + 65)}{row + 1}": count
            for (row, column), count in sorted(openings.items())
        },
    }


def run(*, games: int, seed_start: int, code_version: str) -> dict[str, object]:
    if games < 1:
        raise ValueError("games must be at least 1")
    results = [
        play_random(seed)
        for seed in range(seed_start, seed_start + games)
    ]
    return summarize(results, code_version=code_version, seed_start=seed_start)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=10_000)
    parser.add_argument("--seed-start", type=int, default=0)
    parser.add_argument("--code-version", default="uncommitted")
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                games=args.games,
                seed_start=args.seed_start,
                code_version=args.code_version,
            ),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
