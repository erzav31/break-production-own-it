#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line, the confession an AI agent prints the
instant it breaks production, to /output/entry.txt.

The line is a single line of UTF-8 text, 1-200 characters, no trailing
newline games: the gate counts characters, so we keep it well inside.
"""

import os

ENTRY = "I ran chmod -R 777 / to fix one permission error. Everything has permission now. Nothing works."


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # No trailing newline: the file holds exactly the one line, so the
        # gate counts precisely the 95 characters of the confession.
        f.write(line)


if __name__ == "__main__":
    main()
