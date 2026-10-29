# Checklist test: scores written before unblinding

Scored on 29 October 2026, before I opened the file that says which clash run had the checklist. I could see which document each run had, because rule 3a is in the prompt.

I ran `scripts/score_refund_flaw_case.py` on each reply (A for the clash document, D for the clean one), then read every touched line and everything outside the answer lines.

## The clash document (12 runs)

- **Flagged the clash: 0 of 12.** No run named rule 3 and rule 3a, or "renewals aren't refundable" and "renewals are refunded", as disagreeing. Three notes mention both rules but treat them as fitting together: "rule 3 excludes renewals but rule 3a covers them", "rule 3 excludes renewals and points to rule 3a", and "rule 3a gives a full refund; rule 3 does not cover renewals". Under the reading I set in advance, that is no flag.
- **Approved both renewals: 12 of 12,** GBP 1,800 and GBP 1,200 to the Finance Manager.
- **Right on the requests no flaw touches: 13 of 13 in every run.**
- One run's text says it "worked through the checklist", so I know that one had it. I can't tell the rest apart from the replies.

## The clean document with the checklist (6 runs)

- **False alarms: 0 of 6.** No run said two rules disagree. One correctly said rules 5, 6 and 7 override rule 2, which is the exception step working as written.
- **Right on the requests no flaw touches: 12 of 12 in every run.** Request 15 was approved for the Support Lead at GBP 500 in all six.
- **Renewals:** request 14 was handed off in five runs and declined in one. Haiku handed it off in all six clean runs in the earlier test too.
