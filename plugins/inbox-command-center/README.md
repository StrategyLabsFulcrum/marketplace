# Inbox Command Center

AI communications manager that triages your email, Slack, and messaging platforms — categorizes messages, drafts replies in your authentic voice, manages calendar conflicts, tracks tasks, enforces smart rules, delivers VIP alerts with pre-written drafts, generates inbox reports, and delivers scheduled daily briefings. Built by Strategy Labs.

## What It Does

The Inbox Command Center turns inbox chaos into a 10-minute daily routine. Connect your email and messaging tools, build a voice profile so drafts actually sound like you, set up smart rules to auto-handle the noise, and triage what's left in prioritized batches with one-word action codes. VIP emails are surfaced immediately with pre-written draft replies. Monthly reports track your inbox health with full analytics.

## Commands

| Command | Description |
|---------|-------------|
| `/setup-wizard` | Full onboarding: connect accounts, build voice profile, A/B calibration, VIP contacts, folder rules, report schedule, task tracker, briefing schedule |
| `/triage` | Daily inbox triage — VIP alerts first, then categorize, batch, and action emails + Slack + calendar |
| `/create-rule` | Step-by-step guided rule creation — delete, prioritization, folder-based, and organization rules |
| `/voice-calibration` | Multi-source voice analysis + A/B message comparison to refine your voice profile |
| `/inbox-report` | Generate comprehensive inbox activity report with analytics, trends, and VIP summaries |

Also triggers on: "check my email", "any new emails?", "what did I miss", "triage", "inbox zero", "draft a reply to [person]", "check Slack", "show my tasks", "create a rule", "inbox report", "email stats"

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **Run `/setup-wizard`** — walks through the full setup:
   - Connect email (Gmail via MCP, Outlook via Rube)
   - Connect Slack + other messaging (optional)
   - Connect calendar
   - Connect meeting/phone call transcript tools (Fireflies, Otter, Gong, etc.)
   - Build your voice profile from transcripts + sent emails + Slack messages + guided questions
   - A/B voice calibration — pick which drafts sound like you
   - Set up VIP contacts with review cadence and daily summary
   - Configure folder rules (Low Priority, Newsletters, Finance, etc.)
   - Set rule suggestion review cadence
   - Configure inbox report schedule
   - Set voice profile review cadence (monthly minimum)
   - Configure task tracker
   - Set up scheduled daily briefing
   - Choose standard rules + create custom rules
3. **Say "check my email"** to run your first triage

## Daily Workflow

**Morning (5-10 min):**
- Open Claude, say "triage" or "check my email"
- VIP emails are shown first with full details and pre-written drafts
- Review remaining batches, rapid-fire your decisions: `1: draft, 2: remind tomorrow 9am, 3: read, 4-7: delete`
- Draft replies get written in your voice, presented for approval

**Throughout the day:**
- "Any new emails?" — quick scan since last check (VIP emails always shown)
- "Draft a reply to [person]" — compose in your voice
- "Show my tasks" — review open items

**End of day:**
- "Anything I missed?" — catch stragglers
- "Set reminders for anything I didn't get to" — defer to tomorrow

**Automated:**
- Daily VIP summary delivered at your configured time
- Monthly inbox report with full analytics
- Voice profile review on your chosen cadence

## Voice Profile

The plugin learns how you actually communicate — not a generic template. Your voice profile is built from:

1. **Phone calls & meeting transcripts** — Fireflies, Otter, Gong, Fathom, Zoom recordings (highest-signal source for authentic voice)
2. **Sent email analysis** — Your actual greeting, sign-off, and phrasing patterns
3. **Slack message analysis** — Tone by channel, emoji usage, how you give feedback
4. **iMessage / SMS analysis** — Casual tone, abbreviations, personal vs. professional style
5. **A/B calibration** — You pick which draft sounds more like you across 20+ scenarios
6. **Continuous learning** — When you edit a draft, the profile updates automatically

### Mandatory Voice Review

Your voice profile is reviewed on a configurable cadence (monthly minimum, bi-weekly or weekly optional). The review re-analyzes all connected sources for tone drift, new phrases, and style changes, then offers targeted A/B calibration for any areas that need refinement.

Supports a **two-voice system** with Brand Knowledge Center: personal voice for internal/casual, brand voice for client-facing.

## VIP System

VIP contacts get special treatment across the entire plugin:

- **Immediate alerts** — VIP emails are shown first during triage with full email body displayed
- **Pre-written drafts** — Every VIP email comes with a draft reply in your voice, ready to send
- **Daily VIP summary** — Dedicated daily digest of all VIP communications (received, sent, pending)
- **Configurable review cadence** — Review your VIP list monthly, bi-weekly, weekly, or quarterly
- **Smart suggestions** — Plugin suggests new VIPs based on your response patterns

## Smart Rules

Rules auto-process messages before they hit your triage:

**Delete rules:**
- Auto-delete from specific senders or domains
- Delete + unsubscribe in one action
- Block sender (permanently auto-delete)
- Time-based deletion (delete after X days)

**Prioritization rules:**
- Escalate senders to HIGH automatically
- Auto-add frequent responders to VIP list
- Priority bump for specific senders or keywords

