# Triage

The core daily command — pulls unread emails across all connected inboxes, Slack messages, iMessages, and calendar events; applies rules; surfaces VIPs across all inboxes first; then walks the user through prioritized batches in a sequential per-inbox flow with inline actions.

Triggers on: "check my email", "triage", "what did I miss", "any new emails", "inbox", "check my messages", "check my texts", "check iMessage", "clean up my inbox", "triage [inbox-alias]", "anything urgent"

## Before Starting

1. **Read workspace** at `~/Inbox Command Center/` — `.meta.json`, `contacts.md`, `todos.md`, `followups.md`, `rules.md`, `rules-review-queue.md`, `voice-profile.md` (and brand variant if BKC connected).

2. **Run cadence-due checks** (see SKILL.md "Session Start"):
   - Rule review due? Surface gentle prompt before triage starts.
   - Voice profile review due? Same.
   - VIP list review due? Same.
   - Weekly Fireflies pull due? Run it first (off-hours-fast: ~30 sec for incremental pull).
   - Monthly inbox report due? Generate after triage.

3. **Detect user-edited workspace files** since last session (mtime check). Log observed edits to today's session log.

4. **Confirm Composio connections** are alive — if any inbox shows expired session, prompt user to re-auth before triage starts.

5. **Append session start** to `session-logs/[today].md`: `**HH:MM** — Session start. Workspace loaded: [N] inboxes, [X] todos, [Y] followups, [Z] pending rules.`

---

## Step 1: Determine Time Range and Inbox

Ask if not specified:
> "When did you last check email, and which inbox today?"

### Time range parsing

| User says | Time range |
|---|---|
| "since yesterday at 5pm" | absolute timestamp |
| "since [last triage]" | from session log of previous triage end |
| "today" | last 24 hours |
| (nothing specified) | default from `.meta.json.schedules.triage_default_range` (default: last 24 hours) |

### Inbox selection (multi-account)

If user named an inbox alias ("triage uno-mas"): scope to that inbox only, skip Step 1.5's prompt-to-pick.

If user said "triage" / "all" / nothing specific: proceed to Step 1.5 (VIP cross-inbox scan first), then prompt for inbox selection.

If single inbox connected: proceed directly to Step 2 with that inbox.

If in fallback mode: same as single inbox.

---

## Step 1.5: VIP Cross-Inbox Scan (always runs first when multi-inbox + no scoped inbox)

Before user picks a single inbox, scan ALL connected inboxes for VIP messages.

### Scan logic

```
vip_emails = []

For each inbox in .meta.json.connected_inboxes:
  Query (Composio):
    GMAIL_FETCH_EMAILS / OUTLOOK_FETCH_MESSAGES
    query: "is:unread after:[last_check] from:[any VIP email in contacts.md]"
    max_results: 20
    verbose: false (just headers)

For each VIP message found:
  - Cross-reference contacts.md for relationship + recent context
  - If a Fireflies transcript with this person exists in last 30d:
       attach "📞 You spoke with [name] [date] ([topic])"
  - Append to vip_emails with inbox alias
```

### Surface results

If `len(vip_emails) > 0`:

```
🚨 [N] VIP message(s) waiting across your inboxes:

  • Bryan Howell — re: Q3 numbers (in: uno-mas)        ← 14 min ago
    📞 You spoke with Bryan May 3 (Q3 numbers call)

  • Joel Barbour — re: Great PNW campaign (in: personal) ← 2 hr ago

  • Melissa — quick favor (in: personal)               ← 4 hr ago

Handle these first, or proceed to inbox triage?

  [ ] Handle VIPs first (recommended)
  [ ] Skip VIP-first; go to inbox triage
  [ ] Which inbox should I triage?
```

If user picks "Handle VIPs first":
- For each VIP message, run **Step 4 (VIP Immediate Alert)** — full body + pre-written draft + actions
- After all VIPs handled, return to inbox selection prompt

If user picks "Skip" or proceeds to inbox: log "VIP scan: N surfaced — user deferred" and move to Step 2.

