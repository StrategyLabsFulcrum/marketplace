# /campaign-new

Start a new campaign from scratch. The Campaign Strategist guides you through goal, audience, budget, channels, and timeline — then builds your complete campaign brief and handoff documents for the Creative Director and Performance Marketing Agent.

## What This Does

Runs the full Campaign Strategist intake and strategy workflow:

1. Loads your brand intelligence and any existing competitive data
2. Walks through campaign goal, audience, budget, and timeline (3 focused question groups)
3. Recommends a channel mix with budget allocation
4. Builds the KPI framework with baselines and targets
5. Produces the master Campaign Brief + handoff briefs
6. Optionally spawns Creative Director and Performance Marketing Agent in parallel

**Output:** A `campaigns/{{campaign-slug}}/` folder with all strategy documents ready for execution.

## When to Use

- Starting any new marketing campaign
- Planning a product or feature launch
- Building a seasonal or promotional campaign
- Responding to a competitive threat
- Kicking off a retention or winback push

## How to Invoke

```
/campaign-new
```

Then answer the guided questions. Have ready:
- Your campaign goal (what you're trying to achieve)
- A rough budget range (or say "recommend one")
- Target launch date

## Tips

- The more context you give on the goal and offer, the sharper the strategy
- Competitive intelligence from `/competitive-landscape` makes the channel strategy much stronger — run that first if you haven't
- You can approve the brief and spawn child agents immediately, or review and edit first
- All outputs save to `campaigns/{{slug}}/` — nothing is lost if you pause mid-session
