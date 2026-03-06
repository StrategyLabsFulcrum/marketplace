---
description: Generate a full content bundle from one product or topic (blog + email + video + social + carousel)
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
argument-hint: "<product name or blog topic>"
---

# Content Multiply — 1 Input → 5 Assets

The Content Multiplier takes a single product or topic and generates a complete cross-channel content bundle. This is the most powerful command in the Brand & Content OS — it creates cohesive, on-brand content across five formats in one pass.

## Before Generating

0. **Check configuration**: Look for `.brand-os-config.md` in the working directory (the same directory that contains `brand-os/`). If found, read it to determine storage mode and output directories. If `mode` is `fast.io` and `auto_pull_on_start` is `true`, check `last_pull`. If stale (older than 24 hours or missing), inform the user: "Your local brand files haven't been synced in [X hours/days]. Run `/sync-brand-os pull` to get the latest from Fast.io, or continue with the local copy." Proceed with local files regardless — never block content generation on sync. If no config file is found, continue with default behavior.

1. **Load brand knowledge**: Read ALL files from the `brand-os/` directory. Every file is relevant for this command. If missing, suggest running `/new-brand-setup` first.
2. **Load the system prompt**: Read `brand-os/system-prompt.md` as foundational context.
3. **Load references**:
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/platform-prompts.md` (Master Templates section — MULTIPLY-1)
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/best-practices.md` (all sections — content spans all platforms)

## Gather Inputs

1. **Input type**: Product name or blog topic? (Use `$ARGUMENTS` if provided.)
2. **The input**: What specific product or topic?
3. **Content pillar** (optional): Which content pillar does this align to? Offer options from `brand-os/content-pillars.md` if available.
4. **Priority channel** (optional): Is there a channel that matters most this time? (This gets the most detailed output.)

## Generation Process

1. Select the MULTIPLY-1 template from platform-prompts reference
2. Populate all auto-variables from brand knowledge
3. Identify the relevant product segment (if applicable) for segment-specific messaging
4. Generate all 5 assets as a cohesive bundle — they should tell the same story adapted for each format
5. Apply NEVER list check across ALL outputs
6. Apply quality filter across ALL outputs
7. Verify platform-specific requirements:
   - Blog: 800+ words, includes Brand Recommendation section
   - Email: 200-350 words, mobile-friendly formatting, team sign-off
   - Video script: 30-45 seconds, visual + VO directions
   - Social caption: Hook in line 1, includes social handles and hashtags
   - Carousel: 5 slides, clear narrative arc

## Output Format

```
# Content Bundle — [Product/Topic Name]
**Content Pillar**: [Aligned pillar]
**Generated**: [Date]

---

## 1. BLOG POST
**Title**: [Title]
**Word Count**: [X] words
**Content Pillar**: [Pillar name]

[Full blog post]

---

## 2. EMAIL
**Subject Line A**: [Option A]
**Subject Line B**: [Option B]
**Preview Text**: [Preview]

[Email body]

**Sign-off**: [Team sign-off]

---

## 3. SHORT VIDEO SCRIPT (30-45 sec)

| Timestamp | Visual | Audio/VO |
|-----------|--------|----------|
| 0:00-0:05 | [Opening shot] | [Hook line] |
| 0:05-0:15 | [Problem visual] | [Problem VO] |
| 0:15-0:30 | [Solution visual] | [Solution VO] |
| 0:30-0:40 | [Result visual] | [Result VO] |
| 0:40-0:45 | [Brand end card] | [CTA] |

**Music/Mood**: [Tone and pacing notes]
**Edit Style**: [Pacing, transitions, speed ramping notes]

---

## 4. SOCIAL CAPTION (Instagram / Facebook)

[Caption with hook, body, CTA, handles, hashtags]

**Platform Notes**: [Any platform-specific adaptations]

---

## 5. CAROUSEL (5 Slides)

| Slide | Headline | Supporting Text | Visual Direction |
|-------|----------|----------------|-----------------|
| 1 | [Hook] | [Subtext] | [Visual note] |
| 2 | [Problem] | [Subtext] | [Visual note] |
| 3 | [Solution] | [Subtext] | [Visual note] |
| 4 | [Result] | [Subtext] | [Visual note] |
| 5 | [CTA] | [Subtext] | [Visual note] |

---

**Brand Voice Check**: ✓ All 5 assets checked | ✓ No NEVER list violations | ✓ Quality filter passed
```

## Auto-Save

After presenting the content, if `.brand-os-config.md` was found and specifies an output directory for `content_bundles` (default: `content-bundles/`), automatically save the full bundle as a single markdown file. Use the naming convention: `{product-or-topic}-content-bundle-{YYYY-MM-DD}.md`. Overwrite if the file already exists. Inform the user: "Saved to `content-bundles/{filename}`."

If no config file was found, offer to save the bundle as a markdown file (current behavior).

## Follow-Up

After presenting the bundle:
- Offer to revise any individual asset
- Offer to generate ad variations (Meta or Google) for the same product using `/paid-ads`
- Suggest scheduling this as a weekly content generation workflow
