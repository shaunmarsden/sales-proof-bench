# Sales Proof Bench

If two AI tools produce different answers to the same sales task, which one is better?

This project is a transparent way to test that question. It uses the same fictional input, the same requested job and the same scorecard. It records what the model did well, what it invented, what still needs a person and where the test is too limited to prove anything useful.

It is not a leaderboard. A model can be good at drafting a follow up and poor at making assumptions visible. The point is to make that visible.

## Start Here

| If you want to... | Open this |
| --- | --- |
| Understand a fair comparison | [Fair Comparison Method](methods/fair-comparison.md) |
| Run the first fictional case | [Northstar Follow Up Case](cases/northstar-follow-up-case.md) |
| Score an output | [Sales Output Rubric](rubrics/sales-output-rubric.md) |
| Record a model run | [Model Run Record](templates/model-run-record.md) |
| See what results are ready | [Results](results/README.md) |

## The Rules

1. Use the same source input for every run.
2. Keep the task request the same.
3. Record the model, date and any relevant setup.
4. Score the output against the evidence, not how confident it sounds.
5. Show limitations and failures as clearly as strengths.
6. Never turn a fictional test into a claim about real commercial impact.

## What This Can Tell You

- Whether one output was better grounded in the supplied evidence
- Whether it made useful questions, actions or drafts
- Whether it kept uncertainty visible
- Whether a setup instruction improved a repeated task

## What This Cannot Tell You Alone

- Which model is universally best
- Whether a model will improve revenue
- Whether an output is safe for every customer situation
- Whether a tool is approved by an organisation

## Current Status

The bench foundation and first fictional case are ready. No public model score has been published yet. A result should appear only when the full input, output, score and limitations can be shown together.

See the [roadmap](ROADMAP.md) for the next tests.
