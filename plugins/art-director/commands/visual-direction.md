# /visual-direction

Develop the visual direction system for a campaign, then brief and spawn the appropriate design specialists. This is the Art Director's primary workflow — from creative concept to complete design package.

## What This Does

1. Loads brand intelligence and design-system/ history
2. Reads the creative concept from the Creative Director
3. Develops the full visual direction system (color, typography, photography, layout, motif, motion)
4. Presents the visual direction for approval before briefing anyone
5. Determines which design specialists are needed based on the channel list
6. Issues tailored, self-contained briefs to each specialist
7. Spawns all specialists in parallel
8. Reviews all outputs against the visual direction system
9. Updates the persistent design-system/ folder
10. Assembles and delivers the design package

## How to Invoke

**Campaign mode — reads brief from Campaign Strategist and creative concept from Creative Director:**
```
/visual-direction
```
The Art Director will ask which campaign to work from, then load the relevant files.

**With a specific campaign slug:**
```
/visual-direction 2026-03-spring-launch
```

**Standalone mode — no existing campaign:**
```
/visual-direction standalone
```
The Art Director will collect context directly: brand, campaign goal, channels in scope, creative direction (if any), and any brand standards to reference.

**Visual direction only — develop the system and stop (no briefs, no specialists):**
```
/visual-direction direction-only
```
Useful when you want to review and refine the visual direction before committing to design execution.

## What You'll Be Asked to Approve

Before any specialist is briefed, the Art Director presents the visual direction system for review:

- Color treatment (palette, ratios, background approach)
- Typography direction (font stack, hierarchy, treatments)
- Photography / illustration style
- Layout principles and composition approach
- Campaign visual motif
- Channel adaptation rules
- Key guardrails

You can approve, request revisions, or redirect entirely. No design work begins until you approve.

## Output

All outputs are saved to `campaigns/{{slug}}/creative/design/`:

```
visual-direction-system.md     ← the complete visual direction
briefs/
  ├── graphic-design-brief.md
  ├── ux-brief.md
  ├── print-brief.md
  └── [others as needed]
outputs/                       ← collected specialist outputs
design-package.md              ← assembled deliverables summary
```

The `design-system/` folder (at project root) is also updated with new standards and campaign history.
