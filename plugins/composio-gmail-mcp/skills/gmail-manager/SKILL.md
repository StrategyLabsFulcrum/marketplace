---
name: gmail-manager
description: >
  When the user mentions "check my email", "fetch emails", "search emails",
  "send an email", "draft a reply", "archive", "label emails", "gmail",
  "my inbox", "unread emails", or references a specific email account by name,
  use this skill to route the request to the correct Gmail account via the
  composio-gmail MCP tools.
---

# Gmail Manager

Multi-account Gmail operations via the composio-gmail MCP server.

## Available Accounts

Always call `list_accounts` first to discover which accounts are connected and their names. Every Gmail tool requires an `account` parameter matching one of these names.

If no accounts are connected, guide the user through `/gmail-setup`.

## Routing Rules

- If the user specifies an account name ("check my work email"), use that account.
- If the user doesn't specify and there's only one account, use it.
- If there are multiple accounts and the user doesn't specify, ask which account they mean.
- If the user says "all accounts" or "everything", run the operation against each account and combine results.

## Common Operations

### Fetch Inbox
```
gmail_fetch_emails(account="work", query="is:unread", max_results=20)
```

### Search
```
gmail_search(account="personal", query="from:alice subject:invoice after:2026/01/01")
```

### Read a Specific Email
```
gmail_get_message(account="work", message_id="<id from fetch>")
```

### Read a Thread
```
gmail_get_thread(account="work", thread_id="<threadId from fetch>")
```

### Send Email
Always confirm recipient, subject, and body with the user before calling. This is irreversible.
```
gmail_send_email(account="work", to="alice@co.com", subject="Re: Invoice", body="...")
```

### Create Draft
Safer alternative — creates a draft the user can review in Gmail before sending.
```
gmail_create_draft(account="work", to="alice@co.com", subject="Re: Invoice", body="...")
```

### Archive
```
gmail_archive(account="work", message_ids="<id1>,<id2>")
```

### Label/Organize
```
gmail_modify_labels(account="work", message_ids="<id>", add_labels="Label_123", remove_labels="INBOX")
```

### List Labels
```
gmail_list_labels(account="work")
```

## Presentation

When showing email results to the user, format them clearly:
- Show sender, subject, and relative time (e.g., "2 hours ago")
- Indicate unread status
- Group by account when showing results from multiple accounts
- Truncate long snippets

## Error Handling

- "Unknown account" → show available accounts from `list_accounts`
- Connection errors → suggest the user re-authenticate with `/gmail-connect`
- No API key → guide through `/gmail-setup`
