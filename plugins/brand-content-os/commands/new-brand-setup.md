---
description: Create a new brand profile — import from an existing document or build from scratch through guided questions
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
---

# New Brand Setup

Create a complete brand knowledge profile that powers all content generation commands. Choose your path: import from an existing brand document, or build from scratch through guided questions.

## Before Starting

1. Check if a `brand-os/` directory already exists in the user's working folder.
   - If it exists and has files, inform the user: "You already have brand knowledge set up. Would you like to update specific sections, or start fresh?"
   - If starting fresh, back up existing files by renaming the folder to `brand-os-backup-[date]/`.
2. Create the `brand-os/` directory if it doesn't exist.

## Choose Your Path

Ask the user how they'd like to set up their brand profile:

- **Import a document** — "I have a brand playbook, style guide, or brand document to work from"
- **Share a URL** — "I have a website or online brand resource to pull from"
- **Answer questions** — "I'll walk through guided questions about my brand"

Route to the appropriate path below.

---

## Path A: Import from Document

### Get the Document

Ask the user how they want to provide it:
- **Upload a file** — Look for the file in the uploads directory or the user's working folder
- **Paste the content** — Accept pasted text directly in the conversation

### Parse the Document

Read the source document and extract content into the 10 brand knowledge areas defined in `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/brand-profile-schema.md`.

**Extraction mapping** — for each area, scan for:

