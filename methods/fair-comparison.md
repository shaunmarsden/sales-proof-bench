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

## Review Before Publishing

The reviewer checks each factual statement against the input. They score every output using the same rubric and write down where judgement was required.

If the score depends on a disputed interpretation, state that. A close result is not a winner just because one reviewer prefers its tone.
