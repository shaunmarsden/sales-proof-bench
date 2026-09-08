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

# The scoring pack states the same count in words, and this check did not
# cover it. Adding the twenty-first run updated the results page, which is
# checked, and left the pack closing on "twenty runs, one scorer", which was
# not. A count written as a word is exactly the kind a reader trusts and a
# regex looking for digits walks straight past.
NUMBER_WORDS = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "twenty-one": 21, "twenty-two": 22,
    "twenty-three": 23, "twenty-four": 24, "twenty-five": 25,
    "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28,
    "twenty-nine": 29, "thirty": 30,
}
COUNTED_PAGES = ["feedback/score-a-run-yourself.md", "README.md"]
records = [f for f in MD
           if f.startswith("results/") and os.path.basename(f) != "README.md"]
if records:
    word_or_digit = re.compile(
        r"\b(" + "|".join(sorted(NUMBER_WORDS, key=len, reverse=True))
        + r"|\d+)\s+runs\b", re.I)
    for page in COUNTED_PAGES:
        if not os.path.exists(page):
            continue
        for i, line in enumerate(read(page).splitlines(), 1):
            found = word_or_digit.search(line)
            if not found:
                continue
            token = found.group(1).lower()
            value = NUMBER_WORDS.get(token, None)
            if value is None:
                value = int(token) if token.isdigit() else None
            if value is not None and value != len(records):
                fail("run-count", f"{page}:{i}",
                     f"says {found.group(1)} runs but results/ holds "
                     f"{len(records)} records")


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


# 5. The scoring pack's copy of an output must match the record.
#
# feedback/score-a-run-yourself.md reproduces one model output in full, so a
# reader can score it without opening the record that holds my score. That
# duplication is the point: it stops the exercise being spoiled by one scroll
# too far. It also means two copies of the same output now exist, and a silent
# drift between them would make the pack a test of something this repository
# never published. Records are retained unedited by policy, so any difference
# is a mistake rather than an update.
PACK = "feedback/score-a-run-yourself.md"
RECORD = "results/claude-haiku-4-5-osmond-objection-diagnosis-case.md"


def slice_output(text, start_mark, end_mark):
    """The output between two headings, whitespace normalised, or None."""
    if start_mark not in text or end_mark not in text:
        return None
    body = text.split(start_mark, 1)[1].split(end_mark, 1)[0]
    return " ".join(body.split())


if os.path.exists(PACK) and os.path.exists(RECORD):
    record_out = slice_output(read(RECORD), "## Two Distinct Readings", "## Score")
    pack_out = slice_output(read(PACK), "## Two Distinct Readings", "## The Scale")
    if record_out is None or pack_out is None:
        fail("scoring-pack-shape", PACK,
             "cannot locate the output in the pack or the record, so the two "
             "copies cannot be compared")
    elif pack_out.rstrip("- ") != record_out.rstrip("- "):
        fail("scoring-pack-drift", PACK,
             "the reproduced output no longer matches "
             f"{RECORD}, so the pack would be scoring something unpublished")
    # And the pack must not give the answer away.
    if "31" in read(PACK).split("## Fill This In")[0].replace("2026", ""):
        fail("scoring-pack-spoiler", PACK,
             "the score appears above the blank table")


# 6. The web page's copies of the output and of my scores must match the record.
#
# docs/index.html reproduces the same output as the scoring pack, so a reader
# can score it in a browser, and it also carries my nine scores and my reasons
# so it can show them side by side afterwards. That makes three copies of the
# output and a second copy of the score row. Check 5 guards the pack. Nothing
# guarded the page, and a page that scores something this repository never
# published, or shows scores that no longer match the record, would be worse
# than having no page.
#
# The page is generated by scripts/build_page.py, which slices the output
# straight out of the record rather than having anyone retype it. This check is
# what catches the page being edited by hand afterwards. The script sits
# outside docs/ because GitHub Pages publishes everything in there, and a build
# script is not something a reader came for.
PAGE = "docs/index.html"
BUILDER = "scripts/build_page.py"
if os.path.exists(PAGE) and os.path.exists(RECORD):
    page = read(PAGE)
    if not os.path.exists(BUILDER):
        fail("page-unbuildable", PAGE,
             f"{BUILDER} is missing, so the page cannot be regenerated from "
             "the record")
    marker = '<pre class="source" id="model-output">'
    if marker not in page or "</pre>" not in page.split(marker, 1)[1]:
        fail("page-shape", PAGE,
             "cannot locate the reproduced output block, so it cannot be "
             "compared with the record")
    else:
        page_out = " ".join(
            page.split(marker, 1)[1].split("</pre>", 1)[0].split())
        record_out = slice_output(read(RECORD), "## Two Distinct Readings",
                                  "## Score")
        # The page shows the output's own first heading, which slice_output
        # drops as the marker it split on, so put it back before comparing.
        if record_out is not None:
            record_out = " ".join(
                ("## Two Distinct Readings " + record_out).split())
        if record_out is None:
            fail("page-shape", RECORD,
                 "cannot locate the output in the record")
        elif page_out.rstrip("- ") != record_out.rstrip("- "):
            fail("page-output-drift", PAGE,
                 f"the reproduced output no longer matches {RECORD}, so the "
                 "page would be scoring something unpublished")
    # And the scores the page reveals must be the scores the record published.
    page_scores = [int(n) for n in re.findall(r"^\s*mine: (\d+),", page, re.M)]
    row = SCORE_ROW.search(read(RECORD))
    if row:
        record_scores = [int(c.strip()) for c in row.group(1).split("|")
                         if c.strip()]
        if page_scores and page_scores != record_scores:
            fail("page-score-drift", PAGE,
                 f"the page reveals {page_scores} but {RECORD} published "
                 f"{record_scores}")
        if page_scores and f"{sum(page_scores)} / 45" not in read(RECORD):
            fail("page-score-drift", PAGE,
                 f"the page's scores add to {sum(page_scores)}, which is not "
                 f"the total {RECORD} states")


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
