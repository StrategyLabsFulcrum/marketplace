# Report Templates Reference

Structural templates, data schemas, and design specifications for competitive intelligence reports and dashboards.

---

## Executive Summary Template

The executive summary is a 1-page strategic brief. Maximum 500 words. Decision-maker audience.

### Structure Rules

1. **Opening line**: One sentence stating the brand's competitive position. No preamble.
2. **Position table**: Max 5 dimensions. Use relative language (Leading, Competitive, Behind, Far Behind).
3. **Threats**: Backed by evidence. Each threat has a "so what" — what happens if ignored.
4. **Opportunities**: Backed by evidence. Each opportunity has an expected impact.
5. **Priorities**: Actionable within 30 days. No vague recommendations.

### Position Assessment Scale

| Rating | Meaning | Evidence Required |
|--------|---------|------------------|
| **Leading** | Best in competitive set | Score or metric exceeds all tracked competitors |
| **Competitive** | On par with most competitors | Within 10% of average competitor score |
| **Behind** | Below average for the set | Below most competitors on this dimension |
| **Far Behind** | Significant gap exists | Worst in set AND gap is >30% from leader |

---

## Full Report Template

### Section 1: Executive Summary
(Same as standalone executive summary)

### Section 2: Competitor Profiles

One profile per competitor. 200-300 words each.

```markdown
## {{Competitor Name}}

**Category**: {{direct/indirect/aspirational}}
**Website**: {{url}}
**Threat Level**: {{High/Medium/Low/Emerging}}

### Strengths
- {{Specific strength with evidence}}

### Weaknesses
- {{Specific weakness with evidence}}

### Notable Tactics
- {{Interesting strategies worth monitoring}}

### Risk to {{Brand Name}}
{{1-2 sentences on what this competitor threatens}}
```

### Section 3: Ad Landscape

Pull from `analysis/ads/comparison.md`. Include:
- Theme distribution chart data (for each competitor)
- Messaging comparison highlights
- Creative quality rankings
- Key trend observations

### Section 4: Journey Comparison

Pull from `analysis/journeys/comparison.md`. Include:
- Stage score comparison
- Best-in-class callouts per stage
- Feature comparison matrix (top 15 features)
- Common patterns and outliers

### Section 5: Gap Analysis

For each key dimension, calculate:
```
Gap = Leader Score - Brand Score
Priority = Gap × Business Impact Weight
```

**Business Impact Weights**:
| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Conversion flow | 1.0 | Directly impacts revenue |
| Product page quality | 0.9 | High-intent visitor experience |
| Ad messaging | 0.8 | Top of funnel volume driver |
| Site navigation | 0.7 | Affects all visitors |
| Post-purchase | 0.6 | Retention and LTV |
| Brand perception | 0.5 | Long-term positioning |

### Section 6: Opportunity Map

Organize recommendations into a 2×2 matrix:

```
              LOW EFFORT          HIGH EFFORT
HIGH IMPACT   Quick Wins          Strategic Bets
LOW IMPACT    Easy Adds           Deprioritize
```

Each recommendation includes:
- **Action**: What to do
- **Evidence**: Why (which competitor data supports this)
- **Effort**: Low/Medium/High
- **Impact**: Low/Medium/High
- **Timeline**: This week / This month / This quarter

---

## Dashboard Data Schema

### `data.js` Structure

