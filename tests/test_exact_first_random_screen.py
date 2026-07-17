import inspect

from templex_zero.exact_first.manifest import selected_candidates

import experiments.run_study_002_random_screen as random_screen


def test_game_seeds_are_stable_and_game_specific():
    assert random_screen.game_seed(1, 0) == random_screen.game_seed(1, 0)
    assert len(
        {
            random_screen.game_seed(1, 0),
            random_screen.game_seed(1, 1),
            random_screen.game_seed(2, 0),
        }
    ) == 3


def test_random_game_is_reproducible_and_terminates():
    candidate = selected_candidates()[0]
    first = random_screen.play_random_game(candidate.spec, 12345)
    second = random_screen.play_random_game(candidate.spec, 12345)
    assert first == second
    assert first["winner"] in (0, 1, None)
    assert 1 <= first["plies"] <= candidate.spec.board_size**2
    assert first["opening"] is not None
    assert len(first["branching"]) == first["plies"]


def test_candidate_screen_records_frozen_aggregate_fields():
    candidate = selected_candidates()[0]
    first = random_screen.screen_candidate(candidate, games=25)
    second = random_screen.screen_candidate(candidate, games=25)
    assert first == second
    assert sum(first["results"][key] for key in ("first_participant", "second_participant", "draw")) == 25
    assert sum(first["openings"].values()) == 25
    assert sum(first["plies"]["histogram"].values()) == 25
    assert sum(first["branching"]["histogram"].values()) == first["branching"]["decision_points"]


def test_random_experiment_does_not_import_exact_values_or_shallow_search():
    source = inspect.getsource(random_screen)
    assert "exact_screen_v1" not in source
    assert "solve_exact" not in source
    assert "minimax" not in source
    assert "heuristic" not in source.lower()
