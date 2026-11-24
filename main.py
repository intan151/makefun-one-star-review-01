#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes one deadpan one-star review of sleep to /output/entry.txt.
Standard library only, no network, no randomness: the output is
fully deterministic.
"""

import os

# One line, 128 characters: sleep as a subscription that overcharges.
# The grievance is the sharpest true one — eight hours paid nightly,
# returned as a sore neck, a dry mouth and the same problems — and the
# sting lands in the last few words ("right on schedule"), with the
# flat "One star." closing the complaint without winking at it.
LINE = "Sleep takes eight hours every night and gives back a sore neck, a dry mouth, and the same problems, right on schedule. One star."


def validate_entry(text):
    """The gate allows UTF-8 text of 1 to 160 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 160):
        raise ValueError("entry must be 1 to 160 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "!" in text:
        raise ValueError("entry must hold the deadpan: no exclamation marks")
    return text


def main():
    entry = validate_entry(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Re-read and confirm the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise RuntimeError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