**Folder rules:**
- Route emails to folders with custom review schedules
- Low Priority folder with weekly digest and auto-cleanup
- Newsletter, Finance, Receipts, Automated/Bot folders
- Custom folders with configurable cadence and auto-actions

**Organization rules:**
- Auto-label, auto-archive, auto-forward
- Template-based auto-draft replies
- Bundle into digests

**Learned rules** (suggested automatically):
- Plugin detects patterns in your triage behavior
- Suggestions categorized as delete, prioritization, or organization rules
- Review cadence configurable: every triage, every 3rd, weekly, monthly, or on demand

## Folder System

Emails are automatically routed to folders based on rules, each with its own review cadence:

| Folder | Default Review | Auto-Action |
|--------|---------------|-------------|
| Low Priority | Weekly digest | Archive 30d, delete 90d |
| Newsletters | Weekly | Delete 14d unread |
| Receipts & Orders | Never (archive) | Keep |
| Finance | Daily digest | Keep |
| Automated/Bot | Daily count | Delete 7d |
| Pending Review | Every triage | Remind 3d |
| Delegated | Daily | Remind 5d |

## Monthly Inbox Report

Comprehensive analytics delivered on your configured cadence:

- **Email volume** — received, sent, daily averages, busiest/quietest days
- **Deletion breakdown** — total deleted, manual vs. rule-based vs. folder auto-cleanup
- **Read but not responded** — flagged items you read but didn't reply to
- **VIP communications summary** — per-VIP breakdown with response times and key threads
- **Rules performance** — auto-processed counts, top rules, zero-trigger cleanup suggestions
- **Folder activity** — per-folder stats and auto-action counts
- **Trends & insights** — volume trends, top senders, triage efficiency, inbox zero days
- **Period comparison** — compare any two periods side by side

## Message Categories

| Category | Meaning | Action |
|----------|---------|--------|
| 🔴 RESPOND | Needs your reply | Draft, remind, delegate |
| 🟡 FYI | Worth knowing | Mark read |
| 🗑️ JUNK | Delete it | Delete, unsubscribe |
| 🔕 UNSUBSCRIBE | Repeat junk | Unsubscribe + auto-junk |

## Quick Action Codes

| Code | Action |
|------|--------|
| `draft` | Draft a reply in your voice |
| `remind [time]` | Task tracker + calendar reminder |
| `read` | Mark as read |
| `delete` | Delete |
| `unsub` | Unsubscribe |
| `dive` | Show full email/thread |
| `delegate [name]` | Forward to someone |
| `skip` | Leave for later |
| `rule` | Create a rule based on this message |

Example: `1: draft, 2: remind monday 9am, 3-6: delete, 7: read, 8: delegate annie`

## Scheduled Daily Briefing

Get an automatic morning summary delivered via:
- **Slack DM** — at your configured time
- **iMessage** — text to yourself
- **Email digest** — summary email to your inbox
- **Calendar block** — recurring event with briefing in description
- **All of the above**

Includes VIP summary, email/Slack/iMessage counts, calendar flags, tasks, and rules summary.

## Connections

| Tool | Via | Purpose |
|------|-----|---------|
| Gmail | MCP | Email triage + drafting |
| Slack | MCP | Message triage + replies + voice learning |
| Google Calendar | MCP | Conflict detection, meeting prep, reminders |
| Fireflies.ai | MCP | Voice learning from meeting/call transcripts |
| iMessage | AppleScript | Message triage + replies + voice learning |
| Outlook | Rube | Email (alternative to Gmail) |
| Otter, Gong, Fathom | Rube | Additional transcript sources |
| Zoom, Google Meet, Loom | Rube | Recording transcripts |
| Teams, WhatsApp, SMS | Rube | Additional messaging platforms |

## Integration

Works with **Brand Knowledge Center** for a two-voice system:
- Personal voice → internal, casual, and personal emails
- Brand voice → client-facing, business development, marketing

## Scheduled Automations

| Automation | Default Cadence | Configurable |
|-----------|----------------|-------------|
| Daily briefing | Weekdays 7:30 AM | Time, days, delivery channel |
| Daily VIP summary | Same as briefing | Time, delivery channel, on/off |
| Voice profile review | Monthly (minimum) | Monthly / bi-weekly / weekly |
| VIP list review | Monthly | Monthly / bi-weekly / weekly / quarterly / on demand |
| Inbox report | Monthly | Monthly / bi-weekly / weekly |
| Rule suggestions | Every 3rd triage | Every triage / 3rd / weekly / monthly / on demand |
| Folder digests | Per-folder setting | Per-folder cadence |

## Tips

- **Run triage daily** — 10 minutes in the morning keeps you at inbox zero
- **Use rapid-fire codes** — `1: draft, 2-5: read, 6-8: delete` processes 8 messages in seconds
- **Let rules do the work** — after a few weeks, 40-60% of messages are auto-processed before you see them
- **Edit drafts freely** — every edit teaches the voice profile; drafts get better over time
- **Review your voice profile regularly** — the mandatory review keeps drafts sounding like you as your style evolves
- **Check your inbox report** — monthly analytics help you understand your communication patterns and optimize rules
- **Say "create a rule" during triage** — build rules in the moment when you see patterns
- **Use folders for email noise** — route low-priority emails to folders instead of deleting them
