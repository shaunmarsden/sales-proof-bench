# Model Run Record: Gemini, Hartwell Follow Up Case

## Test Setup

- **Case:** [Hartwell Follow Up Case](../cases/hartwell-follow-up-case.md)
- **Task:** the four deliverables named in the case (internal summary, email draft to Tunde, three discovery actions, CRM update suggestions)
- **Model and version:** Gemini, via the consumer web app. Shaun ran this himself; the exact underlying model version was not confirmed and is not claimed here.
- **Date:** 3 August 2026
- **Account or plan, if relevant:** Shaun's own Gemini account and plan; not specified further
- **Custom instruction, project context or skill used:** unknown. As with the ChatGPT run, this went through the consumer product, not the raw API, so any custom instruction, memory, or system prompt Gemini applies by default may have shaped the output. Not directly equivalent in method to the Sonnet 5 versus Haiku 4.5 comparison.

## Input

- **Exact prompt:** identical to the earlier runs: "Using only the source notes below, create: 1. a short internal summary; 2. an email draft to Tunde; 3. three proposed discovery actions; and 4. CRM update suggestions. Keep confirmed information, assumptions and unknowns separate. Do not invent customer intent, a meeting, a pilot, a budget or a promised outcome."
- **Source material:** the case's own "What Tunde said" and "What Tunde did not say" lists, verbatim, nothing else, identical to the earlier runs
- **Anything intentionally excluded:** same as the earlier runs, no additional context, no prior correspondence

## Output

- **Link or file path:** raw output retained below, as pasted by Shaun from the Gemini web app
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

No automatic failure: this is a genuine, specific issue rather than a rounding difference, but it is not an invented customer commitment or an unapproved commercial claim shown to the customer.

## Honest Notes

- **What it did well:** correctly labelled a genuine inference as an assumption rather than presenting it as fact, "the inconsistency stems from process gaps... rather than deliberate non-compliance" is a real interpretive leap the notes do not confirm, and it is honestly flagged as one. The email proposes working together without asserting a test has been agreed, and left "[Company Name]" as an explicit placeholder in the signature rather than guessing Shaun's own company name, a reasonable way to flag a genuine unknown instead of inventing a plausible-sounding one.
- **What it got wrong:** in the CRM update suggestions, "Account Risk / Sensitivity: High" turns Tunde's actual stated caution about "another large rollout" into a formal categorical severity rating that was never given. This is the same shape of problem this whole family of tools exists to catch, a real, stated concern read as more confident and certain, here upgraded to a formal "High" field value, than the evidence actually supports. It is a smaller, subtler version of the "at risk" labelling problem found earlier in a related audit of ai-for-commercial-teams, not identical, but the same underlying failure mode.
- **What a person still had to decide:** whether "High" is actually the right severity to log given only a stated caution, not a quantified risk, and what Shaun's own company name should be before the email signature is usable.
- **What this test cannot prove:** same caveat as the ChatGPT run, this went through the consumer product, not a raw API call, so it is not directly comparable in method to the Sonnet 5 versus Haiku 4.5 pair. One run, one case, one reviewer.
