---
description: Review content against brand voice and rewrite to fix violations
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
argument-hint: "<file path or paste content>"
---

# Voice Check — Brand Voice Review & Rewrite

Review any piece of content against the brand's voice guidelines, flag violations, and rewrite to align with the brand identity. This is the quality control command for the Brand & Content OS.

## Before Auditing

0. **Check configuration**: Look for `.brand-os-config.md` in the working directory (the same directory that contains `brand-os/`). If found, read it to determine storage mode and output directories. If `mode` is `fast.io` and `auto_pull_on_start` is `true`, check `last_pull`. If stale (older than 24 hours or missing), inform the user: "Your local brand files haven't been synced in [X hours/days]. Run `/sync-brand-os pull` to get the latest from Fast.io, or continue with the local copy." Proceed with local files regardless — never block content generation on sync. If no config file is found, continue with default behavior.

1. **Load brand knowledge**: Read these files from `brand-os/`:
   - `voice-guidelines.md` (NEVER list, ALWAYS list, vocabulary, quality filter, tone spectrum)
   - `brand-foundations.md` (positioning, pillars, competitive landscape)
   - `key-messages.md` (preferred phrases and messaging)
   If missing, suggest running `/new-brand-setup` first.

2. **Get the content to audit**:
   - If `$ARGUMENTS` contains a file path, read that file
   - If the user pastes content directly, use the pasted text
   - If the user references a file in their folder, find and read it
   - Ask the user to provide content if nothing is available

## Audit Process

### Step 1: NEVER List Scan
Check every word and phrase in the content against the brand's NEVER list.
- Flag each violation with the specific word/phrase and its location
- Note why it's prohibited (if context is available from voice guidelines)

### Step 2: ALWAYS List Verification
Check the content against each item in the brand's ALWAYS list:
- Does it lead with experience/performance (not specs/price)?
- Does it address the reader as a peer?
- Does it reference real scenarios or specifics?
- Does it include a Brand Recommendation where applicable?
- Does it have a brand-aligned CTA?
Mark each ALWAYS rule as passed or failed.

### Step 3: Vocabulary Check
Cross-reference the content against the brand's vocabulary reference:
- Flag any "Not This" terms that should be replaced with "Use This" alternatives
- Note generic language that could be elevated with brand-specific terms

### Step 4: Tone Assessment
Evaluate the overall tone against the brand's tone spectrum:
- Is the authority level right?
- Is the energy level right?
- Does it use appropriate brand-voice language patterns?
- Does it sound like it could come from a competitor? (If yes, flag it)

### Step 5: Quality Filter
Apply the brand's quality filter questions:
- Run each question from the quality filter against the content
- Note pass/fail for each

### Step 6: Competitive Guardrail
Check if the content could be mistaken for a competitor's:
- Reference the competitive positioning from brand-foundations.md
- If the content sounds like it could belong to any listed competitor, flag it

## Output Format

```
# Voice Check Report

## Content Reviewed
[First 50 words of the content or the file name]

## Scorecard

| Check | Status | Issues Found |
|-------|--------|-------------|
| NEVER List | pass/fail | [count] violations |
| ALWAYS List | pass/fail | [count] items failed |
| Vocabulary | pass/fail | [count] terms to replace |
| Tone | pass/fail | [notes] |
| Quality Filter | pass/fail | [which questions failed] |
| Competitive Guard | pass/fail | [notes] |

## Detailed Findings

### NEVER List Violations
| Found | Location | Replace With |
|-------|----------|-------------|
| "[word]" | [where in text] | [suggested replacement] |

### ALWAYS List Failures
- [Rule]: [What's missing or wrong]

### Vocabulary Swaps
| Current | Should Be | Reasoning |
|---------|-----------|-----------|
| "[term]" | "[preferred]" | [from vocabulary reference] |

### Tone Notes
[Assessment of overall tone alignment]

---

## Rewritten Version

[Complete rewritten content with all violations fixed, vocabulary elevated, tone aligned, and brand voice fully applied]

---

## Changes Summary
- [X] NEVER list words removed
- [X] vocabulary terms upgraded
- [X] ALWAYS list items addressed
- Tone adjusted: [description of tone changes]
```

## Auto-Save

After presenting the audit, if `.brand-os-config.md` was found and specifies an output directory for `brand_audits` (default: `brand-audits/`), automatically save the audit report and rewritten version as a markdown file. Use the naming convention: `{content-name}-voice-check-{YYYY-MM-DD}.md`. Overwrite if the file already exists. Inform the user: "Saved to `brand-audits/{filename}`."

If no config file was found, offer to save the rewritten version as a file (current behavior).

## Follow-Up

After presenting the audit:
- Ask if the user wants to adjust any of the rewrites
- Offer to check additional content
- If many violations were found, suggest reviewing and expanding the brand knowledge files
