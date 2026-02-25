---
description: Set up brand knowledge for a new client through guided onboarding
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# Brand Setup — Guided Onboarding

Walk the user through capturing their brand knowledge to power the Brand & Content OS. This creates structured brand files that all other commands use for on-brand content generation.

## Before Starting

1. Check if a `brand-os/` directory already exists in the user's working folder.
   - If it exists and has files, inform the user: "You already have brand knowledge set up. Would you like to update specific sections, or start fresh?"
   - If starting fresh, back up existing files by renaming the folder to `brand-os-backup-[date]/`.
2. Create the `brand-os/` directory if it doesn't exist.

## Onboarding Flow

Guide the user through these 10 areas using AskUserQuestion for structured choices and conversational follow-ups for open-ended answers. For each area, accept brief answers — the user can always come back and expand later.

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

## File Creation

After all areas are complete (or the user chooses to proceed with what's been captured), create these files in the `brand-os/` directory:

1. **brand-foundations.md** — Areas 1-4 (business snapshot, positioning, competitors, pillars)
2. **voice-guidelines.md** — Area 5 (tone, never/always lists, vocabulary, quality filter)
3. **content-pillars.md** — Area 8 (content themes and calendar)
4. **key-messages.md** — Areas 6-7 (segments, taglines, power phrases)
5. **platform-config.md** — Area 9 (social, tech stack, team)
6. **system-prompt.md** — Area 10 (auto-assembled from all other files)

## Completion Message

After files are created:
- List all files created with a brief description of each
- Note any areas that were skipped or left brief, and suggest the user can expand them later by editing the files directly or running `/brand-setup` again
- Suggest trying `/paid-ads` or `/content-multiply` to see the brand knowledge in action
- Remind the user that the more detail in their brand files, the better the content generation will be
