# Monthly Report

Comprehensive monthly pipeline analysis with conversion metrics, channel performance, strategy recommendations, and quarterly audit triggers. Suggested cadence: first Monday of each month, 30 minutes.

## Before Starting

1. Load all lead lists from `lead-lists/`.
2. Load all weekly reports from `lead-lists/reports/` for the month.
3. Load discovery log from `lead-lists/.config/discovery-log.md`.
4. Load connections config from `lead-lists/.config/connections.md`.
5. Determine if this is a quarterly boundary (every 3rd month triggers the full audit).

---

## Section 1: Funnel Visualization

Build the full pipeline funnel with counts and percentages:

```
[MONTH] [YEAR] — PIPELINE REPORT

FUNNEL:
Not Started (22) ──→ Drafted (3) ──→ Sent (25) ──→ Responded (8) ──→ Converted (3)
       46%              6%              52%             17%              6%
                                                          ↘ Declined (2) 4%
                                           ↘ Stale (5) 10%

TOTAL: 48 leads | ACTIVE PIPELINE: 36 | CLOSED: 10 | UNTOUCHED: 22
```

---

## Section 2: Conversion Metrics

```
CONVERSION METRICS — [Month]
├── Total leads in pipeline: 48
├── Outreach sent: 25 (52% of list contacted)
├── Response rate: 32% (8 of 25 sent)
├── Meeting rate: 20% (5 of 25 sent)
├── Conversion rate: 12% (3 of 25 sent)
├── Average days to response: 4.8 days
├── Average days to conversion: 14 days
├── Average deal value from converted: $[X] (if tracked)
├── Estimated pipeline value: $[X] (responded leads × avg deal value)
```

---

## Section 3: Performance by Lead Type

For each lead type in the pipeline:

```
BY LEAD TYPE:

ESTATE/PROBATE ATTORNEYS (24 leads)
├── Contacted: 15 (63%)
├── Response rate: 27% (4 of 15)
├── Conversion rate: 13% (2 of 15)
├── Best performer: Kristina Mattson → active referral partner
├── Avg. days to response: 3.5 days
├── Best channel: Email (35% response rate)
├── Insight: Elder law attorneys respond at 2x the rate of general estate planners
├── Recommendation: Prioritize elder law and probate-focused firms

INSURANCE/RESTORATION (24 leads)
├── Contacted: 10 (42%)
├── Response rate: 20% (2 of 10)
├── Conversion rate: 10% (1 of 10)
├── Best performer: Sandra Teal → coffee meeting, referral pending
├── Avg. days to response: 6.2 days (slower than attorneys)
├── Best channel: Phone (25%) + Drop-in (50%)
├── Insight: Restoration company owners respond better to phone and in-person
├── Recommendation: Shift from email-first to phone-first for this segment
```

---

## Section 4: Channel Performance

```
BY CHANNEL:

| Channel | Sent | Responses | Rate | Meetings | Conversions | Insight |
|---------|------|-----------|------|----------|-------------|---------|
| Email | 15 | 5 | 33% | 3 | 2 | Highest volume, solid rate |
| Phone | 8 | 1 | 13% | 1 | 0 | Low response, but high meeting conversion when connected |
| LinkedIn | 4 | 1 | 25% | 1 | 1 | Small sample, good for BDMs |
| Drop-in | 4 | 2 | 50% | 2 | 1 | HIGHEST rate — Jared showing up in person wins |
| SMS | 2 | 0 | 0% | 0 | 0 | Not effective for cold outreach |

TOP INSIGHT: Drop-in visits convert at 50% — the highest rate by far.
When Jared shows up in person, people respond. Increase drop-in visits.

RECOMMENDATION:
├── Primary: Email for attorneys (33% response)
├── Primary: Drop-in + Phone for restoration (50% + 25% in-person)
├── Secondary: LinkedIn for business development contacts
├── Deprioritize: SMS for cold outreach
```

---

## Section 5: Discovery Summary

```
DISCOVERY — [Month]
├── Discovery runs: 4 (weekly cadence maintained)
├── New leads found: 12
├── New leads added: 9
├── Skipped (duplicates): 3
├── List growth: 40 → 48 (+20%)
│
├── Sources that produced leads:
│   ├── Google Maps (new businesses): 4 leads
│   ├── Firm website team page updates: 3 leads
│   ├── WA State Bar new admissions: 1 lead
│   └── Referral from converted lead: 1 lead
│
├── List saturation:
│   ├── Estate Attorneys: ~85% of known firms covered (near saturation)
│   └── Insurance/Restoration: ~65% of known companies covered (room to grow)
```