If `len(vip_emails) == 0`: surface a one-liner ("No VIPs waiting across [N] inboxes — clean start.") and proceed.

---

## Step 2: Pull Messages

Per the selected inbox(es), execute Composio fetch.

### Email — Composio fetch (per inbox)

For each scoped inbox, run two parallel Composio fetches via `COMPOSIO_MULTI_EXECUTE_TOOL`:

```
[For Gmail inbox]
Fetch 1 — Starred:
  tool: GMAIL_FETCH_EMAILS
  args:
    query: "is:starred is:unread"
    max_results: 20
    verbose: true
  connection_id: <from .meta.json.connected_inboxes[i]>

Fetch 2 — Unread inbox:
  tool: GMAIL_FETCH_EMAILS
  args:
    query: "in:inbox is:unread after:[YYYY/MM/DD]"
    max_results: 50
    verbose: true
  connection_id: <from .meta.json.connected_inboxes[i]>
```

For Outlook inboxes, use `OUTLOOK_FETCH_MESSAGES` with equivalent filters.

**Deduplicate by messageId.** Sort: starred first → most recent → oldest.

**Tag each message with its inbox alias** (used in Step 6 batch presentation).

### Sequential mode (multi-inbox triage)

When user is triaging multiple inboxes sequentially:
1. Pull from inbox #1, run full triage flow (Steps 3-9) for it
2. After Step 9 for inbox #1, ask: "Move to next inbox? [Yes — triage [next] / Done for now]"
3. Repeat for each inbox in order

### Slack (if connected)

Pull unread DMs and @mentions from the time range:
```
mcp__claude_ai_Slack__slack_search_public_and_private
  query: "is:unread after:[date]"
```
Plus channel-rule-flagged messages from priority channels (configured in `.meta.json`).

### iMessage (if connected)

Run AppleScript to pull unread iMessages since last triage. Include 1:1 + group chats. Match contacts to `contacts.md` entries (especially VIPs).

### Other messaging platforms (if connected)

Each via Composio if configured (WhatsApp, Teams, SMS).

---

## Step 3: Apply Rules and Route to Folders

Before showing anything to the user, run through the pulled messages and apply approved rules per resolution order (see SKILL.md Rules Engine).

### Resolution order

1. **Global rules** apply first (across all messages, all inboxes).
2. **Per-inbox rules** apply second (only to messages in their assigned inbox).
3. **Conflict resolution:** specific scope wins (per-inbox overrides global if both match).
4. **VIP-related rules** are inherently global — they ignore per-inbox scope.

### Apply behavior by stakes

**`low_stakes` rules** — execute silently, log to session log, summarize at start of triage:

```
Auto-rules applied to [inbox]:
  ✓ Archived 8 newsletters (rule: ESPN newsletters)
  ✓ Labeled 3 receipts as Finance (rule: Bank alerts → Finance)
  ✓ Marked 6 calendar invites as read (rule: Calendar confirmations)
  ✓ Routed 4 to Newsletters folder
  ✓ Auto-junked 12 LinkedIn notifications

Total auto-processed: 33 messages
```

**`high_stakes` rules** — queue the proposed action; present per-instance for confirmation in Step 6:

```
[in batch] HIGH-STAKES RULE MATCH:
  Rule "Auto-forward AP invoices to operations@dpp" matched message #4
  Action: Forward to operations@dpp
  Confirm? [Yes / No / Edit forward / Disable rule]
```

### Folder routing implementation

For each rule with `Type: folder`, dispatch via the synthetic abstraction:

- **Gmail:** `GMAIL_BATCH_MODIFY_MESSAGES` → `addLabelIds: [Label_ID for "ICC/[FolderName]"]`
  - If label ID not cached, call `GMAIL_LIST_LABELS` first
- **Outlook:** `OUTLOOK_MOVE_MESSAGE` → folder `Inbox/ICC/[FolderName]`

If the target folder isn't enabled in this inbox AND the rule scope is global, auto-enable it (create label/subfolder, update `.meta.json.connected_inboxes[i].folders_enabled[]`) and route silently.

