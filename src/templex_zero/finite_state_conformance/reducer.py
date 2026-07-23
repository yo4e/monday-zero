"""Frozen Study 004 black-box counterexample reducer.

The reducer receives one failing trace and reset-and-execute access to a
reference model and implementation under test. It contains no exact shortest-
trace oracle and makes no claim that its greedy result is globally minimal.
"""
from __future__ import annotations

from dataclasses import dataclass

from .execution import BlackBoxSystem, Trace, execute_trace, validate_trace
from .schema import MealyModel


@dataclass(frozen=True)
class ReductionResult:
    original_trace: Trace
    reduced_trace: Trace
    unique_executions: int
    cache_hits: int
    failing_candidates: int

    def __post_init__(self) -> None:
        if not self.original_trace:
            raise ValueError("original_trace must be non-empty")
        if not self.reduced_trace:
            raise ValueError("reduced_trace must be non-empty")
        if len(self.reduced_trace) > len(self.original_trace):
            raise ValueError("reducer cannot lengthen a trace")


class _FailureEvaluator:
    def __init__(self, reference: MealyModel, system: BlackBoxSystem) -> None:
        self.reference = reference
        self.system = system
        self._cache: dict[tuple[int, int, Trace], bool] = {}
        self.unique_executions = 0
        self.cache_hits = 0
        self.failing: set[Trace] = set()

    def fails(self, trace: Trace) -> bool:
        key = (id(self.reference), id(self.system), trace)
        if key in self._cache:
            self.cache_hits += 1
            return self._cache[key]
        execution = execute_trace(self.reference, self.system, trace)
        result = execution.detected
        self._cache[key] = result
        self.unique_executions += 1
        if result:
            self.failing.add(trace)
        return result


def _shortest_failing_prefix(trace: Trace, evaluator: _FailureEvaluator) -> Trace:
    low = 1
    high = len(trace)
    while low < high:
        middle = (low + high) // 2
        candidate = trace[:middle]
        if evaluator.fails(candidate):
            high = middle
        else:
            low = middle + 1
    return trace[:low]


def _delete_chunks(trace: Trace, evaluator: _FailureEvaluator) -> Trace:
    current = trace
    while len(current) > 2:
        changed = False
        for chunk_size in range(len(current) - 1, 1, -1):
            for start in range(0, len(current) - chunk_size + 1):
                candidate = current[:start] + current[start + chunk_size :]
                if candidate and evaluator.fails(candidate):
                    current = candidate
                    changed = True
                    break
            if changed:
                break
        if not changed:
            break
    return current


def _delete_individual_actions(trace: Trace, evaluator: _FailureEvaluator) -> Trace:
    current = trace
    while len(current) > 1:
        changed = False
        for index in range(len(current)):
            candidate = current[:index] + current[index + 1 :]
            if candidate and evaluator.fails(candidate):
                current = candidate
                changed = True
                break
        if not changed:
            break
    return current


def reduce_counterexample(
    reference: MealyModel,
    system: BlackBoxSystem,
    failing_trace: Trace,
) -> ReductionResult:
    """Apply the four frozen reduction stages in their committed order."""

    validate_trace(failing_trace)
    if not failing_trace:
        raise ValueError("failing_trace must be non-empty")
    evaluator = _FailureEvaluator(reference, system)
    if not evaluator.fails(failing_trace):
        raise ValueError("supplied trace does not produce an output mismatch")

    current = _shortest_failing_prefix(failing_trace, evaluator)
    current = _delete_chunks(current, evaluator)
    current = _delete_individual_actions(current, evaluator)

    same_length = [
        candidate for candidate in evaluator.failing if len(candidate) == len(current)
    ]
    reduced = min(same_length) if same_length else current
    if not evaluator.fails(reduced):
        raise AssertionError("reducer selected a non-failing trace")

    return ReductionResult(
        original_trace=failing_trace,
        reduced_trace=reduced,
        unique_executions=evaluator.unique_executions,
        cache_hits=evaluator.cache_hits,
        failing_candidates=len(evaluator.failing),
    )
