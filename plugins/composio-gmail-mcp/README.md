# Composio Gmail MCP

Multi-account Gmail access for Claude Code and Cowork via Composio.

## What It Does

Connects unlimited Gmail accounts through Google OAuth and exposes them as MCP tools. Every tool takes an `account` parameter so you always know which inbox you're operating on.

Works standalone or as the email backend for other plugins like Inbox Command Center.

## Commands

| Command | Description |
|---------|-------------|
| `/gmail-setup` | First-time setup — set API key and connect your first Gmail account |
| `/gmail-connect` | Connect an additional Gmail account |

## Tools Available

Once the MCP server is running, these tools are available to all plugins:

| Tool | Description |
|------|-------------|
| `list_accounts` | Show all connected Gmail accounts |
| `connect_account` | Add a new Gmail account via Google OAuth |
| `setup_api_key` | Set/update the Composio API key |
| `gmail_fetch_emails` | Fetch emails with optional search query |
| `gmail_get_message` | Get full message content by ID |
| `gmail_get_thread` | Get all messages in a thread |
| `gmail_search` | Search with Gmail query syntax |
| `gmail_send_email` | Send an email |
| `gmail_create_draft` | Create a draft |
| `gmail_list_labels` | List all labels/folders |
| `gmail_modify_labels` | Add/remove labels from messages |
| `gmail_archive` | Archive messages |
| `gmail_get_profile` | Get account info |

## Getting Started

### 1. Get a Composio API Key

Sign up at [composio.dev](https://app.composio.dev) and copy your API key from Settings.

### 2. Install the MCP Server

```bash
claude mcp add composio-gmail -- uv run --directory <path-to-plugin>/mcp-server python server.py
```

Or add to `~/.claude.json` manually:

```json
{
  "mcpServers": {
    "composio-gmail": {
      "command": "uv",
      "args": ["run", "--directory", "<path-to-plugin>/mcp-server", "python", "server.py"]
    }
  }
}
```

### 3. Run Setup

In Claude Code: `/gmail-setup` — walks you through API key and first account connection.

### 4. Connect More Accounts

In Claude Code: `/gmail-connect` — opens Google OAuth to add another account.

## Configuration

Config is stored at `~/.config/composio-gmail-mcp/config.json`:

```json
{
  "api_key": "ak_...",
  "accounts": {
    "work": { "entity_id": "default", "label": "Work (scott@company.com)" },
    "personal": { "entity_id": "mailtop-personal", "label": "Personal (me@gmail.com)" }
  }
}
```

Adding accounts via `connect_account` or `/gmail-connect` updates this file automatically.

## Dependencies

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- [Composio](https://composio.dev) account and API key
