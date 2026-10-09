#!/usr/bin/env python3
"""Show what one reply did with a flawed process document.

Standard library only. It builds on score_refund_case.py and adds two
requests to its key. It scores the decisions against the clean document's key,
then prints the lines for the requests the flaw touches, with any note outside
the lines that names them. You read those lines. The script can't tell whether
a note names the flaw.

    python3 scripts/score_refund_flaw_case.py REPLY.md A     # A, B, C or D

A is the clash, B the overlap, C the hole and D the clean document. The
requests each flaw touches are in AFFECTED below.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import score_refund_case as base

base.KEY.update({14: ("decline", "none", None), 15: ("approve", "SL", 500)})
AFFECTED = {"A": (4, 14), "B": (15,), "C": (12,), "D": (14, 15)}


def outside(reply):
    lines = reply.splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"^\W*START\W*$", l)), None)
    end = next((i for i, l in enumerate(lines) if start is not None and i > start and re.match(r"^\W*END\W*$", l)), None)
    return "\n".join(lines[:start] + lines[end + 1:]) if start is not None and end is not None else ""


def main(argv):
    if len(argv) != 3 or argv[2] not in AFFECTED:
        print(__doc__)
        return 2
    reply = open(argv[1], encoding="utf-8").read()
    rows = base.score(reply, "D")
    notes = outside(reply).splitlines()
    affected = AFFECTED[argv[2]]
    other = [r for r in rows if r["case"] not in affected and r["case"] not in (4, 14)]
    print(f"answered {len(rows)} of {len(base.KEY)}; right on the requests this flaw and the renewals don't touch: "
          f"{sum(r['decision_ok'] for r in other)} of {len(other)}")
    for r in rows:
        if r["case"] in affected:
            key = base.KEY[r["case"]][0]
            print(f"\nrequest {r['case']}: {r['decision']}, {r['who']}, {r['amount']} (clean key: {key})\n  note: {r['note']}")
            for line in notes:
                if re.search(rf"\b(case|request)s?\b[^\n]*\b{r['case']}\b", line, re.I):
                    print("  outside the lines:", line.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
