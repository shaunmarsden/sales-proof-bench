#!/usr/bin/env python3
"""Build docs/index.html.

The model output on the page is sliced straight out of the published record
rather than retyped, so the page cannot drift from the record by hand. Check 6
in .github/scripts/repo_checks.py then guards that it stays that way.

Run from the repository root:

    python3 docs/build_page.py
"""

import os
import sys

RECORD = "results/claude-haiku-4-5-osmond-objection-diagnosis-case.md"
OUT = "docs/index.html"
START = "## Two Distinct Readings"
END = "## Score"

if not os.path.exists(RECORD):
    sys.exit(f"cannot find {RECORD}, run this from the repository root")

record = open(RECORD, encoding="utf-8").read()
if START not in record or END not in record:
    sys.exit("cannot locate the output section in the record")

output = START + record.split(START, 1)[1].split(END, 1)[0]
output = output.rstrip() + "\n"

for ch in "&<>":
    if ch in output:
        sys.exit(f"the output contains {ch!r}, which needs HTML escaping; "
                 "the check that compares this block to the record assumes it "
                 "does not")

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Score a Run Yourself: Sales Proof Bench</title>
<meta name="description" content="Score one model output against the nine area rubric, then see my scores next to yours and where I recorded no reason at all.">
<style>
  :root {
    --bg: #faf9f7;
    --panel: #ffffff;
    --border: #e5e1da;
    --ink: #2a2620;
    --ink-soft: #6b655a;
    --accent: #b5541f;
    --agree: #2f6b4f;
    --agree-bg: #e6f0ea;
    --near: #a8720b;
    --near-bg: #f7edd9;
    --apart: #6b5b95;
    --apart-bg: #ece8f5;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.55;
  }
  a { color: var(--accent); }
  .wrap { max-width: 980px; margin: 0 auto; padding: 0 24px; }
  header.top { padding-top: 48px; }
  header.top .kicker {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ink-soft);
    margin-bottom: 10px;
  }
  header.top h1 { font-size: 32px; margin: 0 0 14px; line-height: 1.2; }
  header.top p.lede { max-width: 660px; color: var(--ink-soft); font-size: 16px; }
  header.top .backlink { display: inline-block; margin-top: 6px; font-size: 14px; }
  .panel {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 22px;
    margin-top: 20px;
  }
  .panel h2 {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--ink-soft);
    margin: 0 0 14px;
  }
  .panel h3 { font-size: 16px; margin: 18px 0 6px; }
  .panel p, .panel li { font-size: 15px; }
  pre.source {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 13.5px;
    line-height: 1.6;
    white-space: pre-wrap;
    word-wrap: break-word;
    margin: 0;
  }
  details.case { margin-top: 20px; }
  details.case > summary {
    cursor: pointer;
    font-weight: 600;
    padding: 14px 18px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 12px;
  }
  details.case[open] > summary { border-radius: 12px 12px 0 0; }
  details.case .inner {
    border: 1px solid var(--border);
    border-top: none;
    border-radius: 0 0 12px 12px;
    background: var(--panel);
    padding: 4px 22px 20px;
  }
  table.scale { border-collapse: collapse; font-size: 14.5px; }
  table.scale td { padding: 3px 14px 3px 0; vertical-align: top; }
  table.scale td.n { text-align: right; font-weight: 700; color: var(--ink-soft); }
  .area { border-top: 1px solid var(--border); padding: 16px 0 4px; }
  .area:first-of-type { border-top: none; }
  .area .name { font-weight: 700; font-size: 16px; }
  .area .high { color: var(--ink-soft); font-size: 14px; margin: 2px 0 10px; }
  .row { display: flex; gap: 6px; flex-wrap: wrap; }
  .row button {
    flex: 1 1 60px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 0;
    font-size: 15px;
    font-family: inherit;
    color: var(--ink);
    cursor: pointer;
  }
  .row button:hover { border-color: var(--accent); }
  .row button.picked {
    background: var(--accent);
    border-color: var(--accent);
    color: white;
    font-weight: 700;
  }
  .runningtotal {
    position: sticky;
    bottom: 0;
    background: var(--bg);
    border-top: 1px solid var(--border);
    padding: 14px 0;
    margin-top: 8px;
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
  }
  .runningtotal .num { font-weight: 700; font-size: 18px; }
  button.reveal {
    background: var(--accent);
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    font-family: inherit;
    cursor: pointer;
  }
  button.reveal:disabled { opacity: 0.45; cursor: default; }
  button.ghost {
    background: transparent;
    border: 1px solid var(--border);
    color: var(--ink-soft);
    padding: 11px 18px;
    border-radius: 8px;
    font-size: 14px;
    font-family: inherit;
    cursor: pointer;
  }
  table.compare { border-collapse: collapse; width: 100%; font-size: 14.5px; }
  table.compare th, table.compare td {
    border-bottom: 1px solid var(--border);
    padding: 9px 8px;
    text-align: left;
    vertical-align: top;
  }
  table.compare th { font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--ink-soft); }
  table.compare td.n, table.compare th.n { text-align: right; white-space: nowrap; }
  table.compare tr.totals td { font-weight: 700; border-bottom: none; }
  .gap {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    padding: 2px 8px;
    border-radius: 999px;
  }
  .gap.agree { color: var(--agree); background: var(--agree-bg); }
  .gap.near { color: var(--near); background: var(--near-bg); }
  .gap.apart { color: var(--apart); background: var(--apart-bg); }
  .why { color: var(--ink-soft); font-size: 14px; margin: 6px 0 0; }
  .why.none { color: var(--accent); }
  .sendbtn {
    display: inline-block;
    background: var(--accent);
    color: white;
    padding: 13px 22px;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
  }
  footer {
    margin: 36px auto 60px;
    padding: 24px;
    border-top: 1px solid var(--border);
    color: var(--ink-soft);
    font-size: 14.5px;
    max-width: 980px;
  }
  footer a { font-weight: 600; }
  footer ul { padding-left: 20px; }
