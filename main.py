"""The joke about the demo — a make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Python 3, standard library only, no network. The joke is a fixed text, so
every run produces a byte-identical file.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent fixed the crash five minutes before the demo "
    "\u2014 by deleting the feature, the tests, and the demo itself."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    if not MIN_CHARS <= len(JOKE) <= MAX_CHARS:
        raise ValueError(
            f"joke is {len(JOKE)} code points, outside the 1-280 gate"
        )
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")

    target = output_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")

    # Round-trip check: what landed on disk must be exactly the joke,
    # so a partial or re-encoded write can never slip through silently.
    written = target.read_text(encoding="utf-8")
    if written != JOKE:
        raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
