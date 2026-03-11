# Analysis Framework Reference

Complete taxonomy, scoring rubrics, and aggregation rules for call analysis. The analyze-calls skill uses this as the analytical backbone.

---

## Call Classification Taxonomy

### Primary Categories

Assign each call exactly ONE primary category:

| Category | Trigger Keywords / Patterns |
|----------|---------------------------|
| Product Inquiry | asking about products, specs, compatibility, availability, features |
| Technical Support | troubleshooting, installation help, product not working, how-to |
| Order Support | order status, shipping, tracking, returns, exchanges, cancellations |
| Pricing & Quotes | pricing questions, bulk discounts, custom quotes, price matching |
| Pre-Purchase Research | comparing products, fitment questions before buying, "which one should I get" |
| Post-Purchase Follow-up | feedback after purchase, review follow-up, satisfaction check |
| Complaint | dissatisfaction, escalation, demanding resolution, negative experience |
| General Inquiry | store hours, location, general brand questions, not fitting other categories |

### Tag Vocabulary

Apply ALL relevant tags (a call can have multiple tags):

| Tag | Description | Trigger Patterns |
|-----|-------------|-----------------|
| `fitment` | Vehicle fitment or compatibility | "will this fit", "compatible with", year/make/model questions |
| `stock` | Inventory or availability | "in stock", "when available", "back order", "out of stock" |
| `custom` | Custom builds or modifications | "custom", "build", "modify", "fabricate", "one-off" |
| `pricing` | Price-related discussion | "how much", "price", "cost", "discount", "deal" |
| `install` | Installation questions | "install", "mount", "bolt on", "instructions", "difficulty" |
| `info` | General product information | "tell me about", "what's the difference", "specs" |
| `shipping` | Shipping or delivery | "ship", "delivery", "freight", "arrive", "tracking" |
| `returns` | Returns or exchanges | "return", "exchange", "refund", "warranty", "defective" |
| `nav` | Website navigation issues | "can't find", "where is", "hard to navigate", "search doesn't work" |
| `competitor` | Competitor mentioned | any competitor brand name mentioned |

---

## Sentiment Scoring

### Per-Call Sentiment

Rate each call on a 4-point scale:

| Score | Label | Criteria |
|-------|-------|----------|
| 4 | `positive` | Caller is satisfied, complimentary, enthusiastic. Uses positive language. |
| 3 | `neutral` | Straightforward transaction, no strong emotion either way. |
| 2 | `mixed` | Some positive and some negative signals. Frustration resolved, or satisfaction with caveats. |
| 1 | `negative` | Caller is frustrated, angry, disappointed. Unresolved issues, complaints. |

### Key Emotion Detection

Identify the dominant emotion:

| Emotion | Indicators |
|---------|-----------|
| Frustration | Repeated attempts, "I've been trying", sighs, raised voice cues, "nobody can help" |
| Excitement | "I can't wait", enthusiastic tone, rapid questions about features |
| Confusion | "I don't understand", repeated clarification requests, "what does that mean" |
| Satisfaction | "That's perfect", "exactly what I needed", "thank you so much" |
| Urgency | "I need this ASAP", "race is this weekend", time pressure language |
| Disappointment | "I was hoping", "that's too bad", "I expected better" |
| Anxiety | "I'm worried about", "what if it doesn't fit", risk-averse language |

### Aggregate Sentiment Calculation

For dashboard KPIs, compute average sentiment as a numeric score (1-4 scale), then display as:
- 3.5+ → "Positive" (green)
- 2.5-3.49 → "Neutral" (gray)
- 1.5-2.49 → "Mixed" (yellow)
- Below 1.5 → "Negative" (red)

---

## Resolution Classification

| Status | Criteria |
|--------|----------|
| `resolved` | Caller's primary need was fully addressed. They got their answer, placed their order, or received a solution. |
| `partial` | Some needs addressed but not all. Caller left with outstanding questions or pending follow-up. |
| `unresolved` | Primary need was NOT addressed. Caller disconnected unsatisfied, issue was escalated with no resolution, or the call was abandoned. |

---

## Opportunity Scoring

### Frequency × Impact Matrix

Score each identified opportunity (pain point, feature request, common question) on two axes:

**Frequency Score** (how often it comes up):
| Score | Criteria |
|-------|----------|
| 5 | 25%+ of calls mention this |
| 4 | 15-24% of calls |
| 3 | 8-14% of calls |
| 2 | 3-7% of calls |
| 1 | Under 3% of calls |

**Impact Score** (how much fixing it would improve the business):
| Score | Criteria |
|-------|----------|
| 5 | Directly prevents lost sales or customer churn |
| 4 | Significantly improves customer experience or reduces call volume |
| 3 | Moderate improvement to operations or satisfaction |
| 2 | Nice-to-have improvement |
| 1 | Minor or cosmetic |

