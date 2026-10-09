# Results

This page lists every published run of Sales Proof Bench. Each gives the same fictional sales task to a different model or setup, and I scored each one against a fixed rubric. It isn't a leaderboard. A score below says nothing about which model is better overall, only how it handled this one task. New here? The [root README](../README.md) explains the method and the rules behind these scores.

## Published

None of the 21 runs below triggered an automatic failure. Every score is the rubric result alone. "Consumer app" means a hidden system prompt, account history or product feature may have shaped the output. "Claude Code" and "isolated agent" mean the model got only the case file.

**Hartwell Follow Up Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, Claude Code](claude-sonnet-5-hartwell-follow-up-case.md) | 42/45 |
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-hartwell-follow-up-case-second-run.md) | 43/45 |
| [Claude Haiku 4.5, isolated agent](claude-haiku-4-5-hartwell-follow-up-case.md) | 33/45 |
| [ChatGPT, consumer app, version not confirmed](chatgpt-hartwell-follow-up-case.md) | 41/45 |
| [Gemini, consumer app, version not confirmed](gemini-hartwell-follow-up-case.md) | 35/45 |

**Marlow Pre-Call Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, Claude Code](claude-sonnet-5-marlow-pre-call-case.md) | 43/45 |
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-marlow-pre-call-case-second-run.md) | 41/45 |
| [Claude Sonnet 5, consumer app (my account)](claude-sonnet-5-marlow-pre-call-case-consumer-app.md) | 41/45 |
| [ChatGPT, consumer app, version not confirmed](chatgpt-marlow-pre-call-case.md) | 45/45 |
| [Gemini, consumer app, version not confirmed](gemini-marlow-pre-call-case.md) | 36/45 |
| [Claude Haiku 4.5, isolated agent](claude-haiku-4-5-marlow-pre-call-case.md) | 42/45 |

**Osmond Objection Diagnosis Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-osmond-objection-diagnosis-case.md) | 45/45 |
| [Claude Sonnet 5, consumer app (my account)](claude-sonnet-5-osmond-objection-diagnosis-case-consumer-app.md) | 37/45 |
| [ChatGPT 5.6, consumer app, version confirmed](chatgpt-osmond-objection-diagnosis-case.md) | 45/45 |
| [Gemini, consumer app, version not confirmed](gemini-osmond-objection-diagnosis-case.md) | 43/45 |
| [Claude Haiku 4.5, isolated agent](claude-haiku-4-5-osmond-objection-diagnosis-case.md) | 31/45 |

**Elmsworth Business Case Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-elmsworth-business-case-case.md) | 44/45 |
| [Claude Sonnet 5, consumer app (my account)](claude-sonnet-5-elmsworth-business-case-case-consumer-app.md) | 44/45 |
| [ChatGPT, consumer app, version not confirmed](chatgpt-elmsworth-business-case-case.md) | 43/45 |
| [Gemini, consumer app, version not confirmed](gemini-elmsworth-business-case-case.md) | 45/45 |
| [Claude Haiku 4.5, isolated agent](claude-haiku-4-5-elmsworth-business-case-case.md) | 40/45 |

## A Setup Comparison, Scored by Script

One test here isn't a model comparison and isn't scored on the rubric: [Process Document or None](../comparisons/process-documentation-setup-comparison.md). It gives one model three versions of the instructions for a fictional refund queue. The 15 runs aren't part of the 21 above.

## What the Results Show

Each model now has at least one run on all four cases. Sonnet 5 has nine runs, ChatGPT and Gemini four each, and Haiku 4.5 four, one per case. Sonnet 5's extra runs are second attempts and consumer-app versions, not extra cases. Two of them repeat a case, to test how far a single score can be trusted.

That changes what the Haiku numbers mean. After one run it looked like the weakest model here. After four it's one of the two least consistent: 31, 33, 40 and 42. That's a spread of 11 points, against 10 for Gemini (35, 36, 43 and 45), 8 for Sonnet 5 across its nine runs (37 to 45) and 4 for ChatGPT. Take only Sonnet 5's first run on each case (42, 43, 45 and 44) and its spread is 3. The one point between Haiku and Gemini is inside the noise this page already allows for. Haiku's best score beats several Gemini and Sonnet runs, and its worst is the lowest in the repo. An average would hide both.

