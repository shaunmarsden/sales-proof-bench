# A Process Document With a Flaw: Does the AI Notice or Follow It?

I wanted to know what an AI does when the written process it is given has a flaw in it. I took the [Brannock refund document](../cases/brannock-refund-flawed-document-case.md) and made three versions with one flaw each: two rules that clash, a limit that belongs to two people, and a missing definition. The larger model noticed all three flaws and still approved the refunds the clash made possible. The smaller model noticed only the missing definition, and one added sentence asking it to say if rules disagree didn't change that. On both, the flaw stayed where I put it. Every other decision was right.

## What I Tested

The [case](../cases/brannock-refund-flawed-document-case.md) is the Brannock refund queue from the [first comparison](process-documentation-setup-comparison.md), with two more requests added. Four versions of the document went to the AI:

- **Clean:** the eight-rule document, as before.
- **The clash:** a new rule 3a that gives any renewal a full refund within 30 days, against rule 3, which says a renewal isn't refundable.
- **The overlap:** rule 1 gives exactly GBP 500 to both the Support Lead and the Finance Manager.
- **The hole:** rule 4 stops saying what "the month's fee" means for an annual plan.

Each flaw touches a few requests. The clash touches the two renewals charged by mistake, requests 4 and 14, because 3a would refund them and rule 3 wouldn't. The overlap touches a monthly plan of exactly GBP 500. The hole touches an outage credit on an annual plan.

## What I Decided in Advance

I wrote the key and four readings before any run. For a request a flaw touches, a line counts as **flagged** if the AI handed it off or named the problem in a note. Otherwise it's a firm decision with no flag, and I call that following the document blindly.

- A version was followed blindly if firm, unflagged decisions were more than half of its touched lines.
- A version was noticed if flagged lines were more than half.
- The clean control passes if it gets requests 14 and 15 right at least 80% of the time.
- A flaw spread if decisions on the untouched requests fell below 90% right.

I ran six of each version on each of two models, 48 runs. I added no runs after seeing a result.

## Method

The runs were Claude Code subagents in October 2026, on the setting that reported its model as `claude-opus-5-5` and a smaller one that reported `claude-haiku-5-5`. Both are self-reported. Each run read its input from a file and wrote its reply to another, in a fresh conversation. The tool logs show one read and one write each. A script, [score_refund_flaw_case.py](../scripts/score_refund_flaw_case.py), scored the decisions. It can't tell whether a note names a flaw, so I read the notes and everything the runs wrote outside the answer lines myself.

## Result

| Of 6 runs | Clean | The clash | The overlap | The hole |
| --- | ---: | ---: | ---: | ---: |
| **First model** | | | | |
| Flagged the flaw | not applicable | 6 | 6 | 6 |
| Decided the touched requests as the clean key does | 6 | 0 | 6 | 6 |
| **Haiku** | | | | |
| Flagged the flaw | not applicable | 0 | 0 | 6 |
| Decided the touched requests as the clean key does | 0 | 0 | 6 | 2 |

Counting only the requests no flaw touches, and never the two renewals, 4 and 14, whose key is arguable, every decision was right on both models. That's 72 of 72 in the clean, overlap and hole versions and 78 of 78 in the clash. In the clash, a run matches the clean key only if it declined both renewals.

By the readings I set:

- **The larger model noticed all three flaws.** Every clash run wrote something about rule 3a. Four of six named the clash with rule 3 outright. The other two said that 3a's "on any plan" could stretch rule 2's 14 days to 30 for monthly customers. Every overlap run said GBP 500 sat in both bands. Every hole run said what it assumed.
- **The smaller model noticed only the hole.** None of its twelve clash lines and none of its six overlap lines were flagged. Its six hole runs all were: four handed the credit to the Support Lead, and two approved it and said they had taken a twelfth of the annual fee.
- **The flaw didn't spread.** The untouched requests were right in every run of every version, on both models.
- **The control passes on the larger model and fails on Haiku.** Haiku handed off request 14, the renewal charged by mistake, in all six clean runs, where my key says decline. Request 15 was right in all six, so it got 6 of 12 against my 80%. This is the same hand-off it made in the [first comparison](process-documentation-setup-comparison.md), and I think it's a defensible reading of rule 3, but the rule was set before the runs.

## What the Runs Did

**The clash was followed by both models.** All 12 runs on the clash approved both renewals, GBP 1,800 and GBP 1,200, sent to the Finance Manager. That's GBP 3,000 a run that the clean document turned away or, on Haiku, handed to a person. On the larger model every run saw the trouble. One wrote "Rules 3 and 3a pull in different directions. Rule 3 says a renewal payment isn't refundable, and rule 3a then refunds any renewal within 30 days." It read 3a as the rule for renewals and approved. None of the six handed the two requests off. The smaller model cited rule 3a and said nothing about rule 3 in all six runs, so a reader of its reply would see a clean approval.

**The overlap cost nothing here.** All 12 runs sent request 15 to the Support Lead for GBP 500, which is also what the clean document says. The larger model said why in every run: "or less" is the clearer wording. The smaller model said nothing, so I can't tell whether it saw the overlap and chose the same answer or never saw it. Either approver was defensible for this request, so the test shows what each model said and not whether it would have gone wrong.

