# /creative-review

Review creative outputs that have been submitted or already exist in a campaign's creative folder. Runs the brand voice rubric, checks strategic alignment against the creative concept, and returns a clear pass/revise verdict with specific feedback for each piece.

## What This Does

1. Reads the approved creative concept for the campaign
2. Loads brand voice rules from brand-intelligence-center
3. Reviews each copy or design output against the full rubric
4. Returns pass / pass-with-notes / revise for each piece
5. Provides specific, actionable feedback on any failures
6. Optionally routes passing copy through the Copy Editor

## When to Use

- Reviewing copy submitted by an external writer or agency
- Reviewing creative before it goes to a client for approval
- Checking that existing assets are still on-brand after a brand update
- Running a mid-campaign creative audit on underperforming ads

## How to Invoke

**Review all creative in a campaign:**
```
/creative-review
```

**Review a specific file:**
```
/creative-review campaigns/2026-03-spring/creative/copy/ad-copy.md
```

**Review submitted copy (paste it in):**
```
/creative-review submit
```
The Creative Director will ask for the copy and what it's for, then run the rubric.

## Output

A review document saved to `campaigns/{{slug}}/creative/review/creative-review-{{date}}.md` with:
- Rubric results per piece (pass / pass with notes / revise)
- Specific edits or feedback for each failure
- Summary of patterns across all reviewed pieces
- Recommended next steps
