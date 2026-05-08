# Inbox Report

Generate and deliver a comprehensive inbox activity report. Runs automatically on the user's configured cadence (monthly by default) or on demand.

In v1.4, reports are **single-file with two layers**:
- **Cross-inbox section** — unified entities (VIPs, voice profile, Fireflies meetings, global rules)
- **Per-inbox sections** — one block per `connected_inboxes` entry

Source data comes primarily from `session-logs/YYYY-MM-DD.md` files in the report period, supplemented by current-state queries.

## Before Starting

1. **Read** `.meta.json` for `connected_inboxes`, `last_inbox_report`, `schedules.inbox_report_cadence`
2. **Read** `contacts.md` for VIP list
3. **Read** `rules.md` for active rules and their trigger counts
4. **List session logs** in `session-logs/` for the report period

## Step 1: Determine Report Period

### Automatic (scheduled)

If invoked by cadence-due automation:
- Period = since `last_inbox_report` to today (typically 1 month for monthly cadence)

### On Demand

User says: "show inbox report" / "generate inbox report" / "monthly report" / "inbox stats" / "compare this month to last"

Ask:
```
What period?
  [ ] This month
  [ ] Last month (default for "monthly report")
  [ ] Last 30 days
  [ ] Custom range — specify start and end
  [ ] Compare two periods
```

For comparison mode, see Step 6.

## Step 2: Gather Data

### Primary feed: session logs

Read every `session-logs/YYYY-MM-DD.md` file within the period. Parse:

```
For each line in session log:
  Match patterns:
    "Triaged [N] emails" → email volume per inbox
    "Sent [draft/reply] to [X]" → sent counter
    "Auto-rules applied: archived [N]..." → rule trigger counts
    "Trashed: [N]" → manual trash counter
    "Permanently deleted [N]" → perma-delete counter
    "Unsubscribed from [X]" → unsubscribe counter
    "Marked read: [N]" → read counter
    "VIP scan: [N] surfaced" → VIP traffic
    "User edited [file]" → workspace edit log
    "Drift A/B completed" → voice review activity
    "Rule created/edited/deleted" → rule mgmt activity
    "Fireflies pull: [N] transcripts" → Fireflies activity
```

This gives most of the report data without re-querying email APIs.

### Supplementary: current-state queries

Some metrics require live queries:

#### Email volume / current state (per inbox)

```
For each inbox in connected_inboxes:
  Composio: GMAIL_FETCH_EMAILS / OUTLOOK_FETCH_MESSAGES
  query: "after:[period_start] before:[period_end]"
  max_results: paginated as needed
  
Compute: total received, unread remaining, by-day distribution
```

For sent volume:
```
  query: "from:me after:[period_start] before:[period_end]"
```

#### Folder counts

```
For each enabled folder per inbox:
  Composio: GMAIL_FETCH_EMAILS with label filter
  Compute: current count, items added in period, auto-actions executed
```

### Rule data

From `rules.md`, sum each rule's `Times triggered` field. Compare against pre-period snapshot (saved as `.meta.json.rule_triggers_snapshot`) to compute period-over-period.

### VIP data

From session logs + Composio queries:
- VIP emails received (per VIP, per inbox)
- VIP emails sent (per VIP)
- Average response time per VIP
- Open VIP threads
- Notable VIPs (silent, new candidates)

### Fireflies data

```
mcp__claude_ai_Fireflies__fireflies_get_transcripts
date_range: period
```

Compute:
- Total meetings analyzed
- Meetings with VIPs (cross-reference contacts.md)
- New transcripts feeding contacts.md notes (count of contacts.md updates from session logs)
- New VIP candidates from meetings (sum of "VIP candidate" events)

### Voice profile data

From session logs + `.meta.json`:
- Drift events count
- Mini A/B fires
- Mandatory review status (completed / due)

### Slack & iMessage (if connected)

From session logs:
- Total Slack items triaged
- Total iMessages triaged
- Replies sent per channel

## Step 3: Generate Report

Write to memory (or directly to file) using the structured format. Report has 4 main sections plus a header.

