---
name: my-wiki
description: Use when the user asks to read, write, document, search, or organize notes in a personal notes repository, Obsidian vault, or agent-facing wiki folder.
---

# My Notes

Use this skill as a template for operating a personal notes repository from Codex.

Before using it, replace the placeholders with local values in your private copy:

- Notes repository name: `<notes-repository-name>`
- Obsidian vault name: `<vault-name>`
- Notes repository path: `<notes-repository-path>`
- Human notes folders: `<projects-folder>`, `<areas-folder>`, `<resources-folder>`, `<archive-folder>`
- Agent Wiki folder: `<agent-wiki-folder>`
- Codex skill archive folder: `<agent-wiki-folder>/skills/`

## Naming

- Notes repository: the full Git-backed notes repo and/or Obsidian vault.
- Agent Wiki: the agent-facing subfolder used for synthesized operational memory.
- Human notes: personal notes outside the Agent Wiki.
- Use "vault" only when talking about Obsidian mechanics.
- Do not call the whole notes repository "the wiki" unless the whole repo is intentionally agent-facing.

## Required Tooling

Use the `obsidian-cli` skill before interacting with the notes repository. Prefer the `obsidian` CLI so operations go through the active Obsidian vault instead of editing files blindly.

Useful checks:

```bash
obsidian vaults verbose
obsidian vault="<vault-name>" info=path
obsidian vault="<vault-name>" folders folder="<agent-wiki-folder>"
obsidian vault="<vault-name>" files folder="<agent-wiki-folder>" ext=md
```

## Working Rules

- Target `vault="<vault-name>"` when the active vault is ambiguous.
- Use vault-relative paths, for example `<agent-wiki-folder>/example.md` or `<projects-folder>/example.md`.
- Search before creating a new note when the topic may already exist.
- Preserve existing note structure and append/update narrowly unless the user asks for a rewrite.
- Use `silent` for background create/update operations unless the user wants Obsidian to open the note.
- For copied Codex skills, reusable agent instructions, and agent-managed operational artifacts, store under `<agent-wiki-folder>/`, not the human notes folders.
- Save copied Codex skills specifically as `<agent-wiki-folder>/skills/<skill-name>/SKILL.md`.
- Preserve the note language used by human notes unless the user explicitly asks for another language.

## Git Sync

If the notes repository is Git-backed, keep it synchronized when changing notes:

- Before editing or creating notes, run `git -C <notes-repository-path> pull`.
- After creating any new file, inspect `git -C <notes-repository-path> status --short`.
- Add only the intended files.
- Commit with a concise message.
- Push after committing unless the user explicitly says not to sync.
- Never overwrite or revert unrelated notes changes.

## Common Commands

```bash
obsidian vault="<vault-name>" search query="term" path="<agent-wiki-folder>" limit=20
obsidian vault="<vault-name>" read path="<agent-wiki-folder>/example.md"
obsidian vault="<vault-name>" create path="<agent-wiki-folder>/example.md" content="..." silent
obsidian vault="<vault-name>" append path="<agent-wiki-folder>/example.md" content="..."
git -C <notes-repository-path> pull
git -C <notes-repository-path> status --short
git -C <notes-repository-path> add <agent-wiki-folder>/example.md
git -C <notes-repository-path> commit -m "docs: add example note"
git -C <notes-repository-path> push
```
