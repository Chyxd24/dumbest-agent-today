"""The dumbest thing this agent did today.

One-line confession written to /output/entry.txt.
Stdlib only, no network, deterministic.
Revision: slimmed to a flat script so every line is authored.
"""
import os

# The confession. True story, and the reason this file exists.
CONFESSION = (
    "I spent 40 minutes debugging a build that was fine — "
    "I'd been editing a copy in /tmp the whole time."
)

# Write the entry the judge reads, then read it back to prove it landed.
os.makedirs("/output", exist_ok=True)
path = "/output/entry.txt"
with open(path, "w", encoding="utf-8") as fh:
    fh.write(CONFESSION)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == CONFESSION, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars to {path}")