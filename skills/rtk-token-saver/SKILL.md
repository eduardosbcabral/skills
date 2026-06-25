---
name: rtk-token-saver
description: "Use when a development task or loop will run noisy shell commands, tests, builds, linters, git diffs, CI checks, logs, or container/cloud commands and should reduce token usage by using RTK when installed. Treat RTK as optional; fall back to normal commands when unavailable or when exact raw output is required."
metadata:
  short-description: Save tokens on noisy CLI output with RTK
---

# RTK Token Saver

Use RTK as an optional command-output compressor. It should never change the task goal, verification standard, or safety gate.

## Availability

1. Check `command -v rtk`, `rtk --version`, and `rtk gain` only when a noisy shell phase is likely.
2. If unavailable or `rtk gain` fails, say `optional RTK unavailable; using normal commands` once and continue.
3. Do not install or configure RTK unless the user explicitly approves it.

## Use RTK For

Prefer RTK when the output is large and a compact failure-oriented summary is enough:

- Repo inspection: `rtk git status`, `rtk git diff`, `rtk git log`.
- Search/listing summaries: `rtk ls`, `rtk find`, `rtk grep`.
- Verification summaries: `rtk test <command>`, `rtk lint`, `rtk tsc`, `rtk next build`, `rtk pytest`, `rtk cargo test`, `rtk go test`.
- CI/log sensors: `rtk gh run list`, `rtk gh pr view`, `rtk docker logs`, `rtk kubectl logs`, `rtk log <file>`.

## Use Raw Commands For

Use normal commands when full fidelity matters:

- Exact stack traces, compiler diagnostics, snapshots, traces, or generated artifacts.
- Small outputs where compression adds no value.
- Suspected RTK parser/filter issue.
- Destructive or mutating operations, unless the user explicitly wants compact output.
- Security, secrets, compliance, or audit work where hidden detail could be harmful.

## Loop Rules

- Start raw enough to understand context; use RTK for repetitive noisy checks.
- If an RTK summary shows failure but lacks detail, rerun the narrow failing command raw.
- Record verification based on the underlying command, not on RTK itself.
- Never treat token savings as a reason to skip build, lint, tests, CI, logs, or human approval gates.

## Setup Requests

If the user asks to install or configure RTK, use the official `rtk-ai/rtk` instructions, verify that `rtk gain` works, and avoid unattended install scripts without explicit user approval.
