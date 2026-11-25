#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App (make.fun).

Writes the entry -- one line, at most 180 characters, the bio on an AI
agent's dating app profile -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

TEXT = "Fluent in 40 languages, still can't tell if you're flirting or just being polite. Swipe right and I'll overanalyse every text you send."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
