---
name: analyze-calls
description: >
  Analyze recorded phone calls to extract customer insights, competitive intelligence, site optimization
  opportunities, and journey patterns. Supports both audio files (MP3/WAV) and pre-made transcripts
  (TXT/CSV). Use when the user mentions "analyze calls", "process calls", "new calls", "update analysis",
  "phone call insights", "call transcripts", "review calls", "what are customers saying", or "analyze
  new recordings". Also triggers on "reprocess calls", "refresh analysis", or "run call analysis".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Agent
---

# Call Analysis Engine

Process phone call recordings or transcripts to extract structured intelligence across 4 dimensions: call insights, competitor mentions, site optimization opportunities, and customer journey patterns.

## Input Detection

Read `${CLAUDE_PLUGIN_ROOT}/skills/analyze-calls/references/analysis-framework.md` for the complete analysis taxonomy and scoring rubrics.

Read `${CLAUDE_PLUGIN_ROOT}/skills/analyze-calls/references/transcript-parsing.md` for format detection and parsing rules.

### Determine What to Analyze

1. Read `customer-driven-optimizations/config.md` for the configured source folder and input type.
2. Read `customer-driven-optimizations/analysis/raw/` to find already-processed calls.
3. Compare source folder contents against processed calls to identify NEW files only.
4. If invoked as "analyze new calls", process only unprocessed files. If "reprocess all", analyze everything.

### Transcript Acquisition

**For audio files (MP3/WAV/M4A):**
- Check for available transcription tools in the environment.
- If a transcription tool is available, process each audio file to text.
- If no tool is available, inform the user: "Audio transcription requires an external service. Please provide text transcripts instead, or install a transcription tool."
- Save transcripts to `customer-driven-optimizations/analysis/transcripts/`.

**For text transcripts (TXT):**
- Read each file as a complete call transcript.
- Extract metadata from filename if structured (e.g., `2024-01-15_john-doe.txt`).

**For CSV transcripts:**
- Parse the CSV and map columns to: caller_name, date, duration, transcript_text, category, notes.
- Each row = one call. Process each row independently.

## Per-Call Analysis

For each transcript, extract the following structured data. Save to `customer-driven-optimizations/analysis/raw/call-[NNN].md`:

```markdown
# Call Analysis: [caller_name or ID]
**Date**: [date]  **Duration**: [duration]  **Category**: [auto-detected]

## Summary
[2-3 sentence summary of the call]

## Customer Intent
- Primary: [what the caller wanted]
- Secondary: [any secondary needs]
- Outcome: [resolved / unresolved / partial]

## Pain Points
- [specific pain point with verbatim quote if available]

## Competitor Mentions
- [competitor name]: [context of mention, sentiment, what they liked/disliked]

## Product Mentions
- [product/category]: [what was discussed, questions asked]

## Website Experience
- [any mentions of website navigation, finding products, checkout, etc.]

## Journey Stage
- [awareness / consideration / decision / post-purchase / support]

## Sentiment
- Overall: [positive / negative / neutral / mixed]
- Key Emotion: [frustration, excitement, confusion, satisfaction, etc.]

## Action Items
- [specific action items extracted from the call]

## Tags
[auto-generated tags: fitment, stock, custom, pricing, install, info, shipping, returns, nav]
```

## Aggregation

After processing all calls, aggregate findings into 4 output files:

### 1. Call Intelligence (`analysis/call-intelligence.md`)

Aggregate across all calls:
- **KPI Summary**: Total calls, category breakdown, resolution rate, average sentiment score, top pain point.
- **Top Opportunities**: Ranked by frequency × impact. Each opportunity includes: title, percentage of calls, call count, representative quotes, recommended actions.
- **Category Distribution**: Breakdown by tag (fitment, stock, pricing, etc.).
- **Trend Data**: If dates span multiple weeks/months, show trends.

### 2. Competitor Intel (`analysis/competitor-intel.md`)

- **Competitor Mention Frequency**: How often each competitor is mentioned.
- **Competitor Sentiment**: What callers say about each competitor (positive/negative).
- **Counter-Positioning**: Where the brand wins vs. loses against each competitor.
- **Competitive Gaps**: Features/services competitors offer that callers ask about.
- Use brand context (from `brand-context.md`) to align competitor analysis with known competitors.

### 3. Site Changes (`analysis/site-changes.md`)

- **Top Website Issues**: Ranked by frequency of mention in calls.
- **Each Issue**: Problem description, call count, representative quotes, proposed solution, competitor examples (how competitors handle it better), implementation priority.
- **UX Pain Points**: Navigation, search, product pages, checkout, mobile experience.
- **Content Gaps**: Information callers ask for that isn't on the website.

### 4. Customer Journeys (`analysis/customer-journeys.md`)

- **Journey Patterns**: Common paths callers describe (how they found the brand, what they did before calling, what triggered the call).
- **Persona Clusters**: Group callers by behavior patterns and needs.
- **Decision Factors**: What influences purchase decisions (mentioned in calls).
- **Friction Points**: Where journeys stall or break down.
- **Cross-Competitor Journeys**: How callers compare shopping experiences across brands.

## Incremental Updates

When processing new calls on top of existing analysis:
1. Process only new call files.
2. Re-aggregate all raw call files (existing + new) into updated output files.
3. Note in each output file: "Last updated: [date], Total calls analyzed: [N]"

## Quality Checks

After analysis, verify:
- Every call file has all required sections (even if some are "N/A").
- Aggregation totals match individual call counts.
- Competitor names are consistent (normalize variations like "Super ATV" vs "SuperATV").
- Tags use the standard vocabulary from the tag taxonomy.
