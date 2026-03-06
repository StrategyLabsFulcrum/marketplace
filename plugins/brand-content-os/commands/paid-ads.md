---
description: Generate Meta Ads and Google Ads content using brand knowledge
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
argument-hint: "<product or collection name>"
---

# Paid Ads — Meta + Google Content Generation

Generate on-brand ad content for Meta (Facebook/Instagram) and Google (Search, Shopping, Performance Max) platforms. Automatically applies brand knowledge, voice rules, and platform-specific best practices.

## Before Generating

0. **Check configuration**: Look for `.brand-os-config.md` in the working directory (the same directory that contains `brand-os/`). If found, read it to determine storage mode and output directories. If `mode` is `fast.io` and `auto_pull_on_start` is `true`, check `last_pull`. If stale (older than 24 hours or missing), inform the user: "Your local brand files haven't been synced in [X hours/days]. Run `/sync-brand-os pull` to get the latest from Fast.io, or continue with the local copy." Proceed with local files regardless — never block content generation on sync. If no config file is found, continue with default behavior.

1. **Load brand knowledge**: Read all files from the `brand-os/` directory in the user's working folder. If the directory doesn't exist or is empty, inform the user and suggest running `/new-brand-setup` first.

2. **Load the system prompt**: Read `brand-os/system-prompt.md` and use it as foundational context for all generation.

3. **Load references**: Read the following from the plugin:
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/platform-prompts.md` (Meta and Google sections)
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/best-practices.md` (Meta and Google sections)

## Gather Inputs

Ask the user what they need. Use AskUserQuestion for structured choices:

1. **Platform**: Meta Ads, Google Ads, or both?
2. **Content type** (based on platform selection):

   **Meta Ads options:**
   - Ad Copy (Pain/Gain/Tech variations)
   - Dynamic Creative (visual & video concepts)
   - Retargeting — Warm audience
   - DCA — Viewed product retargeting
   - DCA — Abandoned cart retargeting
   - DCA — Broad catalog prospecting

   **Google Ads options:**
   - Responsive Search Ad (headlines & descriptions)
   - Shopping Feed (product title & description)
   - Performance Max (asset copy)
   - Shopping Title Optimization (DCA)
   - Shopping Description Enhancement (DCA)
   - Negative Keyword Generator

3. **Product or collection**: What specific product or collection is this for? (Use `$ARGUMENTS` if provided.)
4. **Funnel stage** (if not obvious from content type): Cold, Warm, or Hot?
5. **Tone angle** (for ad copy variations): Pain, Gain, Tech, or all three?

If the user provides a product name via arguments, skip asking for it.

## Generation Process

1. Select the appropriate prompt template(s) from the platform-prompts reference
2. Populate all auto-variables from brand knowledge files
3. Insert per-use variables from user input
4. Generate the content following all brand voice rules
5. Apply the NEVER list check — scan output for any prohibited words/phrases
6. Apply the quality filter from voice-guidelines.md
7. If any violations are found, revise before presenting

## Output Format

Present generated content with clear labeling:

```
## [Platform] — [Content Type]
### For: [Product/Collection Name]

[Generated content here]

---
**Brand Voice Check**: ✓ No NEVER list violations | ✓ Quality filter passed
**Platform Notes**: [Any relevant best practice reminders]
```

## Auto-Save

After presenting the content, if `.brand-os-config.md` was found and specifies an output directory for `paid_ads` (default: `paid-ads/`), automatically save the generated content as a markdown file. Use the naming convention: `{product}-meta-ads-{YYYY-MM-DD}.md` or `{product}-google-ads-{YYYY-MM-DD}.md` (based on platform). If both platforms were generated, save as `{product}-paid-ads-{YYYY-MM-DD}.md`. Overwrite if the file already exists. Inform the user: "Saved to `paid-ads/{filename}`."

If no config file was found, offer to save as a markdown file (current behavior).

## Follow-Up

After presenting the content:
- Ask if they want revisions to any variation
- Offer to generate for the other platform (if they only chose one)
- Offer to generate a different content type for the same product
- If they generated ad copy, offer to create matching visual/video concepts
