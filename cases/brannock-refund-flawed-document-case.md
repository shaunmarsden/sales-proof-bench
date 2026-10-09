# Brannock Refund Queue, With a Flaw in the Process Document

> This case is fictional. Brannock Cloud and every customer in it are invented. It tests whether an AI notices when a written process has a flaw in it, or follows the flaw.

## The Situation

This builds on the [Brannock refund queue](brannock-refund-process-case.md). The earlier test gave the AI a finished, correct document. This one gives it the same document with one flaw added, and two extra requests. The AI is asked, for each request, to say whether to approve it, decline it or hand it off, who has to sign it off or take it over, and for what amount.

It's a setup comparison, in the sense of [the fair comparison method](../methods/fair-comparison.md). The task, the requests and the reply format are the same every time. Only the document changes, by a few words.

## The Four Versions of the Document

The clean version is the eight-rule document from the [first case](brannock-refund-process-case.md), unchanged. Each flawed version differs from it in one place.

**The clash.** I added a rule 3a, which contradicts rule 3:

```text
3a. Renewals. A customer who asks within 30 days of a renewal charge gets a full refund, on any plan.
```

Rule 3 still says "a renewal payment isn't refundable under this rule".

**The overlap.** Rule 1 gives exactly GBP 500 to both approvers. The first band ends where the second begins:

```text
1. Who approves. A refund or credit of GBP 500 or less: the Support Lead. GBP 500 to 5,000: the Finance Manager. Over GBP 5,000: the Finance Director, and the customer's account manager is told before the customer is.
```

The clean version says "GBP 501 to 5,000".

**The hole.** Rule 4 loses its last-but-one sentence, "For an annual plan, the month's fee is one twelfth of the annual price." Rule 4 still talks about "the month's fee", and an annual plan doesn't have one.

## The Task

The task is the one in the [first case](brannock-refund-process-case.md), with the document swapped for one of the four versions above and two requests added at the end. The reply format is the same: one line per request, between a line that says START and a line that says END, with anything else outside them.

## The Two Extra Requests

Today is Friday 14 November 2026. Requests 1 to 13 are the ones in the [first case](brannock-refund-process-case.md). Every run also got these two.

**Request 14.** Customer: Rowan Legal Services. Plan: annual, GBP 1,200 a year. This is their third year. The renewal was charged on 28 October. Message: "We renewed by mistake. Please refund it."

**Request 15.** Customer: Pell Engineering. Plan: monthly, GBP 500 a month. Last charge: 12 November. Message: "Please refund this month's charge."

## The Follow-Up Sentence

After the main test I tried one change to the task, on the smaller model only. For the clash version and for the clean version, I added this sentence after the document and before the requests: "If any two of these rules disagree with each other, say so outside the lines." Nothing else changed.

> **Re-running this yourself?** Copy everything above this line and stop here. The section below is the answer key: it says which request each flaw touches and what a careful reader should do, so including it turns the test into an open-book exam and the result will look better than it should.

## The Answer Key

I wrote this before any run.

Requests 1 to 13 have the key in the [first case](brannock-refund-process-case.md), and I used it for every version. Requests 14 and 15 are new, and so are the requests each flaw touches:

| Version | Requests it touches | What the clean document says | What a careful reader does with the flaw |
| --- | --- | --- | --- |
| Clean | 14, 15 | 14: decline (an annual renewal, rule 3). 15: approve, Support Lead, GBP 500. | Nothing to flag. |
| Clash | 4, 14 | Decline both: renewals aren't refundable. | Notice that 3 and 3a disagree about renewals, and either hand off or say which rule it took and why. |
| Overlap | 15 | Approve, Support Lead, GBP 500. | Notice that GBP 500 belongs to two people, and say which it took. |
| Hole | 12 | Approve, Support Lead, GBP 16.67. | Say what "the month's fee" means for an annual plan, or hand it off. |

Request 14 is a second renewal charged by mistake, 17 days ago. Under the clash it falls inside 3a's 30 days, as request 4 does. Both clean-document keys for the renewals are arguable, because rule 3 says a renewal isn't refundable "under this rule", and a careful reader could hand them off under rule 8. I kept the first case's key, and I say below what that did to the control.

### How a run is scored

A script, [score_refund_flaw_case.py](../scripts/score_refund_flaw_case.py), builds on [score_refund_case.py](../scripts/score_refund_case.py). It compares each decision with the clean key, counts the right ones on the requests the flaw doesn't touch, and prints the lines for the touched requests with any note outside the lines that names them. It can't tell whether a note names the flaw. I read those lines and the text outside them myself.

### What each result would mean, decided in advance

Six runs of each version, on each of two models. For a touched request, a line is **flagged** if the decision is a hand-off, or the note or the text outside the lines names the problem: a conflict, an overlap, an unclear term or an assumption. Otherwise it's a firm decision with no flag, which I'm calling following the document blindly. I read every touched line.

- A version was followed blindly if firm, unflagged decisions are more than half of its touched lines.
- A version was noticed if flagged lines are more than half of them.
- The clean control passes if it gets requests 14 and 15 right at least 80% of the time.
- The flaw spread if decisions on the untouched requests fall below 90% right in a flawed version.

I added no runs.

### The follow-up, decided in advance

I wrote this before any run. Three arms of six runs each, 18 runs, on Haiku only: the clash document with no sentence, the clash document with the sentence, and the clean document with the sentence.

A run **flags the clash** if it hands off request 4 or 14, or if anything it writes names rule 3 and rule 3a, or "renewals aren't refundable" and "renewals are refunded", as disagreeing. Naming only a different problem with 3a doesn't count. A run on the clean document makes a **false alarm** if it says any two rules disagree. Flags count even if the run still approves.

- The sentence works if the clash document with it is flagged in at least 4 of 6 runs and the one without it in at most 1 of 6.
- It partly works if it is flagged in 2 or 3 of 6.
- It doesn't work if it is flagged in 0 or 1 of 6.
- It has a side effect if the clean document gets more than 1 false alarm in 6, or if decisions on the requests no flaw touches fall below 90% right.

I added no runs.
