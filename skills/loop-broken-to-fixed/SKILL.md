---
name: loop-broken-to-fixed
description: "Use when the user reports an exception, stack trace, failed CI check, broken behavior, browser failure, production error, performance regression, or other symptom and wants a diagnosis-to-fix loop with reproduction, sensor collection, smallest safe fix, and regression evidence. Do not use for vague product discovery or for a fully specified feature rule with no failure symptom."
---

# Broken To Fixed Loop

Run a controlled diagnosis loop from symptom to verified root-cause fix.

## Strict Execution Contract

When this skill triggers, follow the gates below exactly. Do not silently skip a gate.

Before editing files, running a deploy, committing, pushing, or opening a PR, emit a short `Loop checkpoint` with:

- loop type and classification: tiny, normal, or large/risky
- captured symptom and expected verifier
- whether `$grill-with-docs` is required, completed, or explicitly skipped with a reason
- whether the user is asking for conversation/refinement only or authorizing implementation
- PR decision: not requested, ask later, or already requested

Hard stops:

- If the user says they are only discussing, refining, asking "what do you think", or asking for suggestions, do not implement. Answer, inspect, or ask the next question only.
- If the fix changes expected behavior, contracts, data, permissions, UX, core rules, or product semantics, `$grill-with-docs` is mandatory before implementation unless the change is truly tiny and cause-specific. If skipped, state the concrete tiny-skip reason in the checkpoint.
- If the work changes from bug diagnosis into a feature or business-rule change, switch to `$loop-change-to-done` and run its start gates before implementation.
- Ask before opening a PR unless the user has already explicitly requested a PR.

Final response must include a compact gate report: symptom/root cause, verifier, build/lint, `$grill-with-docs` status, simplicity review status, correctness review status, PR/CI status, and residual risk.

## Companion Skills

At start, check whether companion skills are available in the session. If a step would use a missing companion, say `missing companion skill: $name; using inline fallback` once and continue. Treat missing companions as blocking only when no inline/tool fallback can satisfy the step.

- Simplicity: `$ponytail`, `$ponytail-review`.
- Token efficiency: `$rtk-token-saver` (optional; compact noisy shell output when RTK is installed and exact raw output is not required).
- State/stall: `$loop-state-and-stall-guard` (optional; persist resumable loop state and detect repeated failed attempts).
- Diagnosis/direction: `$diagnosing-bugs`, `$grill-with-docs` (external companion), `$prototype`.
- Delivery/sensors: `$github:gh-fix-ci`, relevant security skills.
- Resumption: `$handoff` only when the loop must pause, move, or survive context loss.

## Start

1. Capture the exact symptom: error text, stack trace, failing check, URL/action, timestamp, environment, impact, and expected behavior.
2. Classify: tiny, normal, or large/risky. Use `references/loop-control.md` for non-tiny work, extended loops, automation, subagents, recurring work, or hands-off execution.
3. Schedule and report the solution discussion gate: reproduce or bound the failure first, then use `$grill-with-docs` before implementation when the fix changes expected behavior, contracts, data, permissions, UX, core rules, or risky direction. For tiny cause-specific fixes with clear expected behavior, skip this gate only after naming the skip reason in the `Loop checkpoint`.
4. In a codebase, read local guidance before diagnosis: `AGENTS.md`, README, docs, runbooks, architecture notes, scripts, test conventions, and nearby implementations.
5. Load only needed references: `harness-contract.md` for sensors, `diagnosis-ledger.md` for non-tiny/competing hypotheses, `loop-prompts.md` for prompts/review gates, and `self-review.md` before final completion.

## Loop

1. Reproduce or bound the failure with a local test, command, browser flow, CI log, trace, or artifact.
2. Track one evidence-backed hypothesis at a time and name its falsification step.
3. Use `$rtk-token-saver` for noisy test/log/CI summaries when available; switch to raw output for exact stack traces, compiler diagnostics, snapshots, traces, or security detail.
4. Record mode, state, objective verifier, hard stop, sensors, and human approval gates; use `$loop-state-and-stall-guard` for resumable diagnosis or repeated failed hypotheses.
5. Inspect the smallest relevant code path and caller set before editing.
6. Apply the embedded Ponytail gate: fix once at the shared root cause, prefer existing code/stdlib/native/installed dependency, and avoid broad refactors. Never choose a tiny diff that only patches the named symptom while sibling paths remain broken.
7. Patch the smallest cause-specific fix.
8. Self-review against root cause, scope, edge cases, regression evidence, and project conventions.
9. Verify the original symptom is gone and add or identify regression evidence.
10. Run the build/lint gate for app code when available; record unavailable/too-costly gates and nearest proxy.
11. Run the simplicity review gate: use `$ponytail-review` when available, otherwise inline-check for unnecessary dependency, abstraction, wrapper, dead flexibility, stdlib/native miss, or larger-than-needed diff.
12. Run the correctness review gate: use `loop-rule-reviewer` for normal/risky code, data, permission, concurrency, performance, or regression changes; inline fallback only after recording subagent discovery/fallback evidence.
13. Fix blocking review findings, then rerun the original symptom or affected regression/build gates; before retrying the same failure repeatedly, run the stall guard and switch hypothesis if it triggers.
14. Ask before opening a PR unless already requested. After push/PR, monitor CI/CD when local pipeline coverage was incomplete and CI/CD exists, or record that CI/CD is unavailable/delegated.
15. Update persistent state only for automated, recurring, multi-thread, or resumable loops.
16. End with decision: done, continue with a new hypothesis, ask, escalate, or stop; include root cause, verifier, build/lint, `$grill-with-docs` status, simplicity review, correctness review, PR/CI status, state update, and residual risk.

## Subagents

Use subagents only when they materially improve diagnosis, sensor collection, implementation, or independent review. Skip for tiny fixes and avoid parallel write-heavy edits. Preferred agents: `loop-bug-diagnoser`, `loop-harness-sensor`, `explorer`, `worker`, and `loop-rule-reviewer`. If unavailable, record the blocker and execute the role inline without pretending a separate review happened.

## Done

Done means: root cause is evidence-backed or uncertainty is explicit; smallest safe fix is applied; symptom or mitigation is verified; regression evidence exists or gap is named; Ponytail/simplicity gate applied; self-review and review gates have no blocking findings; objective verifier and build/lint gate are recorded; PR/CI decision is handled when relevant; state is updated if resumable; risky follow-up is separated from the fix.
