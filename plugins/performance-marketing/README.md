# Performance Marketing

Translates campaign strategy and creative packages into live paid media. The Performance Marketing Agent builds the media plan, configures campaigns across all platforms, sets up tracking and UTMs, and executes optimization actions from the Marketing Analytics Orchestrator.

**The Performance Marketing Agent does not write copy or design assets.** Those come from the Creative Director and Art Director. It takes their outputs and turns them into operational campaigns.

## What It Does

1. Reads the campaign brief (Campaign Strategist) and creative package (Creative Director)
2. Builds the media plan — budget allocation, campaign structure, audience tiers, creative assignment
3. Sets up tracking — UTM parameters, platform pixels, conversion events
4. Spawns platform specialists in parallel to configure each channel
5. Runs a pre-launch quality checklist before authorizing any campaign to go live
6. Executes optimization actions from the Marketing Analytics Orchestrator on live campaigns
7. Maintains an optimization log — a complete audit trail of every change made

## Commands

| Command | What It Does |
|---------|-------------|
| `/campaign-launch` | Build media plan, configure all channels, set up tracking — complete activation package |
| `/campaign-optimize` | Execute optimization actions from Marketing Analytics on live campaigns |

## Platform Specialists (Spawned in Parallel)

| Specialist | Handles |
|-----------|---------|
| Meta Ads Specialist | Facebook/Instagram — campaign setup, audiences, creative assignment, bid strategy |
| Google Ads Specialist | Search, Display, Shopping, Performance Max — keywords, ad groups, bidding, extensions |
| Email Campaign Specialist | Klaviyo/Mailchimp — campaign config, sequence logic, segments, deliverability |
| LinkedIn Ads Specialist | B2B targeting, campaign structure, creative assignment |
| TikTok Ads Specialist | Video campaign setup, targeting, creative requirements |

## How It Fits

```
Campaign Strategist → campaign-brief.md + channel-strategy.md
                                ↓
Creative Director → creative-package.md
                                ↓
Performance Marketing Agent
  → media-plan.md
  → tracking setup (UTMs, pixels, conversion events)
  → platform specialists (parallel)
      ├── meta-setup.md
      ├── google-setup.md
      ├── email-setup.md
      └── [others]
  → launch-checklist.md
  → analytics-handoff.md → Marketing Analytics Orchestrator
                                ↑
Marketing Analytics → optimization-actions.md
                                ↓
Performance Marketing Agent (/campaign-optimize)
  → optimization-log.md (every change documented)
```

## Output Structure

```
campaigns/{{slug}}/activation/
├── media-plan.md              ← budget allocation, campaign structure, KPIs by channel
├── utm-parameters.md          ← every URL tagged — no untagged traffic
├── tracking-verification.md  ← pixel + conversion event verification checklist
├── meta-setup.md              ← complete Meta Ads configuration
├── google-setup.md            ← complete Google Ads configuration
├── email-setup.md             ← email campaign/sequence configuration
├── [channel]-setup.md         ← additional channels
├── launch-checklist.md        ← pre-launch approval gate
├── analytics-handoff.md       ← brief for Marketing Analytics Orchestrator
└── optimization-log.md        ← running log of every campaign change
```

## Execution Options

| Option | How |
|--------|-----|
| Manual | Setup documents contain every field needed to configure campaigns in each platform's UI |
| Rube MCP | Direct API execution via Meta Marketing API, Google Ads API, Klaviyo API — when configured |
| Bulk upload | Google Ads Editor CSV for large Search campaigns |

## Key Principles

**Tracking first:** No campaign launches without verified tracking. A week of untracked data is permanently lost.

**Learning phase discipline:** During the platform learning phase (first 50 conversions per ad set), do not make budget changes above 20%, do not change targeting, do not change creative. Every significant change resets the learning phase.

**Budget discipline:** Never exceed approved budget. Always hold 10–15% as optimization reserve.

**Document everything:** Every change to a live campaign is logged. This is how Marketing Analytics understands performance shifts, and how the team learns what works.

## Plugin Dependencies

- **brand-intelligence-center** (required) — brand context, website URL, conversion events
- **campaign-strategist** (required) — campaign brief, channel strategy, KPI targets
- **creative-director** (recommended) — creative package with approved copy and assets
- **marketing-analytics** (recommended) — optimization actions to execute on live campaigns
