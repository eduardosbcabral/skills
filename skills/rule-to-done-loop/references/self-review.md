# Self-Review

Use this before declaring an implementation complete. This is the agent reviewing its own work, separate from external reviewer agents.

## Implementation Review

Check:

- Does the implementation satisfy the stated rule and acceptance examples?
- Are positive, negative, and boundary cases handled where relevant?
- Did the change follow nearby project patterns?
- Is the implementation scoped to the requested behavior?
- Did the Ponytail/simplicity gate avoid unnecessary dependencies, abstractions, wrappers, files, or speculative flexibility?
- Are auth, permissions, billing, data ownership, migrations, validation, and UI/API contracts considered when relevant?
- Are tests or focused checks aligned with the rule?
- Did the change introduce unrelated refactors or documentation churn?

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
