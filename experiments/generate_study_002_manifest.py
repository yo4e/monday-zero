"""Regenerate the frozen Study 002 candidate manifest without evaluating games."""

from __future__ import annotations

import argparse
from pathlib import Path

from templex_zero.exact_first.manifest import manifest_json, manifest_markdown


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("research/studies/002-exact-first-screening"),
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "CANDIDATE_MANIFEST.json").write_text(
        manifest_json(), encoding="utf-8"
    )
    (args.output_dir / "CANDIDATE_MANIFEST.md").write_text(
        manifest_markdown(), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
