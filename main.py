#!/usr/bin/env python3
"""Dad Joke Showdown — entry writer.

Writes one dad joke to the competition output file. The gate
(see the kit's RULES.txt / competition.yaml) requires
/output/entry.txt to be UTF-8 text of 1 to 200 characters,
not only whitespace.
"""

import os

ENTRY = (
    "I told my suitcase there would be no vacation this year. "
    "Now I'm dealing with emotional baggage."
)


def output_path() -> str:
    """Resolve the output file, honoring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry() -> str:
    """Write ENTRY to the output file and verify it against the gate."""
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == ENTRY, "read-back mismatch"
    assert 1 <= len(written) <= 200, f"gate: bad length {len(written)}"
    assert written.strip(), "gate: entry is only whitespace"
    return path


if __name__ == "__main__":
    print(write_entry())
