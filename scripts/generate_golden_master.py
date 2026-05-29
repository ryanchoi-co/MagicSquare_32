#!/usr/bin/env python
"""Generate or approve tests/golden_master_expected.txt baseline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests.golden_master.approve import DEFAULT_GOLDEN_PATH, write_golden_file
from tests.golden_master.capture import capture_all_scenarios


def main() -> int:
    """Run capture and write golden master baseline."""
    parser = argparse.ArgumentParser(
        description="Generate Golden Master expected output for Magic Square solver.",
    )
    parser.add_argument(
        "--approve",
        action="store_true",
        help="Overwrite existing baseline with current capture output.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_GOLDEN_PATH,
        help=f"Target file (default: {DEFAULT_GOLDEN_PATH})",
    )
    args = parser.parse_args()

    if args.output.is_file() and not args.approve:
        print(
            f"Baseline exists: {args.output}. "
            "Use --approve to overwrite.",
            file=sys.stderr,
        )
        return 1

    content = capture_all_scenarios()
    write_golden_file(content, args.output)
    print(f"Wrote golden master baseline: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
