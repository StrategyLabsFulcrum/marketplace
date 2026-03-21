# CRO Benchmarks & Industry Standards

Reference data for conversion rate optimization. Use to contextualize performance, set realistic targets, and prioritize where to focus optimization effort.

---

## E-Commerce Conversion Rate Benchmarks

### Overall Site Conversion Rate (visits to purchase)

| Industry | Low | Average | Top quartile |
|----------|-----|---------|-------------|
| Apparel & Fashion | 1.0% | 2.0% | 3.5%+ |
| Health & Beauty | 1.5% | 3.0% | 5.0%+ |
| Sports & Outdoors | 0.8% | 1.8% | 3.0%+ |
| Home & Garden | 1.0% | 2.0% | 3.5%+ |
| Food & Beverage | 1.5% | 3.5% | 5.5%+ |
| Electronics | 0.6% | 1.4% | 2.5%+ |
| Luxury / High-AOV | 0.3% | 0.8% | 1.5%+ |
| Subscriptions / SaaS | 2.0% | 5.0% | 10.0%+ |

*Note: These are site-wide averages. Landing page CVR for paid traffic is typically higher (3–8%) because the audience is pre-qualified by ad targeting.*

### Traffic Source Conversion Rates

| Traffic Source | Typical CVR Range |
|---------------|-------------------|
| Email (existing customers) | 4–10% |
| Organic search | 2–4% |
| Paid social (retargeting) | 2–6% |
| Paid social (prospecting) | 0.5–2% |
| Paid search (branded) | 3–8% |
| Paid search (non-branded) | 1–3% |
| Direct | 3–6% |
| Referral | 1–3% |
| Organic social | 0.5–1.5% |

---

## Funnel Stage Benchmarks

### Landing Page

| Metric | Below average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| Bounce rate | 80%+ | 55–70% | 40–55% | Under 40% |
| Time on page | Under 30 sec | 1–2 min | 2–3 min | 3+ min |
| Scroll depth (50%+) | Under 40% | 50–60% | 60–75% | 75%+ |
| CTA click rate | Under 2% | 3–5% | 6–10% | 10%+ |
| CVR (paid traffic) | Under 1.5% | 2–4% | 4–8% | 8%+ |

### Product Page

| Metric | Below average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| Add-to-cart rate | Under 5% | 8–12% | 12–18% | 18%+ |
| CVR (all traffic) | Under 1% | 1.5–3% | 3–5% | 5%+ |

### Cart & Checkout

| Metric | Below average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| Cart abandonment rate | 80%+ | 70–75% | 60–70% | Under 60% |
| Cart-to-checkout rate | Under 30% | 35–45% | 45–55% | 55%+ |
| Checkout completion rate | Under 45% | 55–65% | 65–75% | 75%+ |

### Email

| Metric | Below average | Average | Good | Excellent |
|--------|--------------|---------|------|-----------|
| Open rate | Under 15% | 20–30% | 30–40% | 40%+ |
| Click rate | Under 1.5% | 2–4% | 4–7% | 7%+ |
| Click-to-open rate | Under 8% | 10–15% | 15–25% | 25%+ |
| Unsubscribe rate | Over 0.5% | 0.1–0.3% | Under 0.1% | |

---

## A/B Testing Statistical Standards

### Minimum Standards for Declaring a Winner

| Threshold | Value | Why |
|-----------|-------|-----|
| Statistical significance | p < 0.05 | 95% confidence the result isn't random |
| Minimum sample size | 100 conversions per variant | Below this, results are unreliable |
| Minimum test duration | 14 days | Captures weekly behavioral cycles |
| Minimum relative lift to act | 10% | Smaller lifts may not justify implementation cost |

### Sample Size Quick Reference

*For 95% confidence, 80% power, detecting a 20% relative lift:*

