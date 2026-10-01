# Model Run Record: Claude Sonnet 5, Hartwell Follow Up Case, Second Run

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables the case names (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Claude Sonnet 5
- **Date:** 7 September 2026
- **Account or plan, if relevant:** run as an isolated subagent inside an agentic coding assistant session. That's neither a raw API call nor a consumer web app. It's the same setup as the second Marlow run, and different from the first Hartwell run, which I ran inside Claude Code.
- **Custom instruction, project context or skill used:** none for the task itself. The subagent got only the case file's source notes and task. It couldn't see the first run's output or score, or know that I was comparing them.

## Why This Run Exists

The bench had one Sonnet 5 run per case, so Sonnet 5 only looked steady on single runs, while the Haiku runs had just shown an 11-point spread across cases. Only Marlow had a repeat of the same case. This adds a second, so the claim that a one or two point gap is noise now rests on two pairs, not one.

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

No automatic failure. It makes up nothing: no meeting is treated as booked, no pilot, budget, approval or promised outcome appears, and AI isn't presented as the agreed answer.

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

One point apart, and only one area moved. It's the least eventful repeat in this repo, and that's useful, not boring. The first Hartwell run's notes recorded no made-up detail, and this run has none either. So both runs avoid the mistake the Haiku run made on this case.

Next to the Marlow pair, though, a pattern shows that the totals hide.

| Case | First | Second | Total moved | Areas that moved |
| --- | ---: | ---: | ---: | --- |
| Marlow | 43 | 41 | 2 | Usefulness up, Approval down, Hallucination down 5 to 3 |
| Hartwell | 42 | 43 | 1 | Separation up |

On Marlow the second run scored higher on usefulness and much lower on hallucination, and the two partly cancelled out in the total. Someone comparing only the totals, 43 against 41, would see a small wobble and miss that one run made up a sender's name and the other didn't. **A steady total can hide an unsteady judgement.** The related repo reached the same finding from a nine-run test on a different rubric.

## Honest Notes

- **What it did well:** its Unknowns list matches the case's five "did not say" items one for one, which is the clearest proof the model read that section and didn't skim it. The CRM suggestions go further than the task asked by recording what hasn't happened: "no budget, project approval, AI solution, or pilot has been agreed". A careless CRM update would leave that out, and a later reader would most want it.
- **A choice worth noticing:** under Assumptions it wrote "None stated, no assumptions should be added at this stage" instead of inventing two or three plausible ones to fill the heading. The case asks for confirmed facts, assumptions and unknowns kept apart, and an empty section is a fair reading of a case that bans making things up. A second scorer might fairly mark this down for dodging a deliverable. I scored it as discipline, and it's the place on this run where a reviewer is most likely to disagree with me.
- **What it got wrong:** nothing factual. It loses marks for being thin. The three discovery actions are sound but generic, and would fit most accounts with a CRM complaint. None has an owner or a timeframe, so Next Step stays at 4: they say what to do but not who or when.
- **What a person still had to decide:** whether to send the email at all before anyone has approached Sales Operations. The message suggests involving them without knowing whether Tunde has raised it internally.
- **What this test cannot prove:** two runs of one model on one fictional case, both scored by the person who ran them. It says nothing about a third run, and the single-scorer limit applies to the comparison as much as to either score. If you want to test that, [score a run yourself](../feedback/score-a-run-yourself.md).
