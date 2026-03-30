---
description: "First-time setup for multi-account Gmail — set Composio API key and connect your first account"
allowed-tools: mcp__composio-gmail__setup_api_key, mcp__composio-gmail__connect_account, mcp__composio-gmail__list_accounts, AskUserQuestion
---

# Gmail Setup

Walk the user through first-time setup of the Composio Gmail MCP server.

## Steps

1. **Check current state** — Call `list_accounts` to see if any accounts are already connected and if an API key is configured.

2. **API key** — If no API key is set (`has_api_key: false`), ask the user for their Composio API key. They can get one at https://app.composio.dev → Settings → API Keys. Call `setup_api_key` with the key they provide.

3. **Connect first account** — Ask the user what they'd like to name this account (e.g., "work", "personal", "client-acme"). Then call `connect_account` with that name. This will open their browser for Google sign-in.

4. **Confirm** — Once the connection is active, call `list_accounts` to show the connected account with its email address.

5. **Next steps** — Let them know they can:
   - Connect more accounts anytime with `/gmail-connect`
   - Use any Gmail tool with the `account` parameter matching the name they chose
   - Other plugins (like Inbox Command Center) can now use these tools for multi-account email
