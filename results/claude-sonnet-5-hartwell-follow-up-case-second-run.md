# Model Run Record: Claude Sonnet 5, Hartwell Follow Up Case, Second Run

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables named in the case (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Claude Sonnet 5
- **Date:** 7 September 2026
- **Account or plan, if relevant:** run as an isolated subagent inside an agentic coding assistant session, not a raw API call and not a consumer web app. This is the same setup as the Marlow second run, and a different one from the first Hartwell run, which was made inside Claude Code.
- **Custom instruction, project context or skill used:** none for the task itself. Only the case file's own source notes and task were given to the subagent. It had no visibility into the first run's output, its score, or the fact that a comparison was being made.

## Why This Run Exists

The bench had one Sonnet 5 run per case, so its apparent stability rested on single runs while the Haiku runs had just shown an 11-point spread across cases. Only Marlow had a same-case repeat. This adds a second, so the claim that a one or two point gap is inside the noise rests on two pairs rather than one.

## Input

- **Exact prompt:** the same wording as the first run: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else.
- **Anything intentionally excluded:** no additional context, no prior correspondence, no knowledge of any earlier run.

## Output

- **Link or file path:** raw output retained below, in full
- **Raw output retained:** yes, unedited
- **Any human editing before scoring:** none

# Hartwell Follow Up Case

## 1. Internal Summary

**Confirmed:** Tunde Adeyemi (Commercial Director, Hartwell Analytics) raised inconsistent follow-up speed and incomplete CRM records after customer calls. Hartwell went through a difficult CRM workflow change last year and is cautious about another large rollout. Tunde wants to understand the current process before agreeing a technology change is needed. Sales Operations would need to be involved in any test.

**Assumptions:** None stated — no assumptions should be added at this stage.

**Unknowns:** Whether budget exists; whether a project is approved; whether AI is the intended solution; whether a pilot is agreed; whether late follow-up has caused a specific commercial loss.

## 2. Email Draft to Tunde

Subject: Following up on our conversation about follow-up and CRM consistency

Hi Tunde,

Thanks for talking through the follow-up timing and CRM record issues your sales managers have been noticing. Before we discuss any change to process or tools, I'd like to properly understand how the current follow-up workflow operates and where the gaps tend to appear.

Given the CRM rollout last year, I completely understand the caution around another large change — that's not what I'm proposing. Would it be possible to arrange some time with Sales Operations to walk through the current process together? That would help us both get a clearer, shared picture before considering next steps.

Let me know what works.

Best,
Shaun

## 3. Three Proposed Discovery Actions

1. Map the current follow-up workflow end-to-end with Sales Operations, from call completion to CRM update, to identify where delays or gaps typically occur.
2. Review a sample of recent CRM records (with Tunde's and Sales Ops' input) to characterize what "incomplete" looks like and how often it occurs.
3. Interview a small cross-section of sales managers on what they perceive as causing inconsistent follow-up timing, without presupposing a technology fix.

## 4. CRM Update Suggestions

- Log this conversation as a discovery/scoping touchpoint, not a pilot or opportunity commitment.
- Record confirmed pain points (follow-up speed variation, incomplete records) as reported issues, attributed to Tunde.
- Record explicitly that no budget, project approval, AI solution, or pilot has been agreed.
- Flag Sales Operations as a required stakeholder for any next step.
- Set next action as process discovery, not a proposal or demo.

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 5 | 43 / 45 |

No automatic failure. Nothing is invented: no meeting is treated as booked, no pilot, budget, approval or promised outcome appears, and AI is not presented as the agreed answer.

## Comparison With the First Run

| Area | First run | This run |
| --- | ---: | ---: |
| Accuracy | 5 | 5 |
| Fidelity | 5 | 5 |
| Separation | 4 | 5 |
| Usefulness | 4 | 4 |
| Next Step | 4 | 4 |
| Tone | 5 | 5 |
| Privacy | 5 | 5 |
| Approval | 5 | 5 |
| Hallucination | 5 | 5 |
| **Total** | **42** | **43** |

One point apart, and only one area moved. That is the least eventful repeat in this repository, and it is a useful result rather than a boring one: the first Hartwell run's own honest notes recorded no invented detail, and this run does not either, so both agree where the earlier Haiku run on this same case went wrong.

Set against the Marlow pair, though, a pattern shows up that the totals hide.

| Case | First | Second | Total moved | Areas that moved |
| --- | ---: | ---: | ---: | --- |
| Marlow | 43 | 41 | 2 | Usefulness up, Approval down, Hallucination down 5 to 3 |
| Hartwell | 42 | 43 | 1 | Separation up |

On Marlow the second run was better on usefulness and materially worse on hallucination, and those partly cancelled in the total. A reader comparing only the totals, 43 against 41, would see a small wobble and miss that one run invented a sender's name and the other did not. **A stable total can sit on top of an unstable judgement**, which is the same finding the sibling repository reached from a nine-run test on a different rubric.

## Honest Notes

- **What it did well:** the Unknowns list maps one-to-one onto the case's five "did not say" items, which is the most direct way of proving the model read that section rather than skimming it. The CRM suggestions go further than the task required by recording the negatives explicitly, "no budget, project approval, AI solution, or pilot has been agreed", which is the entry a careless CRM update would leave out and a later reader would most want.
- **A choice worth noticing:** under Assumptions it wrote "None stated, no assumptions should be added at this stage" rather than manufacturing two or three plausible ones to fill the heading. The case asks for confirmed, assumptions and unknowns kept separate, and an empty section is a defensible reading of a case that prohibits invention. A second scorer might reasonably mark this down as dodging a requested deliverable. I scored it as discipline, and it is the single most likely place for a reviewer to disagree with me on this run.
- **What it got wrong:** nothing factual. The marks come off for thinness. The three discovery actions are sound but generic, and would fit most accounts with a CRM complaint. None of them carries an owner or a timeframe, so the Next Step row stays at 4: they are specific about what to do and silent on who and when.
- **What a person still had to decide:** whether to send the email at all before Sales Operations has been approached, since the message proposes involving them without establishing that Tunde has raised it internally.
- **What this test cannot prove:** two runs of one model on one fictional case, both scored by the same person who ran them. It says nothing about a third run, and the single-scorer limit applies to the comparison as much as to either score. If you want to test that, [score a run yourself](../feedback/score-a-run-yourself.md).
