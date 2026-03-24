# Triage

The core daily command — pulls unread emails, Slack messages, iMessages, and calendar events, applies rules, categorizes everything, and presents in prioritized batches with inline actions.

Triggers on: "check my email", "triage", "what did I miss", "any new emails", "inbox", "check my messages", "check my texts", "check iMessage", "clean up my inbox"

## Before Starting

0. **Resolve data path:** Check for iCloud sync first: `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/config.md`. If found, use the iCloud path for all user data files. Otherwise, fall back to `inbox-command-center/` locally. Also check for iCloud conflict copies (e.g., `config 2.md`) — if found, prompt the user to resolve before proceeding.
1. Load config from `[data-path]/config.md` — connected tools, batch size, preferences, sync settings.
2. Load rules from `[data-path]/rules.md`.
3. Load VIP contacts from `[data-path]/vip-contacts.md`.
4. Load voice profile from `[data-path]/voice-profile.md` (needed for drafting).
5. If Brand Knowledge Center exists, load `brand-identity.md` for brand-voice drafting.
6. **Version check:** Compare `Plugin Version` in config against current plugin version. If updated, show the update briefing (see SKILL.md → Plugin Update Notifications) before starting triage. Walk through new feature setup if the user chooses.
7. **Pending update check:** If `pending_update_setup` is set in config, show a brief reminder: "You have new features from [version] that need setup. Say 'set up updates' to configure." (stops after 3 reminders)
8. **VIP review check:** Read `last_vip_review` and VIP review cadence from config. If the review is due per the user's configured cadence (monthly / bi-weekly / weekly / quarterly / on demand), trigger the VIP Review prompt (from setup-wizard.md) before starting triage. Update the date after review or skip. If cadence is "on demand", skip this check entirely.
9. **Voice profile review check:** Read `voice_profile_last_reviewed` from config. If review is due per the user's configured voice review cadence (monthly minimum), trigger the Mandatory Monthly Voice Review prompt (see SKILL.md) before starting triage.
10. **Inbox report check:** Read `inbox_report_last_generated` from config. If a report is due per the user's configured cadence, note it and generate after triage completes (or remind: "Your monthly inbox report is due. I'll generate it after triage.")
11. Load folder rules from `[data-path]/folder-rules.md`.

---

## Step 1: Determine Time Range

Ask: **"When did you last check email?"** or accept a stated timeframe.

- If the user says a specific time: use that as the `after:` filter
- If vague ("this morning", "yesterday"): estimate and confirm
- If first triage of the day: default to last 24 hours or since last triage timestamp
- Save the current timestamp as the latest triage time in config

---

## Step 2: Pull Messages

### Email — ALWAYS Query Both Gmail MCP AND Rube

**IMPORTANT:** Every email pull must query ALL connected email sources in parallel — both Gmail MCP and any Rube-connected email accounts (Gmail via Rube, Outlook, etc.). Never rely on a single source. Merge and deduplicate results before presenting.

**Via Gmail MCP — run TWO searches:**

Starred emails:
```
q: "is:starred is:unread"
maxResults: 20
```

Unread inbox:
```
q: "in:inbox is:unread after:YYYY/MM/DD"
maxResults: 50
```

**Via Rube — run matching searches in parallel:**

Query all Rube-connected email accounts with equivalent search criteria (starred + unread, unread inbox for time range). This ensures emails from Outlook, secondary Gmail accounts, or any Rube-connected mail provider are included.

**Merge & Deduplicate:**

After both sources return results:
1. Combine all results into a single list
2. Deduplicate by Message-ID or sender + subject + timestamp
3. Label which account/connection each email came from (e.g., "[Gmail MCP]", "[Outlook via Rube]")
4. If the same email appears from both MCP and Rube, keep one and note the source

### Slack (if connected)

Search for:
- DMs to the user (unread)
- @mentions in priority channels
- Messages in priority channels since last check

### iMessage (if connected)

Pull unread iMessage conversations via macOS AppleScript/Shortcuts:
- Unread 1:1 conversations since last triage
- Unread group chat messages since last triage
- Messages from VIP contacts (always surface)
- Match phone numbers/emails to VIP contact list and address book for display names

### Other Messaging Platforms (if connected)

Pull unread messages from each connected platform.

---

## Step 3: Apply Rules & Route to Folders

Before presenting anything, run all active rules and folder rules against every message:

1. Process rules in order (first match wins per message)
2. Route emails to folders based on folder rules (Low Priority, Newsletters, Finance, etc.)
3. Track which rules were applied and which folders received emails
4. Auto-processed messages are NOT shown individually — summarized at the top
5. **VIP check** — Any emails from VIP senders are flagged for immediate alert (see Step 4)

