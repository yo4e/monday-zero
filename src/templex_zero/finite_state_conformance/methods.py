"""Frozen Study 004 black-box testing methods.

The methods may inspect the reference model for planning. They interact with the
implementation under test only through the BlackBoxSystem interface. This module
contains no corpus classification, paired-state oracle, or benchmark execution.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import hashlib
from itertools import product
import random
from typing import Iterator

from .execution import (
    BlackBoxSystem,
    Trace,
    TransitionKey,
    TransitionPairKey,
    execute_trace,
)
from .schema import ACTIONS, MealyModel

METHOD_UNIFORM_RANDOM = "uniform-random"
METHOD_LEXICOGRAPHIC_BREADTH = "lexicographic-breadth"
METHOD_TRANSITION_COVERAGE = "transition-coverage-guided"
CAMPAIGN_COUNT = 8


@dataclass(frozen=True)
class MethodResult:
    method: str
    budget: int
    detected: bool
    failing_trace: Trace | None
    mismatch_index: int | None
    expected_output: str | None
    observed_output: str | None
    actions_executed: int
    resets: int
    tests_executed: int
    transition_coverage: tuple[TransitionKey, ...]
    transition_pair_coverage: tuple[TransitionPairKey, ...]

    def __post_init__(self) -> None:
        if self.budget <= 0:
            raise ValueError("budget must be positive")
        if not 0 <= self.actions_executed <= self.budget:
            raise ValueError("actions_executed outside budget")
        if self.resets != self.tests_executed:
            raise ValueError("every test must be reset-delimited")
        if self.detected != (self.failing_trace is not None):
            raise ValueError("detected and failing_trace disagree")
        if self.detected and self.mismatch_index is None:
            raise ValueError("detected result requires mismatch_index")
        if not self.detected and any(
            value is not None
            for value in (
                self.mismatch_index,
                self.expected_output,
                self.observed_output,
            )
        ):
            raise ValueError("non-detection cannot contain mismatch fields")


def campaign_lengths(budget: int) -> tuple[int, ...]:
    """Split a formal budget into eight non-empty near-equal campaigns."""

    if budget < CAMPAIGN_COUNT:
        raise ValueError("budget must permit eight non-empty campaigns")
    base, remainder = divmod(budget, CAMPAIGN_COUNT)
    return tuple(base + (1 if index < remainder else 0) for index in range(CAMPAIGN_COUNT))


def _validate_digest(value: str, name: str) -> None:
    if len(value) != 64:
        raise ValueError(f"{name} must be 64 hexadecimal characters")
    try:
        int(value, 16)
    except ValueError as exc:
        raise ValueError(f"{name} must be hexadecimal") from exc


def random_campaign_seed(
    corpus_digest: str,
    mutant_id: str,
    budget: int,
    campaign_index: int,
) -> int:
    """Derive one independent fixed seed from the frozen campaign identity."""

    _validate_digest(corpus_digest, "corpus_digest")
    if not mutant_id:
        raise ValueError("mutant_id must be non-empty")
    if budget <= 0:
        raise ValueError("budget must be positive")
    if not 0 <= campaign_index < CAMPAIGN_COUNT:
        raise ValueError("campaign_index outside frozen eight-campaign range")
    material = "\x1f".join(
        (corpus_digest, mutant_id, str(budget), str(campaign_index))
    ).encode("utf-8")
    return int(hashlib.sha256(material).hexdigest(), 16)


def random_campaign_traces(
    corpus_digest: str,
    mutant_id: str,
    budget: int,
) -> tuple[Trace, ...]:
    traces: list[Trace] = []
    for campaign_index, length in enumerate(campaign_lengths(budget)):
        generator = random.Random(
            random_campaign_seed(corpus_digest, mutant_id, budget, campaign_index)
        )
        traces.append(tuple(generator.choice(ACTIONS) for _ in range(length)))
    return tuple(traces)


def lexicographic_sequences() -> Iterator[Trace]:
    """Yield non-empty traces by increasing length under a0 < a1 < a2."""

    length = 1
    while True:
        yield from product(ACTIONS, repeat=length)
        length += 1


def shortest_reference_paths(reference: MealyModel) -> dict[int, Trace]:
    """Find shortest lexicographically first reset paths to reachable states."""

    paths: dict[int, Trace] = {reference.reset_state: ()}
    queue: deque[int] = deque([reference.reset_state])
    while queue:
        state = queue.popleft()
        prefix = paths[state]
        for action_index, action in enumerate(ACTIONS):
            target = reference.transitions[state][action_index].target
            if target not in paths:
                paths[target] = prefix + (action,)
                queue.append(target)
    return paths


def transition_target_traces(
    reference: MealyModel,
) -> tuple[tuple[TransitionKey, Trace], ...]:
    """Frozen deterministic candidate traces for reachable transitions."""

    paths = shortest_reference_paths(reference)
    candidates = [
        ((state, action), paths[state] + (action,))
        for state in paths
        for action in ACTIONS
    ]
    return tuple(sorted(candidates, key=lambda item: (len(item[1]), item[1], item[0])))


def transition_pair_target_traces(
    reference: MealyModel,
) -> tuple[tuple[TransitionPairKey, Trace], ...]:
    """Frozen deterministic candidate traces for reachable transition pairs."""

    paths = shortest_reference_paths(reference)
    candidates: list[tuple[TransitionPairKey, Trace]] = []
    for state in paths:
        for first_index, first_action in enumerate(ACTIONS):
            middle = reference.transitions[state][first_index].target
            for second_action in ACTIONS:
                key = (state, first_action, middle, second_action)
                candidates.append((key, paths[state] + (first_action, second_action)))
    return tuple(sorted(candidates, key=lambda item: (len(item[1]), item[1], item[0])))


def _finish_result(
    *,
    method: str,
    budget: int,
    detected_execution,
    actions_executed: int,
    tests_executed: int,
    covered_transitions: set[TransitionKey],
    covered_pairs: set[TransitionPairKey],
) -> MethodResult:
    if detected_execution is None:
        return MethodResult(
            method=method,
            budget=budget,
            detected=False,
            failing_trace=None,
            mismatch_index=None,
            expected_output=None,
            observed_output=None,
            actions_executed=actions_executed,
            resets=tests_executed,
            tests_executed=tests_executed,
            transition_coverage=tuple(sorted(covered_transitions)),
            transition_pair_coverage=tuple(sorted(covered_pairs)),
        )
    return MethodResult(
        method=method,
        budget=budget,
        detected=True,
        failing_trace=detected_execution.failing_trace,
        mismatch_index=detected_execution.mismatch_index,
        expected_output=detected_execution.expected_output,
        observed_output=detected_execution.observed_output,
        actions_executed=actions_executed,
        resets=tests_executed,
        tests_executed=tests_executed,
        transition_coverage=tuple(sorted(covered_transitions)),
        transition_pair_coverage=tuple(sorted(covered_pairs)),
    )


def _execute_campaigns(
    *,
    method: str,
    reference: MealyModel,
    system: BlackBoxSystem,
    budget: int,
    traces: Iterator[Trace],
) -> MethodResult:
    if budget <= 0:
        raise ValueError("budget must be positive")
    actions_executed = 0
    tests_executed = 0
    covered_transitions: set[TransitionKey] = set()
    covered_pairs: set[TransitionPairKey] = set()

    for trace in traces:
        remaining = budget - actions_executed
        if len(trace) > remaining:
            break
        execution = execute_trace(reference, system, trace)
        tests_executed += 1
        actions_executed += execution.actions_executed
        covered_transitions.update(execution.transitions)
        covered_pairs.update(execution.transition_pairs)
        if execution.detected:
            return _finish_result(
                method=method,
                budget=budget,
                detected_execution=execution,
                actions_executed=actions_executed,
                tests_executed=tests_executed,
                covered_transitions=covered_transitions,
                covered_pairs=covered_pairs,
            )
        if actions_executed == budget:
            break

    return _finish_result(
        method=method,
        budget=budget,
        detected_execution=None,
        actions_executed=actions_executed,
        tests_executed=tests_executed,
        covered_transitions=covered_transitions,
        covered_pairs=covered_pairs,
    )


def run_uniform_random(
    reference: MealyModel,
    system: BlackBoxSystem,
    *,
    budget: int,
    corpus_digest: str,
    mutant_id: str,
) -> MethodResult:
    return _execute_campaigns(
        method=METHOD_UNIFORM_RANDOM,
        reference=reference,
        system=system,
        budget=budget,
        traces=iter(random_campaign_traces(corpus_digest, mutant_id, budget)),
    )


def run_lexicographic_breadth(
    reference: MealyModel,
    system: BlackBoxSystem,
    *,
    budget: int,
) -> MethodResult:
    return _execute_campaigns(
        method=METHOD_LEXICOGRAPHIC_BREADTH,
        reference=reference,
        system=system,
        budget=budget,
        traces=lexicographic_sequences(),
    )


def run_transition_coverage_guided(
    reference: MealyModel,
    system: BlackBoxSystem,
    *,
    budget: int,
) -> MethodResult:
    """Execute transition coverage once, then repeated pair-coverage rounds.

    A new pair-coverage round begins after every reachable pair has been covered
    in the current round. This deterministic repetition consumes the available
    equal-action budget without adapting to mutant internals. A test is never
    partially executed when it does not fit the remaining budget.
    """

    if budget <= 0:
        raise ValueError("budget must be positive")
    transition_candidates = transition_target_traces(reference)
    pair_candidates = transition_pair_target_traces(reference)
    uncovered_transitions = {key for key, _ in transition_candidates}
    uncovered_pairs_in_round = {key for key, _ in pair_candidates}

    actions_executed = 0
    tests_executed = 0
    covered_transitions: set[TransitionKey] = set()
    covered_pairs: set[TransitionPairKey] = set()

    while actions_executed < budget:
        if uncovered_transitions:
            candidates = [
                (key, trace)
                for key, trace in transition_candidates
                if key in uncovered_transitions
            ]
        else:
            if not uncovered_pairs_in_round:
                uncovered_pairs_in_round = {key for key, _ in pair_candidates}
            candidates = [
                (key, trace)
                for key, trace in pair_candidates
                if key in uncovered_pairs_in_round
            ]

        if not candidates:
            break
        _, trace = candidates[0]
        remaining = budget - actions_executed
        if len(trace) > remaining:
            break

        execution = execute_trace(reference, system, trace)
        tests_executed += 1
        actions_executed += execution.actions_executed
        covered_transitions.update(execution.transitions)
        covered_pairs.update(execution.transition_pairs)
        uncovered_transitions.difference_update(execution.transitions)
        uncovered_pairs_in_round.difference_update(execution.transition_pairs)

        if execution.detected:
            return _finish_result(
                method=METHOD_TRANSITION_COVERAGE,
                budget=budget,
                detected_execution=execution,
                actions_executed=actions_executed,
                tests_executed=tests_executed,
                covered_transitions=covered_transitions,
                covered_pairs=covered_pairs,
            )

    return _finish_result(
        method=METHOD_TRANSITION_COVERAGE,
        budget=budget,
        detected_execution=None,
        actions_executed=actions_executed,
        tests_executed=tests_executed,
        covered_transitions=covered_transitions,
        covered_pairs=covered_pairs,
    )