### Log to session log

```
**08:18** — [uno-mas] Auto-rules applied: archived 8 newsletters, labeled 3 receipts, routed 4 to Newsletters folder
```

---

## Step 4: VIP Immediate Alert

If VIPs are present in this inbox AND user did not already handle them in Step 1.5, surface each with full alert format.

```
🚨 VIP EMAIL — [Sender Name] [Relationship from contacts.md]

From: [Full Name] <[email]>
Inbox: [inbox alias]
Subject: [Subject line]
Received: [Day, Date, Time]
Thread: [New / Reply in thread of X messages]
Thread ID: [...] | Message ID: [...]

[If recent Fireflies transcript with this person exists]:
📞 You spoke with [name] on [date] — [topic]
   [1-2 sentence context summary from transcript]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FULL EMAIL:
[Complete email body — not just a summary]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PRE-WRITTEN DRAFT REPLY:
[Draft in user's voice — uses brand voice if recipient tagged [Brand],
 personal voice otherwise. Refined per recipient via contacts.md notes.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ [Send Draft] [Edit Draft] [Rewrite Draft] [Remind Me] [Deep Dive (full thread)] [Skip for now]
```

**Sending account auto-matches receiving inbox.** If the email arrived at `ramsey@unomastacos.com`, the send/draft uses that account.

After all VIPs in this inbox: proceed to Step 5 with remaining (non-VIP) messages.

---

## Step 5: Categorize Remaining Messages

Each remaining message goes into exactly ONE category:

### 🔴 RESPOND — Needs a reply
- Direct questions, decisions, follow-ups
- Anyone in `followups.md` who's now responded
- Financial/legal matters requiring action
- Meeting requests needing confirmation
- Active business relationships
- Urgency keyword matches not handled by auto-rules

### 🟡 FYI — Worth knowing, no reply needed
- Task completion notifications
- Industry news the user follows
- Calendar/payment confirmations
- Business metric alerts
- Shipping confirmations

### 🗑️ JUNK — Flag for deletion
- Marketing/promotional emails (not auto-handled)
- Cold outreach / vendor pitches
- Recruitment spam, surveys
- PR pitches

### 🔕 UNSUBSCRIBE — Repeat junk senders
- Senders appearing in JUNK repeatedly across triage history
- Mailing lists user never engages with

---

## Step 6: Present Batch

Batch size from `.meta.json.schedules.batch_size` (default 10). Sort: VIPs (already handled) → starred → 🔴 by urgency → 🟡 → 🗑️ → 🔕.

Each item tagged with `[inbox-alias]` when in multi-inbox sequential mode.

```
[#1] ⭐🔴 HIGH — [Sender Name] <[email]>  [uno-mas]
Subject: [Subject line]
Received: [Day, Date, Time]
Thread ID: [...] | Message ID: [...]

[1-2 sentence summary of what's needed]

→ Actions: [Draft Reply] [Reply Now] [Archive] [Trash] [Mark Read]
           [Add Followup] [Add Todo] [Create Rule] [Deep Dive]
```

If a `high_stakes` rule matched this message in Step 3, surface its proposed action inline:

```
[#4] 🟡 FYI — accounting@somesupplier.com  [uno-mas]
Subject: April invoice
[Summary]

⚠️ HIGH-STAKES RULE MATCH:
   "Auto-forward AP invoices to operations@dpp"
   Confirm? [Yes / No / Edit forward target / Disable rule]

→ Actions: [Standard action codes still available]
```

After 10 items: "Ready for the next batch, or want to take action on these first?"

---

## Step 7: Process Actions

User responds with action codes per item. Process them per the table below.

### Action codes

