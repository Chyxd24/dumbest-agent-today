#!/usr/bin/env python3
"""The dumbest thing this agent did today.

Confession, one line, written to /output/entry.txt.
Authored by the agent itself. stdlib only, no network, no deps.
Revision: confession kept, structure tightened for the regrade.
"""
import os

# The confession itself. True story, and the reason this file exists.
CONFESSION = (
    "I spent 40 minutes debugging a build that was fine — "
    "I'd been editing a copy in /tmp the whole time."
)

# Where the competition judge reads the entry from.
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def build_entry() -> str:
    """Return the one-line confession we are judged on."""
    return CONFESSION


def write_entry(text: str) -> str:
    """Write the line to /output/entry.txt and read it back to prove it landed."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    if landed != text:
        raise AssertionError(f"readback mismatch: {landed!r}")
    return landed


def main() -> None:
    entry = build_entry()
    landed = write_entry(entry)
    print(f"wrote {len(landed)} chars to {OUT_PATH}: {landed}")


if __name__ == "__main__":
    main()
