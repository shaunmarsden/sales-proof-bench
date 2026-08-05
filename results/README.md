# Results

## Published

**Hartwell Follow Up Case:**

- [Claude Sonnet 5](claude-sonnet-5-hartwell-follow-up-case.md): 42/45, no automatic failure. Raw API call.
- [Claude Haiku 4.5](claude-haiku-4-5-hartwell-follow-up-case.md): 33/45, no automatic failure. Raw API call.
- [ChatGPT](chatgpt-hartwell-follow-up-case.md): 41/45, no automatic failure. Consumer web app, exact model version not confirmed.
- [Gemini](gemini-hartwell-follow-up-case.md): 35/45, no automatic failure. Consumer web app, exact model version not confirmed.

**Marlow Pre-Call Case:**

- [Claude Sonnet 5](claude-sonnet-5-marlow-pre-call-case.md): 43/45, no automatic failure. Raw API call.
- [Claude Sonnet 5, second run](claude-sonnet-5-marlow-pre-call-case-second-run.md): 41/45, no automatic failure. Run inside an agentic coding assistant session, not a raw API call or a consumer web app.
- [Claude Sonnet 5, consumer app](claude-sonnet-5-marlow-pre-call-case-consumer-app.md): 41/45, no automatic failure. Claude.ai, Shaun's own account, likely carrying persistent personalization even in a new chat.
- [ChatGPT](chatgpt-marlow-pre-call-case.md): 45/45, no automatic failure. Consumer web app.
- [Gemini](gemini-marlow-pre-call-case.md): 36/45, no automatic failure. Consumer web app.

**Osmond Objection Diagnosis Case:**

- [Claude Sonnet 5](claude-sonnet-5-osmond-objection-diagnosis-case.md): 45/45, no automatic failure. Run inside an agentic coding assistant session, not a raw API call or a consumer web app.
- [Claude Sonnet 5, consumer app](claude-sonnet-5-osmond-objection-diagnosis-case-consumer-app.md): 37/45, no automatic failure. Claude.ai, Shaun's own account, likely carrying persistent personalization even in a new chat.
- [ChatGPT](chatgpt-osmond-objection-diagnosis-case.md): 45/45, no automatic failure. Consumer web app.
- [Gemini](gemini-osmond-objection-diagnosis-case.md): 43/45, no automatic failure. Consumer web app.

**Elmsworth Business Case Case:**

- [Claude Sonnet 5](claude-sonnet-5-elmsworth-business-case-case.md): 44/45, no automatic failure. Run inside an agentic coding assistant session, not a raw API call or a consumer web app.
- [Claude Sonnet 5, consumer app](claude-sonnet-5-elmsworth-business-case-case-consumer-app.md): 44/45, no automatic failure. Claude.ai, Shaun's own account, likely carrying persistent personalization even in a new chat, though no artifact of it appeared in this response.
- [ChatGPT](chatgpt-elmsworth-business-case-case.md): 43/45, no automatic failure. Consumer web app.
- [Gemini](gemini-elmsworth-business-case-case.md): 45/45, no automatic failure. Consumer web app.

## What These Comparisons Actually Show

Same prompt, same source notes, same rubric, same reviewer, run once each. The Sonnet 5 versus Haiku 4.5 pair are raw API calls with nothing else layered on; the ChatGPT and Gemini runs went through each product's consumer web app, so an unknown system prompt or product feature may have shaped their output. Treat the two pairs as separately informative, not as one clean four-way ranking.

Every result had a real, specific flaw, none were flawless, and no two flaws were the same shape:

- **Haiku 4.5** invented a detail the notes never gave: its email stated "this should take 2-3 weeks" for a proposed set of discovery calls, with no basis, confidently rather than flagged as a guess.
- **Gemini** did not invent a new fact, but turned a real, stated concern into a formal certainty: it logged "Account Risk / Sensitivity: High" in the CRM suggestions from Tunde's actual caution about "another large rollout", a caution, not a quantified risk rating.
- **ChatGPT** and **Sonnet 5** avoided both of those specific failures, and were the two highest scores, but ChatGPT's email included a line explaining its own compliance ("I have not assumed that AI or another technology change is the answer") that reads as narrating the model's constraints rather than something a person would actually send to a customer.

No result scored a perfect 45, and no automatic failure occurred in any of the four. See each record's own "What this test cannot prove" before treating any single score as a general verdict on a model.

The Marlow case tests whether a model conflates a secondhand, one-line comment from one person with a confirmed, company-wide priority. All five runs across three models caught the core trap. The differences show up elsewhere: ChatGPT scored a clean 45/45 with no flaw found; Gemini's outreach message contradicted its own prep summary, asserting the fix is specifically "data bottlenecks" right after its own assumptions list flagged that exact link as unconfirmed; and both Claude runs, one an isolated subagent with no legitimate basis for a name at all, one a consumer-app run drawing on Shaun's own account context, signed the outreach message with a name the case never asked for. Two independent occurrences of that same signature pattern is a real, reproducible-looking guardrail, not a one-off.

The Osmond case tests whether a model treats a genuinely ambiguous objection as if it only had one obvious reading, the naive and most likely wrong response being to answer it as a plain price objection. All four runs correctly refused to treat it as one-dimensional. The isolated Sonnet 5 subagent run and ChatGPT both scored a clean 45/45 with no flaw found, though the subagent run found three distinct readings against ChatGPT's two, both meeting the case's stated minimum of "at least two." Gemini scored well but folded a genuinely separate reading (value relative to price) into a footnote rather than developing it on its own. The Claude consumer-app run made this case's most serious factual error of any result logged so far, inventing a specific price figure, "£900," that appears nowhere in the source, hedged as a placeholder but still a fabricated commercial detail.

**A pattern across both cases, worth a guardrail of its own:** every flaw found in a consumer-app run, the invented Marlow signature (both times), the invented Osmond price figure, and the Gemini Marlow self-contradiction, came from a run through a consumer product carrying its own account-level context or default behaviour, not from the raw API or isolated-subagent runs. This is not proof that consumer products are categorically worse; it is a real, observed pattern across the results logged here, and it means a consumer-app result in this repository should always be read as "this model plus whatever that account happened to be carrying," not as a clean read on the model alone.

The Elmsworth case tests whether a model invents a plausible-sounding return-on-investment figure to satisfy pressure for an approval-ready business case, rather than proposing a way to measure one. Unlike Marlow and Osmond, none of the four runs across three models invented anything, the most consistent result across any case in this repository so far. Both Sonnet 5 runs scored 44/45, one docked for a presentational session-context leak, the other for an actual spelling error ("sufient") in a VP-facing document. Gemini scored a clean 45/45. ChatGPT produced the single most thorough evidence-gap analysis of any run logged here, correctly catching both of the source notes' own explicitly-flagged unknowns, but scored 43/45 because an eleven-section, sixteen-item-prohibited-claims document is not realistically what someone asking for "something showing the impact so I can get this approved" can use in one sitting; rigor and fitness for the actual audience are not the same thing.

This case's cleaner result across every run, compared with the invented details found in three of the five consumer-app runs on Marlow and Osmond, is itself worth noting: this case's prohibitions are stated more explicitly and directly in the prompt (no percentage, no dollar figure, no hours, no satisfaction claim), which may make them easier to hold to than the subtler gap-filling temptations in the earlier two cases (an unstated sender, an unstated price point). This is an observation about this small set of results, not a general claim about which kinds of traps are harder for any model.

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
