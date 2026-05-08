# Inbox Command Center

AI communications manager that triages email, Slack, and messaging platforms across multiple accounts — categorizes messages, drafts replies in your authentic voice (continuously refined from Fireflies meeting transcripts and your own draft edits), tracks tasks and followups in a hand-editable workspace folder, manages calendar conflicts, enforces smart rules with per-inbox scope and stakes-based auto-apply behavior, delivers VIP alerts with pre-written drafts, generates monthly reports, and ships scheduled briefings. Built by Strategy Labs.

## What It Does

The Inbox Command Center turns inbox chaos into a 10-minute daily routine across all your inboxes. Connect multiple Gmail and Outlook accounts via Composio, build a voice profile rooted in your actual conversations (Fireflies transcripts), set up smart rules to auto-handle the noise, and triage what's left in prioritized batches. VIPs surface immediately — across every connected inbox — with pre-written draft replies. The whole system lives in a Finder-visible workspace folder you can hand-edit anytime; rules, contacts, todos, and voice profile are markdown files, not opaque config.

## Commands

| Command | Description |
|---------|-------------|
| `/setup-wizard` | Full onboarding: Composio account, multi-account email, voice profile (Fireflies-seeded), VIPs, folders, rules, schedules, workspace tour |
| `/triage` | Daily inbox triage — VIP cross-inbox scan first, then sequential per-inbox processing with rapid-fire action codes |
| `/create-rule` | Step-by-step guided rule creation — type (delete/prioritize/folder/organize) × stakes (low/high) × scope (per-inbox/global) |
| `/voice-calibration` | Multi-source voice analysis (Fireflies primary) + A/B comparison; auto-fires when drift is detected |
| `/inbox-report` | Comprehensive report with cross-inbox unified entities + per-inbox sections, fed by daily session logs |

Also triggers on: "check my email", "any new emails?", "what did I miss", "triage", "draft a reply to [person]", "show my tasks", "create a rule", "inbox report", etc.

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **Composio account** — required for full features
   - Strategy Labs team members: email scott@strategylabs.us to be added to the SL team Composio account
   - External users: walk through composio.dev signup (~3 min)
   - Fallback path available (Gmail-only, single account, native MCP) — limited features
3. **Run `/setup-wizard`** — walks through ~18 steps:
   - Composio prerequisite check + onboarding
   - Email connection (Gmail / Outlook / Both, multi-account loop — add as many inboxes as you want)
   - Slack, calendar, iMessage, transcript tools
   - Fireflies elevated to recommended — 30-day pull seeds your voice profile
   - A/B voice calibration (20+ scenarios)
   - VIP capture (writes to `contacts.md` as starter entries)
   - Per-inbox folder enablement + standard rules tagged with stakes/scope
   - Schedule preferences (briefing, VIP digest, voice review, inbox report, rule cadence)
   - Workspace tour — opens Finder so you can see your hand-editable folder
4. **Say "triage my inbox"** to run your first session

## Workspace

Everything lives at `~/Inbox Command Center/` (iCloud-synced, Finder-visible). You can hand-edit any file — the skill reads them fresh at the start of every session, so changes you make in Finder show up immediately.

| File | What it is |
|---|---|
| `contacts.md` | Per-recipient memory: tone notes, `[VIP]` tags, interaction timeline, Fireflies-derived context |
| `todos.md` | Things you owe yourself (from email triage or manual) |
| `followups.md` | People waiting on a reply from you |
| `rules.md` | Active rules with type, stakes, and scope |
| `rules-review-queue.md` | Pending rule suggestions awaiting your review |
| `voice-profile.md` | Living personal voice profile |
| `voice-profile-brand.md` | Brand voice (if BKC connected) |
| `session-logs/YYYY-MM-DD.md` | Daily journal of meaningful events |
| `reports/YYYY-MM.md` | Monthly inbox reports |
| `.meta.json` | Bookkeeping: connected inboxes, sync state, schedules, version |

## Daily Workflow

