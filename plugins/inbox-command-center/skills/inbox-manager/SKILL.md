---
name: inbox-manager
description: >
  Inbox Command Center for managing email, Slack, iMessage, and messaging platforms.
  Use when the user mentions "check my email", "inbox", "triage", "what did I miss",
  "clean up my inbox", "draft a reply", "inbox zero", "unsubscribe", "email manager",
  "comms manager", "check Slack", "check iMessage", "check my texts", "any important emails",
  "what do I need to respond to", "create a rule", "message rules", "voice profile",
  "daily briefing", "morning update", "check my messages", "send me a reminder",
  "inbox report", "email report", "email stats", "VIP contacts", "VIP summary",
  "voice review", "calibrate my voice", "folder rules", "low priority emails",
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
6. **Task Layer** — Tracks reminders and follow-ups via Apple Reminders, a markdown task list, ClickUp, or Google Sheets. Delivers scheduled reminders via a dedicated Slack channel or iMessage.
7. **Briefing Layer** — Delivers scheduled daily summaries and reminders via Slack, iMessage, email, or calendar.

## Connection Methods

Tools can be connected two ways:

### Direct MCP Connection
Claude's built-in MCP integrations for:
- Gmail (read, search, draft, label) — **draft only via MCP; cannot send directly. Connect Gmail via Rube for full read + write/send.**
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
For tools not available via MCP, or for full email read + write/send capability, use Rube:
- **Gmail** — Full read + write/send (vs. MCP which is draft-only). Recommended if you want approved drafts sent automatically.
- **Outlook / Microsoft 365** — Full read + write/send
- Otter.ai, Gong, Fathom (meeting transcripts)
- Zoom cloud recordings
- SMS platforms (Twilio, etc.)
- iMessage (via macOS AppleScript/Shortcuts as a fallback if direct connection isn't available)
- Any tool with an API that Rube can reach

**Gmail: MCP vs. Rube**
| Capability | Gmail MCP | Gmail via Rube |
|-----------|-----------|---------------|
| Read emails | ✅ | ✅ |
| Search | ✅ | ✅ |
| Create drafts | ✅ | ✅ |
| Label / archive | ✅ | ✅ |
| Send directly | ❌ | ✅ |

When Gmail is connected via MCP only, the triage send prompt reads "Save as draft" — the user sends manually from Gmail. When connected via Rube, the prompt reads "Send" — it sends immediately after approval.

### Connection Config

Stored in `inbox-command-center/config.md`:

```markdown
# Inbox Command Center — Configuration

## Connected Accounts
| Tool | Connection | Account | Status | Send Capability |
|------|-----------|---------|--------|----------------|
| Gmail | MCP | [email] | Active | Draft only |
| Gmail | Rube | [email] | Active | Full read + write |
| Outlook | Rube | [email] | Active | Full read + write |
| Slack | MCP | [workspace] | Active | Full read + write |
| iMessage | AppleScript | [phone/email] | Active | Full read + write |
| Google Calendar | MCP | primary | Active | — |
| Fireflies | MCP | [account] | Active | — |

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

## Task Tracker
- Backend: [apple-reminders / markdown / clickup / google-sheets / calendar-only / none]
- Location: [list name / file path / sheet URL / list ID]

## Unsubscribe
- Mode: [auto / batch / manual]

## VIP Review
- Last reviewed: [date]
- Frequency days: [14 / 30 / 90 / never]
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
├── folder-rules.md           # Folder-based rules and settings
├── rule-suggestions.md       # Pending learned suggestions
├── tasks.md                  # Task list (if markdown backend selected)
├── task-tracker-link.md      # Link to Google Sheet or ClickUp (if external backend selected)
├── reports/                  # Monthly inbox reports
│   └── [YYYY-MM].md
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
| folder-rules.md | Yes | Folder rules consistent across devices |
| rule-suggestions.md | Yes | Learned suggestions accumulate across devices |
| reports/ | Yes | Monthly reports available on all devices |
| tasks.md | Yes | Markdown task list syncs with all other data (if markdown backend selected) |
| task-tracker-link.md | Yes | Points to the same external task tracker (if Google Sheets or ClickUp selected) |
| Apple Reminders tasks | Already cloud | Reminders sync via iCloud independently — no action needed |
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

The plugin tracks patterns and suggests rules across three categories:

#### Delete Rules
| Pattern Detected | Suggestion |
|-----------------|-----------|
| Same sender junked 3+ times | "Auto-delete all from [sender]?" |
| User never opens emails from sender | "Auto-delete + unsubscribe from [sender]?" |
| User deletes all emails matching a pattern | "Auto-delete emails with [subject pattern]?" |
| Emails from a domain always deleted | "Auto-delete all from @[domain]?" |
| User deletes without reading from sender 5+ times | "Permanently block [sender]? (auto-delete, skip trash)" |

#### Prioritization Rules
| Pattern Detected | Suggestion |
|-----------------|-----------|
| User responds to same sender within 1 hour | "Mark [sender] as VIP?" |
| User always forwards invoices to same person | "Auto-forward invoices to [person]?" |
| User stars emails from a sender every time | "Escalate [sender] to 🔴 HIGH automatically?" |
| User always reads a sender's emails immediately | "Prioritize [sender] above other 🟡 FYI?" |
| User repeatedly creates tasks from a sender's emails | "Auto-create task for emails from [sender]?" |
| Emails from a domain always triaged first | "Move @[domain] to top of batch?" |
| User always replies to emails with specific keywords | "Escalate emails containing [keywords] to 🔴?" |

#### Organization Rules
| Pattern Detected | Suggestion |
|-----------------|-----------|
| Same email type always marked read | "Auto-archive [type]?" |
| User creates similar reminders for same email type | "Create recurring reminder for [type]?" |
| User drafts similar replies to same type | "Create a template for [type]?" |
| User always labels a sender's emails the same way | "Auto-label [sender] as [label]?" |
| Emails from a sender always routed to a folder | "Auto-route [sender] to [folder]?" |

#### Rule Suggestion Review Cadence

Users choose how often they review rule suggestions during onboarding. Options:

| Cadence | When Suggestions Are Presented |
|---------|-------------------------------|
| **Every triage** | After each triage session, show any new suggestions |
| **Every 3rd triage** (default) | After every 3rd triage session |
| **Weekly** | Once per week, at the start of the first triage of the week |
| **Monthly** | Bundled into the monthly inbox report |
| **On demand only** | Never auto-present — user must say "show rule suggestions" |

Stored in config:
```markdown
## Rule Suggestions
- Review cadence: [every triage / every 3rd triage / weekly / monthly / on demand]
- Last reviewed: [date]
- Pending suggestions: [count]
```

When presenting suggestions:
> "I've noticed some patterns. Here are rule suggestions based on your behavior:"
>
> **DELETE RULES:**
> - "You've deleted emails from [sender] 5 times. Auto-delete future emails from them?" [Enable / Dismiss]
>
> **PRIORITIZATION RULES:**
> - "You respond to [sender] within an hour every time. Add them as VIP?" [Enable / Dismiss]
>
> **ORGANIZATION RULES:**
> - "You always label invoices as 'Finance'. Auto-label them?" [Enable / Dismiss]
>
> "[Enable all / Review each / Dismiss all / Change review cadence]"

### Folder-Based Rules

The plugin supports folder-based organization with custom review settings for each folder. Folders act as holding zones with their own triage behavior.

#### Folder Structure

```markdown
### Folder: [Name]
- **Purpose:** [description]
- **Priority level:** HIGH / MEDIUM / LOW / ARCHIVE
- **Auto-route rules:** [which emails go here]
- **Review cadence:** [every triage / daily digest / weekly digest / monthly digest / never]
- **Review style:** [individual items / summary only / count only]
- **Auto-actions:**
  - After [X] days unread: [archive / delete / escalate / remind]
  - After [X] days in folder: [archive / delete / keep]
- **Created:** [date]
- **Email count:** [current count]
```

#### Standard Folders (suggested during onboarding)

| Folder | Purpose | Default Review | Default Auto-Action |
|--------|---------|---------------|-------------------|
| **Low Priority** | Emails that aren't urgent but shouldn't be deleted | Weekly digest summary | Archive after 30 days unread |
| **Newsletters** | Newsletters user actually reads | Weekly digest | Delete after 14 days unread |
| **Receipts & Orders** | Purchase confirmations, shipping updates | Never (searchable archive) | Keep indefinitely |
| **Finance** | Bank alerts, invoices, payment confirmations | Daily digest | Keep indefinitely |
| **Automated/Bot** | CI/CD notifications, system alerts, app notifications | Daily summary (count only) | Delete after 7 days |
| **Pending Review** | Emails user wants to come back to | Every triage | Remind after 3 days |
| **Delegated** | Emails forwarded to someone else, awaiting their response | Daily check | Remind after 5 days if no response |

#### Low Priority Folder — Special Behavior

The Low Priority folder has enhanced settings for managing email noise without losing potentially useful messages:

```markdown
### Folder: Low Priority
- **Purpose:** Non-urgent emails that don't need immediate attention
- **What goes here:**
  - Emails from senders not on VIP list and not flagged 🔴
  - Newsletters user sometimes reads
  - CC'd emails where user isn't primary recipient
  - Internal FYI announcements
  - Vendor/partner updates that aren't time-sensitive
- **Review cadence:** Weekly digest (default) — configurable
- **Review style:** Summary with counts by sender/type
- **Digest format:**
  > 📂 LOW PRIORITY DIGEST — [X] emails this week
  > ├── [X] from newsletters ([list top 3 senders])
  > ├── [X] CC'd threads ([list top 3])
  > ├── [X] vendor updates ([list top 3])
  > ├── [X] internal FYI ([list top 3])
  > └── Oldest unread: [X] days
  >
  > [Review all] [Delete all read] [Archive all > 30 days] [Skip]
- **Auto-actions:**
  - After 30 days unread: Archive (move to All Mail, remove from folder)
  - After 90 days unread: Delete
  - If sender escalates (sends follow-up or marks urgent): Move to inbox for next triage
```

#### Folder Review Settings

Users configure how each folder is reviewed:

| Setting | Options |
|---------|---------|
| **Review cadence** | Every triage / Daily / Weekly / Monthly / Never / On demand |
| **Review style** | Individual items (full triage) / Summary with drill-down / Count only / Skip |
| **Presentation order** | Before main triage / After main triage / Separate session |
| **Notification** | Include in briefing / Include in inbox report only / Silent |

#### Folder Rules in Config

```markdown
## Folder Rules
| Folder | Review Cadence | Review Style | Auto-Action | Notification |
|--------|---------------|-------------|-------------|-------------|
| Low Priority | Weekly digest | Summary | Archive 30d, Delete 90d | Briefing |
| Newsletters | Weekly | Summary | Delete 14d unread | Report only |
| Receipts & Orders | Never | — | Keep | Silent |
| Finance | Daily | Summary | Keep | Briefing |
| Automated/Bot | Daily | Count only | Delete 7d | Report only |
| Pending Review | Every triage | Individual | Remind 3d | Briefing |
| Delegated | Daily | Individual | Remind 5d | Briefing |
```

### Rules Storage

All rules stored in `inbox-command-center/rules.md`. Folder rules stored in `inbox-command-center/folder-rules.md`. Learned suggestions stored in `inbox-command-center/rule-suggestions.md` until approved or dismissed.

## Voice Profile System

### Building the Voice Profile

The voice profile is built from five sources during setup and refined continuously:

**Source A: Meeting Transcripts & Phone Calls**
If Fireflies, Otter, Gong, Fathom, or other transcript tools are connected:
- Analyze last 30 days of transcripts (meetings, phone calls, video calls)
- Extract: greetings, closings, common phrases, tone shifts by audience, vocabulary, humor style, sentence structure
- Weight recent transcripts higher than older ones
- Phone call transcripts are especially valuable for capturing the user's natural, unscripted voice

**Source B: Sent Email Analysis**
Scan the connected email's sent folder (last 30-60 days):
- Greeting patterns by recipient type
- Sign-off patterns
- Average email length
- Tone range (formal ↔ casual)
- Common phrases and structures
- How they handle requests, follow-ups, difficult conversations

**Source C: Slack Message Analysis**
If Slack is connected, analyze the user's sent messages (last 30 days):
- Tone and formality by channel (public vs. DM vs. thread)
- Emoji and reaction usage patterns
- Message length by context
- How they give feedback, ask questions, and acknowledge work
- Differences between team-facing and client-facing channels
- Common Slack-specific phrases and shorthand

**Source D: iMessage / SMS Analysis**
If iMessage is connected, analyze sent messages (last 30 days):
- Casual tone patterns
- Abbreviation and emoji usage
- How style differs between personal and professional contacts
- Response patterns (length, tone, speed)

**Source E: A/B Voice Calibration**
After analyzing all available sources, generate A/B comparison messages for the user to choose between. This refines the profile through direct preference testing.

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
| New phone call transcripts available | Re-analyze for natural speech patterns |
| User gives explicit feedback | Immediate update to voice profile |
| User runs `/voice-calibration` | New A/B pairs for scenarios that need refinement |

### Mandatory Monthly Voice Review

The voice profile **must** be revisited at least once per month. Users can optionally increase this frequency.

#### Review Cadence Config

```markdown
## Voice Profile Review
- Review cadence: [monthly / bi-weekly / weekly]
- Last reviewed: [date]
- Next review due: [date]
- Review sources: [transcripts, email, slack, imessage] (which sources to re-analyze)
```

#### How the Monthly Review Works

On the first triage after the review is due, the plugin triggers:

```
🎙️ VOICE PROFILE REVIEW — Due for your [monthly / bi-weekly / weekly] check-in

Your voice profile was last updated [X] days ago.

WHAT'S CHANGED SINCE LAST REVIEW:
├── 📧 [X] new sent emails analyzed
├── 🎙️ [X] new call/meeting transcripts available
├── 💬 [X] new Slack messages analyzed
├── 📱 [X] new iMessages analyzed
├── ✏️ [X] draft edits you made (voice corrections captured)

DETECTED SHIFTS:
├── Your email tone has shifted slightly more [casual/formal] this month
├── New phrase detected: "[phrase]" — used [X] times
├── Sign-off change: You've been using "[new sign-off]" more than "[old sign-off]"
├── [Any other detected changes]

RECOMMENDATIONS:
├── Re-analyze [X] new transcripts to capture current speech patterns
├── Run a quick 5-pair A/B calibration focused on [area]
├── Update your NEVER list — you used "[phrase]" twice this month (still avoid it?)

[Full review (re-analyze all sources + A/B calibration)]
[Quick review (update from new data, skip A/B)]
[Snooze 1 week]
[Change review cadence]
```

#### Multi-Source Re-Analysis

During a monthly review, the plugin re-analyzes all connected sources:

1. **Phone calls / Meeting transcripts** — Pull any new transcripts since last review. These are the highest-signal source for authentic voice because they capture unscripted, real-time communication.
2. **Sent emails** — Analyze emails sent since last review for tone drift, new patterns, or changes in greeting/sign-off usage.
3. **Slack messages** — Analyze sent Slack messages for changes in casual tone, emoji usage, and how the user communicates with different teams.
4. **iMessage / SMS** — If connected, analyze for shifts in personal communication style.
5. **Draft edits** — Compile all edits the user made to drafts since last review. These are direct voice corrections and the most explicit signal.

After re-analysis, present a summary of changes and offer A/B calibration for any areas where the profile seems outdated.

#### Voice Profile Version History

Each monthly review creates a snapshot. The voice profile tracks:

```markdown
## Review History
| Date | Sources Analyzed | Key Changes | A/B Pairs Tested |
|------|-----------------|-------------|-----------------|
| [date] | 45 emails, 12 transcripts, 200 Slack msgs | Tone shifted casual, new sign-off | 5 pairs |
| [date] | 30 emails, 8 transcripts | Added 3 phrases to NEVER list | 0 pairs |
```

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

### Dual-Source Email Scanning

**IMPORTANT:** Every email operation — triage, quick check, search, report, or any email-related request — MUST query both Gmail MCP and all Rube-connected email accounts in parallel. Never rely on a single source. Merge and deduplicate results before processing.

### Batch Processing

1. Pull all unread + starred emails for the time range from ALL connected email sources (Gmail MCP + Rube)
2. Apply rules first — auto-processed emails are reported as a summary, not individually
3. **VIP check** — If any emails are from VIP senders, surface them immediately (see VIP Immediate Alert below)
4. Route emails to folders based on folder rules (Low Priority, Newsletters, etc.)
5. Sort remaining by: starred first → 🔴 by urgency → 🟡 → 🗑️
6. Present in batches of [configured size, default 10]
7. After each batch: "Ready for the next batch, or take action on these first?"

### VIP Immediate Alert

When an email is received from a VIP sender, it is **always surfaced immediately** — before normal batch processing. The alert includes full email details and a pre-written draft reply.

```
🚨 VIP EMAIL — [Sender Name] ([Relationship])

From: [Full Name] <[email]>
Subject: [Subject line]
Received: [Day, Date, Time]
Thread: [New / Reply in thread of X messages]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FULL EMAIL:
[Complete email body displayed — not just a summary]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PRE-WRITTEN DRAFT REPLY:
[Draft reply written in the user's voice, appropriate to the sender's
relationship tag and the email content. Uses personal voice for
internal/casual contacts, brand voice for client-facing if BKC connected.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ [Send Draft] [Edit Draft] [Rewrite Draft] [Remind Me] [Deep Dive (full thread)] [Skip for now]
```

#### VIP Alert Behavior

| Scenario | What Happens |
|----------|-------------|
| **During triage** | VIP emails are pulled to the top of the first batch with full alert format |
| **Quick check ("any new emails?")** | VIP emails are always shown, even if everything else is clear |
| **Between triages** | If daily briefing or VIP digest is configured, VIP emails appear there |
| **Multiple VIP emails** | Each gets its own alert block, presented in order of receipt |

#### Pre-Written Draft Logic

The draft is generated automatically based on:
1. **Email content** — What's being asked/discussed
2. **Sender relationship** — Tone and formality adjusted per VIP contact settings
3. **Thread context** — If a reply in an existing thread, draft considers the full conversation
4. **Voice profile** — Uses the user's authentic voice (personal or brand as appropriate)
5. **Priority notes** — Any VIP-specific instructions (e.g., "Always CC [person] on replies", "More formal with this person")

The user should never have to write from scratch for a VIP email — the draft is ready for review and send.

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

## Unsubscribe Workflow

When the user assigns `unsub` to a message, execute the unsubscribe — don't just flag it.

### Execution Methods (in priority order)

**1. List-Unsubscribe header (one-click)**
Check the raw email headers for a `List-Unsubscribe` field. This is included in most legitimate marketing and newsletter emails. It contains either a `mailto:` address or an `https://` URL.
- `mailto:` unsubscribe: Send the specified unsubscribe email automatically
- `https://` unsubscribe: Execute a GET/POST request to the URL to complete the unsubscribe

This is the cleanest method — no link extraction, no browser required.

**2. Unsubscribe link extraction**
If no `List-Unsubscribe` header is present, scan the email body for unsubscribe links. Look for text containing "unsubscribe", "manage preferences", "opt out", "email preferences", or "manage your subscription".

Extract the URL and present:
> "Found unsubscribe link for [sender]: [url] — Open to complete? [Open / Skip]"

If the email was connected via Rube (full write access), attempt to call the URL directly. Otherwise, open in the user's browser.

**3. Auto-junk rule (no mechanism found)**
If neither method finds an unsubscribe mechanism (automated alerts, scraper lists, transactional emails repurposed for spam):
> "No unsubscribe link found in this email from [sender]. Want me to create a rule to auto-junk all future emails from them? [Yes / No]"

### Batch vs. Immediate Mode

Behavior is controlled by `unsubscribe_mode` in config:

**`auto` (immediate):** Execute each unsubscribe as soon as it's assigned during triage. Report in the action confirmation batch:
> "✓ Unsubscribed from: [sender1] (one-click), [sender2] (one-click). [sender3]: no link found — created auto-junk rule."

**`batch` (end of triage):** Collect all `unsub` assignments during triage. At the end, execute together:

```
UNSUBSCRIBE QUEUE — 4 senders

├── [sender1] — List-Unsubscribe header found ✓ (will execute)
├── [sender2] — List-Unsubscribe header found ✓ (will execute)
├── [sender3] — Unsubscribe link found: [url] — confirm? [Yes / Skip]
└── [sender4] — No link found — create auto-junk rule? [Yes / Skip]

[Execute all] [Review each]
```

**`manual`:** Present the unsubscribe link or header URL for each, let the user handle it themselves. Just surface the mechanism, don't execute.

### Post-Unsubscribe

After a successful unsubscribe:
- Create a rule: auto-junk any future emails from the same sender (they may still arrive despite unsubscribing)
- Log in triage complete summary under "🔕 Unsubscribed"

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

The task tracker backend is configured during setup. All backends use the same task data model and action commands — only the storage mechanism differs.

### Task Data Model

| Field | Description |
|-------|-------------|
| ID | T001, T002... |
| Created | Date added |
| Due | Target date/time |
| Source | Email, Slack, iMessage, Calendar, Manual |
| From | Sender name |
| Description | Brief task name |
| Summary | 1-2 sentence context |
| Priority | HIGH / MEDIUM / LOW |
| Status | ⬜ Open / 🔄 In Progress / ✅ Done / ⏭️ Deferred |
| Completed | Date completed |
| Notes | Follow-up notes |

### Supported Backends

**Apple Reminders** (`task_tracker: apple-reminders`)
- Create: Add reminder to "Inbox Tasks" list with due date, priority, and notes
- Read: List open reminders from the list for morning summary
- Update: Mark complete, update due date, add notes
- Best for: Mac/iPhone users who want zero friction and no extra accounts

**Markdown task list** (`task_tracker: markdown`)
- Stored at `[data-path]/tasks.md` — same iCloud folder as config, voice profile, and rules
- Read/write as a structured markdown table
- Update status in-place; append new rows
- Best for: users who want everything in one simple folder

**ClickUp** (`task_tracker: clickup`)
- Create tasks in a configured ClickUp list via Rube
- Read open tasks, update status, add comments
- Best for: users who already use ClickUp for project management

**Google Sheets** (`task_tracker: google-sheets`)
- Sheet name: "Inbox Task Tracker" (created during setup if not found)
- Add rows, update status, filter by due date and priority
- Best for: users who want flexible filtering and reporting

### Calendar Reminder Integration

Regardless of backend, when a task is created with a due time:
1. Add task to the configured backend
2. Create Google Calendar event: "📬 [Task ID]: [Description]"
3. Event description includes task context
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
- **Include:** Email summary, Slack summary, iMessage summary, Calendar flags, Task reminders, Rules summary, VIP summary
```

## Daily VIP Summary

A dedicated daily summary of all VIP communications is generated and sent to the user. This is separate from (and in addition to) the morning briefing.

### VIP Summary Config

```markdown
## VIP Summary
- Enabled: Yes
- Delivery: [Slack DM / iMessage / Email / All]
- Time: [HH:MM AM/PM] (default: same as morning briefing)
- Include: [emails received, emails sent, threads active, pending drafts]
```

### VIP Summary Format

```
⭐ DAILY VIP SUMMARY — [Date]

[X] VIP communications today

━━━ EMAILS RECEIVED FROM VIPs ━━━

📧 [Sender Name] ([Relationship]) — [Time]
   Subject: [Subject line]
   Summary: [1-2 sentence summary]
   Status: [Replied ✅ / Draft pending ✏️ / Unread 🔴 / Read, no reply needed 🟡]

📧 [Sender Name] ([Relationship]) — [Time]
   Subject: [Subject line]
   Summary: [1-2 sentence summary]
   Status: [Replied ✅ / Draft pending ✏️ / Unread 🔴]

━━━ EMAILS SENT TO VIPs ━━━

📤 To: [Name] — [Subject] — [Time]
📤 To: [Name] — [Subject] — [Time]

━━━ ACTIVE VIP THREADS ━━━

🔄 [Name] — [Subject] — [X] messages, last activity [time]
   [Brief context of where the thread stands]

━━━ PENDING ━━━

⏳ [X] VIP emails awaiting your response
├── [Name] — [Subject] — received [time ago]
├── [Name] — [Subject] — received [time ago]

→ Say "triage" to take action on pending VIP items
```

### VIP Summary Delivery

The VIP summary is delivered daily at the configured time via the user's chosen channel. It provides a complete picture of all VIP communications for the day — what came in, what went out, what's pending, and what threads are active.

## Monthly Inbox Report

A comprehensive monthly report on inbox activity, trends, and communications. Generated automatically and sent to the user on the cadence they choose.

### Report Cadence Config

```markdown
## Inbox Report
- Cadence: [monthly / bi-weekly / weekly]
- Delivery: [Email / Slack DM / iMessage / All]
- Day: [1st of month / last business day / custom]
- Time: [HH:MM AM/PM]
- Last generated: [date]
```

### Report Content

```
📊 INBOX REPORT — [Month Year]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 EMAIL VOLUME
├── Total received: [X]
├── Total sent: [X]
├── Average per day: [X] received / [X] sent
├── Busiest day: [Day, Date] ([X] emails)
├── Quietest day: [Day, Date] ([X] emails)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗑️ DELETION BREAKDOWN
├── Total emails deleted: [X]
│   ├── Manually deleted (during triage): [X]
│   ├── Rule-based auto-deleted: [X]
│   │   ├── By rule: [Rule Name] — [X] deleted
│   │   ├── By rule: [Rule Name] — [X] deleted
│   │   └── By rule: [Rule Name] — [X] deleted
│   ├── Folder auto-cleanup (expired): [X]
│   └── Unsubscribe + delete: [X]
├── Deletion rate: [X]% of all received emails
├── Manual vs. automated: [X]% manual / [X]% automated
└── Trend: [↑ X% more / ↓ X% fewer / → same] as last month

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 READ BUT NOT RESPONDED
├── Total read without reply: [X]
├── By category:
│   ├── 🟡 FYI (expected — no reply needed): [X]
│   ├── 🔴 RESPOND (flagged but not replied): [X] ⚠️
│   │   ├── [Sender] — [Subject] — [X] days ago
│   │   ├── [Sender] — [Subject] — [X] days ago
│   │   └── [Sender] — [Subject] — [X] days ago
│   └── Skipped during triage: [X]
├── Average time to respond (when you do): [X] hours
└── Response rate: [X]% of 🔴 items replied to

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VIP COMMUNICATIONS SUMMARY
├── Total VIP emails received: [X]
├── Total VIP emails sent: [X]
├── VIP response rate: [X]%
├── Average VIP response time: [X] hours
│
├── BY VIP CONTACT:
│   ├── [Name] ([Relationship])
│   │   ├── Received: [X] | Sent: [X] | Avg response: [X]h
│   │   └── Key threads: [brief list]
│   ├── [Name] ([Relationship])
│   │   ├── Received: [X] | Sent: [X] | Avg response: [X]h
│   │   └── Key threads: [brief list]
│   └── [Name] ([Relationship])
│       ├── Received: [X] | Sent: [X] | Avg response: [X]h
│       └── Key threads: [brief list]
│
├── VIP threads still open/pending: [X]
│   ├── [Name] — [Subject] — awaiting [your reply / their reply]
│   └── [Name] — [Subject] — awaiting [your reply / their reply]
│
└── Notable: [Any VIP who went silent, new VIP candidates, etc.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ RULES PERFORMANCE
├── Total messages auto-processed: [X]
├── By action:
│   ├── Auto-junked: [X]
│   ├── Auto-archived: [X]
│   ├── Auto-labeled: [X]
│   ├── Auto-forwarded: [X]
│   ├── Auto-deleted: [X]
│   └── Auto-routed to folder: [X]
├── Top rules by volume:
│   ├── [Rule Name] — triggered [X] times
│   ├── [Rule Name] — triggered [X] times
│   └── [Rule Name] — triggered [X] times
├── Rules with 0 triggers this month: [list — candidates for cleanup]
└── New rule suggestions pending: [X]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📂 FOLDER ACTIVITY
├── Low Priority: [X] received, [X] auto-archived, [X] auto-deleted
├── Newsletters: [X] received, [X] read, [X] auto-deleted
├── Finance: [X] received
├── Automated/Bot: [X] received, [X] auto-deleted
├── [Other folders]: [stats]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 TRENDS & INSIGHTS
├── Email volume trend: [↑/↓/→] vs. last month
├── Response time trend: [↑/↓/→] vs. last month
├── Top 5 senders (by volume): [list with counts]
├── Top 5 senders you reply to most: [list]
├── New senders this month: [X] ([X] became repeat)
├── Busiest time of day: [hour range]
├── Triage efficiency: [X]% of inbox handled by rules (vs. [X]% last month)
├── Average triage session: [X] minutes, [X] messages
└── Inbox zero days: [X] out of [X] business days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 SLACK & iMESSAGE (if connected)
├── Slack: [X] messages triaged, [X] replied, [X] skipped
├── iMessage: [X] messages triaged, [X] replied, [X] skipped
├── Cross-platform dedup: [X] items merged

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ACTIONS DUE
├── Pending rule suggestions: [X] — [Review now]
├── VIP list review: [due / not due]
├── Voice profile review: [due / not due]
├── Stale follow-ups: [X] emails sent with no reply > 7 days
└── [Any other action items]
```

### Report Delivery

The report is delivered via the user's configured channel. If delivered via email, it is formatted as a clean, readable email. If via Slack or iMessage, it is sent as a structured message with the key highlights and a link to the full report (stored in the user data directory as `inbox-command-center/reports/[YYYY-MM].md`).

### Report Storage

Monthly reports are saved to the user data directory:

```
inbox-command-center/
├── reports/
│   ├── 2026-01.md
│   ├── 2026-02.md
│   └── 2026-03.md
```

Users can view past reports anytime: "Show my inbox report for January" or "Compare this month to last month".

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
├── commands/                    # Command files (setup-wizard, triage, create-rule, voice-calibration, inbox-report)
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
├── folder-rules.md           # Folder-based rules and review settings
├── rule-suggestions.md       # Pending learned suggestions
├── tasks.md                  # Task list (markdown backend only)
├── task-tracker-link.md      # Link to external tracker (Google Sheets / ClickUp)
└── reports/                  # Monthly inbox reports
    └── [YYYY-MM].md
```

When local only:
```
inbox-command-center/
├── config.md
├── voice-profile.md
├── vip-contacts.md
├── rules.md
├── folder-rules.md
├── rule-suggestions.md
├── task-tracker-link.md
└── reports/
    └── [YYYY-MM].md
```
