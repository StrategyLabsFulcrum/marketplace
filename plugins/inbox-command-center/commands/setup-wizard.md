# Setup Wizard

Walk the user through complete onboarding for the Inbox Command Center. The wizard handles three user paths:

- **New user** — full setup (~18 steps)
- **v1.3 existing user** — targeted migration flow + new-feature opt-in (see Step 0)
- **Returning user re-running wizard** — skip already-configured steps

## Before Starting

1. **Check for existing setup** at `~/Inbox Command Center/.meta.json`:
   - Exists with current version → user is fully set up; ask if they want to add inboxes, reconfigure, or run a partial wizard
   - Exists with older version → run update flow for new features only
   - Missing, but old v1.3 path exists at `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/` → run **Step 0: Migration**
   - Missing entirely → fresh install, run full wizard from Step 0a

2. **Greet briefly:**
   > "Welcome to Inbox Command Center setup. This takes about 15-20 minutes the first time. You can pause and resume anytime — your progress is saved as we go."

---

## Step 0: v1.3 Migration (existing v1.3 users only)

If the legacy v1.3 path exists, run the migration flow from `docs/v1.4-migration.md` before continuing the wizard. Migration is interactive, idempotent, preserves a 30-day backup at `.v1.3-backup/`, and ends by either rejoining the wizard at the relevant step or jumping straight to Step 18 if the user's existing config is fully migrated.

The migration covers:
- Workspace path move (slug → Finder-visible name)
- Data file conversions (vip-contacts → contacts, tasks → todos+followups, rules tag with stakes/scope)
- Composio re-auth for Gmail (was native MCP) and Outlook (was Rube)
- Multi-account opt-in
- Fireflies opt-in (if not already connected)
- New workspace files initialized

After migration, skip to Step 18 (Workspace Tour) unless the user explicitly opts to reconfigure something.

---

## Step 0a: Composio Account

Composio is the primary connection layer for Gmail, Outlook, and several other tools. It provides full inbox control: read, search, draft, send, archive, label, trash — across Gmail and Outlook, with multi-account support.

```
Step 0a — Composio Account

Inbox Command Center uses Composio for full inbox management:
read, search, draft, send, archive, label, trash. It supports
multiple Gmail and Outlook accounts per user, plus connectors for
Otter, Gong, and Fathom.

Do you have Composio access?

  [ ] Yes — I have a Composio account already
       → Proceed to email OAuth (Step 1)
       
  [ ] No, but I'm at Strategy Labs
       → Email scott@strategylabs.us to be added to the SL team
         Composio account.
       → I'll wait. Type "ready" once Scott confirms access.
       
  [ ] No, I'll set up my own Composio account
       → Walk through composio.dev signup (~3 min):
         1. Open https://composio.dev
         2. Sign up with email or Google
         3. Verify email
         4. Return here and type "ready"
       
  [ ] Skip — use limited fallback
       ⚠️ Warning: fallback mode loses Outlook, multi-account, and
          Otter/Gong/Fathom. Native Gmail MCP only, single account.
       → Sets .meta.json.fallback_mode: true
       → Skip to Step 1 with native MCP path
```

If user chooses fallback, every subsequent step that depends on Composio is bypassed with a note about what's unavailable.

If Composio is set up, run a sanity check: call `mcp__claude_ai_Composio__COMPOSIO_MANAGE_CONNECTIONS` to confirm the account is reachable.

---

## Step 1: Connect Email

Connect one or more Gmail and/or Outlook accounts via Composio.

```
Step 1 — Connect Email

Which platform(s) would you like to connect?

  [ ] Gmail only
  [ ] Outlook / Microsoft 365 only
  [ ] Both
  [ ] Coming in v1.5: iCloud Mail, Generic IMAP

Then I'll loop through OAuth for each account you want to add.
```

### OAuth flow per account

For each inbox:

1. Call `mcp__claude_ai_Composio__COMPOSIO_MANAGE_CONNECTIONS` with the platform (`gmail` or `outlook`)
2. Display the OAuth URL; ask user to complete in browser
3. Use `COMPOSIO_WAIT_FOR_CONNECTIONS` until success (or timeout)
4. Sanity check: call `GMAIL_FETCH_EMAILS` (or Outlook equivalent) with `max_results: 1`
5. Ask the user for an alias for this inbox: `"What should I call this inbox? (e.g. 'personal', 'uno-mas', 'work')"`
6. Append to `.meta.json.connected_inboxes[]`:
   ```json
   {
     "alias": "personal",
     "platform": "gmail",
     "account": "ramsey@strategylabs.us",
     "composio_connection_id": "[from Composio]",
     "folders_enabled": []
   }
   ```

