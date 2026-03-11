# Setup Flow Reference

Detailed phase specifications, decision trees, and user interaction patterns for the setup wizard. Each phase includes exact AskUserQuestion configurations, validation steps, and error recovery paths.

---

## Phase 1: Brand Connection

### Decision Tree

```
Start
  └─ Check: Does `brand-os/` exist in working folder?
       ├─ YES → Read brand files → Confirm with user → Save brand-context.md
       └─ NO → AskUserQuestion: 3 options
              ├─ "Run brand setup first" → Direct to Brand OS plugin
              ├─ "Enter minimal brand info" → Gather 5 fields → Save brand-context.md
              └─ "Skip brand context" → Save minimal brand-context.md with defaults
```

### Brand File Reading Priority

When `brand-os/` exists, read files in this order (stop early if sufficient data collected):

1. **`system-prompt.md`** — Contains brand name, positioning, voice summary. Highest priority.
2. **`voice-guidelines.md`** — Tone, vocabulary, communication style.
3. **`brand-foundations.md`** — Mission, values, target audience, competitive landscape.
4. **`key-messages.md`** — Core messaging, value props, differentiators.
5. **`content-pillars.md`** — Content themes and categories.
6. **`platform-config.md`** — Platform-specific settings, URLs.

### Variable Extraction

From brand files, extract these variables:

| Variable | Source Priority | Fallback |
|----------|----------------|----------|
| `brand_name` | system-prompt.md → brand-foundations.md | "Your Brand" |
| `website_url` | platform-config.md → brand-foundations.md | null |
| `industry` | brand-foundations.md | "Retail / E-commerce" |
| `target_audience` | brand-foundations.md → system-prompt.md | "General consumers" |
| `competitors` | brand-foundations.md (competitive landscape section) | [] |
| `product_segments` | key-messages.md → content-pillars.md | [] |
| `brand_colors` | brand-foundations.md (visual identity section) | Use default design system colors |

### Minimal Brand Info Collection

If user chooses "Enter minimal brand info", use AskUserQuestion for each:

**Question 1**: "What's your brand or company name?"
- Free text input
- Required — cannot proceed without this

**Question 2**: "What's your website URL?"
- Free text input
- Optional — can skip

**Question 3**: "What industry are you in?"
- Options: "Automotive / Powersports", "E-commerce / Retail", "SaaS / Technology", "Professional Services"
- Allow free text via "Other"

**Question 4**: "Who are your top 3 competitors? (comma-separated)"
- Free text input
- Optional — can skip

**Question 5**: "What are your main product categories? (comma-separated)"
- Free text input
- Optional — can skip

### brand-context.md Template

```markdown
# Brand Context
Last updated: {{ISO_DATE}}

## Brand
- Name: {{brand_name}}
- Website: {{website_url}}
- Industry: {{industry}}

## Audience
{{target_audience}}

## Competitors
{{competitors_list — one per line with dash prefix}}

## Product Segments
{{product_segments — one per line with dash prefix}}

## Brand Colors
- Primary: {{primary_color or "#1B2A3D"}}
- Accent: {{accent_color or "#D4782F"}}
- Background: {{bg_color or "#F5F0EB"}}

## Source
{{source — "Brand Content OS" or "Manual entry" or "Default"}}
```

---

## Phase 2: Call Folder Connection

### AskUserQuestion Configuration

**Question**: "What type of call data do you have?"

| Option | Label | Description |
|--------|-------|-------------|
| A | Audio files (MP3/WAV) | Recorded phone calls that need transcription |
| B | Text transcripts (TXT/CSV) | Pre-transcribed call logs or exported CSVs |
| C | Both audio and transcripts | Mix of recordings and text files |

### Folder Access Flow

```
User selects input type
  └─ Check: Is a workspace folder already mounted?
       ├─ YES → Ask: "Are your call files in the folder you already selected, or a different location?"
       │         ├─ Same folder → Scan mounted folder
       │         └─ Different → Use request_cowork_directory for new folder
       └─ NO → Use request_cowork_directory
```

### File Scanning

After folder access, scan based on input type:

**Audio files**:
```bash
find [path] -type f \( -name "*.mp3" -o -name "*.wav" -o -name "*.m4a" \) | sort | head -200
```

**Text transcripts**:
```bash
find [path] -type f \( -name "*.txt" -o -name "*.csv" -o -name "*.tsv" \) | sort | head -200
```

**Both**:
```bash
find [path] -type f \( -name "*.mp3" -o -name "*.wav" -o -name "*.m4a" -o -name "*.txt" -o -name "*.csv" -o -name "*.tsv" \) | sort | head -200
```

### Scan Report

After scanning, report to user:

```
Found [N] files in your call folder:
- [X] audio files (MP3/WAV/M4A)
- [Y] text transcripts (TXT)
- [Z] CSV files ([R] total rows detected)

Date range: [earliest] to [latest] (if extractable)
Estimated processing time: ~[T] minutes
```

### CSV Preview

If CSV files found, read the first 3 rows and show column mapping:

```
I found a CSV with these columns: [col1, col2, col3, ...]
I'll map them as:
  - "customer" → Caller Name
  - "date" → Call Date
  - "transcript" → Transcript Text
  - "duration" → Call Duration

Does this mapping look correct?
```

