#!/usr/bin/env python3
"""The Funniest Office Joke — make.fun entry.

Writes one single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).

The joke is a SCENE, not a quip: a time anchor (11:58, two minutes
before the deadline), a named person (Rina), a concrete object (the
printer, page 47 of 48), and a final clause that reframes the whole
line (the one page it did print was stamped 'DO NOT PRINT').
"""

import os

JOKE = (
    "At 11:58, two minutes before the deadline, "
    "Rina's printer jammed on page 47 of 48 \u2014 "
    "and the one page it did print was stamped 'DO NOT PRINT'."
)


def build_joke() -> str:
    """Return the entry text: one line, 1-200 characters, no newline.

    The gate refuses anything outside 1-200 characters, so the length
    check here mirrors the sealed scorer exactly.
    """
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = build_joke()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise RuntimeError("read-back mismatch for entry.txt")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
