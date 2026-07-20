"""Deterministic file bundle for the frozen Study 003 corpus."""
from __future__ import annotations

import hashlib

from .corpus import generate_corpus
from .schema import ExpectedVerdict, SyntheticCorpus, TraceFixture, canonical_json_bytes, canonical_sha256


def corpus_bundle_files(corpus: SyntheticCorpus | None = None) -> dict[str, bytes]:
    """Return small independently auditable JSON files plus a hash index."""
    corpus = corpus or generate_corpus()
    groups: list[tuple[str, list[TraceFixture]]] = [
        ("minimal.json", [trace for trace in corpus.traces if trace.trace_id.startswith("P")]),
    ]
    for prefix in ("C1", "C2", "C3", "C4"):
        groups.append(
            (f"{prefix.lower()}.json", [trace for trace in corpus.traces if trace.trace_id.startswith(prefix)])
        )

    files: dict[str, bytes] = {}
    index_files: list[dict[str, object]] = []
    for filename, group_traces in groups:
        contracts: dict[str, dict[str, object]] = {}
        serialized_traces: list[dict[str, object]] = []
        for trace in group_traces:
            contract_id = trace.contract.contract_id
            contracts.setdefault(contract_id, trace.contract.to_dict())
            trace_dict: dict[str, object] = {
                "trace_id": trace.trace_id,
                "category": trace.category,
                "contract_id": contract_id,
                "events": [event.to_dict() for event in trace.events],
                "expected": trace.expected.to_dict(),
            }
            if trace.mutation_operator is not None:
                trace_dict["mutation_operator"] = trace.mutation_operator
                trace_dict["source_trace_id"] = trace.source_trace_id
            serialized_traces.append(trace_dict)
        payload = {
            "schema_version": corpus.schema_version,
            "group": filename.removesuffix(".json"),
            "contracts": list(contracts.values()),
            "traces": serialized_traces,
        }
        encoded = canonical_json_bytes(payload)
        files[filename] = encoded
        index_files.append(
            {
                "path": filename,
                "sha256": hashlib.sha256(encoded).hexdigest(),
                "trace_ids": [trace.trace_id for trace in group_traces],
            }
        )

    index = {
        "schema_version": corpus.schema_version,
        "proposal_path": corpus.proposal_path,
        "proposal_commit": corpus.proposal_commit,
        "canonical_corpus_sha256": canonical_sha256(corpus),
        "trace_count": len(corpus.traces),
        "valid_count": sum(trace.expected.verdict is ExpectedVerdict.VALID for trace in corpus.traces),
        "invalid_count": sum(trace.expected.verdict is ExpectedVerdict.INVALID for trace in corpus.traces),
        "event_count": sum(len(trace.events) for trace in corpus.traces),
        "files": index_files,
    }
    files["index.json"] = canonical_json_bytes(index)
    return files
