# Campaign Brief Schema

Full output templates for all campaign documents produced by the Campaign Strategist.

---

## campaign-brief.md

The master strategy document. Every downstream agent reads this.

```markdown
# Campaign Brief — {{Campaign Name}}

> **Campaign Slug**: {{campaign-slug}}
> **Created**: {{date}}
> **Last Updated**: {{date}}
> **Status**: Draft | Approved | Active | Complete

---

## 1. Campaign Overview

| Field | Value |
|-------|-------|
| **Campaign Name** | {{name}} |
| **Campaign Type** | Acquisition / Launch / Promotional / Lead Gen / Retention / Winback / Awareness / Competitive Response |
| **Primary Goal** | {{one sentence — specific and measurable}} |
| **Start Date** | {{date}} |
| **End Date** | {{date or "Always-on"}} |
| **Total Budget** | ${{amount}} |
| **Brand** | {{brand name from brand-intelligence-center}} |

---

## 2. Audience Brief

**Primary Segment**: {{who — specific, not "everyone"}}

**Journey Stage**: Awareness / Consideration / Decision / Retention

**The job they're hiring this campaign to do**:
> {{JTBD statement — "When [situation], I want to [motivation], so I can [expected outcome]"}}

**Key psychological lever** (from switching dynamics):
> **{{Push / Pull / Habit / Anxiety}}** — {{description of the specific force at play}}

**The belief this campaign must create or reinforce**:
> "{{The one belief the audience needs to hold to take the desired action}}"

**Audience exclusions**:
{{Who this campaign is NOT for — from anti-persona in differentiation.md}}

---

## 3. Messaging Territory

**Core Message** (one sentence — what this campaign communicates):
> {{single sentence}}

**Support Messages** (reinforce the core — 2–3 bullets):
- {{support message 1}}
- {{support message 2}}
- {{support message 3}}

**Proof Point to Lead With**:
> {{Most credible evidence from proof-goals.md relevant to this campaign}}

**Competitive Angle**:
> {{How the message positions against the primary alternative — what we're better than}}

**Tone for This Campaign**:
> {{Reference voice-identity.md personality traits most relevant to this campaign moment}}
> *Example: Lead with bold confidence. This campaign is assertive — not warm. Save the warmth for retention.*

**Angles to Avoid**:
- {{Saturated competitive message 1}}
- {{Saturated competitive message 2}}
- {{Brand NEVER list items most relevant here}}

---

## 4. Channel Strategy

| Channel | Role | Budget | Budget % | Start Date | Notes |
|---------|------|--------|----------|-----------|-------|
| {{channel}} | Prospecting / Retargeting / Owned / Earned | ${{amount}} | {{%}} | {{date}} | {{notes}} |

**Budget totals**:
- Paid media: ${{amount}}
- Creative production: ${{amount}}
- Other: ${{amount}}
- **Total**: ${{amount}}

**Channels excluded and why**:
- {{Channel}}: {{reason — budget, audience mismatch, brand fit}}

---

## 5. KPI Framework

### Primary KPIs — the {{N}} numbers that define success

| Metric | Baseline | Target | Measurement Platform | Attribution |
|--------|---------|--------|---------------------|------------|
| {{metric}} | {{baseline or "no prior data"}} | {{target}} | {{platform}} | {{model}} |

### Secondary KPIs — leading indicators

| Metric | Channel | Target | Why It Matters |
|--------|---------|--------|---------------|
| {{metric}} | {{channel}} | {{target}} | {{rationale}} |

### Attribution Model
**Official reporting**: {{model}} via {{platform}}
**In-platform optimization**: Platform-reported ROAS/CPL used for bid decisions only

### Reporting Cadence
{{Daily / Weekly / Monthly}} — first report on {{date}}

---

## 6. Campaign Timeline

| Phase | Dates | Key Activities | Agent Responsible |
|-------|-------|---------------|-------------------|
| **Setup** | {{dates}} | Tracking setup, audience building, creative production | Performance Marketing, Creative Director |
| **Pre-launch** | {{dates}} | QA, creative review, channel setup | All |
| **Soft launch** | {{dates}} | Limited budget test, validate tracking, identify winning creative | Performance Marketing |
| **Full launch** | {{dates}} | Full budget deployment, all channels live | Performance Marketing |
| **{{Peak / Mid-point}}** | {{dates}} | {{activities}} | {{agents}} |
| **Wind down** | {{dates}} | Reduce spend, shift messaging | Performance Marketing |
| **Post-campaign** | {{dates}} | Results analysis, reporting, learnings | Analytics |

**Critical dates**:
- Creative assets due from Creative Director: {{date}}
- Tracking verified: {{date}}
- Campaign live: {{date}}
- First optimization review: {{date}}

---

## 7. Creative Requirements

*Detailed creative brief is in `creative-brief.md`. This section is a summary for planning.*

**Assets required**:

| Format | Channel | Quantity | Priority | Due Date |
|--------|---------|----------|----------|---------|
| Static image | Meta | {{n}} variants | High | {{date}} |
| Video (15s) | Meta, IG Stories | {{n}} variants | High | {{date}} |
| Email | {{platform}} | {{n}} emails | High | {{date}} |
| Landing page | Web | 1 draft | High | {{date}} |
| {{format}} | {{channel}} | {{n}} | {{priority}} | {{date}} |

**Existing assets that can be repurposed**:
{{list or "None — all net new"}}

**Creative production budget**: ${{amount or "N/A — in-house"}}

---

## 8. Constraints and Approvals

**Legal / compliance considerations**:
{{e.g., claims that require substantiation, regulated industries, FTC disclosure requirements}}

**Approval gates**:
| Deliverable | Approver | Deadline |
|------------|---------|---------|
| Campaign Brief | {{name}} | {{date}} |
| Creative | {{name}} | {{date}} |
| Media Plan | {{name}} | {{date}} |
| Campaign Live | {{name}} | {{date}} |

**Messages / angles explicitly off-limits**:
{{list — from brand NEVER rules + competitive sensitivity}}

---

## 9. Open Questions

Items that must be resolved before launch. Campaign Strategist flags; user or relevant agent resolves.

| # | Question | Owner | Due | Status |
|---|---------|-------|-----|--------|
| 1 | {{question}} | {{owner}} | {{date}} | Open |

---

## 10. References

- Brand context: `brand-intelligence-center/system-prompt.md`
- Competitive intel: `competitive-landscape/reports/executive-summary.md`
- Creative brief: `campaigns/{{slug}}/creative-brief.md`
- Performance brief: `campaigns/{{slug}}/performance-brief.md`
- KPI framework: `campaigns/{{slug}}/kpi-framework.md`
- Timeline: `campaigns/{{slug}}/timeline.md`
```

