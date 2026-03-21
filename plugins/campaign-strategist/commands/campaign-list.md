# /campaign-list

List all campaigns in the `campaigns/` directory with their status, type, dates, and budget.

## What This Does

Reads all campaign folders and displays a summary table:

| Campaign | Type | Status | Dates | Budget |
|---------|------|--------|-------|--------|
| 2026-03-spring-acquisition | Acquisition | Active | Mar 15 – Apr 30 | $18,000 |
| 2026-04-product-launch | Launch | Planned | Apr 1 – Apr 30 | $25,000 |

## How to Invoke

```
/campaign-list
```

## Status Values

- **Draft** — Brief in progress, not yet approved
- **Approved** — Brief approved, waiting on creative/setup
- **Active** — Campaign is live
- **Paused** — Temporarily stopped
- **Complete** — Campaign finished
