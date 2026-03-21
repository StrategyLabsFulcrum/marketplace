# Data Ingestion Guide

How to get data into the Marketing Analytics system. Three methods — from simplest to most automated.

---

## Method 1: Pasted Platform Exports (Always Available)

The simplest and most universal approach. Export from the platform, paste into the conversation. Works with any platform, no API keys required.

### Meta Ads Manager Export

**What to export:**
1. Open Ads Manager
2. Set date range for the analysis period
3. View: Campaign level (for campaign overview) or Ad Set level (for audience analysis) or Ad level (for creative analysis)
4. Columns to include: Delivery, Performance, Engagement (use "Customize Columns" to add ROAS, CPL, CPA as needed)
5. Export as CSV or copy the table directly

**Paste format:** Raw CSV text or table — the Analytics Orchestrator will parse it.

**Key columns to include:**
- Campaign/Ad Set/Ad Name
- Status
- Delivery
- Reach, Impressions
- CPM, CPC, CTR
- Link Clicks
- Results (your conversion event)
- Cost per Result
- Amount Spent
- ROAS (if e-commerce)
- Frequency

### Google Ads Export

**What to export:**
1. Campaigns tab → select date range
2. Segment by: None (for campaign level) or Day (for trends)
3. Columns: Impressions, Clicks, CTR, Avg. CPC, Cost, Conversions, Conv. Rate, Cost/Conv., Conv. Value, ROAS
4. Download as CSV

**For Search campaigns, also include:**
- Search Impression Share (is budget or quality the constraint?)
- Search Lost IS (Budget) — if high, you're limited by budget, not bids
- Quality Score (at keyword level)

### Google Analytics 4 Export

**What to export (Acquisition report):**
1. Reports → Acquisition → Traffic Acquisition
2. Date range: analysis period
3. Dimensions: Session source/medium
4. Metrics: Sessions, Engaged Sessions, Engagement Rate, Conversions, Revenue
5. Export as CSV

**What to export (Conversion report):**
1. Reports → Monetization → Ecommerce Purchases (or Events → Conversions)
2. Date range, segmented by source/medium

### Klaviyo Export

**Campaign performance:**
1. Campaigns → select campaign
2. View Report → export metrics
3. Key metrics: Recipients, Delivered, Opened, Clicked, Conversions, Revenue, Unsubscribes, Spam Reports

**Flow performance:**
1. Flows → select flow → Analytics tab
2. Key metrics per email: same as above
3. Export or screenshot the full flow metrics table

### Shopify / E-commerce Platform

**What to export:**
1. Analytics → Reports → Sales by traffic source
2. Date range: analysis period
3. Metrics: Sessions, Conversion rate, Orders, Revenue

**Or paste the Marketing dashboard summary** — the aggregate numbers from the Overview are sufficient for ROI analysis.

---

## Method 2: Files in campaigns/{{slug}}/data/

Drop exported files directly into the campaign's data folder. The Analytics Orchestrator will check this folder automatically.

### Expected File Structure

```
campaigns/{{slug}}/data/
├── meta-ads-{{YYYY-MM-DD}}.csv       ← Meta Ads Manager export
├── google-ads-{{YYYY-MM-DD}}.csv     ← Google Ads export
├── ga4-acquisition-{{YYYY-MM-DD}}.csv ← Google Analytics 4 export
├── email-performance-{{YYYY-MM-DD}}.csv ← Klaviyo/ESP export
├── revenue-{{YYYY-MM-DD}}.csv        ← E-commerce / CRM revenue data
└── notes-{{YYYY-MM-DD}}.md          ← Analyst notes, context, anomalies
```

### Naming Convention
`{{platform}}-{{report-type}}-{{YYYY-MM-DD}}.csv`

Consistent naming allows the orchestrator to identify the most recent file for each platform automatically.

### notes.md Format

Use the notes file to give the Analytics Orchestrator context that isn't in the numbers:

```markdown
# Data Notes — {{date}}

## What happened this period
- {{Any significant events: creative refresh, budget change, audience change, platform outage}}
- {{Seasonal factors: holiday, sale, product launch}}
- {{External factors: competitor activity, market event}}

## Data quality issues
- {{Any gaps, tracking issues, platform discrepancies}}

## Questions to investigate
- {{Specific question to answer with this data}}
```

---

## Method 3: Rube MCP (Automated Pulls)

When Rube connections are configured, the Analytics Orchestrator can pull live data directly without manual exports. This is the most efficient option for regular reporting cadences.

### Checking for Existing Recipes

Before building new integrations, check for existing Rube recipes:

```
RUBE_FIND_RECIPE with query: "marketing analytics [platform name]"
```

### Setting Up a New Rube Connection

