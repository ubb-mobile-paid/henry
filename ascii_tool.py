#!/usr/bin/env python3

"""Print ASCII codes with their corresponding characters."""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print ASCII codes and corresponding characters."
    )
    parser.add_argument(
        "--start",
        type=int,
        default=32,
        help="Starting ASCII code (default: 32).",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=126,
        help="Ending ASCII code (default: 126).",
    )
    return parser.parse_args()


def format_character(code: int) -> str:
    if 32 <= code <= 126:
        return chr(code)
    return repr(chr(code))[1:-1]


def main() -> int:
    args = parse_args()
    if args.start < 0 or args.end > 127 or args.start > args.end:
        raise SystemExit("Expected 0 <= --start <= --end <= 127")

    for code in range(args.start, args.end + 1):
        print(f"{code:3} {format_character(code)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
