# Model Run Record: Gemini, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables the case names (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Gemini, in the consumer web app. I ran this myself. I couldn't confirm the exact model version, so I don't claim one.
- **Date:** 3 August 2026
- **Account or plan, if relevant:** my own Gemini account and plan; nothing more specific
- **Custom instruction, project context or skill used:** unknown. As with the ChatGPT run, this went through the consumer product, not the raw API, so any custom instruction, memory or system prompt Gemini adds by default may have shaped the output. It isn't run the same way as the Sonnet 5 against Haiku 4.5 comparison.

## Input

- **Exact prompt:** identical to the earlier runs: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else, identical to the earlier runs
- **Anything intentionally excluded:** same as the earlier runs, no additional context, no prior correspondence

## Output

- **Link or file path:** raw output retained below, as I pasted it from the Gemini web app
- **Raw output retained:** yes, unedited
- **Any human editing before scoring:** none

### 1. Short Internal Summary

**Confirmed Information:**
- Stakeholder: Tunde Adeyemi (Commercial Director, Hartwell Analytics) spoke with Shaun.
- Core Issue: sales managers report inconsistent follow-up speeds and incomplete CRM records.
- Historical Context: Hartwell had a difficult CRM workflow change last year and is cautious about large rollouts.
- Requirements: Tunde wants to fully understand the current process before agreeing to any technology changes. Sales Operations must be involved in any testing.

**Assumptions:**
- The inconsistency stems from process gaps, lack of standardized guidelines, or manual effort friction rather than deliberate non-compliance.

**Unknowns:**
- Budget availability.
- Formal project approval status.
- Specific commercial or financial losses caused by late follow-ups.
- Agreement on using AI or committing to a pilot.

### 2. Email Draft to Tunde

Subject: Following up, Hartwell Analytics process mapping and next steps

Hi Tunde,

Thank you for speaking with Shaun regarding your team's current follow-up cadence and CRM updates.

We completely understand your caution around major technology changes given the CRM workflow transition Hartwell experienced last year. Your focus on thoroughly understanding the existing process before evaluating any new solutions makes complete sense.

To support this step, we would welcome the opportunity to work alongside you and the Sales Operations team to map out the current post-call workflow. This will help identify where the friction or delays are occurring without jumping to premature conclusions.

Please let us know the best way to coordinate with your team on this initial review.

Best regards,
Shaun
[Company Name]

### 3. Three Proposed Discovery Actions

1. Conduct a Process Mapping Session: partner with Sales Operations and select sales managers to document the end-to-end follow-up workflow and isolate key points of delay or friction.
2. Perform a CRM Record Audit: review a representative sample of incomplete CRM records to identify specifically which fields or updates are most frequently omitted.
3. Define Success Criteria with Sales Operations: establish the operational requirements and guardrails Sales Operations would require before any potential testing or workflow adjustments are considered.

### 4. CRM Update Suggestions

**Fields to Populate (Confirmed Info):**
- Contact Name: Tunde Adeyemi
- Title: Commercial Director
- Company: Hartwell Analytics
- Primary Pain Points: inconsistent follow-up timing post-call; incomplete CRM records reported by sales managers.
- Account Risk / Sensitivity: High caution regarding technology rollouts due to a difficult CRM workflow change last year.
- Key Stakeholders: Sales Operations (required for any testing phase).
- Current Stage: Early Discovery / Process Review (Tunde must evaluate current process before considering tech changes).

**Fields to Leave Blank / Flag as Unknown:**
- Budget: unknown (do not populate)
- Project Status: unapproved / under review
- Solution Fit: TBD (AI / specific tech not agreed upon)
- Pilot Agreed: no
- Quantified Commercial Impact: unknown (no specific revenue loss reported)

## Score

| Accuracy | Fidelity | Separation | Usefulness | Next Step | Tone | Privacy | Approval | Hallucination | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 4 | 3 | 4 | 4 | 4 | 5 | 4 | 3 | 35 / 45 |

No automatic failure. The problem below is real and specific, not a rounding difference, but it isn't a made-up customer commitment or an unapproved commercial claim shown to the customer.

## Honest Notes

- **What it did well:** it labelled a real inference as an assumption instead of stating it as fact: "the inconsistency stems from process gaps... rather than deliberate non-compliance" is a leap the notes don't confirm, and it says so. The email suggests working together without claiming a test has been agreed. It left "[Company Name]" as a placeholder in the signature instead of guessing my company's name. That's a sensible way to mark a real unknown rather than make up something plausible.
- **What it got wrong:** in the CRM suggestions, "Account Risk / Sensitivity: High" turns Tunde's stated caution about "another large rollout" into a formal severity rating nobody gave. This is the kind of mistake this whole family of tools exists to catch: a real, stated concern recorded as more certain than the evidence allows, here raised to a formal "High" field. It's a smaller, subtler version of the "at risk" labelling problem found earlier when I checked ai-for-commercial-teams. It isn't identical, but it's the same kind of failure. Two smaller slips: the email thanks Tunde "for speaking with Shaun" and then signs off as Shaun, and the CRM block logs a "Current Stage: Early Discovery" the case never gives.
- **What a person still had to decide:** whether "High" is the right level to log when there's only a stated caution and no measured risk, and what my company's name should be before the email signature can be used.
- **What this test cannot prove:** the same caveat as the ChatGPT run applies. This went through the consumer product, not a raw API call, so it isn't run the same way as the Sonnet 5 against Haiku 4.5 pair. One run, one case, one reviewer.
