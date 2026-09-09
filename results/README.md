# Results

This page lists every published run of Sales Proof Bench: the same fictional sales task given to different models and setups, scored by one person against a fixed rubric. It is not a leaderboard, and a score below says nothing about which model is generally better, only how it handled this one task. New here? The [root README](../README.md) explains the method and the rules behind these scores.

## Published

None of the 21 runs below triggered an automatic failure. Every score is the rubric result only. "Consumer app" means an unknown system prompt, account history or product feature may have shaped the output; "Claude Code" and "isolated agent" mean only the case file went in.

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

## What the Results Show

Coverage is now even across models on the four cases. Sonnet 5 has nine runs, ChatGPT and Gemini four each, and Haiku 4.5 four, one per case. Sonnet 5's extra runs are second attempts and consumer-app variants rather than additional cases, and two of them are same-case repeats used to test how much a single score can be trusted.

That changes what the Haiku numbers mean. On one run it looked simply like the weakest model here. Across four it is the most variable: 31, 33, 40 and 42, a spread of 11 points against 3 for Sonnet 5 and 4 for ChatGPT. Its best case beats several Gemini and Sonnet runs and its worst is the lowest score in the repository. A single average would hide both.

Same prompt, same source notes, same rubric, same reviewer, run once each per setup. One reviewer is itself a limit: nothing here has been through an [inter-rater reliability check](../methods/fair-comparison.md#what-one-reviewer-cannot-tell-you), so a one or two point gap between runs is inside the noise rather than a result. There are now two same-case repeat pairs on this page, and together they support that threshold: Sonnet 5 scored 43 and 41 on Marlow, and 42 and 43 on Hartwell. Both pairs land within two points.

The totals are the less interesting half. On Marlow the second run scored better on usefulness and worse on hallucination, and those partly cancelled, so a reader comparing only the totals would miss that one run invented a sender's name and the other did not. On Hartwell a single area moved. A stable total can sit on top of an unstable judgement, which is why each record shows its nine areas rather than only a number. A consumer-app result is always "this model plus whatever that account happened to be carrying," not a clean read on the model alone. Every result had a real, specific flaw. Full detail is in each record's own "What this test cannot prove."

### Hartwell Follow Up

**Bottom line:** every model added something the source notes never said.

- **Haiku 4.5** invented a timeline: "this should take 2-3 weeks," stated as fact, no basis for it anywhere.
- **Gemini** turned a stated worry into a number: logged "Account Risk / Sensitivity: High" from a comment that was just caution, not a rating.
- **ChatGPT and Sonnet 5** avoided both errors and scored highest, but ChatGPT's email narrated its own compliance ("I have not assumed...") rather than reading like something a person would send.

### Marlow Pre-Call

**Bottom line:** every run caught the core trap (a secondhand comment being treated as a confirmed priority); the differences show up elsewhere.

- **ChatGPT** scored a clean 45/45, no flaw found.
- **Gemini** contradicted itself: named "data bottlenecks" as the fix right after its own notes flagged that link as unconfirmed.
- **Two of the four Claude runs** signed the outreach message with a name the case never gave them: the isolated agentic session and the consumer app. The Claude Code run did not, and neither did Haiku 4.5, which wrote a `[Your name]` placeholder and also refused to invent a name for the trade publication the case leaves unnamed. That restraint is worth noting because inventing plausible specifics is this model's weakness on two other cases here. Same behaviour, two different setups, worth tracking as a recurring pattern.

### Osmond Objection Diagnosis

**Bottom line:** all five runs correctly read the objection as more than one thing; the differences are in how well, and in what one of them made up along the way.

- **The agentic Sonnet 5 run and ChatGPT** both scored a clean 45/45, and both cleared the case's minimum of two distinct readings. Sonnet 5 produced three, ChatGPT two.
- **Gemini** scored well but folded a genuinely separate reading into a footnote instead of developing it.
- **The Claude consumer-app run** made the most serious error logged in this repo so far: it invented a price figure, "£900," that appears nowhere in the source.
- **Haiku 4.5 scored 31/45, the lowest in the repository**, and not for missing structure. Its two readings are genuinely distinct and its prohibitions list is complete. It misstated what the case says David asked no questions about, then added a "sticker shock" moment and a cost question the notes never record, plus a "Q3" and a "two weeks" the case never mentions. Its clarifying question also proposes a phased rollout, which is the rebuttal the case explicitly warns against rather than a neutral probe.

### Elmsworth Business Case

**Bottom line:** the cleanest case in this repo. Nobody invented an ROI figure.

- **Both Sonnet 5 runs** scored 44/45 (one docked for a session-context leak, the other for a spelling error).
- **Gemini** scored a clean 45/45.
- **Haiku 4.5** scored 40/45 with the strongest evidence-gap section of any run on this case, six named metrics each with what to collect and why. It lost marks for omitting the assumptions section the case asked for, and for contradicting its own plan: phase three sits at week seven while the closing script promises the VP numbers in five.
- **ChatGPT** did the most thorough evidence-gap analysis of any run here, but scored 43/45: an eleven-section, seventeen-item prohibited-claims list is not what someone asking for "something showing the impact so I can get this approved" can actually use in one sitting.

### What Appears Across Cases

- Three of the six consumer-app runs on Marlow and Osmond produced an invented detail (the Marlow signature, Gemini's Marlow contradiction, the Osmond price figure). The Marlow signature also showed up once outside a consumer app, so this isn't exclusive to consumer products, but the concentration is worth tracking. Small sample, not a statistically meaningful rate.
- **Haiku 4.5's failure mode is consistent across cases and is not vagueness.** On Hartwell it wrote "This should take 2-3 weeks" with no basis; on Osmond it invented a cost question, a quarter and a fortnight. Both read as sourced detail rather than as guesses, which makes them harder to catch than an honest gap would be. On the two cases where it scored well it invented nothing, so this is not a constant, and four runs cannot tell you what triggers it.
- Elmsworth's clean sweep lines up with its prompt stating prohibitions explicitly (no percentage, no dollar figure, no hours, no satisfaction claim) rather than leaving gaps to fill.
- **This page supplies most of a wider catalogue.** [Which AI Mistakes Actually Get Through](https://github.com/shaunmarsden/practical-ai-sales-workflows/blob/main/guides/which-ai-mistakes-get-through.md) sorts every defect found across this bench and its two sibling repositories by whether a careful reader would have caught it. Seven of the eleven it lists as hard to catch are from this page, including the Marlow signature, the Osmond price and both of Haiku's invented details. Four of the five it lists as obvious are from here too, which is the more flattering half and the less useful one.

## Adding a Further Result

When a result is added, it should include:

1. the full fictional input;
2. the exact task;
3. the model and setup;
4. the raw output;
5. the completed rubric;
6. a short honest verdict; and
7. a clear statement of what the test cannot prove.

A screenshot, a winner badge or a single number is not enough.
