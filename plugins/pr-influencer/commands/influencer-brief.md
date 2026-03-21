# /influencer-brief

Create a complete influencer campaign structure — creator roster criteria, vetting checklist, per-creator briefs, tracking setup, and budget allocation — for a brand partnership campaign.

## How to Invoke

**New influencer campaign from a campaign brief:**
```
/influencer-brief campaigns/2026-03-spring-launch/brief.md
```

**Standalone with inline description:**
```
/influencer-brief product launch targeting wellness micro-influencers on Instagram and TikTok, $15k budget
```

**Specific creator evaluation:**
```
/influencer-brief vet @[handle] for spring launch campaign
```

**Ambassador program design:**
```
/influencer-brief ambassador-program
```

## What You Get

- Campaign strategy overview (tiers, budget allocation, platform split)
- Creator vetting criteria tailored to the campaign audience and objective
- Suggested creator tier and quantity breakdown
- Per-creator brief template (filled in for each confirmed creator)
- Tracking setup: UTM parameters + promo codes per creator
- FTC compliance checklist
- Whitelisting/paid amplification notes (if applicable)

## Output Location

All files saved to `campaigns/[slug]/pr-influencer/`:
```
strategy-overview.md
creator-roster.md
creator-brief-[handle].md     ← one per creator
tracking-setup.md
```
