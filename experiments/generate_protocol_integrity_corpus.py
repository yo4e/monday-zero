"""Regenerate the frozen Study 003 synthetic corpus bundle."""
from __future__ import annotations

import argparse
from pathlib import Path

from templex_zero.protocol_integrity import canonical_sha256, corpus_bundle_files, generate_corpus

DEFAULT_OUTPUT = Path("research/studies/003-protocol-integrity/data/synthetic_corpus_v1")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    corpus = generate_corpus()
    files = corpus_bundle_files(corpus)
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in files.items():
        (args.output / name).write_bytes(payload)
    print(f"wrote {len(files)} files to {args.output} ({len(corpus.traces)} traces)")
    print(f"sha256 {canonical_sha256(corpus)}")


if __name__ == "__main__":
    main()
