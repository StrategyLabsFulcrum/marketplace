# Inbox Report

Generate and deliver a comprehensive inbox activity report. Runs automatically on the user's configured cadence (monthly by default) or on demand.

Triggers on: "inbox report", "email report", "show my report", "monthly report", "how's my inbox doing", "inbox stats", "email stats", "show my inbox report for [month]", "compare this month to last month"

## Before Starting

0. **Resolve data path:** Check for iCloud sync first: `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/config.md`. If found, use the iCloud path. Otherwise, fall back to `inbox-command-center/` locally.
1. Load config from `[data-path]/config.md` — report cadence, delivery preferences.
2. Load VIP contacts from `[data-path]/vip-contacts.md`.
3. Load rules from `[data-path]/rules.md` and `[data-path]/folder-rules.md`.
4. Check for previous reports in `[data-path]/reports/` for trend comparison.

---

## Step 1: Determine Report Period

### Automatic (scheduled)
When triggered by cadence (monthly/bi-weekly/weekly), the report covers the full period since the last report.

### On Demand
When the user requests a report:

> "What period should this report cover?"
>
> - **This month so far** (default)
> - **Last month** — full previous month
> - **Custom range** — "Show me [date] to [date]"
> - **Compare** — "Compare this month to last month" / "Compare March to January"

---

## Step 2: Gather Data

Pull data from all connected sources for the report period:

### Email Data
Using Gmail MCP (or Rube for Outlook):

1. **Received emails:** Search `in:inbox after:YYYY/MM/DD before:YYYY/MM/DD` — count total
2. **Sent emails:** Search `in:sent after:YYYY/MM/DD before:YYYY/MM/DD` — count total
3. **Deleted emails:** Search `in:trash after:YYYY/MM/DD before:YYYY/MM/DD` — count total
4. **Read but unresponded:** Search for emails in the 🔴 RESPOND category that were marked read but have no sent reply in the thread
5. **Per-sender breakdown:** Group received emails by sender for top senders list
6. **Per-day breakdown:** Count emails per day for volume trends
7. **Response times:** For emails where user replied, calculate time between receipt and reply

### Rule Data
From the triage history and rules.md:
- Count triggers per rule for the period
- Separate manual deletes vs. rule-based deletes vs. folder auto-cleanup deletes
- Track which rules had zero triggers (candidates for cleanup)

### Folder Data
From folder-rules.md and triage history:
- Count emails routed to each folder
- Count auto-actions executed (archive, delete, remind)
- Current email count per folder

### VIP Data
Cross-reference email data with VIP contacts list:
- Per-VIP email volume (received and sent)
- Per-VIP response time
- Active threads with each VIP
- Pending/open items per VIP

### Slack & iMessage Data (if connected)
- Messages triaged, replied to, skipped
- Cross-platform dedup count

---

## Step 3: Generate Report

Build the report using the format defined in SKILL.md → Monthly Inbox Report → Report Content.

Key sections:
1. **Email Volume** — Total received, sent, daily averages, busiest/quietest days
2. **Deletion Breakdown** — Total deleted, manual vs. rule-based vs. folder auto-cleanup, deletion rate, trend vs. last period
3. **Read But Not Responded** — Total, by category (FYI expected vs. flagged RESPOND items missed), response rate, average response time
4. **VIP Communications Summary** — Per-VIP breakdown with received/sent/response time, key threads, open items
5. **Rules Performance** — Auto-processed count, top rules by volume, zero-trigger rules, pending suggestions
6. **Folder Activity** — Per-folder stats
7. **Trends & Insights** — Volume trends, top senders, new senders, busiest time of day, triage efficiency, inbox zero days
8. **Slack & iMessage** — If connected
9. **Actions Due** — Pending rule suggestions, VIP review status, voice profile review status, stale follow-ups

---

## Step 4: Present Report

### Interactive (on demand)
Present the full report in conversation with drill-down options:

```
📊 INBOX REPORT — [Period]

[Full report content per SKILL.md format]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DRILL DOWN:
→ "Show me all VIP details"
→ "Show deletion breakdown by rule"
→ "Show read-but-not-responded list"
→ "Show folder stats"
→ "Compare to [previous period]"
→ "Show top senders"
→ "Show response time trends"
```

### Scheduled Delivery
When auto-generated on cadence:
- **Email delivery:** Format as a clean, readable email with key highlights at the top and full detail below. Send to user's primary email.
- **Slack DM:** Send a condensed version with key numbers and a note: "Full report saved to your inbox report archive."
- **iMessage:** Send a brief summary with top 5 stats: "Your March inbox report: [X] received, [X] sent, [X] deleted ([X]% automated), [X] VIP threads active. Full report in your archive."

---

## Step 5: Save Report

Save the generated report to the user data directory:

```
[data-path]/reports/[YYYY-MM].md
```

For weekly/bi-weekly reports, use: `[YYYY-MM-DD].md`

Update config:
```markdown
## Inbox Report
- Last generated: [date]
- Next due: [date]
```

---

## Step 6: Comparison Mode

When the user asks to compare periods:

```
📊 INBOX COMPARISON — [Period A] vs. [Period B]

                          [Period A]    [Period B]    Change
Emails received:          [X]           [X]           [↑/↓ X%]
Emails sent:              [X]           [X]           [↑/↓ X%]
Emails deleted:           [X]           [X]           [↑/↓ X%]
  Manual deletes:         [X]           [X]           [↑/↓ X%]
  Rule-based deletes:     [X]           [X]           [↑/↓ X%]
Response rate:            [X]%          [X]%          [↑/↓ X%]
Avg response time:        [X]h          [X]h          [↑/↓ X%]
Rules auto-processed:     [X]%          [X]%          [↑/↓ X%]
VIP emails:               [X]           [X]           [↑/↓ X%]
Inbox zero days:          [X]           [X]           [↑/↓ X%]

KEY CHANGES:
├── [Notable trend 1]
├── [Notable trend 2]
└── [Notable trend 3]

RECOMMENDATIONS:
├── [Actionable suggestion based on trends]
└── [Actionable suggestion based on trends]
```

---

## Drill-Down Commands

After presenting a report, the user can drill into specific sections:

| Command | What It Shows |
|---------|--------------|
| "Show VIP details" | Full per-VIP breakdown with thread summaries |
| "Show deletion details" | Every rule that deleted emails, with counts and examples |
| "Show unresponded emails" | List of 🔴 RESPOND emails that were read but never replied to |
| "Show folder stats" | Per-folder activity with auto-action counts |
| "Show top senders" | Top 20 senders by volume with reply rates |
| "Show response times" | Response time distribution by sender type and day of week |
| "Show rule performance" | All rules ranked by trigger count, with zero-trigger cleanup suggestions |
| "Show trends" | Week-over-week charts for volume, response time, and triage efficiency |
