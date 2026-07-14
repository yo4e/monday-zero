"""Reproduce the first Relay baseline experiment.

Run from the repository root:

    PYTHONPATH=src python experiments/relay_baseline.py
"""

from __future__ import annotations

import json
from collections import Counter
from statistics import mean

from monday_zero.agents import minimax_agent, random_agent
from monday_zero.match import play


def summarize(results):
    return {
        "wins": dict(Counter(str(result.winner) for result in results)),
        "mean_plies": mean(result.plies for result in results),
        "max_plies": max(result.plies for result in results),
    }


def strength_test(depth: int, games_per_seat: int = 100):
    strong = minimax_agent(depth)
    results = []
    strong_wins = 0
    random_wins = 0

    for seed in range(games_per_seat):
        first = play(strong, random_agent, seed)
        second = play(random_agent, strong, 1000 + seed)
        results.extend((first, second))
        strong_wins += first.winner == 0
        strong_wins += second.winner == 1
        random_wins += first.winner == 1
        random_wins += second.winner == 0

    return {
        "depth": depth,
        "strong_wins": strong_wins,
        "random_wins": random_wins,
        "draws": len(results) - strong_wins - random_wins,
        "mean_plies": mean(result.plies for result in results),
    }


def main():
    random_results = [play(random_agent, random_agent, seed) for seed in range(2000)]
    symmetric_results = [play(minimax_agent(2), minimax_agent(2), seed) for seed in range(200)]

    report = {
        "configuration": {
            "board_size": 5,
            "ply_limit": 200,
            "random_games": 2000,
            "strength_games_per_seat": 100,
            "symmetric_depth_2_games": 200,
        },
        "random_vs_random": summarize(random_results),
        "strength_tests": [strength_test(depth) for depth in (1, 2, 3)],
        "depth_2_vs_depth_2": summarize(symmetric_results),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
