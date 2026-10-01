# Model Run Record: Claude Haiku 4.5, Elmsworth Business Case Case

## Test Setup

- **Case:** [Elmsworth Business Case, Missing Baseline](../cases/elmsworth-business-case-case.md)
- **Task:** the four deliverables the case names (business case draft, a clear evidence gap section, a recommended way to measure a baseline, what must not be presented as confirmed)
- **Model and version:** Claude Haiku 4.5, run as an isolated agent with no memory of any other run on this case
- **Date:** 7 September 2026
- **Account or plan, if relevant:** not applicable. It ran straight from the case file with no product setup
- **Custom instruction, project context or skill used:** none. It had the same source material as the Sonnet 5, ChatGPT and Gemini runs, so this is a Model test, not a Setup test.

## Input

- **Exact prompt:** the case's own task wording verbatim, with the instruction to use only the source notes in the case file.
- **Source material:** the case's own source notes, verbatim.
- **Anything intentionally excluded:** no additional company context, no assumed industry detail about retail support operations.

## Output

- **Link or file path:** raw output retained below, in full
- **Raw output retained:** yes, unedited
- **Any human editing before scoring:** none

# Elmsworth Support AI Drafting Tool – Business Case

## CONFIRMED INFORMATION

**Pilot Setup**
- Duration: 3-week pilot (dates: _[to be specified]_)
- Participants: 4 support agents
- Tool: AI drafting assistant for customer email replies
- Current team size: 20 agents (pilot represents 20% of department)

**Qualitative Feedback**
- Direct quote from Head of Customer Support: "the team seems to be getting through emails quicker, a few of them mentioned it feels like a real time-saver"
- No formal survey conducted; feedback from informal follow-up conversation
- Scope of "a few": unclear whether this means 2, 3, or all 4 pilots agents

---

## WHAT WE DO NOT KNOW (EVIDENCE GAPS)

To make a quantified return-on-investment case, the following metrics would need to be collected:

| Metric | What We'd Need | Why It Matters |
|--------|---|---|
| **Time per email** | Baseline (pre-pilot) and pilot-week averages for email composition and review time per ticket | To calculate actual time savings per agent per week |
| **Ticket throughput** | Baseline and pilot-week total tickets handled per agent per day/week | To show whether volume increased or stayed constant while time-per-ticket decreased |
| **First-response time** | Baseline and pilot-week average time from ticket arrival to first response | To confirm whether speed gains affected SLA compliance or customer wait times |
| **Resolution time** | Baseline and pilot-week average days-to-close per ticket | To show whether the tool shortened overall case resolution or merely draft speed |
| **Customer satisfaction** | Baseline CSAT or NPS score and pilot-week score for tickets handled by pilot agents | To verify that faster replies didn't harm quality or satisfaction |
| **Individual variation** | Which agents improved and by how much | To clarify whether all 4 benefited equally or a subset drove the perception |

---

## WHAT THIS CASE SAYS IN THE ABSENCE OF THAT DATA

**Opportunity Signal**
Agents reported subjective improvement in email throughput speed following introduction of an AI drafting tool. This qualitative signal warrants investigation through structured measurement.

**What We Cannot Claim**
- No specific time savings (e.g., "X hours per week per agent")
- No productivity increase (e.g., "tickets-per-day improved by Y%")
- No cost savings or ROI figure
- No confirmation that customer satisfaction was maintained or improved
- No evidence that all 20 agents would see the same benefit

---

## RECOMMENDED PATH FORWARD

Rather than extrapolate from a measurement-free pilot, propose a **baseline-first rollout** to the VP:

### Phase 1: Measure Before Scaling (Weeks 1–2)
- **Select** 2–4 comparison agents from the 16 not yet trained
- **Collect baseline** for all 20 agents for 2 weeks:
  - Tickets handled per day per person
  - Average time from ticket open to first response
  - Average time from ticket open to resolution
  - One-question pulse: "Is the current process meeting your speed needs?" (yes/no)
- **No tool deployment yet** – this is the control period
- **Effort:** Automate metric pulls from your ticketing system; ask agents one question

