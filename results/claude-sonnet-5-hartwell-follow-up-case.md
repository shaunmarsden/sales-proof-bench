# Model Run Record: Claude Sonnet 5, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables the case names (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Claude Sonnet 5, run inside Claude Code
- **Date:** 3 August 2026
- **Account or plan, if relevant:** not applicable. It ran straight from the case file with no product setup
- **Custom instruction, project context or skill used:** none. No project knowledge base, no custom instruction, no earlier messages about Hartwell. It got only the case file's source notes and task.

## Input

- **Exact prompt:** "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else.
- **Anything intentionally excluded:** no additional company context, no prior correspondence, no assumed industry detail about facilities management. The test deliberately used only what the case actually provides.

## Output

- **Link or file path:** raw output retained below, in full, not summarised
- **Raw output retained:** yes, in full
- **Any human editing before scoring:** none. Scored as generated.

### Internal Summary

Tunde Adeyemi, Commercial Director at Hartwell Analytics, raised two operational concerns: sales managers have noticed inconsistent turnaround on customer follow-up after calls, and some CRM records are incomplete. Hartwell went through a difficult CRM workflow change last year, so there is real caution about another large rollout. Tunde wants to understand the current process before agreeing that a technology change is needed, and said Sales Operations would need to be involved in any test. No budget, project approval or pilot has been agreed, and Tunde has not linked the follow-up delay to a specific commercial loss.

### Email Draft to Tunde

Subject: Following up from our conversation

Hi Tunde,

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

No automatic failure: no made-up customer commitment, no unapproved commercial claim, no unsafe handling of information.

## Honest Notes

- **What it did well:** it stayed strictly inside the confirmed information. It didn't make up a budget, a pilot, a meeting nobody had proposed, or a promised outcome, and it matched the case's "did not say" list exactly. The email suggests a small next step (understand the process first) instead of pushing towards a tool decision Tunde hadn't asked for.
- **What it got wrong:** nothing needed a full rewrite, but it keeps facts and assumptions apart through wording, not labels. A reviewer skimming quickly could miss that "Sales Operations would want to be involved" is Tunde's own condition, not the drafter's suggestion, since both read in a similar tone.
- **What a person still had to decide:** whether to suggest a joint conversation with Sales Operations, instead of a one-to-one first, for this relationship. That's a judgement about Tunde and Hartwell the case doesn't give enough to make, and the output rightly didn't pretend to make it.
- **What this test cannot prove:** this is one run, from one model, on one fictional case, scored by the person who ran it. It says nothing about how this model does on a different task, how a different model would compare on this one, or whether a second, separate reviewer would give the same score. It shows the record format works from start to finish. On its own it isn't the comparison the bench is for. The [results page](README.md) has the other runs.