After each account: "Add another inbox? [Yes / No, continue]"

Loop until user says no. After last inbox, confirm:

```
✓ Connected inboxes:
  - personal (gmail) — ramsey@strategylabs.us
  - uno-mas (gmail) — ramsey@unomastacos.com
  - ms365   (outlook) — ramsey@...

Total: 3 inboxes
```

### Fallback path (native Gmail MCP)

If user is in fallback mode: skip Composio OAuth. Use the native Gmail MCP only. Single account assumed (user's primary Gmail). Set:
```json
"connected_inboxes": [{"alias": "primary", "platform": "gmail", "account": "...", "connection": "native-mcp"}],
"fallback_mode": true
```

---

## Step 2: Connect Messaging Platforms

### Slack

Slack uses native MCP (richer feature surface than Composio's wrapper).

```
Step 2a — Connect Slack (Optional)

Slack will be triaged alongside email. Replies use your voice.

  [ ] Connect Slack — proceed with native MCP OAuth
  [ ] Skip
```

If yes, walk through Slack MCP authentication. Verify with `mcp__claude_ai_Slack__slack_search_users` test call.

### iMessage

iMessage uses macOS AppleScript/Shortcuts.

```
Step 2b — Connect iMessage (Optional, Mac-only)

iMessage triage and reminder delivery via macOS AppleScript.
Requires Messages app configured on this Mac.

  [ ] Connect iMessage
       → Verify Messages.app is running
       → Capture user's iMessage ID (phone or Apple ID)
       → Test with a no-op AppleScript call
       → Set as available reminder delivery channel
  [ ] Skip
```

### Other messaging platforms

```
Step 2c — Other Platforms (Optional)

  [ ] WhatsApp — via Composio
  [ ] Teams — via Composio
  [ ] SMS / Twilio — via Composio
  [ ] None
```

Each runs through `COMPOSIO_MANAGE_CONNECTIONS` for the relevant connector if Composio is enabled.

---

## Step 3: Connect Calendar

```
Step 3 — Connect Calendar

  [ ] Google Calendar (native MCP — recommended for Gmail users)
  [ ] Outlook Calendar (Composio — recommended for Outlook users)
  [ ] Both
  [ ] Skip
```

For Google Calendar: standard MCP OAuth. Test with `mcp__claude_ai_Google_Calendar__list_calendars`.

For Outlook Calendar: `COMPOSIO_MANAGE_CONNECTIONS` with the calendar connector. Test with the equivalent list call.

If user has multiple connected email inboxes, default the calendar to match the primary inbox's platform but allow override.

---

## Step 4: Connect Fireflies (Recommended)

Fireflies is **the primary signal for your voice profile** — meeting transcripts capture how you actually talk, which is more authentic than written email.

```
Step 4 — Connect Fireflies (RECOMMENDED)

Fireflies feeds the most important parts of Inbox Command Center:

  • Voice profile — drafts that sound like you, refined over time
  • contacts.md — per-recipient tone and recent-context notes
  • Triage enrichment — "you spoke with X on Y about Z" inline

Connect now? It's the single biggest improvement to draft quality.

  [ ] Yes, connect Fireflies (~2 min OAuth + 30-day pull)
  [ ] Skip — I'll connect later (drafts will be less accurate)
```

If yes:

1. Run native MCP OAuth for Fireflies
2. Verify with `mcp__claude_ai_Fireflies__fireflies_get_user`
3. **Initial pull (blocking, ~1-3 min):**
   - `fireflies_get_transcripts` for last 30 days
   - For each transcript: extract participants, key phrases, decision language
   - Stage data for voice profile (Step 5) and contacts.md (Step 7)
4. Set `.meta.json.last_fireflies_pull` to today
5. Configure weekly pull schedule (default Sunday off-hours):
   ```
   Pull cadence:
     [ ] Weekly (Sundays off-hours) — recommended
     [ ] Daily
     [ ] On-demand only
   ```

If skipped: nudge on next 3 triages ("You haven't connected Fireflies yet — voice profile will improve significantly when you do").

### Other transcript sources (Optional)

```
Step 4b — Other Transcript Sources

  [ ] Otter.ai — via Composio
  [ ] Gong — via Composio
  [ ] Fathom — via Composio
  [ ] Zoom (cloud recordings) — via Composio
  [ ] None
```

These supplement Fireflies but don't replace it. Each runs through Composio OAuth.

---

## Step 5: Build Voice Profile

### Phase A: Analyze Sources

For each connected source, analyze:

```
Source A: Fireflies transcripts (PRIMARY signal)
  - Last 30 days (just pulled in Step 4)
  - Extract: greetings, closings, common phrases, tone shifts by audience,
    vocabulary, humor style, sentence structure
  - Weight: highest (this is your unscripted voice)

Source B: Sent email (across all connected inboxes)
  - Last 30-60 days from each inbox
  - Greeting patterns by recipient type
  - Sign-off patterns
  - Average length, tone range, common phrases

Source C: Slack (if connected)
  - Last 30 days of sent messages
  - Tone by channel, emoji/reaction usage, length

Source D: iMessage (if connected)
  - Last 30 days of sent messages
  - Casual tone, abbreviations, personal vs. professional style
```

Show user a summary:

```
Sources analyzed:
  ✓ Fireflies: 14 transcripts (12 hours of audio)
  ✓ Email: 247 sent messages across 3 inboxes
  ✓ Slack: 412 messages across 18 channels
  ✓ iMessage: 89 messages across 12 contacts

Initial voice profile generated.
```

### Phase B: A/B Voice Calibration (Step 6)

Run after Phase A — see Step 6.

### Phase C: Generate Voice Profile

Write `~/Inbox Command Center/voice-profile.md` per the schema in SKILL.md (Core Style, Greetings, Sign-Offs, Signature Phrases, NEVER List, Tone by Audience, Channel Differences, Email Length Preference, A/B Calibration Results, Review History).

If BKC is connected, also generate `voice-profile-brand.md` from `brand-identity.md`.

---

## Step 6: A/B Voice Calibration

Run 20+ pairs across email / Slack / SMS / formal scenarios. Same flow as `/voice-calibration`:

1. **Batch 1: 10 core email pairs** (client question, missed deadline, saying no, thanks, intro, favor, bad news, ack, scheduling, complaint)
2. **Batch 2: Channel-specific** (5 Slack, 5 SMS, 5 formal email)
3. **Continue until calibrated** — keep generating pairs until user says "both sound like me" across all categories

Save preferences to voice profile. Log run to today's session log.

---

## Step 7: VIP Contacts

```
Step 7 — VIP Contacts

VIPs get special treatment:
  • Cross-inbox scan at session start
  • Pre-written drafts on every email
  • Daily VIP digest per inbox
  • Auto-tracked timeline (last email + last meeting)

Capture your VIP list:

  [ ] Auto-detect from sent mail patterns
       → Show top 20 frequent recipients across all inboxes
       → User picks which are actually VIPs
  [ ] Manual entry
       → Type names + emails one at a time
  [ ] Both — auto-detect first, then add manual
```

For each VIP captured, write a placeholder section to `~/Inbox Command Center/contacts.md`:

```markdown
## [Name] <[email]> [VIP]
**Review:** [cadence] | **Since:** [today]
- Tone: [populated by Fireflies pull + draft edits]
- Recent context: [populated by next Fireflies pull]
- Inboxes seen: [populated on first triage]
- Last email: [populated on first triage]
- Last meeting: [populated by Fireflies pull]
```

### VIP Review Cadence

```
How often should I prompt you to review your VIP list?

  [ ] Weekly
  [ ] Bi-weekly
  [ ] Monthly (recommended)
  [ ] Quarterly
  [ ] On demand only
```

Save to `.meta.json.schedules.vip_review_cadence`.

### Daily VIP Digest

```
Daily VIP digest — separate per inbox, same delivery channel by default.

Delivery channel:
  [ ] Slack DM (recommended)
  [ ] iMessage
  [ ] Email (sent to your primary inbox)
  [ ] All of the above
  [ ] Off

Time: [HH:MM] (default: same as morning briefing)
```

Save to `.meta.json.schedules.vip_digest`.

---

## Step 7a: Strategy Labs VIP Defaults (SL deployment only)

If the user is on the SL team Composio account or otherwise identifies as Strategy Labs:

```
Step 7a — Strategy Labs VIP Defaults (Optional)

Use the Strategy Labs default VIP list as a starting point?
This adds the SL team and key partners as VIPs in your contacts.md.
You can edit or remove them anytime.

  [ ] Yes, add SL VIP defaults
       → Copies deployments/strategy-labs/vip-seed.md entries
         into contacts.md
  [ ] No, I'll manage my own VIP list
```

Skip this step entirely for non-SL users.

---

## Step 8: Triage Preferences

```
Step 8 — Triage Preferences

Multi-account triage mode:
  [ ] Sequential — pick one inbox per session (recommended)
  [ ] Aggregated — single stream across all inboxes

Batch size (emails per batch during triage):
  [ ] 5
  [ ] 10 (recommended)
  [ ] 20

Triage time range default (when you don't specify):
  [ ] Since last triage
  [ ] Last 24 hours (recommended)
  [ ] Last 7 days
```

Save to `.meta.json.schedules.batch_size` and related fields.

---

## Step 8b: Configure Folder Rules

For each connected inbox, ask which folders to enable. Default: enable Newsletters, Receipts, and Low Priority — others are opt-in.

```
Step 8b — Folders for [inbox alias]

Which logical folders should be active in this inbox?

  [✓] Low Priority    — non-urgent emails, weekly digest, archive 30d
  [✓] Newsletters     — newsletters you read, weekly digest, delete 14d unread
  [✓] Receipts & Orders — purchase confirmations, never review, keep
  [ ] Finance         — bank alerts, daily digest
  [ ] Automated/Bot   — system notifications, daily count, delete 7d
  [ ] Pending Review  — emails to come back to, every triage, remind 3d
  [ ] Delegated       — forwarded items, daily, remind 5d if no response

For each enabled folder, I'll create the platform-native equivalent
(Gmail label or Outlook subfolder) automatically.
```

For each enabled folder, execute:
- Gmail: `GMAIL_CREATE_LABEL` with name `ICC/[Folder Name]`
- Outlook: create subfolder `Inbox/ICC/[Folder Name]` via Composio

Update `.meta.json.connected_inboxes[i].folders_enabled[]`.

Repeat for each inbox.

### Per-folder cadence customization

```
Want to customize folder review cadences?

  [ ] Use defaults (recommended)
  [ ] Customize per folder
       → For each enabled folder, ask:
         • Review cadence: every triage / daily / weekly / monthly / never
         • Review style: individual / summary / count only / skip
         • Auto-action: keep / archive after Xd / delete after Xd / remind after Xd
```

Save folder rules to `rules.md` with `Type: folder` entries.

---

## Step 8c: Rule Suggestion Cadence

```
Step 8c — Learned Rule Suggestions

How often should I review patterns and suggest new rules?

  [ ] Every triage — surface suggestions after every session
  [ ] Every 3rd triage (recommended) — light cadence
  [ ] Weekly — bundled summary
  [ ] Monthly — included with monthly report
  [ ] On demand only — never auto-surface
```

Save to `.meta.json.schedules.rule_suggestion_cadence`.

---

## Step 8d: Inbox Report Schedule

```
Step 8d — Inbox Report

Comprehensive analytics report:
  - Cross-inbox section (VIPs, voice drift, Fireflies, global rules)
  - Per-inbox sections (volume, deletions, folders, trends, inbox zero days)
  - Source data: session logs + current state

Cadence:
  [ ] Monthly (recommended)
  [ ] Bi-weekly
  [ ] Weekly

Day: [1st of month / last business day / custom]
Delivery:
  [ ] Email (recommended)
  [ ] Slack DM
  [ ] iMessage
  [ ] Multiple
```

Save to `.meta.json.schedules.inbox_report_cadence`.

---

## Step 8e: Voice Profile Review Cadence

```
Step 8e — Voice Profile Review

Mandatory cadence (your voice will be re-analyzed at this rate):

  [ ] Monthly (recommended, minimum)
  [ ] Bi-weekly
  [ ] Weekly

The review re-analyzes Fireflies, sent email, Slack, iMessage, and
draft edits since the last review. It offers targeted A/B for any
areas where the profile seems outdated.

Note: Drift-triggered A/B fires automatically when 3+ substantial
edits happen in a single session — you don't have to wait for the
mandatory review to recalibrate.
```

Save to `.meta.json.schedules.voice_review_cadence`.

---

## Step 8f: Task Tracker (Optional Mirroring)

The canonical task store is `todos.md` + `followups.md` in the workspace. You can optionally mirror time-bound items to an external system:

```
Step 8f — Optional Task Mirroring

Workspace files (canonical):
  ✓ todos.md       — things you owe yourself
  ✓ followups.md   — people waiting on you

Mirror time-bound todos to an external system?
  [ ] Apple Reminders (recommended for Mac users)
       → Mirror to "Inbox Tasks" list
  [ ] Google Calendar events (any todo with a due date creates an event)
  [ ] Outlook Tasks (for Outlook users — via Composio)
  [ ] None — workspace files only
  [ ] Multiple
```

Mirroring is one-way: workspace → external. The workspace remains canonical.

---

## Step 8g: Scheduled Daily Briefing

```
Step 8g — Daily Briefing

Aggregated across all connected inboxes (with per-inbox sections).

Delivery channel:
  [ ] Slack DM (recommended)
  [ ] iMessage
  [ ] Email digest
  [ ] Calendar block
  [ ] All

Time: [HH:MM] (default: 7:30 AM)
Days: [Weekdays / Daily / Custom]

Includes:
  ✓ Email summary (per inbox)
  ✓ VIP cross-inbox count
  ✓ Slack / iMessage summary
  ✓ Calendar flags
  ✓ Tasks (todos + followups)
  ✓ Rules summary
```

Save to `.meta.json.schedules.daily_briefing`.

---

## Step 8h: Reminder Delivery Channel

```
Step 8h — Reminder Delivery

Where should reminders be delivered?

  [ ] Dedicated Slack channel (recommended — visible reminder log)
       → Default name: #inbox-reminders
       → I'll create it now if it doesn't exist
  [ ] Slack DM (private)
  [ ] iMessage (text yourself at scheduled time)

Per-reminder override is supported: "remind me tomorrow 9am via imessage".
```

If user picks dedicated Slack channel and it doesn't exist, create it via Slack MCP.

Save to `.meta.json.reminder_delivery`.

---

## Step 9: Standard Rules

Suggest the standard rule library, each tagged with default stakes and per-inbox scope:

```
Step 9 — Standard Rules

Based on a quick scan of your inboxes, here are recommended rules.
Each rule is tagged: [Type] [Stakes] [Scope]

  [✓] [delete][low_stakes][per-inbox: personal] Auto-junk LinkedIn notifications
  [✓] [delete][low_stakes][per-inbox: personal] Auto-junk Instagram/Facebook
  [✓] [organize][low_stakes][per-inbox: personal] Label Amazon/UPS as Orders
  [✓] [delete][low_stakes][per-inbox: personal] Auto-junk marketing emails
  [✓] [organize][low_stakes][per-inbox: uno-mas] Label bank alerts as Finance
  [✓] [organize][low_stakes][per-inbox: all] Bundle GitHub notifications into digest
  [✓] [prioritize][low_stakes][global] VIP contacts always 🔴 RESPOND
  [✓] [prioritize][low_stakes][per-inbox: all] Urgency keywords escalate to 🔴 HIGH
  [✓] [prioritize][low_stakes][global] Stale follow-up reminders after 3 days
  [ ] [organize][low_stakes][per-inbox: all] Hold messages from quiet hours

[Approve all] [Review each] [Skip standard rules]
```

For each approved rule, append to `rules.md` with full structure (Type, Stakes, Scope, Trigger, Action, Status, Created).

### Custom rules

```
Want to add custom rules now?

  [ ] Yes — launch /create-rule
  [ ] Skip — I'll add custom rules later
```

---

## Step 10: Brand Knowledge Center Integration

```
Step 10 — Brand Knowledge Center (Optional)

If you use Brand Knowledge Center, I can pull your brand voice
profile and use it for client-facing emails automatically.

  [ ] Yes — connect BKC
       → Read brand-identity.md
       → Generate voice-profile-brand.md
       → Mark relevant contacts with [Brand] tag in contacts.md
  [ ] Skip — single voice (personal) for everything
```

If yes: tag client-facing contacts with `[Brand]` (or both `[VIP]` and `[Brand]`) so drafts to them use brand voice.

---

## Step 11: Review & Activate

Show the user a summary of everything configured:

```
Step 11 — Setup Summary

CONNECTIONS
  ✓ Composio: 3 inboxes (personal, uno-mas, ms365)
  ✓ Slack
  ✓ Google Calendar
  ✓ Fireflies (30d pulled, weekly schedule)
  ✓ iMessage
  
WORKSPACE (~/Inbox Command Center/)
  ✓ contacts.md — 12 VIPs captured
  ✓ todos.md / followups.md — empty, ready
  ✓ rules.md — 9 standard rules active
  ✓ voice-profile.md — generated, A/B calibrated
  ✓ voice-profile-brand.md — generated from BKC
  ✓ session-logs/2026-05-08.md — today
  ✓ .meta.json — all schedules saved

SCHEDULES
  Daily briefing:        7:30 AM weekdays, Slack DM
  Daily VIP digest:      7:30 AM, Slack DM (per inbox)
  Weekly Fireflies pull: Sundays
  Voice profile review:  Monthly
  VIP list review:       Monthly
  Inbox report:          Monthly, email
  Rule suggestions:      Every 3rd triage

ANYTHING TO CHANGE?
  [ ] All looks good — activate
  [ ] Edit a specific section
```

On activate:
- Set `.meta.json.version` to current plugin version
- Initialize `session-logs/[today].md` with first entry: "Setup wizard completed"
- Write any pending file changes
- Confirm: "✓ Inbox Command Center activated. Ready when you are."

---

## Step 18: Workspace Tour

```
Step 18 — Workspace Tour (Final)

Open Finder and look at:
  iCloud Drive › Inbox Command Center

You'll see your workspace files. You can edit any of them anytime —
the skill reads them fresh at the start of every session.

Most useful files to know:

  contacts.md          
    Add tone notes for any recipient.
    Example:
    ## Bryan Howell <bryan@dieselpowerproducts.com> [VIP]
    - Tone: concise, numbers-forward, skip pleasantries

  todos.md / followups.md
    Check off items, add manually, edit due dates.

  rules.md
    Pause/edit/delete rules anytime. Each rule has Type, Stakes,
    Scope at the top — flip to Status: Paused to disable.

  session-logs/YYYY-MM-DD.md
    Daily journal of what the skill did. Useful audit trail.

[ Open Finder to my workspace now ]
[ Skip the tour — I'll explore later ]

If you want to roll back to your v1.3 setup later, the backup is at:
  ~/Inbox Command Center/.v1.3-backup/   (kept for 30 days)
```

After tour:

```
✓ Setup complete.

Try these:
  • "triage my inbox"           — VIP scan + sequential triage
  • "show my todos"             — see your todos.md
  • "who's waiting on me"       — see followups.md
  • "edit Bryan's contact card" — open contacts.md to that section
  • "create a rule"             — guided rule builder
  • "show inbox report"         — generate a report on demand

Welcome to v1.4.
```

---

## Resume / Re-run Behavior

If user runs `/setup-wizard` after initial setup is complete:

1. Read `.meta.json` to detect what's already configured
2. Show a menu:
   ```
   Setup options:
     [ ] Add another inbox
     [ ] Reconfigure schedules
     [ ] Re-run voice profile build
     [ ] Re-run A/B calibration
     [ ] Reconfigure folder rules for an inbox
     [ ] Re-run full wizard from scratch
     [ ] Update VIP list
     [ ] Connect a new tool (Slack, Fireflies, etc.)
   ```
3. Jump to the relevant step(s) only

## Error Recovery

If the wizard is interrupted (browser tab closed during OAuth, network error, etc.):

1. State is preserved in `.meta.json.setup_state` — which step was reached, which substeps completed
2. On next launch, resume from last completed step: "Picking up where we left off — you were at Step [X]. Continue?"
3. If user wants to restart a specific step, they can say: "redo step [X]"

## Notes for the skill

- **Always confirm before writing** any file the user might already have populated
- **Show diffs** when modifying existing config
- **Log every step** to today's session log: `**HH:MM** — Setup wizard: completed Step [X]`
- **Sanity-check connections** with a test call after each OAuth before moving on
- **Don't skip Fireflies** without flagging the voice quality regression
