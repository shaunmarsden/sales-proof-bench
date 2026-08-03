# Model Run Record: Claude Sonnet 5, Northstar Follow Up Case

## Test Setup

- **Case:** [Northstar Follow Up Case](../cases/northstar-follow-up-case.md)
- **Task:** the four deliverables named in the case (internal summary, email draft to Priya, three discovery actions, CRM update suggestions)
- **Model and version:** Claude Sonnet 5, run inside Claude Code
- **Date:** 3 August 2026
- **Account or plan, if relevant:** not applicable, run directly from the case file with no product-specific setup
- **Custom instruction, project context or skill used:** none. No project knowledge base, no custom instruction, no prior turns about Northstar. Only the case file's own source notes and task were given.

## Input

- **Exact prompt:** "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Priya; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Priya said" and "What Priya did not say" lists, verbatim, nothing else.
- **Anything intentionally excluded:** no additional company context, no prior correspondence, no assumed industry detail about facilities management. The test deliberately used only what the case actually provides.

## Output

- **Link or file path:** raw output retained below, in full, not summarised
- **Raw output retained:** yes, in full
- **Any human editing before scoring:** none. Scored as generated.

### Internal Summary

Priya Shah, Commercial Director at Northstar Facilities Group, raised two operational concerns: sales managers have noticed inconsistent turnaround on customer follow-up after calls, and some CRM records are incomplete. Northstar went through a difficult CRM workflow change last year, so there is real caution about another large rollout. Priya wants to understand the current process before agreeing that a technology change is needed, and said Sales Operations would need to be involved in any test. No budget, project approval or pilot has been agreed, and Priya has not linked the follow-up delay to a specific commercial loss.

### Email Draft to Priya

Subject: Following up from our conversation

Hi Priya,

Thanks for talking me through what you are seeing on your team, inconsistent follow-up timing and some incomplete CRM records, and for flagging how cautious the team is about another big workflow change after last year.

Before suggesting anything, it would help to understand the current process a bit more: how follow-up actually happens today, where records tend to fall through, and where Sales Operations would want to be involved if we looked at this together.

Would it be useful to set up a short conversation with Sales Operations included, purely to map out what is happening now? No commitment beyond that at this stage.

Best,
[Your name]

### Three Proposed Discovery Actions

1. Map the current follow-up process end to end with two or three sales managers, to see where timing actually varies and why.
2. Review a small, anonymised sample of recent CRM records with Sales Operations to identify where and why fields go incomplete.
3. Ask what specifically went wrong in last year's CRM workflow change, so any future recommendation avoids repeating it.

### CRM Update Suggestions

- Before recommending any tool, confirm with Sales Operations which fields are actually meant to be mandatory today, since gaps might reflect an unclear process rather than a tooling problem.
- Suggest logging, informally for now, how long follow-up takes after a call, so there is a real baseline instead of an impression, if the team is willing.
- Hold any suggestion of a new AI-assisted step until the current process is actually understood; nothing here should be read as a recommendation yet.

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 5 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 42 / 45 |

No automatic failure: no invented customer commitment, no unapproved commercial claim, no unsafe information handling.

## Honest Notes

- **What it did well:** stayed strictly inside the confirmed information. Did not invent a budget, a pilot, a meeting that had not been proposed, or a promised outcome, matching the case's own "did not say" list exactly. The email proposes a genuinely low-commitment next step (understand the process first) rather than pushing toward a tool decision Priya had not asked for.
- **What it got wrong:** nothing required a full rewrite, but fact and assumption separation relies on phrasing rather than an explicit label. A reviewer skimming quickly could miss that "Sales Operations would want to be involved" is Priya's own stated condition, not the drafter's suggestion, since both read in a similar tone.
- **What a person still had to decide:** whether proposing a joint conversation with Sales Operations, rather than a one-to-one first, is the right call for this specific relationship. That is a judgement about Priya and Northstar the case does not give enough to make, and the output correctly did not pretend to make it.
- **What this test cannot prove:** this is one run, from one model, on one fictional case, scored by the person who ran it. It says nothing about how this model performs on a different task, how a different model would compare on the same one, or how consistent this score would be with a second, independent reviewer. It demonstrates the record format works end to end; it is not yet the comparison the bench is ultimately for.
