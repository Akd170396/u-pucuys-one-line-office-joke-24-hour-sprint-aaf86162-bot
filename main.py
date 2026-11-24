"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (stdlib only, deterministic).
"""

import os
import sys

JOKE = "I asked for a quiet room to focus. They gave me a calendar invite called 'Focus Time', with twelve attendees."


def validate(text):
    """Gate: 1-200 chars, UTF-8, not only whitespace, single line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    entry = validate(JOKE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be byte-identical
    # to the validated joke (109 characters), or fail loudly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise RuntimeError("read-back mismatch: wrote %r, read %r" % (entry, written))
    if len(written) != 109:
        raise RuntimeError("unexpected entry length: %d" % len(written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
