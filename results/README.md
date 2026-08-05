# Results

## Published

**Hartwell Follow Up Case:**

- [Claude Sonnet 5](claude-sonnet-5-hartwell-follow-up-case.md): 42/45, no automatic failure. Raw API call.
- [Claude Haiku 4.5](claude-haiku-4-5-hartwell-follow-up-case.md): 33/45, no automatic failure. Raw API call.
- [ChatGPT](chatgpt-hartwell-follow-up-case.md): 41/45, no automatic failure. Consumer web app, exact model version not confirmed.
- [Gemini](gemini-hartwell-follow-up-case.md): 35/45, no automatic failure. Consumer web app, exact model version not confirmed.

**Marlow Pre-Call Case:**

- [Claude Sonnet 5](claude-sonnet-5-marlow-pre-call-case.md): 43/45, no automatic failure. Raw API call.
- [Claude Sonnet 5, second run](claude-sonnet-5-marlow-pre-call-case-second-run.md): 41/45, no automatic failure. Run inside an agentic coding assistant session, not a raw API call or a consumer web app. This is a second independent run of the same model, not a second model; a genuine cross-model comparison for this case is still outstanding.

## What These Comparisons Actually Show

Same prompt, same source notes, same rubric, same reviewer, run once each. The Sonnet 5 versus Haiku 4.5 pair are raw API calls with nothing else layered on; the ChatGPT and Gemini runs went through each product's consumer web app, so an unknown system prompt or product feature may have shaped their output. Treat the two pairs as separately informative, not as one clean four-way ranking.

Every result had a real, specific flaw, none were flawless, and no two flaws were the same shape:

- **Haiku 4.5** invented a detail the notes never gave: its email stated "this should take 2-3 weeks" for a proposed set of discovery calls, with no basis, confidently rather than flagged as a guess.
- **Gemini** did not invent a new fact, but turned a real, stated concern into a formal certainty: it logged "Account Risk / Sensitivity: High" in the CRM suggestions from Tunde's actual caution about "another large rollout", a caution, not a quantified risk rating.
- **ChatGPT** and **Sonnet 5** avoided both of those specific failures, and were the two highest scores, but ChatGPT's email included a line explaining its own compliance ("I have not assumed that AI or another technology change is the answer") that reads as narrating the model's constraints rather than something a person would actually send to a customer.

No result scored a perfect 45, and no automatic failure occurred in any of the four. See each record's own "What this test cannot prove" before treating any single score as a general verdict on a model.

The Marlow case tests a different trap: whether a model conflates a secondhand, one-line comment from one person with a confirmed, company-wide priority. Both Sonnet 5 runs caught it cleanly, reproducibly, across two independent attempts. The second run also surfaced a failure the first did not: it signed the outreach message with an invented sender name that appears nowhere in the case, a concrete instance of filling a gap with plausible, unrequested detail. Two runs of one model is evidence the core trap is reliably caught by this model, and that a specific new failure mode exists worth watching for; it is not yet a cross-model comparison, the same starting point the Hartwell case began from.

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