---

## Section 6: Strategy Recommendations

Based on all data, generate actionable recommendations:

```
STRATEGY RECOMMENDATIONS — [Next Month]

1. DOUBLE DOWN: Drop-in visits
   Why: 50% response rate — highest of any channel
   Action: Plan 3-4 drop-ins per week, cluster around estimate locations
   Target: Attorneys downtown Spokane, restoration companies in Spokane Valley

2. SHIFT: Restoration outreach from email to phone + drop-in
   Why: 13% email response vs. 50% in-person for this segment
   Action: Lead with phone call, follow up with drop-in if no answer

3. EXPAND: Add new lead type — Title Companies
   Why: Estate attorneys are near saturation (85%). Title companies
   are a natural adjacent referral source for demolition.
   Action: Research 10-15 title companies in Spokane + CdA

4. DEEPEN: Add second contacts at high-value firms
   Why: 8 firms only have one contact. Adding a second increases
   touch surface and reduces single-point-of-failure risk.
   Action: Research additional contacts at 5-star firms

5. RE-ENGAGE: Stale leads with seasonal angle
   Why: 5 stale leads from initial outreach. Spring demo season is
   the perfect re-engagement hook.
   Action: New outreach angle: "Spring demo season is here — we're
   booking out. Wanted to reconnect."

6. TRACK ROI: Start logging job values from referrals
   Why: 3 converted leads but no revenue data yet. Need this for
   quarterly ROI analysis.
   Action: When a referred job comes in, log the value in lead notes.
```

---

## Section 7: Quarterly Audit (every 3rd month)

If this is a quarterly boundary (Month 3, 6, 9, 12), append the full audit:

### ROI Analysis

```
QUARTERLY ROI — Q[X] [Year]

INVESTMENT:
├── Time invested: ~2 hours/week × 12 weeks = 24 hours
├── Ad spend on lead gen: $0 (organic research)
├── Tools: $0 (no paid tools used)
├── Total investment: 24 hours of time

RETURNS:
├── Total leads generated: 63
├── Converted to active referral partners: 4
├── Jobs received from lead referrals: 7
├── Revenue from referred jobs: $47,500
├── Revenue per hour invested: $1,979/hr
├── Cost per converted lead: ~6 hours
├── Estimated annual value of 4 partners: $150K-$200K
```

### Win/Loss Analysis

```
WIN PATTERNS:
├── Lead type: Elder law attorneys convert at 3x the rate of general estate
├── Channel: Drop-in → Email follow-up is the winning sequence
├── Timing: Leads contacted within 48 hours of discovery convert 2x faster
├── Trait: Firm owners/founders convert. Associates rarely do.

LOSS PATTERNS:
├── Phone-only outreach to restoration companies — 0% conversion
├── Large franchise operations (BELFOR, national SERVPRO) — slow/no response
├── Leads over 30 miles away — lower engagement than local
```

### List Health

```
LIST HEALTH:
├── Total leads: 63
├── Contacted: 45 (71%)
├── Active pipeline: 12 (19% — healthy)
├── Converted: 4 (6%)
├── Declined/Stale: 8 (13%)
├── Untouched: 18 (29%)
├── List age: 90 days
├── Freshness: 80% of leads verified within 30 days
```

### Expansion Planning

```
EXPANSION RECOMMENDATIONS:
├── 1. New lead type: Title Companies (natural adjacency)
├── 2. New lead type: Home Inspectors (see demo needs during inspections)
├── 3. New lead type: Bankruptcy Trustees (property liquidation)
├── 4. Geographic expansion: 60-mile radius adds Pullman, Moscow, Sandpoint
├── 5. Referral chain: Ask 4 converted partners for 2-3 introductions each
├── 6. Re-engage declined: 3 of 8 worth retrying with spring demo season angle
```

---

## Save Report

Save to `lead-lists/reports/monthly-[month]-[year].md` (or `quarterly-Q[X]-[year].md` for quarterly reports).

Offer:
- "Regenerate dashboard? [Yes / No]"
- "Run discovery? [Yes / Later]"
- "Draft outreach for recommended leads? [Yes / Later]"
- "Export updated CRM file? [Yes / No]"
