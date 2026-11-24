#!/usr/bin/env python3
"""Print the one-line roast for the u-nayyy Roast Your Own Agent entry.

Stdlib only. Resolves entry.txt next to this file so it works from any
cwd, including a read-only /bot mount. Prints exactly one line.
"""

from pathlib import Path


def main() -> int:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    print(text.rstrip("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
