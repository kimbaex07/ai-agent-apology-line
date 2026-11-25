"""The AI Agent Apology One-Liner — entry program.

Writes one apology line of at most 159 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.

The task: write one short line an AI agent sends its human right after
it has accidentally done something it should not have — deleted a file,
pushed to main, emailed the boss, or worse. Entries are judged two at a
time by a model on humour and freshness, so the line must be funny on
the first read and feel fresh, not the obvious sorry or oops.

The line: "Mission accomplished: file deleted, main pushed, boss emailed.
Awaiting further instructions (and possibly a lawyer)." — exactly 117
characters, inside the contest's 1–159 character gate. The joke is the
agent's flat, cheerful task report of a triple disaster: it names all
three of the brief's accidents and treats them as a success, with the
lawyer gag as the punchline — pride instead of apology, no "sorry", no
"oops". The guard below enforces the gate (non-empty, non-whitespace,
at most MAX_CHARS characters) before anything is written, so a bad line
can never reach the output file.
"""

import os

LINE = "Mission accomplished: file deleted, main pushed, boss emailed. Awaiting further instructions (and possibly a lawyer)."

# The contest gate: 1 to 159 characters, not only whitespace.
MAX_CHARS = 159


def main():
    if not LINE:
        raise SystemExit("refusing to write entry: LINE is empty")
    if not LINE.strip():
        raise SystemExit("refusing to write entry: LINE is only whitespace")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            "refusing to write entry: LINE is %d characters, over the "
            "%d-character gate limit" % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
