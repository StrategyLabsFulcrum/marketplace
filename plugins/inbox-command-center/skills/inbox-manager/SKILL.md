---
name: inbox-manager
description: >
  Inbox Command Center for managing email, Slack, iMessage, and messaging platforms.
  Use when the user mentions "check my email", "inbox", "triage", "what did I miss",
  "clean up my inbox", "draft a reply", "inbox zero", "unsubscribe", "email manager",
  "comms manager", "check Slack", "check iMessage", "check my texts", "any important emails",
  "what do I need to respond to", "create a rule", "message rules", "voice profile",
  "daily briefing", "morning update", "check my messages", "send me a reminder",
  or anything related to email, messaging, or communications management.
---

# Inbox Command Center

An AI communications manager that triages email, Slack, iMessage, and messaging platforms — categorizes messages, drafts replies in the user's authentic voice, manages calendar, tracks tasks, enforces smart rules, and delivers scheduled briefings and reminders via the user's preferred channel.

## How It Works

The Inbox Command Center has seven layers:

1. **Connection Layer** — Connects to email, Slack, messaging, calendar, and meeting transcript tools via MCP or Rube.
2. **Rules Layer** — Applies user-configured rules to auto-categorize, archive, forward, label, or escalate messages before triage.
3. **Triage Layer** — Categorizes remaining messages as RESPOND, FYI, JUNK, or UNSUBSCRIBE. Presents in prioritized batches with inline actions.
4. **Voice Layer** — Maintains a living voice profile built from meeting transcripts, sent emails, and A/B calibration. Drafts replies that sound like the user.
5. **Calendar Layer** — Detects conflicts, unresponded invites, marathon blocks, and meetings needing prep.
6. **Task Layer** — Tracks reminders and follow-ups via Google Sheet + Calendar events. Delivers scheduled reminders via a dedicated Slack channel or iMessage.
7. **Briefing Layer** — Delivers scheduled daily summaries and reminders via Slack, iMessage, email, or calendar.

## Connection Methods

Tools can be connected two ways:

### Direct MCP Connection
Claude's built-in MCP integrations for:
- Gmail (read, search, draft, label)
- Slack (read channels, DMs, send messages)
- Google Calendar (read, create, respond to events)
- Fireflies.ai (meeting transcripts)

### iMessage Connection
iMessage is connected via macOS AppleScript/Shortcuts integration:
- **Read:** Pull recent iMessage conversations, unread messages, and group chats
- **Write:** Send iMessage replies and new messages to contacts
- **Scheduled reminders:** Send timed reminder messages to yourself via iMessage (alternative to Slack DM reminders)
- **Requires:** macOS with Messages app configured, iMessage account active
- **Note:** iMessage integration runs locally on the user's Mac via AppleScript automation through Rube or direct shell access

