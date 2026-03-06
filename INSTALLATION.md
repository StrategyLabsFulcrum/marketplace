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

Run `/new-brand-setup` and choose your path:

- **Import a document** — Upload or paste an existing brand guide, style guide, or playbook
- **Share a URL** — Point to a website or online brand resource
- **Answer questions** — Walk through a guided interview about your brand

Claude will create structured brand knowledge files from whichever path you choose. During setup, you'll also be asked whether to store files locally or sync to Fast.io for team collaboration.

## Step 4: Start Generating Content

Once your brand knowledge is set up, use any of these commands:

| Command | What It Does |
|---------|--------------|
| `/paid-ads` | Generate Meta Ads and Google Ads copy (12 template types) |
| `/email-sms` | Generate Klaviyo email campaigns and SMS messages (7 template types) |
| `/shopify-content` | Generate product pages, collection intros, and blog posts |
| `/content-multiply` | One product or topic becomes 5 assets: blog + email + video script + social + carousel |
| `/voice-check` | Review any content against your brand voice, flag violations, and get rewrites |
| `/sync-brand-os` | Sync brand knowledge between local files and Fast.io for team collaboration |

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

- **Be thorough during `/new-brand-setup`.** The more detail you provide upfront, the more on-brand every generated piece will be.
- **Use `/voice-check` on everything.** It works on content from any source — not just what this plugin generates.
- **Expand over time.** As you use the plugin and notice where content could be sharper, go back and add detail to your brand files.
- **Sync with your team.** Use `/sync-brand-os` to share brand files via Fast.io so multiple team members can collaborate on the same brand knowledge.
- **Run `/sync-brand-os pull` at session start** when working with a team to ensure you have the latest brand files.

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
