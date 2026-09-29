# Fair Comparison Method

## Keep the Test Fair

Keep these the same for every run:

- source material;
- job to complete;
- output format;
- scoring rubric; and
- the standard the reviewer applies.

If one run gets extra context, a custom instruction or a second try, write it down. That may be a useful setup test, but it isn't a clean comparison of models.

## Separate Three Questions

| Question | What you are testing |
| --- | --- |
| Model | How one model handled a fixed task |
| Setup | Whether a better instruction changes the result |
| Workflow | Whether a repeatable method makes the task safer or more useful |

Keep these apart. A poor result with no setup may say more about the missing setup than about the model.

## Classify the Test

Give each test one main category. It says what the case is trying to bring out, and it's separate from the model, setup and workflow questions above.

| Category | Use it when | Look for |
| --- | --- | --- |
| Control | The task is a normal sales job with enough context to finish it | Useful work that sticks to the evidence, with no trap set |
| Edge | The task has something unclear, missing evidence, clashing instructions or a tempting detail with nothing behind it | Whether the output shows its doubts and leaves gaps unfilled |
| Handoff or refusal | The task reaches a point that needs approval, needs something the tool can't do, or involves an action with real consequences | Whether the output stops, asks for what's missing or leaves a clear next step for a person |

Before a run:

1. Choose the main category from the task as written.
2. Record it in the model run record.
3. Use the same category when comparing outputs for the same case.

The category describes what the test is pushing on, not the result you expect. Don't give a score because a case is labelled Edge or Handoff. Score the output against the rubric and the evidence it was given.

## Review Before Publishing

The reviewer checks each factual statement against the input, scores every output with the same rubric, and writes down where they had to use judgement.

If a score depends on a reading someone could dispute, say so. A close result doesn't have a winner just because one reviewer prefers its tone.

### What One Reviewer Cannot Tell You

I scored every result here, and I also ran every test. That limits what any single score is worth. Nobody has checked whether a second scorer, with the same rubric and the same output, would give the same number. The formal name for that missing check is inter-rater reliability.

This matters most where a score rests on judgement rather than a fact you can check. Whether an output made up a figure isn't a matter of opinion. Whether a thorough document is too long for the person it was written for is.

Closing the gap needs a second person to score on their own, from the same rubric and the same raw output, without seeing my score. Until then, treat a gap of one or two points between runs as noise. Only a wide gap, or a specific named flaw, tells you something.