### Rube Connection
For tools not available via MCP, use Rube to connect:
- Outlook / Microsoft 365
- Otter.ai, Gong, Fathom (meeting transcripts)
- Zoom cloud recordings
- SMS platforms (Twilio, etc.)
- iMessage (via macOS AppleScript/Shortcuts as a fallback if direct connection isn't available)
- Any tool with an API that Rube can reach

### Connection Config

Stored in `inbox-command-center/config.md`:

```markdown
# Inbox Command Center — Configuration

## Connected Accounts
| Tool | Connection | Account | Status |
|------|-----------|---------|--------|
| Gmail | MCP | [email] | Active |
| Slack | MCP | [workspace] | Active |
| iMessage | AppleScript | [phone/email] | Active |
| Google Calendar | MCP | primary | Active |
| Fireflies | MCP | [account] | Active |

## Primary Email
[email] — used for drafting replies by default

## Time Zone
[timezone]

## Batch Size
[number] emails per batch (default: 10)

## Scheduled Briefing
- Delivery: [Slack DM / iMessage / Email / Calendar / None]
- Time: [HH:MM AM/PM]
- Days: [Mon-Fri / Daily / Custom]

## Reminder Delivery
- Channel: [Slack Channel / Slack DM / iMessage]
- Slack Channel: [#inbox-reminders or custom name]
- Default: [user's preference]
```

## Cross-Device Sync

The Inbox Command Center supports syncing all user data across multiple macOS devices via iCloud Drive. This ensures your configuration, voice profile, rules, VIP contacts, and triage state are consistent whether you're on your laptop or desktop.

### How It Works

All user data files are stored in a shared iCloud Drive folder instead of a local-only directory:

```
~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/
├── config.md                 # Connected tools, preferences, schedule, version tracking
├── voice-profile.md          # Living voice profile
├── vip-contacts.md           # Priority contact list with relationship tags
├── rules.md                  # Active message rules
├── rule-suggestions.md       # Pending learned suggestions
├── task-tracker-link.md      # Link to Google Sheet
└── CHANGELOG.md              # Version history and update notes
```

### Data Path Resolution

When loading or saving user data, the plugin resolves the data directory in this order:

1. **iCloud path** (preferred): `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/`
2. **Local fallback**: `inbox-command-center/` in the current working directory

On first run, the setup wizard asks whether to enable cross-device sync. If enabled, all user data is created in and read from the iCloud path. If the iCloud path is not available (e.g., iCloud Drive is disabled or not signed in), the plugin falls back to local storage and warns the user.

### What Syncs

| Data | Syncs via iCloud | Notes |
|------|-----------------|-------|
| config.md | Yes | All preferences, connected accounts, schedule, version tracking |
| voice-profile.md | Yes | Full voice profile — consistent drafting voice across devices |
| vip-contacts.md | Yes | VIP list stays current on both devices |
| rules.md | Yes | Rules apply everywhere |
| rule-suggestions.md | Yes | Learned suggestions accumulate across devices |
| task-tracker-link.md | Yes | Points to the same Google Sheet |
| Google Sheet tasks | Already cloud | Google Sheets syncs independently — no action needed |
| Google Calendar events | Already cloud | Calendar syncs independently |
| Slack reminders | Already cloud | Slack messages sync independently |

### Conflict Handling

iCloud Drive handles file-level sync automatically. In rare cases where the same file is edited on two devices simultaneously before sync completes:
- iCloud creates a conflict copy (e.g., `config 2.md`)
- On next plugin load, the plugin detects conflict copies and prompts: "A sync conflict was detected in [file]. Which version do you want to keep?" Shows a diff summary of the two versions.
- After resolution, the conflict copy is deleted

### Sync Status in Config

```markdown
## Cross-Device Sync
- Enabled: Yes
- Storage: iCloud Drive
- Path: ~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/
- Devices: [MacBook Pro, iMac]
- Last synced: [auto-managed by iCloud]
```

### Setup on a New Device

When the plugin detects that iCloud sync is enabled (the iCloud folder exists with a valid `config.md`) but is running on a device not yet listed:
1. Auto-detect the device name
2. Add it to the devices list in config
3. Confirm: "Synced! Found your Inbox Command Center config from [other device]. You're all set."
4. Verify MCP connections are active on this device (Gmail, Slack, etc. may need re-authentication per device)

## Rules Engine

### How Rules Work

Rules run automatically before every triage. They process messages in order — first match wins. Rules can be:
- **Standard rules** — Pre-built common rules suggested during setup
- **Custom rules** — Created by the user via `/create-rule`
- **Learned rules** — Suggested by the plugin based on repeated user behavior

### Rule Structure

Each rule has:

```markdown
### Rule: [Name]
- **Status:** Active / Paused
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
  - Forward to: [email]
  - Auto-draft using: [template]
  - Create task: [priority]
  - Create reminder in: [time]
  - Archive / Delete
  - Snooze until: [time]
  - Escalate to: 🔴 HIGH
- **Exceptions:**
  - Sender is VIP
  - Subject contains: [override keywords]
- **Created:** [date]
- **Last triggered:** [date]
- **Times triggered:** [count]
```

### Standard Rules (suggested during onboarding)

These are offered during setup based on inbox scan:

| Category | Rule | Default Action |
|----------|------|----------------|
| Social Notifications | LinkedIn, Instagram, Facebook, X notifications | 🗑️ Auto-junk |
| Shipping Confirmations | Amazon, UPS, FedEx, USPS tracking | 🟡 Label "Orders", mark read |
| Marketing Emails | Promotional emails, sales blasts | 🗑️ Auto-junk |
| Financial Alerts | Bank alerts, payment confirmations | 🟡 Label "Finance", keep in triage |
| App Notifications | GitHub, Jira, Trello, Asana, Notion | 🟡 Bundle into digest |
| Calendar Confirmations | Accepted/declined meeting notifications | Mark read, archive |
| VIP Priority | Emails from VIP contact list | Always 🔴 RESPOND |
| Urgency Keywords | "urgent", "ASAP", "deadline", "EOD" | Escalate to 🔴 HIGH |
| Stale Follow-Up | Emails user sent with no reply in 3 days | Create follow-up reminder |
| New Sender Alert | First-time sender not in contacts | Flag "New sender — verify" |
| Quiet Hours | Messages received between [X PM - Y AM] | Hold for morning triage |
| Newsletter Digest | Newsletters user actually reads | Bundle into weekly digest |
| Bot/Automated | Automated system notifications | Skip triage unless keyword match |

### Learned Rule Suggestions

The plugin tracks patterns and suggests rules:

| Pattern Detected | Suggestion |
|-----------------|-----------|
| Same sender junked 3+ times | "Auto-junk all from [sender]?" |
| Same email type always marked read | "Auto-archive [type]?" |
| User always forwards invoices to same person | "Auto-forward invoices to [person]?" |
| User responds to same sender within 1 hour | "Mark [sender] as VIP?" |
| User never opens emails from sender | "Unsubscribe from [sender]?" |
| User creates similar reminders for same email type | "Create recurring reminder for [type]?" |
| User drafts similar replies to same type | "Create a template for [type]?" |

Present suggestions after every 3rd triage session:
> "I've noticed some patterns. Here are rule suggestions based on your behavior this week:"

### Rules Storage

All rules stored in `inbox-command-center/rules.md`. Learned suggestions stored in `inbox-command-center/rule-suggestions.md` until approved or dismissed.

## Voice Profile System

### Building the Voice Profile

The voice profile is built from three sources during setup:

**Source A: Meeting Transcripts**
If Fireflies, Otter, Gong, Fathom, or other transcript tools are connected:
- Analyze last 30 days of transcripts
- Extract: greetings, closings, common phrases, tone shifts by audience, vocabulary, humor style, sentence structure
- Weight recent transcripts higher than older ones

**Source B: Sent Email Analysis**
Scan the connected email's sent folder (last 30-60 days):
- Greeting patterns by recipient type
- Sign-off patterns
- Average email length
- Tone range (formal ↔ casual)
- Common phrases and structures
- How they handle requests, follow-ups, difficult conversations

**Source C: A/B Voice Calibration**
After analyzing transcripts and sent emails, generate A/B comparison messages for the user to choose between. This refines the profile through direct preference testing.

### A/B Calibration Process

1. **First batch: 10 pairs** — Cover a range of scenarios:
   - Responding to a client question
   - Following up on a missed deadline
   - Saying no to a meeting request
   - Thanking someone for their work
   - Introducing yourself to a new contact
   - Asking for a favor
   - Delivering bad news
   - Quick acknowledgment
   - Scheduling a call
   - Handling a complaint

   For each scenario, present Option A and Option B with different tone/style approaches. User picks which sounds more like them (or says "neither" and explains).

2. **Second batch: Channel-specific** — After the first 10 refine the core profile:
   - 5 Slack message pairs (shorter, more casual)
   - 5 SMS pairs (ultra-short)
   - 5 formal email pairs (client-facing, longer)

3. **Continue until both options approved** — When the user says "both sound like me" on a pair, that scenario is dialed in. Keep generating new pairs for uncalibrated scenarios until all types are approved.

### Voice Profile Storage

Stored in `inbox-command-center/voice-profile.md`:

```markdown
# Voice Profile — [User's Name]

## Generated From
- Sent email analysis: [X] emails from [date range]
- Meeting transcripts: [X] transcripts from [tool name]
- A/B calibration: [X] pairs tested, [X] preferences captured
- Guided questions: [answered/skipped]
- Last updated: [date]

## Core Style
[3-5 sentence summary]

## Greetings
| Audience | Greeting | Example |
|----------|----------|---------|
| Close colleagues | [pattern] | [real example] |
| Clients | [pattern] | [real example] |
| New contacts | [pattern] | [real example] |
| Quick replies | [pattern] | [real example] |

## Sign-Offs
| Context | Sign-off |
|---------|----------|
| Standard | [pattern] |
| Warm/relationship | [pattern] |
| Quick/casual | [pattern] |

## Signature Phrases
[Phrases this person actually uses, with context for when to use each]

## NEVER List
[Words, phrases, and patterns this person would never write]

## Structure Pattern
[How they typically structure messages]

## Tone by Audience
| Audience | Tone | Example |
|----------|------|---------|
| Team/internal | [description] | [example] |
| Clients | [description] | [example] |
| Vendors/partners | [description] | [example] |
| Personal/casual | [description] | [example] |

## Channel Differences
| Channel | How Style Differs |
|---------|------------------|
| Email | [description] |
| Slack | [description] |
| iMessage | [description] |
| SMS | [description] |

## Email Length Preference
[Typical length + when they go longer/shorter]

## A/B Calibration Results
[Key preferences captured from calibration pairs]
```

### Two-Voice System

If Brand Knowledge Center is connected:
- **Personal voice** (from voice profile) — for most messages
- **Brand voice** (from BKC `brand-identity.md`) — for client-facing, marketing, or business development
- Auto-select based on recipient (VIP contact relationship tag) or ask when ambiguous

### Continuous Voice Learning

| Trigger | What Happens |
|---------|-------------|
| User edits a draft before approving | Note changes as voice corrections, update profile |
| New meeting transcripts available | Periodic re-analysis for tone evolution |
| User gives explicit feedback | Immediate update to voice profile |
| Monthly prompt | "Want me to re-analyze recent emails/calls to refresh your voice profile?" |
| User runs `/voice-calibration` | New A/B pairs for scenarios that need refinement |

## Email Triage

### Categorization

Every email goes into exactly ONE category:

#### 🔴 RESPOND — Needs a reply
- Direct questions, decisions, follow-ups
- VIP contacts (always)
- Financial/legal matters requiring action
- Meeting requests needing confirmation
- Anyone with active business relationship
- Urgency keyword matches

#### 🟡 FYI — Worth knowing, no reply needed
- Task completion notifications
- Industry news user follows
- Calendar/payment confirmations
- Business metric alerts
- Shipping confirmations

#### 🗑️ JUNK — Flag for deletion
- Marketing/promotional emails
- Social media notifications
- Cold outreach / vendor pitches
- Recruitment spam, surveys
- Software updates, PR pitches

#### 🔕 UNSUBSCRIBE — Repeat junk senders
- Senders appearing in JUNK repeatedly
- Mailing lists user never engages with

### Batch Processing

1. Pull all unread + starred emails for the time range
2. Apply rules first — auto-processed emails are reported as a summary, not individually
3. Sort remaining by: starred first → 🔴 by urgency → 🟡 → 🗑️
4. Present in batches of [configured size, default 10]
5. After each batch: "Ready for the next batch, or take action on these first?"

### Presentation Format

```
[#1] ⭐🔴 HIGH — [Sender Name] <[email]>
Subject: [Subject line]
Received: [Day, Date, Time]

[1-2 sentence summary of what's needed]

→ Actions: [Draft Reply] [Remind Me] [Mark Read] [Deep Dive] [Create Rule]
```

### Quick Action Codes

| Code | Action |
|------|--------|
| `draft` | Draft a reply in user's voice |
| `remind [time]` | Add to task tracker + calendar event + deliver via configured channel |
| `read` | Mark as read, no action |
| `delete` | Flag for deletion |
| `unsub` | Unsubscribe |
| `dive` | Pull and display full email/thread |
| `delegate [name]` | Forward to named person |
| `skip` | Leave in inbox |
| `rule` | Create a rule based on this email |

## Slack Triage

### Categorization

Same system as email:
- 🔴 RESPOND — DMs asking questions, @mentions needing decisions
- 🟡 FYI — Team updates, completed tasks, shared resources
- ⏭️ SKIP — Bot messages, conversations between others, general chatter

### Channel Rules

Channel-level rules from setup:
- **Priority channels** — Always surface (e.g., #client-alerts)
- **Muted channels** — Never surface (e.g., #random)
- **Keyword alerts** — Surface from any channel if keywords match

### Integration with Email Triage

Slack items are numbered after email items in the same batch (email #1-8, Slack #9-10, iMessage #11-12) so user can rapid-fire across all platforms in one response.

## iMessage Triage

### Connection
iMessage is connected via macOS AppleScript/Shortcuts integration. The Messages app must be running on the user's Mac.

### Categorization

Same system as email and Slack:
- 🔴 RESPOND — Direct messages asking questions, time-sensitive requests, VIP contacts
- 🟡 FYI — Confirmations, shared links/photos, casual updates
- ⏭️ SKIP — Group chat chatter, reactions, tapbacks

### Message Pulling
- Pull unread iMessage conversations since last triage
- Include both 1:1 conversations and group chats
- Prioritize VIP contacts and messages containing questions or action items
- Show contact name (matched from VIP list and contacts) alongside phone number/email

### iMessage Actions
| Code | Action |
|------|--------|
| `draft` | Draft an iMessage reply in user's voice (casual/SMS style) |
| `remind [time]` | Create task + send yourself an iMessage reminder at the specified time |
| `read` | Mark conversation as read |
| `skip` | Leave for later |

### Integration with Triage Batches
iMessage items are numbered after Slack items in the same batch so the user can rapid-fire actions across email, Slack, and iMessage in a single response.

### iMessage as Reminder Delivery Channel
Users can choose iMessage instead of (or in addition to) Slack for scheduled reminders:
- **Task reminders** — When a `remind [time]` action fires, send an iMessage to the user at the scheduled time instead of a Slack DM
- **Briefing delivery** — Morning briefings can be sent via iMessage
- **Follow-up nudges** — Stale follow-up reminders delivered via iMessage
- Configured in `config.md` under `Reminder Delivery` — user chooses Slack channel, Slack DM, or iMessage as their default reminder channel

## Scheduled Reminders

The reminder system lets users create, schedule, and deliver future reminders through their preferred channel — a dedicated Slack channel, Slack DM, or iMessage.

### Creating Reminders

Reminders can be created from multiple entry points:

| Entry Point | How |
|-------------|-----|
| **During triage** | `remind [time]` or `remind [time] via [channel]` on any message |
| **Standalone** | "Remind me to [task] at [time]" or "Set a reminder for [time]" |
| **From rules** | Rules can auto-create reminders (e.g., stale follow-ups) |
| **Recurring** | "Remind me every [Monday/day/week] to [task]" |

### Reminder Delivery Channels

| Channel | How It Works | Best For |
|---------|-------------|----------|
| **Slack Channel** | Posts reminder to a dedicated channel (e.g., `#inbox-reminders`) — created during setup or on first use | Teams who want a visible reminder log; easy to review history |
| **Slack DM** | Sends reminder as a DM to yourself | Personal/quiet reminders within Slack |
| **iMessage** | Sends reminder as an iMessage to yourself at the scheduled time | Users who live on their phone; reminders that follow you outside of work tools |

### Dedicated Slack Reminder Channel

During setup (or on first reminder if not yet configured), the plugin offers to create a dedicated Slack channel for reminders:

> "Would you like me to create a dedicated Slack channel for your reminders? This gives you a single place to see all upcoming and past reminders."
>
> - **Yes, create #inbox-reminders** — Creates a private channel named `#inbox-reminders` (or custom name)
> - **Use a different name** — User specifies channel name
> - **Use an existing channel** — User picks from existing channels
> - **No, use DMs instead** — Reminders go to Slack DM
> - **No, use iMessage** — Reminders go to iMessage

When posting to the Slack reminder channel:
```
📬 REMINDER — [Time]

[Task context / original message summary]

Source: [Email from Jim Schlosser / Slack DM from Scott / Manual]
Created: [date] during triage
Task ID: T017

→ [Mark Done] [Snooze 1hr] [Snooze Tomorrow]
```

### Reminder Format by Channel

**Slack Channel / DM:**
```
📬 Reminder: [Brief description]
Due: [time]
Context: [1-2 sentence summary of the original message or task]
Task: T017 | Source: [Email / Slack / iMessage / Manual]
```

**iMessage:**
```
📬 Reminder: [Brief description]
[1-2 sentence context]
(from Inbox Command Center)
```

### Standalone Reminder Creation

Users can create reminders outside of triage:

> "Remind me to follow up with Joel about the wholesale pricing tomorrow at 2pm"
> "Set a reminder for Friday 9am to review the Q2 projections"
> "Remind me every Monday at 8am to check the client dashboard"

The plugin:
1. Parses the task, time, and any recurrence
2. Adds to task tracker Google Sheet
3. Creates Google Calendar event
4. Schedules delivery via the user's configured channel (or asks if not yet configured)
5. Confirms: "✓ T018 created — I'll remind you to follow up with Joel tomorrow at 2pm via [channel]"

### Recurring Reminders

For recurring reminders:
- Stored in task tracker with recurrence pattern
- Each instance is scheduled independently
- After each reminder fires, the next instance is auto-scheduled
- User can cancel the series or skip individual instances
- Examples:
  - "Remind me every Monday at 9am to check the weekly report"
  - "Remind me on the 1st of every month to send invoices"
  - "Remind me every Friday at 4pm to update the client dashboard"

## Calendar Triage

### Flags

| Flag | What It Catches |
|------|----------------|
| ❓ UNRESPONDED | Events with `needsAction` or `tentative` status |
| ⚠️ CONFLICTS | Overlapping meeting times |
| 🏃 MARATHON | 3+ consecutive meetings with < 15 min gap |
| 📋 PREP NEEDED | Meetings with "review", "presentation", "pitch", or external attendees |

### Calendar Action Codes

| Code | Action |
|------|--------|
| `accept` | Accept invitation |
| `decline [reason]` | Decline with optional message |
| `tentative` | Mark tentative |
| `reschedule` | Find alternative times |
| `buffer` | Add 15-min buffer before/after |
| `prep` | Set reminder 30 min before |

## Task Tracker

### Google Sheet Structure

Sheet name: **"Inbox Task Tracker"** (created during setup if doesn't exist)

| Column | Description |
|--------|-------------|
| ID | T001, T002... |
| Created | Date added |
| Due | Target date/time |
| Source | Email, Slack, iMessage, Calendar, Manual |
| From | Sender name |
| Subject | Brief description |
| Summary | 1-2 sentence context |
| Priority | HIGH / MEDIUM / LOW |
| Status | ⬜ Open / 🔄 In Progress / ✅ Done / ⏭️ Deferred |
| Completed | Date completed |
| Notes | Follow-up notes |

### Calendar Reminder Integration

When a task is created:
1. Add row to Google Sheet
2. Create Google Calendar event: "📬 [Task ID]: [Description]"
3. Event description includes task context + link to sheet
4. Schedule reminder delivery via the user's configured channel (Slack channel, Slack DM, or iMessage)

### Morning Integration

During morning triage, after email/Slack batch 1:
- Surface tasks due today or overdue
- "You also have [X] open tasks — [X] overdue, [X] due today."

## Scheduled Daily Briefing

### Delivery Methods

| Method | How It Works |
|--------|-------------|
| **Slack DM** | Auto-send summary to user at configured time |
| **iMessage** | Send summary as an iMessage to the user at configured time |
| **Email Digest** | Send summary email to user's inbox |
| **Calendar Block** | Create/update recurring event with briefing in description |
| **All** | Maximum coverage — deliver via all connected channels |

### Briefing Content

```
☀️ Morning Briefing — [Date]

📧 EMAIL: [X] unread ([X] 🔴 need response, [X] 🟡 FYI, [X] 🗑️ junk)
├── 🔴 [Top 3 RESPOND items with sender + subject + 1-line summary]

💬 SLACK: [X] unread ([X] 🔴 need response)
├── 🔴 [Top items]

💬 iMESSAGE: [X] unread ([X] 🔴 need response)
├── 🔴 [Top items]

📅 CALENDAR: [X] meetings today, [X] unresponded, [X] conflicts
├── [Any flags]

📋 TASKS: [X] due today, [X] overdue
├── [Top items]

⚡ RULES APPLIED: [X] messages auto-processed since last triage
├── [X] auto-junked, [X] auto-archived, [X] auto-labeled

→ Say "triage" to take action
```

### Briefing Schedule Config

```markdown
## Scheduled Briefing
- **Delivery:** Slack DM / iMessage / Email / Calendar / All
- **Time:** 7:30 AM
- **Days:** Monday through Friday
- **Include:** Email summary, Slack summary, iMessage summary, Calendar flags, Task reminders, Rules summary
```

## Plugin Update Notifications

When the Inbox Command Center (or any Strategy Labs marketplace plugin) is updated, the plugin detects the version change and presents the user with a guided update message on the next session. This is powered by the marketplace-wide update notification system (see `UPDATE-NOTIFICATIONS.md` at the marketplace root).

### How It Works

1. Each plugin stores its installed version in `config.md` under `Plugin Version`
2. The plugin's `CHANGELOG.md` tracks all version changes with new features, connections, and setup steps
3. On load, the plugin compares the installed version vs. the current plugin version
4. If a new version is detected, the plugin presents an update briefing before any other action

### Update Briefing Format

```
🆕 INBOX COMMAND CENTER — Updated to v1.2.0

Here's what's new:

NEW FEATURES:
├── 🔄 Cross-Device Sync — Config, voice profile, rules, and VIP contacts sync across Macs via iCloud
├── 💬 iMessage Integration — Read, write, and triage iMessages alongside email and Slack
├── ⏰ Scheduled Reminders — Create, schedule, and deliver reminders via Slack channel, Slack DM, or iMessage
├── 📢 Dedicated Slack Reminder Channel — All reminders in one place (#inbox-reminders)
├── 🔁 Recurring Reminders — "Remind me every Monday at 9am to..."

SETUP NEEDED:
├── 1. Cross-Device Sync — Enable iCloud sync for your config and data [Set up now / Skip]
├── 2. iMessage — Connect your iMessage account [Set up now]
├── 3. Reminder Channel — Choose where reminders are delivered [Configure]
├── 4. Slack Reminder Channel — Create #inbox-reminders [Create now / Skip]

[Set up all new features] [Set up later] [Show full changelog]
```

### Guided Setup for New Features

When the user chooses "Set up all new features" or "Set up now" on any item:
- Walk through only the new/changed setup steps (not the full setup wizard)
- Pre-fill existing configuration where possible
- Update `config.md` with new settings
- Mark the update as acknowledged

If the user chooses "Set up later":
- Save a flag in `config.md`: `pending_update_setup: v1.1.0`
- On next triage, show a brief reminder: "You have new features from v1.1.0 that need setup. Say 'set up updates' to configure."
- After 3 reminders, stop prompting (user can always say "set up updates" manually)

### Version Tracking in Config

```markdown
## Plugin Version
- Installed: 1.1.0
- Last update acknowledged: 1.1.0
- Pending setup: none
```

## File Structure

### Plugin Source (in marketplace repo)
```
plugins/inbox-command-center/
├── .claude-plugin/plugin.json   # Plugin metadata and version
├── CHANGELOG.md                 # Version history and update notes
├── README.md                    # Plugin overview
├── commands/                    # Command files (setup-wizard, triage, create-rule, voice-calibration)
└── skills/inbox-manager/SKILL.md  # This file — full skill documentation
```

### User Data (synced via iCloud or local)

When cross-device sync is enabled:
```
~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/
├── config.md                 # Connected tools, preferences, schedule, version tracking, sync settings
├── voice-profile.md          # Living voice profile
├── vip-contacts.md           # Priority contact list with relationship tags
├── rules.md                  # Active message rules
├── rule-suggestions.md       # Pending learned suggestions
└── task-tracker-link.md      # Link to Google Sheet
```

When local only:
```
inbox-command-center/
├── config.md
├── voice-profile.md
├── vip-contacts.md
├── rules.md
├── rule-suggestions.md
└── task-tracker-link.md
```
