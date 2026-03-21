# /test-design

Design a specific A/B or multivariate test — hypothesis, variant specification, sample size requirements, statistical parameters, and implementation brief.

## How to Invoke

**Test a specific element:**
```
/test-design headline on spring launch landing page
/test-design CTA button copy and placement on product page
/test-design checkout form — reduce fields
```

**From a hypothesis:**
```
/test-design hypothesis: adding testimonials near CTA will increase CVR
```

**Multi-variant test:**
```
/test-design 3-way test: short form vs long form vs video landing page
```

## What You Get

- Full hypothesis statement (structured format)
- Control vs. variant specification (exact copy, layout, or element changes)
- Sample size requirement calculation
- Estimated test duration based on traffic
- Traffic split recommendation
- Implementation brief for development/design team
- Success criteria and stop-test conditions
- Analysis plan

## Output Location

`campaigns/[slug]/cro/test-designs/test-[slug].md`
