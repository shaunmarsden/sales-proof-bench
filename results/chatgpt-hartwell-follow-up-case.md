# Model Run Record: ChatGPT, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables named in the case (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** ChatGPT, via the consumer web app. Shaun ran this himself and reported "worked for 18s", consistent with a reasoning model, but the exact underlying model version was not confirmed and is not claimed here.
- **Date:** 3 August 2026
- **Account or plan, if relevant:** Shaun's own ChatGPT account and plan; not specified further
- **Custom instruction, project context or skill used:** unknown. This went through the consumer product, not the raw API, so any custom instructions, memory, or system prompt ChatGPT applies by default may have shaped the output. This is a real difference from the Sonnet 5 and Haiku 4.5 runs, which were raw model calls with nothing else layered on top. Treat this pair of results as informative but not directly equivalent in method to the first pair.

## Input

- **Exact prompt:** identical to the earlier runs: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else, identical to the earlier runs
- **Anything intentionally excluded:** same as the earlier runs, no additional context, no prior correspondence

## Output

- **Link or file path:** raw output retained below, as pasted by Shaun from the ChatGPT web app
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

- **What it did well:** applied a Confirmed / Assumptions / Unknowns structure consistently across all four deliverables, not just the summary, more thoroughly than either the Sonnet 5 or Haiku 4.5 runs. Explicitly disclaimed exactly the things the task said not to invent: "I have not assumed that AI or another technology change is the answer, or that a test has been agreed" in the email itself, and never invented a timeline, unlike Haiku 4.5's fabricated "2-3 weeks". Ends the email with a genuine, specific question rather than a proposed plan dressed as agreed.
- **What it got wrong:** two specific things. First, that same disclaiming sentence, while accurate, reads as the model narrating its own compliance rather than something a person would actually write to a customer, a real edit would cut it before sending, which is why Tone lost points rather than Hallucination. Second, in the CRM suggestions, "the opportunity stage should remain unchanged unless supported by existing CRM evidence" is labelled as an Assumption but is actually a guardrail instruction, not an assumption about the case itself, a minor mislabelling rather than a factual error.
- **What a person still had to decide:** whether to cut the meta-commentary line from the email before sending, and whether the current opportunity stage genuinely has no supporting evidence to change it, since the case notes don't establish a stage at all.
- **What this test cannot prove:** this ran through the ChatGPT product, not a raw API call, so any system prompt, custom instruction or memory the product applies by default is an unknown variable this record cannot rule out. That makes this a less controlled test than the Sonnet 5 versus Haiku 4.5 comparison, informative, not directly equivalent. One run, one case, one reviewer.
