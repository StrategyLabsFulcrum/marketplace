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

4. **Confirm Himalaya connectivity** is alive — for each connected inbox, run `~/.cargo/bin/himalaya envelope list -a <himalaya_alias> --page-size 1 -o json 2>/dev/null`. Non-zero exit or auth-rejected error → surface the specific account to the user (Gmail = app password issue, Outlook = OAuth token issue) and prompt for repair before triage starts.

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

(No fallback mode in v1.5 — every connected inbox uses the same Himalaya path.)

---

## Step 1.5: VIP Cross-Inbox Scan (always runs first when multi-inbox + no scoped inbox)

Before user picks a single inbox, scan ALL connected inboxes for VIP messages.

### Scan logic

```
vip_emails = []
vip_addrs = collect addr field for every contact with [VIP] tag in contacts.md
last_check_date = YYYY-MM-DD from time range parsing

For each inbox in .meta.json.connected_inboxes:
  himalaya_alias = inbox.himalaya_alias

  # Strategy A — for small VIP lists (< ~20): loop per-sender
  For each addr in vip_addrs:
    Bash:
      ~/.cargo/bin/himalaya envelope list \
        -a <himalaya_alias> -f INBOX -o json --page-size 20 \
        -- 'from <addr> and after <last_check_date>' 2>/dev/null
    Parse JSON; keep envelopes where !flags.includes("Seen")

  # Strategy B — for large VIP lists (>= ~20): fetch all unread once, filter client-side
  # (Avoids running 20+ IMAP SEARCH queries against the same INBOX.)
  Bash:
    ~/.cargo/bin/himalaya envelope list \
      -a <himalaya_alias> -f INBOX -o json --page-size 200 \
      -- 'after <last_check_date>' 2>/dev/null
  Parse; keep envelopes where !flags.includes("Seen") AND from.addr in vip_addrs

For each VIP message found:
  - Cross-reference contacts.md for relationship + recent context
  - If a Fireflies transcript with this person exists in last 30d:
       attach "📞 You spoke with [name] [date] ([topic])"
  - Append to vip_emails with inbox alias
```

Run inboxes in parallel — each `himalaya envelope list` is independent, so multiple `Bash` tool calls can fire concurrently in one assistant turn.

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

Per the selected inbox(es), execute two parallel Himalaya envelope fetches via the `Bash` tool. Both fetches per inbox are independent so issue them in one assistant turn (multiple Bash tool calls).

### Email — Himalaya fetch (per inbox)

For each scoped inbox, fetch starred-unread + unread-inbox:

```
[For Gmail account]
Fetch A — Starred (read from Gmail's [Gmail]/Starred IMAP folder):
  Bash: ~/.cargo/bin/himalaya envelope list \
          -a <himalaya_alias> -f "[Gmail]/Starred" -o json --page-size 20 \
          2>/dev/null
  Parse JSON; keep envelopes where !flags.includes("Seen")

Fetch B — Unread INBOX since last check:
  Bash: ~/.cargo/bin/himalaya envelope list \
          -a <himalaya_alias> -f INBOX -o json --page-size 50 \
          -- 'after <YYYY-MM-DD>' 2>/dev/null
  Parse JSON; keep envelopes where !flags.includes("Seen")

[For Outlook account]
Fetch A — Starred:
  Bash: ~/.cargo/bin/himalaya envelope list \
          -a outlook -f INBOX -o json --page-size 50 \
          -- 'after <YYYY-MM-DD>' 2>/dev/null
  Parse JSON; keep envelopes where flags.includes("Flagged") AND !flags.includes("Seen")
  (Outlook doesn't expose a dedicated "Starred" folder via IMAP — filter the \Flagged
   flag client-side.)

Fetch B — Unread INBOX since last check:
  Same Bash as above; keep envelopes where !flags.includes("Seen")
  (Strategy: one fetch covers both flag and unread filters.)
```

