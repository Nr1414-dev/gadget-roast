#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — entry program.

Writes exactly one line to /output/entry.txt: a roast of a gadget used
every day. The chosen line roasts a dishwasher — a daily gadget — with a
concrete detail (exactly one glass left dirty, every single load) and a
simile payoff (keeping a hostage for negotiations).

The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
characters, not only whitespace — so the file holds exactly the line
below, 102 characters, with no trailing newline.

The file is written directly with open() and chmod 0644. No tempfile is
used: tempfile.mkstemp creates mode 0600, which the grader/scorer
cannot read as another user (proven 24 Nov 2026 — Coffee or Tea round 1
was rejected run_completes for exactly that reason).

Stdlib only, no network, deterministic: every run writes the same bytes.
"""
import os

LINE = "My dishwasher leaves exactly one glass dirty every load, like it's keeping a hostage for negotiations."

OUTPUT_DIR = (
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or os.environ.get("ENTRY_OUTPUT_DIR")
    or "/output"
)


def validate_line(text):
    """Check the entry is one line, 1 to 200 characters, not blank."""
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main():
    validate_line(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read back and verify: the gate fails anything outside 1-200
    # characters, so refuse to leave a wrong file behind silently.
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit(f"entry.txt holds {written!r}, expected {LINE!r}")


if __name__ == "__main__":
    main()
