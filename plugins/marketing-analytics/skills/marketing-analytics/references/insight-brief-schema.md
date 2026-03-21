# Insight Brief Schema

Templates for all Marketing Analytics output documents. These are the structured formats that route insights from analytics back to the agents who act on them.

---

## Performance Report Template
`analytics/reports/performance-report-{{YYYY-MM-DD}}.md`

```markdown
# Marketing Performance Report
**Period:** {{start date}} — {{end date}}
**Campaigns covered:** {{campaign slugs}}
**Prepared by:** Marketing Analytics Orchestrator
**Date:** {{date}}
**Prior report:** {{link to previous report, if exists}}

---

## Executive Summary

> 5 bullets maximum. The most important things. Lead with the most critical finding — not the most positive.

- {{Finding 1 — most important insight from this period}}
- {{Finding 2}}
- {{Finding 3}}
- {{Finding 4}}
- {{Finding 5}}

**Overall health:** 🟢 On Track / 🟡 At Risk / 🔴 Off Track
**Action required:** Yes — {{what needs to happen}} / No — continue current direction

---

## Campaign KPI Scorecard

### {{Campaign Name}} ({{slug}})
**Goal:** {{campaign goal from brief}}
**Period:** {{campaign start}} — {{campaign end}} | Day {{N}} of {{total days}}

| Metric | Target | Actual | Pacing % | Status |
|--------|--------|--------|---------|--------|
| {{Primary KPI}} | {{target}} | {{actual}} | {{%}} | 🟢/🟡/🔴 |
| {{Secondary KPI 1}} | {{target}} | {{actual}} | {{%}} | 🟢/🟡/🔴 |
| {{Secondary KPI 2}} | {{target}} | {{actual}} | {{%}} | 🟢/🟡/🔴 |
| Spend to date | {{budget}} | {{actual}} | {{%}} | 🟢/🟡/🔴 |
| ROAS | {{target}} | {{actual}} | — | 🟢/🟡/🔴 |

**Trend (WoW):** {{Improving / Holding / Declining}} — {{primary metric}} {{direction}} {{%}}
**Projected end-of-campaign:** At current pace, will {{hit / miss}} target by {{projected shortfall/surplus}}

**Key observations:**
- {{Observation 1}}
- {{Observation 2}}

---

## Channel Performance Breakdown

| Channel | Spend | Impressions | Clicks | CTR | Conversions | CVR | CPA | ROAS |
|---------|-------|------------|--------|-----|-------------|-----|-----|------|
| {{Channel 1}} | ${{}} | {{}} | {{}} | {{}}% | {{}} | {{}}% | ${{}} | {{}}× |
| {{Channel 2}} | ${{}} | {{}} | {{}} | {{}}% | {{}} | {{}}% | ${{}} | {{}}× |
| **Total** | ${{}} | {{}} | {{}} | {{}}% | {{}} | {{}}% | ${{}} | {{}}× |

**Channel efficiency ranking (by CPA, lowest to highest):**
1. {{Channel}} — ${{CPA}}
2. {{Channel}} — ${{CPA}}
3. {{Channel}} — ${{CPA}}

**Budget allocation vs. performance:**
{{Channel}} is receiving {{X}}% of spend but delivering {{Y}}% of conversions. {{Observation about whether allocation is efficient.}}

---

## Creative Performance Breakdown

### Top Performers
| Creative | Format | Hook Type | Impressions | CTR | CVR | CPA | Status |
|---------|--------|----------|------------|-----|-----|-----|--------|
| {{Name/ID}} | {{format}} | {{hook}} | {{}} | {{}}% | {{}}% | ${{}} | Active |

### Underperformers / Fatigue Flags
| Creative | Format | Issue | Recommendation |
|---------|--------|-------|---------------|
| {{Name/ID}} | {{format}} | {{CTR down X% / frequency Y}} | {{Pause / Refresh}} |

**Winning pattern this period:**
{{What the top performers have in common — format, hook, angle, visual approach}}

**What to retire:**
{{What's fatigued or not working — specific creative, with reason}}

---

## Revenue and ROI Summary

| Metric | This Period | Prior Period | Change |
|--------|------------|-------------|--------|
| Marketing-attributed revenue | ${{}} | ${{}} | {{+/-%}} |
| Total ad spend | ${{}} | ${{}} | {{+/-%}} |
| Blended ROAS | {{}}× | {{}}× | {{+/-%}} |
| New customers | {{}} | {{}} | {{+/-%}} |
| Blended CAC | ${{}} | ${{}} | {{+/-%}} |
| LTV:CAC (estimated) | {{}}:1 | — | — |

**Break-even ROAS:** {{calculated from gross margin}} — current ROAS is {{above / below / at}} break-even
**ROI verdict:** {{Profitable growth / Break-even growth / Loss-leader / Unprofitable}} — {{1 sentence rationale}}

---

## Key Findings

Ranked by importance — the most critical insights from this period's data.

### Finding 1 — {{Title}}
**What:** {{Specific observation with supporting data}}
**Why it matters:** {{Strategic significance}}
**Confidence:** High / Medium / Low — {{data quality note if medium/low}}

### Finding 2 — {{Title}}
...

### Finding 3 — {{Title}}
...

---

## Recommended Actions

| Priority | Action | Owner | Rationale | Expected Impact |
|---------|--------|-------|-----------|----------------|
| 🔴 High | {{Specific action}} | Performance Marketing | {{data-based reason}} | {{expected result}} |
| 🟡 Medium | {{Specific action}} | Campaign Strategist | {{reason}} | {{expected result}} |
| 🟢 Low | {{Specific action}} | Creative Director | {{reason}} | {{expected result}} |

---

## Data Notes

**Data sources used:** {{list of platforms/exports/files used}}
**Data gaps:** {{any missing data and what it means for confidence}}
**Assumptions made:** {{any assumptions, clearly labeled}}
**Attribution model:** {{which model was used and why}}
**Next report:** {{recommended date or trigger}}
```