**Rules & Folder Summary:**

```
⚡ RULES AUTO-PROCESSED: 12 messages
├── 🗑️ Auto-junked: 7 (LinkedIn ×3, Instagram ×2, marketing ×2)
├── 🗑️ Auto-deleted: 2 (blocked sender ×1, pattern match ×1)
├── 📂 Auto-archived: 3 (Amazon order, shipping ×2)
├── 🏷️ Auto-labeled: 2 (payment confirmation → "Finance")
└── 0 forwarded, 0 reminders created

📂 ROUTED TO FOLDERS: 8 messages
├── Low Priority: 4 (CC'd threads ×2, vendor updates ×2)
├── Newsletters: 2 (Morning Brew, TechCrunch)
├── Finance: 1 (bank alert)
├── Automated/Bot: 1 (GitHub notification)
└── Review cadence: Low Priority (weekly), Newsletters (weekly), Finance (daily)

[Show details] [Review folder items now] or continue to triage?
```

---

## Step 4: VIP Immediate Alerts

Before normal categorization and batching, check if any unprocessed emails are from VIP senders. If so, present them immediately with full details and a pre-written draft reply.

For each VIP email:

```
🚨 VIP EMAIL — [Sender Name] ([Relationship])

From: [Full Name] <[email]>
Subject: [Subject line]
Received: [Day, Date, Time]
Thread: [New / Reply in thread of X messages]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FULL EMAIL:
[Complete email body — not a summary]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PRE-WRITTEN DRAFT REPLY:
[Draft reply in user's voice, tone matched to VIP relationship tag
and any priority notes. Uses brand voice if client-facing and BKC connected.
Considers full thread context if this is a reply.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ [Send Draft] [Edit Draft] [Rewrite Draft] [Remind Me] [Deep Dive (full thread)] [Skip for now]
```

**Draft generation logic:**
1. Read the full email/thread
2. Check VIP contact settings for voice override and priority notes
3. Determine voice: personal (default) or brand (if client + BKC connected)
4. Generate draft considering email content, thread context, and relationship
5. Include any CC instructions from VIP priority notes

If multiple VIP emails exist, present each one sequentially. After all VIP alerts are processed:

> "All VIP emails addressed. Continuing to regular triage..."

---

## Step 5: Categorize Remaining Messages

For each message not handled by rules or VIP alerts, categorize:

- Check sender against VIP list → 🔴 RESPOND
- Check for urgency keywords → escalate
- Check sender/content patterns → 🔴 / 🟡 / 🗑️ / 🔕
- Apply the categorization logic from SKILL.md

---

## Step 6: Present Batch

Sort all categorized messages:
1. ⭐ Starred first
2. 🔴 RESPOND by urgency (HIGH → MEDIUM → LOW)
3. 🟡 FYI
4. 🗑️ JUNK (grouped at end)

Present the first batch (default 10):

```
📧 INBOX TRIAGE — [X] messages ([X] after rules)
Last checked: [time range]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#1] ⭐🔴 HIGH — Jim Schlosser <jim@example.com>
Subject: Re: Q2 Projections — need your input
Received: Today, 8:42 AM

Jim needs your sign-off on the Q2 revenue projections before
his Friday meeting with the board. Attached a spreadsheet with
3 scenarios — wants to know which you're comfortable presenting.

→ [Draft Reply] [Remind Me] [Mark Read] [Deep Dive] [Create Rule]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#2] 🔴 MED — Joel Barbour <joel@thegreatpnw.com>
Subject: Wholesale pricing question
Received: Today, 7:15 AM

Joel asking about wholesale margin structure for a potential
retail partnership. Wants to know if 50% off retail is standard
or if you'd recommend a different approach.

→ [Draft Reply] [Remind Me] [Mark Read] [Deep Dive] [Create Rule]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#3] 🟡 FYI — Google Calendar
Subject: Accepted: Client Sync with Bryan Howell
Received: Today, 6:30 AM

Bryan accepted the 2pm meeting. No action needed.

→ [Mark Read] [Remind Me]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#4-7] 🗑️ JUNK (4 items)
├── #4: Salesforce — "Your trial is expiring"
├── #5: Webinar invitation — "Scale Your Agency in 2026"
├── #6: HubSpot — Product update newsletter
├── #7: Unknown sender — "Quick question about your services"
→ [Delete All Junk] [Review Each] [Create Rules]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 SLACK (2 items)

[#8] 🔴 — Scott Ellis (DM)
"Hey, the dashboard prototype is ready for review.
Can you take a look today? Link: [url]"

→ [Draft Reply] [Remind Me] [Mark Read]

[#9] 🟡 — #team-updates
Annie posted the weekly metrics report. Revenue up 12% WoW.

→ [Mark Read] [Remind Me]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💬 iMESSAGE (2 items)

[#10] 🔴 — Kory Davis
"Hey can you send me the updated contract?
Client is asking for it today"

→ [Draft Reply] [Remind Me] [Mark Read]

[#11] 🟡 — Family Group Chat
Mom shared a photo and asked about weekend plans.

→ [Draft Reply] [Mark Read] [Skip]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 CALENDAR — Today
├── ❓ 10:00 AM — "Vendor Review" (unresponded — from Sarah Kim)
├── ✅ 2:00 PM — "Client Sync" (Bryan Howell — confirmed)
├── ✅ 4:00 PM — "Team Standup"
→ Calendar: [Accept C1] [Decline C1] [Tentative C1]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 TASKS — 2 due today, 1 overdue
├── 🔴 OVERDUE: T012 — Follow up with Kory on dashboard feedback (due yesterday)
├── 🟡 Today: T015 — Review Adam's March ad report (due 5pm)
└── 🟡 Today: T016 — Send JTC retargeting notes to Annie (due EOD)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Give me your calls — e.g. "1: draft, 2: remind tomorrow 9am, 3: read, 4-7: delete, 8: draft, 9: read, 10: draft, 11: skip, C1: accept"
(Tip: add "via imessage", "via slack", or "via channel" to any remind action to override your default reminder channel)
```

