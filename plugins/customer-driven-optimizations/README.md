# Customer Driven Optimizations

Turn recorded customer phone calls into actionable intelligence with a deployable HTML dashboard.

## What It Does

This plugin analyzes your phone call recordings or transcripts and produces a 4-page interactive dashboard covering:

1. **Call Intelligence** — KPI overview, top customer pain points, sentiment trends, category breakdowns, and prioritized action items.
2. **Competitor Intel** — Who customers mention, what they say about competitors, where you win and lose, and strategic counter-positioning.
3. **Site Changes** — Website issues surfaced by callers, with proposed solutions, competitor examples, wireframe mockups, and implementation steps.
4. **Customer Journeys** — Persona clusters, journey stage mapping, decision factors, friction points, and cross-brand comparison.

## Getting Started

Say **"set up customer optimizations"** or **"analyze my calls"** to launch the setup wizard. It walks through 4 steps:

1. **Brand connection** — Links to your Brand Content OS profile (if available) or collects basic brand info.
2. **Call folder** — Point to a folder of audio files (MP3/WAV) or text transcripts (TXT/CSV).
3. **Analysis** — Processes each call to extract insights, competitor mentions, site issues, and journey patterns.
4. **Dashboard** — Generates 4 self-contained HTML pages ready to deploy on Netlify, Vercel, or any static host.

## Adding New Calls

When you add new recordings or transcripts to your call folder, just say **"analyze new calls"**. The plugin detects unprocessed files, analyzes only the new ones, re-aggregates all data, and regenerates the dashboard.

## Supported Input Formats

- **Audio**: MP3, WAV, M4A (requires a transcription tool in the environment)
- **Text transcripts**: TXT files (one call per file, with or without speaker labels)
- **CSV/TSV**: Tabular exports with one row per call — auto-detects column mapping

## Brand Content OS Integration

If you have the Brand Content OS plugin installed with a completed brand profile, this plugin reads your brand files automatically to customize the dashboard with your brand name, known competitors, and product categories. No duplicate setup needed.

## Skills

| Skill | Trigger Phrases |
|-------|----------------|
| `setup-wizard` | "set up customer optimizations", "connect calls", "get started" |
| `analyze-calls` | "analyze calls", "process new calls", "refresh analysis" |
| `generate-dashboard` | "generate dashboard", "update dashboard", "rebuild pages" |

## Output Structure

```
customer-driven-optimizations/
├── brand-context.md
├── config.md
├── analysis/
│   ├── call-intelligence.md
│   ├── competitor-intel.md
│   ├── site-changes.md
│   ├── customer-journeys.md
│   └── raw/
│       ├── call-001.md
│       └── ...
└── dashboard/
    ├── index.html
    ├── competitor.html
    ├── site-changes.html
    ├── journeys.html
    ├── _headers
    └── _redirects
```

## Deployment

After dashboard generation, ask to **"create a deploy zip"** and you'll get a zip file ready to drag-and-drop onto Netlify or upload to any static host.

## Requirements

- Cowork mode with folder access
- Brand Content OS plugin (optional, for brand context)
- Audio transcription tool (optional, only needed for audio files)
