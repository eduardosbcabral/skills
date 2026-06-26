---
name: loop-state-and-stall-guard
description: "Use as an optional companion for long, resumable, automated, repeated, or failure-prone engineering loops that need durable on-disk state, attempt journaling, resume context, and stall detection. Do not use for tiny one-shot tasks unless the user asks for resumability or the same verification failure repeats."
metadata:
  short-description: Persist loop state and detect repeated stalls
---

# Loop State And Stall Guard

Keep long loops from forgetting, restarting, or repeating the same failed approach. For tiny one-shot work, do nothing.

## When To Use

Use this only when one applies:

- The task is automated, scheduled, multi-thread, or explicitly resumable.
- The task spans multiple iterations, PR/CI waits, external sensors, or a Codex goal.
- A verifier fails repeatedly and the next attempt risks repeating the same approach.
- The user asks to continue later or preserve the loop state.

## State Location

Prefer an existing project state location if present. Otherwise use `.agent-loop/` at the repo root.

Files:

- `.agent-loop/state.md`: human-readable current objective, phase, verifier, gates, blockers, and resume point.
- `.agent-loop/journal.jsonl`: append-only attempt records.

Do not create state files for small one-pass work.

## Script

Use the bundled `scripts/loop_state.py` when available. If the script path is unavailable in the runtime, do the same steps inline with markdown state and an append-only JSONL journal.

Common commands:

```bash
python3 scripts/loop_state.py init --objective "..." --mode controlled --verifier "..."
python3 scripts/loop_state.py record --phase implement --action "..." --hypothesis "..." --gate fail --evidence-file /tmp/gate.log
python3 scripts/loop_state.py resume
python3 scripts/loop_state.py stall --threshold 3 --exit-code
```

When the script lives inside a global skill folder, call it by its installed path. Keep state paths relative to the target repo.

## Loop Contract

1. Initialize state before a resumable or automated loop starts.
2. At the start of each resumed turn, read `resume` output before choosing the next action.
3. After every meaningful attempt, record action, hypothesis, gate result, evidence, and next step.
4. Before retrying after a failed gate, run the stall check.
5. If the same failure fingerprint repeats at the threshold, do not retry the same approach. Switch strategy, reduce scope, ask for user input, or escalate.
6. Mark done only with concrete verifier evidence in the same turn.

## Done Evidence

Final output should mention the state location when this skill was used, plus:

- last verifier result;
- whether stall check was clear or triggered;
- resume point if not done;
- open blockers or human gates.