---

## Strategic Insight Brief Template
`analytics/briefs/strategic-brief-{{YYYY-MM-DD}}.md`

Recipient: Campaign Strategist
Purpose: Strategic memo — what the data means for strategy, not a data report

```markdown
# Strategic Insight Brief
**To:** Campaign Strategist
**From:** Marketing Analytics
**Re:** {{Campaign name / period}}
**Date:** {{date}}

---

## Situation

{{2–3 sentences. What the data shows overall. Be direct — lead with the most important thing.}}

Example: "The spring acquisition campaign is pacing 22% behind target with 14 days remaining. The shortfall is concentrated in Google Search, which is generating leads at 2.1× the target CPL. Meta is performing ahead of target and could absorb additional budget."

---

## Strategic Implications

**On campaign goal:** {{Is the original goal still achievable? What would it take? Should it be revised?}}

**On audience:** {{What is the data revealing about the target audience — who's responding, who isn't, any surprises?}}

**On messaging/offer:** {{Any signals that the current messaging or offer needs adjustment?}}

**On channels:** {{What the channel mix data suggests for strategy — not specific bid changes but channel-level strategic direction}}

**On budget:** {{Is current budget allocation aligned with performance? Any case for reallocation or budget adjustment?}}

---

## Recommended Strategic Adjustments

1. **{{Adjustment title}}**
   What: {{Specific change to campaign strategy}}
   Why: {{Data supporting this — specific numbers}}
   Risk: {{What could go wrong or what we'd give up}}

2. **{{Adjustment title}}**
   ...

3. **{{Adjustment title}}**
   ...

---

## Decisions Needed

The following require Campaign Strategist judgment:

- **{{Decision 1}}:** {{The choice to make and the relevant data context}}
- **{{Decision 2}}:** {{The choice to make}}

---

## Supporting Data
Full performance report: `analytics/reports/performance-report-{{date}}.md`
```

---

## Optimization Action List Template
`analytics/briefs/optimization-actions-{{YYYY-MM-DD}}.md`

