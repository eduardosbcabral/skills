---
name: idea-to-program-loop
description: "Use when the user has a rough product idea, customer PDF/spec, meeting notes, large epic, or non-technical business request and wants to turn it into an executable software program of work: domain model, business rules, architecture boundaries, vertical slices, unknowns, harness sensors, and a first implementation goal. Do not use for a small already-specified code change or for a direct bug symptom."
---

# Idea To Program Loop

Turn rough intent into a controlled program of work: source facts, domain rules, vertical slices, evidence, and a first build goal.

## Companion Skills

At start, check whether companion skills are available in the session. If a step would use a missing companion, say `missing companion skill: $name; using inline fallback` once and continue. Treat missing companions as blocking only when no inline/tool fallback can satisfy the step.

- Simplicity: `$ponytail`, `$ponytail-review`.
- Direction/domain: `$grill-with-docs` (external companion), `$domain-modeling`, `$prototype`.
- Planning outputs: `$to-prd`, `$to-issues`, `$handoff`.
- Delivery/sensors: `$improve-codebase-architecture`, `$github:gh-fix-ci`, `$saas-backend-patterns`, `$saas-frontend-patterns`, relevant security skills.

## Start

1. Identify the input: idea, customer PDF/spec, notes, product gap, epic, or non-technical business request.
2. Classify: tiny, normal, or large/risky. Use `references/loop-control.md` for normal/large work, extended loops, automation, subagents, recurring work, or hands-off execution.
3. Use `$grill-with-docs` only when product direction, domain language, source facts, business decisions, or acceptance evidence are unclear enough that the loop would encode guesses.
4. If targeting a codebase, read local guidance before planning: `AGENTS.md`, README, docs, architecture notes, scripts, test conventions, and existing flows.
5. Load only needed references: `harness-contract.md` for sensors, `program-brief.md` for normal/large work, `loop-prompts.md` for prompts/review gates, and `self-review.md` before final completion.

## Loop

1. Separate source facts from assumptions, contradictions, unknowns, and decisions needed.
2. Extract actors, workflows, terms, rules, permissions, lifecycle states, integrations, data objects, and constraints.
3. Define harness evidence: source checks, local tests/CLI, build/typecheck/lint, browser paths, CI, logs/traces, docs, customer artifacts, or optional external sensors.
4. Record mode, state, objective verifier/acceptance evidence, hard stop, sensors, and human approval gates.
5. Apply the embedded Ponytail gate to planning: slice the smallest user-visible or system-verifiable program, reuse existing product/code/platform capability, and avoid speculative architecture. Never cut explicit customer rules, security, accessibility, data ownership, compliance, or required validation.
6. Produce a brief rule catalog, glossary, vertical slices, and first phase goal.
7. Self-review against source facts, assumptions, missing decisions, slice quality, and evidence.
8. Run the simplicity review gate: use `$ponytail-review` when code/artifacts exist, otherwise inline-check for overbuilt scope, unnecessary abstraction, premature platform work, or larger-than-needed first slice.
9. Run the correctness review gate: use `loop-rule-reviewer` for normal/large plans; inline fallback only after recording subagent discovery/fallback evidence.
10. Fix blocking review findings or expose unresolved decisions.
11. Create a concrete Codex goal only when the user asks for a goal or extended implementation loop.
12. If code changes are produced, run the build/lint gate when available and record gaps/proxies.
13. Ask before opening a PR unless already requested. After push/PR, monitor CI/CD when local pipeline coverage was incomplete and CI/CD exists, or record that CI/CD is unavailable/delegated.
14. Update persistent state only for automated, recurring, multi-thread, or resumable loops.
15. Stop for user input before billing, authorization, legal/compliance, data ownership, or core workflow semantics are decided by guess.
16. End with decision: done, continue, ask, escalate, or stop; include evidence, build/lint if code changed, simplicity review, correctness review, PR/CI status, state update, and open risks.

## Subagents

Use subagents only when they materially improve domain extraction, repo exploration, sensor inventory, slice planning, implementation, or independent review. Skip for tiny tasks and avoid parallel implementation until slice ownership is clear. Preferred agents: `loop-domain-extractor`, `explorer`, `loop-harness-sensor`, `loop-slice-planner`, `loop-rule-reviewer`, and `worker`. If unavailable, record the blocker and execute the role inline without pretending a separate review happened.

## Done

Done means: source facts, assumptions, and unknowns are separated; domain rules and slices are explicit enough for implementation; acceptance evidence is named; Ponytail/simplicity gate applied; self-review and review gates have no blocking findings; objective verifier or judgment gap is honest; build/lint and PR/CI are handled if code changed; state is updated if resumable; unresolved business decisions are named instead of hidden in code.
