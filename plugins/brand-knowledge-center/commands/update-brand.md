# Update Brand

Edit or expand a specific area of your brand knowledge profile without re-running the full setup wizard.

## Before Starting

1. Check if `brand-knowledge-center/` exists in the user's working directory.
   - If it doesn't exist: "You don't have a brand profile yet. Run `/brand-setup` to create one."
   - If it exists: Read all existing files to understand current state.
2. Read the full skill definition at `${CLAUDE_PLUGIN_ROOT}/skills/brand-knowledge/SKILL.md` for field definitions and file templates.

## Determine What to Update

Ask the user what they'd like to update, or detect from their message. Map to the correct area:

| User Says | Area | File |
|-----------|------|------|
| "business", "company info", "team", "roles", "accounting" | Business Overview | `business-overview.md` |
| "financial", "P&L", "balance sheet", "revenue", "margins" | Financial Snapshot | `financial-snapshot.md` |
| "social", "platforms", "tools", "CRM", "website platform" | Digital Ecosystem | `digital-ecosystem.md` |
| "brand", "voice", "tone", "colors", "fonts", "pillars", "guidelines" | Brand Identity | `brand-identity.md` |
| "audience", "messaging", "content pillars", "personas" | Audience & Messaging | `audience-messaging.md` |
| "competitors", "competitive", "market" | Competitive Landscape | `competitive-landscape.md` |
| "everything", "full review" | All areas | All files |

If unclear, present the options:
"Which area would you like to update?"
1. Business Overview — company info, team roles, accounting
2. Financial Snapshot — P&Ls, balance sheets, key metrics
3. Digital Ecosystem — social media, platforms, tools
4. Brand Identity — voice, tone, colors, fonts, pillars
5. Audience & Messaging — personas, messaging frameworks, content pillars
6. Competitive Landscape — competitors, positioning, comparison

## Update Flow

### For a Single Area

1. Read the current file for that area
2. Present the current content in a clean summary
3. Ask: "What would you like to change or add?"
4. Accept the user's input:
   - If they provide specific edits, apply them
   - If they upload a new document (e.g., updated P&L), re-extract and merge
   - If they want to expand a thin section, run the relevant guided questions from the setup wizard
5. Present the updated version for review
6. Once approved, write the updated file
7. Regenerate `system-prompt.md` to reflect the changes

### For "Full Review"

1. Read all files
2. Present a condensed summary of each area (2-3 lines each)
3. Ask: "Which areas need updates?"
4. Walk through each flagged area using the single-area flow above
5. Regenerate `system-prompt.md` after all updates are complete

## Adding New Information

The update command also handles adding entirely new information to an existing profile:

- **New team member:** Add to the Key Team table in `business-overview.md`
- **New financial period:** Upload new P&L, extract metrics, add to the financial timeline in `financial-snapshot.md`
- **New social platform:** Add to the Social Media table in `digital-ecosystem.md`
- **New competitor:** Add to `competitive-landscape.md`, scrape their website if URL provided, update the competitive matrix
- **New audience segment:** Add to `audience-messaging.md`, build a messaging framework for them
- **New brand pillar:** Add to the Brand Pillars table in `brand-identity.md`

## After Every Update

1. Confirm the changes with the user
2. Write the updated file(s)
3. Regenerate `brand-knowledge-center/system-prompt.md` — read all knowledge files and reassemble
4. Notify the user: "Updated {{area}} and regenerated the system prompt. Your brand knowledge center is current."
