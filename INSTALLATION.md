# Brand Content OS — Installation Guide

Welcome! This guide walks you through installing and setting up the Brand Content OS plugin in your Claude Cowork workspace.

## Prerequisites

- An active Claude Cowork (or Claude Code) subscription
- A folder selected in Cowork where your brand files will be stored

## Step 1: Add the Strategy Labs Marketplace

Open Claude Cowork and run:

```
/plugin marketplace add StrategyLabsFulcrum/marketplace
```

This adds the Strategy Labs marketplace to your plugin catalog. You only need to do this once.

## Step 2: Install the Brand Content OS Plugin

```
/plugin install brand-content-os@strategy-labs-plugins
```

After installation, you'll see new slash commands available in your Cowork session.

## Step 3: Set Up Your Brand

You have two options depending on whether you already have brand documentation:

### Option A: Guided Brand Setup (Recommended for New Brands)

Run `/brand-setup` and Claude will walk you through an interactive onboarding wizard covering your brand positioning, voice, vocabulary, competitors, content pillars, and key messages.

### Option B: Import Existing Brand Document

If you already have a brand guide, style guide, or similar document, run `/brand-import`. You can upload the document, paste text, or point to a Google Drive file. Claude will parse it into structured brand knowledge files.

## Step 4: Start Generating Content

Once your brand knowledge is set up, use any of these commands:

| Command | What It Does |
|---------|--------------|
| `/paid-ads` | Generate Meta Ads and Google Ads copy (12 template types) |
| `/email-sms` | Generate Klaviyo email campaigns and SMS messages (7 template types) |
| `/shopify-content` | Generate product pages, collection intros, and blog posts |
| `/content-multiply` | One product or topic becomes 5 assets: blog + email + video script + social + carousel |
| `/brand-audit` | Review any content against your brand voice, flag violations, and get rewrites |

## How Brand Knowledge Is Stored

The plugin creates a `brand-os/` folder in your working directory with these files:

| File | What's In It |
|------|-------------|
| `brand-foundations.md` | Business info, positioning, competitive landscape, brand pillars |
| `voice-guidelines.md` | Tone spectrum, NEVER/ALWAYS lists, vocabulary, quality filter |
| `content-pillars.md` | Content themes and editorial calendar framework |
| `key-messages.md` | Taglines, power phrases, product segment messaging |
| `platform-config.md` | Social channels, tech stack, team sign-offs |
| `system-prompt.md` | Auto-assembled AI prompt (generated from all other files) |

You can edit these files directly at any time. More brand detail = better output.

## Tips for Best Results

- **Start with `/brand-setup` even if it feels thorough.** The more detail you provide upfront, the more on-brand every generated piece will be.
- **Use `/brand-audit` on everything.** It works on content from any source — not just what this plugin generates.
- **Expand over time.** As you use the plugin and notice where content could be sharper, go back and add detail to your brand files.
- **Share the `brand-os/` folder with your team.** If stored in Google Drive, multiple team members can contribute to and benefit from the same brand knowledge.

## Updating the Plugin

When Strategy Labs releases updates, run:

```
/plugin marketplace update strategy-labs-plugins
```

Then reinstall to get the latest version:

```
/plugin install brand-content-os@strategy-labs-plugins
```

## Need Help?

Contact scott@strategylabs.us for support.
