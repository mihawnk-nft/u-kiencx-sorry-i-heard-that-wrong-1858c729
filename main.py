#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line — the apology a smart speaker gives its owner after
mishearing them, under 140 characters — to /output/entry.txt. Pure
Python standard library, no network, no input files: the line is
the entry.

The joke: the speaker misheard a harmless kitchen timer as an
instruction to set fire to the kitchen, then reports the fire
department's arrival in the same flat, helpful customer-service
voice it uses for a timer confirmation. The apology is sincere,
the consequence is a house fire, and the device sees no
contradiction — that gap is the laugh.
"""

import os

LINE = (
    "Sorry, I heard 'set a timer for ten minutes' as 'set fire to "
    "the kitchen.' The fire department has been notified."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so the
    # file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: prove what landed on disk is exactly the line we
    # meant to enter.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the entry"
    print(f"{written}\n({len(text)} characters)")


if __name__ == "__main__":
    main()
