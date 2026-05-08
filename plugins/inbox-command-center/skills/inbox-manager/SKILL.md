---
name: inbox-manager
description: >
  Inbox Command Center for managing email (multi-account Gmail and Outlook via Composio),
  Slack, iMessage, and messaging platforms. Use when the user mentions "check my email",
  "inbox", "triage", "what did I miss", "clean up my inbox", "draft a reply", "inbox zero",
  "unsubscribe", "email manager", "comms manager", "check Slack", "check iMessage",
  "check my texts", "any important emails", "what do I need to respond to",
  "create a rule", "message rules", "voice profile", "daily briefing", "morning update",
  "check my messages", "send me a reminder", "inbox report", "email stats",
  "VIP contacts", "VIP summary", "voice review", "calibrate my voice",
  "folder rules", "low priority emails", "edit my contacts",
  "who's waiting on me", "show my followups", "show my todos",
  or anything related to email, messaging, or communications management.
---

# Inbox Command Center

An AI communications manager that triages email (multi-account via Composio), Slack, iMessage, and messaging platforms — categorizes messages, drafts replies in the user's authentic voice, manages calendar, tracks tasks via a hand-editable workspace folder, enforces smart rules with stakes and scope, and delivers scheduled briefings and reminders via the user's preferred channel.

## How It Works

The Inbox Command Center has eight layers:

1. **Connection Layer** — Connects to email (Gmail/Outlook via Composio, multi-account), Slack/Calendar/Fireflies (native MCP), iMessage (AppleScript), and other tools.
2. **Workspace Layer** — Reads and writes a hand-editable workspace folder at `~/Inbox Command Center/` containing todos, followups, contacts, rules, voice profile, and session logs.
3. **Rules Layer** — Applies user-configured rules to auto-categorize, archive, forward, label, or escalate messages before triage. Each rule has type, stakes (low/high), and scope (per-inbox/global).
4. **Triage Layer** — Categorizes remaining messages as RESPOND, FYI, JUNK, or UNSUBSCRIBE. Sequential per-inbox processing with rapid-fire action codes.
5. **Voice Layer** — Maintains a living voice profile primarily fed by Fireflies meeting transcripts, secondary sources (sent email, Slack, iMessage), continuous draft-edit learning, and A/B calibration.
6. **Calendar Layer** — Detects conflicts, unresponded invites, marathon blocks, and meetings needing prep.
7. **Task Layer** — Tracks todos and followups in markdown files (`todos.md`, `followups.md`). Optional augmentation: Apple Reminders, Google Calendar events for time-bound items.
8. **Briefing Layer** — Delivers scheduled daily summaries, VIP digests, weekly Fireflies pulls, monthly reports, and reminders via Slack, iMessage, email, or calendar.

## Session Start — Run Every Time

Before any other action, the skill performs these checks:

1. **Read workspace files** at `~/Inbox Command Center/`:
   - `.meta.json` — version, connected_inboxes, last_rule_review, last_fireflies_pull, schedules, voice_drift_counter
   - `contacts.md` — VIPs and per-recipient notes
   - `todos.md` — open todos
   - `followups.md` — people waiting on the user
   - `rules.md` — active rules with type/stakes/scope
   - `rules-review-queue.md` — pending suggestions
   - `voice-profile.md` and `voice-profile-brand.md` (if BKC connected)

2. **Migration check** — If old v1.3 paths exist (`~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/`) and new path is empty, trigger v1.3 → v1.4 migration flow.

3. **Version check** — If installed plugin version differs from `.meta.json.version`, present update briefing.

4. **Detect cadence-due automations:**
   - Rule review (compare `last_rule_review` against cadence)
   - Voice profile review (compare against cadence)
   - VIP list review (compare against cadence)
   - Fireflies pull (compare `last_fireflies_pull` against weekly cadence)
   - Monthly inbox report (compare against cadence)

5. **Detect user edits** to workspace files since last session (via mtime). Log to today's session log: e.g. "User edited contacts.md (Bryan section)".

6. **Greet with brief context, not a wall:**
   > "Morning Ramsey. You have N todos, M followups, K pending rule suggestions across [inbox count] inboxes. Last session [most recent log entry]. What are we working on?"

Then wait. Let the user drive.

## Connection Methods

The plugin uses three connection types depending on the tool:

### Composio (primary connection layer)

For email (Gmail and Outlook, multi-account) and tools without native MCP support. All Composio calls go through `mcp__claude_ai_Composio__COMPOSIO_MULTI_EXECUTE_TOOL`.

**Gmail tools:**

