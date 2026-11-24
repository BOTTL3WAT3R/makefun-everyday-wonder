#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — entry program (program/v1).

Writes one sentence about a small moment of wonder in everyday life to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Standard library only; deterministic output.
"""

import os

ENTRY = (
    "At the red light, forty strangers tilt their heads to the same slow "
    "cloud, and for eight seconds the city has exactly one thought."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
