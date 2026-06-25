---
name: azure-cli
description: Use when working with Azure from the terminal and you need to choose between Azure CLI resource commands and Azure DevOps Services commands, especially for `az`, `az containerapp`, `az keyvault`, `az acr`, `az postgres`, `az repos`, `az pipelines`, `az boards`, `az artifacts`, or `az devops wiki`, or when auth/scope between Azure subscriptions and Azure DevOps orgs is the blocker.
---

# Azure CLI

Use this skill when the task involves Azure from the terminal. The key decision is whether the task belongs to the Azure resource plane or the Azure DevOps org/project plane.

## Azure CLI vs Azure DevOps

- Use core Azure CLI for Azure resources in a subscription:
  - `az account`
  - `az group`
  - `az keyvault`
  - `az acr`
  - `az containerapp`
  - `az postgres`
  - `az deployment`
- Use the `azure-devops` extension for Azure DevOps Services:
  - `az devops`
  - `az repos`
  - `az pipelines`
  - `az boards`
  - `az artifacts`
  - `az devops wiki`

Rule of thumb:

- If the object lives in an Azure subscription or resource group, use core `az`.
- If the object lives in an Azure DevOps organization or project, use `az` plus the `azure-devops` extension.

## Working Rules

- Treat Azure DevOps commands as cloud-only. Do not use this skill for Azure DevOps Server/on-prem.
- Reuse existing auth when it already works.
- Prefer non-destructive inspection first.
- Do not ask the user to paste secrets into chat.
- Use `--help` before guessing command shape.
- Use `az devops invoke` only when first-class Azure DevOps commands do not cover the operation.

## Quick Start

Run these checks first when setup or auth may be the blocker:

```bash
az version
az account show
az extension show --name azure-devops
az devops configure -l
```

If you want a read-only diagnostic for Azure DevOps context, run:

```bash
./scripts/azdo-cli-doctor.sh
```

## Authentication Model

There are two auth layers and they are related but not identical:

- `az login` authenticates the Azure account context used by core Azure CLI.
- Azure DevOps commands may also need Azure DevOps org/project defaults or explicit `--organization` and `--project`.
- In some environments, Azure DevOps API calls still need `az devops login` or `AZURE_DEVOPS_EXT_PAT`, even when `az login` already works for subscription commands.

Use:

```bash
az login
az devops configure -l
az devops login --organization https://dev.azure.com/<org>
```

only when the existing auth state is missing or insufficient.

## Choosing the Command Family

### Resource Plane

Use core Azure CLI for:

```bash
az account show
az group list -o table
az keyvault secret list --vault-name <vault>
az acr repository list --name <registry> -o table
az containerapp job show --name <job> --resource-group <rg> -o json
az deployment group what-if --resource-group <rg> --template-file <file>
```

### Azure DevOps Plane

Use the extension for:

```bash
az repos list --organization https://dev.azure.com/<org> --project <project> -o table
az pipelines list --organization https://dev.azure.com/<org> --project <project> -o table
az pipelines runs list --organization https://dev.azure.com/<org> --project <project> -o table
az boards query --organization https://dev.azure.com/<org> --project <project> --id <query-id>
az devops wiki list --organization https://dev.azure.com/<org> --project <project> -o table
```

## Scope and Defaults

Inspect Azure DevOps defaults first:

```bash
az devops configure -l
```

Set them only when useful:

```bash
az devops configure --defaults organization=https://dev.azure.com/<org> project=<project>
```

If the repo already has an Azure Repos remote, prefer repo-local context when supported. For sensitive or ambiguous commands, pass `--organization` and `--project` explicitly.

## Wiki Access

If the user gives a browser wiki URL, do not guess the CLI page path from the slug.

Use:

```bash
az devops wiki list --organization https://dev.azure.com/<org> --project <project> -o table
az devops wiki page show --organization https://dev.azure.com/<org> --project <project> --wiki <wiki> --path '/' --recursion-level oneLevel -o json
az devops wiki page show --organization https://dev.azure.com/<org> --project <project> --wiki <wiki> --path '/Section/Page Title' --include-content -o json
```

Resolve the real `path` from returned `path` fields before fetching the page content.

## Common Failure Modes

- Azure subscription commands fail: check `az login` and `az account show`.
- Azure DevOps commands fail with auth errors: verify org/project scope, then consider `az devops login`.
- Extension missing or stale: `az extension add --name azure-devops` or `az extension update --name azure-devops`.
- Wrong repo inferred: pass explicit `--organization` and `--project`.
- Sandbox or filesystem log-path issues: use a writable `HOME` or `AZURE_CONFIG_DIR` inside the workspace.

Example:

```bash
mkdir -p .azure-home
cp -R ~/.azure .azure-home/
HOME=$PWD/.azure-home az account show
```

## References

- Read `references/official-docs.md` for Microsoft Learn links on both core Azure CLI and the Azure DevOps extension.
