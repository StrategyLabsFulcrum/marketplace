# /campaign-launch

Build the media plan, configure all platform campaigns, set up tracking and UTMs, and produce the complete activation package — ready for launch or Rube API execution.

## What This Does

1. Reads the campaign brief and channel strategy from the Campaign Strategist
2. Reads the creative package from the Creative Director
3. Builds the media plan (budget allocation, campaign structure, audience configuration, creative assignment)
4. Sets up tracking — UTM parameters, pixel events, conversion actions
5. Spawns platform specialists (Meta, Google, Email, LinkedIn, TikTok) in parallel
6. Runs pre-launch quality checklist
7. Delivers the complete activation package
8. Produces an analytics handoff brief for the Marketing Analytics Orchestrator

## How to Invoke

**Standard launch — reads campaign brief, builds full activation:**
```
/campaign-launch
```

**Launch for a specific campaign:**
```
/campaign-launch 2026-03-spring-launch
```

**Tracking setup only — creative not ready yet:**
```
/campaign-launch setup-only
```
Sets up UTM structure, verifies pixels, creates conversion events. Media plan and creative assignment deferred until creative is ready.

**Media plan only — not yet executing:**
```
/campaign-launch plan-only
```
Builds and presents the media plan for approval. Does not generate platform setup documents until plan is approved.

**Specific channels only:**
```
/campaign-launch channels: meta, email
```

## What You'll Need

- `campaigns/{{slug}}/strategy/campaign-brief.md` — goal, audience, budget, timeline
- `campaigns/{{slug}}/strategy/channel-strategy.md` — channel mix and budget allocation
- `campaigns/{{slug}}/creative/creative-package.md` — available ad copy and creative assets

Tracking can be configured before creative is ready. Platform campaign setup requires approved creative.

## Output

Everything saved to `campaigns/{{slug}}/activation/`:

```
media-plan.md              ← budget allocation, structure, creative assignments
utm-parameters.md          ← full UTM table for all ads and emails
tracking-verification.md  ← pixel and conversion event verification
meta-setup.md              ← complete Meta campaign configuration
google-setup.md            ← complete Google campaign configuration
email-setup.md             ← email campaign/sequence configuration
launch-checklist.md        ← pre-launch verification, launch approval
analytics-handoff.md       ← brief for Marketing Analytics Orchestrator
```

## Execution Options

**Manual:** Setup documents contain every field needed to configure campaigns in each platform's UI.

**Rube MCP:** If Rube connections are configured, campaigns can be executed directly via the platform APIs. The Performance Marketing Agent will check for existing Rube recipes before building new ones.

**Bulk upload:** Google Ads Editor CSV format available for large Search campaigns.