```javascript
var REPORT_META = {
  brand: "{{brand_name}}",
  generated: "{{ISO date}}",
  competitor_count: N,
  ads_analyzed: N,
  journeys_mapped: N
};

var COMPETITORS = [
  {
    id: "slug",
    name: "Display Name",
    website: "https://...",
    color: "#HEX",
    colorDark: "#HEX",
    category: "direct",
    threat_level: "high|medium|low|emerging",
    overview: {
      strengths: ["...", "..."],
      weaknesses: ["...", "..."],
      notable_tactics: ["...", "..."]
    },
    ads: {
      total_observed: N,
      platforms: ["meta", "google"],
      top_themes: [
        { theme: "Theme Name", percentage: N }
      ],
      creative_quality: N,  // 1-5
      strategic_sophistication: N,  // 1-5
      offer_aggressiveness: "high|medium|low",
      key_messages: ["...", "..."]
    },
    journey: {
      overall_score: N,  // out of 60
      stages: {
        discovery: N,     // out of 10
        browse: N,
        evaluate: N,
        convert: N,
        post_purchase: N,
        retention: N
      },
      highlights: ["...", "..."],
      weaknesses: ["...", "..."],
      unique_tactics: ["...", "..."]
    }
  }
];

var AD_COMPARISON = {
  theme_matrix: {
    "theme-slug": {
      "comp-id": "heavy|moderate|light|none",
      // ...
    }
  },
  messaging_overlap: ["...", "..."],
  messaging_gaps: ["...", "..."],
  trends: [
    { trend: "...", direction: "rising|falling|stable", evidence: "..." }
  ]
};

var JOURNEY_COMPARISON = {
  stage_leaders: {
    discovery: { leader: "comp-id", score: N },
    browse: { leader: "comp-id", score: N },
    // ...
  },
  best_practices: [
    { practice: "...", seen_at: "comp-id", stage: "..." }
  ],
  common_weaknesses: ["...", "..."]
};

var RECOMMENDATIONS = [
  {
    id: N,
    action: "...",
    evidence: "...",
    effort: "low|medium|high",
    impact: "low|medium|high",
    quadrant: "quick-win|strategic-bet|easy-add|deprioritize",
    timeline: "this-week|this-month|this-quarter",
    category: "ads|journey|content|conversion|positioning"
  }
];
```

---

## Dashboard Page Specifications

### Page 1: Overview (`index.html`)

**KPI Row** (4 cards):
- Competitors Tracked: `REPORT_META.competitor_count`
- Ads Analyzed: `REPORT_META.ads_analyzed`
- Journeys Mapped: `REPORT_META.journeys_mapped`
- Last Updated: `REPORT_META.generated`

**Competitor Cards** (grid):
- One card per competitor
- Shows: name, category badge, threat level badge, overall journey score, ad quality score
- Card border-left uses competitor's brand color
- Click expands to show strengths/weaknesses

**Radar Chart** (Chart.js):
- One line per competitor (in their brand color)
- Axes: Ad Volume, Ad Quality, Site UX, Conversion, Post-Purchase, Content
- Include brand's own scores if available

**Quick Links**: Cards linking to Ad Intelligence, Journey Comparison, Strategy pages

### Page 2: Ad Intelligence (`ads.html`)

**Competitor Tabs**: Tab bar with one tab per competitor (brand color underline)

**Per-Competitor View**:
- Theme distribution doughnut chart
- Top 5 themes list with percentage bars
- Key messages card
- Creative quality score visualization (star rating or gauge)
- Strategic sophistication score

**Comparison View** (toggle):
- Theme matrix heatmap table
- Messaging overlap Venn diagram (or list)
- Offer aggressiveness comparison bar chart
- Trend timeline if multiple snapshots exist

### Page 3: Journey Comparison (`journeys.html`)

**Stage Score Bar Chart**: Grouped bar chart, one group per stage, one bar per competitor (brand colors)

**Competitor Journey Cards**: Expandable cards showing per-stage scores and highlights

**Feature Matrix**: Interactive table with checkmarks — competitors across columns, UX features down rows

**Best Practices**: Carousel or card grid of best practices observed, attributed to competitor

### Page 4: Strategy & Actions (`strategy.html`)

**Effort/Impact Matrix**: 2×2 visual quadrant with recommendation dots

**Action Items List**: Filterable by category, effort, impact, timeline. Each item shows:
- Action title
- Evidence summary
- Effort/Impact badges
- Timeline badge
- Checkbox for tracking

**Gap Analysis Bars**: Horizontal bar chart showing gap size per dimension

**30/60/90 Day Timeline**: Visual timeline with recommendations plotted by deadline

---

## Netlify Deployment Files

### `_headers`
```
/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
```

### `_redirects`
```
/ /index.html 200
```

---

## File Output Structure

```
competitive-landscape/reports/
├── executive-summary.md
├── full-report.md
├── dashboard/
│   ├── index.html
│   ├── ads.html
│   ├── journeys.html
│   ├── strategy.html
│   ├── data.js
│   ├── theme.css          (optional — shared styles)
│   ├── _headers
│   └── _redirects
└── config.md               (generation metadata)
```
