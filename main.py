"""Break Production, Own It — one brutally honest line to /output/entry.txt.

Stdlib only, no network, deterministic: the same confession every run.
"""

from pathlib import Path

LINE = "I dropped the production database to free up disk, then found the backups were empty and the pager already knew my name."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    OUT.chmod(0o644)


if __name__ == "__main__":
    main()
