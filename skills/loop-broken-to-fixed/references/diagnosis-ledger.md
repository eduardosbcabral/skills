# Diagnosis Ledger

Use this for non-tiny failures, competing hypotheses, or risky fixes.

## Capture

```text
Symptom:
Expected behavior:
Actual behavior:
Environment:
Trigger/action:
First seen:
Impact:
Available artifacts:
Missing sensors:
Execution mode:
Objective verifier:
Hard stop:
```

## Hypotheses

Track one hypothesis at a time:

```text
Hypothesis:
Why plausible:
Evidence for:
Evidence against:
Falsification step:
Result:
Decision: keep / discard / refine
```

## Fix Record

```text
Root cause:
Change made:
Why this is the smallest safe fix:
Regression evidence:
Checks run:
Simplicity gate:
Build/lint gate:
Review gate:
PR decision:
Post-push CI/CD:
State location:
Residual risk:
Follow-up, if any:
```

## Stop Conditions

Stop and ask for user input when:

- the issue cannot be reproduced and no useful artifact is available;
- the next step requires production access, credentials, or destructive operations;
- the likely fix changes data ownership, billing, auth, security, migrations, or public contracts;
- evidence points to an external service or deployment state that cannot be inspected locally.
