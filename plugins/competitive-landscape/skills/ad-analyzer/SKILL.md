---
name: ad-analyzer
description: >
  Analyze competitor advertising across Meta (Facebook/Instagram) and Google Ads. Extract themes,
  messaging patterns, creative strategies, spend signals, and trends. Compare across competitors to
  identify gaps and opportunities. Use when the user mentions "analyze ads", "competitor ads",
  "ad analysis", "what ads are they running", "meta ads", "google ads", "facebook ads", "ad trends",
  "ad themes", "messaging analysis", "creative analysis", "ad spend", "ad strategy", or "what are
  competitors advertising". Also triggers on "refresh ad data", "update ad analysis", "compare ads",
  or "ad intelligence".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# Ad Analyzer

Analyze competitor advertising across Meta and Google platforms to extract themes, messaging patterns, creative strategies, and competitive positioning insights.

## Pre-Analysis Setup

1. Read `competitive-landscape/competitors/registry.json` to get the active competitor list.
   - If no registry exists, invoke the `competitor-tracker` skill first.
2. For each active competitor, check for existing ad analysis in `competitive-landscape/competitors/{{id}}/ads/`.
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/ad-analyzer/references/analysis-framework.md` for the complete scoring and categorization system.

## Data Collection

### Meta Ads (Facebook / Instagram)

For each competitor, the user provides ad data through one of these methods:

**Method 1: Ad Library Export (preferred)**
- User provides screenshots, CSV exports, or copy-pasted text from the Meta Ad Library.
- Parse and structure: ad creative text, headline, description, CTA, format (image/video/carousel), active dates, page name.

**Method 2: Manual Input**
- User describes or pastes ad copy they've observed.
- Structure each ad entry with available fields.

**Method 3: Existing Research**
- User provides a document, spreadsheet, or notes with ad observations.
- Parse and normalize into the standard schema.

### Google Ads (Search / Display / Shopping)

For each competitor, the user provides data through:

**Method 1: Ads Transparency Center Export**
- User provides screenshots or text from Google Ads Transparency Center.
- Parse: ad text, format, advertiser name, date range.

**Method 2: Search Result Observations**
- User provides screenshots or descriptions of competitor ads seen in search results.
- Extract: headline, description lines, display URL, extensions, search terms that triggered the ad.

**Method 3: Third-Party Tool Data**
- User provides exports from SEMrush, SpyFu, SimilarWeb, or similar tools.
- Parse and normalize into the standard schema.

## Per-Competitor Ad Analysis

For each competitor, produce a structured analysis saved to `competitive-landscape/competitors/{{id}}/ads/analysis.md`:

```markdown
# {{Competitor Name}} — Ad Analysis

**Last Updated**: {{date}}
**Ads Reviewed**: {{count}}
**Platforms**: Meta, Google

## Overview Stats
- **Total Active Ads (Meta)**: {{count}}
- **Total Ad Formats**: {{breakdown by image/video/carousel}}
- **Google Search Presence**: {{high/medium/low}}
- **Estimated Monthly Ad Volume**: {{range if available}}

## Meta Ads Analysis

### Creative Themes
1. **{{Theme Name}}** ({{% of ads}})
   - Description: {{what this theme is about}}
   - Example headlines: {{2-3 representative headlines}}
   - Visual style: {{description of creative approach}}
   - CTA pattern: {{common CTAs used}}

### Messaging Patterns
- **Primary Value Props**: {{list}}
- **Emotional Hooks**: {{urgency, FOMO, aspiration, etc.}}
- **Promotional Patterns**: {{discount types, offer structures}}
- **Audience Signals**: {{who the ads seem to target}}

### Creative Strategy
- **Format Mix**: {{% image, % video, % carousel}}
- **Copy Length**: {{short/medium/long trend}}
- **Brand vs. Direct Response**: {{ratio}}
- **Landing Page Patterns**: {{where ads link to}}

## Google Ads Analysis

### Search Ad Themes
1. **{{Theme Name}}**
   - Keywords targeted: {{inferred keywords}}
   - Headline patterns: {{common headline structures}}
   - Description patterns: {{common description structures}}
   - Extensions used: {{sitelinks, callouts, structured snippets}}

### Shopping / Display Presence
- **Shopping Ads**: {{yes/no, product categories}}
- **Display Ads**: {{yes/no, observed placements}}
- **Remarketing Signals**: {{any observed remarketing patterns}}

## Key Takeaways
- {{3-5 bullet points of strategic observations}}

## Opportunities for {{Brand Name}}
- {{Specific gaps or angles the brand could exploit}}
```

## Cross-Competitor Comparison

After analyzing individual competitors, produce a comparison saved to `competitive-landscape/analysis/ads/comparison.md`:

```markdown
# Ad Landscape Comparison

**Date**: {{date}}
**Competitors Analyzed**: {{count}}

## Theme Matrix

| Theme | {{Comp 1}} | {{Comp 2}} | {{Comp 3}} | {{Brand}} |
|-------|-----------|-----------|-----------|----------|
| {{theme}} | ✅ Heavy | ⚠️ Light | ❌ None | {{status}} |

## Messaging Comparison

### Value Proposition Overlap
- **Everyone says**: {{common messages across all competitors}}
- **Unique to {{Comp 1}}**: {{differentiating messages}}
- **Unique to {{Comp 2}}**: {{differentiating messages}}
- **Nobody says (opportunity)**: {{gaps in the market}}

### Promotional Strategy Comparison
| Tactic | {{Comp 1}} | {{Comp 2}} | {{Comp 3}} |
|--------|-----------|-----------|-----------|
| Discount frequency | | | |
| Free shipping threshold | | | |
| Urgency tactics | | | |
| Loyalty/rewards | | | |

### Creative Quality Assessment
| Dimension | {{Comp 1}} | {{Comp 2}} | {{Comp 3}} |
|-----------|-----------|-----------|-----------|
| Visual quality | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| Copy sophistication | | | |
| Brand consistency | | | |
| CTA effectiveness | | | |

## Trend Analysis
- **Rising themes**: {{themes appearing more frequently}}
- **Declining themes**: {{themes fading out}}
- **Seasonal patterns**: {{holiday, seasonal, event-driven}}

## Strategic Recommendations
1. **{{Recommendation}}**: {{rationale}}
2. **{{Recommendation}}**: {{rationale}}
3. **{{Recommendation}}**: {{rationale}}
```

## Incremental Updates

When the user provides new ad data:
1. Read existing analysis for the relevant competitor(s).
2. Incorporate new ads into the analysis.
3. Note trends: what's changed since last analysis.
4. Re-run the cross-competitor comparison.
5. Update `last_updated` timestamps.

## Quality Checks

After analysis, verify:
- Every active competitor has an individual analysis file.
- Theme categorization is consistent across competitors (same theme names).
- The comparison matrix includes all active competitors.
- Recommendations are specific and actionable (not generic advice).
- Competitor names match exactly with registry.json entries.
