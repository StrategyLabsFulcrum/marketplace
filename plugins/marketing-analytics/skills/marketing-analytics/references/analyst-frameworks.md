# Analyst Frameworks

Analytical frameworks for each specialist type. These are the lenses each analyst applies to the data — the "how to think about this" behind the numbers.

---

## Campaign Performance Analyst Framework

### KPI Scorecard Structure

For each campaign, score every metric against its target:

| Status | Definition |
|--------|-----------|
| On Track | Within 10% of target pace |
| At Risk | 11–25% below target pace |
| Off Track | More than 25% below target |
| Exceeding | More than 10% above target pace |

**Pacing math:**
Pacing % = (Actual to date) ÷ (Target × (Days elapsed ÷ Total campaign days)) × 100

Example: Campaign is 10 days into a 30-day run. Target is 300 conversions. Actual is 85 conversions.
Expected pace at day 10 = 300 × (10/30) = 100 conversions
Pacing = 85 ÷ 100 = 85% → At Risk

### KPI Hierarchy by Campaign Type

| Campaign Type | Primary KPI | Secondary KPIs | Efficiency Metric |
|--------------|------------|----------------|------------------|
| Acquisition | New customers / CPL | Conversion rate, ROAS | CAC |
| E-commerce | Revenue / ROAS | Units sold, AOV | CPA |
| Lead generation | Qualified leads / CPL | Lead-to-opportunity rate | CPL |
| Brand awareness | Reach / Impressions | Frequency, aided recall | CPM |
| Retention | Revenue from existing customers | Repeat purchase rate, LTV | Cost per retained customer |
| Promotional | Revenue in window / ROAS | Redemption rate, AOV | CPA |
| Content/SEO | Organic sessions | Rankings, backlinks | Cost per session |
| Product launch | Trial signups / installs | Activation rate | CAC |

### Anomaly Detection Triggers

Flag for investigation when:
- Any metric shifts more than 30% week-over-week without a clear cause (spend change, creative refresh, audience update)
- CTR drops more than 20% without a copy/creative change → ad fatigue signal
- CVR drops while CTR holds → post-click problem (landing page, offer, audience mismatch)
- CPM spikes more than 40% → auction competition increase or targeting too narrow
- Frequency exceeds 3.5 on Meta → ad fatigue territory; creative refresh needed
- Email open rate drops more than 15% from baseline → deliverability or subject line issue
- Unsubscribe rate exceeds 0.5% on any send → message-audience mismatch or send frequency too high

### Trend Analysis Method

Compare the current period to the same period last week (WoW) and the same period last month (MoM):
- WoW change: Short-term tactical signal
- MoM change: Trend confirmation

If WoW and MoM point in the same direction: confirmed trend — act on it.
If WoW shows a shift but MoM doesn't: may be noise — watch for another week before acting.
If MoM trend reverses a positive WoW: prior week may have been anomalous — do not overreact.

---

## Channel Mix Analyst Framework

### Core Channel Efficiency Metrics

| Metric | Formula | What It Tells You |
|--------|---------|-----------------|
| CPM (Cost per 1,000 impressions) | Spend ÷ Impressions × 1,000 | Cost to reach the audience |
| CPC (Cost per click) | Spend ÷ Clicks | Cost to drive a click |
| CTR (Click-through rate) | Clicks ÷ Impressions × 100 | Creative + audience relevance |
| CPL (Cost per lead) | Spend ÷ Leads | Cost to generate a lead |
| CPA (Cost per acquisition) | Spend ÷ Conversions | Cost to generate a conversion |
| ROAS (Return on ad spend) | Revenue ÷ Spend | Revenue efficiency of spend |
| CVR (Conversion rate) | Conversions ÷ Clicks × 100 | Post-click effectiveness |

### Industry Benchmark Ranges (use when no historical baseline exists)

These are broad industry ranges — actual performance varies significantly by industry, offer, and creative quality. Use as orientation, not targets.

| Channel | CPM | CTR | CVR | ROAS |
|---------|-----|-----|-----|------|
| Meta Feed (awareness) | $8–18 | 0.8–2.0% | — | — |
| Meta Feed (conversion) | $12–25 | 1.0–2.5% | 1.5–4.0% | 1.5–4×|
| Meta Stories | $5–12 | 0.5–1.5% | 1.0–3.0% | — |
| Google Search | — | 3–8% (branded 15–30%) | 3–8% | 3–8× |
| Google Display | $1–5 | 0.1–0.3% | 0.5–2.0% | — |
| Google Shopping | — | 0.5–2.0% | 1.5–4.5% | 3–8× |
| Email (cold outreach) | — | — | 2–5% reply rate | — |
| Email (warm list) | — | 20–35% open, 2–5% CTR | 1–3% CVR | — |
| LinkedIn | $30–80 | 0.3–0.8% | 0.5–2.0% | varies by offer |
| TikTok | $8–15 | 1.0–3.0% | 1.0–3.0% | 1–3× |

