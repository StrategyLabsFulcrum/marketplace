# Analytics & Data Setup Wizard

Connects marketing data sources, audits historical performance, and establishes the benchmarks that every agent in the system uses as their baseline.

Without this setup, the Marketing Analytics agent has no baseline to compare against, the Performance Marketing agent has no historical ROAS to plan around, and the CRO Orchestrator has no baseline CVR to optimize from. This wizard runs once and gets smarter with every quarterly refresh.

---

## What It Does

**1. Data Source Inventory**
Identifies which platforms are active (Meta, Google Ads, GA4, Klaviyo, Shopify, Stripe, CRM) and walks through data export instructions for each.

**2. Historical Audit**
Analyzes 5 dimensions of historical performance:
- Paid media performance by platform and campaign
- Website and conversion funnel breakdown
- Email marketing performance and list health
- Revenue economics (AOV, CAC, LTV, LTV:CAC)
- Tracking health (pixel status, CAPI, UTMs, attribution)

**3. Benchmark Establishment**
Creates a living benchmarks file covering every active channel — CTR, CPA, ROAS, CVR, open rates, revenue per send, AOV, and more. Marks confidence level for each metric based on data volume.

**4. Data Health Report**
Prioritized list of tracking fixes, UTM gaps, attribution issues, and data integrity problems to resolve before the next campaign.

---

## Slash Command

```
/analytics-setup           ← full first-time setup
/analytics-setup connect   ← add a new data source
/analytics-setup audit     ← quarterly refresh
/analytics-setup health-check  ← quick tracking check
```

---

## Output Files

All outputs saved to `brand-intelligence-center/analytics/`:

| File | Contents |
|------|----------|
| `audit-[date].md` | Full historical performance audit |
| `benchmarks.md` | Living baseline metrics for all channels |
| `data-health.md` | Tracking fixes and attribution issues |

---

## Agents Unlocked After Setup

| Agent | What becomes available |
|-------|----------------------|
| Marketing Analytics | Baseline benchmarks for performance comparison |
| Performance Marketing | Historical ROAS and CPAs for media planning |
| CRO Orchestrator | Baseline CVR and funnel metrics to optimize from |
| Campaign Strategist | Historical channel performance for budget allocation |

---

## Refresh Cadence

| When | What to run |
|------|-------------|
| First time | `/analytics-setup` — full setup |
| Adding a new channel | `/analytics-setup connect [platform]` |
| Every quarter | `/analytics-setup audit` — refresh all benchmarks |
| After a major campaign | `/analytics-setup benchmark-update` — update paid metrics |

---

## Supported Platforms

Meta Ads · Google Ads · Google Analytics 4 · Klaviyo · Shopify · WooCommerce · Stripe · HubSpot · Salesforce · TikTok Ads · LinkedIn Ads · Pinterest Ads · Google Search Console