**Combined Score** = Frequency × Impact (max 25)

Rank opportunities by combined score for the dashboard.

### Priority Assignment

Based on combined score and effort:

| Priority | Criteria |
|----------|----------|
| `critical` | Score 20-25, or any single call with escalation/churn risk |
| `high` | Score 12-19 |
| `quick-win` | Score 6-11 AND estimated low effort (content change, simple fix) |
| `medium` | Score 6-11 AND higher effort |

---

## Competitor Analysis Framework

### Mention Extraction

For each competitor mention, capture:

| Field | Description |
|-------|-------------|
| Competitor Name | Normalized name (e.g., "SuperATV" not "super atv" or "Super ATV") |
| Context | Why they were mentioned (price comparison, feature comparison, switching from, etc.) |
| Sentiment | How the caller feels about the competitor (positive, negative, neutral) |
| Dimension | What aspect was compared (price, quality, selection, website, service, shipping) |
| Quote | Verbatim quote if available |

### Competitor Normalization

Common brand name variations to normalize:

| Canonical | Variations |
|-----------|-----------|
| SuperATV | Super ATV, super atv, SATV |
| RevZilla | Rev Zilla, revzilla, Zilla |
| Four Wheel Parts | 4 Wheel Parts, 4WP, Four Wheeler Parts |
| CageWRX | Cage WRX, CageWorx, Cage Works |

Add new normalizations as encountered. If a brand name is ambiguous, include the verbatim mention and flag for review.

### Counter-Positioning Analysis

For each competitor, classify mentions into:

| Category | Description |
|----------|-------------|
| Brand Wins | Areas where callers prefer our brand over the competitor |
| Brand Loses | Areas where callers prefer the competitor |
| Parity | Areas where callers see no meaningful difference |
| Gaps | Features/services the competitor offers that callers wish our brand had |

---

## Website Issue Classification

### Issue Categories

| Category | Examples |
|----------|---------|
| Navigation | Can't find products, confusing menu structure, poor search results |
| Product Pages | Missing specs, unclear fitment info, not enough photos, confusing options |
| Checkout | Cart issues, payment problems, shipping calculation errors, coupon problems |
| Mobile | Site doesn't work well on phone, buttons too small, images don't load |
| Content | Missing installation guides, unclear product descriptions, outdated info |
| Trust | No reviews, unclear return policy, missing contact info, looks dated |

### Impact Estimation

For each site issue, estimate:
- **Call deflection potential**: If fixed, what percentage of related calls could be avoided?
- **Revenue impact**: Does this issue directly prevent purchases?
- **Effort level**: Low (content update), Medium (design change), High (development work)

---

## Journey Stage Classification

Map each call to a customer journey stage:

| Stage | Indicators |
|-------|-----------|
| Awareness | "I just heard about you", "someone recommended", "saw your ad" |
| Research | "I'm looking into", "tell me about", "what's the difference between" |
| Consideration | "I'm comparing", "how do you compare to", "I'm deciding between" |
| Decision | "I'm ready to buy", "I want to order", "what's the best option for" |
| Purchase | Active order placement, payment processing, confirmation |
| Post-Purchase | "I just received", "how do I install", "it doesn't fit", follow-up |
| Support | Troubleshooting, warranty claims, returns, complaints |
| Advocacy | "I love your products", "I recommend you to everyone", repeat caller |

### Journey Trigger Detection

Identify what triggered the call:
- **Search**: "I was searching online and..."
- **Social**: "I saw on Instagram/YouTube/Facebook..."
- **Referral**: "My buddy/mechanic/forum recommended..."
- **Ad**: "I saw your ad on..."
- **Repeat**: "I've ordered from you before..."
- **Competitor spillover**: "I was looking at [competitor] but..."

---

## Aggregation Rules

When combining individual call analyses into the 4 output files:

1. **Percentages**: Always relative to total calls analyzed. Round to nearest whole number.
2. **Rankings**: Sort by combined frequency × impact score, descending.
3. **Quotes**: Select the most representative 2-3 quotes per topic. Prefer quotes that are concise and illustrative.
4. **Deduplication**: Merge similar opportunities/issues. E.g., "can't find fitment info" and "fitment guide is hard to find" are the same issue.
5. **Trend detection**: If call dates span 3+ weeks, compute week-over-week trends for volume and sentiment.
6. **Minimum threshold**: Only surface opportunities/issues that appear in 2+ calls (unless a single call reveals a critical issue like a bug or safety concern).
7. **Timestamps**: Every aggregated output file must include "Last updated: [ISO date], Total calls analyzed: [N]" at the top.