```
📊 INBOX COMMAND CENTER REPORT — [Period]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CROSS-INBOX (unified entities)

⭐ VIP COMMUNICATIONS
├── Total received: [N]    Total sent: [M]
├── Avg response time: [X]h
├── Per-VIP breakdown:
│   ├── Bryan Howell — Recv: [X] | Sent: [Y] | Avg: [Z]h | Inboxes: [list]
│   ├── Joel Barbour — Recv: [X] | Sent: [Y] | Avg: [Z]h | Inboxes: [list]
│   └── Annie Brophy — Recv: [X] | Sent: [Y] | Avg: [Z]h | Inboxes: [list]
├── VIP threads still open: [N]
│   ├── [Name] — [Subject] — awaiting [your reply / their reply]
│   └── ...
├── Notable:
│   • Silent VIPs (no contact this period): [list]
│   • New VIP candidates suggested: [N] (in rules-review-queue.md)
│   • [Any other notable VIP patterns]

🎙️ VOICE PROFILE
├── Drift events this period: [N]
├── Mini A/B fires: [N]
├── Mandatory review: [completed YYYY-MM-DD / due]
├── Top edit dimensions: [tone (X), sign-off (Y), structure (Z)]
├── Voice profile last updated: [date]

📞 FIREFLIES INGESTED
├── Total meetings analyzed: [N]
├── Meetings with VIPs: [M]
├── New transcripts feeding contacts.md: [N] entries updated
├── New VIP candidates from meetings: [N]
├── Top recurring topics: [list, if surface-able]

⚡ GLOBAL RULES PERFORMANCE
├── Total triggers: [N]
├── Top global rules:
│   ├── [Rule name] — triggered [X] times
│   ├── [Rule name] — triggered [X] times
│   └── [Rule name] — triggered [X] times
├── Zero-trigger global rules: [list — candidates for cleanup]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PER-INBOX

── personal (ramsey@strategylabs.us) ──
  📧 Volume: [N] received, [M] sent
  ├── Daily average: [X] received, [Y] sent
  ├── Busiest day: [Day, Date] ([Z] emails)
  └── Quietest day: [Day, Date] ([Z] emails)
  
  🗑️ Deletions: [X] manual / [Y] rule-based / [Z] folder cleanup
  ├── Trashed: [T]    Permanently deleted: [P]
  ├── Top deletion rules: [list with counts]
  └── Unsubscribe + delete: [U]
  
  📖 Read but unanswered (RESPOND): [N] flagged
  ├── [Sender] — [Subject] — [N] days ago
  ├── [Sender] — [Subject] — [N] days ago
  └── ...
  
  📂 Folder activity:
  ├── Newsletters: [X] received, [Y] read, [Z] auto-deleted
  ├── Receipts: [X] received, kept
  ├── Low Priority: [X] received, [Y] auto-archived
  └── [other enabled folders]
  
  ⚡ Per-inbox rules:
  ├── Total triggers: [N]
  ├── Top rules: [list]
  └── Zero-trigger rules: [list]
  
  📈 Inbox zero days: [X] of [Y] business days
  📈 Avg triage session: [N] minutes, [M] messages

── uno-mas (ramsey@unomastacos.com) ──
  [same structure]

── ms365 (ramsey@...) ──
  [same structure]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CROSS-PLATFORM SUMMARY

💬 Slack: [N] items triaged, [Y] replied, [Z] skipped
💬 iMessage: [N] items triaged, [Y] replied, [Z] skipped
🔄 Cross-platform dedup: [X] items merged across channels

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRENDS (vs. previous period)

📈 Volume vs. last period: [+/-X%] received, [+/-Y%] sent
📈 Response time vs. last: [+/-X%] (avg [Z]h)
📈 Triage efficiency: [X]% auto-handled by rules ([+/-Y%] vs. last)
📈 Top 5 senders by volume: [list]
📈 Top 5 senders you reply to most: [list]
📈 New senders this period: [N] ([X] became repeat)
📈 Busiest time of day: [hour range]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACTIONS DUE

├── Pending rule suggestions: [N] — [Review now]
├── VIP list review: [due / not due]
├── Voice profile review: [due / not due]
├── Stale follow-ups: [N] > 7 days (in followups.md)
└── Workspace edits this period: [N] hand-edits detected
```

