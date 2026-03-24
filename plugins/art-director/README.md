# Art Director

Owns the visual execution of every campaign across all channels — digital and non-digital. The Art Director develops the visual direction system, maintains brand design standards, and directs all design specialists: graphic design, print, OOH, packaging, UX/web, and motion.

**The Art Director does not produce design files.** It directs, briefs, reviews, and assembles.

## What It Does

1. Loads brand intelligence — voice-identity.md is the foundation; design-system/ is the living visual record
2. Reads the creative concept from the Creative Director (or collects context in standalone mode)
3. Develops the visual direction system — the complete visual translation of the creative concept
4. Gets visual direction approved before briefing anyone
5. Issues tailored, self-contained briefs to each needed design specialist
6. Spawns all specialists in parallel
7. Reviews every output against the visual direction system and brand standards
8. Updates the persistent design-system/ folder with new standards and history
9. Assembles and delivers the complete design package

## Commands

| Command | What It Does |
|---------|-------------|
| `/visual-direction` | Develop the visual direction system for a campaign — concept → briefs → parallel execution → design package |
| `/design-review` | Review existing design outputs against the visual direction system |

## How It Fits

The Art Director works in parallel with the Creative Director, both reporting to the Campaign Strategist brief:

```
Campaign Strategist
  → campaign-brief.md
      ↓                    ↓
Creative Director      Art Director
  → creative concept     → visual direction system
  → copy briefs          → design briefs
      ↓ [parallel]           ↓ [parallel]
  Copy specialists      ├── Graphic Design Agent (digital)
  Copy Editor           ├── UX/Website Designer
                        ├── Print Design Agent
                        ├── OOH Design Agent
                        ├── Packaging/Brand Design Agent
                        └── Motion Design Agent
                            ↓
                        Design Package → Creative Director (final assembly)
```

The Creative Director produces a creative concept including 3–5 visual direction words. The Art Director reads those words and expands them into the full visual direction system that every design specialist executes against.

## Specialists Directed

| Specialist | When Used |
|-----------|----------|
| Graphic Design Agent | Digital ads (Meta, Google Display), email graphics, organic social, digital banners |
| UX/Website Designer | Landing pages, microsites, web components, user flows |
| Print Design Agent | Magazine ads, direct mail, brochures, collateral |
| OOH Design Agent | Billboards, transit, bus shelters, bus wraps, retail POS |
| Packaging/Brand Design Agent | Product packaging, labels, trade show displays, corporate identity |
| Motion Design Agent | Video ads, animated social, GIFs, branded motion assets |

## Output Structure

```
campaigns/{{slug}}/creative/design/
├── visual-direction-system.md     ← the visual direction for this campaign
├── briefs/                        ← specialist briefs issued
│   ├── graphic-design-brief.md
│   ├── ux-brief.md
│   ├── print-brief.md
│   ├── ooh-brief.md
│   └── [others]
├── outputs/                       ← design outputs collected from specialists
└── design-package.md              ← assembled summary of all design deliverables

design-system/                     ← persistent, cross-campaign visual record
├── brand-standards.md             ← accumulated brand visual standards
├── campaign-history.md            ← visual history across all campaigns
└── component-library/             ← reusable visual components, patterns, approved motifs
```

The `design-system/` folder lives outside any specific campaign and grows over time. It is the Art Director's institutional memory — every new campaign reads it before starting, and every completed campaign adds to it.

## The Visual Direction System

The Art Director's primary output. Developed before any specialist is briefed. Consists of:

- **Color treatment** — primary hierarchy, ratios, background approach, CMYK/Pantone values
- **Typography direction** — font stack, hierarchy, tracking, line height, typographic treatments
- **Photography / illustration style** — type, subject, lighting, composition, grading, production level
- **Layout principles** — grid, white space, visual hierarchy, composition approach, CTA treatment
- **Campaign visual motif** — the ownable visual element that unifies all executions
- **Motion direction** — pacing, transitions, text animation, music, voiceover (when in scope)
- **Channel adaptation rules** — how the system flexes across 12+ media types without losing coherence

The visual direction system is the thread connecting every ad, email, billboard, packaging, and print piece. Without it, individual outputs may be strong in isolation but feel disconnected as a campaign.

## Design Review

The Art Director reviews every design output against 8 visual criteria:
1. Brand visual NEVER rules compliance
2. Visual direction alignment
3. Campaign motif application
4. Typography compliance
5. Color system compliance
6. Production spec compliance
7. Channel-specific adaptation
8. Cross-channel coherence

Verdicts: **Pass** / **Pass with notes** / **Revise** / **Escalate** (brand-level concern requiring brand-intelligence-center update)

## Plugin Dependencies

- **brand-intelligence-center** (required) — voice-identity.md anchors the Art Director's brand visual standards
- **creative-director** (required in campaign mode) — provides the creative concept and visual direction words the Art Director expands
- **campaign-strategist** (recommended) — provides campaign brief with channel list, audience, and strategic context
- **competitive-landscape** (recommended) — competitive visual analysis informs visual differentiation strategy
- **gemini-creative** (optional) — when connected, the Art Director offers model selection before spawning specialists. Users choose which AI models generate assets (Gemini Imagen 3, Veo 2, DALL-E, Midjourney, or multi-model comparison). The selection is passed to every specialist brief for consistent model usage across the campaign.
