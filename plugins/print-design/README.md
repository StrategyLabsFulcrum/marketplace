# Print Design Agent

Produces print design specifications — magazine ads, direct mail, brochures, and printed collateral. Complete CMYK color specs, typography, image requirements, and production-ready documentation. Specialist agent — directed by the Art Director.

## What It Does

1. Loads brand visual standards (with priority on CMYK/Pantone values for print)
2. Reads the print design brief from the Art Director
3. Produces complete layout specifications for every print format
4. Specifies CMYK values for all colors, Pantone equivalents where defined
5. Provides image requirements (resolution, mode, file format)
6. Produces pre-production checklist and proofing requirements

## Formats Covered

| Format | Typical Sizes |
|--------|-------------|
| Magazine ads | Full page, half page, quarter page, DPS |
| Newspaper ads | Full page, half page, quarter page |
| Direct mail postcard | 4×6, 5×7, 6×9, 6×11 |
| Self-mailer | Tri-fold 8.5×11, other fold configurations |
| Brochure | Tri-fold, bi-fold, Z-fold |
| Flyer / sheet | 8.5×11, 5.5×8.5 |

## Output

`campaigns/{{slug}}/creative/design/outputs/print-design.md`

Complete layout specification with CMYK colors, typography specs, image requirements, production notes, and pre-production checklist.

## Dependencies

- **brand-intelligence-center** (required) — brand identity, CMYK/Pantone values
- **art-director** (directs this agent) — visual direction system, print brief