## Step 4: Present Report

### Interactive (on demand)

Present the report in chat. Offer drill-downs:

```
[full report rendered above]

Drill down on any section?

  [ ] Show all VIP threads in detail
  [ ] Show all flagged unanswered RESPOND items
  [ ] Show rule performance with trigger history
  [ ] Compare to previous period
  [ ] Save report to file (auto-saved already)
  [ ] Done
```

### Scheduled delivery

If invoked automatically on cadence:
1. Generate report
2. Save to `~/Inbox Command Center/reports/[YYYY-MM].md`
3. Deliver via channel(s) per `.meta.json.schedules.inbox_report_delivery`:
   - **Email** — formatted email body sent to user's primary inbox
   - **Slack DM** — posted as a thread with key highlights + link to full report file
   - **iMessage** — short summary with key numbers + "Full report at: [path]"
   - **Multiple** — deliver via all configured

## Step 5: Save Report

Always save to `~/Inbox Command Center/reports/[YYYY-MM].md` (or `[YYYY-MM-DD]_to_[YYYY-MM-DD].md` for custom periods).

Update `.meta.json`:
- `last_inbox_report` = today
- `next_inbox_report_due` = today + cadence
- `rule_triggers_snapshot` = current trigger counts (for next period's delta)

Log to session log:
```
**HH:MM** — Inbox report generated for [period], saved to reports/[filename]
```

## Step 6: Comparison Mode

If user requests comparison:

```
Compare which two periods?
  [ ] This month vs. last month
  [ ] This week vs. last week
  [ ] Custom — specify both periods
```

Generate both reports (in memory). Present side-by-side or interleaved comparison:

```
📊 PERIOD COMPARISON

[Period A] vs. [Period B]

CROSS-INBOX
  VIP emails received:    [A] vs [B]    [+/-X%]
  VIP avg response time:  [A]h vs [B]h  [+/-X%]
  Voice drift events:     [A] vs [B]    [+/-X%]
  Fireflies meetings:     [A] vs [B]    [+/-X%]
  Global rule triggers:   [A] vs [B]    [+/-X%]

PER-INBOX (personal)
  Received:               [A] vs [B]    [+/-X%]
  Sent:                   [A] vs [B]    [+/-X%]
  Inbox zero days:        [A] vs [B]    [+/-X]
  Triage efficiency:      [A]% vs [B]%  [+/-X pts]
  ...

[Repeat per inbox]

NOTABLE CHANGES:
  • [Auto-detected significant deltas, e.g.:]
  • Volume up 23% in personal — new newsletters?
  • Response time worsened from 4h to 7h — investigate?
  • Inbox zero days dropped from 18 to 11 — what changed?
```

## Drill-Down Commands

These can be requested mid-report or as standalone:

| Command | What it shows |
|---|---|
| "show VIP detail" | Full thread list per VIP for the period |
| "show flagged unanswered" | All RESPOND items not yet replied to |
| "show rule performance" | Detailed trigger history per rule with timestamps |
| "show folder digest" | Per-folder weekly digests for the period |
| "show silent senders" | Senders who emailed in previous periods but went silent |
| "show new VIP candidates" | Auto-suggested VIPs from response patterns + Fireflies frequency |
| "show triage efficiency" | Auto-rule % over time, time-per-session trends |

---

## Notes for the skill

- **Source from session logs first** — they're cheap to read and don't hit Composio rate limits. Live queries supplement.
- **Cache rule trigger snapshots** in `.meta.json.rule_triggers_snapshot` so deltas work next period
- **Don't double-count** — same email surfacing in cross-inbox VIP section AND per-inbox section is fine; just be consistent across reports
- **Keep cross-inbox section unified** — VIPs, voice, Fireflies, global rules — these are properties of the user, not the inbox
- **Per-inbox sections mirror each other in structure** — easier to scan when consistent
- **Trend detection should highlight 1-2 standout deltas** — don't bury surprising changes in long lists
- **Reports are markdown** — let the user open in Finder, fork, share, etc.
- **Always save before delivering** — even if delivery fails, the file is on disk
