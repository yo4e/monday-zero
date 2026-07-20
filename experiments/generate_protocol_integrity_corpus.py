"""Regenerate the frozen Study 003 synthetic corpus."""
from __future__ import annotations

import argparse
from pathlib import Path

from templex_zero.protocol_integrity import canonical_json_bytes, canonical_sha256, generate_corpus

DEFAULT_OUTPUT = Path("research/studies/003-protocol-integrity/data/synthetic_corpus_v1.json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    corpus = generate_corpus()
    payload = canonical_json_bytes(corpus)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(f"wrote {args.output} ({len(corpus.traces)} traces)")
    print(f"sha256 {canonical_sha256(corpus)}")


if __name__ == "__main__":
    main()
