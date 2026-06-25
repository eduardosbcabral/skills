# Loop Prompts

Use only for non-tiny, risky, worker, or reviewer steps.

## Self Prompt

```text
Goal:
Facts/evidence:
Mode/state/hard stop:
Scope/files:
Constraints:
Simplicity path:
Verifier + build/lint:
Sensors:
Human/PR/CI gates:
Return:
```

## Worker Prompt

```text
Use the current loop skill for this bounded task.
Task:
Own:
Constraints:
Simplicity path:
Evidence required:
Do not touch:
Return:
```

## Reviewer Prompt

```text
Review against the loop objective. Return actionable findings only.
Check: correctness, rule/root-cause/source facts, edge cases, verification, build/lint, simplicity/overbuilding, state/resume, PR/CI, scope, security, permissions, comprehension debt.
```

Keep prompts bounded by facts, ownership, evidence, and stop conditions. For tiny tasks, skip explicit prompt synthesis.
