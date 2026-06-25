#!/usr/bin/env bash
set -euo pipefail

repo_path="${1:-$PWD}"

status() {
  local label="$1"
  local state="$2"
  local detail="${3:-}"
  if [[ -n "$detail" ]]; then
    printf '%-22s %s - %s\n' "$label" "$state" "$detail"
  else
    printf '%-22s %s\n' "$label" "$state"
  fi
}

parse_remote() {
  local remote_url="$1"

  case "$remote_url" in
    https://dev.azure.com/*|https://*@dev.azure.com/*)
      local remainder="${remote_url#https://}"
      remainder="${remainder#*@}"
      remainder="${remainder#dev.azure.com/}"
      local org="${remainder%%/*}"
      remainder="${remainder#*/}"
      local project="${remainder%%/*}"
      printf 'organization=https://dev.azure.com/%s project=%s\n' "$org" "$project"
      ;;
    https://*.visualstudio.com/*)
      local host="${remote_url#https://}"
      local org="${host%%.*}"
      local remainder="${remote_url#https://*.visualstudio.com/}"
      local project="${remainder%%/*}"
      printf 'organization=https://%s.visualstudio.com project=%s\n' "$org" "$project"
      ;;
    git@ssh.dev.azure.com:v3/*)
      local remainder="${remote_url#git@ssh.dev.azure.com:v3/}"
      local org="${remainder%%/*}"
      remainder="${remainder#*/}"
      local project="${remainder%%/*}"
      printf 'organization=https://dev.azure.com/%s project=%s\n' "$org" "$project"
      ;;
  esac
}

if ! command -v az >/dev/null 2>&1; then
  status "Azure CLI" "MISSING" "install Azure CLI first"
  exit 1
fi

az_version="$(az version --query '"azure-cli"' -o tsv 2>/dev/null || true)"
if [[ -n "$az_version" ]]; then
  status "Azure CLI" "OK" "$az_version"
else
  status "Azure CLI" "WARN" "unable to read version"
fi

ext_version="$(az extension show --name azure-devops --query version -o tsv 2>/dev/null || true)"
if [[ -n "$ext_version" ]]; then
  status "azure-devops ext" "OK" "$ext_version"
else
  status "azure-devops ext" "MISSING" "run: az extension add --name azure-devops"
fi

if [[ -n "${AZURE_DEVOPS_EXT_PAT:-}" ]]; then
  status "PAT env var" "SET" "AZURE_DEVOPS_EXT_PAT is present"
else
  status "PAT env var" "NOT SET" "okay if auth is stored via az devops login or az login"
fi

account="$(az account show --query user.name -o tsv 2>/dev/null || true)"
if [[ -n "$account" ]]; then
  status "az login state" "OK" "$account"
else
  status "az login state" "UNKNOWN" "no active az login session detected"
fi

config_output="$(az devops configure -l 2>/dev/null || true)"
if [[ -n "$config_output" ]]; then
  status "az devops config" "INFO"
  printf '%s\n' "$config_output" | sed '/^[[:space:]]*$/d; s/^/  /'
else
  status "az devops config" "WARN" "unable to read config"
fi

if git -C "$repo_path" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  status "git repo" "YES" "$repo_path"
  remotes="$(git -C "$repo_path" remote -v | awk '{print $2}' | sort -u || true)"
  azure_remotes="$(printf '%s\n' "$remotes" | grep -E 'dev\.azure\.com|visualstudio\.com|ssh\.dev\.azure\.com' || true)"
  if [[ -n "$azure_remotes" ]]; then
    status "Azure remotes" "FOUND"
    while IFS= read -r remote; do
      [[ -z "$remote" ]] && continue
      printf '  %s\n' "$remote"
      parsed="$(parse_remote "$remote" || true)"
      if [[ -n "$parsed" ]]; then
        printf '    %s\n' "$parsed"
      fi
    done <<<"$azure_remotes"
  else
    status "Azure remotes" "NONE" "no Azure DevOps remotes in this repo"
  fi
else
  status "git repo" "NO" "$repo_path"
fi

printf '\n'
printf 'Suggested next steps:\n'
printf '  1. If organization/project are missing, run: az devops configure --defaults organization=https://dev.azure.com/<org> project=<project>\n'
printf '  2. For one-off commands, prefer explicit --organization and --project flags.\n'
printf '  3. If the repo is an Azure Repos checkout, try commands with --detect true when supported.\n'
