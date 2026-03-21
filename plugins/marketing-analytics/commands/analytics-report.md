# /analytics-report

Run a full marketing performance report. Spawns all four specialist analysts in parallel, synthesizes findings, and produces a complete output package: performance report, strategic insight brief, optimization action list, and creative performance brief.

## What This Does

1. Loads campaign KPI targets and strategic context
2. Collects performance data (pasted, from files, or via Rube)
3. Spawns all needed specialist analysts simultaneously
4. Synthesizes cross-channel, cross-analyst insights
5. Produces the full output package
6. Routes briefs to Campaign Strategist, Performance Marketing Agent, and Creative Director

## When to Use

- Weekly performance review
- Monthly campaign analysis
- End-of-campaign post-mortem
- Before a budget review or strategy conversation

## How to Invoke

**Full report — all active campaigns, last 30 days:**
```
/analytics-report
```

**Specific campaign:**
```
/analytics-report 2026-03-spring-launch
```

**Specific date range:**
```
/analytics-report last-7-days
/analytics-report 2026-03-01 to 2026-03-21
```

**Specific channels only:**
```
/analytics-report channels: meta, email
```

## What You'll Need

Have at least one of these ready:
- Exported data pasted from your ad platforms (Meta Ads Manager, Google Ads, Klaviyo, GA4)
- CSV exports dropped into `campaigns/{{slug}}/data/`
- Rube connections configured for live pulls

The more complete the data, the more complete the report. The Analytics Orchestrator will work with whatever you have and clearly note any gaps.

## Output

All documents saved automatically:

```
analytics/reports/performance-report-{{date}}.md
analytics/briefs/strategic-brief-{{date}}.md        → Campaign Strategist
analytics/briefs/optimization-actions-{{date}}.md   → Performance Marketing Agent
analytics/briefs/creative-brief-{{date}}.md         → Creative Director + Art Director
analytics/benchmarks.md                             → updated with new actuals
```
