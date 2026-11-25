#!/usr/bin/env python3
"""Snooze Button Roast — one line roasting an alarm clock that rings
at 6 AM on a Saturday. Writes the roast to /output/entry.txt."""

from pathlib import Path

ENTRY = "My alarm rang at 6 AM on a Saturday with the confidence of a man who has never once checked a calendar — so I made the snooze button my union rep."

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> int:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the 200 limit")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
