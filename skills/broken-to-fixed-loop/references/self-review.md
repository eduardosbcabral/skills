# Self-Review

Use this before declaring a fix complete. This is the agent reviewing its own work, separate from external reviewer agents.

## Patch Review

Check:

- Does the change address the stated root cause rather than only hiding the symptom?
- Is the fix the smallest safe change?
- Did the Ponytail/simplicity gate avoid unnecessary dependencies, abstractions, wrappers, files, or speculative flexibility?
- Did the change stay within the intended scope?
- Are affected edge cases considered?
- Are auth, permissions, billing, data ownership, migrations, security, and concurrency risks considered when relevant?
- Does the regression evidence actually exercise the original symptom or closest practical proxy?
- Did the change introduce unrelated refactors or cleanup?

## Finding Handling

For each self-review finding:

```text
Finding:
Evidence:
Decision: fix now / defer / not an issue
Reason:
```

Fix blocking findings before final verification. If deferring a finding, name it as residual risk.

## Completion Statement

In the final summary, include one concise line:

```text
Self-review: no blocking findings / fixed findings: ... / residual risk: ...
```
