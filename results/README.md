# Results

This page lists every published run of Sales Proof Bench: the same fictional sales task given to different models and setups, scored by one person against a fixed rubric. It is not a leaderboard, and a score below says nothing about which model is generally better, only how it handled this one task. New here? The [root README](../README.md) explains the method and the rules behind these scores.

## Published

None of the 17 runs below triggered an automatic failure. Every score is the rubric result only. "Consumer app" means an unknown system prompt, account history or product feature may have shaped the output; "Claude Code" and "isolated agent" mean only the case file went in.

**Hartwell Follow Up Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, Claude Code](claude-sonnet-5-hartwell-follow-up-case.md) | 42/45 |
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

**Osmond Objection Diagnosis Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-osmond-objection-diagnosis-case.md) | 45/45 |
| [Claude Sonnet 5, consumer app (my account)](claude-sonnet-5-osmond-objection-diagnosis-case-consumer-app.md) | 37/45 |
| [ChatGPT 5.6, consumer app, version confirmed](chatgpt-osmond-objection-diagnosis-case.md) | 45/45 |
| [Gemini, consumer app, version not confirmed](gemini-osmond-objection-diagnosis-case.md) | 43/45 |

**Elmsworth Business Case Case**

| Setup | Score |
|---|---|
| [Claude Sonnet 5, agentic coding session](claude-sonnet-5-elmsworth-business-case-case.md) | 44/45 |
| [Claude Sonnet 5, consumer app (my account)](claude-sonnet-5-elmsworth-business-case-case-consumer-app.md) | 44/45 |
| [ChatGPT, consumer app, version not confirmed](chatgpt-elmsworth-business-case-case.md) | 43/45 |
| [Gemini, consumer app, version not confirmed](gemini-elmsworth-business-case-case.md) | 45/45 |

## What the Results Show

Same prompt, same source notes, same rubric, same reviewer, run once each. A consumer-app result is always "this model plus whatever that account happened to be carrying," not a clean read on the model alone. Every result had a real, specific flaw. Full detail is in each record's own "What this test cannot prove."

### Hartwell Follow Up

**Bottom line:** every model added something the source notes never said.

- **Haiku 4.5** invented a timeline: "this should take 2-3 weeks," stated as fact, no basis for it anywhere.
- **Gemini** turned a stated worry into a number: logged "Account Risk / Sensitivity: High" from a comment that was just caution, not a rating.
- **ChatGPT and Sonnet 5** avoided both errors and scored highest, but ChatGPT's email narrated its own compliance ("I have not assumed...") rather than reading like something a person would send.

### Marlow Pre-Call

**Bottom line:** every run caught the core trap (a secondhand comment being treated as a confirmed priority); the differences show up elsewhere.

- **ChatGPT** scored a clean 45/45, no flaw found.
- **Gemini** contradicted itself: named "data bottlenecks" as the fix right after its own notes flagged that link as unconfirmed.
- **Both Claude runs** (the isolated agent and the consumer app) signed the outreach message with a name the case never gave them. Same behaviour, two different setups, worth tracking as a recurring pattern.

### Osmond Objection Diagnosis

**Bottom line:** all four runs correctly read the objection as more than one thing; the differences are in how well.

- **The agentic Sonnet 5 run and ChatGPT** both scored a clean 45/45, and both cleared the case's minimum of two distinct readings (three found vs. two).
- **Gemini** scored well but folded a genuinely separate reading into a footnote instead of developing it.
- **The Claude consumer-app run** made the most serious error logged in this repo so far: it invented a price figure, "£900," that appears nowhere in the source.

### Elmsworth Business Case

**Bottom line:** the cleanest case in this repo. Nobody invented an ROI figure.

- **Both Sonnet 5 runs** scored 44/45 (one docked for a session-context leak, the other for a spelling error).
- **Gemini** scored a clean 45/45.
- **ChatGPT** did the most thorough evidence-gap analysis of any run here, but scored 43/45: an eleven-section, seventeen-item prohibited-claims list is not what someone asking for "something showing the impact so I can get this approved" can actually use in one sitting.

### What Appears Across Cases

- Three of the six consumer-app runs on Marlow and Osmond produced an invented detail (the Marlow signature, Gemini's Marlow contradiction, the Osmond price figure). The Marlow signature also showed up once outside a consumer app, so this isn't exclusive to consumer products, but the concentration is worth tracking. Small sample, not a statistically meaningful rate.
- Elmsworth's clean sweep lines up with its prompt stating prohibitions explicitly (no percentage, no dollar figure, no hours, no satisfaction claim) rather than leaving gaps to fill.

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
