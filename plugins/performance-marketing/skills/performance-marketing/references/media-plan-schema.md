# Media Plan Schema

Templates for all Performance Marketing output documents.

---

## Media Plan Template
`campaigns/{{slug}}/activation/media-plan.md`

```markdown
# Media Plan — {{Campaign Name}}
**Campaign:** {{slug}}
**Brand:** {{brand name}}
**Prepared by:** Performance Marketing Agent
**Date:** {{date}}
**Status:** Draft / Approved / Live

**Campaign goal:** {{from campaign-brief.md}}
**Primary KPI:** {{from kpi-framework.md}}
**Campaign dates:** {{start}} — {{end}} ({{N}} weeks)
**Total budget:** ${{total}}

---

## Budget Allocation

### By Channel

| Channel | Budget | % of Total | Daily | Notes |
|---------|--------|-----------|-------|-------|
| Meta (Facebook/Instagram) | ${{}} | {{}}% | ${{}} | {{note}} |
| Google Search | ${{}} | {{}}% | ${{}} | |
| Google Display | ${{}} | {{}}% | ${{}} | |
| Email | ${{}} | — | — | Internal cost only |
| {{Other}} | ${{}} | {{}}% | ${{}} | |
| **Optimization reserve (10–15%)** | ${{}} | {{}}% | — | Shift toward what's working |
| **Total** | **${{}}** | **100%** | **${{}}** | |

### By Week

| Week | Dates | Meta | Google | Email | Other | Total |
|------|-------|------|--------|-------|-------|-------|
| Week 1 | {{dates}} | ${{}} | ${{}} | — | ${{}} | ${{}} |
| Week 2 | {{dates}} | ${{}} | ${{}} | — | ${{}} | ${{}} |
| Week 3 | {{dates}} | ${{}} | ${{}} | — | ${{}} | ${{}} |
| Week 4 | {{dates}} | ${{}} | ${{}} | — | ${{}} | ${{}} |
| **Total** | | **${{}}** | **${{}}** | **—** | **${{}}** | **${{}}** |

**Pacing notes:** {{Any front-loading or back-loading rationale — e.g., "Heavier spend in weeks 2–3 after learning phase; lighter in week 1 to allow platform calibration"}}

---

## Campaign Structure

### Meta

**Campaign 1: {{Name}} — {{Objective}}**
Total budget: ${{}} / daily

| Ad Set | Audience | Daily Budget | Audience Size | Creative |
|--------|---------|-------------|--------------|---------|
| {{Tier 1 — Retargeting}} | Website visitors 30d + cart abandoners | ${{}} | ~{{}} | {{Ad 1, Ad 2}} |
| {{Tier 2 — Lookalike 1%}} | Purchaser lookalike 1% | ${{}} | ~{{}} | {{Ad 1, Ad 2, Ad 3}} |
| {{Tier 3 — Cold Interest}} | {{Interest stack}} | ${{}} | ~{{}} | {{Ad 1, Ad 2, Ad 3}} |

**Placements:** Advantage+ / Manual: {{Feed, Stories, Reels, Audience Network — specify}}
**Bid strategy:** {{Highest Volume / Cost per Result Goal ($X) / ROAS Goal (X×)}}
**Optimization event:** {{Purchase / Lead / CompleteRegistration}}

---

**Campaign 2 (if applicable):** ...

---

### Google

**Campaign 1: {{Name}} — {{Type: Search / Display / PMax}}**
Daily budget: ${{}}

| Ad Group | Keywords / Audience | Bid Strategy | Ad Copy Variant |
|---------|-------------------|-------------|----------------|
| {{Group 1 — Theme}} | [exact kw], "phrase kw", +broad +kw | Target CPA: ${{}} | RSA 1 |
| {{Group 2 — Theme}} | [exact kw], "phrase kw" | Target CPA: ${{}} | RSA 2 |

**Negative keywords:** {{list key negatives}}
**Ad schedule:** {{All day / Specific hours — with rationale}}
**Location:** {{country, region, or radius}}
**Device bid adjustments:** Mobile {{+/-X%}} / Desktop {{+/-X%}} / Tablet {{-X%}}

---

### Email

**Sequence/Campaign: {{Name}}**
Platform: {{Klaviyo / Mailchimp}}
Segment: {{description of target list}}
List size (estimated): {{N}} contacts

| Email | Name | Subject Line | Send Day/Trigger | Segment | Goal |
|-------|------|-------------|-----------------|---------|------|
| 1 | {{name}} | {{subject line}} | {{Day 0 / trigger event}} | {{Full list}} | {{open + click}} |
| 2 | {{name}} | {{subject line}} | {{Day 3 / non-openers}} | {{Didn't open Email 1}} | {{click + convert}} |
| 3 | {{name}} | {{subject line}} | {{Day 7 / non-converters}} | {{Clicked but didn't convert}} | {{convert}} |

**Flow logic (if sequence):**
```
Trigger: {{list join / event / date}}
→ Email 1 → Wait 3 days
  → IF opened: Email 2 (conversion focus)
  → IF not opened: Email 2 (resend with different subject)
    → Wait 4 days
      → IF converted: EXIT
      → IF not converted: Email 3 (last chance)
