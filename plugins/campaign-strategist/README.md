# Campaign Strategist

The primary orchestrator for campaign planning and go-to-market strategy. Transforms a campaign goal into a complete, actionable brief that every downstream agent — Creative Director, Performance Marketing, SEO, Email — can execute from.

## What It Does

1. **Loads brand context** — reads brand-intelligence-center before touching strategy
2. **Checks competitive intelligence** — pulls competitive-landscape data to inform messaging and channel decisions
3. **Runs structured intake** — collects campaign goal, audience, budget, timeline, and channels in 3 focused question groups
4. **Builds the strategy** — campaign type classification, audience brief, messaging territory, channel mix with budget allocation
5. **Produces the KPI framework** — primary KPIs with baselines and targets before any creative begins
6. **Writes the Campaign Brief** — the master document every downstream agent reads
7. **Produces handoff briefs** — structured Creative Brief and Performance Brief for parallel agent spawning
8. **Coordinates execution** — spawns Creative Director and Performance Marketing Agent in parallel with user approval

## Output Structure

```
campaigns/
└── {{campaign-slug}}/
    ├── campaign-brief.md       ← master strategy document (all agents read this)
    ├── channel-strategy.md     ← channel-by-channel expanded plan
    ├── kpi-framework.md        ← measurement plan with baselines and targets
    ├── timeline.md             ← phases, milestones, and checklist
    ├── creative-brief.md       ← handoff to Creative Director
    └── performance-brief.md    ← handoff to Performance Marketing Agent
```

## Commands

| Command | What It Does |
|---------|-------------|
| `/campaign-new` | Start a new campaign — full intake and strategy build |
| `/campaign-list` | List all campaigns with status, type, dates, and budget |

## How It Fits in the System

The Campaign Strategist sits at the top of the execution stack. It runs **after** Brand Strategist and Competitive Intelligence have done their work, and **before** any creative or paid media work begins.

```
[Brand Intelligence Center]     ← always loads first
         ↓
[Competitive Research Agent]    ← informs messaging + channel strategy
         ↓
[Campaign Strategist]           ← builds the brief (this plugin)
         ↓              ↓
[Creative Director]    [Performance Marketing]   ← run in parallel
```

## Plugin Dependencies

- **brand-intelligence-center** (required) — provides brand context, customer profile, differentiation, and proof points
- **competitive-landscape** (recommended) — ad analysis and journey data sharpen channel and messaging strategy

## Campaign Types Supported

| Type | Example |
|------|---------|
| Acquisition | "Drive new customer purchases from cold audiences" |
| Launch | "Launch our new product to existing and new audiences" |
| Promotional | "Black Friday sale — maximize revenue in 5 days" |
| Lead Generation | "Fill the sales pipeline with qualified B2B leads" |
| Retention | "Increase repeat purchase rate among 90-day buyers" |
| Winback | "Reactivate customers who haven't bought in 180+ days" |
| Brand / Awareness | "Build awareness in a new geographic market" |
| Competitive Response | "Counter a competitor's aggressive pricing campaign" |

## Requirements

- Cowork mode with folder access
- Brand Intelligence Center (run `/brand-setup` first if not set up)
- Competitive Landscape plugin (optional but recommended)
