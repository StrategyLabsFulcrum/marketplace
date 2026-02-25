---
name: brand-os
description: >
  Brand & Content Operating System for managing client brand knowledge and generating on-brand content.
  Use when the user mentions "brand setup", "brand voice", "content generation", "brand guidelines",
  "content strategy", "brand profile", "brand knowledge", "voice guidelines", "content pillars",
  "brand audit", or wants to create marketing content that follows specific brand rules.
  Also triggers when the user asks about their brand files, positioning, tone, vocabulary,
  or competitive landscape.
version: 0.1.0
---

# Brand & Content Operating System

A framework for capturing, storing, and applying brand knowledge to generate consistent, on-brand content across all marketing channels.

## How It Works

The Brand OS has two layers:

1. **Brand Knowledge Layer** — Structured files that capture everything about a client's brand (positioning, voice, vocabulary, competitors, content pillars, key messages). These live in a `brand-os/` folder.
2. **Content Generation Layer** — Platform-specific prompt templates that combine brand knowledge with per-use inputs (product name, content goal, etc.) to generate content.

When any content command runs, it automatically reads the brand knowledge files and injects the relevant context into the prompt templates. The user only needs to provide what's unique to that specific piece of content.

## Brand Knowledge Storage

Brand knowledge is stored as structured markdown files in a `brand-os/` subfolder within the user's working directory.

### File Structure

```
brand-os/
├── brand-foundations.md      # Positioning, pillars, competitive landscape
├── voice-guidelines.md       # Tone, never/always lists, vocabulary
├── content-pillars.md        # Content themes and calendar framework
├── key-messages.md           # Taglines, power phrases, segment messaging
├── platform-config.md        # Social URLs, tech stack, team, channels
└── system-prompt.md          # Auto-assembled AI foundation prompt
```

### Alternative: Google Drive Storage

If the user prefers Google Drive, brand files can be stored as Google Docs in a shared folder. When using Drive storage, the `platform-config.md` file should note the Drive folder ID. Use the Google Drive MCP tools to fetch content when generating.

## Reading Brand Knowledge

Before generating any content, read ALL brand knowledge files from the `brand-os/` directory. If a file is missing or empty, note what's missing and suggest the user run `/brand-setup` to complete it.

### Priority Loading Order

1. `system-prompt.md` — Always load first (contains the assembled brand identity)
2. `voice-guidelines.md` — Critical for any content generation
3. `brand-foundations.md` — Positioning and competitive context
4. `key-messages.md` — Taglines, phrases, segment-specific language
5. `content-pillars.md` — Thematic guidance
6. `platform-config.md` — Channel-specific details

## Variable System

Brand knowledge files contain pre-defined values that auto-populate into prompt templates. Per-use variables are gathered at generation time.

### Pre-Populated Variables (from brand files)

These are filled automatically from the brand knowledge:

| Variable | Source File | Example |
|----------|------------|---------|
| `{{brand_name}}` | brand-foundations.md | "Rugged Terrain" |
| `{{website_url}}` | brand-foundations.md | "ruggedterrain.com" |
| `{{core_promise}}` | brand-foundations.md | "We don't just sell parts..." |
| `{{target_audience}}` | brand-foundations.md | "The Performance Junkie" |
| `{{point_of_difference}}` | brand-foundations.md | "Battle-Hardened Curation" |
| `{{brand_pillars}}` | brand-foundations.md | List of pillars |
| `{{competitors}}` | brand-foundations.md | Competitor positioning |
| `{{tone_rules}}` | voice-guidelines.md | Tone spectrum |
| `{{never_list}}` | voice-guidelines.md | Words/phrases to avoid |
| `{{always_list}}` | voice-guidelines.md | Required patterns |
| `{{vocabulary}}` | voice-guidelines.md | Preferred/avoided terms |
| `{{content_pillars}}` | content-pillars.md | Theme definitions |
| `{{taglines}}` | key-messages.md | Core taglines |
| `{{power_phrases}}` | key-messages.md | Reusable phrases |
| `{{product_segments}}` | key-messages.md | Segment-specific messaging |
| `{{social_channels}}` | platform-config.md | Social URLs |
| `{{team_members}}` | platform-config.md | Team and sign-off names |

### Per-Use Variables (asked at generation time)

These are gathered each time content is generated:

| Variable | When to Ask | Example |
|----------|------------|---------|
| `{{product_name}}` | Always for product-specific content | "Gen 2 Heavy-Duty Tie Rods" |
| `{{collection_name}}` | For collection-level content | "Suspension Upgrades" |
| `{{content_goal}}` | When ambiguous | "Brand awareness" or "Product conversion" |
| `{{platform}}` | When the command covers multiple | "Instagram" or "Facebook" |
| `{{tone_angle}}` | For ad variations | "Pain/fear", "Gain/aspiration", "Technical" |
| `{{funnel_stage}}` | For ads and email | "Cold", "Warm", "Hot/retargeting" |
| `{{season_or_timing}}` | When seasonally relevant | "Spring riding season" |
| `{{keyword_group}}` | For Google Ads/SEO | "heavy duty UTV axles" |

When a per-use variable has been used before, offer the previous value as a default.

## Content Generation Principles

When generating any content through this plugin:

1. **Load brand knowledge first** — Read all brand files before generating
2. **Inject the system prompt** — Always prepend the assembled system prompt as foundational context
3. **Apply voice rules strictly** — Check output against the never list and always list
4. **Lead with experience, not specs** — Sell the feeling, then support with details
5. **Use the vocabulary reference** — Prefer the brand's terminology over generic alternatives
6. **Address the reader as a peer** — Never as a "customer" or "user" (unless the brand specifies otherwise)
7. **Tie to brand pillars** — Every piece of content should connect to at least one content pillar
8. **Include a brand-aligned CTA** — Never generic; always connects to brand identity

## Additional Resources

- **`references/brand-profile-schema.md`** — Complete schema for all 10 brand knowledge areas with field definitions and examples
- **`references/platform-prompts.md`** — All generalized prompt templates organized by platform
- **`references/best-practices.md`** — Platform-specific best practices for Meta, Email, SMS, Google, and Shopify
- **`references/variable-glossary.md`** — Complete variable reference with definitions, sources, and mapping
