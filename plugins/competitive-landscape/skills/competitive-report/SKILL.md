---
name: competitive-report
description: >
  Generate competitive intelligence reports and deployable dashboards from tracked competitor data.
  Produces side-by-side comparisons, gap analysis, strategic recommendations, and interactive HTML
  reports. Use when the user mentions "generate report", "competitive report", "build dashboard",
  "competitor dashboard", "comparison report", "competitive analysis report", "landscape report",
  "export analysis", "create comparison", or "build the report". Also triggers on "update report",
  "refresh dashboard", "package for deploy", or "create a competitive overview".
allowed-tools: Read, Write, Edit, Bash, Glob, Agent
---

# Competitive Report Generator

Build structured reports and deployable HTML dashboards from the competitor tracking, ad analysis, and journey mapping data collected by the other competitive-landscape skills.

## Pre-Generation

1. Read `competitive-landscape/competitors/registry.json` for the active competitor roster.
2. Read all per-competitor analysis files:
   - `competitors/{{id}}/ads/analysis.md` (from ad-analyzer)
   - `competitors/{{id}}/journeys/analysis.md` (from journey-mapper)
   - `competitors/{{id}}/profile.md` (from competitor-tracker)
3. Read cross-competitor comparisons:
   - `analysis/ads/comparison.md`
   - `analysis/journeys/comparison.md`
4. Read `${CLAUDE_PLUGIN_ROOT}/skills/competitive-report/references/report-templates.md` for the output structure.
5. Create output directory: `competitive-landscape/reports/`.

## Report Types

### 1. Executive Summary Report (`reports/executive-summary.md`)

A concise strategic overview for decision-makers.

```markdown
# Competitive Landscape — Executive Summary

**Brand**: {{brand_name}}
**Date**: {{date}}
**Competitors Tracked**: {{count}}

## Competitive Position at a Glance

| Dimension | {{Brand}} Position | Leader | Gap |
|-----------|-------------------|--------|-----|
| Ad Volume | {{position}} | {{leader}} | {{gap description}} |
| Ad Quality | {{position}} | {{leader}} | {{gap description}} |
| Site Experience | {{position}} | {{leader}} | {{gap description}} |
| Conversion Flow | {{position}} | {{leader}} | {{gap description}} |
| Post-Purchase | {{position}} | {{leader}} | {{gap description}} |

## Top 3 Threats
1. **{{Threat}}**: {{description and evidence}}
2. **{{Threat}}**: {{description and evidence}}
3. **{{Threat}}**: {{description and evidence}}

## Top 3 Opportunities
1. **{{Opportunity}}**: {{description and rationale}}
2. **{{Opportunity}}**: {{description and rationale}}
3. **{{Opportunity}}**: {{description and rationale}}

## Recommended Priorities (Next 30 Days)
1. {{Action item with expected impact}}
2. {{Action item with expected impact}}
3. {{Action item with expected impact}}
```

### 2. Full Competitive Report (`reports/full-report.md`)

Comprehensive analysis combining all data sources.

**Sections**:
1. **Executive Summary** — Key findings and recommendations
2. **Competitor Profiles** — One page per competitor with overview, strengths, weaknesses
3. **Ad Landscape** — Cross-competitor ad analysis, theme comparison, creative assessment
4. **Journey Comparison** — Stage-by-stage UX comparison across competitors
5. **Gap Analysis** — Where the brand under-indexes vs. the competitive set
6. **Opportunity Map** — Prioritized list of actions organized by effort and impact
7. **Appendix** — Raw data tables, scoring details, methodology notes

### 3. Interactive HTML Dashboard

Generate a deployable multi-page HTML dashboard for visual consumption of competitive intelligence.

#### Dashboard Pages

**Page 1: Competitive Overview (`index.html`)**
- KPI row: Competitors tracked, total ads analyzed, journeys mapped, last updated
- Competitor cards: Photo/logo placeholder, name, category, threat level, key stats
- Radar chart: Multi-axis comparison across key dimensions
- Quick-action links to detailed pages

**Page 2: Ad Intelligence (`ads.html`)**
- Per-competitor ad breakdown with theme distribution charts
- Side-by-side messaging comparison table
- Creative quality scores visualization
- Theme matrix heatmap
- Trend timeline (if multiple analysis snapshots exist)
- Strategic recommendations section

**Page 3: Journey Comparison (`journeys.html`)**
- Stage-by-stage score comparison bar chart
- Per-competitor journey cards with stage scores
- Best practices carousel
- UX feature comparison matrix (interactive checkboxes)
- Friction points and opportunities callouts

**Page 4: Strategy & Actions (`strategy.html`)**
- Prioritized action items with effort/impact matrix
- Gap analysis visualization
- 30/60/90 day recommendation timeline
- Competitive positioning map (2x2 quadrant)
- Win/loss themes summary

#### Dashboard Design System

Follow the same design language as the CDO dashboard for consistency:

- **Color palette**: Dark navy (`#1B2A3D`), burnt orange accent (`#D4782F`), warm beige background (`#F5F0EB`), white cards
- **Typography**: System font stack, with Barlow Condensed for display if `theme.css` is available
- **Components**: KPI cards, competitor cards with brand colors, Chart.js charts, comparison tables, action item cards
- **Navigation**: Shared nav bar across all pages with brand name and 4 page links
- **Responsive**: CSS Grid with responsive breakpoints
- **Self-contained**: Each HTML file has inline CSS/JS. Only external dependency is Chart.js CDN.

#### Shared Navigation

```html
<nav class="site-nav">
  <a href="index.html" class="nav-brand">{{BRAND_NAME}}</a>
  <a href="index.html" class="nav-link">📊 Overview</a>
  <a href="ads.html" class="nav-link">📢 Ad Intelligence</a>
  <a href="journeys.html" class="nav-link">🗺 Journey Comparison</a>
  <a href="strategy.html" class="nav-link">🎯 Strategy & Actions</a>
</nav>
```

#### Data Architecture

Extract all dynamic data into a shared `data.js` file loaded by each page:

```javascript
var COMPETITORS = [ /* competitor objects from registry */ ];
var AD_ANALYSIS = { /* per-competitor ad themes, scores, comparisons */ };
var JOURNEY_SCORES = { /* per-competitor stage scores */ };
var RECOMMENDATIONS = [ /* prioritized action items */ ];
```

This keeps pages lightweight and makes updates easy — regenerate `data.js` and pages update automatically.

## Post-Generation

1. Create `_headers` and `_redirects` files for Netlify deployment.
2. Offer to create a deploy zip: `zip -r competitive-report.zip reports/dashboard/`
3. Provide links to each generated file.
4. Update `competitive-landscape/reports/config.md` with generation timestamp.

## Incremental Updates

When re-generating after new analysis:
- Re-read all analysis files (they contain updated data).
- Regenerate all report files and dashboard pages.
- Note in each output: "Last updated: {{date}}"

## CDO Integration

If the `customer-driven-optimizations` plugin is also installed:
- Cross-reference competitor mentions from call analysis with ad/journey data.
- Include a "Voice of Customer" section in reports showing what customers say about competitors.
- Link to the CDO dashboard's competitor and journey pages where relevant.
- The competitive-landscape dashboard can serve as the competitor-focused companion to the CDO call intelligence dashboard.
