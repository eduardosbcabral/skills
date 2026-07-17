# Loop State And Stall Guard

Use only for resumable, automated, multi-session, external-wait, or repeated-failure work.

Keep one compact state record:

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

After each meaningful attempt, update evidence and next action. Before repeating a failed gate, compare the failure fingerprint. On the third unchanged failure, switch hypothesis, sensor, implementation point, or ask for the missing authority/context. Do not replay the same action.
