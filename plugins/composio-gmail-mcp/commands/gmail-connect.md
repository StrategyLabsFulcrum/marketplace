---
description: "Connect an additional Gmail account via Google OAuth"
allowed-tools: mcp__composio-gmail__connect_account, mcp__composio-gmail__list_accounts, AskUserQuestion
---

# Connect Gmail Account

Add another Gmail account to the multi-account Gmail MCP server.

## Steps

1. **Show current accounts** — Call `list_accounts` to show what's already connected.

2. **Get account details** — Ask the user:
   - What name for this account? (short, lowercase, no spaces — e.g., "client-acme", "side-project")
   - Optional: a human-readable label (e.g., "Acme Corp")

3. **Connect** — Call `connect_account` with the name and label. This opens the browser for Google OAuth sign-in. Let the user know they need to complete sign-in in the browser.

4. **Confirm** — Once connected, call `list_accounts` to show all accounts including the new one.
