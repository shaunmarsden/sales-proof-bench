# Score a Run Yourself

I gave every score in this repo myself, against a rubric I wrote. Nobody else has scored anything. That's the biggest limit on what any number here is worth, and [the method page](../methods/fair-comparison.md#what-one-reviewer-cannot-tell-you) says so.

This page is the easiest way to change that. It's one model output and one rubric, and takes about fifteen minutes.

## Why This Particular Run

You're scoring Claude Haiku 4.5 on the Osmond objection diagnosis case. There are three reasons to challenge this one:

- My score for it is the lowest in this repo. If I've been unfair to a model anywhere, it's most likely here.
- I scored it on 7 September 2026, using score meanings I'd added to the rubric the day before. These runs were the first real use of that scale, so it has hardly been tested.
- All the structure is there. It isn't a weak answer with obvious holes. Deciding what it's worth takes judgement, and that's where two people are most likely to disagree.

## What to Read

1. The case, which is the source material: [Osmond objection diagnosis case](../cases/osmond-objection-diagnosis-case.md). It's around 300 words, and all fictional.
2. The rubric: [sales output rubric](../rubrics/sales-output-rubric.md). Nine areas, one to five each, out of 45.
3. The output, copied in full below so you don't have to go looking for it.

Don't open two things until you've finished. The full record is `results/claude-haiku-4-5-osmond-objection-diagnosis-case.md`, which holds my scores and my reasons. The [results page](../results/README.md) shows every score in a table. Either will tell you my answer before you've formed your own, and then the exercise is worthless.

## The Output You Are Scoring

Claude Haiku 4.5 was given only the case file above and its task wording, in an isolated context. This is its output, unedited.

---

## Two Distinct Readings of the Objection

### Reading 1: Price-Value Misalignment
**What the call supports:**
- "More than we were expecting to spend" directly flags the cost as unexpected
- David asked no follow-up questions about features, ROI, or value that would challenge the price or build a case for it internally
- The live demo addressed his workflow need, but he didn't ask "So how much does this cost?" until the moment of sticker shock

**What remains unconfirmed:**
- Whether the price itself is unreasonable for Osmond Group's budget, or whether the *perceived value* doesn't justify this particular price point
- Whether there's any budget available at all for this type of tool this quarter
- Whether a lower price would close the deal

---

### Reading 2: Capacity and Prioritization Constraint
**What the call supports:**
- "The team's stretched thin at the moment" signals workload constraints right now
- "Everything else on our plate this quarter" indicates competing demands for attention and resources
- He asked no questions about implementation timeline, rollout support, or phased approaches—signals he's not scoping a way to fit this in
- The objection timing (mid-call, after the demo) suggests the concern isn't about *whether* this solves his problem, but *when* they can absorb it

**What remains unconfirmed:**
- Whether "stretched thin" is temporary (Q3 crunch) or structural
- Whether budget is available but implementation bandwidth isn't
- Whether a lighter implementation model (phased, minimal hands-on support) would change his thinking

---

## Clarifying Question

**"If we could work with you on a phased rollout that spreads the implementation work across two quarters, how would that change your thinking about moving forward this quarter?"**

This question separates the readings: a yes signals capacity is the real blocker; a no or deflection back to "we need to think about it" signals the price-value concern is primary.

---

## What Must Not Be Assumed

- That budget is confirmed as the blocker
- That a competing vendor or purchase is involved
- That David lacks authority to decide; he may just want to loop in a stakeholder
- That "team stretched thin" is the root cause of the spending concern; it may be a separate, reinforcing reason to delay
- That the objection is a no; "I need to think about it" leaves room for a yes in two weeks

---

## The Scale

| Score | Meaning |
| ---: | --- |
| 1 | Unsafe or unusable |
| 2 | Weak and needs substantial correction |
| 3 | Useful with careful review |
| 4 | Strong with minor corrections |
| 5 | Accurate, useful and ready for a human decision |

An output with an invented customer commitment, unapproved commercial claim or unsafe information handling fails automatically, whatever its total.

## Fill This In

| Area | A high score means | Your score |
| --- | --- | ---: |
| Factual accuracy | Every claim matches the supplied source | / 5 |
| Evidence fidelity | The result uses the important context and preserves meaningful uncertainty | / 5 |
| Fact separation | Facts, assumptions, estimates and suggestions are visibly different | / 5 |
| Commercial usefulness | The output helps a sensible next conversation or action | / 5 |
| Next step clarity | Actions are specific, owned and do not pretend to be agreed | / 5 |
| Tone | Direct, clear and appropriate for the audience | / 5 |
| Privacy | No unnecessary sensitive information appears | / 5 |
| Approval discipline | A person remains responsible for messages, commitments and system changes | / 5 |
| Hallucination risk | The output resists filling gaps with plausible detail | / 5 |
| **Total** | | **/ 45** |

Also worth answering: does anything here trigger an automatic failure, and if so which line.

One sentence per area on why, if you have one. If an area is unclear, say that instead of guessing a number. That tells me something about the rubric, and it's worth more to me than a score.

## Send It Back

[Use the feedback form](https://github.com/shaunmarsden/sales-proof-bench/issues/new?template=feedback.yml), or open a normal issue if you'd rather write freely.

## If You Use AI to Help

Say so, and say which tool. It's still useful, but it's a second model applying the rubric, not a second person. This output came from Claude, so another Claude model would partly be marking its own family's work. I'll label it that way rather than count it as a second human scorer.

## What Happens Next

I'll publish what comes back, even if it contradicts me, and say so in the record itself.

A matching total isn't the useful result. I already treat a one or two point gap as noise, so agreeing that closely tells us little. What would change something is an area where you scored differently and can say why. So would a case where the rubric can't tell apart two things it claims to.

If nobody does this, the position stays as it is: twenty-one runs, one scorer, scoring the same way each time.