**Deduplicate by envelope `id`** within each inbox (Fetch A + Fetch B may overlap on starred-unread items in Gmail; for Outlook it's the same fetch).

Sort: starred first → most recent → oldest.

**Tag each envelope with its inbox alias** (used in Step 6 batch presentation): append `inbox_alias: "<alias>"` to each parsed envelope object before passing downstream.

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

(WhatsApp / Teams / other messaging platforms are not currently in scope for the Himalaya-based architecture — they'd be added later as separate MCP servers if/when needed.)

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

For each rule with `Type: folder`, dispatch via a single Himalaya `message move` (same call shape for Gmail and Outlook — both are IMAP folders):

```
~/.cargo/bin/himalaya message move \
  -a <himalaya_alias> -f INBOX <envelope.id> "ICC/<FolderName>" 2>/dev/null
```

Multiple messages routed to the same folder in one batch: issue one `message move` per envelope (Himalaya doesn't have a batch-move). For typical triage volumes (10s of messages per rule) this is fine; for hundreds, consider running them as parallel `Bash` calls.

**Auto-provision missing folders.** Before the first move into a logical folder, check that it exists:

```
~/.cargo/bin/himalaya folder list -a <himalaya_alias> -o json 2>/dev/null
```

If `ICC/<FolderName>` is not in the result, create it:

```
~/.cargo/bin/himalaya folder add -a <himalaya_alias> "ICC/<FolderName>" 2>/dev/null
```

Then update `.meta.json.connected_inboxes[i].folders_enabled[]` to include the folder.

If a global rule references a folder not enabled in some inbox, auto-enable + route silently.

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
| `reply` | Same as draft + send on confirmation | Assemble RFC-822 with `In-Reply-To` + `References` → `himalaya message send -a <alias> < /tmp/reply.eml 2>/dev/null` |
| `remind [time]` | Add to todos.md + calendar event | See Remind Actions |
| `read` | Mark as read | `himalaya flag add -a <alias> -f INBOX <ID> seen 2>/dev/null` |
| `delete` | Move to trash (recoverable) | Gmail: `himalaya message move -a <alias> -f INBOX <ID> "[Gmail]/Trash" 2>/dev/null` • Outlook: `himalaya message move -a outlook -f INBOX <ID> "Deleted Items" 2>/dev/null` |
| `archive` | Remove from INBOX | Gmail: `himalaya message move -a <alias> -f INBOX <ID> "[Gmail]/All Mail" 2>/dev/null` • Outlook: `himalaya message move -a outlook -f INBOX <ID> Archive 2>/dev/null` |
| `unsub` | Execute unsubscribe | See Unsubscribe Actions |
| `dive` | Show full thread | `himalaya message thread -a <alias> -f INBOX <ID> -o json 2>/dev/null` |
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

4. **Send:** assemble the reply as an RFC-822 message body in a temp file (e.g. `/tmp/reply-<id>.eml`) with `In-Reply-To: <original-message-id>` and `References: <original-references-chain>` headers — these preserve threading on both Gmail and Outlook. Then:

   ```
   ~/.cargo/bin/himalaya message send -a <himalaya_alias> < /tmp/reply-<id>.eml 2>/dev/null
   ```

   Sending account = receiving inbox (per the inbox alias the message came from).

5. **Save as draft (instead of sending):**

   ```
   ~/.cargo/bin/himalaya message save -a <himalaya_alias> -f "[Gmail]/Drafts" < /tmp/reply-<id>.eml 2>/dev/null
   ```

   For Outlook, the drafts folder is typically `Drafts` (no `[Gmail]/` prefix).

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
1. Fetch full message via `~/.cargo/bin/himalaya message read -a <alias> -f INBOX <ID> -o json 2>/dev/null`
2. Parse the `List-Unsubscribe` header from the returned headers map:
   - `mailto:<addr>` → write an empty message addressed to `<addr>` to `/tmp/unsub.eml` and `himalaya message send -a <alias> < /tmp/unsub.eml 2>/dev/null`
   - `https://<url>` → `curl -sSL -X POST <url>` via Bash (some senders require POST; fall back to GET if 405)
3. If no header, scan body for unsubscribe link. Attempt `curl` against extracted URL; otherwise surface URL to user to open in browser.
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

1. Resolve `[name]` to email via `contacts.md` (no people-search fallback; if not found, ask user for the address)
2. Assemble a forward message: fetch the original via `himalaya message read -a <alias> -f INBOX <ID> -o json 2>/dev/null`, prefix `Fwd: ` to the subject, embed the original body (with optional inline commentary), set `To: <delegate-addr>`. Write to `/tmp/fwd-<id>.eml` then `himalaya message send -a <alias> < /tmp/fwd-<id>.eml 2>/dev/null`.
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
  💾 Drafts saved: [Z]
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
- **Always confirm permanent delete** — `himalaya message delete` flips `\Deleted` and expunges; moving to Trash is the safe default
- **Preserve thread integrity** — assemble replies with `In-Reply-To` + `References` headers from the original message; never send a bare reply
- **Match sending account** — outgoing replies use the inbox the message arrived at (`himalaya_alias`)
- **Edit tracking is continuous** — capture every diff, write to contacts.md
- **Be decisive on categorization** — if it's junk, call it junk; user can override
- **Keep FYI brief** — single line per item
- **Cross-reference contacts.md before asking** — if the user has notes about a person, use them
- **Log to session-logs/[today].md** continuously — not at end-of-session
- **Update .meta.json incrementally** — don't batch counter increments
- **Always suppress stderr on Himalaya calls** — `2>/dev/null` is required for clean JSON parsing
