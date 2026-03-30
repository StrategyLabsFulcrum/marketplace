"""Multi-account Gmail MCP server via Composio.

Exposes Gmail operations with explicit account routing.
Each tool accepts an `account` parameter ("work", "personal", etc.)
that maps to a Composio entity_id.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
from functools import lru_cache
from typing import Any

from composio import ComposioToolSet
from mcp.server.fastmcp import FastMCP

# --- Configuration ---

CONFIG_PATH = os.path.expanduser("~/.config/composio-gmail-mcp/config.json")

def load_config() -> dict:
    """Load account config from file or environment.

    On first run (no config file, no env var), returns empty accounts
    so the user can add them via connect_account.
    """
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)

    api_key = os.environ.get("COMPOSIO_API_KEY", "")
    return {
        "api_key": api_key,
        "accounts": {},
    }


CONFIG = load_config()
ACCOUNTS: dict[str, dict] = CONFIG.get("accounts", {})
API_KEY: str = CONFIG.get("api_key", "")
ACCOUNT_NAMES = list(ACCOUNTS.keys())
_config_lock = threading.Lock()


def save_config() -> None:
    """Persist current config to disk with restrictive permissions."""
    config_dir = os.path.dirname(CONFIG_PATH)
    os.makedirs(config_dir, exist_ok=True)
    os.chmod(config_dir, 0o700)
    fd = os.open(CONFIG_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump({"api_key": API_KEY, "accounts": ACCOUNTS}, f, indent=2)


def refresh_account_names() -> None:
    """Update ACCOUNT_NAMES after adding a new account."""
    global ACCOUNT_NAMES
    ACCOUNT_NAMES = list(ACCOUNTS.keys())


# --- Composio toolset cache ---

@lru_cache(maxsize=10)
def get_toolset(account: str) -> ComposioToolSet:
    if account not in ACCOUNTS:
        raise ValueError(
            f"Unknown account '{account}'. Available: {ACCOUNT_NAMES}"
        )
    entity_id = ACCOUNTS[account]["entity_id"]
    return ComposioToolSet(api_key=API_KEY, entity_id=entity_id)


def execute(account: str, action: str, params: dict) -> dict:
    try:
        ts = get_toolset(account)
    except ValueError as e:
        return {"error": str(e)}
    result = ts.execute_action(action=action, params=params)
    if isinstance(result, dict):
        return result
    if isinstance(result, list) and len(result) > 0:
        item = result[0]
        return item.get("response", item) if isinstance(item, dict) else {}
    return {}


def unwrap(result: dict) -> dict:
    """Unwrap nested Composio response."""
    return result.get("data", result)


# --- MCP Server ---

mcp = FastMCP(
    "composio-gmail",
    instructions=(
        "Multi-account Gmail server. Use `list_accounts` to see connected accounts. "
        "Use `connect_account` to add a new Gmail account via Google OAuth. "
        "All Gmail tools require an `account` parameter matching a connected account name."
    ),
)


@mcp.tool()
def setup_api_key(api_key: str) -> str:
    """Set the Composio API key. Required before connecting accounts.

    Get your key from https://app.composio.dev → Settings → API Keys.

    Args:
        api_key: Your Composio API key (starts with "ak_")
    """
    if not api_key.startswith("ak_"):
        return json.dumps({
            "error": "Invalid API key format. Composio keys start with 'ak_'.",
            "get_key": "Get your key from https://app.composio.dev → Settings → API Keys.",
        }, indent=2)

    # Validate the key with a lightweight API call
    try:
        test_ts = ComposioToolSet(api_key=api_key)
        test_ts.client.get_entity("validation-check")
    except Exception as e:
        return json.dumps({
            "error": f"API key validation failed: {e}",
            "get_key": "Verify your key at https://app.composio.dev → Settings → API Keys.",
        }, indent=2)

    global API_KEY
    with _config_lock:
        API_KEY = api_key
        get_toolset.cache_clear()
        save_config()
    return json.dumps({
        "status": "saved",
        "message": "API key validated and saved. You can now use connect_account to add Gmail accounts.",
    }, indent=2)


@mcp.tool()
def list_accounts() -> str:
    """List all connected Gmail accounts and their status."""
    if not ACCOUNTS:
        return json.dumps({
            "accounts": [],
            "message": "No Gmail accounts connected yet. Use connect_account to add one.",
            "has_api_key": bool(API_KEY),
        }, indent=2)

    results = []
    for name, cfg in ACCOUNTS.items():
        try:
            data = unwrap(execute(name, "GMAIL_GET_PROFILE", {}))
            results.append({
                "account": name,
                "label": cfg.get("label", name),
                "email": data.get("emailAddress", "unknown"),
                "total_messages": data.get("messagesTotal", 0),
                "total_threads": data.get("threadsTotal", 0),
                "status": "active",
            })
        except Exception as e:
            results.append({
                "account": name,
                "label": cfg.get("label", name),
                "status": f"error: {e}",
            })
    return json.dumps(results, indent=2)


@mcp.tool()
def connect_account(name: str, label: str = "") -> str:
    """Connect a new Gmail account via Google OAuth. Opens a browser for sign-in.

    After calling this, the user must complete sign-in in the browser.
    The tool will wait up to 120 seconds for authentication to complete,
    then save the new account to config.

    Args:
        name: Short name for this account (e.g. "client-acme", "side-project"). Lowercase, no spaces.
        label: Human-readable label (e.g. "Acme Corp"). Defaults to the name.
    """
    if not API_KEY:
        return json.dumps({
            "error": "No Composio API key configured.",
            "setup": (
                "Set COMPOSIO_API_KEY environment variable, or create "
                f"{CONFIG_PATH} with: "
                '{"api_key": "YOUR_KEY", "accounts": {}}'
            ),
            "get_key": "Sign up at https://app.composio.dev and copy your API key from Settings.",
        }, indent=2)

    name = name.lower().replace(" ", "-")
    if name in ACCOUNTS:
        return json.dumps({"error": f"Account '{name}' already exists. Choose a different name."})

    entity_id = f"mailtop-{name}"
    label = label or name

    try:
        ts = ComposioToolSet(api_key=API_KEY)
        entity = ts.client.get_entity(entity_id)

        # Check if entity already has an active Gmail connection (e.g. from a previous timed-out attempt)
        try:
            connections = entity.get_connections(app_name="gmail")
            active = [c for c in connections if getattr(c, "status", None) == "ACTIVE"]
            if active:
                # Already authenticated — skip OAuth, go straight to saving
                profile_ts = ComposioToolSet(api_key=API_KEY, entity_id=entity_id)
                profile_result = profile_ts.execute_action(action="GMAIL_GET_PROFILE", params={})
                if isinstance(profile_result, list) and profile_result:
                    profile_data = profile_result[0].get("response", {}).get("data", {})
                elif isinstance(profile_result, dict):
                    profile_data = profile_result.get("data", profile_result)
                else:
                    profile_data = {}
                email = profile_data.get("emailAddress", "unknown")
                label_with_email = f"{label} ({email})" if email != "unknown" else label
                with _config_lock:
                    ACCOUNTS[name] = {"entity_id": entity_id, "label": label_with_email}
                    refresh_account_names()
                    get_toolset.cache_clear()
                    save_config()
                return json.dumps({
                    "status": "connected",
                    "email": email,
                    "label": label_with_email,
                    "message": f"Found existing connection. Saved {email} as '{name}'.",
                }, indent=2)
        except Exception:
            pass  # No existing connections — proceed with OAuth

        conn_request = entity.initiate_connection(app_name="gmail", use_composio_auth=True)

        auth_url = conn_request.redirectUrl
        # Open browser for OAuth
        if sys.platform == "darwin":
            subprocess.Popen(["open", auth_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif sys.platform == "linux":
            subprocess.Popen(["xdg-open", auth_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        result = {
            "status": "waiting_for_auth",
            "auth_url": auth_url,
            "message": f"Browser opened for Google sign-in. Complete authentication to connect '{name}'.",
            "account_name": name,
            "entity_id": entity_id,
        }

        # Wait for the connection to become active in a blocking fashion
        # (MCP tool calls are synchronous from the client's perspective)
        try:
            conn_request.wait_until_active(client=ts.client, timeout=120.0)
        except Exception:
            result["status"] = "timeout"
            result["message"] = (
                f"Authentication not completed within 120 seconds. "
                f"You can still sign in at: {auth_url}\n"
                f"After signing in, call connect_account again with name='{name}' to retry."
            )
            return json.dumps(result, indent=2)

        # Connection is active — get the email address
        profile_ts = ComposioToolSet(api_key=API_KEY, entity_id=entity_id)
        profile_result = profile_ts.execute_action(action="GMAIL_GET_PROFILE", params={})
        if isinstance(profile_result, list) and profile_result:
            profile_data = profile_result[0].get("response", {}).get("data", {})
        elif isinstance(profile_result, dict):
            profile_data = profile_result.get("data", profile_result)
        else:
            profile_data = {}

        email = profile_data.get("emailAddress", "unknown")
        label_with_email = f"{label} ({email})" if email != "unknown" else label

        # Save to config
        with _config_lock:
            ACCOUNTS[name] = {"entity_id": entity_id, "label": label_with_email}
            refresh_account_names()
            get_toolset.cache_clear()
            save_config()

        result["status"] = "connected"
        result["email"] = email
        result["label"] = label_with_email
        result["message"] = f"Successfully connected {email} as '{name}'."
        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps({"error": str(e)}, indent=2)


@mcp.tool()
def gmail_get_profile(account: str) -> str:
    """Get Gmail profile info (email address, message/thread counts).

    Args:
        account: Account name (e.g. "work", "personal")
    """
    data = unwrap(execute(account, "GMAIL_GET_PROFILE", {}))
    return json.dumps(data, indent=2)


@mcp.tool()
def gmail_fetch_emails(
    account: str,
    query: str = "",
    max_results: int = 10,
    label_ids: str = "",
    include_body: bool = False,
    page_token: str = "",
) -> str:
    """Fetch emails from a Gmail account.

    Args:
        account: Account name (e.g. "work", "personal")
        query: Gmail search query (e.g. "is:unread", "from:boss@co.com")
        max_results: Number of emails to fetch (1-500)
        label_ids: Comma-separated label IDs to filter by (e.g. "INBOX,UNREAD")
        include_body: Whether to include full message body (slower)
        page_token: Pagination token from previous response
    """
    params: dict[str, Any] = {
        "max_results": min(max_results, 500),
        "include_payload": include_body,
        "verbose": include_body,
    }
    if query:
        params["query"] = query
    if label_ids:
        params["label_ids"] = [lid.strip() for lid in label_ids.split(",")]
    if page_token:
        params["page_token"] = page_token

    data = unwrap(execute(account, "GMAIL_FETCH_EMAILS", params))
    messages = data.get("messages", [])

    # Return compact summaries unless full body requested
    if not include_body:
        compact = []
        for m in messages:
            compact.append({
                "messageId": m.get("messageId"),
                "threadId": m.get("threadId"),
                "sender": m.get("sender"),
                "subject": m.get("subject"),
                "snippet": m.get("snippet", ""),
                "timestamp": m.get("messageTimestamp"),
                "labelIds": m.get("labelIds", []),
                "isUnread": "UNREAD" in m.get("labelIds", []),
            })
        result = {"messages": compact, "account": account}
    else:
        result = {"messages": messages, "account": account}

    next_token = data.get("nextPageToken")
    if next_token and next_token != "":
        result["nextPageToken"] = next_token

    return json.dumps(result, indent=2)


@mcp.tool()
def gmail_get_message(account: str, message_id: str) -> str:
    """Get a specific email message by ID with full content.

    Args:
        account: Account name (e.g. "work", "personal")
        message_id: Gmail message ID (hex string from fetch_emails)
    """
    data = unwrap(execute(account, "GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID", {
        "message_id": message_id,
    }))
    return json.dumps(data, indent=2)


@mcp.tool()
def gmail_get_thread(account: str, thread_id: str) -> str:
    """Get all messages in a thread.

    Args:
        account: Account name (e.g. "work", "personal")
        thread_id: Gmail thread ID
    """
    data = unwrap(execute(account, "GMAIL_FETCH_MESSAGE_BY_THREAD_ID", {
        "thread_id": thread_id,
    }))
    return json.dumps(data, indent=2)


@mcp.tool()
def gmail_send_email(
    account: str,
    to: str,
    subject: str,
    body: str,
    cc: str = "",
    bcc: str = "",
    is_html: bool = False,
) -> str:
    """Send an email. Irreversible — confirm details before calling.

    Args:
        account: Account name (e.g. "work", "personal")
        to: Recipient email address
        subject: Email subject
        body: Email body (plain text or HTML)
        cc: CC recipients (comma-separated)
        bcc: BCC recipients (comma-separated)
        is_html: Whether body is HTML
    """
    params: dict[str, Any] = {
        "recipient_email": to,
        "subject": subject,
        "body": body,
    }
    if cc:
        params["cc"] = cc
    if bcc:
        params["bcc"] = bcc
    if is_html:
        params["is_html"] = True

    data = unwrap(execute(account, "GMAIL_SEND_EMAIL", params))
    return json.dumps({"status": "sent", "account": account, "data": data}, indent=2)


@mcp.tool()
def gmail_create_draft(
    account: str,
    to: str,
    subject: str,
    body: str,
    cc: str = "",
    bcc: str = "",
) -> str:
    """Create an email draft (does not send).

    Args:
        account: Account name (e.g. "work", "personal")
        to: Recipient email address
        subject: Email subject
        body: Email body
        cc: CC recipients (comma-separated)
        bcc: BCC recipients (comma-separated)
    """
    params: dict[str, Any] = {
        "recipient_email": to,
        "subject": subject,
        "body": body,
    }
    if cc:
        params["cc"] = cc
    if bcc:
        params["bcc"] = bcc

    data = unwrap(execute(account, "GMAIL_CREATE_EMAIL_DRAFT", params))
    return json.dumps({"status": "draft_created", "account": account, "data": data}, indent=2)


@mcp.tool()
def gmail_list_labels(account: str) -> str:
    """List all labels/folders for an account.

    Args:
        account: Account name (e.g. "work", "personal")
    """
    data = unwrap(execute(account, "GMAIL_LIST_LABELS", {}))
    labels = data.get("labels", [])
    compact = [{"id": l.get("id"), "name": l.get("name"), "type": l.get("type")} for l in labels]
    return json.dumps(compact, indent=2)


@mcp.tool()
def gmail_modify_labels(
    account: str,
    message_ids: str,
    add_labels: str = "",
    remove_labels: str = "",
) -> str:
    """Add or remove labels from messages. Use to archive (remove INBOX), mark read (remove UNREAD), etc.

    Args:
        account: Account name (e.g. "work", "personal")
        message_ids: Comma-separated message IDs
        add_labels: Comma-separated label IDs to add
        remove_labels: Comma-separated label IDs to remove
    """
    ids = [mid.strip() for mid in message_ids.split(",")]
    add = [l.strip() for l in add_labels.split(",") if l.strip()] if add_labels else []
    remove = [l.strip() for l in remove_labels.split(",") if l.strip()] if remove_labels else []

    data = unwrap(execute(account, "GMAIL_BATCH_MODIFY_MESSAGES", {
        "messageIds": ids,
        "addLabelIds": add,
        "removeLabelIds": remove,
    }))
    return json.dumps({"status": "modified", "account": account, "data": data}, indent=2)


@mcp.tool()
def gmail_archive(account: str, message_ids: str) -> str:
    """Archive messages (remove from inbox).

    Args:
        account: Account name (e.g. "work", "personal")
        message_ids: Comma-separated message IDs to archive
    """
    return gmail_modify_labels(account, message_ids, remove_labels="INBOX")


@mcp.tool()
def gmail_search(account: str, query: str, max_results: int = 20) -> str:
    """Search emails with Gmail query syntax.

    Args:
        account: Account name (e.g. "work", "personal")
        query: Gmail search query (e.g. "from:alice subject:invoice after:2026/01/01")
        max_results: Max results (1-500)
    """
    return gmail_fetch_emails(account, query=query, max_results=max_results)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
