#!/usr/bin/env python3

"""Print ASCII codes with their corresponding characters."""

from __future__ import annotations

import argparse

PRINTABLE_START = 32
PRINTABLE_END = 126
MAX_ASCII = 127
CODE_WIDTH = 4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print ASCII codes and corresponding characters."
    )
    parser.add_argument(
        "--start",
        type=int,
        default=PRINTABLE_START,
        help=f"Starting ASCII code (default: {PRINTABLE_START}).",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=PRINTABLE_END,
        help=f"Ending ASCII code (default: {PRINTABLE_END}).",
    )
    return parser.parse_args()


def format_character(code: int) -> str:
    """Return printable ASCII directly and escape non-printable characters."""
    if PRINTABLE_START <= code <= PRINTABLE_END:
        return chr(code)
    return repr(chr(code))[1:-1]


def main() -> int:
    args = parse_args()
    if args.start < 0:
        raise SystemExit(f"--start must be >= 0 (got {args.start})")
    if args.end > MAX_ASCII:
        raise SystemExit(f"--end must be <= {MAX_ASCII} (got {args.end})")
    if args.start > args.end:
        raise SystemExit(
            f"--start must be <= --end (got start={args.start}, end={args.end})"
        )

    print(f"{'code':>{CODE_WIDTH}} char")
    print(f"{'-' * CODE_WIDTH} ----")
    for code in range(args.start, args.end + 1):
        print(f"{code:>{CODE_WIDTH}} {format_character(code)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
