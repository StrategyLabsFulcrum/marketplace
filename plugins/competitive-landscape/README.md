# Competitive Landscape

Track competitors, analyze their advertising strategies, map their customer journeys, and generate actionable competitive intelligence reports.

## What It Does

This plugin gives any brand a structured system for understanding and outmaneuvering their competitive landscape:

1. **Competitor Tracker** — Manage a roster of competitors with profiles, brand colors, ad library links, and categorization (direct, indirect, aspirational).
2. **Ad Analyzer** — Analyze competitor advertising across Meta and Google. Extract themes, messaging patterns, creative quality, offer strategies, and trends.
3. **Journey Mapper** — Map customer journeys on competitor websites. Score each stage from discovery through retention. Identify UX patterns, friction points, and best practices.
4. **Competitive Report** — Generate executive summaries, full competitive reports, and deployable HTML dashboards that visualize the entire competitive landscape.

## Getting Started

Say **"track competitors"** or **"set up competitive analysis"** to start. The plugin walks through:

1. **Brand context** — Connects to Brand Content OS or CDO brand data if available, or collects basic brand info.
2. **Add competitors** — Add 2-4 competitors to track with their websites and categories.
3. **Analyze** — Run ad analysis and journey mapping as data is provided.
4. **Report** — Generate reports and dashboards on demand.

## Skills

| Skill | Trigger Phrases |
|-------|----------------|
| `competitor-tracker` | "add competitor", "track competitor", "manage competitors", "competitor list" |
| `ad-analyzer` | "analyze ads", "competitor ads", "ad themes", "what are they running" |
| `journey-mapper` | "map journey", "competitor UX", "site walkthrough", "conversion funnel" |
| `competitive-report` | "generate report", "competitive dashboard", "comparison report", "landscape report" |

## Output Structure

```
competitive-landscape/
├── competitors/
│   ├── registry.json
│   ├── super-atv/
│   │   ├── profile.md
│   │   ├── ads/
│   │   │   └── analysis.md
│   │   └── journeys/
│   │       └── analysis.md
│   └── revzilla/
│       └── ...
├── analysis/
│   ├── ads/
│   │   └── comparison.md
│   └── journeys/
│       └── comparison.md
└── reports/
    ├── executive-summary.md
    ├── full-report.md
    └── dashboard/
        ├── index.html
        ├── ads.html
        ├── journeys.html
        ├── strategy.html
        ├── data.js
        ├── _headers
        └── _redirects
```

## Integration with Other Plugins

- **Brand Content OS** — Reads brand knowledge to personalize reports and pre-populate known competitors.
- **Customer Driven Optimizations** — Cross-references competitor mentions from call analysis with ad/journey data for a complete picture.

## Deployment

After generating a dashboard, ask to **"create a deploy zip"** for a zip file ready to drag-and-drop onto Netlify or any static host.

## Requirements

- Cowork mode with folder access
- Brand Content OS plugin (optional, for brand context)
- Customer Driven Optimizations plugin (optional, for call data cross-reference)