---

## channel-strategy.md

Expanded channel-by-channel plan. Supplements the summary table in campaign-brief.md.

```markdown
# Channel Strategy — {{Campaign Name}}

> Campaign: {{campaign-slug}}
> Total Budget: ${{amount}}
> Date Range: {{start}} → {{end}}

---

## Channel Breakdown

{{Repeat the following block for each active channel}}

### {{Channel Name}}

**Role in campaign**: {{prospecting / retargeting / nurture / conversion / retention}}
**Budget**: ${{amount}} (${{amount/month}} × {{n}} months)
**Start date**: {{date}}

**Audience targeting**:
- {{audience description, custom audiences, lookalikes, exclusions}}

**Campaign objective** (platform setting):
- {{Awareness / Traffic / Leads / Conversions / Catalog Sales}}

**Creative format priority**:
1. {{primary format — e.g., "Single image — 1080x1080"}}
2. {{secondary format — e.g., "15s vertical video"}}

**Messaging priority for this channel**:
- {{Which of the 3 support messages leads on this channel and why}}

**Bid strategy**:
- {{Lowest cost / Cost cap / Bid cap / Target CPA / Manual CPC}}
- Target CPA / Target ROAS: ${{amount}} / {{x}}x

**Key optimizations to watch**:
- {{Metric 1}}: Alert if {{threshold}}
- {{Metric 2}}: Alert if {{threshold}}

**Creative refresh schedule**:
- Initial launch: {{n}} variants
- First refresh: {{date or "after 2 weeks" or "at frequency = 3+"}}

---

## Budget Pacing

| Channel | Total Budget | Month 1 | Month 2 | Month 3 |
|---------|-------------|---------|---------|---------|
| {{channel}} | ${{total}} | ${{m1}} | ${{m2}} | ${{m3}} |
| **Total** | **${{total}}** | **${{m1}}** | **${{m2}}** | **${{m3}}** |

**Pacing notes**:
{{e.g., "Front-load Month 1 for launch awareness, scale back in Month 3 as organic kicks in"}}

---

## Cross-Channel Sequencing

How channels work together — the customer path through this campaign:

```
[Awareness] → Meta prospecting + PR/Influencer
     ↓
[Consideration] → Retargeting (Google Display + Meta) + Email nurture
     ↓
[Decision] → Google Search (branded) + Email (offer) + SMS (urgency)
     ↓
[Retention] → Email post-purchase + Meta existing customer audience
```

**Cross-channel cap**: No customer should see paid ads across all channels simultaneously. Suppress paid retargeting for customers who have already converted.
```

---

## kpi-framework.md (Campaign-Level)

Campaign-specific measurement plan. Filled by Campaign Strategist using `references/kpi-framework.md`.

