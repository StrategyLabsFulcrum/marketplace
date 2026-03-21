# Email Copywriter

Writes email marketing copy for the full range of sequence types. Specialist agent — receives briefs from the Creative Director and produces complete email sequences with subject lines, preview text, body copy, and CTAs.

## What It Does

1. Loads brand voice from brand-intelligence-center
2. Reads the Email Copywriter brief from the Creative Director
3. Maps the sequence arc before writing a single email
4. Writes each email in full — 3+ subject line options, preview text, body, CTA, PS
5. Checks compliance (CAN-SPAM, GDPR basics) before delivering
6. Delivers fully formatted sequence with A/B test recommendations

## Sequence Types

| Type | Typical Length |
|------|--------------|
| Welcome series | 5–7 emails |
| Promotional campaign | 3–5 emails |
| Abandoned cart | 3 emails |
| Nurture / lead sequence | 5–8 emails |
| Re-engagement | 3–4 emails |
| Cold outreach | 3 emails (max) |
| Newsletter | 1 issue |
| Lifecycle / trigger | Single email per trigger |

## Output

`campaigns/{{slug}}/creative/copy/email-copy.md`

Each email fully written with multiple subject line options, recommended A/B tests, sequence flow logic, and compliance notes.

## Dependencies

- **brand-intelligence-center** (required) — brand voice, NEVER rules
- **creative-director** (spawns this agent) — sequence brief with arc, per-email assignments, audience
