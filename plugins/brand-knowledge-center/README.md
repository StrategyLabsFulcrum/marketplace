# Brand Knowledge Center

A setup wizard that builds a comprehensive brand profile through a guided, step-by-step onboarding process. The output is a structured `brand-knowledge-center/` folder of markdown files that serves as the foundation for all Strategy Labs marketplace plugins.

Built by Strategy Labs.

## What It Does

The Brand Knowledge Center walks brand owners through a complete business and brand onboarding:

1. **Business Foundation** — Website, industry identification, accounting approach, key team roles
2. **Financial Context** — P&L and balance sheet uploads with automatic metric extraction
3. **Digital Presence** — Social media URLs (scraped or manual), website platform, CRM, email/SMS tools
4. **Brand Identity** — Upload existing guidelines or answer guided questions (fonts, colors, pillars, messaging)
5. **Audience & Messaging** — Target audiences and messaging frameworks (suggested or custom)
6. **Competitive Landscape** — Competitors identified and confirmed, with URLs and positioning notes
7. **Review & Generate** — Review all collected information, generate the system prompt

## Output

```
brand-knowledge-center/
├── business-overview.md        # Company info, industry, accounting, key roles
├── financial-snapshot.md       # Key metrics extracted from P&Ls and balance sheets
├── digital-ecosystem.md        # Social URLs, website platform, CRM, tools
├── brand-identity.md           # Brand guidelines, fonts, colors, pillars, messaging
├── audience-messaging.md       # Target audiences, personas, messaging frameworks
├── competitive-landscape.md    # Competitors, URLs, positioning comparison
└── system-prompt.md            # Auto-assembled brand context for AI tools
```

## Commands

| Command | Description |
|---------|-------------|
| `/brand-setup` | Run the full setup wizard — import documents, scrape your website, or answer guided questions |
| `/update-brand` | Edit or expand a specific area without re-running the full wizard |

## Getting Started

1. Install the plugin
2. Run `/brand-setup`
3. Follow the step-by-step wizard
4. Use the generated `brand-knowledge-center/` folder as context for any other Strategy Labs plugin

## Why This Exists

Most Strategy Labs plugins — competitive landscape analysis, local business marketing, content generation, customer-driven optimizations — need brand context to deliver high-value results. Instead of each plugin asking the same onboarding questions, run Brand Knowledge Center once and every plugin can reference the output.
