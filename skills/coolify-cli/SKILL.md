---
name: coolify-cli
description: Use when working with the Coolify CLI to install or verify the binary, configure contexts and API tokens, use SSH tunnels for protected self-hosted panels, inspect servers/projects/resources/apps/databases/services, deploy resources, read deployment logs, and manage environment variables.
metadata:
  short-description: Operate Coolify from the CLI
---

# Coolify CLI

Use this skill when the user asks to operate Coolify from the terminal.

## Source Of Truth

The CLI is `coollabsio/coolify-cli`; check the upstream README if the command surface may have changed:

```sh
curl -fsSL https://raw.githubusercontent.com/coollabsio/coolify-cli/main/README.md
coolify help
coolify <command> --help
```

Prefer installed CLI help for exact flags because the local binary version may lag behind the README.

## Local Setup

Install on macOS/Linux:

```sh
brew install coollabsio/coolify-cli/coolify-cli
```

Official script alternative:

```sh
curl -fsSL https://raw.githubusercontent.com/coollabsio/coolify-cli/main/scripts/install.sh | bash
```

Verify:

```sh
command -v coolify
coolify version
coolify config
coolify context list
```

The config file is normally `~/.config/coolify/config.json`. Treat it as secret-bearing once contexts are configured.

## Tokens And Contexts

Get a token from the Coolify dashboard at `/security/api-tokens`.

Cloud:

```sh
coolify context set-token cloud <token>
```

Self-hosted:

```sh
coolify context add -d <context_name> <url> <token>
coolify context use <context_name>
coolify context verify
coolify context version
```

Useful context commands:

```sh
coolify context list
coolify context get <context_name>
coolify context set-token <context_name> <token>
coolify context update <context_name> --url <new_url>
coolify context delete <context_name>
```

Never print tokens back to the user. Avoid `--show-sensitive` unless the user explicitly asks and understands it will reveal secrets.

## Protected Self-Hosted Panels

If a panel is behind an access proxy, the CLI may receive an HTML login page instead of JSON. For local CLI operations, use an SSH tunnel to the Coolify port on the server:

```sh
ssh -fN -L <local_port>:localhost:<remote_coolify_port> <host_alias>
coolify context add -f -d <context_name> http://localhost:<local_port> <token>
coolify context verify
```

If the local port is already taken, choose another local port and update the context URL:

```sh
coolify context update <context_name> --url http://localhost:<local_port>
```

## Read-Only Discovery

Start with read-only commands before making changes:

```sh
coolify server list
coolify project list
coolify resource list
coolify app list
coolify database list
coolify service list
coolify team current
```

Use machine-readable output for scripts:

```sh
coolify server list --format=json
coolify app list --format=pretty
```

Inspect details:

```sh
coolify server get <server_uuid> --resources
coolify app get <app_uuid>
coolify database get <database_uuid>
coolify service get <service_uuid>
```

## Deployments And Logs

Deploy by name when names are unambiguous:

```sh
coolify deploy name <resource_name>
coolify deploy batch api,worker,frontend
```

Deploy by UUID when precision matters:

```sh
coolify deploy uuid <resource_uuid>
coolify deploy uuid <resource_uuid> --force
coolify deploy uuid <resource_uuid> --pull-request-id <id>
coolify deploy uuid <resource_uuid> --docker-tag <tag>
```

Monitor:

```sh
coolify deploy list
coolify deploy get <deployment_uuid>
coolify app deployments list <app_uuid>
coolify app deployments logs <app_uuid>
coolify app deployments logs <app_uuid> <deployment_uuid> -n 200
coolify app logs <app_uuid>
```

Use `--debuglogs` only when normal deployment logs do not explain the failure; it may reveal internal command details.

## Environment Variables

Application envs:

```sh
coolify app env list <app_uuid>
coolify app env get <app_uuid> <env_uuid_or_key>
coolify app env create <app_uuid> --key KEY --value VALUE
coolify app env update <app_uuid> <env_uuid_or_key> --value VALUE
coolify app env sync <app_uuid> --file .env
```

Service envs:

```sh
coolify service env list <service_uuid>
coolify service env sync <service_uuid> --file .env
```

Important behavior: `env sync` updates existing variables and creates missing variables, but does not delete variables absent from the `.env` file.

## Databases And Backups

Common commands:

```sh
coolify database list
coolify database start <uuid>
coolify database stop <uuid>
coolify database restart <uuid>
coolify database backup list <database_uuid>
coolify database backup executions <database_uuid> <backup_uuid>
coolify database backup trigger <database_uuid> <backup_uuid>
```

Database deletion is destructive by default because it can delete configuration, volumes, cleanup Docker data, and connected networks. Confirm intent explicitly before running delete commands.

## Safety Rules

- Read first, mutate second. List and inspect resources before starting, stopping, deleting, deploying, or changing env vars.
- Ask before persistent credential changes, token creation, deletes, force deploys, stopping production resources, or database backup/delete changes.
- Do not echo secrets, pasted tokens, env values, private keys, or `--show-sensitive` output.
- Prefer `--context <name>` when there is any doubt about the active target.
- For access-protected panels, diagnose `invalid character '<' looking for beginning of value` as likely HTML login response, then use an SSH tunnel context.
- For server maintenance beyond CLI API operations, verify live state before changing anything.
