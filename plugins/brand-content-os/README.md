# Brand & Content OS

A plugin that captures brand knowledge and generates on-brand content across paid ads, email, SMS, Shopify, and social channels. Built by Strategy Labs.

## What It Does

The Brand & Content OS has two layers:

1. **Brand Knowledge Layer** — Structured files that capture everything about a brand (positioning, voice, vocabulary, competitors, content pillars, key messages). These power all content generation.
2. **Content Generation Layer** — Platform-specific prompt templates that combine brand knowledge with per-use inputs to generate consistent, on-brand content.

Once brand knowledge is set up, every piece of generated content automatically follows the brand's voice rules, uses preferred vocabulary, avoids prohibited language, and aligns with the brand's positioning.

## Commands

| Command | Description |
|---------|-------------|
| `/brand-setup` | Guided onboarding wizard — captures brand knowledge through interactive questions |
| `/brand-import` | Parse an existing brand document (upload, paste, or Google Drive) into structured brand files |
| `/paid-ads` | Generate Meta Ads and Google Ads content (12 template types) |
| `/email-sms` | Generate Klaviyo email campaigns and SMS messages (7 template types) |
| `/shopify-content` | Generate product pages, collection intros, and blog posts |
| `/content-multiply` | The Multiplier — one product or topic → blog + email + video script + social + carousel |
| `/brand-audit` | Review any content against brand voice, flag violations, and rewrite |

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **Run `/brand-setup`** to create your brand profile through guided questions, OR run `/brand-import` if you already have a brand document
3. **Start generating** with `/paid-ads`, `/email-sms`, `/shopify-content`, or `/content-multiply`
4. **Quality check** any content with `/brand-audit`

## Brand Knowledge Files

Brand knowledge is stored in a `brand-os/` folder with these files:

| File | Contents |
|------|----------|
| `brand-foundations.md` | Business info, positioning, competitive landscape, brand pillars |
| `voice-guidelines.md` | Tone spectrum, NEVER list, ALWAYS list, vocabulary, quality filter |
| `content-pillars.md` | Content themes, editorial calendar framework |
| `key-messages.md` | Taglines, power phrases, product segment messaging |
| `platform-config.md` | Social channels, tech stack, team sign-offs |
| `system-prompt.md` | Auto-assembled AI foundation prompt (generated from all other files) |

These files can also be stored in Google Drive for team collaboration.

## Content Templates

The plugin includes 25+ prompt templates covering:

- **Meta Ads** (6): Ad copy variations, dynamic creative, retargeting, DCA templates, prospecting
- **Email** (5): Welcome series, abandoned cart, newsletter, product launch, win-back
- **SMS** (2): Product drop alerts, VIP exclusive offers
- **Google Ads** (6): RSA headlines, shopping feed, Performance Max, title optimization, description enhancement, negative keywords
- **Shopify** (2): Product pages, collection pages
- **Master Templates** (2): Content Multiplier (1→5 assets), Brand Voice Audit

## Tips

- **More brand detail = better output.** The richer your brand knowledge files, the more on-brand the generated content will be.
- **Expand over time.** Start brief, then add detail as you use the plugin and notice where content could be more specific.
- **Edit brand files directly.** You can open and edit any file in the `brand-os/` folder to refine your brand knowledge.
- **Use `/brand-audit` regularly.** It's great for reviewing content from any source — not just content this plugin generated.
