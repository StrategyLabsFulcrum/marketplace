---
description: Import an existing brand document and convert it to structured brand files
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# Brand Import — Parse Existing Brand Document

Parse an uploaded or pasted brand document (playbook, style guide, brand book, etc.) and convert it into the structured brand knowledge files that power the Brand & Content OS.

## Before Starting

1. Ask the user how they want to provide their brand document:
   - **Upload a file** — Look for the file in the uploads directory or the user's working folder
   - **Paste the content** — Accept pasted text directly in the conversation
   - **Google Drive** — Ask for the document name or URL, then use Google Drive tools to fetch it

2. Check if a `brand-os/` directory already exists:
   - If yes, ask whether to merge with existing files or start fresh
   - If starting fresh, back up existing files

## Parsing Process

Read the source document and extract content into the 10 brand knowledge areas defined in `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/brand-profile-schema.md`.

### Extraction Mapping

For each area, scan the document for relevant content:

1. **Business Snapshot** — Look for: company name, website, team names, revenue, platforms, industry
2. **Core Positioning** — Look for: mission statements, value propositions, positioning frameworks, "about us" language, promises
3. **Competitive Positioning** — Look for: competitor mentions, comparison tables, differentiation language, "what we're not"
4. **Brand Pillars** — Look for: values, principles, beliefs, "what we stand for"
5. **Voice & Tone** — Look for: tone descriptors, word lists (do/don't), writing rules, vocabulary tables, guidelines
6. **Product Segments** — Look for: product categories, segment-specific messaging, model-specific content
7. **Key Messages** — Look for: taglines, slogans, power phrases, recurring copy
8. **Content Pillars** — Look for: content themes, editorial calendar, topic categories
9. **Platform Config** — Look for: social URLs, tool names, team members, sign-off patterns
10. **System Prompt** — Look for: existing AI prompts, system instructions, brand brief sections

### Smart Extraction Rules

- Preserve the brand's actual language — do not paraphrase taglines, power phrases, or voice descriptions
- If the document uses a positioning framework (like Four-Wall), map it directly
- If the document has NEVER/ALWAYS lists, extract them verbatim
- If vocabulary tables exist, preserve the exact preferred/avoided pairs
- Flag any areas where the document is ambiguous or missing information

## User Review

After parsing, present the extracted content organized by area:

1. Show each area with what was found
2. Highlight any areas that were **not found** or seem **incomplete**
3. Ask the user to confirm, correct, or expand each area
4. For missing areas, offer to run a mini-interview (like `/brand-setup` but just for the gaps)

## File Creation

Create the same file structure as `/brand-setup`:

1. `brand-os/brand-foundations.md`
2. `brand-os/voice-guidelines.md`
3. `brand-os/content-pillars.md`
4. `brand-os/key-messages.md`
5. `brand-os/platform-config.md`
6. `brand-os/system-prompt.md` (auto-assembled)

## Completion Message

- List all files created
- Note what percentage of the brand profile was populated from the document vs. what's still missing
- Suggest running `/brand-setup` for any gaps
- Suggest trying a content command to see the imported knowledge in action