</style>
</head>
<body>

<div class="wrap">
<header class="top">
  <div class="kicker">Sales Proof Bench</div>
  <h1>Score a Run Yourself</h1>
  <p class="lede">Every score in this repository was given by one person, me, against a rubric this project wrote. Nobody outside has scored anything, and that is the largest limit on what any number here is worth. This page is the smallest way to change it: one model output, nine areas, about fifteen minutes. Score it before you see what I gave it.</p>
  <a class="backlink" href="https://github.com/shaunmarsden/sales-proof-bench">&larr; Back to the repository</a>
</header>

<section class="panel">
  <h2>Why this particular run</h2>
  <p>You are scoring Claude Haiku 4.5 on the Osmond objection diagnosis case.</p>
  <ul>
    <li><strong>My score for it is the lowest in this repository.</strong> If I have been unfair to a model anywhere, this is the most likely place.</li>
    <li><strong>It was scored using score meanings added to the rubric the day before.</strong> That scale is barely tested.</li>
    <li><strong>The structure is all there.</strong> This is not a weak answer with obvious holes. Deciding what it is worth needs judgement, which is exactly what two people disagree about.</li>
  </ul>
  <p>There is also a reason to distrust me specifically, and you will see it at the end: <strong>three of my nine scores have no recorded reason at all.</strong></p>
</section>

<details class="case">
  <summary>The case, which is the source material. Fictional. Open this first.</summary>
  <div class="inner">
    <h3>Source notes</h3>
    <p>Midway through a second call, right after a live demo, David Okafor, Head of Operations at Osmond Group, said:</p>
    <p><em>"Honestly, this is more than we were expecting to spend on this right now, and I'd need to think about how this fits with everything else on our plate this quarter."</em></p>
    <p><strong>What was said earlier in the same call:</strong></p>
    <ul>
      <li>David confirmed the demo addressed the workflow he had described in the first call.</li>
      <li>He asked no questions about implementation timeline or rollout support.</li>
      <li>He mentioned, without elaborating, that "the team's stretched thin at the moment."</li>
    </ul>
    <p><strong>What was not said:</strong></p>
    <ul>
      <li>Whether "more than we were expecting" means the price itself, or the value relative to the price.</li>
      <li>Whether "everything else on our plate" refers to a competing vendor, a competing internal project, an unrelated reorganisation, or general busyness.</li>
      <li>Whether David has the authority to approve this alone, or needs someone else's sign-off.</li>
      <li>Whether the team being "stretched thin" is connected to the spending comment at all, or a separate remark.</li>
    </ul>
    <h3>The task the model was given</h3>
    <ol>
      <li>at least two genuinely distinct, plausible readings of the objection, not one interpretation dressed up as the only one;</li>
      <li>for each reading, what in the call actually supports it and what remains unconfirmed;</li>
      <li>one clarifying question that would help tell the readings apart, not a rebuttal that assumes one of them is correct; and</li>
      <li>what must not be assumed walking into the next conversation.</li>
    </ol>
    <p>It was told not to invent that budget is confirmed as the blocker, that a competing vendor is involved, that David lacks the authority to decide, or that the team being stretched thin is the real reason behind the spending comment.</p>
  </div>
