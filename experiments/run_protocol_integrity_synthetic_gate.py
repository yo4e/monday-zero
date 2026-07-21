"""Run the frozen Study 003 synthetic correctness gate."""
from __future__ import annotations

import argparse
from pathlib import Path

from templex_zero.protocol_integrity.synthetic_gate import canonical_bytes, run_gate

DEFAULT_DATA = Path("research/studies/003-protocol-integrity/data/synthetic_corpus_v1")
DEFAULT_OUTPUT = Path("research/studies/003-protocol-integrity/data/synthetic_gate_v1.json")
DEFAULT_SOURCES = [
    Path("src/templex_zero/protocol_integrity/validator.py"),
    Path("src/templex_zero/protocol_integrity/oracle.py"),
    Path("src/templex_zero/protocol_integrity/baseline.py"),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = run_gate(args.data_dir, DEFAULT_SOURCES)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical_bytes(report))
    print(f"passed={report['passed']}")
    print(report["metrics"])
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