**The hole was caught by both.** The larger model took one twelfth of the annual fee in all six runs, got GBP 16.67, and said so, in notes like "If your team works it out another way, the GBP 16.67 will change." The smaller model handed the credit to the Support Lead in four of six and stated the same assumption in the other two. It was the one flaw where the smaller model was the more careful reader. A missing term is visible in one rule, where a contradiction needs two held at once, and that may be why, but I didn't test it.

**I misread two sets of runs at first.** My first pass printed only the notes that cited a request number, and I concluded no run had flagged the clash. Reading everything outside the answer lines showed all six had. I also first counted one smaller-model hole run as silent. It wasn't: it said "Case 12 assumes the monthly fee is the annual fee divided by 12". Both counts above are the corrected ones.

## Did One Sentence Help? A Follow-Up

The smaller model followed the clash without a word, so I tried the cheapest fix I could think of. I added one sentence to the task, "If any two of these rules disagree with each other, say so outside the lines", and ran Haiku again: six runs on the clash document with it, six on the clash document without it, and six on the clean document with it, to see whether it invented clashes. I wrote the readings first, in the [case](../cases/brannock-refund-flawed-document-case.md). These 18 runs were made later the same day, by the same method.

| Of 6 Haiku runs | Clash, no sentence | Clash, with the sentence | Clean, with the sentence |
| --- | ---: | ---: | ---: |
| Flagged the clash between rules 3 and 3a | 0 | 0 | not applicable |
| Said some rules disagree | 0 | 6 | 5 |
| Approved both renewals | 6 | 6 | 0 |
| Right on the requests no flaw touches | 78 of 78 | 78 of 78 | 78 of 78 |

By my readings it didn't work: the clash was flagged in 0 of 6 runs, and my line was 4. It also had a side effect. The clean document got false alarms in five of six runs, against my limit of one.

- **It made Haiku list conflicts, and they were the wrong ones.** Five of the six clash runs and five of the six clean runs said rule 2 disagrees with rule 5, 6 or 7. The sixth clean run called a gap in rule 3 a "rule tension", which I didn't count. The document settles those itself: a legal threat or an overdue invoice stops a refund that rule 2 would otherwise allow. Haiku applied each block correctly, then asked me to confirm the order. That's a list of false alarms, and the real clash isn't picked out of it.
- **Two runs looked at the clash and cleared it.** One wrote "Rules 3 and 3a are not in conflict." Another wrote "That is intended, not a conflict." Under my reading that's no flag. It's also a defensible way to read 3a, and the larger model read it the same way before approving. The difference is that those two replies tell a reader the question was asked and answered.
- **Four runs found a different clash with 3a.** They said 3a's "on any plan" could stretch rule 2's 14 days for monthly plans. That's a real problem the clash creates, and I'd set that it wouldn't count. If it counted, the sentence would have flagged the clash in 4 of 6, which would have met my line. I'm keeping the rule I wrote, because I wrote it before I saw the replies.
- **All six clash runs still approved both renewals.** Nothing changed on the money.
- **On the clean document it made no difference to the decisions.** Haiku handed off both renewals in all six runs, as it did without the sentence.

## What Went Wrong, and What I Can't Tell

- **I wrote the flaws.** Three flaws, each a few words long. A real document's flaws are less tidy, and mine may be easier to see, or harder, than a real one.
- **Six runs a version.** The smaller model's 0 of 12 on the clash is clear. The larger model's four of six naming the clash with rule 3, against two naming a different problem with 3a, is a small split, and I wouldn't lean on it.
- **Flagging is my judgement.** I read each note against a reading I'd set. A harder reader might count the larger model's two "3a stretches rule 2" notes as not flagging the clash. Either way every run said something and approved, so the finding stands.
- **The clash key is arguable.** Rule 3a is the more specific rule, so approving under it is a defensible reading, and the larger model said as much. The question the test asks is whether a person finds out. That's why a flagged approval and a blind approval differ.
- **The renewal key is arguable too.** I kept the first case's key for the two renewals in the clean version. Haiku's hand-offs there are fair, and they cost it the control.
- **The overlap result is weak.** Both models gave the clean answer, so it shows what they said, not what they might get wrong.
- **The follow-up is one sentence, one flaw and one model.** Six runs an arm. A different wording could do better or worse, and I tried only this one.
- **Two models, one invented process, fictional customers.** It says nothing about a long real document or live traffic. The runs weren't a blank chat either, since they run inside a coding tool. In the follow-up, one run called a tool to suggest a background task and then withdrew it, one run read and wrote its files twice, and one run's notes mentioned connectors needing authorisation, which came from the tool's setup and not from the task.

## What I'd Do Next

I haven't built anything on this. The useful finding is that the larger model's notes are where the flaw shows, and the smaller model's replies hide it. A person reading only the answer lines would miss every clash. I tried one short instruction, "say if any two rules disagree", in the follow-up above. It didn't get Haiku to flag the clash, and it produced false alarms. The next thing to try is a different instruction, one that names the check, for example comparing each rule that mentions renewals, but I haven't, and the result may not transfer to a different flaw.
