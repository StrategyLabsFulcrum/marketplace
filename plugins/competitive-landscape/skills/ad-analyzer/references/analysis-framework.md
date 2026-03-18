# Ad Analysis Framework Reference

Scoring rubrics, categorization taxonomy, and analysis templates for structured ad intelligence.

---

## Ad Entry Schema

Each individual ad observed is stored as a structured entry:

```json
{
  "id": "comp-id_platform_NNN",
  "competitor_id": "competitor-slug",
  "platform": "meta|google_search|google_display|google_shopping",
  "captured_date": "YYYY-MM-DD",
  "active_since": "YYYY-MM-DD",
  "format": "image|video|carousel|text|shopping",
  "headline": "...",
  "primary_text": "...",
  "description": "...",
  "cta": "Shop Now|Learn More|Sign Up|Get Offer|...",
  "landing_url": "...",
  "themes": ["theme-slug", ...],
  "offers": {
    "discount_type": "percentage|fixed|bogo|free_shipping|bundle|none",
    "discount_value": "20%",
    "conditions": "min order $99"
  },
  "audience_signals": ["interest-targeting", "remarketing", "lookalike", "broad"],
  "notes": "..."
}
```

---

## Theme Taxonomy

Standard theme categories for consistent cross-competitor comparison:

### Product-Focused Themes
| Slug | Name | Description |
|------|------|-------------|
| `product-showcase` | Product Showcase | Hero shot of product, features highlighted |
| `new-arrival` | New Arrival | Launching or recently added products |
| `best-seller` | Best Seller | Social proof via popularity |
| `product-comparison` | Product Comparison | Side-by-side vs. competitor or previous model |
| `product-demo` | Product Demo | Video/carousel showing product in use |
| `product-bundle` | Bundle/Kit | Multiple products sold together |

### Value & Offer Themes
| Slug | Name | Description |
|------|------|-------------|
| `discount-sale` | Discount/Sale | Percentage or dollar-off promotion |
| `free-shipping` | Free Shipping | Shipping offer as primary hook |
| `flash-sale` | Flash Sale/Limited Time | Urgency-driven promotion |
| `seasonal-sale` | Seasonal Sale | Holiday, end-of-season, event-tied |
| `loyalty-reward` | Loyalty/Rewards | Points, membership, VIP offers |
| `bundle-deal` | Bundle Deal | Save by buying multiple items |

### Brand & Lifestyle Themes
| Slug | Name | Description |
|------|------|-------------|
| `brand-story` | Brand Story | About the brand, mission, heritage |
| `lifestyle` | Lifestyle | Aspirational imagery, brand world |
| `ugc-testimonial` | UGC/Testimonial | Customer photos, reviews, stories |
| `community` | Community | Events, groups, rider culture |
| `behind-scenes` | Behind the Scenes | Manufacturing, team, process |

### Education & Content Themes
| Slug | Name | Description |
|------|------|-------------|
| `how-to` | How-To/Tutorial | Installation guides, tips, advice |
| `buying-guide` | Buying Guide | Help choosing the right product |
| `comparison-guide` | Comparison Guide | Editorial-style product comparison |
| `blog-content` | Blog/Content | Drive traffic to content |

### Competitive & Positioning Themes
| Slug | Name | Description |
|------|------|-------------|
| `competitive-claim` | Competitive Claim | Direct or indirect competitor callout |
| `category-leader` | Category Leadership | "#1 in...", "Most trusted..." |
| `guarantee` | Guarantee/Promise | Satisfaction, fitment, price match |
| `exclusivity` | Exclusivity | "Only at...", proprietary products |

---

## Scoring Rubrics

### Creative Quality Score (1-5)

| Score | Visual Quality | Copy Quality | Overall Impression |
|-------|---------------|-------------|-------------------|
| 5 | Professional photography/video, strong branding, polished | Compelling, clear value prop, emotional hook, strong CTA | Would stop a fast-scrolling user |
| 4 | Good quality visuals, consistent branding | Clear messaging, decent hook, appropriate CTA | Solid, professional ad |
| 3 | Acceptable visuals, some brand elements | Functional copy, value prop present but not compelling | Gets the job done |
| 2 | Low quality or generic stock visuals | Weak or confusing copy, unclear value prop | Forgettable, blends in |
| 1 | Poor visuals, no brand consistency | Bad copy, no clear message or CTA | Actively hurts brand perception |

### Strategic Sophistication Score (1-5)

| Score | Description |
|-------|-------------|
| 5 | Multi-format funnel strategy visible (awareness → consideration → conversion). Clear audience segmentation. Strong retargeting signals. |
| 4 | Mix of brand and DR content. Some funnel structure. Audience targeting evident. |
| 3 | Mostly conversion-focused but with some brand building. Basic targeting. |
| 2 | All ads look the same — single message, single audience. No funnel thinking. |
| 1 | Appears to be boosted posts or minimal effort. No strategy visible. |

### Competitive Threat Level

| Level | Criteria |
|-------|---------|
| **High** | Large ad volume, high creative quality, aggressive offers, strong brand presence, visible retargeting |
| **Medium** | Moderate ad volume, decent creative, standard offers, some brand consistency |
| **Low** | Few active ads, low creative quality, infrequent campaigns, weak brand presence |
| **Emerging** | New or increasing ad activity — may not be high volume yet but showing investment |

---

## Comparison Dimensions

When comparing competitors side-by-side, score across these dimensions:

| Dimension | What to Evaluate |
|-----------|-----------------|
| **Ad Volume** | How many active ads (Meta) / how frequently seen (Google) |
| **Format Diversity** | Range of ad formats used (image, video, carousel, etc.) |
| **Theme Diversity** | Range of themes and messages across their ad portfolio |
| **Offer Aggressiveness** | How heavy on discounts and promotions |
| **Creative Quality** | Average creative quality score across ads |
| **Brand Consistency** | How consistent is visual and messaging identity |
| **Funnel Coverage** | Ads across awareness, consideration, and conversion stages |
| **Platform Coverage** | Presence across Meta, Google Search, Display, Shopping |
| **Landing Page Quality** | Where ads direct traffic and the quality of those pages |
| **Unique Angles** | Any distinctive approaches not seen from others |

---

## Trend Detection

When analyzing ads over time, flag:

1. **New themes appearing**: Competitor testing new messages or audiences.
2. **Themes disappearing**: Competitor abandoning strategies (possible signal of poor performance).
3. **Offer escalation**: Increasing discount depth or frequency.
4. **Creative investment**: Quality improving over time (agency hire, new tools).
5. **Platform shifts**: Moving budget between Meta and Google.
6. **Seasonal patterns**: Recurring campaigns around events, holidays, seasons.
7. **Competitive responses**: Ads that appear to directly counter another brand's messaging.

---

## Output File Locations

| File | Purpose |
|------|---------|
| `competitors/{{id}}/ads/analysis.md` | Per-competitor ad analysis |
| `competitors/{{id}}/ads/meta/` | Raw Meta ad data/screenshots |
| `competitors/{{id}}/ads/google/` | Raw Google ad data/screenshots |
| `analysis/ads/comparison.md` | Cross-competitor comparison |
| `analysis/ads/trends.md` | Trend analysis over time (if multiple snapshots) |
