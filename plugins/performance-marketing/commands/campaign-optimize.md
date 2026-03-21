# /campaign-optimize

Execute optimization actions from the Marketing Analytics Orchestrator on live campaigns. Takes the optimization action list and produces precise execution steps — or runs them directly via Rube if configured.

## What This Does

1. Reads the optimization action list from `analytics/briefs/optimization-actions-{{date}}.md`
2. Reviews each action — validates it against current campaign structure
3. Groups actions by platform for efficient execution
4. Executes or documents each action
5. Logs every change to the optimization log
6. Flags any actions that conflict with campaign structure or require human judgment

## How to Invoke

**Standard optimize — reads most recent optimization actions brief:**
```
/campaign-optimize
```

**From a specific analytics brief:**
```
/campaign-optimize analytics/briefs/optimization-actions-2026-03-21.md
```

**For a specific campaign:**
```
/campaign-optimize 2026-03-spring-launch
```

**Single action — describe the change directly:**
```
/campaign-optimize pause the underperforming Meta ad sets
/campaign-optimize shift $500 from Google Display to Meta
/campaign-optimize increase Meta budget by 20%
```

## What Gets Produced

**Execution documents** (when manual execution is needed):
- Step-by-step instructions per platform with every setting to change
- Organized by platform so all Meta changes can be done in one session

**Via Rube MCP** (when configured):
- Direct API execution
- Confirmation of changes with before/after values

**Optimization log entry** (always):
- Every change logged to `campaigns/{{slug}}/activation/optimization-log.md`
- Includes: what changed, why, before/after values, expected impact

## Do Not Touch List

The optimize command will also flag creative and ad sets that are performing well and should not be touched. Interference with well-performing campaigns is one of the most common performance marketing errors.

## When to Use

- After receiving an optimization action list from `/analytics-brief` or `/analytics-report`
- When a specific platform issue needs to be addressed (creative fatigue, budget pacing, audience exhaustion)
- Before a budget review — document all optimizations made since last report
- Weekly as part of the regular campaign management cycle