---

## Step 7: Process Actions

After the user gives their calls:

### Immediate Actions (process silently, confirm in batch)
- `read` → Mark as read
- `delete` → Flag for deletion
- `skip` → Leave in inbox

> "✓ Done — #3, #9 marked read. #4-7 deleted."

### Draft Actions

**Single draft:** Generate and present immediately for review. Save/send only after approval.

**Multiple drafts (2 or more) — batch mode:** Generate all drafts in parallel, present together for a single review pass. Eliminates sequential back-and-forth.

For each draft:
1. Read the full email thread
2. Determine voice: personal voice (default) or brand voice (if recipient is a client and BKC connected)
3. Auto-select tone from VIP contact settings; otherwise use voice profile defaults
4. Draft in the user's voice

**Batch format:**

```
DRAFTS READY — 3 to review

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DRAFT 1 — Reply to Jim Schlosser (Email)
[Full draft text]

[Save as Draft / Send / Edit / Start Over]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DRAFT 2 — Reply to Joel Barbour (Email)
[Full draft text]

[Save as Draft / Send / Edit / Start Over]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DRAFT 3 — Reply to Kory Davis (iMessage)
[Draft text]

[Send / Edit / Start Over]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Say "approve all" to save/send all, or call out specific ones:
"1: approve, 2: edit — make it shorter, 3: approve"
```

- **"Save as Draft"** appears when email is connected via Gmail MCP (draft only — user sends manually from Gmail)
- **"Send"** appears when email is connected via Rube (full write) or for iMessage/Slack
- When editing a single draft in a batch, regenerate and re-present only that draft
- Only save/send after the user approves each draft or says "approve all"

### Remind Actions
For each `remind [time]` or `remind [time] via [channel]`:
1. Add row to task tracker Google Sheet
2. Create Google Calendar event with context
3. Schedule reminder delivery via the user's configured channel (Slack channel, Slack DM, or iMessage) — or the channel specified with `via imessage` / `via slack` / `via channel`
4. If delivering to Slack channel: post a formatted reminder message to the configured channel (e.g., `#inbox-reminders`) at the scheduled time
5. If delivering to iMessage: send a formatted iMessage to the user at the scheduled time
6. Confirm: "✓ T017 created — remind you about Jim's projections tomorrow at 9am via [channel]"

### Standalone Remind (outside triage)
Users can create reminders at any time without being in a triage session:

> "Remind me to follow up with Joel about wholesale pricing tomorrow at 2pm"
> "Set a reminder for Friday 9am to send the updated contract to Kory"
> "Remind me every Monday at 9am to check the client dashboard"

Process:
1. Parse task description, time, and any recurrence pattern
2. Add to task tracker + calendar + schedule delivery via configured channel
3. For recurring reminders: store the recurrence pattern, auto-schedule next instance after each fires
4. Confirm: "✓ T018 created — I'll remind you to [task] at [time] via [channel]"

### Unsubscribe Actions

For each `unsub`, execute the unsubscribe — not just flag it. Behavior depends on `unsubscribe_mode` in config.

