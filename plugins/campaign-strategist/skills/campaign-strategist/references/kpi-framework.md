# KPI Framework

Reference for the Campaign Strategist. Defines primary and secondary KPIs by campaign type, industry benchmarks for baseline-setting, and measurement guidance.

---

## KPI Selection Principles

1. **Primary KPIs are outcome metrics** — They measure whether the campaign achieved its business goal. Never let vanity metrics (impressions, followers) be primary KPIs.
2. **Maximum 3 primary KPIs** — More than 3 creates diffusion. If a campaign has one goal, it has one primary KPI.
3. **Secondary KPIs are leading indicators** — They signal whether primary KPIs are on track before the campaign ends.
4. **Every KPI needs a baseline and a target** — A KPI without a target is just a number.
5. **Attribution must be defined upfront** — Disagreeing about attribution after the campaign ends is a trust-destroyer.

---

## KPI Matrix by Campaign Type

### Acquisition Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Customer Acquisition Cost (CAC) | Primary | Total spend ÷ new customers acquired | CRM + Ads platforms |
| Return on Ad Spend (ROAS) | Primary | Revenue attributed ÷ ad spend | Meta Ads Manager / GA4 |
| New Customer % | Primary | New customers ÷ total customers in period | CRM / Shopify |
| Click-Through Rate (CTR) | Secondary | Clicks ÷ impressions per ad | Platform native |
| Landing Page CVR | Secondary | Conversions ÷ landing page sessions | GA4 |
| Cost Per Click (CPC) | Secondary | Spend ÷ clicks | Platform native |
| Add-to-Cart Rate | Secondary (eComm) | ATC ÷ product page views | Shopify / GA4 |

**Benchmarks to calibrate targets:**
- Meta acquisition ROAS benchmark (eComm): 2.5–4x
- Google Search acquisition ROAS: 3–6x
- CAC should be <33% of 12-month LTV
- Landing page CVR benchmark: 2–5% (varies widely by offer and traffic temp)

---

### Launch Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Units / Revenue in Launch Window | Primary | Total sales in defined launch period | CRM / Shopify |
| Trial or Signup Rate | Primary (SaaS) | Signups ÷ unique visitors | GA4 |
| Awareness Reach | Secondary | Unique accounts reached | Meta / TikTok / YouTube |
| PR Coverage Achieved | Secondary | # of placements secured | Manual tracking |
| Email List Growth | Secondary | New subscribers during launch | Klaviyo / platform |
| Cost Per Acquisition | Secondary | Paid spend ÷ conversions | Ads platforms |

**Benchmarks:**
- Product launch email open rate: 30–45% (subscriber list expects launch)
- Launch day traffic vs. baseline: target 3–5x for a significant launch
- Launch ROAS is often below steady-state — factor in awareness cost

---

### Promotional Campaign (Sale / Seasonal)

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Revenue in Promo Window | Primary | Total revenue during campaign dates | Shopify / CRM |
| ROAS | Primary | Campaign revenue ÷ paid spend | Ads platforms + GA4 |
| Orders / Conversions | Primary | Total transactions in window | Shopify |
| AOV (Average Order Value) | Secondary | Revenue ÷ orders | Shopify |
| Cart Abandonment Rate | Secondary | Abandoned carts ÷ initiated carts | Shopify / GA4 |
| Email Revenue Contribution | Secondary | Revenue from email clicks | Klaviyo |
| SMS Contribution | Secondary | Revenue from SMS clicks | Attentive / Klaviyo |

**Benchmarks:**
- BFCM / major sale email open rates: 20–35%
- Promotional email CVR: 2–5%
- Promotional landing page CVR: 4–8% (urgency lifts conversion)
- Blended ROAS target for promotions: 3–5x minimum

---

### Lead Generation Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Cost Per Lead (CPL) | Primary | Spend ÷ total leads generated | Ads platforms + CRM |
| Lead Quality Score | Primary | % of leads that meet ICP criteria | CRM / manual |
| Sales Qualified Lead (SQL) Rate | Primary | SQLs ÷ total leads | CRM |
| Form Completion Rate | Secondary | Form submits ÷ form views | GA4 |
| Landing Page CVR | Secondary | Leads ÷ landing page sessions | GA4 |
| Lead-to-Close Rate | Secondary | Won deals ÷ leads (lagging) | CRM |

**Benchmarks:**
- B2B CPL via LinkedIn: $50–$200+ depending on ACV
- B2B CPL via Google Search: $30–$100
- B2C CPL via Meta: $5–$30
- Form completion rate benchmark: 20–40% (reduce fields to improve)
- Acceptable CPL = (ACV × Close Rate × Gross Margin) ÷ 3

---

### Retention Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Repeat Purchase Rate | Primary | Customers who bought 2+ times in period | Shopify / CRM |
| Customer Lifetime Value (LTV) | Primary | Avg revenue per customer over 12 months | CRM |
| Churn Rate | Primary | Customers lost ÷ total customers | CRM |
| Email Engagement Rate | Secondary | Opens + clicks / sends | Klaviyo |
| Days Between Purchases | Secondary | Avg time between repeat orders | Shopify |
| NPS / CSAT | Secondary | Survey-based satisfaction | Typeform / Delighted |