```markdown
# KPI Framework — {{Campaign Name}}

> Campaign: {{campaign-slug}}
> Goal: {{primary goal}}
> Dates: {{start}} → {{end}}

---

## Primary KPIs

These are the {{N}} numbers that define whether this campaign succeeded.

| Metric | Definition | Baseline | Target | +/- vs. Baseline | Platform |
|--------|-----------|---------|--------|-----------------|---------|
| {{metric}} | {{definition}} | {{baseline}} | {{target}} | {{delta %}} | {{platform}} |

**How baseline was set**: {{historical data / industry benchmark / estimated}}

---

## Secondary KPIs (Leading Indicators)

| Metric | Channel | Current | Target | Alert Threshold |
|--------|---------|---------|--------|----------------|
| CTR | Meta | {{x}}% | {{y}}% | Below {{z}}% → review creative |
| CPC | Google | ${{x}} | ${{y}} | Above ${{z}} → review bids |
| Landing page CVR | Web | {{x}}% | {{y}}% | Below {{z}}% → CRO review |
| Email open rate | Klaviyo | {{x}}% | {{y}}% | Below {{z}}% → subject line test |

---

## Attribution

**Official reporting model**: {{model}}
**Reporting platform**: {{GA4 / CRM / custom}}
**In-platform optimization**: Platform-reported metrics (acknowledged overreporting)

**How we handle cross-channel deduplication**:
{{Description — e.g., "GA4 last-click is the official source of truth. Platform-reported ROAS used for bid optimization only. We expect a 20-30% gap between platform-reported and GA4."}}

---

## Target-Setting Math

**Revenue goal for this campaign**: ${{amount}}
**Average order value**: ${{AOV}}
**Required orders**: {{revenue ÷ AOV}} orders
**Expected landing page CVR**: {{x}}%
**Required sessions**: {{orders ÷ CVR}} sessions
**Expected paid CTR**: {{x}}%
**Required impressions**: {{sessions ÷ CTR}} impressions
**Implied CPM needed**: ${{budget ÷ (impressions ÷ 1000)}}
**Assessment**: {{Realistic / Stretch / Requires recalibration}}

---

## Reporting Schedule

| Report | Cadence | Audience | Owner |
|--------|---------|---------|-------|
| Pacing check | {{daily / weekly}} | Internal | Performance Marketing |
| Performance review | {{weekly / biweekly}} | {{stakeholders}} | Campaign Strategist |
| Creative performance | After 7 days live | Creative Director | Performance Marketing |
| Final campaign report | {{date}} | All | Analytics |
```

---

## timeline.md

Campaign phases with dates and milestone owners.

```markdown
# Campaign Timeline — {{Campaign Name}}

> Campaign: {{campaign-slug}}
> Total Duration: {{N}} days / weeks / months

---

## Phase Overview

| Phase | Start | End | Status |
|-------|-------|-----|--------|
| Setup & production | {{date}} | {{date}} | Planned |
| Pre-launch | {{date}} | {{date}} | Planned |
| Soft launch | {{date}} | {{date}} | Planned |
| Full launch | {{date}} | {{date}} | Planned |
| {{Peak / Midpoint}} | {{date}} | {{date}} | Planned |
| Wind down | {{date}} | {{date}} | Planned |
| Post-campaign | {{date}} | {{date}} | Planned |

---

## Milestone Checklist

### Setup & Production
- [ ] Campaign Brief approved — {{date}}
- [ ] Creative Director briefed — {{date}}
- [ ] Performance Marketing Agent briefed — {{date}}
- [ ] Tracking events verified in GA4 — {{date}}
- [ ] Audiences built (Meta custom audiences, Google lists) — {{date}}
- [ ] Landing page live and tested — {{date}}
- [ ] Email sequences activated in {{platform}} — {{date}}

### Pre-Launch (T-7 to T-1)
- [ ] All creative assets delivered by Creative Director — {{date}}
- [ ] Creative QA complete (brand voice check, legal review) — {{date}}
- [ ] Campaigns set up in ad platforms (not yet live) — {{date}}
- [ ] UTM parameters verified on all links — {{date}}
- [ ] Email send schedule confirmed — {{date}}
- [ ] Stakeholder preview / approval — {{date}}

### Soft Launch
- [ ] Limited budget activated ({{%}} of full budget) — {{date}}
- [ ] Initial creative variants running ({{N}} variants) — {{date}}
- [ ] Tracking confirmed firing correctly — {{date}}
- [ ] 48-hour check: CTR, CVR, CPA on pace — {{date}}

### Full Launch
- [ ] Full budget deployed — {{date}}
- [ ] All channels live simultaneously — {{date}}
- [ ] Launch email sent — {{date}}
- [ ] Social launch content published — {{date}}
- [ ] PR / influencer content live (if applicable) — {{date}}

### Active Campaign
- [ ] Week 1 performance review — {{date}}
- [ ] First creative optimization (pause underperformers) — {{date}}
- [ ] Week 2 performance review — {{date}}
- [ ] Creative refresh if frequency > 3 — {{date}}
- [ ] {{Additional milestones based on campaign type}}

### Wind Down
- [ ] Budget reduction to {{%}} of peak — {{date}}
- [ ] Shift messaging to retention / post-purchase — {{date}}
- [ ] Final email / SMS (last chance if promotional) — {{date}}

### Post-Campaign
- [ ] All campaigns paused — {{date}}
- [ ] Data exported from all platforms — {{date}}
- [ ] Final performance report complete — {{date}}
- [ ] Learnings documented and saved to campaign folder — {{date}}
- [ ] Brand intelligence updated with campaign insights — {{date}}
```
