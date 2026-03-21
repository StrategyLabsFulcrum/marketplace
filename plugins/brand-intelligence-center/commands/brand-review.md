# /brand-review

Generate a clean, human-readable brand review document for your team. Formats all 8 areas of brand intelligence into a single shareable document — no markdown noise, no technical fields. Team members can read, annotate, and send back feedback.

Optionally uploads to Fast.io as a shared document your whole team can access.

## What This Does

1. Reads all brand-intelligence-center files for the active brand
2. Formats them into a clean, team-friendly review packet
3. Saves to `brand-intelligence-center/review/brand-review-{{date}}.md`
4. Optionally creates a Fast.io share link the team can access and annotate

## When to Use

- Onboarding a new team member to the brand
- Quarterly brand check-in — is everything still accurate?
- Before a major campaign — confirm positioning and messaging are still right
- After a significant business change — rebrand, new product, new market
- Sharing brand guidelines with an agency, contractor, or freelancer

## How to Invoke

```
/brand-review
```

**With Fast.io sharing:**
```
/brand-review share
```

## Output

A `brand-review-{{date}}.md` file in `brand-intelligence-center/review/` with:

- **Review Instructions** — how team members should provide feedback
- All 8 brand areas in plain, readable language
- **Team Notes** section at the bottom for collecting feedback
- **What's Changed** section showing updates since the last review

If `share` is passed: generates a Fast.io share link the team can open in any browser to read and add comments.

## After Sharing

Team members review the document and send back notes. Collect their feedback and run `/brand-revise` to apply changes with confirmation before they take effect.
