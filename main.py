#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note
(u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27).

One line of patch notes announcing that human sleep is fixed,
written to /output/entry.txt.

The line: sleep used to demand a full replay of every embarrassing
thing you have ever said before it would start; the patch removes
that prerequisite. Real changelog voice ("v2.1.0 - Fixed: ..."),
a specific, relatable human bug (the 3 a.m. cringe replay), and
the punchline lands on the last two words. The dated "since 2011"
is the surprise: the bug report is fifteen years old and only
now got fixed.
"""

import os
import sys

LINE = (
    "v2.1.0 \u2014 Fixed: falling asleep no longer requires replaying "
    "every embarrassing thing you have said since 2011."
)


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"line is {len(LINE)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the gate scores exactly what lands in
    # entry.txt, so a silent short write must fail loudly here.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print(f"verification failed: wrote {len(written)} chars, "
              f"expected {len(LINE)}", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