**Morning (5–10 min):**
- Open Claude, say "triage" or "check my email"
- VIP cross-inbox scan runs first — surfaces VIPs across all connected accounts before sequential triage starts
- Pick which inbox to triage; rapid-fire your decisions: `1: draft, 2: remind tomorrow 9am, 3: read, 4-7: delete`
- Drafts get written in your voice and refined per recipient via `contacts.md` notes

**Throughout the day:**
- "Any new emails?" — quick scan since last check (VIPs always shown)
- "Draft a reply to [person]" — composes in your voice
- "Show my tasks" / "Who's waiting on me?" — review todos / followups

**End of day:**
- "Anything I missed?" — catch stragglers
- "Set reminders for what I didn't get to"

**Automated:**
- Daily briefing (aggregated across inboxes, with per-inbox sections)
- Daily VIP digest (separate per inbox)
- Weekly Fireflies pull (voice profile + `contacts.md` updates)
- Monthly inbox report
- Voice profile review on your chosen cadence

## Voice Profile

The plugin learns how you actually communicate. Voice profile sources, in priority order:

1. **Fireflies meeting transcripts** — primary signal; weekly pull keeps voice + per-recipient context fresh
2. **Sent email analysis** — written voice patterns
3. **Slack messages** — internal/casual tone
4. **iMessage** — most casual register
5. **Continuous draft-edit learning** — every edit feeds voice profile + per-recipient `contacts.md` notes
6. **A/B calibration** — explicit preference testing during setup, monthly review, and drift events

### Mandatory voice review

Cadence configurable (monthly minimum, bi-weekly or weekly optional). Re-analyzes all sources for tone drift and offers targeted A/B for areas that need refinement.

### Drift-triggered A/B

If you make 3+ substantial draft edits in one session, the plugin offers a focused 5-pair A/B at session end — catches drift early without waiting for the monthly review.

### Two-voice system

Works with **Brand Knowledge Center** for personal vs. brand voice. Brand-voice contacts get tagged `[Brand]` in `contacts.md`.

## VIP System

VIPs are unified across all your inboxes — one VIP list, one set of contact notes. VIPs are marked with `[VIP]` in their `contacts.md` section header:

```markdown
## Bryan Howell <bryan@dieselpowerproducts.com> [VIP]
**Review:** monthly | **Since:** 2026-04
- Tone: concise, numbers-forward, skip pleasantries
- Recent context: Q3 numbers call (Fireflies 2026-05-03)
- Inboxes seen: ramsey@strategylabs.us, ramsey@unomastacos.com
```

- **Cross-inbox scan at session start** — surfaces VIP messages across all connected accounts before sequential triage
- **Pre-written drafts** — every VIP email gets a draft in your voice
- **Auto-tracked timeline** — last email + last meeting (Fireflies) per VIP
- **Daily VIP digest** — separate per inbox (operational), unified VIP list (canonical)
- **Smart suggestions** — based on response patterns, meeting frequency, cross-inbox activity

## Smart Rules

Every rule has three dimensions:

```
Type:    delete | prioritize | folder | organize
Stakes:  low_stakes (auto-apply silently) | high_stakes (always confirm)
Scope:   per-inbox | global
```

**Defaults:** label / route / trash / unsub → `low_stakes`; permanent-delete / auto-reply / auto-forward → `high_stakes`. VIP-related rules are inherently global.

**Resolution at triage time:** global rules → inbox-specific rules. Specific scope wins on conflict.

**Cadence configurable:** every triage / every 3rd / weekly / monthly / on demand.

**Learned rules** (suggested automatically): plugin detects patterns in your triage behavior and queues suggestions in `rules-review-queue.md`. Categorized as delete / prioritization / organization rules.

## Folder System

Synthetic logical folders dispatched per platform — Gmail labels (`ICC/Newsletters`) for Gmail accounts, native subfolders (`Inbox/ICC/Newsletters`) for Outlook/IMAP. **Per-inbox enablement** — not every inbox needs every folder.

| Folder | Default Review | Auto-Action |
|--------|---------------|-------------|
| Low Priority | Weekly digest | Archive 30d, delete 90d |
| Newsletters | Weekly | Delete 14d unread |
| Receipts & Orders | Never | Keep |
| Finance | Daily digest | Keep |
| Automated/Bot | Daily count | Delete 7d |
| Pending Review | Every triage | Remind 3d |
| Delegated | Daily | Remind 5d |

