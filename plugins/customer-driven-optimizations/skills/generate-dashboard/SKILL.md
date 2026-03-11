---
name: generate-dashboard
description: >
  Generate a deployable 4-page HTML dashboard from call analysis data. Produces Call Intelligence,
  Competitor Intel, Site Changes, and Customer Journeys pages with interactive charts, data tables,
  and action items. Use when the user mentions "generate dashboard", "build dashboard", "update
  dashboard", "create report", "deploy dashboard", "make the dashboard", "refresh dashboard",
  "export analysis", or "build the HTML pages". Also triggers on "create deploy zip", "package
  for Netlify", or "update the site".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Dashboard Generator

Build a 4-page static HTML dashboard from the structured analysis files in `customer-driven-optimizations/analysis/`. Each page is a self-contained HTML file with inline CSS and JavaScript — no external dependencies except Chart.js CDN.

## Pre-Generation

1. Read `customer-driven-optimizations/brand-context.md` for brand name, competitors, and colors.
2. Read all 4 analysis output files from `customer-driven-optimizations/analysis/`.
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/generate-dashboard/references/design-system.md` for the complete CSS specification.
4. Read `${CLAUDE_PLUGIN_ROOT}/skills/generate-dashboard/references/page-templates.md` for the structural blueprint of each page.
5. Create the output directory: `customer-driven-optimizations/dashboard/`.

## Design System

All pages share a consistent design system defined in the design-system reference. Key principles:

- **Color palette**: Dark navy (`#1B2A3D`), burnt orange accent (`#D4782F`), warm beige background (`#F5F0EB`), white cards.
- **Typography**: System font stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`).
- **Components**: KPI cards, opportunity cards with expandable details, Chart.js charts, sortable/filterable data tables, tag system, modal overlays.
- **Navigation**: Shared site-nav bar across all pages with brand name and 4 page links.
- **Responsive**: Grid layouts with responsive breakpoints.

The brand name in the nav and headers should use the value from `brand-context.md`. If no brand context exists, use "Customer Intelligence" as the default.

## Page Generation

### Page 1: Call Intelligence Dashboard (`index.html`)

The main overview page. Structure:
- **Header**: Brand name, total calls badge, date range, "Analyze New Calls" button (modal trigger).
- **KPI Row**: 5 cards — Total Calls, Top Issue %, Resolution Rate, Avg Sentiment, Action Items.
- **Top Opportunities**: Grid of expandable opportunity cards ranked by frequency × impact. Each card shows rank, title, percentage, call count, stats, and expandable recommendation.
- **Charts Row**: 2 Chart.js charts — Category Distribution (doughnut) and Call Volume Trend (line).
- **Call Log Table**: Sortable, filterable, paginated table of all calls with search, category filter, expand for details.
- **Action Items Section**: Filterable action cards with priority levels (critical, high, quick-win, medium), checkboxes, and expandable details.
- **Import Modal**: Drop zone UI for new file analysis (triggers the analyze-calls skill concept).

Data source: `analysis/call-intelligence.md` + `analysis/raw/call-*.md`.

### Page 2: Competitor Ad Intelligence (`competitor.html`)

Competitive analysis page. Structure:
- **Header**: Report title, competitor count, date range badge.
- **Tab Navigation**: One tab per competitor (use brand colors from brand-context if available).
- **Per-Competitor Section**: Headline metrics, ad examples/mentions from calls, messaging analysis, counter-positioning recommendations.
- **Comparison Table**: Side-by-side competitor comparison across key dimensions.
- **Strategic Recommendations**: Prioritized actions for competitive positioning.

Data source: `analysis/competitor-intel.md`.

Competitor brand colors: Assign each competitor a distinct color. If known competitors match the standard set (SuperATV → `#E8B100`, RevZilla → `#FF3300`, etc.), use those. Otherwise auto-assign from the palette.

### Page 3: Site Changes (`site-changes.html`)

Website optimization recommendations. Structure:
- **Hero Header**: Title, call count, recommendation count.
- **Stats Row**: Summary KPIs.
- **Per-Change Section** (numbered): Each site change includes:
  - Problem/Solution cards (red/green left-border).
  - Call count badge with representative quotes.
  - Competitor Examples: How competitors handle this better (with wireframe-style SVG mockups).
  - Proposed Mockup: SVG wireframe of the recommended change.
  - Implementation Card: Dark-background card with numbered steps and impact badges.
- **Section Dividers**: Styled dividers between recommendations.

Data source: `analysis/site-changes.md`.

### Page 4: Customer Journeys (`journeys.html`)

Journey mapping page. Structure:
- **Header**: Title, total journeys mapped, personas identified.
- **Persona Cards**: Each identified persona with demographics/psychographics summary.
- **Journey Flowcharts**: For each major journey pattern, a horizontal flowchart with stages (Trigger → Research → Compare → Decide → Purchase → Support), showing pain points and opportunities at each stage.
- **Cross-Competitor Comparison**: Table comparing journey experience across brands.
- **Recommendation Cards**: Prioritized actions to improve customer journeys.

Data source: `analysis/customer-journeys.md`.

## Shared Elements

Every page must include:

**Site Navigation Bar** (top of every page):
```html
<nav class="site-nav">
  <span class="nav-brand">{{BRAND_NAME}}</span>
  <a href="index.html" class="nav-link [active if current]">Call Intelligence</a>
  <a href="competitor.html" class="nav-link [active if current]">Competitor Intel</a>
  <a href="site-changes.html" class="nav-link [active if current]">Site Changes</a>
  <a href="journeys.html" class="nav-link [active if current]">Customer Journeys</a>
</nav>
```

**Chart.js CDN** (on pages with charts):
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
```

**Meta tags**: UTF-8 charset, viewport for responsive.

## Post-Generation

1. Create `_headers` and `_redirects` files for Netlify deployment.
2. Copy all dashboard files to the user's workspace folder.
3. Offer to create a deploy zip: `cd dashboard && zip -r /tmp/dashboard-deploy.zip . && cp /tmp/dashboard-deploy.zip [workspace]/`
4. Provide computer:// links to each HTML file.
5. Update `customer-driven-optimizations/config.md` with generation timestamp.

## Incremental Updates

When regenerating after new call analysis:
- Re-read all analysis files (they will contain updated aggregations).
- Regenerate all 4 HTML pages with updated data.
- Preserve the same file structure and naming.