Recipient: Performance Marketing Agent
Purpose: Specific, executable actions — no narrative

```markdown
# Optimization Action List
**To:** Performance Marketing Agent
**From:** Marketing Analytics
**Date:** {{date}}
**Campaign:** {{slug}}
**Covers:** {{date range}}

---

## 🔴 High Priority (Act within 24–48 hours)

**Action:** {{Specific action}}
**Channel:** {{channel / platform / ad set / email}}
**What to do:** {{Exact instruction — pause X, increase budget on Y by Z%, add negative keyword W}}
**Rationale:** {{1–2 sentences — the specific data behind this}}
**Expected impact:** {{What we expect to happen}}

---

**Action:** {{Next action}}
...

---

## 🟡 Medium Priority (Act within 1 week)

**Action:** {{Specific action}}
**Channel:** {{channel}}
**What to do:** {{Instruction}}
**Rationale:** {{Data}}
**Expected impact:** {{Expected result}}

---

## 🟢 Low Priority / Test Queue (When bandwidth allows)

**Action:** {{Test or optimization to run when current priorities are handled}}
**Channel:** {{channel}}
**What to do:** {{Instruction}}
**Rationale:** {{Hypothesis}}
**How to measure:** {{What metric determines success}}

---

## Do Not Touch

The following are performing well — do not optimize them. Leave them running.

- {{Ad set / campaign / creative}} — {{why: on target, still learning, etc.}}
- {{Another}}

---

## Notes for Performance Marketing
{{Any context the Performance Marketing Agent needs to execute these actions correctly — platform-specific notes, constraints, dependencies}}
```

---

## Creative Performance Brief Template
`analytics/briefs/creative-brief-{{YYYY-MM-DD}}.md`

Recipients: Creative Director, Art Director
Purpose: Data-informed creative direction — what to evolve, what to retire, what to test

```markdown
# Creative Performance Brief
**To:** Creative Director, Art Director
**From:** Marketing Analytics
**Re:** Creative performance signals — {{period}}
**Date:** {{date}}

---

## What's Working

The following creative approaches are outperforming benchmarks. These patterns should inform new creative development.

### Paid Social
- **Format:** {{e.g., "Static 1080×1080 is outperforming video 2:1 on CPL this period — likely due to product clarity at a glance"}}
- **Hook type:** {{e.g., "'Before/after results' hook is generating 1.8× average CTR vs. 'problem-first' hooks"}}
- **Copy angle:** {{e.g., "Messaging focused on speed-to-value is outperforming price/savings messaging"}}
- **Visual approach:** {{e.g., "Clean product-on-white visuals outperforming lifestyle photography by 40% CVR"}}

### Email
- **Subject lines:** {{What subject line patterns are driving highest open rates}}
- **Body copy:** {{What format, length, or CTA approach is driving highest CTR}}
- **Visual treatment:** {{What email layouts or imagery are performing best}}

---

## What to Retire

The following should be paused or not repeated.

| Asset | Platform | Issue | Performance Signal |
|-------|---------|-------|------------------|
| {{Ad name/ID}} | Meta | Creative fatigue | CTR down 45% from week 1; frequency 4.8 |
| {{Ad name/ID}} | Google Display | Low CVR | 0.3% CVR vs. 1.4% campaign average |
| {{Email name}} | Email | Low engagement | 18% open, 0.4% CTR; below baseline |

---

## Patterns in Top Performers

{{The insight paragraph — synthesize what the top-performing creative has in common. This is the signal for the Creative Director to build on.}}

Example: "Across paid and email, the clearest pattern in top performers is specificity — ads and emails that name a specific result ('cut response time by 3 days') consistently outperform those with general benefit claims ('work faster'). Second pattern: solo product shots outperforming lifestyle shots by 1.6× on CVR — suggests the audience wants to evaluate the product itself, not the lifestyle around it."

---

## Recommended New Directions

Based on performance patterns, these are the highest-priority creative hypotheses to test:

1. **{{Hypothesis name}}**
   Direction: {{Specific creative direction to test}}
   Rationale: {{Performance data supporting this}}
   Suggested format: {{format, channel}}

2. **{{Hypothesis name}}**
   ...

3. **{{Hypothesis name}}**
   ...

---

## Visual Performance Notes (For Art Director)

{{Specific observations about visual execution — format, composition, color, photography style — that are showing up in performance data.}}

Examples:
- "Bold typographic treatments (campaign line at large scale) are driving higher CTR in the feed environment — worth leaning into"
- "Portrait 4:5 format is outperforming square 1:1 by 28% on delivery cost — shift new creative to 4:5 first"
- "Photography with direct eye contact is generating higher engagement than product-only shots on awareness objectives"

---

## Audience Signals

{{Any audience-level data that should inform creative targeting:}}
- Age/demo segment performing best: {{}}
- Audience showing highest CVR: {{}}
- Audience that's not converting despite high CTR: {{}} — may indicate messaging mismatch

---

## Supporting Data
Full performance report: `analytics/reports/performance-report-{{date}}.md`
```

