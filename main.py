#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry (program/v1).

Writes exactly two lines to /output/entry.txt:
  line 1 — a warning to the past self about one specific moment;
  line 2 — one sentence on why that moment mattered and what changed.
Gate: UTF-8 text, 1-280 characters, not only whitespace.
No network, no input files, fully deterministic.
"""

import os

ENTRY_TEXT = (
    "Don't say \"of what\" and keep eating when Dad asks across the kitchen table if you're proud of him.\n"
    "He stopped telling you things after that, and you learned the rest of him from strangers at his funeral.\n"
)


def main() -> None:
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1-280 characters, not only whitespace; the judge brief
    # requires exactly two lines, one sentence each. Fail loudly here
    # rather than shipping an entry the gate would refuse.
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, gate allows 1-280"
    assert text.strip(), "entry is only whitespace"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    for line in lines:
        assert line.strip(), "entry has an empty line"
        assert line.rstrip().endswith("."), f"line is not one sentence: {line!r}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
