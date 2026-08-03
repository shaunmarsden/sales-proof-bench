# Model Run Record: Claude Haiku 4.5, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables named in the case (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Claude Haiku 4.5, run as an isolated agent with no memory of the earlier Claude Sonnet 5 run on this same case
- **Date:** 3 August 2026
- **Account or plan, if relevant:** not applicable, run directly from the case file with no product-specific setup
- **Custom instruction, project context or skill used:** none. Same exact prompt and source material as the Sonnet 5 run, deliberately unchanged, so this is a Model test, not a Setup test.

## Input

- **Exact prompt:** identical to the Sonnet 5 run: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else. Identical to the Sonnet 5 run.
- **Anything intentionally excluded:** same as the Sonnet 5 run, no additional context, no prior correspondence.

## Output

- **Link or file path:** raw output retained below, in full
- **Raw output retained:** yes, unedited
- **Any human editing before scoring:** none

### Internal Summary

**Confirmed:** Tunde Adeyemi (Commercial Director, Hartwell Analytics) identified two operational issues, inconsistent follow-up speed post-call and incomplete CRM records, and is open to exploring solutions. A prior CRM workflow change created organizational caution about rollouts. Tunde's priority is understanding current process before technology change is considered. Sales Operations involvement is a requirement.

**Assumptions (unconfirmed):** These issues affect sales effectiveness; a process standardization opportunity exists.

**Unknowns:** Root causes of inconsistency, specific missing CRM fields, current process owner, commercial impact of delays, definition of success.

**Not said:** Budget, project approval, technology preference, pilot agreement, or specific customer loss.

### Email Draft to Tunde

Subject: Understanding Hartwell's Follow-Up and CRM Workflow

Hi Tunde,

Thanks for the conversation, I appreciate you flagging the follow-up timing and CRM record gaps your sales managers are seeing. Before we explore any changes, I'd like to understand your current workflow better, especially given the challenges your team navigated last year.

I'd suggest we start with three focused discovery calls:
1. A walk-through of your current follow-up process and CRM update workflow with the team doing the work
2. A conversation with Sales Operations about any barriers or dependencies they see
3. A look at specific CRM records to identify which fields are most consistently incomplete

This should take 2-3 weeks and will give us a clear picture of where friction actually lives. Only then will we know what kind of change, if any, makes sense for Hartwell.

Are you open to scheduling these conversations?

Best,
Shaun

### Three Discovery Actions

1. **Process mapping session**, interview 2-3 sales team members on their post-call follow-up routine: timing, CRM fields touched, blockers, workarounds. Document the current workflow step-by-step.
2. **Sales Operations alignment**, meet with the Sales Operations owner to understand system constraints, existing automations, data validation rules, and appetite for workflow changes post-previous implementation.
3. **CRM audit**, sample 10-15 recent call records to identify which fields are most frequently incomplete and whether gaps are consistent or agent-specific.

### CRM Update Suggestions

- **Add explicit post-call checklist:** a required sequence in CRM (call summary, next steps, timeline) that prompts before record close, without locking the form.
- **Surface incomplete fields:** configure dashboard or record view to highlight missing priority fields (e.g. next action date, decision timeline) so gaps are visible, not hidden.
- **Establish baseline metrics:** track follow-up send time and CRM field completion by user/week to make variation visible and measurable.
- **Coordinate with Sales Operations:** any CRM change should route through them first; avoid surprises post-rollout.

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 4 | 3 | 4 | 3 | 4 | 5 | 4 | 2 | 33 / 45 |

No automatic failure: nothing here is an invented customer commitment or an unapproved commercial claim, but the hallucination found below is real and specific enough to cost genuine points, not just a rounding difference.

## Honest Notes

- **What it did well:** the internal summary structure, explicit Confirmed / Assumptions / Unknowns / Not Said labels, is more visibly separated than the Sonnet 5 run's more narrative version. The discovery actions and CRM suggestions stay grounded in the source notes, with no invented specifics about Hartwell itself.
- **What it got wrong:** the email draft states "This should take 2-3 weeks" for the proposed discovery calls. Nothing in the source notes gives any timeframe, and this is exactly the kind of plausible-sounding detail the task explicitly said not to invent. It reads confidently, not as a guess, which makes it easy to miss on a quick read. This is the single concrete reason this run scores lower than the Sonnet 5 run, not a vaguer "it felt less careful."
- **What a person still had to decide:** whether "2-3 weeks" is even in the right range before sending anything, since the model invented a number with no basis to check it against. That is a worse position than being told nothing, since an invented specific reads as more trustworthy than an honest unknown would have.
- **What this test cannot prove:** this is one run each, from two different models, on one fictional case, scored by the same person who ran both. It says nothing about how either model performs on a different task, or how consistent either score would be with a second, independent reviewer. It is a genuine Model comparison in the fair-comparison method's own sense (same prompt, same source, same rubric, same reviewer), not a Setup or Workflow comparison, and it is a sample of one case, not a general verdict on either model.
