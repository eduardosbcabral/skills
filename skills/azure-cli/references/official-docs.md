# Azure CLI and Azure DevOps official docs

Use these sources when the task depends on exact Azure CLI or Azure DevOps extension behavior.

## Primary docs

- Azure CLI overview: https://learn.microsoft.com/cli/azure/
- Azure CLI command reference: https://learn.microsoft.com/cli/azure/reference-index?view=azure-cli-latest
- Quickstart: https://learn.microsoft.com/pt-br/azure/devops/cli/?view=azure-devops
- Command reference: https://learn.microsoft.com/cli/azure/devops?view=azure-cli-latest
- PAT auth: https://learn.microsoft.com/azure/devops/cli/log-in-via-pat?view=azure-devops

## What the docs say

- Core Azure CLI manages Azure subscription/resource commands such as `account`, `group`, `deployment`, `keyvault`, `acr`, and `containerapp`.
- The `azure-devops` extension adds the `devops`, `pipelines`, `artifacts`, `boards`, and `repos` command groups, including wiki commands under `az devops wiki`.
- The extension works with Azure DevOps Services, not Azure DevOps Server.
- Standard setup flow is: install Azure CLI, add or update the `azure-devops` extension, authenticate, then set default `organization` and `project`.
- Interactive auth uses `az login`.
- PAT auth can use `az devops login`, stdin piping, or the `AZURE_DEVOPS_EXT_PAT` environment variable.
- Many commands can work without stored defaults if `--organization` and `--project` are passed explicitly.
- Use `--help` for exact command syntax and `--open` when the user wants the portal artifact opened in a browser.
- Use `az devops invoke` only when first-class commands do not cover the endpoint you need.

## Practical bias for this skill

- Reuse the auth already configured on the machine when possible.
- Inspect defaults before mutating them.
- Distinguish resource-plane work from Azure DevOps org/project work before choosing commands.
- Prefer explicit scope for one-off or risky commands.
- If the current repo already points at Azure Repos, use that context before changing global config.
- For wiki access, treat browser URLs as hints. Resolve the actual page `path` from `az devops wiki page show` output before fetching content.