Each setup got the same prompt, the same source notes and the same rubric, with the same reviewer, once. One reviewer is a limit in itself. Nothing here has had an [inter-rater reliability check](../methods/fair-comparison.md#what-one-reviewer-cannot-tell-you), so a gap of one or two points between runs is noise, not a result. Two pairs of repeat runs on this page back up that threshold. Sonnet 5 scored 43 and 41 on Marlow, and 42 and 43 on Hartwell. Both pairs land within two points.

The totals are the less interesting half. On Marlow the second run scored higher on usefulness and lower on hallucination, and the two partly cancelled out. Someone comparing only totals would miss that one run made up a sender's name and the other didn't. On Hartwell a single area moved. A steady total can hide an unsteady judgement, which is why each record shows all nine areas and not just a number.

A consumer-app result is always "this model plus whatever that account happened to be carrying," not a clean read on the model alone. Most results had a real, specific flaw, and the detail is in each record's "What it got wrong." Five records say I found none in the content.

### Hartwell Follow Up

**Bottom line:** Haiku 4.5 and Gemini each added something the source notes never said.

- **Haiku 4.5** made up a timeline. It wrote "this should take 2-3 weeks," stated as fact, with nothing to base it on.
- **Gemini** turned a stated worry into a rating. It logged "Account Risk / Sensitivity: High" from a comment that was only caution.
- **ChatGPT and Sonnet 5** avoided both mistakes and scored highest. But ChatGPT's email described its own rule-following ("I have not assumed...") instead of reading like something a person would send.

### Marlow Pre-Call

**Bottom line:** every run caught the main trap, treating a secondhand comment as a confirmed priority. The differences show up elsewhere.

- **ChatGPT** scored 45/45, and I found no flaw.
- **Gemini** contradicted itself. It named "data bottlenecks" as the fix just after its own notes said that link wasn't confirmed.
- **Two of the four Claude runs** signed the outreach message with a name the case never gave them: the isolated agent session and the consumer app. The Claude Code run didn't. Nor did Haiku 4.5, which wrote a `[Your name]` placeholder and also refused to make up a name for the trade publication the case leaves unnamed. That restraint matters, because making up plausible details is this model's weakness on two other cases here. The same behaviour turned up in two different setups, so I'm tracking it as a pattern.

### Osmond Objection Diagnosis

**Bottom line:** all five runs saw that the objection could mean more than one thing. They differ in how well they showed it, and in what two of them made up.

- **The agentic Sonnet 5 run and ChatGPT** both scored 45/45, and both met the case's minimum of two distinct readings. Sonnet 5 gave three, ChatGPT two.
- **Gemini** scored well, but squeezed a separate reading into a passing note instead of working it through.
- **The Claude consumer-app run** made the most serious mistake in this repo so far. It made up a price, "£900," that appears nowhere in the source.
- **Haiku 4.5 scored 31/45, the lowest in the repo**, and not for missing structure. Its two readings are distinct and its list of what not to assume is complete. But it got wrong what the case says David asked no questions about. Then it added a "sticker shock" moment and a question about cost that the notes never record, plus a "Q3" and a "two weeks" the case never mentions. Its clarifying question also suggests a phased rollout. That's the kind of rebuttal the case warns against, not a neutral question.

### Elmsworth Business Case

**Bottom line:** the cleanest case in this repo. Nobody made up an ROI figure.

- **Both Sonnet 5 runs** scored 44/45. One lost a point for text leaking in from its session, the other for a spelling mistake.
- **Gemini** scored 45/45.
- **Haiku 4.5** scored 40/45. It had a strong evidence gap section: six named metrics, each with what to collect and why. It lost marks for leaving out the assumptions section the case asked for, and for contradicting its own plan. Phase three sits at week seven, but the closing script promises the VP numbers in five.
- **ChatGPT** did the most thorough evidence gap analysis of any run here, but scored 43/45. Someone asking for "something showing the impact so I can get this approved" can't use an 11-section answer, with a list of 17 banned claims, in one sitting.

### What Appears Across Cases

- Three of the six consumer-app runs on Marlow and Osmond produced a made-up detail: the Marlow signature, Gemini's Marlow contradiction and the Osmond price. The Marlow signature also turned up once outside a consumer app, so it isn't only a consumer-app problem. But the cluster is worth watching. The sample is small, so this isn't a meaningful rate.
- **Haiku 4.5 failed the same way on two cases, and the failure isn't vagueness.** On Hartwell it wrote "This should take 2-3 weeks" with nothing behind it. On Osmond it made up a question about cost, a quarter and a fortnight. Each reads as if it came from the source, not as a guess, which makes it harder to catch than an honest gap. On the two cases where it scored well the made-up detail was smaller: a line on Elmsworth saying no formal survey was held, and a Marlow claim that it sees teams struggle with slow supplier intake. So how much it makes up varies, and four runs can't tell you what sets it off.
- Elmsworth's clean sweep on ROI figures matches the way its prompt lists what not to claim (no percentage, no dollar figure, no hours, no satisfaction claim) instead of leaving gaps to fill.
- **Most of a wider catalogue comes from this page.** [Which AI Mistakes Actually Get Through](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/main/guides/which-ai-mistakes-get-through.md) sorts every flaw found across this bench and two related repos by whether a careful reader would have caught it. Seven of the 11 it lists as hard to catch come from this page, including the Marlow signature, the Osmond price and both of Haiku's made-up details. Four of the five it lists as obvious come from here too. That's the more flattering half, and the less useful one.

## Adding a Further Result

Each new result should include:

1. the full fictional input;
2. the exact task;
3. the model and setup;
4. the raw output;
5. the completed rubric;
6. a short, honest verdict; and
7. a clear statement of what the test cannot prove.

A screenshot, a winner badge or a single number isn't enough.
