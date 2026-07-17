# Loop State And Stall Guard

Use only for resumable, automated, multi-session, external-wait, or repeated-failure work.

```text
Objective:
Phase:
Objective verifier:
Completed gates:
Blockers:
Last failure fingerprint:
Attempts with same fingerprint:
Next action:
Resume command or context:
```

Update the record after a meaningful attempt. Before repeating a failed gate, compare its fingerprint. On the third unchanged failure, switch strategy or request the missing authority/context. Do not replay the same action.
