# Graphic Design Agent

Produces digital design assets for paid and organic channels. Outputs Canva direction, AI image generation prompts, and complete asset specifications. Specialist agent — directed by the Art Director.

## What It Does

1. Loads brand visual standards and campaign visual direction system
2. Reads the design brief from the Art Director
3. Produces complete design direction for every asset format in scope
4. Three execution paths: Canva direction / AI image prompts / spec for human designer
5. Self-reviews against visual direction system and brand NEVER rules
6. Delivers organized by platform and format with export specifications

## Formats Covered

| Platform | Formats |
|---------|---------|
| Meta | Feed (1:1, 4:5), Stories (9:16), Carousel cards |
| Google Display | Standard banner sizes (300×250, 728×90, 160×600, 300×600, etc.) |
| TikTok | In-Feed (9:16), TopView |
| LinkedIn | Single image, Carousel |
| Email | Header/hero image, inline graphics |
| Organic social | Any format per platform |

## Output

`campaigns/{{slug}}/creative/design/outputs/digital-assets.md`

Complete Canva direction or AI prompts for every asset, with file naming and export specifications.

## Dependencies

- **brand-intelligence-center** (required) — brand colors, fonts, logo rules
- **art-director** (directs this agent) — visual direction system, design brief