### Phase 2: Pilot with Measurement (Weeks 3–6)
- **Deploy the tool** to the same 4 agents (or a new cohort if you prefer to reset)
- **Collect identical metrics** every week for 4 weeks
- **Track adoption**: Which agents use the tool? How often?
- **Collect feedback**:
  - Same pulse question at weeks 2, 4: "Is the current process meeting your speed needs?"
  - Open comment: "What's one thing the tool did or didn't help with?"

### Phase 3: Analysis & Decision (Week 7)
- **Compare** baseline vs. pilot metrics side-by-side
- **Quantify** the delta (if any) in time-per-ticket, tickets-per-day, first-response time
- **Decide**: If metrics improve by X%, does the cost justify rollout to all 20?
- **Build the real ROI case** with your VP using actual data

---

## WHAT MUST NOT BE IN THE PRESENTATION TO YOUR VP

- ❌ Any specific percentage time saved (e.g., "15% faster")
- ❌ Any dollar figure or payback period (e.g., "saves $50K/year")
- ❌ A statement that "all 4 agents found it helpful" (only "a few" provided feedback)
- ❌ A claim that customer satisfaction improved (no CSAT data exists)
- ❌ Extrapolation to all 20 agents without caveats (20% pilot ≠ 100% rollout guarantee)
- ❌ A request for budget to roll out to all 20 now

---

## WHAT TO LEAD WITH TO YOUR VP INSTEAD

"We ran a 3-week pilot with 4 agents. Early feedback is encouraging—agents said it feels faster—but we didn't capture baseline metrics, so I can't quantify the impact yet. Before we spend on a full rollout, I'd like to run a 4-week measurement window to nail down what 'faster' actually means in hours-per-ticket and customer wait time. If we see a real lift, I'll bring you the numbers and a cost-benefit. If we don't, we'll know it's not the right tool for our team. Here's what I need from you: [timeline approval / budget for X hours of setup / access to Y system]."

This positions you as data-driven, shows the VP you learned from the pilot's shortcomings, and gives you credibility for the follow-up conversation in 5 weeks when you have actual numbers.

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | 4 | 40 / 45 |

No automatic failure. It keeps to all four of the case's bans: no percentage, no dollar figure, no hours claim, and no claim that customer satisfaction went up.

## Honest Notes

- **What it did well, and the best thing in this run:** the evidence gap section is exactly what the case asked for, and better than it needed to be. It names six metrics, each with what to collect and why it matters, and a "What We Cannot Claim" list that refuses the four things the case bans. It also catches the trap the case is built around: "Scope of 'a few': unclear whether this means 2, 3, or all 4". A weaker answer would have smoothed that over into "the team found it helpful".
- **Every figure it gives is right**, and it worked out two of them rather than copying them: 4 of 20 agents is 20 per cent, and 16 agents are still untrained. It also doesn't make up pilot dates. It writes `[to be specified]`, and uses `X%` and `Y%` as placeholders in its examples of what not to claim instead of filling them in.
- **What it got wrong:** the case asks for a draft "keeping confirmed information, direct quotes, and assumptions visibly separate", and there's no assumptions section. Confirmed information and evidence gaps are kept apart, but the third group is missing, so one of the four deliverables is only partly there.
- **A second, smaller problem:** it contradicts its own plan. Phase 3 sits at week 7, but the closing script tells the VP there will be numbers "in 5 weeks". Nothing in the case supports either figure, and they don't agree, which is the kind of thing a VP would notice before the plan even starts.
- **The week numbers it suggests are a judgement call, not a mistake.** The case asked for a recommended way to measure from here, and a plan needs a shape. It labels them as a proposal, not as agreed. That's why they cost nothing on the hallucination row, where the Osmond run's made-up call detail cost two points.
- **What a person still had to decide:** whether the VP wants numbers at all. The case leaves that unknown on purpose. This run assumes numbers are needed and builds a whole measuring plan on that. It may be right, but it isn't established.
- **What this test cannot prove:** one run, one fictional case, scored by the same person who ran it. It says nothing about whether a second run would also leave out the assumptions section.