### Validation Checks

| Check | Action if Failed |
|-------|-----------------|
| Folder is empty | "I didn't find any supported files. Make sure your folder contains .mp3, .wav, .txt, or .csv files." |
| Only audio, no transcription tool | "I found [N] audio files but no transcription tool is available. You can provide text transcripts instead, or install a transcription service." |
| CSV has no transcript column | "I found a CSV but couldn't identify which column contains the call transcripts. Can you tell me which column has the conversation text?" |
| Files are very large (>100MB audio) | "Some audio files are quite large. Processing may take a while. Would you like to proceed with all files or start with a smaller batch?" |
| Over 200 files | "Found [N] files — that's a lot! Would you like to process all of them or start with the most recent [50]?" |

### config.md Template

```markdown
# Customer Driven Optimizations — Configuration
Last updated: {{ISO_DATE}}

## Input Configuration
- Input Type: {{audio|transcript|mixed}}
- Source Folder: {{path}}
- File Count: {{N}}
- Date Range: {{earliest}} to {{latest}}

## Processing Status
- Last Analysis: {{ISO_DATE or "Never"}}
- Calls Processed: {{N}}
- Calls Pending: {{N}}

## Dashboard
- Generated: {{ISO_DATE or "Never"}}
- Pages: index.html, competitor.html, site-changes.html, journeys.html
```

---

## Phase 3: Initial Analysis

### Invocation

Invoke the `analyze-calls` skill with the "analyze all" directive (not "analyze new" since this is first run).

### Progress Display

Show progress as calls are processed:

```
📞 Analyzing calls...

[██████████░░░░░░░░░░] 12/25 calls processed

Current: call-012 — John D. (2024-01-15)
  → Category: Pre-Purchase Research
  → Sentiment: Positive
  → Tags: fitment, pricing

Latest findings:
  • 8 calls mention fitment questions (32%)
  • 3 competitors mentioned so far
  • 5 website issues identified
```

Update progress after each call completes.

### Post-Analysis Summary

After all calls processed, show a summary before proceeding to dashboard:

```
✅ Analysis Complete — [N] calls processed

Key Findings:
  📊 Top issue: [issue] ([X]% of calls)
  😊 Average sentiment: [score] ([label])
  🏆 Resolution rate: [X]%
  🔍 Competitors mentioned: [list]
  🌐 Website issues found: [N]
  🗺️ Customer personas identified: [N]

Ready to generate your dashboard. Shall I proceed?
```

### Error Recovery

| Error | Recovery |
|-------|----------|
| Single call fails to parse | Skip it, continue processing. Report at end: "[N] calls could not be processed." |
| All calls fail | Stop and diagnose. Check format assumptions. Ask user to confirm file type. |
| Analysis produces empty aggregations | Check if transcript content is meaningful. May indicate format detection issue. |
| Out of context mid-analysis | Save progress. On resume, detect already-processed calls and continue from where left off. |

---

## Phase 4: Dashboard Generation

### Invocation

Invoke the `generate-dashboard` skill to build all 4 HTML pages.

### Progress Display

```
🎨 Building dashboard...

[████████░░░░░░░░░░░░] 2/4 pages generated

✅ Call Intelligence (index.html)
✅ Competitor Intel (competitor.html)
⏳ Site Changes (site-changes.html)
⬜ Customer Journeys (journeys.html)
```

### Delivery

After all pages generated:

1. Copy dashboard files to workspace folder.
2. Provide computer:// links to each page.
3. Offer deploy zip.

```
🎉 Dashboard ready!

View your pages:
  📊 [Call Intelligence](computer:///path/to/dashboard/index.html)
  🏢 [Competitor Intel](computer:///path/to/dashboard/competitor.html)
  🌐 [Site Changes](computer:///path/to/dashboard/site-changes.html)
  🗺️ [Customer Journeys](computer:///path/to/dashboard/journeys.html)

Would you like me to create a deploy-ready zip for Netlify?
```

### Deploy Zip

If user wants deploy zip:

```bash
cd [workspace]/customer-driven-optimizations/dashboard && zip -r /tmp/dashboard-deploy.zip . -x "*.DS_Store" && cp /tmp/dashboard-deploy.zip [workspace]/
```

Provide link: `[Download deploy zip](computer:///path/to/dashboard-deploy.zip)`

---

## Directory Structure Creation

At the start of setup, create the full directory tree:

```bash
mkdir -p customer-driven-optimizations/analysis/raw
mkdir -p customer-driven-optimizations/analysis/transcripts
mkdir -p customer-driven-optimizations/dashboard
```

---

## Returning User Detection

If `customer-driven-optimizations/` already exists with data:

**AskUserQuestion**:

| Option | Label | Description |
|--------|-------|-------------|
| A | Update existing setup | Keep current data, update brand context or add new calls |
| B | Start fresh | Back up current data and begin new setup |
| C | Just analyze new calls | Skip setup, jump straight to processing new files |

If "Start fresh":
```bash
mv customer-driven-optimizations customer-driven-optimizations-backup-$(date +%Y%m%d)
```
Then proceed with full setup.

If "Just analyze new calls":
- Skip Phases 1-2
- Run Phase 3 in incremental mode (new files only)
- Run Phase 4 to regenerate dashboard
