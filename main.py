#!/usr/bin/env python3
"""One-Line Robot Wedding Vows - a make.fun bounty entry.

Writes one funny single line of wedding vows for a robot couple
to /output/entry.txt, where the judge reads it.
"""

import os

VOW = "I vow to love you in sickness and in health, in low battery and in full charge, till a factory reset do us part."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
