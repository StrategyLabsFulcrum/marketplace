# /cro-audit

Run a full CRO audit of the marketing funnel — identify friction points, map drop-off by stage, and produce a prioritized hypothesis backlog for A/B testing.

## How to Invoke

**Full funnel audit from a campaign:**
```
/cro-audit campaigns/2026-03-spring-launch/brief.md
```

**Audit with analytics data:**
```
/cro-audit [paste GA4 funnel data or provide file path]
```

**Audit a specific page:**
```
/cro-audit landing page only — [page URL or description]
/cro-audit product pages
/cro-audit checkout flow
```

**Heuristic audit (no data required):**
```
/cro-audit heuristic — describe the funnel and I'll apply best practices analysis
```

## What You Get

- Funnel map with drop-off rates at each stage (if data provided)
- Friction inventory: every identified friction point
- Message match analysis (ad → landing page)
- Prioritized hypothesis backlog with ICE scores
- Quick wins (high ease, high confidence changes to implement immediately)
- Test roadmap: recommended sequence for A/B tests

## Output Location

`campaigns/[slug]/cro/funnel-audit.md` + `hypothesis-backlog.md`
