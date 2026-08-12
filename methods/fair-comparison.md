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
