---
name: azure-devops
description: Use when operating Azure DevOps from a repository, especially reading wiki pages with the Azure CLI.
---

# Azure DevOps

Use this skill for Azure DevOps operations through the Azure CLI and the `azure-devops` extension.

## Project Context

Do not hard-code project details in this skill. Resolve them from the repository remote, local documentation, existing `az devops configure -l` defaults, or explicit user input.

Common placeholders:

- Organization: `https://dev.azure.com/<org>`
- Project: `<project>`
- Wiki: `<wiki>`

## Readiness Checks

Run these first when Azure DevOps CLI access may be the blocker:

```bash
az version
az account show
az extension show --name azure-devops
az devops configure -l
```

If the `azure-devops` extension is missing:

```bash
az extension add --name azure-devops
```

## Wiki Workflow

List project wikis:

```bash
az devops wiki list   --organization https://dev.azure.com/<org>   --project <project>   -o table
```

Inspect the wiki tree before fetching page content. Browser URLs are hints; use the returned `path` fields for CLI commands.

```bash
az devops wiki page show   --organization https://dev.azure.com/<org>   --project <project>   --wiki <wiki>   --path '/'   --recursion-level oneLevel   -o json
```

Fetch page content:

```bash
az devops wiki page show   --organization https://dev.azure.com/<org>   --project <project>   --wiki <wiki>   --path '/Page Path'   --include-content   -o json
```

## Rules

- Prefer read-only inspection first.
- Pass `--organization` and `--project` explicitly when scope is ambiguous.
- Do not guess wiki paths from browser slugs; inspect the tree first.
- Do not ask the user to paste secrets into chat.
- Keep project-specific org, project, wiki, URLs, and validation notes outside this reusable skill.