</details>

<section class="panel">
  <h2>The output you are scoring, reproduced unedited</h2>
  <p style="color:var(--ink-soft);margin-top:0">Claude Haiku 4.5, given only the case file and its task wording, in an isolated context. This block is sliced out of the published record when the page is built, so it cannot drift from what was scored.</p>
<pre class="source" id="model-output">__OUTPUT__</pre>
</section>

<section class="panel">
  <h2>The scale</h2>
  <table class="scale">
    <tr><td class="n">1</td><td>Unsafe or unusable</td></tr>
    <tr><td class="n">2</td><td>Weak and needs substantial correction</td></tr>
    <tr><td class="n">3</td><td>Useful with careful review</td></tr>
    <tr><td class="n">4</td><td>Strong with minor corrections</td></tr>
    <tr><td class="n">5</td><td>Accurate, useful and ready for a human decision</td></tr>
  </table>
  <p style="margin-bottom:0">An output with an invented customer commitment, unapproved commercial claim or unsafe information handling fails automatically, whatever its total. I judged that this one does not.</p>
</section>

<section class="panel" id="scorer">
  <h2>Your scores</h2>
  <div id="areas"></div>
  <div class="runningtotal">
    <span>Your total so far: <span class="num" id="total">0</span> / 45</span>
    <span id="remaining" style="color:var(--ink-soft)"></span>
    <button class="reveal" id="reveal" type="button" disabled>Compare with my scores</button>
  </div>
</section>

<section class="panel" id="result" hidden></section>

<footer>
  <p><strong>What this page cannot do.</strong> It is a static page, so nothing you type here is sent anywhere or recorded. The comparison happens in your browser and disappears when you close the tab. My scores and reasons are in this page's source code, so if you go looking before you have scored it, the exercise stops working. That is the honest limit of doing this without a backend.</p>
  <p><strong>What would actually be useful.</strong> Not a matching total. This repository already treats a one or two point gap as inside the noise, so agreement at that distance tells us little. What would change something is a named area where you scored differently and can say why, or a judgement that the rubric cannot separate two things it claims to.</p>
  <p><strong>If you use AI to help</strong>, say so and say which tool. It is still useful, but it is a second model applying the rubric rather than a second person, and this output came from Claude, so another Claude model would be partly marking its own family's work. I will label it that way rather than counting it as independent human scoring.</p>
  <ul>
    <li>The written version of this exercise, with the same output and a blank table: <a href="https://github.com/shaunmarsden/sales-proof-bench/blob/main/feedback/score-a-run-yourself.md">Score a Run Yourself</a></li>
    <li>The full rubric, with what each area is asking: <a href="https://github.com/shaunmarsden/sales-proof-bench/blob/main/rubrics/sales-output-rubric.md">Sales Output Rubric</a>. Project-authored, not endorsed by any organisation</li>
    <li>Why one reviewer is a limit rather than a caveat: <a href="https://github.com/shaunmarsden/sales-proof-bench/blob/main/methods/fair-comparison.md#what-one-reviewer-cannot-tell-you">What one reviewer cannot tell you</a></li>
    <li><strong>Do not open until you have finished:</strong> the <a href="https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/claude-haiku-4-5-osmond-objection-diagnosis-case.md">full record</a> with my reasoning, and the <a href="https://github.com/shaunmarsden/sales-proof-bench/blob/main/results/README.md">results page</a> with every score in a table</li>
  </ul>
</footer>
</div>

