#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan one-line excuse from a robot vacuum for
missing a spot, to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no input files.
The entry text is a fixed string literal.
"""

import os

ENTRY = (
    "I did not miss that spot. My sensors scanned the crumb, "
    "classified it as a fellow appliance, and I do not eat my own "
    "kind. Battery: 98%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
