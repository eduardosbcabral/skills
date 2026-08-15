# AI Agent Skills

Public, reusable skills and custom agents for software-development workflows.

## Layout

- `skills/`: Codex and cross-tool Agent Skills.
- `.codex/agents/`: Codex custom-agent profiles.
- `.claude/skills/`: Claude Code-specific skills.
- `.claude/agents/`: Claude Code custom subagents.
- `scripts/install.py`: installs Codex skills with mapped custom agents.

## Codex

Install all Codex skills:

```bash
python3 scripts/install.py --all
```

Install the orchestration loop and its agents:

```bash
python3 scripts/install.py loop-orchestration
```

Install into one project instead of the user runtime:

```bash
python3 scripts/install.py --project /path/to/workspace loop-orchestration
```

Invoke it explicitly with `$loop-orchestration`, or let Codex load it when the request matches its description. Restart Codex after adding a new top-level skill or custom-agent file.

## Claude Code

Install the Claude-specific loop and its two subagents:

```bash
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R .claude/skills/claude-loop-orchestration ~/.claude/skills/
cp .claude/agents/claude-loop-*.md ~/.claude/agents/
```

Invoke it with `/claude-loop-orchestration`, or let Claude load it from its description. Restart the Claude Code session after adding or editing subagent files.

## Orchestration

Both variants detect whether work starts as an idea, scoped change, or failure. The primary session remains the parent, substantial bounded work goes to a worker, analytical decisions go to an advisor, verification is proportional, and normal or risky change sets receive a fresh final review.

The Codex profiles pin their native models in `.codex/agents/`. The Claude profiles use Opus for read-only analysis and review, and Sonnet for bounded implementation. Model details stay out of the skills themselves.

`rtk-token-saver` remains an independent optional skill. Installing a loop does not install or configure RTK.

## Privacy

Keep this repository generic and public. Do not add personal paths, private hostnames, IP addresses, tokens, customer names, repository names, or environment-specific credentials. Use placeholders for examples. Private workflows belong in a private source.

## Included Skills

- `azure-cli`
- `azure-devops`
- `claude-loop-orchestration` (Claude Code)
- `codex-remove-ui-noise`
- `codex-report-usage`
- `coolify-cli`
- `loop-orchestration`
- `rtk-token-saver`
- `saas-backend-patterns`
- `saas-frontend-patterns`
- `saas-project-bootstrap`