**Benchmarks:**
- eCommerce repeat purchase rate: 25–40% (strong brands hit 50%+)
- Retention email open rate: 25–40% (engaged list)
- Healthy churn rate: <5% monthly (SaaS), <20% annual (subscription)

---

### Winback Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Reactivation Rate | Primary | Lapsed customers who purchase ÷ lapsed customers contacted | CRM |
| Revenue from Reactivated Customers | Primary | Total revenue from winback purchasers | Shopify / CRM |
| Unsubscribe Rate | Secondary | Unsubscribes ÷ sends | Klaviyo |
| Winback Email Open Rate | Secondary | Opens ÷ sends (expect lower than list avg) | Klaviyo |

**Benchmarks:**
- Winback email open rate: 10–20% (lapsed list is cold)
- Reactivation rate target: 5–15% of lapsed segment
- Define "lapsed" by purchase cycle — 2x average purchase interval = lapsed

---

### Brand / Awareness Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Unique Reach | Primary | Unique accounts reached | Meta / YouTube / TikTok |
| Share of Voice (SOV) | Primary | Brand mentions ÷ total category mentions | Social listening tool |
| Brand Lift | Primary | Aided/unaided awareness change | Meta Brand Lift study / survey |
| CPM | Secondary | Cost per 1,000 impressions | Platform native |
| Video View Rate | Secondary | Views ÷ impressions | Meta / YouTube |
| Frequency | Secondary | Avg impressions per unique person | Meta Ads Manager |

**Benchmarks:**
- Effective frequency for awareness: 3–7 impressions per person
- Meta CPM: $5–$30 depending on audience and creative
- YouTube CPV: $0.01–$0.05 for skippable, $0.05–$0.20 for non-skippable
- Brand lift studies meaningful at $50,000+ campaign spend

---

### Competitive Response Campaign

| KPI | Type | Definition | Platform |
|-----|------|-----------|---------|
| Competitor Keyword Impression Share | Primary | Impressions ÷ eligible impressions on competitor terms | Google Search Console / Ads |
| Branded Search Volume Protection | Primary | YoY change in branded search volume | Google Search Console |
| Conquest CTR | Secondary | CTR on competitor keyword ads | Google Ads |
| Competitive Win Rate (Sales) | Secondary | Won deals in competitive scenarios | CRM |

---

## Baseline-Setting Guide

When the user doesn't have a baseline:

**For paid campaigns:**
- Pull last 30-day data from Meta Ads Manager / Google Ads
- If no prior campaigns: use industry benchmarks and flag that targets are estimates
- First 14 days of a new campaign = learning phase — don't evaluate against KPI targets until learning exits

**For email:**
- Pull 90-day average open rate, CTR, CVR from Klaviyo
- Segment by campaign type (promotional vs. flow) — they have different baselines

**For revenue:**
- Pull same period last year (SPLY) for seasonal campaigns
- Pull trailing 30 days for non-seasonal campaigns
- For launches, there is no baseline — set a forecast range, not a single point

**For organic:**
- Pull trailing 90 days of traffic from GA4
- Organic campaigns take 60–90 days to show meaningful results — set 90-day and 6-month targets

---

## Target-Setting Guidance

Start with what the business needs, work backward to what the campaign must deliver:

1. **Revenue goal for the period**: Comes from `proof-goals.md` (current business focus) and `financial.md`
2. **Estimated CVR**: From baseline or benchmarks
3. **Required traffic / leads**: Revenue goal ÷ AOV ÷ CVR
4. **Required reach**: Traffic needed ÷ expected CTR
5. **Required budget**: Reach needed × CPM or CPC benchmarks

Surface this math in the campaign brief. It makes budget discussions objective.

---

## Attribution Model Guidance

| Model | Best For | Caution |
|-------|---------|---------|
| Last-click | Simple attribution, single-channel campaigns | Undercredits awareness channels |
| First-click | Lead generation, understanding what drives top-of-funnel | Undercredits close-driving channels |
| Linear | Multi-channel campaigns, balanced view | Dilutes credit — hard to optimize |
| Time-decay | Short promotional windows | Not useful for longer campaigns |
| Data-driven | High volume campaigns with 30+ conversions/week per channel | Requires GA4 / Meta CAPI |
| Platform-reported | Use for within-platform optimization decisions only | Will overreport vs. GA4 (deduplication issue) |

**Recommendation for most campaigns**: Report GA4 (last-click or linear) as official numbers. Use platform-reported ROAS for in-platform optimization decisions only. Always note the attribution model when reporting results.

---

## Reporting Cadence Recommendation

| Campaign Length | Reporting Cadence |
|----------------|------------------|
| 1–2 weeks (promo) | Daily during active window |
| 1 month | Weekly check-in, final report at end |
| 3 months | Weekly check-in, monthly review, final report |
| Always-on | Monthly review, quarterly deep dive |

Always include in reports:
- Actuals vs. targets for each primary KPI
- Spend pacing (on track vs. over/under)
- Creative performance ranking (which variants won)
- Recommended optimizations for next period
