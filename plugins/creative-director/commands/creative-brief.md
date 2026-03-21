# /creative-brief

Start a creative project. The Creative Director loads your brand context, collects what you need (or reads an existing campaign brief), develops the creative concept for your approval, then briefs and spawns all specialist agents in parallel.

## What This Does

1. Loads brand intelligence — voice, customer, differentiation, proof points
2. Reads your campaign brief (if one exists) or collects context from you directly
3. Develops the creative concept — the unifying idea behind all executions
4. Gets your approval on the concept before briefing anyone
5. Determines which specialists are needed (copywriters, designers)
6. Issues tailored briefs and spawns all specialists in parallel
7. Reviews every output against the brand rubric
8. Routes all copy through the Copy Editor
9. Assembles and delivers the complete creative package

## When to Use

- After Campaign Strategist has produced a campaign brief — run this to execute the creative
- Starting a creative project outside of a full campaign (standalone mode)
- Need to produce a specific set of assets without full campaign infrastructure

## How to Invoke

**Campaign mode** (recommended — reads existing campaign brief):
```
/creative-brief
```
The Creative Director will detect your active campaign and read its brief.

**Standalone mode** (no campaign folder needed):
```
/creative-brief standalone
```
Collects context from you directly and builds a mini creative brief before proceeding.

## Output

All creative saved to `campaigns/{{slug}}/creative/` (or `creative/{{project-slug}}/` in standalone mode):

- `creative-concept.md` — the approved unifying concept
- `briefs/` — specialist briefs issued to each agent
- `copy/` — all copy outputs, Copy Editor reviewed
- `design/` — graphic design brief and UX brief
- `review/` — rubric review notes for each output
- `creative-package.md` — assembled summary of all deliverables

## Tips

- The creative concept approval step is not optional — it's what makes the entire package coherent
- The more complete your brand-intelligence-center is, the sharper the concept will be
- Competitive landscape data makes the concept more differentiated — run `/competitive-landscape` first if you haven't
- Standalone mode is great for one-off creative projects (a single email, a social series, a landing page)
