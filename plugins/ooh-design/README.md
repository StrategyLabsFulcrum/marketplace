# OOH Design Agent

Designs out-of-home advertising — billboards, transit ads, bus shelters, bus wraps, and street-level media. Enforces strict copy constraints and viewing-distance legibility standards. Specialist agent — directed by the Art Director.

## What It Does

1. Loads brand visual standards
2. Applies OOH copy rules before writing a single word (7 words max for highway; scaled by format)
3. Produces 2–3 copy options within the word limit for each format
4. Produces complete design specifications with typography at scale
5. Specifies legibility requirements (minimum type size at viewing distance)
6. Handles digital OOH (DOOH) specifications separately from print vinyl

## Formats Covered

| Format | Max Copy | Viewing Context |
|--------|---------|----------------|
| Highway bulletin (14×48) | 5–7 words | 65mph, 500–1,500 ft |
| Urban poster (10.5×36) | 7–10 words | 35mph, 100–300 ft |
| Bus shelter | 15–20 words | Pedestrian, 5–15 ft |
| Subway / transit station | 25–40 words | Captive, 3–10 ft |
| Bus wrap / king | 5–10 words | Moving + stopped |
| Retail POS | Up to 50 words | Pedestrian, 1–5 ft |
| Digital OOH (DOOH) | Same as format type | sRGB, animation rules |

## Output

`campaigns/{{slug}}/creative/design/outputs/ooh-design.md`

Copy options, complete design specifications, typography at scale, CMYK/sRGB specs, and vendor coordination notes.

## Dependencies

- **brand-intelligence-center** (required) — brand identity, colors
- **art-director** (directs this agent) — visual direction system, OOH brief