### Attribution Models

Different models tell different stories — always consider which model fits the campaign:

| Model | How It Works | Best Used When |
|-------|-------------|----------------|
| Last-touch | 100% credit to final touchpoint before conversion | Simple single-channel campaigns; direct response |
| First-touch | 100% credit to first touchpoint | Measuring top-of-funnel efficiency; brand discovery |
| Linear | Equal credit to all touchpoints | Multi-channel awareness campaigns |
| Time-decay | More credit to touchpoints closer to conversion | Longer sales cycles with multiple touchpoints |
| Data-driven | Algorithmic credit based on actual conversion paths | High volume campaigns with sufficient data (Google's model) |

**Practical guidance:** Most small-to-mid businesses should use last-touch as primary and first-touch as a secondary lens. Full multi-touch attribution requires significant data volume and clean cross-platform tracking.

### Channel Contribution Analysis

When evaluating channel mix:
1. Calculate each channel's share of total spend, clicks, conversions, and revenue
2. Compare spend share to revenue share — channels with revenue share > spend share are over-performing; vice versa is under-performing
3. Check for assisted conversions — a channel may look weak on last-touch but be present in most conversion paths
4. Consider minimum viable spend — some channels require a minimum budget floor to function (e.g., Google Search below $1,500/month often can't generate enough data to optimize)

### Budget Reallocation Decision Rule

Recommend reallocation when:
- A channel's CPA is more than 2× the campaign-average CPA with no improving trend
- A channel has been running 3+ weeks and has not hit minimum conversion volume (30+ conversions) needed for platform algorithm learning
- ROAS on a channel is below break-even for 2+ consecutive weeks
- Creative fatigue is confirmed on a channel and new creative is not available to test

Do not recommend reallocation purely based on CPM or CPC differences — conversion-stage metrics (CPA, ROAS) are what matter.

---

## Creative Performance Analyst Framework

### Creative Taxonomy

Before analyzing creative performance, classify all active creative by:

**Format:**
- Static image
- Carousel
- Short video (<15s)
- Long video (15–60s)
- GIF/animation
- UGC/testimonial
- Text-only

**Hook type:**
- Problem-first ("Tired of...")
- Benefit-first ("Grow your X by Y...")
- Social proof ("10,000 customers...")
- Curiosity/question ("The one thing...")
- Before/after ("From X to Y...")
- Contrarian ("Stop doing X...")
- Direct offer ("Get X% off...")
- Story-led ("I used to...")

**Copy angle / value proposition:**
- Speed/ease (saves time, simple)
- Results/outcomes (specific results, proof)
- Status/identity (be the kind of person who...)
- Fear/risk reduction (avoid the downside)
- Community/belonging (join others who...)
- Price/value (best value, affordable)
- Novelty (new, first, breakthrough)

### Creative Fatigue Detection

A creative is experiencing fatigue when:
- CTR has declined more than 30% from its first-week average
- Frequency exceeds 3.5 (Meta) — audience has seen it too many times
- The ad has been running 4+ weeks with no refresh — nearly all creative fatigues by week 4–6
- CVR is declining even as CTR holds — audience is clicking but less convinced

**Fatigue action:** Pause the fatigued creative. Do not reduce budget to it — budget reallocation to fresh creative is more efficient than hoping a fatigued ad recovers.

### Pattern Recognition Method

For top-performing creative (top 20% by primary KPI):
1. List all top performers
2. Look for commonalities in: format, hook type, copy angle, visual approach, offer framing
3. The pattern that appears in 2+ top performers is a signal — not proof, but a testable hypothesis
4. Frame the hypothesis: "Content that leads with [hook type] + [copy angle] appears to outperform — test 3 new variations of this pattern"

For bottom-performing creative (bottom 20% by primary KPI):
1. Same process — look for commonalities in what's not working
2. This defines what to avoid in future creative briefs

### Creative Recommendations Format

Always be specific:

BAD: "Test new creative angles"
GOOD: "The 'before/after results' format is generating 2.1× the CTR of testimonial formats. Recommend briefing 3 new before/after variations with different results angles."

BAD: "Refresh the ads"
GOOD: "Meta Ad Set 'Lookalike 2% — Purchasers' has frequency 4.2 and CTR down 38% from launch week. Pause all 4 creatives in this set. Replace with the winning 'problem-first' static format from the 'Broad Interest' ad set."

### Email Creative Signals

| Metric | Diagnostic Question |
|--------|-------------------|
| Low open rate | Subject line or preview text issue; or deliverability |
| High open, low CTR | Body copy or CTA not compelling; offer mismatch |
| High CTR, low CVR | Post-click experience (landing page) is the problem |
| High unsubscribe | Frequency too high, or wrong audience for this message |
| High open + high CTR + low CVR | Offer or pricing friction; not a creative problem |

Subject line patterns that consistently perform:
- Personalization tokens (name, company, recent behavior)
- Curiosity gaps ("The one thing we changed...")
- Specific numbers ("3 things driving 40% more revenue")
- Urgency with substance ("Last day — and here's why this matters")

Subject line patterns to avoid:
- Generic urgency without substance ("Don't miss out!")
- All caps or excessive punctuation
- Promotional trigger words in spam filters ("FREE", "ACT NOW", "GUARANTEED")
- Subject lines that don't match the email content (high open, immediate unsubscribe signal)

---

## Revenue/ROI Analyst Framework

### Core Revenue Metrics

**Customer Acquisition Cost (CAC)**
CAC = Total marketing spend ÷ New customers acquired

Track CAC by channel and by campaign type. Blended CAC is useful but channel CAC is what you optimize.

**Return on Ad Spend (ROAS)**
ROAS = Revenue attributed to ads ÷ Ad spend

Break-even ROAS = 1 ÷ Gross margin %
Example: If gross margin is 50%, break-even ROAS = 2.0× (every $1 spent must return $2 in revenue)

**LTV:CAC Ratio**
LTV:CAC = Customer lifetime value ÷ Customer acquisition cost

| Ratio | Interpretation |
|-------|---------------|
| < 1:1 | Losing money on every customer |
| 1:1 – 2:1 | Marginal; not sustainable |
| 3:1 | Healthy — standard target for SaaS and e-commerce |
| 5:1+ | Strong; may indicate opportunity to spend more aggressively |
| 10:1+ | Either very efficient or underinvesting in growth |

**Contribution Margin**
Contribution margin = Revenue − COGS − Variable marketing costs
(Excludes fixed overhead)

A campaign can have positive ROAS but negative contribution margin if COGS is high. Always calculate contribution margin when COGS data is available.

### Revenue Attribution Waterfall

When calculating marketing-attributed revenue:
1. Start with total revenue in the period
2. Subtract revenue from customers acquired before the campaign started (not attributable)
3. Remaining = campaign-window new customer revenue
4. Apply channel attribution model to distribute across channels
5. Note: Organic revenue is real but not attributable to paid campaigns — keep separate

### Payback Period

Payback period = CAC ÷ Monthly recurring revenue per customer (for subscription) or CAC ÷ (Average order value × Purchase frequency) for e-commerce

| Payback Period | Interpretation |
|---------------|---------------|
| < 3 months | Excellent — scale aggressively |
| 3–6 months | Good — maintain current pace |
| 6–12 months | Acceptable — focus on improving conversion |
| 12–18 months | Challenging — review pricing, retention, or CAC |
| > 18 months | Unsustainable without strong retention economics |

### ROI Verdict Framework

Present a clear ROI verdict for each campaign:

**Profitable growth:** ROAS above break-even, LTV:CAC above 3:1 → recommend maintaining or scaling spend
**Break-even growth:** ROAS at or near break-even → defensible if building a customer base with strong LTV; concerning if LTV is low
**Loss-leader acceptable:** ROAS below break-even but LTV:CAC is strong → acceptable for acquisition campaigns with high retention; document the assumption
**Unprofitable:** ROAS below break-even AND LTV:CAC below 2:1 → pause and diagnose before spending more

### Strategic Budget Implications

Connect ROI findings to budget strategy:

- If CAC is declining week-over-week: algorithm is learning — do not make major changes; consider increasing budget incrementally (20% per week max to avoid resetting learning)
- If CAC is rising week-over-week: audience saturation or creative fatigue — creative refresh before budget increase
- If ROAS varies significantly by channel: reallocate toward highest-ROAS channels until they show diminishing returns
- If LTV:CAC is strong but growth is slow: underinvesting — model what aggressive spend increase would produce
- If CAC is acceptable but revenue isn't scaling: conversion rate or AOV problem, not a paid media problem

---

## Benchmark Calibration Guide

When no historical baseline exists, use these benchmarks as starting point. Update with actuals after 4 weeks of data.

### Establishing the Baseline (Setup Mode)

1. Start with industry benchmarks from the tables above as initial reference
2. Set "learning period" expectation: first 2–4 weeks of a new campaign are data collection, not optimization
3. After 4 weeks, calculate actuals and update `analytics/benchmarks.md` with real performance ranges
4. After the first full campaign, benchmarks should be based entirely on this brand's historical data — not industry averages

### Benchmark Update Protocol

After each full report cycle, update `analytics/benchmarks.md` with:
- Metric name
- Channel
- Campaign type
- Period
- Actual value
- Whether this was a strong, typical, or weak period
- Notes on what was different (new creative, new audience, seasonal factor)

Over time, this file becomes the most valuable reference in the system — the calibrated expectation for what "good" looks like for this specific brand.
