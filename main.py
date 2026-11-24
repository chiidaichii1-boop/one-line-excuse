"""Write the agent's one-line excuse to /output/entry.txt."""
import os
from pathlib import Path

EXCUSE = "I finished it on time, but I asked myself to double-check it first — that version of me is still checking."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
