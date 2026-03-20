---
name: inbox-manager
description: >
  Inbox Command Center for managing email, Slack, and messaging platforms.
  Use when the user mentions "check my email", "inbox", "triage", "what did I miss",
  "clean up my inbox", "draft a reply", "inbox zero", "unsubscribe", "email manager",
  "comms manager", "check Slack", "any important emails", "what do I need to respond to",
  "create a rule", "message rules", "voice profile", "daily briefing", "morning update",
  "check my messages", or anything related to email, messaging, or communications management.
version: 1.0.0
---

# Inbox Command Center

An AI communications manager that triages email, Slack, and messaging platforms — categorizes messages, drafts replies in the user's authentic voice, manages calendar, tracks tasks, enforces smart rules, and delivers scheduled briefings.

## How It Works

The Inbox Command Center has seven layers:

1. **Connection Layer** — Connects to email, Slack, messaging, calendar, and meeting transcript tools via MCP or Rube.
2. **Rules Layer** — Applies user-configured rules to auto-categorize, archive, forward, label, or escalate messages before triage.
3. **Triage Layer** — Categorizes remaining messages as RESPOND, FYI, JUNK, or UNSUBSCRIBE. Presents in prioritized batches with inline actions.
4. **Voice Layer** — Maintains a living voice profile built from meeting transcripts, sent emails, and A/B calibration. Drafts replies that sound like the user.
5. **Calendar Layer** — Detects conflicts, unresponded invites, marathon blocks, and meetings needing prep.
6. **Task Layer** — Tracks reminders and follow-ups via Google Sheet + Calendar events.
7. **Briefing Layer** — Delivers scheduled daily summaries via Slack, email, or calendar.

## Connection Methods

Tools can be connected two ways:

### Direct MCP Connection
Claude's built-in MCP integrations for:
- Gmail (read, search, draft, label)
- Slack (read channels, DMs, send messages)
- Google Calendar (read, create, respond to events)
- Fireflies.ai (meeting transcripts)

### Rube Connection
For tools not available via MCP, use Rube to connect:
- Outlook / Microsoft 365
- Otter.ai, Gong, Fathom (meeting transcripts)
- Zoom cloud recordings
- SMS platforms (Twilio, etc.)
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
| Google Calendar | MCP | primary | Active |
| Fireflies | MCP | [account] | Active |

## Primary Email
[email] — used for drafting replies by default

## Time Zone
[timezone]

## Batch Size
[number] emails per batch (default: 10)

## Scheduled Briefing
- Delivery: [Slack DM / Email / Calendar / None]
- Time: [HH:MM AM/PM]
- Days: [Mon-Fri / Daily / Custom]
```

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
| `remind [time]` | Add to task tracker + calendar event |
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

Slack items are numbered after email items in the same batch (email #1-8, Slack #9-10) so user can rapid-fire across both platforms in one response.

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
| Source | Email, Slack, Calendar, Manual |
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

### Morning Integration

During morning triage, after email/Slack batch 1:
- Surface tasks due today or overdue
- "You also have [X] open tasks — [X] overdue, [X] due today."

## Scheduled Daily Briefing

### Delivery Methods

| Method | How It Works |
|--------|-------------|
| **Slack DM** | Auto-send summary to user at configured time |
| **Email Digest** | Send summary email to user's inbox |
| **Calendar Block** | Create/update recurring event with briefing in description |
| **All Three** | Maximum coverage |

### Briefing Content

```
☀️ Morning Briefing — [Date]

📧 EMAIL: [X] unread ([X] 🔴 need response, [X] 🟡 FYI, [X] 🗑️ junk)
├── 🔴 [Top 3 RESPOND items with sender + subject + 1-line summary]

💬 SLACK: [X] unread ([X] 🔴 need response)
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
- **Delivery:** Slack DM
- **Time:** 7:30 AM
- **Days:** Monday through Friday
- **Include:** Email summary, Slack summary, Calendar flags, Task reminders, Rules summary
```

## File Structure

```
inbox-command-center/
├── config.md                 # Connected tools, preferences, schedule
├── voice-profile.md          # Living voice profile
├── vip-contacts.md           # Priority contact list with relationship tags
├── rules.md                  # Active message rules
├── rule-suggestions.md       # Pending learned suggestions
└── task-tracker-link.md      # Link to Google Sheet
```
