# Weekly Review

Weekly pipeline performance report — tracks movement, velocity, wins/losses, stale leads, and recommends next week's actions. Suggested cadence: Monday morning, 15-20 minutes.

## Before Starting

1. Load all lead lists from `lead-lists/`.
2. Read discovery settings from `lead-lists/.config/discovery-settings.md` if it exists.
3. Determine the review period (last 7 days from today).

---

## Section 1: Pipeline Movement

Compare current status counts to status counts from 7 days ago (tracked in outreach_notes timestamps):

```
PIPELINE MOVEMENT — [Date Range]

| Status | Last Week | This Week | Change |
|--------|-----------|-----------|--------|
| Not Started | 30 | 22 | -8 (contacted) |
| Drafted | 5 | 3 | -2 (sent) |
| Sent | 6 | 12 | +6 |
| Responded | 1 | 3 | +2 |
| Converted | 0 | 1 | +1 🎉 |
| Declined | 0 | 1 | +1 |
| Stale | 0 | 2 | +2 |
| TOTAL | 42 | 44 | +2 (new leads added) |
```

---

## Section 2: Outreach Activity

Count all outreach actions logged this week:

```
OUTREACH ACTIVITY
├── Messages sent: 8 (5 email, 2 phone, 1 drop-in)
├── Follow-ups sent: 4
├── Responses received: 2
├── Meetings scheduled: 1
├── Meetings completed: 1
├── Drop-in visits: 2
```

---

## Section 3: Wins & Losses

**Wins** — Leads that moved to "responded" or "converted" this week:

```
🟢 THIS WEEK'S WINS
├── Kristina Mattson (Estate Attorney) — Meeting completed, she'll refer
│   estate cleanout and demo work. CONVERTED! 🎉
│   Channel: Email → Phone meeting | Days to convert: 8
│
└── Sandra Teal (ServiceMaster) — Replied "let's grab coffee"
    Channel: LinkedIn message | Days to respond: 4
```

**Losses** — Leads that moved to "declined" or "stale":

```
🔴 THIS WEEK'S LOSSES
├── Pamela Rohr (Attorney) — Replied "not interested at this time"
│   Channel: Email | Touches: 2
│   → Revisit in 6 months? [Yes — set reminder / No — archive]
│
└── Richard Gilleran (Attorney) — No response after 3 touches (30+ days)
    Channel: Phone → Email → Phone
    → Archive or try new angle? [Archive / New Angle / Skip]
```

---

## Section 4: Velocity Metrics

Calculate performance metrics for the review period:

```
VELOCITY METRICS
├── Avg. days from first contact to response: 4.2 days
├── Overall response rate: 25% (5 of 20 contacted)
├── Meeting conversion rate: 60% (3 of 5 responded → meeting)
│
├── BY CHANNEL:
│   ├── Email: 33% response rate (best) — 4 of 12 sent
│   ├── Drop-in: 50% response rate — 1 of 2 (small sample)
│   ├── LinkedIn: 25% response rate — 1 of 4 sent
│   └── Phone: 0% response rate — 0 of 6 calls
│
├── BY LEAD TYPE:
│   ├── Estate Attorneys: 23% response rate — 3 of 13 contacted
│   └── Insurance/Restoration: 17% response rate — 2 of 12 contacted
│
├── BY RELEVANCE:
│   ├── 5-star leads: 35% response rate
│   └── 4-star leads: 12% response rate
```

---

## Section 5: Stale Lead Review

List all leads that have gone stale or are at risk:

```
⚠️ GOING STALE (3)
├── L-010 Pamela Rohr — 4 touches, explicit decline
│   Recommendation: Archive. Set 6-month re-engagement reminder.
│
├── L-011 Richard Gilleran — 3 touches, no response, 32 days
│   Recommendation: Try one final approach — different channel or new angle
│
└── L-022 Steve Knight — 2 touches, no response, 28 days
    Recommendation: Try drop-in. Large operation, may need in-person contact.

Actions: [Archive all stale / Review each / Skip]
```

---

## Section 6: Recommended Actions for Next Week

Based on velocity, pipeline state, and follow-up cadence:

```
RECOMMENDED ACTIONS — NEXT WEEK

PRIORITY OUTREACH (5 leads):
1. L-017 Jason Gray ★★★★★ — Dual Spokane/CdA office, high volume
   Channel: Email | Draft ready? No → generate with /lead-outreach
2. L-018 Kimmer Callahan ★★★★★ — 1 of 5 Board Certified EPLS in Idaho
   Channel: Email | Draft ready? No
3. L-021 Scott Whitaker ★★★★★ — Largest Restoration 1 operator in US
   Channel: Phone | Script ready? No
4. L-035 Gary Valkenaar ★★★★★ — BELFOR GM, enterprise relationship
   Channel: Email | Draft ready? No
5. L-037 Johnny Guinn ★★★★★ — IAS Claims, new Spokane office owner
   Channel: Email | Draft ready? No

FOLLOW-UPS DUE:
├── L-024 Sandra Teal — Coffee meeting pending, confirm date
├── L-005 Holland McBurns — Follow-up #2 due Wednesday
└── L-033 Michael Kilpatrick — Follow-up #1 due Monday

MEETINGS TO SCHEDULE:
└── Sandra Teal — She said "let's grab coffee." Propose a date.

DISCOVERY:
└── Last discovery run: 7 days ago. Run /lead-discovery now? [Yes / Next week]
```

---

## Section 7: Discovery Check

At the end of every weekly review, check discovery status:

- If last discovery was 7+ days ago: **"Discovery is due. Run `/lead-discovery` to find new leads?"**
- If last discovery was < 7 days ago: **"Discovery is current (last run: [date]). [X] new leads found."**
- If no discovery has ever run: **"You haven't run lead discovery yet. Run `/lead-discovery` to grow your list?"**

---

## Save Weekly Report

Save the weekly report to `lead-lists/reports/weekly-[date].md` for historical tracking.

After saving, offer:
- "Regenerate dashboard with latest data? [Yes / No]"
- "Run lead discovery now? [Yes / Later]"
- "Draft outreach for recommended leads? [Yes / I'll do it later]"
