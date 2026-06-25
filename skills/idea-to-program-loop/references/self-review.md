# Self-Review

Use this before declaring a program brief, slice plan, or implementation goal complete. This is the agent reviewing its own work, separate from external reviewer agents.

## Program Review

Check:

- Are source facts separated from assumptions?
- Are contradictions and unknowns visible?
- Are actors, workflows, domain terms, business rules, permissions, states, and integrations captured at the right level?
- Are slices vertical and independently verifiable?
- Does the first implementation goal avoid promising a giant one-shot build?
- Did the Ponytail/simplicity gate keep the first slice and technical plan as small as the source facts allow?
- Are evidence and sensors realistic for the target repo/environment?
- Are billing, auth, legal/compliance, data ownership, and core workflow decisions gated for user input when unclear?
- Did the plan invent product decisions not supported by source material?

## Finding Handling

For each self-review finding:

```text
Finding:
Evidence:
Decision: fix now / defer / needs user input / not an issue
Reason:
```

Fix blocking findings before presenting the program. Convert unresolved business decisions into explicit questions or stop conditions.

## Completion Statement

In the final summary, include one concise line:

```text
Self-review: no blocking findings / fixed findings: ... / needs user input: ...
```
