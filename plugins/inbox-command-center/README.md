# Inbox Command Center

AI communications manager that triages your email, Slack, and messaging platforms — categorizes messages, drafts replies in your authentic voice, manages calendar conflicts, tracks tasks, enforces smart rules, and delivers scheduled daily briefings. Built by Strategy Labs.

## What It Does

The Inbox Command Center turns inbox chaos into a 10-minute daily routine. Connect your email and messaging tools, build a voice profile so drafts actually sound like you, set up smart rules to auto-handle the noise, and triage what's left in prioritized batches with one-word action codes.

## Commands

| Command | Description |
|---------|-------------|
| `/setup-wizard` | Full onboarding: connect accounts, build voice profile, A/B calibration, VIP contacts, rules, task tracker, briefing schedule |
| `/triage` | Daily inbox triage — categorize, batch, and action emails + Slack + calendar |
| `/create-rule` | Step-by-step guided rule creation for automated message handling |
| `/voice-calibration` | A/B message comparison to refine your voice profile |

Also triggers on: "check my email", "any new emails?", "what did I miss", "triage", "inbox zero", "draft a reply to [person]", "check Slack", "show my tasks", "create a rule"

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **Run `/setup-wizard`** — walks through the full setup:
   - Connect email (Gmail via MCP, Outlook via Rube)
   - Connect Slack + other messaging (optional)
   - Connect calendar
   - Connect meeting transcript tools (Fireflies, Otter, Gong, etc.)
   - Build your voice profile from transcripts + sent emails + guided questions
   - A/B voice calibration — pick which drafts sound like you
   - Set up VIP contacts (auto-detected from email frequency)
   - Configure task tracker
   - Set up scheduled daily briefing
   - Choose standard rules + create custom rules
3. **Say "check my email"** to run your first triage

## Daily Workflow

**Morning (5-10 min):**
- Open Claude, say "triage" or "check my email"
- Review batches, rapid-fire your decisions: `1: draft, 2: remind tomorrow 9am, 3: read, 4-7: delete`
- Draft replies get written in your voice, presented for approval

**Throughout the day:**
- "Any new emails?" — quick scan since last check
- "Draft a reply to [person]" — compose in your voice
- "Show my tasks" — review open items

**End of day:**
- "Anything I missed?" — catch stragglers
- "Set reminders for anything I didn't get to" — defer to tomorrow

## Voice Profile

The plugin learns how you actually communicate — not a generic template. Your voice profile is built from:

1. **Meeting transcripts** — Fireflies, Otter, Gong, Fathom, Zoom recordings
2. **Sent email analysis** — Your actual greeting, sign-off, and phrasing patterns
3. **A/B calibration** — You pick which draft sounds more like you across 20+ scenarios
4. **Continuous learning** — When you edit a draft, the profile updates automatically

Supports a **two-voice system** with Brand Knowledge Center: personal voice for internal/casual, brand voice for client-facing.

## Smart Rules

Rules auto-process messages before they hit your triage:

**Standard rules** (suggested during setup):
- Auto-junk social notifications (LinkedIn, Instagram, etc.)
- Auto-archive shipping confirmations and calendar accepts
- VIP contacts always flagged as priority
- Urgency keywords escalate to HIGH
- Quiet hours hold messages for morning

**Custom rules** (create anytime with `/create-rule`):
- Step-by-step guided builder
- Test against past 30 days before activating
- Chain multiple actions (label + forward + mark read)

**Learned rules** (suggested automatically):
- Plugin detects patterns in your triage behavior
- "You've junked this sender 4 times — auto-junk them?"

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
- **Email digest** — summary email to your inbox
- **Calendar block** — recurring event with briefing in description
- **All three**

## Connections

| Tool | Via | Purpose |
|------|-----|---------|
| Gmail | MCP | Email triage + drafting |
| Slack | MCP | Message triage + replies |
| Google Calendar | MCP | Conflict detection, meeting prep, reminders |
| Fireflies.ai | MCP | Voice learning from meeting transcripts |
| Outlook | Rube | Email (alternative to Gmail) |
| Otter, Gong, Fathom | Rube | Additional transcript sources |
| Zoom, Google Meet, Loom | Rube | Recording transcripts |
| Teams, WhatsApp, SMS | Rube | Additional messaging platforms |

## Integration

Works with **Brand Knowledge Center** for a two-voice system:
- Personal voice → internal, casual, and personal emails
- Brand voice → client-facing, business development, marketing

## Tips

- **Run triage daily** — 10 minutes in the morning keeps you at inbox zero
- **Use rapid-fire codes** — `1: draft, 2-5: read, 6-8: delete` processes 8 messages in seconds
- **Let rules do the work** — after a few weeks, 40-60% of messages are auto-processed before you see them
- **Edit drafts freely** — every edit teaches the voice profile; drafts get better over time
- **Run `/voice-calibration` monthly** — or whenever drafts feel off
- **Say "create a rule" during triage** — build rules in the moment when you see patterns