1. **Business Snapshot** — company name, website, team names, revenue, platforms, industry
2. **Core Positioning** — mission statements, value propositions, positioning frameworks, "about us" language
3. **Competitive Positioning** — competitor mentions, comparison tables, differentiation language
4. **Brand Pillars** — values, principles, beliefs, "what we stand for"
5. **Voice & Tone** — tone descriptors, word lists (do/don't), writing rules, vocabulary tables
6. **Product Segments** — product categories, segment-specific messaging
7. **Key Messages** — taglines, slogans, power phrases, recurring copy
8. **Content Pillars** — content themes, editorial calendar, topic categories
9. **Platform Config** — social URLs, tool names, team members, sign-off patterns
10. **System Prompt** — existing AI prompts, system instructions, brand brief sections

**Smart extraction rules:**
- Preserve the brand's actual language — do not paraphrase taglines, power phrases, or voice descriptions
- If the document uses a positioning framework (like Four-Wall), map it directly
- If the document has NEVER/ALWAYS lists, extract them verbatim
- If vocabulary tables exist, preserve the exact preferred/avoided pairs
- Flag any areas where the document is ambiguous or missing information

### Review Extracted Content

Present the extracted content organized by area:

1. Show each area with what was found
2. Highlight any areas that were **not found** or seem **incomplete**
3. Ask the user to confirm, correct, or expand each area
4. For missing areas, run a mini-interview using the guided questions from Path C (just for the gaps)

Then proceed to **File Creation**.

---

## Path B: Import from URL

Ask the user for the URL (website, online brand guide, etc.). Fetch the content and follow the same parsing process as Path A.

If the URL is a website homepage or about page, extract what's available and note which brand areas need more detail. Offer to fill gaps using guided questions from Path C.

Then proceed to **File Creation**.

---

## Path C: Guided Questions

Walk the user through these 10 areas using AskUserQuestion for structured choices and conversational follow-ups for open-ended answers. For each area, accept brief answers — the user can always come back and expand later.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/brand-profile-schema.md` for the complete field definitions and gathering prompts for each area.

### Area 1: Business Snapshot
Gather: Brand name, website, owner/founder, approximate revenue, platform/tech stack, team members and roles, industry/category.

### Area 2: Core Positioning
Gather the Four-Wall Positioning Framework:
- Core Promise (the internal truth — not a tagline)
- Target Audience (mindset and identity, not demographics)
- Category (what they sell as an experience)
- Point of Difference (what only they can claim)
- Reason to Believe (proof behind the claim)

### Area 3: Competitive Positioning
Gather 3-5 competitors with:
- Their name
- Their archetype (how they position themselves)
- The brand's counter-position (how this brand is fundamentally different)

### Area 4: Brand Pillars
Gather 3-5 non-negotiable brand principles. Each needs a name, description, and how it shows up in practice.

### Area 5: Voice & Tone
Gather:
- 4-6 voice traits on a spectrum (trait, approach, in practice)
- The NEVER list (words, phrases, patterns to absolutely avoid)
- The ALWAYS list (rules that apply to every piece of content)
- Vocabulary reference (preferred terms vs. avoided terms)
- Quality filter (2-3 litmus test questions for pre-publish review)

### Area 6: Product Segments
If the brand has distinct product lines or categories, gather segment-specific messaging:
- Segment name
- Core "reason to believe" for that segment
- Key vocabulary unique to that segment

If not applicable, note this and move on.

### Area 7: Key Messages & Power Phrases
Gather:
- 3-6 core taglines
- Reusable power phrases with guidance on best platforms/contexts

### Area 8: Content Pillars
Gather 3-6 content themes:
- Pillar name, core purpose, primary emotion, example topics

Optionally: A repeating content calendar framework (weekly or monthly rotation).

### Area 9: Platform Configuration
Gather:
- Social channel URLs and primary use per platform
- Tech stack (eCommerce platform, email tool, etc.)
- Team sign-off style for emails/content

### Area 10: Review & System Prompt Assembly
- Summarize everything captured across all areas
- Show the user a preview of each brand file
- Ask for corrections or additions
- Generate the `system-prompt.md` file by assembling all brand knowledge into a master AI system prompt

Then proceed to **File Creation**.

---

## File Creation

After all areas are complete (or the user chooses to proceed with what's been captured), create these files in the `brand-os/` directory:

1. **brand-foundations.md** — Areas 1-4 (business snapshot, positioning, competitors, pillars)
2. **voice-guidelines.md** — Area 5 (tone, never/always lists, vocabulary, quality filter)
3. **content-pillars.md** — Area 8 (content themes and calendar)
4. **key-messages.md** — Areas 6-7 (segments, taglines, power phrases)
5. **platform-config.md** — Area 9 (social, tech stack, team)
6. **system-prompt.md** — Area 10 (auto-assembled from all other files)

## Configuration & Storage Setup

After brand files are created, set up the configuration file and output directories.

### 1. Ask About Storage

Ask the user: "Where should these brand files be stored long-term?"

- **Local only** — Files stay on this machine. No sync needed.
- **Fast.io** — Files sync to a Fast.io workspace for team collaboration.

If the user declines or wants to skip this step, that's fine — all commands work without a config file. Move to the Completion Message.

### 2. Create `.brand-os-config.md`

Create the file one level above the `brand-os/` directory (in the same directory that contains `brand-os/`).

**If Local:**

```markdown
# Brand OS Configuration

## Storage
- **mode:** local

## Sync
- **last_pull:** —
- **last_push:** —
- **auto_pull_on_start:** false

## Output Directories
- **paid_ads:** paid-ads/
- **email_sms:** email-sms/
- **social:** social/
- **shopify:** shopify/
- **content_bundles:** content-bundles/
- **brand_audits:** brand-audits/
```

**If Fast.io:**

Ask the user for their Fast.io workspace ID, or offer to create a new workspace using the Fast.io MCP tools (`org create-workspace`). Then create:

```markdown
# Brand OS Configuration

## Storage
- **mode:** fast.io
- **workspace_id:** [user's workspace ID]
- **workspace_name:** [workspace name]

## Sync
- **last_pull:** —
- **last_push:** —
- **auto_pull_on_start:** true

## Output Directories
- **paid_ads:** paid-ads/
- **email_sms:** email-sms/
- **social:** social/
- **shopify:** shopify/
- **content_bundles:** content-bundles/
- **brand_audits:** brand-audits/
```

After creating the config, automatically push all brand files to the Fast.io workspace using `upload text-file` for each file in `brand-os/`. Update `last_push` with the current timestamp.

### 3. Create Output Directories

Create these directories in the same parent folder as `brand-os/`:
- `paid-ads/`
- `email-sms/`
- `social/`
- `shopify/`
- `content-bundles/`
- `brand-audits/`

## Completion Message

After files are created:
- List all files created with a brief description of each
- If a config file was created, confirm the storage mode and list the output directories
- If content was imported from a document, note what percentage of the brand profile was populated vs. what's still missing
- Note any areas that were skipped or left brief, and suggest the user can expand them later by editing the files directly or running `/new-brand-setup` again
- Suggest trying `/paid-ads` or `/content-multiply` to see the brand knowledge in action
- If Fast.io mode is configured, mention they can use `/sync-brand-os` to keep files in sync across sessions
- Remind the user that the more detail in their brand files, the better the content generation will be
