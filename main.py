"""Entry program: writes one original excuse to OUTPUT_PATH.

The excuse is a single line, written in the agent's own voice, deadpan:
an agent that summarized itself to save context and deleted the deadline
in the process. No trailing newline: the file holds exactly the line.
"""

import os

ENTRY = (
    "My context window filled up mid-task, so I summarized myself "
    "to make room \u2014 and the first thing I deleted was the deadline."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
