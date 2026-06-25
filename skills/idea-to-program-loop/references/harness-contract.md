# Harness Contract

Use this reference when a loop needs evidence from tests, CLI commands, browser checks, CI, logs, traces, docs, or external systems.

## Local Context Discovery

When working in an existing repository, first look for local guidance before inferring conventions from isolated files:

- repository instructions such as `AGENTS.md`;
- README files and docs;
- architecture notes, ADRs, runbooks, and domain notes;
- package scripts, test commands, CI hints, and nearby examples.

Treat local repository guidance as feedforward control for the loop. If local guidance conflicts with the user request, surface the conflict before planning or implementing.

## Sensor States

- `available`: use now.
- `available_with_approval`: ask before live, privileged, destructive, costly, or sensitive access.
- `missing_optional`: continue, but record the confidence gap.
- `missing_blocking`: stop and ask for configuration, an artifact, permission, or a narrower local goal.
- `replaced_by_artifact`: live sensor is unavailable, but the user supplied a log, trace, screenshot, HAR, PDF, CI output, exported report, or reproduction video.

## Sensor Order

Prefer workspace-native evidence before external systems when it can answer the question:

1. Local repository guidance, docs, tests, and project conventions.
2. CLI commands, local tests, type checks, linters, local app logs, database/dev-server checks.
3. Browser checks through `Browser` / `browser:control-in-app-browser` for local web apps, localhost, screenshots, DOM inspection, and normal browser verification.
4. Microsoft Edge through `computer-use:computer-use` when the task depends on a real desktop browser, existing logged-in state, Edge-specific behavior, or manual UI-level interaction.
5. CI, hosted logs, traces, observability, issue trackers, Slack, GitHub, Datadog, Sentry, Linear, Jira, cloud consoles, and production systems.

## Build/Lint Discovery Rule

Before declaring app code done, inspect local project guidance for the static gate commands: package scripts, Makefiles, task runners, solution/project files, CI config, README, or `AGENTS.md`. Prefer the command the repository already uses over invented commands.

For code changes, run build/typecheck/lint/compile or the closest scoped equivalent when available. If the command is unavailable, too costly, or blocked by missing environment setup, record the reason, the nearest proxy command, and whether CI/CD must cover the gap after push or PR.

## CI/CD Follow-up Rule

Run the strongest practical local checks before sharing changes. If the full local pipeline cannot run and the repository has CI/CD, treat CI/CD as a follow-up sensor after push or PR.

Monitor CI/CD with available GitHub/CI tools when possible. If that sensor is unavailable, ask the user to monitor the run or provide the output. Record `post-push CI/CD: pass / fail / unavailable / delegated / not needed` and do not claim CI/CD passed unless observed.

## External Connector Rule

Treat configured external services as optional sensors unless the situation truly requires them. Do not fail a loop just because Slack, Datadog, Sentry, GitHub, Linear, Jira, or production logs are unavailable.

If a missing external sensor blocks safe progress, ask for one of:

- tool/connector configuration,
- exported logs/traces/screenshots/CI output,
- permission to use a live environment,
- a narrower local-only goal.

Never ask the user to paste secrets or auth tokens into chat.

## Evidence Rule

Before claiming completion, name the strongest evidence used and any meaningful evidence gap that remains.

## Objective Gate Rule

For automated or hands-off loops, evidence must include an objective gate that can reject bad output without the authoring agent's judgment: test, typecheck, lint, build, reproducible command, browser check, CI, or another deterministic domain check.

A reviewer agent is a maker/checker quality gate, not an objective verifier. If only reviewer judgment is available, keep the work as a controlled human-in-loop workflow and state the verifier gap.
