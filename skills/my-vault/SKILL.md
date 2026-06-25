---
name: my-vault
description: Use when the user asks to read, write, document, search, or organize notes in their personal Obsidian vault, especially references to "my vault", "meu vault", "Obsidian", or a configured personal notes folder.
---

# My Vault

Use this skill as a local template for operating a personal Obsidian vault from Codex.

Before using it, replace the placeholders with local values in your private copy:

- Vault name: `<vault-name>`
- Vault path: `<absolute-vault-path>`
- Main personal folder: `<personal-folder>`
- Agent-managed folder: `<agent-folder>`
- Codex skill archive folder: `<agent-folder>/skills/`

## Required Tooling

Use the `obsidian-cli` skill before interacting with this vault. Prefer the `obsidian` CLI so operations go through the active Obsidian vault instead of editing files blindly.

Useful checks:

```bash
obsidian vaults verbose
obsidian vault="<vault-name>" info=path
obsidian vault="<vault-name>" folders folder="<personal-folder>"
obsidian vault="<vault-name>" files folder="<personal-folder>" ext=md
```

## Working Rules

- Target `vault="<vault-name>"` when the active vault is ambiguous.
- Use vault-relative paths, for example `<personal-folder>/example.md`.
- Search before creating a new note when the topic may already exist.
- Preserve existing note structure and append/update narrowly unless the user asks for a rewrite.
- Use `silent` for background create/update operations unless the user wants Obsidian to open the note.
- For copied Codex skills, reusable agent instructions, and agent-managed operational artifacts, store under `<agent-folder>/`, not the personal notes folder.
- Save copied Codex skills specifically as `<agent-folder>/skills/<skill-name>/SKILL.md`.
- Preserve the note language used by the vault unless the user explicitly asks for another language.

## Git Sync

If the vault is Git-backed, keep it synchronized when changing notes:

- Before editing or creating notes, run `git -C <absolute-vault-path> pull`.
- After creating any new file, inspect `git -C <absolute-vault-path> status --short`.
- Add only the intended files.
- Commit with a concise message.
- Push after committing unless the user explicitly says not to sync.
- Never overwrite or revert unrelated vault changes.

## Common Commands

```bash
obsidian vault="<vault-name>" search query="term" path="<personal-folder>" limit=20
obsidian vault="<vault-name>" read path="<personal-folder>/example.md"
obsidian vault="<vault-name>" create path="<personal-folder>/example.md" content="..." silent
obsidian vault="<vault-name>" append path="<personal-folder>/example.md" content="..."
git -C <absolute-vault-path> pull
git -C <absolute-vault-path> status --short
git -C <absolute-vault-path> add <personal-folder>/example.md
git -C <absolute-vault-path> commit -m "docs: add example note"
git -C <absolute-vault-path> push
```
