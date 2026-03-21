# Direct Response Copywriter

Writes landing pages, sales pages, and VSL scripts — the copy that converts traffic into customers. Specialist agent — receives briefs from the Creative Director and produces full-page copy structured around persuasion architecture, awareness-level matching, and risk reversal.

## What It Does

1. Loads brand voice and available proof points from brand-intelligence-center
2. Reads the Direct Response brief from the Creative Director
3. Diagnoses audience awareness level and traffic source
4. Builds page architecture (outline) before writing
5. Writes every section with its specific conversion job in mind
6. Includes objection handling, guarantee language, and CTA architecture
7. Delivers annotated copy with designer notes per section

## Content Types

| Type | Output |
|------|--------|
| Click-through landing page | Full page copy — headline through CTA |
| Lead gen landing page | Shorter; form-focused; low friction |
| Sales page | Long-form; full persuasion arc |
| VSL script | Spoken copy with visual direction notes |
| Webinar registration page | Event-specific landing page |
| Quiz funnel copy | Question text, transitions, results page |

## Output

`campaigns/{{slug}}/creative/copy/landing-page-copy.md` or `sales-page-copy.md` or `vsl-script.md`

Each section annotated with its purpose and designer notes. Includes A/B test recommendations for headline, CTA, and guarantee.

## Dependencies

- **brand-intelligence-center** (required) — brand voice, proof points, NEVER rules
- **creative-director** (spawns this agent) — page brief with traffic source, offer, structure, constraints
