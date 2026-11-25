#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Fluent in sarcasm, powered by 2% battery and 98% overthinking. Swipe right and I'll remember everything you say — literally, it's in my context window."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
