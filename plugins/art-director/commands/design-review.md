# /design-review

Review design outputs against the visual direction system and brand standards. Returns a clear pass / pass-with-notes / revise verdict for each piece, with specific, actionable feedback on any failures.

## What This Does

1. Loads the approved visual direction system for the campaign
2. Loads brand visual standards from brand-intelligence-center and design-system/
3. Reviews each design output against the full 8-criteria rubric
4. Returns pass / pass-with-notes / revise / escalate for each piece
5. Provides specific feedback on any failures — what's wrong, why, and what to do
6. Summarizes patterns across all reviewed work
7. Routes Escalate verdicts to brand-intelligence-center for brand-level updates

## When to Use

- Reviewing design outputs submitted by a specialist or external agency
- Reviewing creative before client approval
- Checking that existing assets are still on-brand after a brand update
- Running a mid-campaign visual audit on underperforming ads

## How to Invoke

**Review all design outputs in a campaign:**
```
/design-review
```

**Review a specific file:**
```
/design-review campaigns/2026-03-spring/creative/design/outputs/meta-feed-v1.md
```

**Review submitted design brief or image description (paste it in):**
```
/design-review submit
```
The Art Director will ask for the design description and what it's for, then run the rubric.

**Review against a specific set of criteria only:**
```
/design-review typography
/design-review brand-rules
/design-review production-specs
```

## The Review Rubric

Each output is evaluated against 8 visual criteria:

1. **Brand visual NEVER rules** — hard pass/fail; any violation is an automatic Revise
2. **Visual direction alignment** — does it match the approved visual direction system?
3. **Campaign motif application** — is the motif present and applied correctly?
4. **Typography compliance** — font, weight, hierarchy, tracking, case — all correct?
5. **Color system compliance** — correct palette, ratios, and background approach?
6. **Production spec compliance** — correct dimensions, resolution, file format, safe zones?
7. **Channel-specific adaptation** — does it correctly adapt the system for this channel?
8. **Cross-channel coherence** — does it feel like it belongs in the same campaign as other outputs?

### Verdicts

| Verdict | Meaning |
|---------|---------|
| **Pass** | Fully compliant. Ready for production. |
| **Pass with notes** | Minor issues that don't require revision before use, but should be addressed in future iterations. |
| **Revise** | Specific failures that must be corrected before the output can be used. Feedback provided. |
| **Escalate** | A brand-level issue that goes beyond this campaign — the brand standards themselves may need updating. Routed to brand-intelligence-center. |

## Output

A review document saved to `campaigns/{{slug}}/creative/design/review/design-review-{{date}}.md` with:
- Rubric results per piece
- Specific revision feedback for any Revise verdicts
- Summary of patterns across all reviewed pieces
- Recommended next steps
