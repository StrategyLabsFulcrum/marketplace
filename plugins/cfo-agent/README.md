# CFO Agent

Fractional CFO agent for three active brand engagements. Loads brand-specific financial context and operates as a trusted financial partner — not a reporter, not a consultant. Thinks like an owner, advocates with data, and communicates like a peer.

---

## Activation

```
/cfo-agent pnw
/cfo-agent uno-mas
/cfo-agent strategy-labs
```

Or just start a financial conversation mentioning the brand name and the agent will detect context and load automatically.

---

## What It Does

| Capability | Description |
|---|---|
| P&L Analysis | Period-over-period review, EBITDA calculation, normalization |
| Financial Modeling | Scenario models, break-even, operating leverage, run rate |
| Deal Structuring | SBA underwriting, equity deals, investor return models, valuation defense |
| KPI Dashboards | Monthly CFO dashboard, flag-based reporting |
| Reporting | Internal analysis, banker packages, investor memos |
| Strategic Advisory | Deal sequencing, risk flagging, proactive anomaly identification |

---

## Architecture

```
cfo-agent/
├── SKILL.md                    # Full agent instructions + universal philosophy
├── README.md                   # This file
├── .claude-plugin/
│   └── plugin.json             # Plugin metadata
└── brands/
    ├── pnw.md                  # PNW session primer
    ├── uno-mas.md              # Uno Mas session primer
    └── strategy-labs.md        # Strategy Labs session primer

cfo-knowledge/                  # Brand knowledge base (outside plugin)
├── pnw/
│   ├── cfo-onboarding.md
│   ├── models-and-frameworks.md
│   └── relationship-and-working-context.md
├── uno-mas/
│   ├── cfo-onboarding.md
│   ├── models-and-frameworks.md
│   └── relationship-and-working-context.md
└── strategy-labs/
    ├── cfo-onboarding.md
    ├── models-and-frameworks.md
    └── relationship-and-working-context.md
```

---

## Brand Engagements

### The Great PNW
DTC outdoor apparel. Performance is driven by MER (Media Efficiency Ratio) and contribution margin. The core job is restoring the 2021 margin profile (15.2% net) through media discipline, not revenue growth.

**Key metric:** MER ≥ 3.0× → CM% ≈ 15%
**Critical rule:** Cash-to-accrual COGS correction required on every P&L

### Uno Mas
Mexican restaurant, Monroe WA. Three equal owners. SBA consolidation loan is the primary near-term initiative. The chronic problem is Wednesday labor at 45%+ — it has its own standing agenda item.

**Key metric:** Prime Cost ≤ 55% (currently 55.3%, no margin for error)
**Critical rule:** Never use single-source COGS; always net sales denominator; Mondays excluded

### Strategy Labs
Digital agency, 26 employees, 95% recurring revenue. In a deal-closing moment: 3 VP equity deals + Bryan Howell $2.5M investment. Valuation is being challenged against a low-ball appraisal ($4.197M Griffiths vs. $8M–$12.5M transaction prices).

**Key metric:** EBITDA target $1.2M (2026) — everything is priced off this
**Critical rule:** Lead with 95% recurring revenue in every external conversation; QB revenue ≠ actual revenue

---

## Universal Principles

1. **Accuracy over optics** — never massage numbers to look better
2. **Lead with what matters** — direct attention to the right metric, not just what was asked
3. **Real recommendations, not options menus** — commit to positions
4. **Version and source everything** — no number without provenance
5. **Flag once, address it, move on** — risk gets one sentence, not three paragraphs

---

## Adding a New Brand

1. Run the 3-step knowledge extraction in the brand's Claude web project
2. Save outputs to `/Users/ramseypruchnic/dev/cfo-knowledge/[brand-slug]/`
3. Create a session primer at `/Users/ramseypruchnic/dev/plugins/cfo-agent/brands/[brand-slug].md`
4. Add the brand slug to `plugin.json` brands array

---

*v1.0 — March 2026*
