---
name: setup-wizard
description: >
  Guided first-time setup for the Customer Driven Optimizations plugin. Walks through brand knowledge
  connection, call folder selection, initial call analysis, and dashboard generation. Use when the user
  mentions "setup", "get started", "connect calls", "analyze my calls", "build dashboard", "customer
  optimization setup", "call intelligence setup", or any first-time configuration of the call analysis
  pipeline. Also triggers on "connect brand", "link brand files", or "set up call folder".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion, Agent
---

# Customer Driven Optimizations — Setup Wizard

Guide the user through a complete first-time setup that connects brand knowledge, ingests phone call data, runs analysis, and generates a deployable dashboard.

## Pre-Flight Check

1. Check if a `customer-driven-optimizations/` directory already exists in the working folder.
   - If it exists with data, inform the user and ask: update existing setup or start fresh?
   - If starting fresh, back up to `customer-driven-optimizations-backup-[date]/`.
2. Check if a `brand-os/` directory exists (from Brand Content OS plugin).
   - If found, read the brand files for context.
   - If not found, offer two paths: run Brand OS setup first, or proceed with minimal brand context.
3. Create the `customer-driven-optimizations/` directory structure.

## Setup Flow — 4 Phases

### Phase 1: Brand Connection

Read `${CLAUDE_PLUGIN_ROOT}/skills/setup-wizard/references/setup-flow.md` for the detailed flow specification.

Check for existing `brand-os/` directory in the user's working folder. If brand files exist:

1. Read all 6 brand files in priority order: `system-prompt.md`, `voice-guidelines.md`, `brand-foundations.md`, `key-messages.md`, `content-pillars.md`, `platform-config.md`.
2. Extract key variables: `{{brand_name}}`, `{{website_url}}`, `{{target_audience}}`, `{{competitors}}`, `{{product_segments}}`.
3. Confirm with user: "I found brand knowledge for [brand_name]. Should I use this for your dashboard?"
4. Save a `customer-driven-optimizations/brand-context.md` file with the extracted brand variables.

If no brand files exist, use AskUserQuestion:
- Option A: "Run brand setup first" — direct user to the Brand Content OS `/brand-setup` command.
- Option B: "Enter minimal brand info" — gather brand name, website, industry, 3 competitors, and key product categories. Save to `brand-context.md`.
- Option C: "Skip brand context" — proceed without brand context (dashboard will be generic).

### Phase 2: Call Folder Connection

Use AskUserQuestion to determine input type:

**Option A: Audio files (MP3/WAV)**
- Ask user to point to a folder containing audio files.
- Use `request_cowork_directory` if the folder isn't already accessible.
- Scan the folder: `find [path] -type f \( -name "*.mp3" -name "*.wav" -name "*.m4a" \) | head -50`
- Report count: "Found [N] audio files. These will need transcription before analysis."
- Note: Audio transcription uses Bash with available transcription tools. If no transcription tool is available, inform user they'll need to provide transcripts instead.

**Option B: Pre-made transcripts (TXT/CSV)**
- Ask user to point to transcript files or a single CSV.
- Scan: `find [path] -type f \( -name "*.txt" -name "*.csv" -name "*.tsv" \) | head -50`
- For CSV: detect columns and map to expected fields (caller, date, duration, transcript_text, category).
- For TXT: assume one file per call with the transcript text.

**Option C: Mixed (both audio and transcripts)**
- Handle both types from the same or different folders.

Save configuration to `customer-driven-optimizations/config.md`:
```
## Input Configuration
- Input Type: [audio|transcript|mixed]
- Source Folder: [path]
- File Count: [N]
- Date Range: [earliest] to [latest]
```

### Phase 3: Initial Analysis

Invoke the `analyze-calls` skill to process all discovered files. This produces structured analysis output files in `customer-driven-optimizations/analysis/`.

Display progress to the user as calls are processed.

### Phase 4: Dashboard Generation

Invoke the `generate-dashboard` skill to build all 4 HTML dashboard pages from the analysis output. The dashboard is saved to `customer-driven-optimizations/dashboard/`.

Deliver the dashboard files to the user's workspace folder and provide computer:// links.

Offer to create a deploy-ready zip for Netlify/Vercel.

## Output Structure

After complete setup, the working directory contains:

```
customer-driven-optimizations/
├── brand-context.md           # Extracted brand variables
├── config.md                  # Input configuration and folder paths
├── analysis/
│   ├── call-intelligence.md   # Aggregated call insights
│   ├── competitor-intel.md    # Competitor mentions and analysis
│   ├── site-changes.md        # Website optimization opportunities
│   ├── customer-journeys.md   # Journey patterns and maps
│   └── raw/                   # Individual call analyses
│       ├── call-001.md
│       ├── call-002.md
│       └── ...
└── dashboard/
    ├── index.html             # Call Intelligence Dashboard
    ├── competitor.html         # Competitor Ad Intelligence
    ├── site-changes.html       # Site Changes & Recommendations
    ├── journeys.html           # Customer Journey Maps
    ├── _headers                # Netlify headers
    └── _redirects              # Netlify redirects
```

## Completion Message

After setup completes:
- Summarize: calls analyzed, key findings count, pages generated.
- Provide computer:// links to each dashboard page.
- Offer to create a deploy zip.
- Explain how to analyze new calls: "When you add new call recordings or transcripts to your folder, just ask me to 'analyze new calls' and I'll update the dashboard."
