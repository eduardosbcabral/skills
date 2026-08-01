---
name: loop-idea-to-build
description: "Use when the user has a rough product idea, customer document, meeting notes, large epic, or non-technical request and wants a clear, executable build path. Produces settled rules, acceptance evidence, vertical slices, and a Change To Done contract. Do not use for an already-specified change or a concrete failure symptom."
---

# Idea To Build Loop

Move from rough intent to one executable change contract.

## State Contract

- **Input:** an idea, document, notes, product gap, epic, or ambiguous business request.
- **Output:** a settled first vertical slice with rules, boundaries, acceptance evidence, and verifier.
- **Next state:** `Change To Done`. If the user only wants discussion, stop with the clarified model and open decisions.
- **Not done:** unresolved decisions are hidden as implementation assumptions.

Conversation and analysis do not authorize edits. Implementation, commit, push, PR, deploy, destructive operations, credentials, and external writes require the user's request or approval appropriate to that action.

## Optional Dependency

Before shell-heavy work, load and follow `$rtk-token-saver` when the skill and its external RTK CLI are available. It is an optional operational dependency, not a companion or embedded behavior. Use its current availability, fallback, fidelity, safety, and verification rules as the source of truth. If unavailable, continue with normal commands; do not install or configure RTK without explicit approval.

## Start

1. Read relevant user-provided sources. In a repository, also read local guidance and the smallest useful set of docs, architecture notes, tests, and existing flows.
2. Separate facts, assumptions, contradictions, unknowns, and decisions.
3. Classify the work:
   - **tiny:** intent and first slice are already clear;
   - **normal:** a few product or domain decisions remain;
   - **risky:** auth, money, data ownership, destructive behavior, compliance, public contracts, or core workflow semantics are involved.
4. For normal/risky ambiguity, use `references/batch-grill-me.md`. Do not interview when repository evidence can answer the question.
5. For normal/risky work, keep the compact record in `references/program-brief.md`.

## Built-in Operating Rules

### Ponytail

Understand the real flow, then choose the first option that works: delete the need, reuse existing code, use the standard library, use the native platform, use an installed dependency, solve it in one line, or write the minimum new code. Do not cut explicit rules, trust-boundary validation, security, accessibility, data-loss handling, or required evidence.

### Ponytail Review

Before declaring the slice ready, look only for removable complexity: `delete`, `stdlib`, `native`, `yagni`, or `shrink`. If none applies, record `Lean already. Ship.`

### Caveman

Keep progress and final prose terse: remove filler, hedging, pleasantries, repeated summaries, tool narration, decorative tables, emoji, and long raw logs. Fragments are fine. Preserve the user's language and preserve code, commands, API names, identifiers, and exact errors. Do not invent abbreviations or sacrifice clarity for security warnings, irreversible confirmations, ambiguity, or multi-step instructions.

## Subagents

Delegate bounded, important work when the role is useful; the parent owns synthesis and decisions.

- `loop-domain-extractor`: extract facts, rules, workflows, unknowns, and contradictions from substantial or ambiguous source material.
- `loop-harness-sensor`: collect independent evidence from tests, CLI, browser, CI, logs, traces, or connected tools.
- `loop-slice-planner`: turn a settled normal/risky model into vertical slices and a first executable goal.
- `loop-rule-reviewer`: independently review the final contract, plan, or implementation against sources, rules, scope, acceptance evidence, and regression risk.

For normal/risky work, delegated `loop-rule-reviewer` review is required before Done. For tiny work, skip it only with a concrete reason. If a named custom agent is unavailable but subagents are supported, use a built-in `default` or `explorer` agent with the same bounded role and record the fallback. If no subagent facility exists, report the review gap instead of claiming delegated review passed. Do not delegate business decisions or allow parallel write ownership to overlap.

## Loop

1. Extract actors, workflows, terms, rules, permissions, lifecycle states, data objects, integrations, and constraints that matter to the first slice.
2. Resolve only currently unblocked decisions. Use evidence first; use Batch Grill Me for the remaining decision frontier.
3. Name acceptance evidence before architecture: examples, focused tests, CLI/API/browser checks, build/typecheck/lint, logs, customer artifacts, or another observable sensor.
4. Design the smallest vertical slice that delivers a user-visible or system-verifiable outcome. Keep future slices out.
5. Write the transition contract:

```text
Objective:
Actor and trigger:
Expected behavior:
Rejected behavior:
Acceptance examples:
Scope / out of scope:
Verifier:
Deferred decisions:
```

6. Run Ponytail Review, then delegate correctness review according to the Subagents contract. Fix blocking findings and re-review affected areas.
7. If implementation was requested, transition into Change To Done and execute the contract. Otherwise, return the contract and stop.

## Conditional Modes

- Use `references/loop-state-and-stall-guard.md` only for resumable, automated, multi-session, external-wait, or repeated-failure work.
- `prototype`: build a throwaway executable only when behavior cannot be settled cheaply in prose, examples, or existing code.
- `to-prd`: reshape the settled model as a PRD only when requested.
- `to-issues`: split settled slices into independently grabbable issues only when requested.
- `handoff`: write a resumption packet only when the work must move or pause.

These are built-in modes, not installed-skill dependencies.

## Done

Done means the first slice has settled rules, explicit boundaries, acceptance evidence, a verifier, and no hidden business decision. Report the outcome, evidence, deferred decisions, residual risk, and next state. Do not force implementation or delivery work that was not requested.