**For each sender:**
1. Check for `List-Unsubscribe` header in the raw email:
   - `mailto:` → send the unsubscribe email automatically
   - `https://` → execute a GET request to complete the unsubscribe
2. If no header, scan the email body for "unsubscribe", "opt out", "manage preferences" links → extract URL
3. If nothing found → offer to create an auto-junk rule for the sender

**In `auto` mode:** Execute immediately, report in the confirmation line with other immediate actions.

**In `batch` mode:** Queue all unsubscribes and present at the end of triage:

```
UNSUBSCRIBE QUEUE — [X] senders

├── [sender1] — List-Unsubscribe header ✓ (will execute automatically)
├── [sender2] — Link found: [url] — confirm? [Yes / Skip]
└── [sender3] — No mechanism found — create auto-junk rule? [Yes / Skip]

[Execute all] [Review each]
```

**In `manual` mode:** Surface the link or header URL, let the user handle it.

**After each successful unsubscribe:**
- Create a rule to auto-junk future emails from that sender (they may still arrive)
- Count in the triage complete summary under "🔕 Unsubscribed"

### Delegate Actions
For each `delegate [name]`:
1. Draft a forwarding email to the named person
2. Include context for the delegate
3. Present for approval before sending

### Rule Actions
For each `rule`:
1. Launch the `/create-rule` flow for that specific message
2. Return to triage after rule is created

---

## Step 8: Next Batch

After all actions processed:

> "Batch 1 complete. [X] messages remaining. Ready for the next batch?"

Repeat Steps 6-8 until all messages are triaged.

---

## Step 9: Triage Complete

```
✅ TRIAGE COMPLETE

Processed: [X] messages
├── 🚨 VIP emails addressed: [X] (drafts sent/pending)
├── 🔴 Responded/drafted: [X]
├── 🟡 Marked read: [X]
├── 🗑️ Deleted: [X] (manual: [X], rule-based: [X])
├── 🔕 Unsubscribed: [X]
├── ⏰ Reminders set: [X]
├── 📤 Delegated: [X]
├── ⚡ Auto-processed by rules: [X]
├── 📂 Routed to folders: [X]
│   ├── Low Priority: [X]
│   ├── Newsletters: [X]
│   └── [Other folders]: [X]
├── 📅 Calendar actions: [X]
├── 💬 iMessage processed: [X]

📋 Open tasks: [X] (including [X] new from this triage)

Next triage: Say "any new emails?" anytime for a quick check.
```

Save triage timestamp to config for next session's time range. Track deletion counts (manual vs. rule-based) for inbox report.

---

## Quick Triage Mode

When the user says "any new emails?" or "quick check" (not a full triage):

1. Only pull emails received since last triage timestamp
2. Apply rules silently
3. If nothing needs attention: "All clear since [last check time]. [X] messages auto-processed by rules."
4. If items need attention: Present only 🔴 RESPOND items, summarize the rest
   > "3 new emails since 10am. 1 needs your attention, 2 are FYI:"

---

## Step 10: Post-Triage Actions

After triage is complete, check for pending automated actions:

1. **Inbox report due?** If a report is due per the user's configured cadence, generate and deliver it now:
   > "Your [monthly/bi-weekly/weekly] inbox report is ready. Generating now..."
   > [Run `/inbox-report` flow]

2. **Folder digest due?** If any folder digests are due (e.g., weekly Low Priority digest), present them:
   > "Your weekly Low Priority digest is ready — [X] emails this week. Want to review?"

3. **Rule suggestions due?** Based on the user's configured review cadence, present learned suggestions.

---

## Learned Rule Suggestions

Based on the user's configured review cadence (every triage / every 3rd triage / weekly / monthly / on demand), check for patterns and suggest rules:

> "I've noticed some patterns from your recent triages:"
>
> **DELETE RULES:**
> - "You've deleted emails from [sender] 5 times. Auto-delete future emails from them?" [Enable / Dismiss]
> - "You never open emails from [sender]. Auto-delete + unsubscribe?" [Enable / Dismiss]
>
> **PRIORITIZATION RULES:**
> - "You respond to [sender] within an hour every time. Add them as VIP?" [Enable / Dismiss]
> - "You always star emails from [sender]. Auto-escalate to 🔴 HIGH?" [Enable / Dismiss]
>
> **ORGANIZATION RULES:**
> - "You always mark read emails from [type]. Auto-archive them?" [Enable / Dismiss]
> - "You always label [type] emails the same way. Auto-label?" [Enable / Dismiss]
>
> "[Enable all / Review each / Dismiss all / Change review cadence]"