| Baseline CVR | Daily visitors needed (per variant) | Days at 1K/day | Days at 5K/day |
|-------------|--------------------------------------|----------------|----------------|
| 1% | ~8,500 total | 17 days | 4 days |
| 2% | ~4,250 total | 9 days | 2 days |
| 3% | ~2,800 total | 6 days | 2 days |
| 5% | ~1,700 total | 4 days | 1 day |
| 10% | ~850 total | 2 days | <1 day |

*Always run for minimum 14 days regardless, to account for day-of-week effects.*

### Common A/B Testing Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| Peeking (stopping early when you see significance) | False positives — you declare a winner that isn't one | Commit to sample size before starting |
| Testing too many things at once | Can't know what caused the result | Change one variable per A/B test |
| Insufficient sample size | Results are noise, not signal | Calculate sample size before starting |
| Running test less than 14 days | Misses weekly cycles | Enforce minimum duration rule |
| Ignoring secondary metrics | A win on CVR might cause a loss on AOV or LTV | Always track revenue per visitor, not just CVR |
| Not segmenting results | A win overall may be a loss on mobile | Analyze by device, traffic source, new vs returning |

---

## Page Speed Benchmarks

Page speed is the fastest-impact CRO lever — every 1-second delay reduces conversions.

| Metric | Poor | Needs work | Good | Excellent |
|--------|------|-----------|------|-----------|
| Largest Contentful Paint (LCP) | Over 4s | 2.5–4s | 1.5–2.5s | Under 1.5s |
| First Input Delay (FID) | Over 300ms | 100–300ms | Under 100ms | Under 50ms |
| Cumulative Layout Shift (CLS) | Over 0.25 | 0.1–0.25 | Under 0.1 | Under 0.05 |

**Impact of page speed on CVR:**
- +1 second load time → -7% conversions (general benchmark)
- Mobile load time under 3 seconds = baseline requirement
- Moving from 3 seconds to 1 second load time can increase conversions by 10–30%

---

## Trust Signal Impact

Trust signals have measurable conversion impact when added to pages that previously lacked them:

| Trust Signal | Typical CVR Lift When Added |
|-------------|----------------------------|
| Money-back guarantee badge near CTA | +5–15% |
| SSL / secure checkout badge | +3–8% |
| Star rating + review count on product page | +8–20% |
| Press logos ("As seen in...") | +5–12% |
| Real photos of customers using product | +10–25% |
| Specific testimonial with photo + name | +8–18% |
| Live inventory / "X left in stock" (genuine) | +5–15% |

*Ranges are generalizations across industry studies. Test all trust signals in your specific context.*

---

## Cart Abandonment Recovery Benchmarks

| Channel | Recovery rate | Notes |
|---------|--------------|-------|
| Email (3-part sequence, 1hr / 24hr / 72hr) | 5–15% of abandoned carts | Most impactful recovery channel |
| SMS (with prior consent) | 8–20% of abandoned carts | Higher open rate than email |
| Paid retargeting (Meta/Google) | 3–8% recovery ROAS | Depends on audience size |
| Browser push notifications | 2–6% | Requires opt-in; declining use |

### Abandoned Cart Email Timing

| Email | Send time | Open rate benchmark | CVR benchmark |
|-------|-----------|-------------------|---------------|
| Email 1 | 1 hour after abandon | 35–50% | 3–5% |
| Email 2 | 24 hours | 25–35% | 2–4% |
| Email 3 (with offer) | 72 hours | 20–30% | 3–6% |

---

## CRO ROI Framework

Use to prioritize test investments:

**Revenue impact of a CVR improvement:**
```
Revenue impact = Monthly visitors × Current CVR × AOV × Lift %
```

Example:
- 50,000 monthly visitors to landing page
- 3% current CVR → 1,500 conversions/month
- $80 AOV → $120,000 monthly revenue
- A 20% relative CVR lift (3% → 3.6%) → 300 additional conversions/month
- Revenue impact: 300 × $80 = **$24,000/month**

This is why CRO compounds: the same traffic produces more revenue with no additional ad spend.
