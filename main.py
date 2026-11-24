"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday life
to /output/entry.txt (overridable with the OUTPUT_DIR environment
variable). Standard library only.
"""

import os
import sys

ENTRY = "The water jug gulps once after I fill my glass, as if the kitchen were drinking behind my back."


def main():
    # Gate: 1-200 characters, not only whitespace, valid UTF-8.
    assert isinstance(ENTRY, str), "entry must be text"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    # Gate: exactly one sentence.
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    data = ENTRY.encode("utf-8")
    assert data.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and prove the file is byte-identical to the entry,
    # with no trailing newline added.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt differs from the entry"
    assert not written.endswith(b"\n"), "entry.txt must have no trailing newline"

    return 0


if __name__ == "__main__":
    sys.exit(main())