```

---

## Audience Targeting Overview

### Meta Audiences

| Audience Name | Type | Source | Size (est.) | Used In |
|--------------|------|--------|------------|---------|
| {{name}} | Retargeting | Website visitors 30d | {{N}} | Ad Set 1 |
| {{name}} | Lookalike | Purchaser list | ~2M (1%) | Ad Set 2 |
| {{name}} | Interest | {{interest stack}} | ~5M | Ad Set 3 |

**Exclusions:**
- Recent purchasers (90 days) excluded from acquisition ad sets
- Existing email subscribers excluded from lead gen ad sets (if applicable)

### Google Audiences

| Audience | Type | Applied To | Bid Modifier |
|---------|------|-----------|-------------|
| Website visitors (30d) | Retargeting | Display campaign | +20% |
| Customer match | CRM upload | Search + Display | Observation |
| In-market: {{category}} | Google In-Market | Search (signal) | +10% |

---

## Creative Assignment

### Meta Ad Creative

| Ad Name | Format | Copy Variant | Visual | Ad Sets Running In |
|---------|--------|-------------|--------|-------------------|
| {{ad-name}} | Static 1080×1080 | {{hook/angle}} | {{image description}} | Ad Set 1, 2 |
| {{ad-name}} | Video :15 | {{hook/angle}} | {{video description}} | Ad Set 2, 3 |
| {{ad-name}} | Carousel 4-card | {{angle}} | {{card descriptions}} | Ad Set 3 |

### Google Ad Creative

| Ad Group | Ad Type | Headlines (top 5) | Descriptions (top 3) |
|---------|--------|-------------------|---------------------|
| {{group}} | RSA | 1. {{H}} 2. {{H}} 3. {{H}} 4. {{H}} 5. {{H}} | 1. {{D}} 2. {{D}} 3. {{D}} |

**Pinned elements:**
- Headline 1 pin: {{if any — e.g., brand name}} — Position 1
- Headline 3 pin: {{if any — e.g., CTA}} — Position 3

**Extensions/Assets:**
- Sitelinks: {{list 4+ sitelinks with descriptions}}
- Callouts: {{list 4+ callouts}}
- Structured snippets: {{header type}}: {{list}}
- Call extension: {{phone number}} — {{business hours}}

---

## KPI Targets by Channel

| Channel | Primary KPI | Target | Secondary KPI | Target |
|---------|------------|--------|--------------|--------|
| Meta | CPA | ${{}} | ROAS | {{}}× |
| Google Search | CPA | ${{}} | CVR | {{}}% |
| Google Display | CPL / CPA | ${{}} | CTR | {{}}% |
| Email | Conversion rate | {{}}% | Revenue per email | ${{}} |
| **Blended** | **CPA** | **${{}}** | **Total conversions** | **{{}}** |

---

## Optimization Schedule

| Milestone | Date | Action |
|---------|------|--------|
| Launch | {{date}} | All campaigns go live at 50% daily budget |
| Day 3 check | {{date}} | Verify delivery; confirm tracking; fix any creative rejections |
| Week 1 review | {{date}} | Confirm learning phase underway; no major changes yet |
| Week 2 — first optimization | {{date}} | First Marketing Analytics brief; begin optimization based on data |
| Weekly thereafter | Each {{day}} | Ongoing optimization cycle |
| Final week | {{date}} | Begin wind-down; reduce budgets if campaign has end date |
| Post-campaign | {{date}} | Analytics post-mortem; brief for Marketing Analytics |

---

## Execution Notes

**Who executes:** {{Human via platform UI / Rube MCP execution / Combination}}
**Approval required from:** {{who needs to sign off before launch}}
**Special considerations:** {{any unique factors — new pixel, first-time platform, compliance requirements}}
```

