# Loop Control

Use for normal/large loops. Tiny work uses the compact path: facts, smallest correct change, check, review if needed, done.

## Ledger

```text
Objective:
Phase:
Source facts:
Assumptions / questions:
Mode: manual / controlled / automated
Available sensors:
Missing sensors:
State location:
Stall guard:
Hard stop:
Objective verifier:
Build/lint gate:
Simplicity gate:
Review gate:
Review gate discovery:
Human approval gate:
PR decision:
Post-push CI/CD:
Decision: done / continue / blocked_waiting_user / escalate / stop
```

## Qualification

- Manual: tiny, one-off, exploratory, weak verifier, or judgment-heavy.
- Controlled: current-session loop with ledger, hard stop, verifier or named gap, self-review, independent review, and human approval for irreversible work.
- Automated: recurring/event-driven/hands-off. Requires recurring value, objective verifier, runnable/observable environment, hard stop, persistent state, and human approval before merge/deploy/dependency/security-sensitive actions.

If any automated requirement is missing, downgrade to controlled/manual. A reviewer is not an objective verifier.

## Companion Skills

At start, compare companion skills named by the parent skill with the session's available skills. If a needed companion is missing, say `missing companion skill: $name; using inline fallback` and continue unless no safe fallback exists.

Use companion skills as helpers, not imports. The loop must still describe the fallback behavior inline.

## Required Gates

1. Intake: state objective and source facts.
2. Context: read local repo guidance before guessing conventions.
3. State: choose response-local ledger or persistent state for recurring/resumable work. Use `$loop-state-and-stall-guard` when available for durable state, resume context, and repeated-failure detection.
4. Simplicity: apply the Ponytail ladder before implementation or slicing: existing code, stdlib, native platform, installed dependency, one-line, then minimal new code. Do not cut explicit requirements, security, accessibility, trust-boundary validation, data-loss handling, or required checks.
5. Work: implement or produce the artifact.
6. Verify: run the original failure, acceptance example, source check, or closest practical proxy.
7. Build/lint: run build/typecheck/lint/compile or scoped equivalent when app code changed; record unavailable/too-costly gates and nearest proxy.
8. Simplicity review: use `$ponytail-review` if available; otherwise inline-check for needless dependency, abstraction, wrapper, dead flexibility, stdlib/native miss, or larger-than-needed diff/slice.
9. Correctness review: use reviewer subagent when available and allowed; inline fallback only after recording discovery/fallback evidence.
10. Repair: fix blocking findings and rerun affected verification/build gates. Before repeating the same failed gate, record the attempt and run the stall guard; switch strategy or ask when it triggers.
11. PR/CI: ask before opening PR unless already requested; after push/PR, monitor CI/CD when local pipeline coverage was incomplete and CI/CD exists, or record unavailable/delegated.
12. Security/comprehension: require human approval before merge, deploy, dependency changes, production writes, permission expansion, or sensitive code.
13. Decide: done, continue, blocked_waiting_user, escalate, or stop.
14. Learn: capture durable lessons only when useful for future runs.

## Human Input

Use `blocked_waiting_user` when progress needs information, authority, configuration, interpretation, or evidence the agent cannot safely obtain. Ask for the smallest safe action or artifact; never ask for secrets in chat.

```text
Blocked on:
Why it matters:
What I need:
Safe alternatives:
Resume point:
```

Do not continue past manual approval gates by guessing approval.

## Persistent State

Use persistent state for automated, scheduled, multi-thread, or resumable loops: repo markdown, issue/PR checklist, tracker item, vault note, or `$loop-state-and-stall-guard` state. Record last run, objective, current work, completed items, escalations, verifier results, review findings, lessons, and resume point.

## Stop Rules

Stop and ask when attempts stop producing new evidence, the stall guard reports repeated same-fingerprint failure, verification cannot progress, scope expands, budget/hard stop is reached, or the next step crosses a permission/irreversible boundary.

## Second Opinion

Use a second-opinion pass before implementation or finalization for architecture, security, data, financial, externally visible, irreversible, or business-critical boundaries.
