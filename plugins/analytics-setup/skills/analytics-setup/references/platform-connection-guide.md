# Platform Connection Guide

Quick reference for connecting each data source to the analytics setup wizard. Covers access requirements, data depth, and known limitations.

---

## Meta Ads Manager

**Access required:** Admin or Advertiser role on the Ad Account
**API access:** Meta Business Suite → Business Settings → Users
**Data depth available:** Up to 3 years of historical data in Ads Manager
**Key limitation:** Attribution window changes (iOS14+) mean pre-2021 data uses different attribution; treat as separate benchmark period
**Event Match Quality:** Check Ads Manager → Events Manager → your pixel → Event Match Quality score (target: 7+/10)
**CAPI status:** Check Events Manager for server events alongside browser events (deduplication required)

### What Resets Benchmarks
- Major audience or placement changes
- iOS 14.5 (April 2021) — attribution window shortened; data before/after not directly comparable
- Shifting from broad to narrow targeting or vice versa

---

## Google Ads

**Access required:** Admin or Standard access on the Google Ads account
**Data depth available:** Up to account creation date
**Key limitation:** Enhanced Conversions requires Google Tag implementation; verify before relying on conversion data
**Smart Bidding:** Note which campaigns use Smart Bidding — their performance data during learning phase (first 2–4 weeks) should be excluded from benchmarks

### Google Ads Editor
For bulk data export: Google Ads Editor → File → Export → All campaigns
Useful for getting full creative performance history across all ad variations

### Performance Max
PMax campaigns have limited visibility. Available metrics: campaign level only (no ad group/asset breakdown in standard exports). Note separately in benchmarks.

---

## Google Analytics 4

**Access required:** Editor or higher on the GA4 property
**Data depth available:** Up to 14 months in standard UI; BigQuery export for unlimited (requires setup)
**Key limitation:** GA4 replaced Universal Analytics in July 2023. If the brand has both, note the switch date — data is not comparable across platforms
**Sampling:** GA4 Explore reports may be sampled on large data sets. Note "(sampled)" indicator in reports.

### Universal Analytics Sunset
UA data stopped collecting July 1, 2023. If benchmarks are needed from pre-July 2023, export UA data separately and note the platform difference.

### Enhanced Measurement
Verify GA4 Enhanced Measurement is enabled: Admin → Data Streams → your stream → Enhanced Measurement toggle
Should be enabled: Page views, Scrolls, Outbound clicks, Site search, Video engagement, File downloads

### eCommerce Implementation
Standard GA4 eCommerce events required for full funnel:
- `view_item` — product page views
- `add_to_cart`
- `begin_checkout`
- `purchase` (with revenue and transaction_id)

Check which are firing: GA4 → Configure → Events

---

## Klaviyo

**Access required:** Viewer or higher
**Data depth available:** Full account history
**Key limitation:** Revenue attribution uses Klaviyo's 5-day click / 1-day open window by default. This may overattribute revenue to email vs platform-reported revenue. Note attribution window in benchmarks.

### List Health Context
Klaviyo's engagement-based sending means lower-engagement contacts may not receive all sends. Open rates reflect sent volume, not total list size — this is correct for email benchmarks.

### Deliverability Indicators to Check
- Klaviyo → Analytics → Deliverability → Domain health
- Bounce rate (hard + soft): Target under 0.5%
- Spam complaint rate: Target under 0.08%
- Sender reputation status: Good / Fair / Poor

---

## Shopify

**Access required:** Staff member with Reports access or higher
**Data depth available:** Full store history
**Key limitation:** Shopify's CVR is calculated as sessions with a purchase / total sessions. This differs from GA4's CVR (which uses user-based calculation). Note which source is being used.

### Shopify vs GA4 Revenue Discrepancy
It's normal for Shopify and GA4 revenue to differ by 5–15%:
- GA4 may miss purchases if the thank-you page isn't loaded (customer closes tab early)
- Shopify includes taxes; GA4 typically excludes them
- Chargebacks and refunds processed in Shopify may not be reflected in GA4

Use Shopify as the revenue source of truth. Use GA4 for traffic and funnel analysis.

### Multi-Currency
If the store accepts multiple currencies, confirm all Shopify revenue reports are in the base currency before using for benchmarks.

---

## Klaviyo + Shopify Integration

When both are connected, Klaviyo attributes revenue to email/SMS touchpoints. This creates double-counting with Shopify's channel attribution. The correct approach:
- **Total revenue:** Use Shopify as source of truth
- **Email-attributed revenue:** Use Klaviyo for email channel performance only
- **Paid-attributed revenue:** Use GA4 (multi-touch) or Meta/Google (last-click)
- Never add Klaviyo revenue + Meta revenue + Google revenue — they overlap

---

## Stripe / Payment Processors

**Access required:** Reporting or Admin
**Best use:** Revenue reconciliation and subscription metrics (MRR, churn, LTV)
**Not needed for:** Campaign performance data (use platform-native data)

Useful Stripe exports:
- Monthly revenue summary (MRR trend)
- Churn rate report
- Customer lifetime value by cohort (Stripe Sigma or export to calculate)

---

## HubSpot CRM

**Access required:** Reporting access
**Best use:** Lead quality, deal pipeline, close rates, lead-to-customer conversion rate by source
**Key metric to extract:** Lead-to-customer conversion rate by traffic source

This connects paid media cost (from Meta/Google) to ultimate revenue (from CRM deals) for true CAC calculation across a longer sales cycle.

---

## Data Quality Red Flags

Issues that invalidate benchmarks — flag these before using data:

| Issue | Impact | Fix |
|-------|--------|-----|
| GA4 not tracking purchases | No CVR or revenue data | Implement purchase event |
| Meta Pixel firing on page load only (not purchase) | No conversion data | Fix pixel event triggers |
| UTMs missing on paid traffic | Can't attribute sessions to channels | Enforce UTM tagging |
| GA4 receiving bot traffic | Inflated sessions, deflated CVR | Enable bot filtering in GA4 |
| Shopify checkout on subdomain | GA4 loses session on checkout | Cross-domain tracking setup |
| Multiple GA4 properties | Data split across properties | Consolidate or note in analysis |
| Meta CAPI not configured | Under-reporting on iOS devices | Set up Conversions API |
| Klaviyo 5-day attribution vs 24-hour | Revenue overattribution to email | Note window; don't combine with other sources |

---

## Benchmark Confidence Thresholds

Minimum data requirements before a metric is reliable:

| Metric | Minimum for "Medium" confidence | Minimum for "High" confidence |
|--------|--------------------------------|-------------------------------|
| Platform CTR | 10,000 impressions | 100,000 impressions |
| Platform CVR | 100 conversions | 500 conversions |
| Email open rate | 10 campaigns sent | 30+ campaigns sent |
| Overall site CVR | 1,000 sessions | 5,000 sessions |
| AOV | 100 orders | 500 orders |
| CAC | 3 months of data | 6+ months of data |
| LTV | 6 months of cohort data | 12+ months of cohort data |

Below minimum thresholds: mark benchmark as "Low confidence — directional only."