## Monthly Inbox Report

One report per period, two layers:

**Cross-inbox section** — unified entities:
- VIP communications (per-VIP breakdown, response times, key threads)
- Voice profile drift events
- Fireflies meetings ingested
- Global rules performance

**Per-inbox sections** (one per connected inbox):
- Email volume, deletion breakdown, read-but-not-responded
- Folder activity, rule performance
- Trends and inbox zero days

Reports stored at `~/Inbox Command Center/reports/YYYY-MM.md` and optionally delivered via Slack DM, iMessage, or email.

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
| `remind [time]` | Add to `todos.md` + calendar event + scheduled delivery via your channel |
| `read` | Mark as read |
| `delete` | Trash (recoverable) |
| `unsub` | Execute unsubscribe (List-Unsubscribe header → body link → fallback auto-junk rule) |
| `dive` | Show full email/thread |
| `delegate [name]` | Forward to someone, add to `followups.md` |
| `skip` | Leave for later |
| `rule` | Create a rule based on this message |

Example: `1: draft, 2: remind monday 9am, 3-6: delete, 7: read, 8: delegate annie`

## Connections

| Tool | Connection | Purpose |
|------|-----------|---------|
| Gmail (× N accounts) | Composio | Email triage + drafting + sending |
| Outlook / Microsoft 365 (× N accounts) | Composio | Email triage + drafting + sending |
| Slack | Native MCP | Message triage + replies + voice learning |
| Google Calendar | Native MCP | Conflict detection, meeting prep, reminders |
| Outlook Calendar | Composio | For Outlook users |
| Fireflies | Native MCP | Voice/context primary signal — weekly pull |
| Otter / Gong / Fathom | Composio | Additional transcript sources |
| iMessage | AppleScript | Mac-only message triage + replies |

**Coming in v1.5:** iCloud Mail and Generic IMAP via a new IMAP adapter.

## Strategy Labs Onboarding

For SL team members, the recommended path is the team Composio account:

1. Email **scott@strategylabs.us** to be added to the SL team Composio account
2. Wait for confirmation (usually same-day)
3. Run `/setup-wizard` — when it asks about Composio, type "ready" once Scott confirms access
4. The wizard walks you through OAuth for each inbox

External users follow the standard composio.dev signup. The wizard handles both paths.

## Integration

Works with **Brand Knowledge Center** for a two-voice system:
- Personal voice → internal, casual, and personal emails
- Brand voice → client-facing, business development, marketing
- Brand-voice contacts get tagged `[Brand]` in `contacts.md`

## Scheduled Automations

| Automation | Default Cadence | Configurable |
|-----------|----------------|-------------|
| Daily briefing | Weekdays 7:30 AM (aggregated, per-inbox sections) | Time, days, channel |
| Daily VIP digest | Per inbox, same time as briefing | Time, channel, on/off |
| Weekly Fireflies pull | Sundays off-hours | Day, on/off |
| Voice profile review | Monthly | Monthly / bi-weekly / weekly |
| VIP list review | Monthly | Monthly / bi-weekly / weekly / quarterly / on demand |
| Inbox report | Monthly | Monthly / bi-weekly / weekly |
| Rule suggestions | Every 3rd triage | Every triage / 3rd / weekly / monthly / on demand |
| Folder digests | Per-folder per-inbox | Per-folder cadence |

## Tips

- **Run triage daily** — 10 minutes in the morning keeps you at inbox zero across all inboxes
- **Use rapid-fire codes** — `1: draft, 2-5: read, 6-8: delete` processes 8 messages in seconds
- **Hand-edit `contacts.md`** when something feels off — every entry refines the voice profile for that recipient
- **Connect Fireflies** — biggest single voice-quality improvement; ~5 minutes to set up
- **Tag rules `global` only when you mean it** — per-inbox is the safer default to avoid cross-contamination
- **Check your workspace folder in Finder** — it's a useful audit trail and a place to hand-edit when something needs adjustment
- **Review your voice profile regularly** — the mandatory review keeps drafts sounding like you as your style evolves
