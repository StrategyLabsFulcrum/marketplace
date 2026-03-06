---
description: Generate Klaviyo email campaigns and SMS messages using brand knowledge
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
argument-hint: "<email type or product name>"
---

# Email & SMS — Klaviyo + SMS Content Generation

Generate on-brand email campaigns and SMS messages. Automatically applies brand knowledge, voice rules, and platform-specific best practices.

## Before Generating

0. **Check configuration**: Look for `.brand-os-config.md` in the working directory (the same directory that contains `brand-os/`). If found, read it to determine storage mode and output directories. If `mode` is `fast.io` and `auto_pull_on_start` is `true`, check `last_pull`. If stale (older than 24 hours or missing), inform the user: "Your local brand files haven't been synced in [X hours/days]. Run `/sync-brand-os pull` to get the latest from Fast.io, or continue with the local copy." Proceed with local files regardless — never block content generation on sync. If no config file is found, continue with default behavior.

1. **Load brand knowledge**: Read all files from the `brand-os/` directory. If missing, suggest running `/new-brand-setup` first.
2. **Load the system prompt**: Read `brand-os/system-prompt.md` as foundational context.
3. **Load references**:
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/platform-prompts.md` (Email and SMS sections)
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/best-practices.md` (Email and SMS sections)

## Gather Inputs

Ask the user what they need:

1. **Channel**: Email, SMS, or both?
2. **Content type** (based on channel):

   **Email options:**
   - Welcome Series (Email 1)
   - Abandoned Cart Reminder
   - Newsletter
   - New Product Launch
   - Win-Back Campaign

   **SMS options:**
   - New Product Drop Alert
   - Exclusive Offer (VIP/Community)

3. **Product name** (if applicable): What product is featured? (Use `$ARGUMENTS` if provided.)
4. **Email type details** (if newsletter): What product or topic should be featured this week?
5. **Offer details** (if SMS exclusive): What's the offer or early access?

## Generation Process

1. Select the appropriate prompt template from platform-prompts reference
2. Populate auto-variables from brand knowledge files
3. Insert per-use variables from user input
4. Apply the team sign-off style from `brand-os/platform-config.md`
5. Generate content following all brand voice rules
6. NEVER list check — scan for prohibited words/phrases
7. Quality filter check
8. For emails: Verify mobile-friendly formatting (short paragraphs, aggressive line breaks)
9. For SMS: Verify character count is under 160 including link placeholder

## Output Format

### For Emails:

```
## Email — [Type]
### For: [Product Name or Topic]

**Subject Line Options:**
A: [Option A]
B: [Option B]

**Preview Text:** [Preview text]

---

[Email body content with formatting]

---

**Sign-off:** [Team sign-off from brand knowledge]

---
**Brand Voice Check**: ✓ No NEVER list violations | ✓ Quality filter passed
**Word Count**: [X] words
**Mobile Readiness**: ✓ Short paragraphs, single CTA
```

### For SMS:

```
## SMS — [Type]
### For: [Product Name or Offer]

**Message:**
[SMS content] [LINK]

**Character Count**: [X]/160
---
**Brand Voice Check**: ✓ No NEVER list violations
```

## Auto-Save

After presenting the content, if `.brand-os-config.md` was found and specifies an output directory for `email_sms` (default: `email-sms/`), automatically save the generated content as a markdown file. Use the naming convention: `{product-or-topic}-{type}-{YYYY-MM-DD}.md` (e.g., `radius-rods-welcome-email-2026-03-06.md` or `march-newsletter-2026-03-06.md`). Overwrite if the file already exists. Inform the user: "Saved to `email-sms/{filename}`."

If no config file was found, offer to save as a markdown file (current behavior).

## Follow-Up

After presenting:
- For Welcome Series: Offer to generate Emails 2-5 of the series
- For Abandoned Cart: Offer to generate the follow-up reminders (24hr, 72hr)
- Offer to create matching SMS for any email (or vice versa)
- Offer to generate the same email type for a different product