| Tool Slug | What It Does |
|---|---|
| `GMAIL_FETCH_EMAILS` | Search + fetch emails (any Gmail query syntax). Primary triage tool. |
| `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` | Get full email by message ID |
| `GMAIL_FETCH_MESSAGE_BY_THREAD_ID` | Get all messages in a thread |
| `GMAIL_LIST_THREADS` | List threads matching a query |
| `GMAIL_LIST_LABELS` | List all Gmail labels (needed for label IDs) |
| `GMAIL_SEND_EMAIL` | Send a new email immediately |
| `GMAIL_REPLY_TO_THREAD` | Reply within an existing thread |
| `GMAIL_CREATE_EMAIL_DRAFT` | Create a draft (doesn't send) |
| `GMAIL_UPDATE_DRAFT` / `GMAIL_SEND_DRAFT` | Update / send saved drafts |
| `GMAIL_LIST_DRAFTS` / `GMAIL_GET_DRAFT` | Manage drafts |
| `GMAIL_BATCH_MODIFY_MESSAGES` | Bulk add/remove labels (mark read, archive, etc.) up to 1000 at once |
| `GMAIL_ADD_LABEL_TO_EMAIL` | Add/remove labels on a single message |
| `GMAIL_MODIFY_THREAD_LABELS` | Add/remove labels on a thread |
| `GMAIL_CREATE_LABEL` | Create custom Gmail label (used for synthetic ICC folders) |
| `GMAIL_MOVE_TO_TRASH` | Move single message to trash (recoverable) |
| `GMAIL_UNTRASH_MESSAGE` | Restore from trash |
| `GMAIL_BATCH_DELETE_MESSAGES` | Permanently delete multiple messages (high_stakes — confirm always) |
| `GMAIL_GET_ATTACHMENT` | Download an attachment |
| `GMAIL_SEARCH_PEOPLE` | Search contacts by name or email |

**Outlook / Microsoft 365 tools** (Composio's `OUTLOOK_*` and `OFFICE365_*` slugs):
- `OUTLOOK_FETCH_MESSAGES`, `OUTLOOK_SEND_MESSAGE`, `OUTLOOK_REPLY_MESSAGE`, `OUTLOOK_CREATE_DRAFT`, `OUTLOOK_MOVE_MESSAGE` (folder routing), `OUTLOOK_DELETE_MESSAGE`, `OUTLOOK_FORWARD_MESSAGE`

**Other Composio connectors:**
- Outlook Calendar (for Outlook users)
- Otter.ai, Gong, Fathom (additional transcript sources)

**Session initialization:**
- Call `COMPOSIO_MANAGE_CONNECTIONS` to start/check OAuth for an account
- Use `COMPOSIO_WAIT_FOR_CONNECTIONS` while user completes browser flow
- Use `COMPOSIO_GET_TOOL_SCHEMAS` if a tool's schema isn't yet loaded

**Tool usage rules:**
- **Mark as read:** `GMAIL_BATCH_MODIFY_MESSAGES` → `removeLabelIds: ["UNREAD"]`
- **Mark as unread:** `addLabelIds: ["UNREAD"]`
- **Archive:** `removeLabelIds: ["INBOX"]`
- **Star:** `GMAIL_ADD_LABEL_TO_EMAIL` → `add_label_ids: ["STARRED"]`
- **Custom labels:** Must use label IDs (e.g., `Label_123`), NOT display names. Call `GMAIL_LIST_LABELS` first.
- **Trash vs. permanent delete:** Default to `GMAIL_MOVE_TO_TRASH` (recoverable). Use `GMAIL_BATCH_DELETE_MESSAGES` only after explicit user confirmation — high_stakes.
- **Thread replies:** Always use `GMAIL_REPLY_TO_THREAD` with thread_id to keep conversations intact.
- **Message IDs:** Always use values from `GMAIL_FETCH_EMAILS` results. Never invent.

### Native MCP

Used where the native MCP feature surface is richer than Composio's wrapper:

| Tool | Why native |
|---|---|
| Slack | Richer thread, canvas, scheduled-message support |
| Google Calendar | `suggest_time`, `respond_to_event`, native event creation |
| Fireflies | Summaries, soundbites, analytics, sentiment beyond Composio's wrapper |

Tool calls follow standard MCP patterns:
- `mcp__claude_ai_Slack__slack_send_message`, `mcp__claude_ai_Slack__slack_read_channel`, etc.
- `mcp__claude_ai_Google_Calendar__list_events`, `mcp__claude_ai_Google_Calendar__create_event`, etc.
- `mcp__claude_ai_Fireflies__fireflies_get_transcripts`, `mcp__claude_ai_Fireflies__fireflies_get_transcript`, etc.

### AppleScript

iMessage uses macOS AppleScript/Shortcuts integration. No Composio or MCP — direct shell access via the local Mac. Requires Messages app configured and iMessage account active.

### Composio fallback path

If a user opts out of Composio, the skill operates in **fallback mode**:
- Native Gmail MCP only (single account)
- No Outlook
- No multi-account
- No Otter / Gong / Fathom
- Slack, Calendar, Fireflies, iMessage still work

Fallback mode is flagged in `.meta.json.fallback_mode: true`. Triage start displays a warning: "You're in fallback mode — features X, Y, Z are unavailable. Run `/setup-wizard` to add Composio."

## Workspace

All user data lives at `~/Inbox Command Center/` (iCloud-synced if iCloud Drive is enabled, local fallback otherwise).

```
~/Inbox Command Center/
├── .meta.json                  # bookkeeping
├── contacts.md                 # per-recipient memory + VIPs
├── todos.md                    # things you owe yourself
├── followups.md                # people waiting on you
├── rules.md                    # active rules with type/stakes/scope
├── rules-review-queue.md       # pending rule suggestions
├── voice-profile.md            # personal voice
├── voice-profile-brand.md      # brand voice (if BKC connected)
├── session-logs/
│   └── YYYY-MM-DD.md          # daily journal
└── reports/
    └── YYYY-MM.md             # monthly inbox reports
```

### File-by-file responsibilities

**`.meta.json`** — Bookkeeping. Read at session start, update on changes.

```json
{
  "version": "1.4.0",
  "migrated_from": "1.3.0",
  "connected_inboxes": [
    {
      "alias": "personal",
      "platform": "gmail",
      "account": "ramsey@strategylabs.us",
      "composio_connection_id": "...",
      "folders_enabled": ["Newsletters", "Receipts", "Low Priority"]
    },
    {
      "alias": "uno-mas",
      "platform": "gmail",
      "account": "ramsey@unomastacos.com",
      "composio_connection_id": "...",
      "folders_enabled": ["Receipts", "Finance", "Low Priority"]
    }
  ],
  "last_rule_review": "2026-05-01",
  "last_fireflies_pull": "2026-05-05",
  "session_count": 47,
  "fallback_mode": false,
  "devices": ["MacBook Pro", "iMac"],
  "schedules": {
    "daily_briefing": {"time": "07:30", "days": "weekdays", "channel": "slack-dm", "enabled": true},
    "vip_digest": {"channel": "slack-dm", "enabled": true},
    "fireflies_pull": {"day": "sunday", "enabled": true},
    "voice_review_cadence": "monthly",
    "vip_review_cadence": "monthly",
    "inbox_report_cadence": "monthly",
    "rule_suggestion_cadence": "every-3rd",
    "batch_size": 10,
    "unsubscribe_mode": "batch"
  },
  "voice_drift_counter": 0,
  "reminder_delivery": {"channel": "slack-channel", "slack_channel": "#inbox-reminders"}
}
```

**`contacts.md`** — Per-recipient memory. Section per person; `[VIP]` tag in header marks priority. Auto-tracked timeline + manual notes.

```markdown
## Bryan Howell <bryan@dieselpowerproducts.com> [VIP]
**Review:** monthly | **Since:** 2026-04
- Tone: concise, numbers-forward, skip pleasantries
- Preferred cc: operations@dpp on financial threads
- Reply target: within 4 hours
- Inboxes seen: ramsey@strategylabs.us, ramsey@unomastacos.com
- Last email: 2026-05-07 (uno-mas)
- Last meeting: 2026-05-03 (Fireflies — Q3 numbers call)
- Recent context: Decision pending re funding source. Tamara at Riverbank offered fund transfer.
```

Brand-voice contacts get `[Brand]` tag (in addition to or instead of `[VIP]`).

**`todos.md`** — Things the user owes themselves. Append-only with status:
```markdown
- [ ] Confirm Q3 numbers — from Joel Barbour — added 2026-04-15 — due 2026-04-20 — priority HIGH
- [ ] Review marketing brief — from Annie — added 2026-05-07 — priority MED
- [x] Send invoice to Bryan — from manual — completed 2026-05-06
```
Done items kept for 14 days then auto-pruned. Time-bound items also create Google Calendar events (or Apple Reminders / Outlook tasks if user opted in).

**`followups.md`** — People waiting on a reply from the user.
```markdown
- Joel Barbour — re: wholesale pricing — sent 2026-05-01 — waiting 6 days
- Annie — re: budget Q — sent 2026-05-04 — waiting 3 days
```
Add when user sends/drafts something expecting a reply. Remove when reply lands. Update "waiting N days" each session.

**`rules.md`** — Active rules. Each rule has type, stakes, and scope.

```markdown
### Rule: Auto-archive ESPN newsletters
- **Type:** delete
- **Stakes:** low_stakes
- **Scope:** per-inbox (personal)
- **Status:** Active
- **Trigger:**
  - Sender: notifications@espn.com
- **Action:**
  - Move to Trash
- **Created:** 2026-04-12
- **Last triggered:** 2026-05-07
- **Times triggered:** 47

### Rule: Escalate emails from Bryan
- **Type:** prioritize
- **Stakes:** low_stakes
- **Scope:** global (VIP)
- **Status:** Active
- **Trigger:**
  - Sender: bryan@dieselpowerproducts.com
- **Action:**
  - Escalate to 🔴 HIGH
- **Created:** 2026-04-01
```

**`rules-review-queue.md`** — Pending suggestions. User reviews on cadence.

```markdown
- [ ] **[low_stakes][per-inbox: uno-mas][delete]** Auto-archive Substack newsletters — proposed 2026-05-05 — reasoning: archived 8 from this sender in last 7 days
- [ ] **[high_stakes][global][organize]** Auto-forward AP invoices to operations@dpp — proposed 2026-05-04 — reasoning: forwarded manually 3 times this week
```

**`voice-profile.md`** and **`voice-profile-brand.md`** — Living voice documents. (See Voice Layer section below.)

**`session-logs/YYYY-MM-DD.md`** — Append-only daily journal.

```markdown
# Session log — 2026-05-07

- **08:14** — Session start
- **08:14** — Workspace loaded: 3 inboxes, 14 todos, 4 followups, 6 pending rules
- **08:15** — VIP scan across all inboxes: 2 surfaced (Bryan@uno-mas, Joel@personal)
- **08:18** — [uno-mas] Triaged 23 emails: 3 respond, 5 FYI, 15 junk
- **08:18** — [uno-mas] Auto-rules applied: archived 8 newsletters, labeled 3 receipts
- **08:21** — [uno-mas] Sent reply to Bryan re Q3 numbers (2 edits → contacts.md)
- **08:24** — [personal] Triaged 12 emails: 1 respond, 4 FYI, 7 junk
- **08:26** — Proposed rule: auto-archive ESPN newsletters (low_stakes) → queued
- **08:28** — Session end: 35 emails handled, 2 sent, 1 followup added, 1 rule queued
- **09:14** — User edited contacts.md (Bryan section) detected via mtime
```

**Log these events:** triage runs, sends, bulk actions, rule proposals/reviews, voice learning events, Fireflies pulls, user-made workspace edits.
**Don't log:** casual back-and-forth, reading individual emails, meta-commentary.

**`reports/YYYY-MM.md`** — Monthly inbox reports (see Monthly Inbox Report section).

### Writing to the workspace

Use Filesystem MCP tools (`mcp__filesystem__write_file` for overwrites; read + append pattern for session logs). Always use absolute paths.

For overwriting (todos, followups, rules, contacts):
```
mcp__filesystem__write_file → ~/Inbox Command Center/[filename]
```

For appending (session logs):
```
mcp__filesystem__read_text_file → existing log
[append your line]
mcp__filesystem__write_file → updated log
```

### Cross-Device Sync

When iCloud Drive is enabled, the workspace lives at `~/Library/Mobile Documents/com~apple~CloudDocs/Inbox Command Center/`. The skill creates a symlink at `~/Inbox Command Center/` pointing to the iCloud path so Finder and shell access both work via the friendly path.

| Data | Syncs via iCloud | Notes |
|---|---|---|
| All workspace .md files | Yes | Hand-editable on any synced device |
| `.meta.json` | Yes | Includes device list — auto-registers new devices |
| `session-logs/` | Yes | Per-day files |
| `reports/` | Yes | Monthly reports available everywhere |
| Apple Reminders | Already cloud | Independent iCloud sync |
| Google Calendar / Sheets | Already cloud | Independent sync |
| Composio account state | Already cloud | Stored server-side |

**Conflict handling:** iCloud creates conflict copies (e.g., `contacts 2.md`). On next session, skill detects conflict copies and prompts resolution with diff summary.

**New device detection:** On first launch on a device not in `.meta.json.devices[]`, auto-add device name and verify Composio + native MCP connections (may need re-auth per device).

## Rules Engine

### How rules work

Rules run automatically before every triage. They process messages using this resolution order:

1. **Global rules** apply first (across all inboxes).
2. **Per-inbox rules** apply second (only to messages in their assigned inbox).
3. **Conflict resolution:** specific scope wins (per-inbox overrides global if both match).
4. **VIP-related rules** are inherently global and never per-inbox-scoped.
5. **Stakes determine apply behavior:**
   - `low_stakes` → execute silently, log to session log, summarize at triage start
   - `high_stakes` → always confirm with user before executing each instance, even after rule approval

### Rule structure

```markdown
### Rule: [Name]
- **Type:** delete | prioritize | folder | organize
- **Stakes:** low_stakes | high_stakes
- **Scope:** per-inbox: [alias] | global
- **Status:** Active | Paused
- **Trigger:**
  - Sender: [email, domain, or pattern]
  - Subject contains: [keywords]
  - Body contains: [keywords]
  - Time received: [window]
  - Sender flagged as junk: [X]+ times
  - No reply after: [time period]
  - Thread length exceeds: [count]
- **Action:**
  - Categorize as: [🔴 / 🟡 / 🗑️ / 🔕]
  - Label: [label name]
  - Mark as: [read / starred]
  - Forward to: [email]                       ← high_stakes default
  - Auto-draft using: [template]              ← low_stakes (drafts only)
  - Auto-reply: [template]                    ← high_stakes default
  - Create task: [priority]
  - Create reminder in: [time]
  - Archive / Trash                           ← low_stakes default
  - Move to folder: [synthetic name]          ← low_stakes default
  - Snooze until: [time]
  - Escalate to: 🔴 HIGH
- **Exceptions:**
  - Sender is VIP
  - Subject contains: [override keywords]
- **Created:** [date]
- **Last triggered:** [date]
- **Times triggered:** [count]
```

### Default stakes by action type

| Action | Default Stakes | Why |
|---|---|---|
| Categorize / label / mark | low_stakes | Reversible metadata |
| Archive | low_stakes | Reversible |
| Move to folder | low_stakes | Reversible |
| Auto-junk / trash | low_stakes | Recoverable from trash |
| Permanent delete | **high_stakes** | Irreversible |
| Auto-forward | **high_stakes** | Touches another human |
| Auto-reply / template send | **high_stakes** | Touches another human |
| Auto-draft | low_stakes | Drafts only, user reviews before send |
| Unsubscribe | low_stakes | Reversible (re-subscribe) |
| VIP escalate / VIP-related | low_stakes (always global) | Just metadata |

User can override default stakes during rule creation in `/create-rule`.

### Standard Rules (suggested during onboarding)

| Category | Rule | Default Action | Stakes |
|---|---|---|---|
| Social Notifications | LinkedIn, Instagram, Facebook, X | 🗑️ Auto-junk | low |
| Shipping Confirmations | Amazon, UPS, FedEx, USPS | 🟡 Label "Orders", mark read | low |
| Marketing Emails | Promotional emails | 🗑️ Auto-junk | low |
| Financial Alerts | Bank alerts, payment confirmations | 🟡 Label "Finance" | low |
| App Notifications | GitHub, Jira, Trello, Asana, Notion | 🟡 Bundle into digest | low |
| Calendar Confirmations | Accepted/declined notifications | Mark read, archive | low |
| VIP Priority | Emails from VIP contacts | Always 🔴 RESPOND | low (global) |
| Urgency Keywords | "urgent", "ASAP", "deadline", "EOD" | Escalate to 🔴 HIGH | low |
| Stale Follow-Up | User-sent emails with no reply 3+ days | Create followup reminder | low |
| New Sender Alert | First-time sender | Flag "New sender — verify" | low |
| Quiet Hours | Messages received between [X PM - Y AM] | Hold for morning triage | low |
| Newsletter Digest | Newsletters user reads | Bundle into weekly digest | low |
| Bot/Automated | System notifications | Skip triage unless keyword match | low |

All Standard Rules default to per-inbox scope when applied during setup.

### Learned rule suggestions

Three categories: **delete**, **prioritization**, **organization**. Suggestions queue in `rules-review-queue.md` with proposed scope and stakes. Cadence configurable: every triage / every 3rd / weekly / monthly / on demand.

**Trigger patterns** (selection — full list preserved from v1.3):

#### Delete suggestions
- Same sender junked 3+ times → "Auto-delete from [sender]?"
- User never opens emails from sender 5+ times → "Auto-delete + unsubscribe?"
- All from a domain always deleted → "Auto-delete domain @[X]?"

#### Prioritization suggestions
- User responds within 1 hour → "Mark [sender] as VIP?"
- User always forwards invoices → "Auto-forward invoices to [person]?"
- User always reads sender's emails immediately → "Prioritize above other 🟡?"
- Cross-inbox correspondence pattern → "[sender] emails 2+ of your accounts — VIP candidate?"
- Fireflies meeting frequency → "You met with [X] 3+ times in 30d — VIP candidate?"

#### Organization suggestions
- Same email type always labeled → "Auto-label [type] as [label]?"
- Same email type always foldered → "Auto-route [sender] to [folder]?"
- Similar drafts repeatedly → "Create a template?"

### Folder rules — synthetic abstraction

Inbox Command Center defines 7 logical "buckets" that map to platform-native implementations:

| Logical folder | Gmail | Outlook / IMAP |
|---|---|---|
| Low Priority | Label `ICC/Low Priority` | Subfolder `Inbox/ICC/Low Priority` |
| Newsletters | Label `ICC/Newsletters` | Subfolder `Inbox/ICC/Newsletters` |
| Receipts & Orders | Label `ICC/Receipts` | Subfolder `Inbox/ICC/Receipts` |
| Finance | Label `ICC/Finance` | Subfolder `Inbox/ICC/Finance` |
| Automated/Bot | Label `ICC/Bot` | Subfolder `Inbox/ICC/Bot` |
| Pending Review | Label `ICC/Pending` | Subfolder `Inbox/ICC/Pending` |
| Delegated | Label `ICC/Delegated` | Subfolder `Inbox/ICC/Delegated` |

The skill abstraction `route_to_folder(inbox_id, message_id, folder_alias)` dispatches to the right tool per platform (`GMAIL_BATCH_MODIFY_MESSAGES` add label, or `OUTLOOK_MOVE_MESSAGE`).

**Per-inbox enablement.** Setup wizard asks per-inbox which folders to enable. Folders auto-create on the platform when enabled. Tracked in `.meta.json.connected_inboxes[i].folders_enabled[]`.

**Default folder behavior:**

| Folder | Default Review | Auto-Action |
|---|---|---|
| Low Priority | Weekly digest | Archive 30d, delete 90d |
| Newsletters | Weekly digest | Delete 14d unread |
| Receipts & Orders | Never (searchable) | Keep |
| Finance | Daily digest | Keep |
| Automated/Bot | Daily count | Delete 7d |
| Pending Review | Every triage | Remind 3d |
| Delegated | Daily | Remind 5d if no response |

**Global rule + missing folder behavior:** if a global folder rule references a folder not enabled in some inbox, auto-enable it silently and route. User sees the folder appear after first match.

### Rules storage

`rules.md` for active rules; `rules-review-queue.md` for pending suggestions. Folder rules are a sub-type of rules with `Type: folder` — stored in the same `rules.md` file rather than a separate file (simpler than v1.3's split).

## Voice Profile

### Sources, in priority order

1. **Fireflies meeting transcripts** — primary, highest authenticity (you actually talking)
2. **Sent email analysis** — written voice patterns
3. **Slack messages** — internal/casual register
4. **iMessage / SMS** — most casual
5. **Continuous draft-edit learning** — every edit feeds voice + per-recipient `contacts.md` notes
6. **A/B calibration** — explicit preference testing

Voice profile is **unified across all inboxes** — one user, one voice. Brand voice (BKC) is a second profile applied to recipients tagged `[Brand]` in `contacts.md`.

### Initial setup (in `/setup-wizard`)

1. Connect Fireflies (recommended).
2. **Pull last 30 days of transcripts (blocking, ~1-3 min).**
3. Pull last 30 days of sent email across all inboxes.
4. Analyze Slack last 30 days.
5. Analyze iMessage last 30 days.
6. Run A/B calibration (20+ pairs across email / Slack / SMS / formal scenarios).
7. Generate `voice-profile.md` and `voice-profile-brand.md` (if BKC connected).

### Weekly Fireflies pull (scheduled)

Cadence: weekly off-hours by default. Configurable.

```
Pull Fireflies transcripts since last_fireflies_pull
  ↓
Pass 1 (voice extraction):
  → phrasing, decision language, register shifts, new phrases, sign-offs
  → append to voice-profile.md (flagged for next monthly review if substantial)

Pass 2 (per-participant extraction):
  → tone observations per person you spoke with
  → append to contacts.md under each name's section
  → IF person not in contacts.md:
       create entry ONLY IF they're a VIP or appear in user's sent mail
       (avoids bloat from one-off transcript participants)

Update .meta.json.last_fireflies_pull = today
Log to session-logs/YYYY-MM-DD.md
```

### Triage-time enrichment

When an email arrives from someone who appeared in a Fireflies transcript in the last 30 days, surface inline:

```
[#3] 🔴 HIGH — Bryan Howell <bryan@dieselpowerproducts.com>
📞 You spoke with Bryan May 3 (Q3 numbers call) — context continues
Subject: Re: Q3 numbers — confirming next steps
```

Lets the user draft replies that pick up where the conversation left off, not where the email thread did.

### Continuous learning from edits

Every time the user edits a draft before sending:
1. Compute diff between draft and final
2. Tag the edit type (tone / wording / structure / sign-off / cc)
3. Update `contacts.md` under that recipient with the observation (under a "Voice notes" sub-section)
4. Increment `voice_drift_counter` in `.meta.json` if substantial (>10% character change OR sign-off / greeting / structure shift)

### Drift-triggered A/B

If `voice_drift_counter >= 3` in a single session, at session end:

> "I noticed 3 substantial edits this session. Want a quick 5-pair A/B to recalibrate the areas that drifted? (~2 min)"

If user accepts, generate 5 A/B pairs targeting the scenarios that triggered the edits. Reset counter after.

### Mandatory monthly voice review

Cadence configurable: monthly (default), bi-weekly, weekly. Stored in `.meta.json.schedules.voice_review_cadence`.

When due, on first triage of the day:

```
🎙️ VOICE PROFILE REVIEW — Due

Last reviewed [N] days ago.

WHAT'S CHANGED:
├── Fireflies: [N] new transcripts ingested
├── Email: [N] new sent items analyzed
├── Slack: [N] new messages analyzed
├── iMessage: [N] new messages analyzed
├── Edits: [N] substantial draft edits captured

DETECTED SHIFTS:
├── [Description of any drift]

[Full review (re-analyze + A/B)] [Quick review (no A/B)] [Snooze 1 week] [Change cadence]
```

### Voice profile storage

```markdown
# Voice Profile — [User's Name]

## Generated From
- Fireflies transcripts: [X] from [date range] — primary signal
- Sent email analysis: [X] emails from [date range]
- Slack messages: [X] messages
- iMessage/SMS: [X] messages
- A/B calibration: [X] pairs tested
- Last updated: [date]

## Core Style
[3-5 sentence summary]

## Greetings
| Audience | Greeting | Example |
|---|---|---|
| Close colleagues | [pattern] | [real example] |
| Clients | [pattern] | [real example] |
| New contacts | [pattern] | [real example] |
| Quick replies | [pattern] | [real example] |

## Sign-Offs
| Context | Sign-off |
|---|---|
| Standard | [pattern] |
| Warm/relationship | [pattern] |
| Quick/casual | [pattern] |

## Signature Phrases
[Phrases the user actually uses, with context]

## NEVER List
[Words, phrases, and patterns the user would never write]

## Structure Pattern
[How they typically structure messages]

## Tone by Audience
| Audience | Tone | Example |
|---|---|---|
| Team/internal | [description] | [example] |
| Clients | [description] | [example] |
| Vendors/partners | [description] | [example] |
| Personal/casual | [description] | [example] |

## Channel Differences
| Channel | How Style Differs |
|---|---|
| Email | [description] |
| Slack | [description] |
| iMessage | [description] |
| SMS | [description] |

## Email Length Preference
[Typical length + when they go longer/shorter]

## A/B Calibration Results
[Key preferences captured]

## Review History
| Date | Sources Analyzed | Key Changes | A/B Pairs Tested |
|---|---|---|---|
| [date] | Fireflies 14, email 45, Slack 200 | Tone shifted casual, new sign-off | 5 pairs |
```

### Two-voice system

If Brand Knowledge Center is connected:
- **Personal voice** (from `voice-profile.md`) — internal/casual contacts (default)
- **Brand voice** (from `voice-profile-brand.md`, sourced from BKC `brand-identity.md`) — recipients tagged `[Brand]` in `contacts.md`
- Auto-select based on recipient tag. Ask if ambiguous.

## Email Triage

### Step 1: Time Range and Inbox Selection

Ask: "When did you last check email?" or accept stated timeframe.

For multi-account users: "Which inbox today, or all of them?" Default behavior:
- **Single inbox** if user names one ("triage uno-mas")
- **Sequential** if user says "triage" or "all" — see Step 1.5

### Step 1.5: VIP Cross-Inbox Scan (always runs first)

Before user picks a single inbox, scan ALL connected inboxes for VIP messages.

```
For each inbox in connected_inboxes:
  GMAIL_FETCH_EMAILS / OUTLOOK_FETCH_MESSAGES with query:
    "is:unread after:[last_check] from:[any VIP email in contacts.md]"
  → collect VIP messages across inboxes
```

Surface results:

```
3 VIP messages waiting across your inboxes:
  • Bryan Howell — re: Q3 numbers (in: uno-mas)        ← 14 min ago
  • Joel Barbour — re: Great PNW campaign (in: personal) ← 2 hr ago
  • Melissa — quick favor (in: personal)               ← 4 hr ago

Handle these first, or proceed to inbox triage? Which inbox?
```

If user handles VIPs first, run VIP Immediate Alert flow for each (full body + pre-written draft). Then return to inbox selection.

### Step 2: Pull Messages

Per the selected inbox(es), execute Composio fetch. Two parallel fetches:

```
COMPOSIO_MULTI_EXECUTE_TOOL with two calls:
  Fetch 1 — Starred:
    GMAIL_FETCH_EMAILS / OUTLOOK_FETCH_MESSAGES
    query: "is:starred is:unread"
    max_results: 20
    verbose: true

  Fetch 2 — Unread inbox:
    GMAIL_FETCH_EMAILS / OUTLOOK_FETCH_MESSAGES
    query: "in:inbox is:unread after:[date]"
    max_results: 50
    verbose: true
```

Deduplicate by messageId. Sort by most recent first.

If multi-inbox sequential: tag each message with its inbox alias.

### Step 3: Apply Rules and Route to Folders

Before showing anything to the user, run through the emails and apply approved rules per the resolution order (global → per-inbox).

For `low_stakes` rules: execute silently, log to session log, summarize at start of triage:

```
Auto-rules applied to [inbox]:
  ✓ Archived 8 newsletters
  ✓ Labeled 3 receipts as Finance
  ✓ Marked 6 calendar invites as read
```

For `high_stakes` rules: queue the proposed action and present it to the user for per-instance confirmation (same flow as v1.3 high-stakes pattern).

### Step 4: VIP Immediate Alert (per inbox)

```
🚨 VIP EMAIL — [Sender Name] [Relationship from contacts.md]

From: [Full Name] <[email]>
Inbox: [inbox alias]
Subject: [Subject line]
Received: [Day, Date, Time]
Thread: [New / Reply in thread of X messages]

[Optional Fireflies enrichment line if recent transcript exists]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FULL EMAIL:
[Complete email body — not just a summary]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PRE-WRITTEN DRAFT REPLY:
[Draft in user's voice; brand voice if recipient tagged [Brand]]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ [Send Draft] [Edit Draft] [Rewrite Draft] [Remind Me] [Deep Dive] [Skip for now]
```

Sending account auto-matches receiving inbox.

### Step 5: Categorize Remaining Messages

🔴 RESPOND / 🟡 FYI / 🗑️ JUNK / 🔕 UNSUBSCRIBE — same definitions as v1.3.

### Step 6: Present Batch

Batch size from `.meta.json.schedules.batch_size` (default 10). For multi-inbox sequential, tag each item with `[inbox-alias]`.

```
[#1] ⭐🔴 HIGH — [Sender Name] <[email]>  [uno-mas]
Subject: [Subject line]
Received: [Day, Date, Time]
Thread ID: [...] | Message ID: [...]

[1-2 sentence summary]

→ Actions: [Draft Reply] [Reply Now] [Archive] [Trash] [Mark Read] [Add Followup] [Add Todo] [Create Rule]
```

After 10: "Ready for the next batch, or want to take action on these first?"

### Step 7: Process Actions

| Code | Action | Implementation |
|---|---|---|
| `draft` | Draft a reply in user's voice | Compose; sending account auto-matches receiving inbox |
| `reply` | Same as draft + send on confirmation | `GMAIL_REPLY_TO_THREAD` / `OUTLOOK_REPLY_MESSAGE` |
| `remind [time]` | Add to todos.md + calendar event | Append + `mcp__claude_ai_Google_Calendar__create_event` |
| `read` | Mark as read | `GMAIL_BATCH_MODIFY_MESSAGES` removeLabelIds: ["UNREAD"] |
| `delete` | Move to trash | `GMAIL_MOVE_TO_TRASH` (recoverable) |
| `unsub` | Execute unsubscribe | List-Unsubscribe header → body link → fallback rule |
| `dive` | Show full email/thread | `GMAIL_FETCH_MESSAGE_BY_THREAD_ID` |
| `delegate [name]` | Forward + add to followups.md | `GMAIL_REPLY_TO_THREAD` (forward variant) + append |
| `skip` | Leave in inbox | No-op |
| `rule` | Create a rule based on this email | Trigger `/create-rule` flow |

**Edit tracking on drafts:** when user edits before sending, compute diff. Update `contacts.md` under recipient. Increment `voice_drift_counter` if substantial.

### Step 8: Next Batch / Step 9: Triage Complete

After all batches:

1. Append summary to today's session log.
2. If `voice_drift_counter >= 3`, offer mini A/B (drift-triggered).
3. Update `followups.md` with anything sent expecting a reply.
4. Update `todos.md` with new items.
5. If pending rule suggestions, surface per cadence.
6. If a rule review or voice review is due, mention it.

## Workspace Memory — Always Read, Always Write

The skill operates on the principle that the workspace is the source of truth across sessions:

1. **Read at session start** — load all workspace files into context.
2. **Update during session** — write changes to workspace files as they happen, don't batch at end.
3. **Log meaningful events** — append to today's session log throughout.
4. **Detect user edits** — check mtimes; log user edits as observed.

Workspace files are markdown so the user can hand-edit at any time. Don't fight user edits — treat them as authoritative when the user changes something the skill had different.

## Unsubscribe Workflow

When the user assigns `unsub`, execute the unsubscribe — don't just flag it.

### Execution methods (priority order)

**1. List-Unsubscribe header (one-click)**
- Fetch full message via `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID`
- Parse the `List-Unsubscribe` header
- `mailto:` → send via `GMAIL_SEND_EMAIL` to the unsubscribe address
- `https://` → execute GET/POST request

**2. Body link extraction**
- If no header, scan body for "unsubscribe", "manage preferences", "opt out", "email preferences"
- Extract URL; for Composio-connected accounts attempt direct call, otherwise open in browser

**3. Auto-junk fallback**
- No mechanism found → create rule: auto-junk all future from sender

### Modes (per `.meta.json.schedules.unsubscribe_mode`)

- **`auto`** — execute each unsubscribe immediately during triage
- **`batch`** — collect during triage, execute at end as a confirmable queue
- **`manual`** — surface mechanism only, user handles externally

After successful unsubscribe: also create auto-junk rule (sender may still send despite unsubscribing).

## Slack Triage

Same v1.3 behavior. Categorization (🔴 / 🟡 / ⏭️). Channel rules (priority / muted / keyword alerts). Slack items integrate with email batches in same triage stream — numbered after email items.

## iMessage Triage

Same v1.3 behavior. macOS AppleScript/Shortcuts integration. Categorization, action codes (draft/remind/read/skip), reminder delivery. iMessage items numbered after Slack items in batches.

## Calendar Triage

Same v1.3 behavior via native Google Calendar MCP. For Outlook users, use Composio's Outlook Calendar slugs.

Flags: ❓ UNRESPONDED / ⚠️ CONFLICTS / 🏃 MARATHON / 📋 PREP NEEDED.

Action codes: accept / decline / tentative / reschedule / buffer / prep.

## Scheduled Reminders

Same delivery mechanics as v1.3 (Slack channel / Slack DM / iMessage). Reminder data lives in `todos.md` (with due dates) instead of Google Sheets. Standalone creation, recurring reminders, dedicated `#inbox-reminders` channel — all preserved.

```
📬 REMINDER — [Time]

[Task context]

Source: [Email from X / Slack DM from Y / Manual]
Created: [date] during triage
Task: T017 (in todos.md)

→ [Mark Done] [Snooze 1hr] [Snooze Tomorrow]
```

Per-reminder channel override: `remind tomorrow 9am via imessage`.

## Task Tracker — workspace-native

Canonical store: `todos.md` + `followups.md`. Replaces v1.3's four-backend model.

Optional one-way mirroring (workspace → external):
- **Apple Reminders** for time-bound items, mirrored to "Inbox Tasks" list (Mac users)
- **Google Calendar event** for any item with a due date (so the OS reminds you)
- **Outlook Tasks** for Outlook users (via Composio)

Mirroring is opt-in during setup wizard. Workspace remains canonical — if external and workspace diverge, workspace wins.

### Task data model in `todos.md`

```markdown
- [ ] [task description] — from [source: email / Slack / iMessage / manual] — added YYYY-MM-DD — due YYYY-MM-DD — priority HIGH/MED/LOW
```

Status flips to `- [x]` on completion. Done items kept 14 days, then auto-pruned.

### Morning integration

During morning triage, after first email batch:
> "You have N open todos — X overdue, Y due today."

Surface overdue/today items inline.

## Scheduled Daily Briefing

**Multi-account aware:** briefing aggregates across all connected inboxes with per-inbox sections.

```
☀️ Morning Briefing — [Date]

📧 EMAIL ACROSS INBOXES: [N] unread total
├── personal:  [N] unread ([X] 🔴, [Y] 🟡, [Z] 🗑️)
│   └── 🔴 [Top 1-2 RESPOND items]
├── uno-mas:   [N] unread ([X] 🔴, [Y] 🟡, [Z] 🗑️)
│   └── 🔴 [Top 1-2 RESPOND items]
└── ms365:     [N] unread

⭐ VIPs WAITING: [N] across all inboxes
├── [VIP — subject — inbox]

💬 SLACK: [X] unread ([Y] 🔴)
💬 iMESSAGE: [X] unread ([Y] 🔴)

📅 CALENDAR: [X] meetings today, [Y] unresponded, [Z] conflicts

📋 TASKS: [X] due today, [Y] overdue (todos.md)
👥 FOLLOWUPS: [N] people waiting on you (followups.md)

⚡ RULES APPLIED since last triage: [X] auto-processed
├── [X] auto-junked, [Y] auto-archived, [Z] auto-labeled, [W] auto-routed

→ Say "triage" to take action
```

Delivery: Slack DM / iMessage / Email / Calendar block / All — per `.meta.json.schedules.daily_briefing.channel`.

## Daily VIP Summary — per inbox

One digest per connected inbox. VIP person can appear in multiple digests if they email more than one of your accounts. Same delivery channel for all by default; per-inbox override available.

```
⭐ VIP SUMMARY — uno-mas — [Date]

[X] VIP communications today (this inbox)

━━━ EMAILS RECEIVED ━━━
📧 Bryan Howell — re: Q3 numbers — 14 min ago
   Status: Unread 🔴
   Last meeting: Fireflies May 3 (Q3 numbers call)

━━━ EMAILS SENT ━━━
📤 To: Tamara Kemper — re: Riverbank — 2 hr ago

━━━ ACTIVE THREADS ━━━
🔄 Bryan — re: Q3 numbers — 5 messages

━━━ PENDING ━━━
⏳ [N] VIP emails awaiting your response in this inbox

→ Say "triage uno-mas" to take action
```

## Monthly Inbox Report

**Single report**, two layers — cross-inbox unified entities and per-inbox breakdowns.

```
📊 INBOX COMMAND CENTER REPORT — [Period]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CROSS-INBOX (unified entities)

⭐ VIP COMMUNICATIONS
├── Total received: [N]    Total sent: [M]
├── Avg response time: [X]h
├── Per-VIP breakdown:
│   ├── Bryan Howell — Recv: [X] | Sent: [Y] | Avg: [Z]h | Inboxes: [list]
│   └── ...
├── VIP threads still open: [N]
├── Notable: [silent VIPs, new VIP candidates, etc.]

🎙️ VOICE PROFILE
├── Drift events this period: [N]
├── Mini A/B fires: [N]
├── Mandatory review: [completed / due]

📞 FIREFLIES INGESTED
├── Total meetings analyzed: [N]
├── New transcripts feeding contacts.md: [N]
├── New VIP candidates from meetings: [N]

⚡ GLOBAL RULES PERFORMANCE
├── Total triggers: [N]
├── Top global rules: [list]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PER-INBOX

── personal (ramsey@strategylabs.us) ──
  📧 Volume: [N] received, [M] sent
  🗑️ Deletions: [X] manual / [Y] rule / [Z] folder cleanup
  📖 Read but unanswered (RESPOND): [N]
  📂 Folder activity: [Newsletters X | Receipts Y | ...]
  ⚡ Per-inbox rules: [N] triggers
  📈 Inbox zero days: [X] of [Y] business days

── uno-mas (ramsey@unomastacos.com) ──
  [same structure]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRENDS

📈 Volume vs. last period: [+/-X%]
📈 Response time vs. last: [+/-X%]
📈 Triage efficiency: [X]% auto-handled by rules
📈 Top 5 senders: [list]
📈 New senders this period: [N] ([X] became repeat)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACTIONS DUE

├── Pending rule suggestions: [N] — [Review now]
├── VIP list review: [due / not due]
├── Voice profile review: [due / not due]
├── Stale follow-ups: [N] > 7 days (in followups.md)
```

**Source data:** primary feed is `session-logs/YYYY-MM-DD.md` files within the report period; supplemented by current state queries (folder counts via Composio, rule trigger counts from `rules.md`).

Stored at `~/Inbox Command Center/reports/[YYYY-MM].md`. Optionally delivered via Slack DM / iMessage / email per `.meta.json.schedules.inbox_report_cadence`.

## Plugin Update Notifications

Same v1.1 mechanic; v1.4 adds a targeted v1.3 → v1.4 migration branch.

When `installed_version` from `.meta.json` is older than skill version:

```
🆕 INBOX COMMAND CENTER — Updated to v[X.Y.Z]

[Brief description of what's new]

[Set up new features now] [Set up later — remind me on next 3 triages] [Show full changelog]
```

If user skips, set `pending_update` in `.meta.json`. Remind on next 3 sessions.

### v1.3 → v1.4 specific migration

If `installed_version == "1.3.0"` (or `migrated_from` is unset and old workspace path exists), trigger the migration flow described in `docs/v1.4-migration.md`. Migration is interactive, idempotent, runs entirely through the skill (no bash scripts), and preserves a v1.3 backup at `.v1.3-backup/` for 30 days.

## Error Handling

| Error | Behavior |
|---|---|
| No results | Treat as valid empty state. Widen query / date range. |
| Composio rate limit (429/403) | Back off and retry; surface to user if persistent. |
| Invalid Gmail label IDs | Call `GMAIL_LIST_LABELS` first to refresh. |
| Composio session expired | Re-run `COMPOSIO_MANAGE_CONNECTIONS` for the affected connector. |
| Tool schema not loaded | Call `COMPOSIO_GET_TOOL_SCHEMAS` for the slug before executing. |
| Workspace file missing on session start | Tell user to run setup-wizard. Don't recreate from scratch — they may have data in iCloud not yet synced. |
| iCloud conflict copy detected | Prompt user with diff summary, ask which version to keep. |
| Filesystem MCP unavailable | Tell user to check Claude config. Workspace is read-only without it. |

## Smart Behaviors

- **Batch threads** — 5 emails in one thread = summarize once; use thread_id for replies
- **Flag phishing/anomalies** — unexpected invoices, password resets, unusual requests
- **Time zone** — User's tz from `.meta.json` (Pacific Time default for SL deployment in Spokane, WA)
- **Keep FYI brief** — single line per item
- **Be decisive** — if it's junk, call it junk; user can override
- **Cross-reference** — same email + Slack DM = one item
- **Always show drafts before sending** — never auto-send without confirmation
- **Always confirm permanent delete** — trash is recoverable; batch delete is not
- **Use the workspace, don't reinvent** — check `contacts.md` before asking
- **Propose, don't impose** — when patterns appear, queue rule suggestions

## Session End

If the user signals they're done ("that's all", "thanks", "I'm good"):

1. Update `followups.md` with anything sent expecting reply
2. Update `todos.md` with anything new
3. If `voice_drift_counter >= 3`, offer mini A/B
4. Append final session-log line summary
5. Increment `session_count` in `.meta.json`
6. If pending rule review or voice review is due and skipped, mention it gently
7. Sign off briefly

## File Structure

### Plugin source (in marketplace repo)

```
plugins/inbox-command-center/
├── .claude-plugin/plugin.json   # Plugin metadata and version
├── CHANGELOG.md                 # Version history
├── README.md                    # Plugin overview
├── commands/
│   ├── setup-wizard.md
│   ├── triage.md
│   ├── create-rule.md
│   ├── voice-calibration.md
│   └── inbox-report.md
├── skills/inbox-manager/SKILL.md  # This file
└── docs/
    ├── v1.4-audit.md            # Build checklist for v1.4
    └── v1.4-migration.md        # v1.3 → v1.4 migration spec
```

### User workspace (synced via iCloud Drive — Finder-visible)

```
~/Inbox Command Center/   (symlinked from ~/Library/Mobile Documents/com~apple~CloudDocs/Inbox Command Center/)
├── .meta.json
├── contacts.md
├── todos.md
├── followups.md
├── rules.md
├── rules-review-queue.md
├── voice-profile.md
├── voice-profile-brand.md
├── session-logs/
│   └── YYYY-MM-DD.md
├── reports/
│   └── YYYY-MM.md
└── .v1.3-backup/  (only present after v1.3 → v1.4 migration; auto-removed after 30d)
```

When iCloud Drive is unavailable, fall back to local `~/Inbox Command Center/` (no sync). Warn user.
