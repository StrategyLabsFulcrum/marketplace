# /checkout-audit

Audit the checkout and purchase flow specifically — identify friction causing cart abandonment and produce a prioritized optimization plan.

## How to Invoke

**Standard checkout audit:**
```
/checkout-audit
```

**With analytics data:**
```
/checkout-audit [paste checkout funnel data from GA4 / Shopify analytics]
```

**Specific platform:**
```
/checkout-audit Shopify checkout
/checkout-audit WooCommerce
/checkout-audit custom checkout
```

## What You Get

- Checkout friction map against the 9 top abandonment causes
- Checklist audit: 12-point checkout optimization checklist with current status
- Prioritized fix list (quick wins first, then test-required changes)
- Cart abandonment email sequence recommendation
- Trust signal audit
- Mobile checkout review
- Payment method gap analysis

## Common Quick Wins

Most checkout audits find at least one of these immediately actionable issues:
- Guest checkout not available or not prominent
- Shipping cost revealed too late (at payment step, not before)
- Too many form fields (especially unnecessary fields like phone number)
- No Apple Pay / Google Pay option
- Security badge not visible at payment step

## Output Location

`campaigns/[slug]/cro/checkout-audit.md` or `brand-assets/cro/checkout-audit.md`
