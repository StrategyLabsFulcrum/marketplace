# Marketing Analytics

Tracks marketing KPIs and performance metrics across all channels, surfaces insights, and routes structured recommendations back to the agents that act on them. This is the feedback loop that connects execution results to strategy — without it, the system plans and runs campaigns but can't learn from what happens.

**The Marketing Analytics Orchestrator does not manage campaigns or place media buys.** It measures, analyzes, and recommends.

## What It Does

1. Collects performance data from any source — pasted exports, files, or Rube MCP live pulls
2. Spawns four specialist analysts in parallel to evaluate campaign KPIs, channel mix, creative performance, and revenue/ROI
3. Synthesizes cross-analyst findings into prioritized insights
4. Builds a structured output package: full report + three targeted briefs
5. Routes recommendations back to Campaign Strategist, Performance Marketing Agent, Creative Director, and Art Director
6. Maintains the `analytics/benchmarks.md` file — the system's accumulated performance baseline

## Commands

| Command | What It Does |
|---------|-------------|
| `/analytics-report` | Full performance report — all analysts, complete output package |
| `/analytics-brief` | Fast insight brief — current status and optimization actions only |

## Four Specialist Analysts

| Specialist | Owns |
|-----------|------|
| **Campaign Performance Analyst** | KPI scorecard, pacing, trend analysis, anomaly detection |
| **Channel Mix Analyst** | Per-channel efficiency, attribution, budget allocation |
| **Creative Performance Analyst** | Ad fatigue, winning patterns, copy angle scoring |
| **Revenue/ROI Analyst** | CAC, LTV, ROAS, contribution margin, ROI verdict |

## The Feedback Loop

Marketing Analytics is the return path in the system:

```
Campaign Strategist → (plans) → Performance Marketing → (activates) → Results
                                                                          ↓
                     ← Strategic brief ← Marketing Analytics ← Performance data
                                    ↓
                     ← Optimization actions ← → Performance Marketing Agent
                     ← Creative performance brief ← → Creative Director + Art Director
```

Without this loop:
- The Campaign Strategist plans based on assumptions, never learns what worked
- The Performance Marketing Agent optimizes in isolation, without strategic context
- The Creative Director receives no signal on which creative concepts are resonating
- Budget decisions are made on gut, not data

With this loop, every campaign makes the next campaign smarter.

## Output Structure

```
analytics/                             ← project-level (cross-campaign)
├── benchmarks.md                      ← accumulated performance baselines
├── kpi-calendar.md                    ← reporting cadence schedule
├── reports/
│   └── performance-report-{{date}}.md ← full report
└── briefs/
    ├── strategic-brief-{{date}}.md    ← → Campaign Strategist
    ├── optimization-actions-{{date}}.md ← → Performance Marketing Agent
    └── creative-brief-{{date}}.md    ← → Creative Director + Art Director

campaigns/{{slug}}/data/               ← campaign-level data files
├── meta-ads-{{date}}.csv
├── google-ads-{{date}}.csv
├── email-performance-{{date}}.csv
└── notes-{{date}}.md
```

## Data Sources

Works with whatever data is available:

| Method | How |
|--------|-----|
| Pasted exports | Export from platform → paste into conversation → Analytics Orchestrator parses it |
| Files | Drop CSV/exports into `campaigns/{{slug}}/data/` |
| Rube MCP | Configure connections once → automated live pulls |

## Modes

| Mode | Use When |
|------|---------|
| `report` | Full weekly/monthly review — all analysts, complete output |
| `brief` | Quick check-in — Campaign Performance Analyst + action list |
| `audit` | Deep dive on a specific question, channel, or creative |
| `setup` | First time — establishes benchmarks and reporting cadence |

## Plugin Dependencies

- **brand-intelligence-center** (required) — brand context, revenue model, primary KPIs
- **campaign-strategist** (recommended) — reads KPI framework and campaign brief for targets
- **creative-director** (recommended) — routes creative performance briefs
- **art-director** (recommended) — routes visual performance notes
