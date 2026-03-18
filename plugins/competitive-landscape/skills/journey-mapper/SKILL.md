---
name: journey-mapper
description: >
  Map and analyze customer journeys on competitor websites. Document conversion funnels, UX patterns,
  CTAs, navigation flows, content strategy, and friction points. Use when the user mentions "map
  journey", "customer journey", "competitor site analysis", "competitor UX", "conversion funnel",
  "how does their site work", "site walkthrough", "competitor experience", "journey analysis",
  "compare websites", or "site teardown". Also triggers on "update journeys", "refresh journey
  analysis", "what's their funnel", or "how do they convert customers".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# Journey Mapper

Map customer journeys across competitor websites — from first touch through conversion and post-purchase. Document UX patterns, conversion funnels, content strategy, and friction points to identify opportunities for the brand.

## Pre-Analysis Setup

1. Read `competitive-landscape/competitors/registry.json` for active competitors.
   - If no registry exists, invoke the `competitor-tracker` skill first.
2. For each competitor, check for existing journey data in `competitive-landscape/competitors/{{id}}/journeys/`.
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/journey-mapper/references/journey-framework.md` for the analysis structure and scoring system.

## Data Collection

Journey data comes from the user through these methods:

### Method 1: Site Walkthrough Notes
The user describes their experience navigating a competitor's website. Capture:
- Pages visited and in what order
- First impressions of homepage
- Navigation structure and ease of finding products
- Product page experience
- Cart and checkout flow
- Trust signals encountered
- Friction points and delights

### Method 2: Screenshots / Screen Recordings
User provides screenshots or describes key pages. Extract:
- Layout patterns and visual hierarchy
- CTAs (text, placement, design)
- Navigation structure
- Content types and density
- Mobile vs desktop differences

### Method 3: Documented Research
User provides notes, documents, or structured observations about competitor sites. Parse and normalize.

### Method 4: User-Reported Experience
User shares their own buying experience or customer feedback about competitor sites.

## Journey Stages

Map each competitor through these standard stages:

### 1. Discovery / First Touch
- **How users find the site**: Paid ads, organic search, social, referral, direct
- **Landing page experience**: What does the first page communicate?
- **First impression**: Professional? Trustworthy? Clear value prop?
- **Time to value**: How quickly does the user understand what the brand offers?

### 2. Browse / Explore
- **Navigation structure**: Category hierarchy, mega menu, search quality
- **Product discovery**: How easy is it to find what you want?
- **Filtering / sorting**: Available options, usability
- **Content depth**: Product descriptions, specs, guides, blog
- **Social proof**: Reviews, ratings, UGC placement

### 3. Evaluate / Compare
- **Product page quality**: Images, descriptions, specs, videos
- **Comparison tools**: Any built-in comparison features?
- **Fitment / compatibility**: How do they handle fitment (if applicable)?
- **Pricing transparency**: Clear pricing? Hidden costs?
- **Trust signals**: Warranties, guarantees, certifications, reviews

### 4. Convert / Purchase
- **Add to cart flow**: Smooth? Upsells? Cross-sells?
- **Cart experience**: Clear summary? Easy to modify?
- **Checkout steps**: How many steps? Guest checkout?
- **Payment options**: Credit card, PayPal, financing, BNPL?
- **Shipping options**: Speed, cost, transparency
- **Friction points**: Where might a user abandon?

### 5. Post-Purchase
- **Order confirmation**: Email quality, tracking info
- **Shipping communication**: Updates, tracking experience
- **Unboxing / delivery**: Packaging, inserts, extras
- **Follow-up**: Review requests, cross-sell emails, loyalty program
- **Support access**: How easy to get help? Returns process?

### 6. Retention / Loyalty
- **Email marketing**: Frequency, quality, personalization
- **Loyalty programs**: Points, tiers, rewards
- **Community**: Forums, social groups, events
- **Remarketing**: Ad frequency, messaging after purchase
- **Repeat purchase UX**: Reorder ease, saved info, recommendations

## Per-Competitor Journey Output

Save to `competitive-landscape/competitors/{{id}}/journeys/analysis.md`:

```markdown
# {{Competitor Name}} — Customer Journey Analysis

**Last Updated**: {{date}}
**Website**: {{url}}

## Journey Score: {{X}}/10

## Stage Breakdown

### 1. Discovery (Score: {{X}}/10)
- **Primary acquisition channels**: {{list}}
- **Landing page effectiveness**: {{assessment}}
- **Key observations**: {{bullet points}}
- **Screenshots/Evidence**: {{references}}

### 2. Browse & Explore (Score: {{X}}/10)
- **Navigation quality**: {{assessment}}
- **Product discovery ease**: {{assessment}}
- **Content depth**: {{assessment}}
- **Key observations**: {{bullet points}}

### 3. Evaluate & Compare (Score: {{X}}/10)
- **Product page quality**: {{assessment}}
- **Trust signals**: {{assessment}}
- **Pricing transparency**: {{assessment}}
- **Key observations**: {{bullet points}}

### 4. Convert & Purchase (Score: {{X}}/10)
- **Checkout flow**: {{assessment}}
- **Payment options**: {{list}}
- **Friction points**: {{bullet points}}
- **Key observations**: {{bullet points}}

### 5. Post-Purchase (Score: {{X}}/10)
- **Communication quality**: {{assessment}}
- **Support access**: {{assessment}}
- **Key observations**: {{bullet points}}

### 6. Retention & Loyalty (Score: {{X}}/10)
- **Loyalty program**: {{description or "None observed"}}
- **Email strategy**: {{assessment}}
- **Key observations**: {{bullet points}}

## UX Highlights
- {{Things this competitor does exceptionally well}}

## UX Weaknesses
- {{Clear friction points or missed opportunities}}

## Unique Tactics
- {{Anything distinctive not seen from other competitors}}

## Opportunities for {{Brand Name}}
- {{Specific things the brand could do better than this competitor}}
```

## Cross-Competitor Journey Comparison

After mapping individual journeys, produce `competitive-landscape/analysis/journeys/comparison.md`:

```markdown
# Customer Journey Landscape Comparison

**Date**: {{date}}
**Competitors Mapped**: {{count}}

## Overall Journey Scores

| Competitor | Discovery | Browse | Evaluate | Convert | Post-Purchase | Retention | **Total** |
|-----------|-----------|--------|----------|---------|---------------|-----------|-----------|
| {{Comp 1}} | X/10 | X/10 | X/10 | X/10 | X/10 | X/10 | **X/60** |
| {{Comp 2}} | X/10 | X/10 | X/10 | X/10 | X/10 | X/10 | **X/60** |

## Stage-by-Stage Leader

| Stage | Best | Why | Worst | Why |
|-------|------|-----|-------|-----|
| Discovery | {{name}} | {{reason}} | {{name}} | {{reason}} |

## Common Patterns
- {{Patterns seen across multiple competitors}}

## Differentiation Opportunities
- {{Where the brand can stand out from ALL competitors}}

## Best Practices to Adopt
- {{Specific tactics worth borrowing, with attribution}}

## Pitfalls to Avoid
- {{Mistakes competitors make that the brand should skip}}
```

## Incremental Updates

When the user provides new journey observations:
1. Update the relevant competitor's journey analysis.
2. Re-score affected stages.
3. Re-run the cross-competitor comparison.
4. Note what changed since last analysis.

## Quality Checks

- Every active competitor has a journey analysis file.
- All 6 stages are scored (even if limited data — note "insufficient data" vs. a low score).
- Comparison table includes all active competitors.
- Recommendations reference specific evidence, not generic advice.
- Journey scores are calibrated consistently across competitors.
