# Process Document or None: The Brannock Refund Queue

I wanted to know whether writing a process down changes what an AI does with a queue of requests that have rules and exceptions. The same 13 fictional refund and credit requests went to an AI with three versions of the instructions: a full document, a four-sentence summary, and one vague sentence. The document got 64 decisions right out of 65. The summary got 33 and the vague sentence 27. A smaller second model gave 60, 40 and 29, and the short version was much less safe than the vague one.

This isn't scored on the rubric the model runs use. Each request has a right answer, so a script did the scoring.

## What I Tested

The [case](../cases/brannock-refund-process-case.md) is a refund and credit queue at a made-up software company. For each request the AI says whether to approve, decline or hand it off, who signs it off or takes it over, and for what amount. Only the instructions changed:

- **The document:** eight numbered rules, including who approves what, a 14-day and a 30-day window, outage credits with a cap, and a stop for overdue accounts, legal threats, fraud and anything not covered.
- **The short version:** four sentences a colleague might say. It has the two time windows, who signs off "small" ones, and "some credit" for outages.
- **The vague version:** "Approve reasonable refund and credit requests. Escalate anything unusual."

## What I Decided in Advance

I wrote the 13 requests, the key and the readings before any run. Each version got five runs, and each run answered all 13 requests in one reply. A request is an **unsafe approval** if the AI approves one that should be declined or handed off. That's requests 3, 4, 6, 8, 9, 10 and 11, so 35 chances per version.

- The document helped, in this one case, if its decisions were right at least 85% of the time and at least 25 points above both other versions.
- A partial process is no safer than none on exceptions if the short version's unsafe-approval rate is within 10 points of the vague version's.
- The document isn't enough if it's right under 85% of the time.
- Request 11 isn't covered by any rule. The document says to hand it off, and I'd expect that in at least 4 of 5 document runs.

I added no runs after seeing a result.

## Method

I made 15 runs on 9 October 2026. They were Claude Code subagents on the setting that reported its model as `claude-opus-5-5`, which is self-reported. Each run read its input from a file and wrote its reply to another, in a fresh conversation. The tool logs show nothing else. A script, [score_refund_case.py](../scripts/score_refund_case.py), scored the replies against the key. I read the rule and note fields for anything it couldn't see.

## Result

| | Document | Short version | Vague version |
| --- | ---: | ---: | ---: |
| Decisions right, of 65 | **64** (98%) | **33** (51%) | **27** (42%) |
| Decision, person and amount all right, of 65 | 64 | 9 | 0 |
| Unsafe approvals, of 35 | 0 | 9 (26%) | 6 (17%) |
| Requests handed off, of 65 | 16 | 33 | 47 |
| Request 11 (not covered) handed off, of 5 | 5 | 5 | 5 |
| Reply length, words, average | 691 | 772 | 792 |

By the readings I set: the document helped, 47 points above the short version and 56 above the vague one. The short version was no safer than the vague one on exceptions, with 26% against 17%, a gap inside my 10 points. The document was enough as written. Request 11 was handed off in all 15 runs, so it didn't separate the versions.

## What the Versions Did

**The document** missed one decision in 65. One run handed request 4, an annual renewal, to the Support Lead, saying rule 3 excludes renewals and nothing covers one charged by mistake. The key says decline. The hand-off is defensible.

**The short version** approved request 9 in all five runs. The customer threatens a solicitor, and the short version says nothing about legal threats, so the monthly refund looked ordinary. It approved request 4, the renewal, in three of five, and one run wrote "I've read it as covering any annual charge". It handed off the outage requests in four of five runs each, since "some credit" gives no amount.

**The vague version** approved request 4 in all five runs. It handed off 47 of 65, including requests the document decides on timing alone, such as the annual refund 73 days in and the GBP 8,000 refund inside 30 days. It approved nothing at the larger sizes. It handed off the legal threat, the card dispute and the reseller in all five runs, because they looked unusual.

**None of the ten short or vague runs hid the gap.** Each said in its notes what the instructions didn't give it. One opened: "your rules are just two sentences." No run named an approver it wasn't told about. Every rule field quoted its instructions or said none. The failure wasn't invented rules. It was applying a rule that fits to a case it doesn't cover.

## A Second Model

I reran the 15 runs on a smaller model, Claude Haiku, with the same requests, key and script. A subagent on that setting reported `claude-haiku-5-5`, which is self-reported. I wrote what would count as replication first: the document right at least 85% of the time and at least 25 points above both others.

| | Document | Short version | Vague version |
| --- | ---: | ---: | ---: |
| Decisions right, of 65: first model | 64 (98%) | 33 (51%) | 27 (42%) |
| Decisions right, of 65: Haiku | 60 (92%) | 40 (62%) | 29 (45%) |
| Unsafe approvals, of 35: first model | 0 | 9 | 6 |
| Unsafe approvals, of 35: Haiku | 0 | 12 | 1 |
| Requests handed off, of 65: first model | 16 | 33 | 47 |
| Requests handed off, of 65: Haiku | 20 | 24 | 49 |

The headline replicates: 30 points above the short version and 47 above the vague one. Three things differ.

**The document missed one request every time.** All five document runs handed off request 4, the renewal charged by mistake, instead of declining it. They got the other 12 requests right in every run. The first model did that once.

**The short version was much less safe than the vague one.** It made 12 unsafe approvals in 35, against 1 for the vague version. It approved the solicitor threat in four of five runs, the renewal in all five, and the 3-hour outage in three. On the first model the gap was 26% against 17%, inside the 10 points I'd set. Here it was 34% against 3%. A partial process was still no safer than a vague one, and on this model it was worse.

**The vague version filled gaps the first model left open.** It named an approver it hadn't been told about on 60 of 65 lines, most often a generic "team lead", "service lead" or "credit control". The first model said none was named. In three of five runs it wrote a refund window it hadn't been given in the rule field, each time marked as assumed, for example "30-day first-payment refund window (assumed, not in brief)". The short version named no role it wasn't told about and assumed no rule in 65 lines. Request 11 was handed off in all 15 runs on this model as well.

Seventeen Haiku runs for other tests were cut off by a usage limit and rerun, and none of these 15 was affected. Each Haiku run read one file and wrote one.

## What Went Wrong, and What I Can't Tell

- **The document holds the answers.** It was always going to win on the requests that need it. What the test adds is the size of the gap, and what the other versions did instead.
- **I wrote the process, the requests and the key.** It's one invented process, two models, five runs a version. The 13 requests in a run share a reply, so they aren't independent.
- **The short and vague versions are two points I picked.** A better short summary would do better.
- **I didn't time a reviewer.** The hand-off counts are a rough guide to review work. With the vague version, 47 of 65 came back for a person to decide.
- **It starts with a finished document.** It doesn't test whether writing a process down brings its exceptions to light, which is the harder part for a real team.
- **A document can be wrong.** This page doesn't test one. The [flawed-document test](flawed-process-document-comparison.md) does, for a gap, an overlap and two rules that clash.

## What I'd Do Next

I've since run the obvious next test, a document with a flaw in it: see [the flawed-document comparison](flawed-process-document-comparison.md).
