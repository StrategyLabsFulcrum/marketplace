---
name: competitor-tracker
description: >
  Manage and track competitors for competitive intelligence analysis. Add, remove, and update competitor
  profiles including their website, ad presence, brand positioning, and key metrics. Use when the user
  mentions "add competitor", "remove competitor", "track competitor", "manage competitors", "update
  competitor list", "who are we tracking", "competitor setup", "add a brand to track", or "edit
  competitor profiles". Also triggers on "new competitor", "stop tracking", or "competitor list".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
---

# Competitor Tracker

Manage the roster of competitors being tracked for ad analysis, journey mapping, and competitive reporting. This skill is the foundation layer — other skills in the competitive-landscape plugin read from the competitor registry this skill maintains.

## Data Location

All competitor data lives in `competitive-landscape/competitors/`. The registry file is `competitive-landscape/competitors/registry.json`.

## Registry Schema

```json
{
  "last_updated": "YYYY-MM-DD",
  "brand": {
    "name": "{{brand_name}}",
    "website": "{{brand_url}}",
    "industry": "{{industry}}"
  },
  "competitors": [
    {
      "id": "competitor-slug",
      "name": "Display Name",
      "website": "https://example.com",
      "status": "active",
      "added": "YYYY-MM-DD",
      "color": "#HEX",
      "colorDark": "#HEX",
      "notes": "Why this competitor matters",
      "categories": ["direct", "indirect", "aspirational"],
      "meta_ads_library_url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q={{brand_name}}",
      "google_ads_transparency_url": "https://adstransparency.google.com/advertiser/{{advertiser_id}}"
    }
  ]
}
```

### Competitor Categories

- **direct** — Sells similar products to the same audience. Primary competitive threat.
- **indirect** — Serves the same audience with different products, or similar products to a different audience.
- **aspirational** — A brand the user admires or wants to emulate (may be in a different vertical).

## Adding a Competitor

When the user wants to add a competitor:

1. Read `competitive-landscape/competitors/registry.json` (create if it doesn't exist).
2. Ask for (or infer from context):
   - **Name** (required): Brand/company name
   - **Website** (required): Homepage URL
   - **Category**: direct, indirect, or aspirational (default: direct)
   - **Color**: Brand color hex code (auto-detect from website if possible)
   - **Notes**: Why they're tracking this competitor
3. Generate a slug ID from the name (lowercase, hyphens, no special chars).
4. Add to the `competitors` array in the registry.
5. Create a competitor profile directory: `competitive-landscape/competitors/{{id}}/`
6. Create a profile file: `competitive-landscape/competitors/{{id}}/profile.md` with:

```markdown
# {{Name}}

**Website**: {{url}}
**Category**: {{category}}
**Added**: {{date}}
**Notes**: {{notes}}

## Overview
[To be populated by ad-analyzer and journey-mapper skills]

## Ad Presence
- Meta Ads Library: {{meta_ads_library_url}}
- Google Ads Transparency: {{google_ads_transparency_url}}

## Key Observations
[To be populated as analysis is run]
```

## Removing a Competitor

1. Set `status` to `"inactive"` in registry.json (soft delete — preserves historical data).
2. The competitor's directory and analysis files are preserved but excluded from active reports.
3. To permanently delete, user must explicitly say "permanently remove" — then delete the directory.

## Listing Competitors

When the user asks "who are we tracking" or "competitor list":

1. Read `registry.json`.
2. Display a formatted table:
   - Name | Website | Category | Status | Added | Notes
3. Show count of active vs. inactive competitors.

## Updating a Competitor

When the user wants to update a competitor's info:

1. Find the competitor in registry.json by name or ID.
2. Update the specified fields.
3. Update `last_updated` timestamp.
4. Update the profile.md file if relevant fields changed.

## Brand Context Integration

If a `brand-os/` directory exists (from Brand Content OS plugin) or a `customer-driven-optimizations/brand-context.md` file exists:

1. Read brand files to extract known competitors.
2. Pre-populate the registry with competitors found in brand context.
3. Confirm with user before adding: "I found these competitors in your brand profile: [list]. Add them all?"

## Initial Setup

When no `competitive-landscape/` directory exists and the user invokes any competitive-landscape skill:

1. Create the directory structure:
   ```
   competitive-landscape/
   ├── competitors/
   │   └── registry.json
   ├── analysis/
   │   ├── ads/
   │   └── journeys/
   └── reports/
   ```
2. Check for Brand Content OS or CDO brand context.
3. Walk through adding the first 2-3 competitors.
4. Confirm the roster before proceeding to analysis.

## Color Assignment

When no color is provided, auto-assign from this palette (skip colors already in use):

```
#E8B100  (gold)
#FF3300  (red-orange)
#2563EB  (blue)
#059669  (emerald)
#9333EA  (purple)
#EC4899  (pink)
#F97316  (orange)
#14B8A6  (teal)
```

Dark variants are generated by reducing lightness by 15%.