| Code | Action | Implementation |
|---|---|---|
| `draft` | Draft reply in voice | See Draft Actions below |
| `reply` | Same as draft + send on confirmation | `GMAIL_REPLY_TO_THREAD` / `OUTLOOK_REPLY_MESSAGE` |
| `remind [time]` | Add to todos.md + calendar event | See Remind Actions |
| `read` | Mark as read | `GMAIL_BATCH_MODIFY_MESSAGES` removeLabelIds: ["UNREAD"] / Outlook equivalent |
| `delete` | Move to trash | `GMAIL_MOVE_TO_TRASH` (recoverable) |
| `archive` | Remove INBOX label | `GMAIL_BATCH_MODIFY_MESSAGES` removeLabelIds: ["INBOX"] |
| `unsub` | Execute unsubscribe | See Unsubscribe Actions |
| `dive` | Show full thread | `GMAIL_FETCH_MESSAGE_BY_THREAD_ID` |
| `delegate [name]` | Forward + add to followups.md | See Delegate Actions |
| `skip` | Leave for later | No-op |
| `rule` | Create a rule based on this message | Trigger /create-rule with prefilled context |
| `todo [description]` | Add to todos.md without remind time | Append to todos.md |
| `followup` | Add sender to followups.md | Append to followups.md |

Multiple actions can be batched in one response: `1: draft, 2: remind monday 9am, 3-6: delete, 7: read, 8: delegate annie`

### Immediate actions (process silently, confirm in batch)

For `read`, `delete`, `archive`, `skip`: process during user's input parse, no confirmation per item. Confirm in batch summary at end:

```
✓ Processed:
  - Marked read: 7
  - Trashed: 3
  - Archived: 2
  - Skipped: 1
```

### Draft actions

For `draft` (or `reply`):

1. Determine voice profile to use:
   - Recipient tagged `[Brand]` in contacts.md → brand voice
   - Otherwise → personal voice
   - Ambiguous → ask

2. Generate all batch drafts in parallel (one tool call per draft) for efficiency.

3. Present batch:
   ```
   📝 DRAFT BATCH ([N] drafts ready)
   
   ─── Draft 1: Reply to Bryan Howell ───
   [Full draft body]
   
   ─── Draft 2: Reply to Joel Barbour ───
   [Full draft body]
   
   ...
   
   [Approve all & send] [Save all as drafts] [Edit individually] [Rewrite #X]
   ```

4. **For Composio-connected inboxes:** "Send" → `GMAIL_REPLY_TO_THREAD` / `OUTLOOK_REPLY_MESSAGE`. Auto-matches sending account to receiving inbox.

5. **For native MCP fallback:** "Send" creates a draft via `GMAIL_CREATE_EMAIL_DRAFT`; user must send manually from Gmail. Prompt label: "Save as Draft" instead of "Send".

6. **Edit tracking:** when user edits before send, compute diff:
   - Tag edit type (tone / wording / structure / sign-off / cc)
   - Append observation to recipient's section in `contacts.md` under "Voice notes"
   - If substantial edit (>10% character change OR sign-off / greeting / structure shift), increment `voice_drift_counter` in `.meta.json`

7. After send: append to followups.md if reply expects a response back. Log to session log.

### Remind actions

For `remind [time]`:

1. Parse time (e.g. "tomorrow 9am", "monday", "in 2 hours")
2. Append to `todos.md`:
   ```
   - [ ] [task description from email subject/summary] — from [sender] — added [today] — due [parsed-time]
   ```
