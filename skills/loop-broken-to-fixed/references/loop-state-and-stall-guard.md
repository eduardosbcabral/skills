# Loop State And Stall Guard

Use for resumable diagnosis, automation, external waits, or repeated failed hypotheses.

```text
Objective:
Phase:
Objective verifier:
Active hypothesis:
Evidence:
Blockers:
Last failure fingerprint:
Attempts with same fingerprint:
Next action:
Resume command or context:
```

Update after every meaningful hypothesis test. Before a retry, compare the failure fingerprint. On the third unchanged failure, discard or revise the hypothesis, change sensor, or request missing authority/context. Never count unchanged waiting state as new evidence.
