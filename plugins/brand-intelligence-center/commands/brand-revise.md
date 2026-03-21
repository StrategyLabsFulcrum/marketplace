# /brand-revise

Apply team feedback and revisions to your brand intelligence files. Shows exactly what will change — as a before/after for each field — and requires confirmation before writing anything. Every revision is logged to the brand changelog.

## What This Does

1. Accepts revision notes (pasted in, or pulled from Fast.io comments)
2. Identifies which brand areas and fields are affected
3. Proposes specific before → after changes for each item
4. Requires your confirmation on each change (or all at once)
5. Applies confirmed changes to the relevant area files
6. Rebuilds `system-prompt.md` from the updated files
7. Logs every change to `brand-intelligence-center/changelog.md`
8. If sync is configured, pushes the updated files to Fast.io

## When to Use

- After collecting feedback from a brand review
- Updating specific brand fields after a business change
- Applying input from a strategy session or brand workshop
- Correcting outdated information found by a team member

## How to Invoke

```
/brand-revise
```

The agent will ask for your revision notes. You can:
- **Paste notes directly** — copy feedback from email, Slack, a doc, or a brand review
- **Reference Fast.io** — if sync is configured, pull comments from the shared review document
- **Describe changes conversationally** — "update our tagline to X" or "add two new competitors"

## Confirmation Flow

For each proposed change, you'll see:

```
Area: Brand Voice & Identity
Field: Tagline

CURRENT: "Built for the road ahead"
PROPOSED: "No road. No rules."

Confirm? [Y / Skip / Edit]
```

You can confirm individually or say "approve all" to accept every proposed change at once.

## What Gets Updated

After confirmed changes are applied:
- The relevant area file(s) are updated
- `system-prompt.md` is automatically rebuilt from all area files
- `changelog.md` records what changed, when, and what the previous value was
- If sync is configured: files are pushed to Fast.io automatically

## Tips

- You don't need to run `/brand-review` first — revisions can come from anywhere
- You can revise one field ("update our primary CTA") or a whole area at once
- Use `/brand-review` afterward to generate a fresh copy for team distribution
