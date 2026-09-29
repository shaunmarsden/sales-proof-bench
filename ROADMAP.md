# Roadmap

## First Results

- ~~A cold comparison using the Hartwell follow up case~~ done: Claude Sonnet 5, Claude Haiku 4.5, ChatGPT and Gemini, see [results](results/README.md)
- A setup comparison: no instruction against a carefully scoped one
- A workflow comparison: one-off prompting against a repeatable checklist

## Later Cases

- ~~Pre call preparation using public and supplied information~~ done: the Marlow case, compared across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- ~~Objection diagnosis with ambiguous buyer wording~~ done: the Osmond case, compared across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- ~~Business case drafting with missing baseline evidence~~ done: the Elmsworth case, compared across Sonnet 5, ChatGPT and Gemini. It's the cleanest result of any case so far: no run made up a figure. See [results](results/README.md)

I've now built all three cases this list started with. The next one should come from real use turning up a new trap, not from adding a fourth case for the sake of it.

## Guardrails Before Adding More

- Publish only fictional or clearly approved material.
- Don't compare tools when the context is changing or hidden.
- Don't claim a result means a model is best overall.
- Keep failures visible.
- Watch for a made-up sender name, or other personal detail nobody asked for, filling a gap the case leaves open. Two separate Marlow runs did this.
- Treat a consumer-app result as "this model plus whatever the account was carrying," never as a clean read on the model. Every flaw I found across the Marlow and Osmond comparisons came from a consumer-app run with account settings or memory switched on, not from a raw API call or an isolated subagent. Those flaws were made-up signatures, a made-up price and an outreach message that contradicted itself. Say plainly in the record whether the account probably had personalisation or memory on. Don't assume a fresh chat carries nothing over.
- A case that lists exactly what not to claim (no percentage, no dollar figure, no hours, no satisfaction claim) got no made-up figures across four runs and three models. That's the cleanest result of any case so far. Marlow and Osmond set subtler traps, where the model had to notice a gap on its own (a sender nobody named, a price nobody gave). So when you write a new case, naming the claims it forbids, not just the kind of trap, seems to help. This is one small set of results, not a proven rule.
- Thorough isn't the same as useful to the person in the case. A model can be as careful as possible with evidence and still write something too long for that person to use, as ChatGPT's eleven-section Elmsworth answer showed. Score usefulness against what the case's fictional requester needs, not just against whether the facts are right.
