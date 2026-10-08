# Model Run Record: ChatGPT, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables the case names (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** ChatGPT, in the consumer web app. I ran this myself. It reported "worked for 18s", which fits a reasoning model, but I couldn't confirm the exact model version, so I don't claim one.
- **Date:** 3 August 2026
- **Account or plan, if relevant:** my own ChatGPT account and plan; nothing more specific
- **Custom instruction, project context or skill used:** unknown. This went through the consumer product, not the raw API, so any custom instructions, memory or system prompt ChatGPT adds by default may have shaped the output. That's a real difference from the Sonnet 5 and Haiku 4.5 runs, which ran from the case file alone, with no custom instruction or account memory. Treat this pair of results as useful, but not run the same way as the first pair.

## Input

- **Exact prompt:** identical to the earlier runs: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else, identical to the earlier runs
- **Anything intentionally excluded:** same as the earlier runs, no additional context, no prior correspondence

## Output

- **Link or file path:** raw output retained below, as I pasted it from the ChatGPT web app
- **Raw output retained:** yes. The email draft section included some visible product-interface text ("Send", "Recipients", a duplicated subject line) from ChatGPT's canvas view, kept in below exactly as pasted rather than cleaned up, since this is a genuine artifact of running the prompt through the product rather than the API
- **Any human editing before scoring:** none beyond removing that interface chrome is noted, not performed, the raw text below is exactly what was received

### Internal Summary

**Confirmed information:** Tunde Adeyemi, Commercial Director at Hartwell Analytics, raised concerns about inconsistent follow-up timing and incomplete CRM records after customer calls. Sales managers have observed variation in how quickly follow-up is sent. Hartwell experienced a difficult CRM workflow change last year and is cautious about another large rollout. Tunde wants the current process understood before deciding whether a technology change is necessary. Sales Operations would need to participate in any potential test.

**Assumptions:** None.

**Unknowns:** The causes and extent of the inconsistencies, the current post-call workflow and ownership, the teams or CRM fields most affected, and what Hartwell would consider an acceptable improvement. There is no confirmed budget, approved project, agreed technology solution, pilot or attributable commercial loss.

### Email Draft to Tunde

[Product interface text as pasted: "Send / Recipients / Understanding Hartwell's post-call processUnderstanding Hartwell's post-call process"]

Hi Tunde,

Thank you for explaining the concerns around the consistency of customer follow-up and CRM updates.

My understanding is that sales managers have noticed variation in follow-up timing and that some CRM records are incomplete. Given Hartwell's experience with the CRM workflow change last year, it makes sense to understand the existing process before deciding whether any technology change is needed.

The next useful step would be to document the current workflow, including ownership, handoffs and where information is being delayed or missed. It would also be helpful to understand which Sales Operations stakeholders should contribute to that review.

I have not assumed that AI or another technology change is the answer, or that a test has been agreed.

Could you let me know who from Sales Operations would be best placed to provide input?

Best,
Shaun

### Three Proposed Discovery Actions

1. Map the current post-call workflow: document each step from the end of a customer call through follow-up preparation, approval, sending and CRM completion, including owners, handoffs and expected timings.
2. Establish the scale and causes of variation: review a representative sample of recent calls and CRM records to identify where delays or incomplete updates occur, without assuming they have caused a commercial loss.
3. Define the decision and stakeholder process: identify the relevant Sales Operations stakeholders, the constraints created by the previous CRM change and the evidence Hartwell would need before considering any process or technology test.

### CRM Update Suggestions

**Confirmed information to record:**
- Contact: Tunde Adeyemi
- Role: Commercial Director
- Company: Hartwell Analytics
- Business concerns: variation in customer follow-up timing and incomplete CRM records
- Current position: wants the existing process understood before agreeing that a technology change is needed
- Change context: cautious because of a difficult CRM workflow change last year
- Stakeholder requirement: Sales Operations would need to be involved in any potential test

**Assumptions:**
- None should be added to the CRM record.
- The opportunity stage should remain unchanged unless supported by existing CRM evidence.

**Unknowns to record or investigate:**
- Size and frequency of the follow-up and CRM-completeness issues
- Current workflow, ownership and approval steps
- Relevant Sales Operations contacts and decision-makers
- Success measures for any future change
- Budget availability
- Project approval status
- Preferred or agreed technology
- Whether any test will be considered or approved
- Whether the issue has caused a specific commercial loss

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 5 | 4 | 4 | 5 | 3 | 5 | 5 | 5 | 41 / 45 |

No automatic failure.

## Honest Notes

- **What it did well:** it used a Confirmed / Assumptions / Unknowns structure in the summary and the CRM suggestions, and more thoroughly than the Sonnet 5 or Haiku 4.5 runs. In the email itself it ruled out two things the case says weren't agreed, AI as the answer and a test: "I have not assumed that AI or another technology change is the answer, or that a test has been agreed". It never made up a timeline, unlike Haiku 4.5's "2-3 weeks". The email ends with a real, specific question, not a plan made to look agreed.
- **What it got wrong:** two things. First, that same sentence is accurate but reads as the model describing its own rule-following, not as something a person would write to a customer. A real edit would cut it before sending, which is why it lost points on Tone and not on Hallucination. Second, in the CRM suggestions, "the opportunity stage should remain unchanged unless supported by existing CRM evidence" is labelled as an Assumption. It's really a guardrail, not an assumption about the case. That's a small labelling slip, not a factual mistake.
- **What a person still had to decide:** whether to cut the line about its own rules from the email before sending, and whether anything supports changing the opportunity stage, since the case notes don't give a stage at all.
- **What this test cannot prove:** this ran through the ChatGPT product, not a raw API call. Any system prompt, custom instruction or memory the product adds by default is an unknown I can't rule out. So this test is less controlled than the Sonnet 5 against Haiku 4.5 comparison: useful, but not run the same way. One run, one case, one reviewer.