Use `RUBE_MANAGE_CONNECTIONS` to set up platform connections:

1. **Meta Marketing API** — requires App ID, App Secret, Access Token, Ad Account ID
2. **Google Ads API** — requires OAuth credentials, Customer ID
3. **Google Analytics Data API** — requires OAuth credentials, Property ID
4. **Klaviyo API** — requires API key
5. **Shopify API** — requires Shop domain, API key, Access token

### Building Analytics Recipes

Once connections exist, create recipes for regular data pulls:

**Weekly Campaign Summary Recipe:**
- Pull: Last 7 days of campaign performance by channel
- Transform: Calculate WoW change for key metrics
- Output: Structured markdown summary → save to `campaigns/{{slug}}/data/`

**Creative Performance Recipe:**
- Pull: Ad-level performance for all active ad sets
- Transform: Calculate CTR trend, frequency, CPA by creative
- Output: Creative leaderboard table → save to `campaigns/{{slug}}/data/`

Use `RUBE_CREATE_UPDATE_RECIPE` to build and save these for reuse.

### Scheduling Automated Reports

Use `RUBE_MANAGE_RECIPE_SCHEDULE` to run analytics recipes on a cadence:
- Weekly: Every Monday at 9am — pulls prior week data
- Monthly: 1st of month — pulls prior month summary
- On-demand: Triggered by Performance Marketing Agent after significant spend changes

---

## Data Quality Standards

### Minimum Data Requirements for Analysis

| Analysis Type | Minimum Data |
|--------------|-------------|
| KPI scorecard | Any spend data + conversion data, even if partial |
| Trend analysis | 2+ time periods of the same metric |
| Creative analysis | 3+ active creatives with 500+ impressions each |
| Attribution/ROI | Revenue data + spend data for same period |
| Benchmark update | 4+ weeks of consistent data |

### When Data Is Incomplete

Always be transparent about data gaps:

1. **Clearly label what's missing:** "Google Search data was not provided — Google channel analysis is excluded from this report."
2. **Use industry benchmarks as placeholders** — labeled as benchmarks, not actuals
3. **Do not extrapolate** from one channel to fill gaps in another
4. **Flag the impact:** "Without conversion tracking data from GA4, ROAS calculations are estimated from Meta's reported conversions only — actual ROAS may differ due to platform attribution overlap."

### Tracking Integrity Checks

Before analysis, verify:

- **UTM parameters:** Are campaigns tagged with consistent UTM parameters? (utm_source, utm_medium, utm_campaign at minimum)
- **Conversion events:** Are the same conversion events being measured across platforms? (Meta reports conversions differently than GA4)
- **Attribution windows:** Meta defaults to 7-day click / 1-day view; Google uses 30-day click by default. Compare on the same basis when possible.
- **Cross-platform double-counting:** Meta and Google may both claim credit for the same conversion. Blended ROAS using platform-reported numbers will always appear higher than actual ROAS. Use GA4 as the source of truth for total conversions; use platform data for channel efficiency metrics.

### The Double-Counting Problem

This is the most common analytics error in multi-channel campaigns.

**Scenario:** Brand spends $5,000 on Meta and $3,000 on Google. Meta reports 150 conversions. Google reports 120 conversions. That's 270 total reported conversions — but GA4 shows 180 actual conversions.

**The problem:** Both platforms are claiming credit for the same 90 conversions. The 270 is inflated.

**How to handle it:**
1. Use GA4 (or your e-commerce platform) as the authoritative conversion count — 180 is the real number
2. Use platform-reported conversions only for within-platform comparison (e.g., Meta ad set A vs. Meta ad set B — the double-counting affects both equally so the relative comparison is still valid)
3. When calculating true ROAS: use actual revenue ÷ total spend, not (Meta reported revenue + Google reported revenue) ÷ total spend

Always flag this in reports: "Platform-reported conversions may include cross-platform double-counting. True conversion count is sourced from GA4."

---

## Analytics Folder Structure

The Analytics Orchestrator maintains an `analytics/` folder at the project root (not inside any specific campaign):

```
analytics/
├── benchmarks.md              ← accumulated performance baselines (cross-campaign)
├── kpi-calendar.md            ← reporting cadence and upcoming review dates
├── reports/
│   ├── performance-report-{{date}}.md
│   ├── performance-report-{{date}}.md
│   └── ...
└── briefs/
    ├── strategic-brief-{{date}}.md       ← → Campaign Strategist
    ├── optimization-actions-{{date}}.md  ← → Performance Marketing Agent
    ├── creative-brief-{{date}}.md        ← → Creative Director + Art Director
    └── ...
```

Campaign-specific data files stay in `campaigns/{{slug}}/data/`. Cross-campaign insights and benchmarks live in `analytics/`.
