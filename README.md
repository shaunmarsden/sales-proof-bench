# Sales Proof Bench

If two AI tools give different answers to the same sales task, which one is better?

This is how I test that. Every model gets the same fictional input, the same job and the same scorecard. I record what each one did well, what it made up, what still needs a person, and where the test is too small to prove anything.

It isn't a leaderboard. A model can be good at drafting a follow-up and poor at showing its assumptions. The point is to show that.

## Start Here

| If you want to... | Open this |
| --- | --- |
| Understand a fair comparison | [Fair Comparison Method](methods/fair-comparison.md) |
| Run the first fictional case | [Hartwell Follow Up Case](cases/hartwell-follow-up-case.md) |
| Run the pre-call prep case | [Marlow Pre-Call Case](cases/marlow-pre-call-case.md) |
| Run the objection diagnosis case | [Osmond Objection Diagnosis Case](cases/osmond-objection-diagnosis-case.md) |
| Run the business case drafting case | [Elmsworth Business Case Case](cases/elmsworth-business-case-case.md) |
| Score an output | [Sales Output Rubric](rubrics/sales-output-rubric.md), which I wrote and no organisation endorses |
| Score a run in your browser | [Score a Run Yourself](https://shaunmarsden.github.io/sales-proof-bench/) |
| Record a model run | [Model Run Record](templates/model-run-record.md) |
| See the results so far | [Results](results/README.md) |

## The Rules

1. Use the same source input for every run.
2. Keep the task request the same.
3. Record the model, the date and anything about the setup that matters.
4. Score the output against the evidence, not against how sure it sounds.
5. Show failures and limits as clearly as strengths.
6. Never turn a fictional test into a claim about real sales results.

[![A fair AI sales comparison](assets/diagrams/27-sales-proof-bench.svg)](methods/fair-comparison.md)

## What This Can Tell You

- Whether one output stuck closer to the evidence it was given
- Whether it gave useful questions, actions or drafts
- Whether it kept doubts visible
- Whether a setup instruction improves a repeated task. No published run has tested this yet: every record here gives its setup instruction as none, unknown or a consumer account with nothing attached

## What This Cannot Tell You Alone

- Which model is best overall
- Whether a model will raise revenue
- Whether an output is safe for every customer situation
- Whether an organisation has approved a tool
- Whether a small score difference is real. I scored everything here myself, against a rubric I wrote, with no second scorer, so a gap of one or two points is noise. [What one reviewer cannot tell you](methods/fair-comparison.md#what-one-reviewer-cannot-tell-you) explains why, and the [results](results/README.md) say which gaps are wide enough to mean something.

## Current Status

The bench has four fictional cases: Hartwell Follow Up, Marlow Pre-Call, Osmond Objection Diagnosis and Elmsworth Business Case. Four models have run every case: Claude Sonnet 5, Claude Haiku 4.5, ChatGPT and Gemini. Sonnet 5 also has second attempts and consumer-app versions, so Hartwell has five results, Marlow six, and Osmond and Elmsworth five each. That's 21 in all. The [results](results/README.md) say what these show and what they don't.

The [roadmap](ROADMAP.md) lists the next tests.

## Disagree With a Score

I've scored everything here myself, and nobody else has scored anything. [Score one run yourself](feedback/score-a-run-yourself.md) is the easiest way to change that. It's one output and one rubric, and takes about 15 minutes. You only see my score after you've written yours. The [browser version](https://shaunmarsden.github.io/sales-proof-bench/) adds up your scores as you go, then shows mine next to yours, area by area. It also names the three of my nine scores that I never gave a reason for. Those are the easiest three to argue with.

## Feedback

Tried this? [Share feedback in the short form](https://github.com/shaunmarsden/sales-proof-bench/issues/new?template=feedback.yml) if something helped, was unclear, or you'd like to see something next. See [what the form asks](feedback/README.md) before you start.

## Part of a Family

These are four free tools for sales teams trying out AI. Each builds on ideas from [Practical AI Sales Workflows](https://github.com/shaunmarsden/practical-ai-sales-workflows). New to all four? Start with [AI for Commercial Teams](https://github.com/shaunmarsden/ai-for-commercial-teams), which covers getting a whole team started. [Sales Value Workshop](https://github.com/shaunmarsden/sales-value-workshop) turns a vague idea into a first test. This one tests whether a tool helps with a task. [Sales Conversation Gym](https://github.com/shaunmarsden/sales-conversation-gym) is for practising the conversations themselves.

My method for comparing models here builds on the one I ran and scored in Practical AI Sales Workflows' [evaluations](https://github.com/shaunmarsden/practical-ai-sales-workflows/tree/main/evaluations). The next case here should extend that work, not repeat it.
