# Roadmap

## First Results

- ~~A cold comparison using the Hartwell follow up case~~ done: Claude Sonnet 5, Claude Haiku 4.5, ChatGPT and Gemini, see [results](results/README.md)
- A setup comparison showing cold versus a carefully scoped instruction
- A workflow comparison showing one off prompting versus a repeatable checklist

## Later Cases

- ~~Pre call preparation using public and supplied information~~ done: the Marlow case, a genuine cross-model comparison across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- ~~Objection diagnosis with ambiguous buyer wording~~ done: the Osmond case, a genuine cross-model comparison across Sonnet 5, ChatGPT and Gemini, see [results](results/README.md)
- ~~Business case drafting with missing baseline evidence~~ done: the Elmsworth case, a genuine cross-model comparison across Sonnet 5, ChatGPT and Gemini, the cleanest result of any case so far, no run invented a figure, see [results](results/README.md)

All three cases originally listed here are now built. The next expansion here should come from real use exposing a genuine new trap, not from adding a fourth case for its own sake.

## Guardrails Before Expansion

- Publish only fictional or clearly approved material
- Do not compare tools using changing or hidden context
- Do not claim a result means a model is generally best
- Keep failures visible
- Watch for an invented sender identity or other unrequested personal detail filling a gap a case does not specify; two independent Marlow runs showed this specifically
- Treat a consumer-app result as "this model plus whatever the account was carrying," never as a clean read on the model. Every flaw found across the Marlow and Osmond comparisons, invented signatures, an invented price figure, a self-contradicting outreach message, came from a consumer-app run with account-level context or defaults active, not from a raw API call or an isolated subagent. State the account's likely personalization or memory status plainly in the record rather than assuming a fresh chat means nothing is carried over
- A case with explicit, itemised prohibitions (no percentage, no dollar figure, no hours, no satisfaction claim) produced zero invented figures across four runs and three models, the cleanest result of any case so far, compared with the subtler gap-filling traps in Marlow and Osmond (an unstated sender, an unstated price). When writing a new case, naming the specific forbidden claims explicitly, not just the general shape of the trap, appears to help; this is one small set of results, not a proven design rule
- Thoroughness is not the same as fitness for the case's own stated audience. A model can be maximally careful about evidence while still producing something too long for the person in the case to actually use, as ChatGPT's eleven-section Elmsworth response showed. Score usefulness against what the case's own fictional requester actually needs, not just against factual correctness