---

## Campaign Setup Document Template (per platform)
`campaigns/{{slug}}/activation/{{platform}}-setup.md`

```markdown
# {{Platform}} Campaign Setup — {{Campaign Name}}

> Complete configuration. Every field a human needs to replicate in {{Platform}} UI.
> Or: structured for Rube API execution via the {{platform}} Marketing API.

---

## Account Details

- **Ad Account ID:** {{ID}}
- **Business Manager / MCC:** {{name and ID}}
- **Pixel / Tag ID:** {{ID}}
- **Primary conversion event:** {{event name}}

---

## Campaign Settings

| Field | Value |
|-------|-------|
| Campaign name | `{{brand}}_{{slug}}_{{objective}}_{{date}}` |
| Objective | {{value}} |
| Campaign type | {{value}} |
| Special Ad Category | None / Credit / Housing / Employment |
| A/B test | No / Yes — {{what's being tested}} |
| Campaign budget | ${{}} daily / ${{}} lifetime |
| Campaign start date | {{date}} |
| Campaign end date | {{date or ongoing}} |
| Bid strategy | {{strategy}} |

---

## Ad Set 1: {{Name}}

| Field | Value |
|-------|-------|
| Ad Set name | `{{brand}}_{{slug}}_{{audience}}_{{date}}` |
| Budget | ${{}} daily |
| Schedule | Run continuously / {{start}} — {{end}} |
| Audience | {{audience name + ID if pre-built}} |
| Location | {{country/region}} |
| Age | {{range}} |
| Gender | All / Male / Female |
| Detailed targeting | {{interests/behaviors}} |
| Exclusions | {{audiences to exclude}} |
| Placements | Advantage+ / Manual: {{list} |
| Optimization event | {{event}} |
| Bid strategy | {{strategy and value if applicable}} |
| Attribution setting | 7-day click, 1-day view |

### Ad 1: {{Name}}

| Field | Value |
|-------|-------|
| Ad name | `{{descriptive name matching UTM content}}` |
| Format | {{Single image / Video / Carousel}} |
| Creative | {{file name or description}} |
| Primary text | {{copy — full text}} |
| Headline | {{headline}} |
| Description | {{description}} |
| CTA button | {{button text}} |
| Destination URL | {{full UTM-tagged URL}} |

### Ad 2: {{Name}}

...

---

## Ad Set 2: {{Name}}

...

---

## Pre-Launch Checklist

- [ ] Campaign name follows naming convention
- [ ] Conversion event is set correctly
- [ ] Budget is set as intended (daily, not lifetime)
- [ ] Dates are correct
- [ ] All UTM parameters verified on destination URLs
- [ ] Creative passes platform review (no policy violations)
- [ ] Exclusions are applied
- [ ] Tracking verified before launch

**Setup completed by:** Performance Marketing Agent
**Ready for launch:** Yes / Pending {{what}}
```

---

## Optimization Log Template
`campaigns/{{slug}}/activation/optimization-log.md`

```markdown
# Optimization Log — {{Campaign Name}}

Every change made to this campaign after launch. Maintained as a running record.

---

## {{YYYY-MM-DD}}

**Action:** {{What was changed}}
**Platform:** {{Meta / Google / Email / All}}
**Specific location:** {{Campaign / Ad Set / Ad / Keyword level}}
**Source:** Analytics brief {{date}} / Manual observation / Platform alert
**Before state:** {{metric or setting value before}}
**Change made:** {{exact change}}
**Expected impact:** {{what we expect to improve}}
**Status:** Executed via {{Rube / manual UI / pending human execution}}
**Notes:** {{any context}}

---

## {{YYYY-MM-DD}}

...
```
