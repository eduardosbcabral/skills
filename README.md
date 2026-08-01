# AI Agent Skills

Reusable Codex skills and custom agents for development workflows.

## Layout

- `skills/`: installable skill folders.
- `.codex/agents/`: custom Codex subagent definitions used by the loop skills.
- `scripts/install.py`: installs skills together with their mapped subagents and optional skill dependencies.

## Install in Codex

Codex discovers personal skills under `${CODEX_HOME:-~/.codex}/skills/` and project-scoped skills under `.agents/skills/`. Custom agents are separate: personal definitions live under `${CODEX_HOME:-~/.codex}/agents/` and project-scoped definitions under `.codex/agents/`.

Install all skills from this repository for your user:

```bash
git clone https://github.com/eduardosbcabral/skills.git /tmp/eduardo-skills
cd /tmp/eduardo-skills
python3 scripts/install.py --all
```

Install one loop skill with its mapped custom agents and `$rtk-token-saver` dependency:

```bash
python3 scripts/install.py loop-change-to-done
```

Install repo-scoped skills instead of user-global skills:

```bash
python3 scripts/install.py --project /path/to/workspace loop-change-to-done
```

The generic Codex skill installer copies only the requested skill folder. It does not follow references to this repository's `.codex/agents/` directory. Use `scripts/install.py` for loop skills when their custom agents should be installed automatically.

Use a skill explicitly by mentioning it in the prompt, for example `$loop-change-to-done`. Codex may also invoke a skill automatically when the task matches the `description` in `SKILL.md`. If a newly copied skill does not appear, restart Codex.

## Install in Claude Code

Claude Code discovers skills from `~/.claude/skills/<skill-name>/SKILL.md` for personal skills and `.claude/skills/<skill-name>/SKILL.md` for project-scoped skills. The command name comes from the skill folder name, so `~/.claude/skills/loop-change-to-done/SKILL.md` is invoked as `/loop-change-to-done`.

Install all skills for your user:

```bash
git clone https://github.com/eduardosbcabral/skills.git /tmp/eduardo-skills
mkdir -p ~/.claude/skills
cp -R /tmp/eduardo-skills/skills/* ~/.claude/skills/
```

Install only one skill:

```bash
mkdir -p ~/.claude/skills
cp -R skills/loop-change-to-done ~/.claude/skills/
```

Install repo-scoped skills instead of user-global skills:

```bash
mkdir -p .claude/skills
cp -R skills/loop-change-to-done .claude/skills/
```

Invoke a Claude Code skill directly with `/skill-name`, for example `/loop-change-to-done`. Claude Code can also load skills automatically from their description. Claude Code detects edits under existing watched skill directories, but restart Claude Code if you create a new top-level skills directory and the skill does not appear.

## Privacy

This repository is intended to stay public. Keep personal paths, private hostnames, IP addresses, tokens, customer names, repository names, and environment-specific credentials out of these files. Use placeholders such as `<vault-name>`, `<project>`, `<host-alias>`, and `<timezone>` instead.

## Included Skills

- `azure-cli`
- `azure-devops`
- `codex-remove-ui-noise`
- `codex-report-usage`
- `coolify-cli`
- `create-wiki-notes`
- `loop-broken-to-fixed`
- `loop-change-to-done`
- `loop-idea-to-build`
- `loop-state-and-stall-guard`
- `my-skills`
- `my-wiki`
- `rtk-token-saver`
- `saas-backend-patterns`
- `saas-frontend-patterns`
- `saas-project-bootstrap`

## Loop Dependencies

The three loop skills bundle their product, change, diagnosis, grilling, simplicity, output-style, and stall-control behavior. They delegate bounded extraction, evidence, planning, diagnosis, implementation, and independent review to custom or built-in subagents.

The repository installer adds each loop's mapped custom agents and the bundled `$rtk-token-saver` optional dependency. RTK uses the external CLI from `rtk-ai/rtk` when available and falls back to normal commands when RTK is unavailable or exact raw output is required.
