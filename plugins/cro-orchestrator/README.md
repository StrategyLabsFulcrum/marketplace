# CRO Orchestrator

Identifies, prioritizes, and tests changes that increase conversion rates across the entire marketing funnel — landing pages, product pages, checkout flows, email sequences, and ad-to-page experiences.

CRO is the highest-leverage growth lever available: the same traffic produces more revenue without increasing ad spend. A 20% improvement in landing page CVR has the same revenue impact as a 20% increase in ad budget — but it compounds across all channels.

---

## What This Agent Does

| Mode | Use Case |
|------|----------|
| `audit` | Full funnel CRO audit — friction mapping, drop-off analysis, hypothesis backlog |
| `hypothesis` | Generate prioritized test hypotheses for a specific page or flow |
| `test-design` | Design a specific A/B or multivariate test with statistical specs |
| `analysis` | Analyze test results and determine winner |
| `post-click` | Optimize the ad → landing page experience (message match) |
| `checkout` | Audit and optimize checkout specifically |

---

## Slash Commands

| Command | Use |
|---------|-----|
| `/cro-audit` | Full funnel audit with ICE-scored hypothesis backlog |
| `/test-design` | Complete A/B test specification with sample size math |
| `/checkout-audit` | Checkout-specific friction audit and optimization plan |

---

## The CRO Hypothesis Framework

Every test is built on a structured hypothesis:

> *"We believe that [specific change] will [increase/decrease] [specific metric] because [evidence/reasoning], measured by [how to measure success]."*

Hypotheses are prioritized using ICE scoring:
- **Impact** — How much could this move the needle?
- **Confidence** — How strong is the evidence?
- **Ease** — How easy is it to implement?

---

## Integration with the Campaign System

```
Campaign Strategist → Campaign Brief
        ↓
Performance Marketing → Drives traffic to landing pages
        ↓
CRO Orchestrator ← Marketing Analytics (provides conversion data)
        ↓
UX Website Designer → Implements winning variants + new wireframes
Direct Response Copy → Rewrites page copy based on CRO findings
Graphic Design Agent → Visual updates for test variants
        ↓
Marketing Analytics → Tracks test results and statistical significance
        ↓
Performance Marketing → Benefits from higher CVR (lower CPA, higher ROAS)
```

---

## Output Structure

```
campaigns/[slug]/cro/
├── funnel-audit.md              ← full funnel analysis and friction inventory
├── hypothesis-backlog.md        ← ICE-scored hypotheses, prioritized
├── test-designs/
│   └── test-[slug].md           ← one design spec per test
├── results/
│   └── test-[slug]-results.md   ← post-test analysis
└── optimization-log.md          ← running log of all tests and outcomes

brand-assets/cro/
└── checkout-audit.md            ← site-wide checkout findings
```

---

## Statistical Standards

All tests run to:
- **95% confidence** (p < 0.05) before declaring a winner
- **Minimum 14-day duration** regardless of sample size achieved
- **Minimum 100 conversions per variant** before reading results
- **Segment analysis** by device and traffic source before finalizing

The optimization log records every test — wins and losses. Losing tests that reveal why users behave a certain way are as valuable as winning tests.