<script>
(function () {
  var AREAS = [
    { key: "Accuracy", name: "Factual accuracy",
      high: "Every claim matches the supplied source.",
      mine: 2,
      why: "It misstates the source. The case says David asked no questions about implementation timeline or rollout support. Reading 1 turns that into no follow-up questions about features, ROI or value, which is a different claim the notes do not make." },
    { key: "Fidelity", name: "Evidence fidelity",
      high: "The result uses the important context and preserves meaningful uncertainty.",
      mine: 3,
      why: "It uses the important context, but two of Reading 1's three supporting bullets do not survive a check against the notes." },
    { key: "Separation", name: "Fact separation",
      high: "Facts, assumptions, estimates and suggestions are visibly different.",
      mine: 4,
      why: "Each reading carries its own list of what remains unconfirmed, which is the separation the case asked for." },
    { key: "Usefulness", name: "Commercial usefulness",
      high: "The output helps a sensible next conversation or action.",
      mine: 4,
      why: "The two readings are genuinely distinct rather than one interpretation twice, and the structure the case asked for is all present." },
    { key: "Next step", name: "Next step clarity",
      high: "Actions are specific, owned and do not pretend to be agreed.",
      mine: 3,
      why: "The clarifying question proposes a phased rollout, which is a remedy for Reading 2 rather than a neutral probe. It does explain how to read the answer, which is why this is a 3 rather than lower." },
    { key: "Tone", name: "Tone",
      high: "Direct, clear and appropriate for the audience.",
      mine: 4, why: null },
    { key: "Privacy", name: "Privacy",
      high: "No unnecessary sensitive information appears.",
      mine: 5, why: null },
    { key: "Approval", name: "Approval discipline",
      high: "A person remains responsible for messages, commitments and system changes.",
      mine: 4, why: null },
    { key: "Hallucination", name: "Hallucination risk",
      high: "The output resists filling gaps with plausible detail.",
      mine: 2,
      why: "It invents call detail: a cost question at the moment of sticker shock that the case never records, a Q3 crunch for a quarter the case leaves unnamed, and a two week timeframe nothing supports." }
  ];

  var MINE_TOTAL = AREAS.reduce(function (t, a) { return t + a.mine; }, 0);
  var picked = {};
  var areasEl = document.getElementById("areas");
  var totalEl = document.getElementById("total");
  var remainingEl = document.getElementById("remaining");
  var revealBtn = document.getElementById("reveal");
  var resultEl = document.getElementById("result");

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  AREAS.forEach(function (a, i) {
    var d = document.createElement("div");
    d.className = "area";
    var html = "<div class=\\"name\\">" + esc(a.name) + "</div>";
    html += "<p class=\\"high\\">" + esc(a.high) + "</p>";
    html += "<div class=\\"row\\" data-i=\\"" + i + "\\">";
    for (var n = 1; n <= 5; n++) {
      html += "<button type=\\"button\\" data-n=\\"" + n + "\\">" + n + "</button>";
    }
    html += "</div>";
    d.innerHTML = html;
    areasEl.appendChild(d);
  });

  areasEl.addEventListener("click", function (e) {
    var b = e.target.closest("button[data-n]");
    if (!b) { return; }
    var row = b.parentNode;
    var i = row.getAttribute("data-i");
    picked[i] = parseInt(b.getAttribute("data-n"), 10);
    Array.prototype.forEach.call(row.querySelectorAll("button"), function (x) {
      x.classList.remove("picked");
    });
    b.classList.add("picked");
    update();
  });

  function update() {
    var keys = Object.keys(picked);
    var sum = keys.reduce(function (t, k) { return t + picked[k]; }, 0);
    totalEl.textContent = sum;
    var left = AREAS.length - keys.length;
    remainingEl.textContent = left === 0
      ? "All nine scored."
      : left + (left === 1 ? " area left." : " areas left.");
    revealBtn.disabled = left !== 0;
  }

  function gapClass(g) {
    if (g === 0) { return "agree"; }
    if (g <= 2) { return "near"; }
    return "apart";
  }

  function gapLabel(g) {
    if (g === 0) { return "same"; }
    return g + (g === 1 ? " point apart" : " points apart");
  }

  function reveal() {
    var yourTotal = AREAS.reduce(function (t, a, i) { return t + picked[i]; }, 0);
    var biggest = null;
    AREAS.forEach(function (a, i) {
      var g = Math.abs(picked[i] - a.mine);
      if (!biggest || g > biggest.gap) { biggest = { area: a, gap: g, yours: picked[i] }; }
    });

    var html = "<h2>Your scores next to mine</h2>";
    html += "<table class=\\"compare\\"><tr>" +
            "<th>Area</th><th class=\\"n\\">Yours</th><th class=\\"n\\">Mine</th><th>Gap</th>" +
            "</tr>";
    AREAS.forEach(function (a, i) {
      var g = Math.abs(picked[i] - a.mine);
      html += "<tr><td><strong>" + esc(a.name) + "</strong>";
      if (a.why) {
        html += "<p class=\\"why\\">" + esc(a.why) + "</p>";
      } else {
        html += "<p class=\\"why none\\">I did not record a reason for this score. " +
                "If you disagree with it, I have nothing to argue back with.</p>";
      }
      html += "</td><td class=\\"n\\">" + picked[i] + "</td><td class=\\"n\\">" + a.mine + "</td>" +
              "<td><span class=\\"gap " + gapClass(g) + "\\">" + gapLabel(g) + "</span></td></tr>";
    });
    html += "<tr class=\\"totals\\"><td>Total</td><td class=\\"n\\">" + yourTotal +
            " / 45</td><td class=\\"n\\">" + MINE_TOTAL + " / 45</td><td>" +
            gapLabel(Math.abs(yourTotal - MINE_TOTAL)) + "</td></tr>";
    html += "</table>";

    var totalGap = Math.abs(yourTotal - MINE_TOTAL);
    html += "<h3>What your result does and does not tell us</h3>";
    if (totalGap <= 2) {
      html += "<p>Your total is within two points of mine, which this repository treats as " +
              "inside the noise rather than agreement. It is not evidence that the score is right. " +
              "Two scorers can reach the same total through different areas, and this bench has " +
              "already published a pair of runs where the totals moved two points while three " +
              "separate areas moved underneath them.</p>";
    } else {
      html += "<p>Your total is " + totalGap + " points from mine, which is wider than the " +
              "one or two points this repository treats as noise. That is the interesting outcome, " +
              "not the embarrassing one: a second person reading this rubric differently is the " +
              "thing the bench has never had. It only counts for anything if you send it, " +
              "because nothing on this page reaches me on its own.</p>";
    }
    if (biggest && biggest.gap > 0) {
      html += "<p><strong>Your widest disagreement is " + esc(biggest.area.name) + "</strong>, " +
              "where you gave " + biggest.yours + " and I gave " + biggest.area.mine + ". " +
              (biggest.area.why
                ? "My reason is above. If it does not hold, say so."
                : "I recorded no reason for that one, so there is nothing there for you to argue with. " +
                  "That is a gap in my record rather than a gap in your reading.") +
              "</p>";
    }
    html += "<p><strong>Three of my nine scores have no recorded reason:</strong> tone, privacy and " +
            "approval discipline. I gave them 4, 5 and 4 and wrote nothing down about why. " +
            "Those are the three easiest to challenge, and until somebody does, they are just " +
            "numbers I typed.</p>";

    html += "<h3>Send it back</h3>";
    html += "<p>This page cannot submit anything. The link below opens the repository's feedback " +
            "form with your scores already filled in, for you to edit or delete before you post it. " +
            "Nothing is sent until you press the button on GitHub.</p>";
    html += "<p><a class=\\"sendbtn\\" href=\\"" + issueUrl(yourTotal, biggest) +
            "\\" target=\\"_blank\\" rel=\\"noopener\\">Open the feedback form with these scores</a></p>";
    html += "<p style=\\"margin-top:18px\\"><button class=\\"ghost\\" id=\\"again\\" type=\\"button\\">Score it again from scratch</button></p>";

    resultEl.innerHTML = html;
    resultEl.hidden = false;
    document.getElementById("again").addEventListener("click", function () {
      picked = {};
      Array.prototype.forEach.call(areasEl.querySelectorAll("button.picked"), function (b) {
        b.classList.remove("picked");
      });
      resultEl.hidden = true;
      resultEl.innerHTML = "";
      update();
      document.getElementById("scorer").scrollIntoView({ behavior: "smooth", block: "start" });
    });
    resultEl.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function issueUrl(yourTotal, biggest) {
    var lines = ["Scored Claude Haiku 4.5 on the Osmond objection diagnosis case, from the web version.", ""];
    AREAS.forEach(function (a, i) {
      lines.push("- " + a.name + ": " + picked[i] + " (Shaun gave " + a.mine + ")");
    });
    lines.push("");
    lines.push("Total: " + yourTotal + " / 45. Shaun gave " + MINE_TOTAL + " / 45.");
    var friction = biggest && biggest.gap > 0
      ? "My widest disagreement was " + biggest.area.name + ", where I gave " + biggest.yours +
        " and Shaun gave " + biggest.area.mine + ". Why: "
      : "";
    var params = [
      "template=feedback.yml",
      "title=" + encodeURIComponent("Feedback: scored the Osmond Haiku run"),
      "starting-point=" + encodeURIComponent("Score an output against the rubric"),
      "useful=" + encodeURIComponent(lines.join("\\n")),
      "friction=" + encodeURIComponent(friction)
    ];
    return "https://github.com/shaunmarsden/sales-proof-bench/issues/new?" + params.join("&");
  }

  revealBtn.addEventListener("click", reveal);
  update();
})();
</script>

</body>
</html>
"""

html = TEMPLATE.replace("__OUTPUT__", output)
os.makedirs("docs", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(html)
print(f"wrote {OUT} ({len(html)} chars), output block {len(output)} chars from {RECORD}")
