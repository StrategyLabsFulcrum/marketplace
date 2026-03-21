# /analytics-setup

Connect marketing data sources, audit historical performance, and establish the benchmarks that every agent in the system uses as their baseline. Run this once after brand setup and refresh quarterly.

## How to Invoke

**Full first-time setup:**
```
/analytics-setup
```

**Add a new data source:**
```
/analytics-setup connect klaviyo
/analytics-setup connect google-ads
```

**Quarterly refresh:**
```
/analytics-setup audit
```

**Update benchmarks only:**
```
/analytics-setup benchmark-update
```

**Quick tracking health check:**
```
/analytics-setup health-check
```

## What Happens

1. **Inventory** — Identify which platforms are active and confirm access
2. **Export guide** — Step-by-step instructions to export data from each platform
3. **Audit** — Analyze paid media, website/funnel, email, and revenue performance
4. **Benchmarks** — Establish baseline metrics for all active channels
5. **Data health** — Identify tracking gaps, attribution issues, and fixes needed

## What You Get

- `brand-intelligence-center/analytics/audit-[date].md` — Full historical audit
- `brand-intelligence-center/analytics/benchmarks.md` — Baseline metrics for all channels
- `brand-intelligence-center/analytics/data-health.md` — Tracking fixes priority list

## Agents Unlocked After Setup

Once benchmarks are established, these agents operate with full context:
- **Marketing Analytics** — has a baseline to compare performance against
- **Performance Marketing** — uses historical ROAS and CPAs for media planning
- **CRO Orchestrator** — has baseline CVR and funnel metrics to optimize from
- **Campaign Strategist** — uses historical channel performance for budget allocation
