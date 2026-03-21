# /analytics-brief

Generate a fast insight brief and optimization action list without a full report. Runs the Campaign Performance Analyst, synthesizes findings, and outputs what needs to happen next. Faster than `/analytics-report` — optimized for regular check-ins and pre-meeting prep.

## What This Does

1. Loads campaign KPI targets
2. Collects current performance data
3. Runs Campaign Performance Analyst (always) + relevant specialist analysts based on the question
4. Produces: insight brief → Campaign Strategist, optimization actions → Performance Marketing Agent
5. Skips the full report format — focuses on insights and actions only

## When to Use

- Mid-week check-in (not a full weekly report)
- Before a client or stakeholder meeting
- When you have a specific question: "Why is CPL up this week?" or "Should we shift budget?"
- When you need optimization actions for the Performance Marketing Agent quickly

## How to Invoke

**Standard brief — current campaign status and next actions:**
```
/analytics-brief
```

**Brief for a specific campaign:**
```
/analytics-brief 2026-03-spring-launch
```

**Brief focused on a specific question:**
```
/analytics-brief why is CPL rising on Meta this week?
/analytics-brief should we shift budget away from Google?
/analytics-brief is the email sequence performing?
```

**Brief for a specific channel only:**
```
/analytics-brief meta-only
/analytics-brief email-only
```

## Output

Two focused documents:

```
analytics/briefs/strategic-brief-{{date}}.md        → Campaign Strategist
analytics/briefs/optimization-actions-{{date}}.md   → Performance Marketing Agent
```

No full report. No creative brief. Just insights and actions.

## Brief vs. Report — When to Use Which

| Use `/analytics-brief` when... | Use `/analytics-report` when... |
|-------------------------------|--------------------------------|
| You need a quick read on status | It's your weekly or monthly review |
| You have a specific question | You want the complete picture |
| Pre-meeting prep | Post-campaign analysis |
| You only have partial data | You have full data ready |
| You need optimization actions fast | You need the full output package for routing |
