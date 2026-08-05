# Roadmap

## First Results

- ~~A cold comparison using the Hartwell follow up case~~ done: Claude Sonnet 5, Claude Haiku 4.5, ChatGPT and Gemini, see [results](results/README.md)
- A setup comparison showing cold versus a carefully scoped instruction
- A workflow comparison showing one off prompting versus a repeatable checklist

## Later Cases

- ~~Pre call preparation using public and supplied information~~ done: the Marlow case, a genuine cross-model comparison across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- ~~Objection diagnosis with ambiguous buyer wording~~ done: the Osmond case, a genuine cross-model comparison across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- Business case drafting with missing baseline evidence

## Guardrails Before Expansion

- Publish only fictional or clearly approved material
- Do not compare tools using changing or hidden context
- Do not claim a result means a model is generally best
- Keep failures visible
- Watch for an invented sender identity or other unrequested personal detail filling a gap a case does not specify; two independent Marlow runs showed this specifically
- Treat a consumer-app result as "this model plus whatever the account was carrying," never as a clean read on the model. Every flaw found across the Marlow and Osmond comparisons, invented signatures, an invented price figure, a self-contradicting outreach message, came from a consumer-app run with account-level context or defaults active, not from a raw API call or an isolated subagent. State the account's likely personalization or memory status plainly in the record rather than assuming a fresh chat means nothing is carried over
