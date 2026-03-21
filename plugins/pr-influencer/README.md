# PR & Influencer Agent

Plans and executes earned media campaigns — press coverage, influencer partnerships, creator collaborations, brand ambassador programs, and UGC strategies. Bridges the gap between brand-paid media and brand-earned media.

Earned media converts at higher rates because it carries independent trust. Third-party voices — journalists, creators, community members — can say things about the brand that the brand cannot say about itself.

---

## What This Agent Does

| Mode | Use Case |
|------|----------|
| Influencer campaign | Brief and structure a creator partnership campaign |
| PR outreach | Press releases, media pitches, journalist outreach |
| Ambassador program | Long-term creator relationship infrastructure |
| UGC strategy | Systems to generate and amplify user content |
| Creator vetting | Evaluate specific creators against brand criteria |
| Media kit | Brand media kit for press and influencer inquiries |

---

## Slash Commands

| Command | Use |
|---------|-----|
| `/influencer-brief` | Campaign strategy, creator roster, per-creator briefs, tracking setup |
| `/pr-pitch` | Press release, journalist pitch, target publication list |

---

## Creator Tier Framework

| Tier | Followers | Strength |
|------|-----------|----------|
| Nano | 1K–10K | Hyper-local trust, highest engagement |
| Micro | 10K–100K | Category authority, community credibility |
| Mid-tier | 100K–500K | Scale with maintained credibility |
| Macro | 500K–1M | Broad awareness |
| Mega | 1M+ | Maximum awareness; lowest direct conversion |

Most DTC brands see the best ROI from micro and mid-tier creators — the trust is higher and the cost-per-engaged-follower is significantly lower.

---

## Integration with the Campaign System

```
Campaign Strategist → Campaign Brief
        ↓
PR & Influencer Agent ←→ Creative Director (visual direction for creator briefs)
        ↓
Creator briefs → External creators produce content
        ↓
Performance Marketing Agent — Whitelist/amplify top-performing creator content
        ↓
Marketing Analytics — Track promo codes, UTM attribution, creator ROI
        ↓
Content Library — Store top-performing UGC and earned media mentions
```

---

## Output Structure

All PR & Influencer outputs live in the campaign folder:

```
campaigns/[slug]/pr-influencer/
├── strategy-overview.md         ← campaign structure and budget allocation
├── creator-roster.md            ← vetted creators with rationale and proposed terms
├── creator-brief-[handle].md    ← one brief per creator
├── press-release.md             ← AP-style press release
├── media-pitch-template.md      ← journalist outreach email template
├── media-target-list.md         ← prioritized outlets and contacts
├── ugc-brief.md                 ← UGC campaign structure
├── ambassador-program.md        ← long-term program architecture
└── tracking-setup.md            ← UTM codes and promo codes per creator
```

---

## FTC Compliance

All influencer campaigns must meet FTC disclosure requirements:
- Paid partnerships: platform native disclosure label + verbal disclosure in video
- Gifted product: disclosure required even without payment if posting is expected
- Affiliate links: explicit affiliate relationship disclosure

The agent includes a compliance checklist in every creator brief and flags any arrangement that requires disclosure.
