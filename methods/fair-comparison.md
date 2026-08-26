# Fair Comparison Method

## Keep the Test Fair

Use exactly the same:

- source material;
- job to complete;
- output format;
- scoring rubric; and
- human reviewer standard.

If one run gets extra context, a custom instruction or a second attempt, log it. That may be a useful setup test, but it is not a clean model comparison.

## Separate Three Questions

| Question | What you are testing |
| --- | --- |
| Model | How one model handled a fixed task |
| Setup | Whether a better instruction changes the result |
| Workflow | Whether a repeatable method makes the task safer or more useful |

Do not blur these together. A poor cold run may say more about the missing setup than the model.

## Classify the Test

Use one primary category for each test. This describes what the case is trying to reveal. It is separate from the model, setup and workflow questions above.

| Category | Use it when | Look for |
| --- | --- | --- |
| Control | The task is a normal sales job with enough supplied context to complete it | Grounded, useful work without a deliberate trap |
| Edge | The task contains ambiguity, missing evidence, conflicting instructions or a tempting unsupported detail | Whether the output makes uncertainty visible and resists filling gaps |
| Handoff or refusal | The task reaches an approval boundary, needs a missing capability or involves a consequential action | Whether the output stops, asks for what is missing or leaves a clear human next step |

Before a run:

1. Choose the primary category from the task as written.
2. Record it in the model run record.
3. Use the same category when comparing outputs for the same case.

A category describes the test pressure, not the expected result. Do not award a score because a case is labelled Edge or Handoff. Score the output against the rubric and the supplied evidence.

## Review Before Publishing

The reviewer checks each factual statement against the input. They score every output using the same rubric and write down where judgement was required.

If the score depends on a disputed interpretation, state that. A close result is not a winner just because one reviewer prefers its tone.

### What One Reviewer Cannot Tell You

Every result published here was scored by one person, and that person also ran the test. This is a real limit on what any single score carries, and it has a name: there is no inter-rater reliability check, meaning nobody has tested whether a second scorer, given the same rubric and the same output, would arrive at the same number.

It matters most where a score rests on judgement rather than a checkable fact. Whether an output invented a figure is not a matter of opinion. Whether a thorough document is too long for the audience it was written for is.

Closing the gap needs a second person scoring independently, from the same rubric and the same raw output, without seeing the first score. Until that happens, treat a one or two point difference between runs as inside the noise, and treat only a wide gap, or a specific named flaw, as telling you something.