---

## Benchmarks File Template
`analytics/benchmarks.md`

Maintained by the Marketing Analytics Orchestrator. Updated after every full report cycle.

```markdown
# Marketing Performance Benchmarks
**Brand:** {{brand name}}
**Last updated:** {{date}}
**Data range:** {{first data point}} — {{most recent report date}}

> These benchmarks are based on actual historical performance for this brand. They replace industry averages as the reference standard. When a new metric appears without historical data, use analyst-frameworks.md industry ranges as a temporary proxy until 4+ weeks of actuals are available.

---

## Paid Social — Meta

| Metric | Typical Range | Strong Performance | Weak (investigate) |
|--------|-------------|-------------------|-------------------|
| CPM | ${{low}}–${{high}} | Below ${{}} | Above ${{}} |
| CTR (Feed) | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CTR (Stories) | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CVR | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CPA | ${{}}–${{}} | Below ${{}} | Above ${{}} |
| ROAS | {{}}×–{{}}× | Above {{}}× | Below {{}}× |
| Frequency (before fatigue) | Up to {{}} | — | Above {{}} |

## Paid Search — Google

| Metric | Typical Range | Strong | Weak |
|--------|-------------|--------|------|
| CTR (Brand) | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CTR (Non-brand) | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CVR | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CPA | ${{}}–${{}} | Below ${{}} | Above ${{}} |
| ROAS | {{}}×–{{}}× | Above {{}}× | Below {{}}× |

## Email

| Metric | Typical Range | Strong | Weak |
|--------|-------------|--------|------|
| Open rate (warm list) | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CTR | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| CVR | {{}}–{{}}% | Above {{}}% | Below {{}}% |
| Unsubscribe rate | Below {{}}% | Below {{}}% | Above {{}}% |

## Revenue Metrics

| Metric | Actual | Notes |
|--------|--------|-------|
| Blended CAC | ${{}} | {{last updated}} |
| CAC — Meta | ${{}} | {{last updated}} |
| CAC — Google | ${{}} | {{last updated}} |
| Avg. LTV ({{period}}) | ${{}} | {{basis for estimate}} |
| LTV:CAC ratio | {{}}:1 | |
| Break-even ROAS | {{}}× | Based on {{}}% gross margin |

## Creative Performance

**Consistently strong formats:** {{list}}
**Consistently strong hook types:** {{list}}
**Formats to avoid:** {{list}}
**Average ad lifespan before fatigue:** {{N}} weeks

## Audience Segments

| Segment | Channel | Typical CPA | Notes |
|---------|---------|------------|-------|
| {{segment}} | {{channel}} | ${{}} | {{observation}} |

## Campaign History Summary

| Campaign | Slug | Goal | Primary KPI Result | ROI Verdict |
|---------|------|------|-------------------|------------|
| {{name}} | {{slug}} | {{goal}} | {{result vs. target}} | {{verdict}} |
```