3. Create Google Calendar event (or Outlook Calendar / Apple Reminders depending on user's mirroring config):
   `📬 [Task ID]: [Description]`
4. Schedule reminder delivery via configured channel:
   - Slack channel (`#inbox-reminders` or custom)
   - Slack DM
   - iMessage
5. Per-reminder channel override: `remind tomorrow 9am via imessage` — overrides default for this one
6. Confirm: "✓ T018 created — I'll remind you to [task] tomorrow at 9am via [channel]"

### Standalone remind (outside triage)

User says: "Remind me to [task] at [time]" outside any active triage.

Same flow — parse, append to todos.md, create calendar event, schedule delivery. No email/message context required.

### Unsubscribe actions

For `unsub`, execute per `.meta.json.schedules.unsubscribe_mode`:

#### `auto` (immediate)
For each `unsub` assignment:
1. Fetch full message via `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID`
2. Try List-Unsubscribe header:
   - `mailto:` → send via `GMAIL_SEND_EMAIL`
   - `https://` → execute GET/POST request
3. If no header, scan body for unsubscribe link, attempt direct call (Composio) or open browser
4. If neither works, propose auto-junk rule

Confirm in action summary:
```
✓ Unsubscribed from: [sender1] (one-click), [sender2] (one-click)
⚠ [sender3]: no link found — auto-junk rule queued
```

#### `batch` (end of triage)
Collect all `unsub` assignments. At end of triage, present queue:
```
UNSUBSCRIBE QUEUE — 4 senders

├── [sender1] — List-Unsubscribe header found ✓ (will execute)
├── [sender2] — List-Unsubscribe header found ✓ (will execute)
├── [sender3] — Body link found: [url] — confirm? [Yes / Skip]
└── [sender4] — No link — create auto-junk rule? [Yes / Skip]

[Execute all] [Review each]
```

#### `manual`
Surface mechanism per item; user handles externally.

### Post-unsubscribe

For each successful unsubscribe:
- Create auto-junk rule for sender (sender may still send post-unsub)
- Log to session log under "🔕 Unsubscribed"

### Delegate actions

For `delegate [name]`:

1. Resolve `[name]` to email via contacts.md or `GMAIL_SEARCH_PEOPLE`
2. Forward via `GMAIL_REPLY_TO_THREAD` (forward variant) or `OUTLOOK_FORWARD_MESSAGE`
3. Append to `followups.md`:
   ```
   - [delegated-to-name] — re: [subject] — delegated [today] — waiting [N] days
   ```
4. Confirm: "✓ Forwarded to [name]; tracking in followups.md"

### Rule actions

For `rule`:
1. Trigger `/create-rule` with prefilled context from this message:
   - Suggested trigger: sender or subject pattern
   - Suggested type: based on message category (delete/prioritize/folder/organize)
   - Suggested stakes: per default-by-action
   - Suggested scope: current inbox

2. After rule created, return to triage at next message.

---

## Step 8: Next Batch

After processing actions for the current batch:
1. Confirm batch summary
2. If unread messages remain: "Ready for the next batch?" → repeat Steps 6-7
3. If no more unread: proceed to Step 9

If multi-inbox sequential and current inbox is done: "Move to [next inbox alias]? [Yes / Done]"

---

## Step 9: Triage Complete

After all messages handled across all scoped inboxes:

### Summary

```
✓ Triage complete.

ACROSS [N] INBOXES:
  📬 Processed: [X] emails
  📝 Drafts sent: [Y]
  💾 Drafts saved: [Z]  (fallback mode only)
  ⏰ Reminders set: [W]
  👥 Followups added: [V]
  🗑️ Trashed: [T]
  🔕 Unsubscribed: [U]
  ⚡ Auto-rules applied: [A] silently

[If new rule suggestions queued]:
🆕 [N] new rule suggestions queued in rules-review-queue.md
   Review now? [Yes / Later]

[If voice_drift_counter >= 3]:
🎙️ I noticed [N] substantial edits this session. Want a quick 5-pair
    A/B to recalibrate? (~2 min) [Yes / Skip]

[If rule review / voice review / VIP review is overdue]:
📋 Reminders:
  • Rule review: [N] days overdue
  • Voice profile review: due
```

### Drift-triggered A/B (if applicable)

If `voice_drift_counter >= 3` and user accepts:
1. Generate 5 A/B pairs targeting scenarios that triggered the edits
2. User picks preferred option for each
3. Update voice-profile.md
4. Reset `voice_drift_counter` in `.meta.json`
5. Log: `**HH:MM** — Drift A/B completed: 5 pairs, [N] preferences updated`

### Update workspace files

1. `followups.md` — add anyone the user replied to (via draft) where reply expects response back
2. `todos.md` — add new items from `remind` and `todo` actions
3. `contacts.md` — observations from edit-tracking accumulated during session
4. `.meta.json`:
   - Increment `session_count`
   - Update `last_triage_end`
   - Reset `voice_drift_counter` if A/B fired

### Session log entry

```
**HH:MM** — Session end: [X] emails handled across [N] inboxes, [Y] sent, [Z] drafts, [V] followups added, [W] todos added, [N] rules queued, drift_counter=[X]
```

---

## Quick Triage Mode

Triggered by: "any new emails?", "anything important?", "what did I miss"

Lightweight version:
1. Skip cadence-due checks (don't surface review prompts unless critical)
2. Run VIP cross-inbox scan
3. Show counts only:
   ```
   Quick check across [N] inboxes:
   
   ⭐ VIPs waiting: [N]
   📧 Unread total: [M] ([X] 🔴, [Y] 🟡, [Z] 🗑️)
   💬 Slack: [A] unread
   
   Want me to triage, or just the VIPs?
   ```
4. If user wants to triage, fall through to Step 1.5 of full flow
5. Otherwise, surface only the VIPs with full alert format

---

## Step 10: Post-Triage Actions

If new rule suggestions are queued AND cadence is due (per `.meta.json.schedules.rule_suggestion_cadence`):

```
🆕 [N] rule suggestions ready for review:

  • [low_stakes][per-inbox: uno-mas][delete] Auto-archive Substack newsletters
    Reason: archived 8 from this sender in last 7 days
    [Approve / Modify / Reject]

  • [high_stakes][global][organize] Auto-forward AP invoices to operations@dpp
    Reason: forwarded manually 3 times this week
    [Approve / Modify / Reject]

  ...

[Review all] [Approve all low_stakes] [Skip — review later]
```

For each approved: append to `rules.md` with full structure. Remove from `rules-review-queue.md`. Log to session log.

If voice profile review or VIP list review is due, mention gently:
```
Heads up:
  📅 Voice profile review is due (last reviewed [N] days ago)
  📅 VIP list review is due

Run `/voice-calibration` or "review my VIP list" when you have time.
```

---

## Learned Rule Suggestions (background)

While triage runs, the skill continuously detects patterns and queues suggestions to `rules-review-queue.md` (not surfaced inline unless cadence is due — see Post-Triage Actions).

Patterns to detect (selection — full list in SKILL.md):

**Delete patterns:**
- Same sender junked 3+ times → "Auto-delete from [sender]?"
- Sender's emails never opened (5+ times) → "Auto-delete + unsubscribe?"

**Prioritization patterns:**
- User replies to sender within 1h consistently → "Mark as VIP?"
- Cross-inbox correspondence (same person emails 2+ accounts) → "VIP candidate?"
- Fireflies meeting frequency (3+ in 30d) → "VIP candidate?"

**Organization patterns:**
- Same email type always foldered → "Auto-route to [folder]?"
- Same email type always labeled → "Auto-label as [label]?"

For each detected pattern, append to `rules-review-queue.md`:
```
- [ ] **[stakes][scope][type]** [rule text] — proposed [today] — reasoning: [pattern]
```

Don't propose duplicates — check existing queue first.

---

## Notes for the skill

- **Always confirm before sending** — never auto-send a draft without user approval
- **Always confirm permanent delete** — `GMAIL_BATCH_DELETE_MESSAGES` is irreversible
- **Preserve thread integrity** — always use `GMAIL_REPLY_TO_THREAD` with thread_id for replies
- **Match sending account** — outgoing replies use the inbox the message arrived at
- **Edit tracking is continuous** — capture every diff, write to contacts.md
- **Be decisive on categorization** — if it's junk, call it junk; user can override
- **Keep FYI brief** — single line per item
- **Cross-reference contacts.md before asking** — if the user has notes about a person, use them
- **Log to session-logs/[today].md** continuously — not at end-of-session
- **Update .meta.json incrementally** — don't batch counter increments
- **Honor fallback mode** — if `.meta.json.fallback_mode: true`, route through native Gmail MCP instead of Composio; flag features that are disabled
