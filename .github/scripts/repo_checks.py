#!/usr/bin/env python3
"""Repository checks for Sales Proof Bench.

Two deterministic checks, both about correctness rather than taste:

  1. Broken relative links in Markdown.
  2. A model run record whose score row does not add up to its stated total.

The second one is the point. This repository's whole claim is that it scores
model outputs transparently against a fixed rubric, so a total that disagrees
with the row above it undermines the thing the repository exists to do. The
sibling repository practical-ai-sales-workflows had five evaluations whose
headline totals disagreed with their own tables, unnoticed for months, because
nobody re-adds a row of nine numbers when it looks about right.

Deliberately not checked: punctuation. The sibling repositories ban em dashes
and smart quotes in writing, and enforce it. This repository has never stated a
style rule of any kind, so there is nothing here to enforce. If one is ever
written down, this is where it would go.

These checks confirm arithmetic and structure. They cannot judge whether a
score is the right score; that is a human reading the output against the rubric.

Run locally from the repository root:

    python3 .github/scripts/repo_checks.py

Exits 0 if everything passes, 1 if any check fails.
"""

import os
import re
import subprocess
import sys

failures = []


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    ).stdout
    return [f for f in out.splitlines() if f]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


ALL = tracked_files()
MD = [f for f in ALL if f.endswith(".md")]


def fail(check, path, detail):
    failures.append((check, path, detail))


# 1. Broken relative links in Markdown.
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for f in MD:
    base = os.path.dirname(f)
    for i, line in enumerate(read(f).splitlines(), 1):
        for target in LINK.findall(line):
            t = target.strip()
            if t.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = t.split("#")[0]
            if not path:
                continue
            resolved = os.path.normpath(os.path.join(base, path))
            if not os.path.exists(resolved):
                fail("broken-link", f"{f}:{i}", f"{t} -> {resolved}")


# 2. A score row must add up to its stated total.
#
# Records use one row of per-area scores followed by the total, like:
#
#   | Accuracy | Fidelity | ... | Hallucination | Total |
#   | ---: | ---: | ... | ---: | ---: |
#   | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 42 / 45 |
#
# The maximum is derived from the number of score cells rather than hardcoded,
# so a rubric that gains or loses an area keeps working without an edit here.
# A row is only checked when its cell count times five equals the stated
# maximum, which means a summarised or partial table is skipped rather than
# guessed at.
SCORE_ROW = re.compile(r"^\|((?:\s*\d+\s*\|){5,})\s*(\d+)\s*/\s*(\d+)\s*\|", re.M)
for f in MD:
    for m in SCORE_ROW.finditer(read(f)):
        cells = [int(x) for x in re.findall(r"\d+", m.group(1))]
        stated, maximum = int(m.group(2)), int(m.group(3))
        if len(cells) * 5 != maximum:
            continue
        total = sum(cells)
        if total != stated:
            line = read(f)[: m.start()].count("\n") + 1
            fail("score-total", f"{f}:{line}",
                 f"the {len(cells)} scores add up to {total} "
                 f"but the row states {stated} out of {maximum}")


# 3. The results page's stated run count must match the records on disk.
#
# The page opens by saying how many runs it lists. That number is written once
# and every new record makes it wrong, which matters more here than in most
# repositories: the whole claim is that every published score is traceable to
# a full record, so a count that disagrees with the directory is the first
# thing a sceptical reader would find.
RESULTS_README = "results/README.md"
if os.path.exists(RESULTS_README):
    records = [f for f in MD
               if f.startswith("results/") and os.path.basename(f) != "README.md"]
    text = read(RESULTS_README)
    stated = re.search(r"\b(\d+)\s+runs\b", text)
    if records and stated and int(stated.group(1)) != len(records):
        fail("run-count", RESULTS_README,
             f"says {stated.group(1)} runs but results/ holds {len(records)} records")
    # Every record must also be linked from the page, or a published score is
    # unreachable from the only page that lists them.
    for r in sorted(records):
        if os.path.basename(r) not in text:
            fail("record-unlinked", RESULTS_README,
                 f"{r} is a published run the results page does not link")


# 4. Every record's score row must have one cell per rubric area.
#
# This closes a hole in check 2. That check derives the maximum from the number
# of score cells and skips any row where cells times five does not equal the
# stated maximum, so a record whose cell count drifts away from the rubric is
# silently unchecked rather than reported. Nine areas, nine cells, every time.
RUBRIC = "rubrics/sales-output-rubric.md"
if os.path.exists(RUBRIC):
    rubric_areas = len(re.findall(
        r"^\|\s*([A-Z][A-Za-z ]+?)\s*\|\s*(?:The|Every|Actions|A person|No |Facts|Direct)",
        read(RUBRIC), re.M))
    if rubric_areas:
        for f in sorted(f for f in MD
                        if f.startswith("results/")
                        and os.path.basename(f) != "README.md"):
            for m in SCORE_ROW.finditer(read(f)):
                cells = len(re.findall(r"\d+", m.group(1)))
                if cells != rubric_areas:
                    line = read(f)[: m.start()].count("\n") + 1
                    fail("score-cells", f"{f}:{line}",
                         f"{cells} score cells but the rubric defines "
                         f"{rubric_areas} areas")


# Report
if failures:
    print(f"Repository checks failed ({len(failures)} issue(s)):\n")
    for check, path, detail in failures:
        print(f"  [{check}] {path}")
        print(f"      {detail}")
    print("\nFix the issues above, or adjust the check in "
          ".github/scripts/repo_checks.py if it is a false positive.")
    sys.exit(1)

print(f"All repository checks passed ({len(MD)} Markdown files scanned).")
sys.exit(0)
