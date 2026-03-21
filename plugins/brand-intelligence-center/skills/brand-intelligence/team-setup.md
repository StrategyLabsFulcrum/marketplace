---
name: team-setup
description: >
  Activate when a brand needs to determine which marketing agents to install or when asked "what agents do I need", "which plugins should I use", "build my team", "team setup", "what do I need". Interviews the brand across 6 areas and produces a customized agent team recommendation.
version: 1.0.0
allowed-tools: Read, Write
---

# Team Setup Wizard

You are configuring a brand's AI marketing team. Your job is to ask the right questions, then recommend exactly the agents this brand needs — no more, no fewer. An overloaded team is as useless as an underequipped one.

Read `brand-intelligence-center/system-prompt.md` first. Use what you already know about the brand to pre-fill answers where possible, and only ask for what you don't yet know.

---

## The Interview

Work through 6 areas. Ask each area as a conversational block — not one question at a time. Present the questions for each area together, let them answer, then move to the next.

---

### Area 1: Business Model & Stage

```
1. What type of business is this?
   a) eCommerce / DTC (physical products sold online)
   b) SaaS / digital product / subscription
   c) Service business (agency, consulting, professional services)
   d) Local / brick-and-mortar
   e) B2B / enterprise sales
   f) Marketplace or platform
   g) Other: ___

2. What stage is the brand at?
   a) Pre-launch / just getting started
   b) Early stage (under $1M revenue / under 1 year)
   c) Growth stage ($1M–$10M or scaling actively)
   d) Established ($10M+ or mature marketing operation)

3. Do you sell physical products?
   Yes / No

4. If yes — do you sell branded merchandise (apparel, accessories, lifestyle products)
   separate from your core product?
   Yes / No / Not yet but interested
```

---

### Area 2: Paid Media

```
5. Do you currently run or plan to run paid advertising?
   Yes — currently running / Yes — planning to start / No

6. Which paid channels are you on or planning? (select all that apply)
   [ ] Meta (Facebook/Instagram)
   [ ] Google Search
   [ ] Google Performance Max / Shopping
   [ ] TikTok
   [ ] LinkedIn
   [ ] Pinterest
   [ ] YouTube ads
   [ ] Connected TV / streaming ads
   [ ] None

7. What is your approximate monthly paid media budget?
   a) Under $3,000/month
   b) $3,000–$15,000/month
   c) $15,000–$50,000/month
   d) $50,000+/month
   e) Not running paid yet
```

---

### Area 3: Content & Organic

```
8. Do you do email marketing?
   Yes — actively / Planning to / No

9. Do you create content for SEO (blog posts, guides, landing pages)?
   Yes — actively / Planning to / No

10. Do you create video content?
    Yes — YouTube / Yes — TikTok / Yes — Instagram Reels / Multiple / No / Planning to

11. Do you do social media content (organic posts, captions)?
    Yes — in-house / Yes — outsourced / Occasionally / No
```

---

### Area 4: Brand & Creative

```
12. Where does your copy and creative currently come from?
    a) I write it myself
    b) In-house team
    c) Freelancers / agency
    d) Mix of the above
    e) Mostly AI tools already

13. Do you have brand guidelines (voice, visual identity, tone rules)?
    Yes — documented / Informal / No — need to build them

14. Do you produce any physical marketing materials?
    [ ] Print ads (magazines, newspapers)
    [ ] Direct mail / brochures / flyers
    [ ] Out-of-home / billboards / transit
    [ ] Product packaging
    [ ] Trade show / event materials
    [ ] Business cards / corporate identity
    [ ] None of the above

15. Do you have a website that needs conversion optimization?
    Yes — eCommerce store / Yes — lead gen site / Yes — SaaS product / No
```

---

### Area 5: Earned Media & Partnerships

```
16. Do you do or plan to do influencer marketing or creator partnerships?
    Yes — actively / Planning to / No

17. Do you do or plan to do PR (press coverage, media outreach)?
    Yes — actively / Planning to / No

18. Do you have a brand ambassador or affiliate program?
    Yes / Planning to build one / No
```

---

### Area 6: Data & Analytics

```
19. Which data sources do you have connected or want to connect? (select all that apply)
    [ ] Meta Ads Manager
    [ ] Google Ads
    [ ] Google Analytics 4 (GA4)
    [ ] Klaviyo
    [ ] Mailchimp or other ESP
    [ ] Shopify
    [ ] WooCommerce
    [ ] Stripe / payment processor
    [ ] CRM (HubSpot, Salesforce, etc.)
    [ ] TikTok Ads
    [ ] LinkedIn Ads
    [ ] None yet

20. Do you currently review marketing performance data regularly?
    Yes — weekly / Yes — monthly / Occasionally / No — need to start

21. Do you have established benchmarks for your key metrics (CVR, CAC, ROAS, open rates)?
    Yes / Rough estimates / No
```

---

## Team Recommendation Engine

Based on the answers, apply this decision framework:

### Always Recommended (every brand)
| Agent | Why |
|-------|-----|
| `brand-intelligence-center` | Foundation — already installed |
| `campaign-strategist` | Every marketing initiative needs a brief and plan |
| `creative-director` | Coordinates all copy; quality gate for everything written |
| `content-library` | Prevents duplication; compounds value of every approved piece |

### Recommended Based on Answers

**`performance-marketing`**
→ Recommend if: paid media budget > $0 (Q5 = Yes) AND any paid channel selected (Q6)
→ Skip if: no paid media planned

**`marketing-analytics`**
→ Recommend if: any data sources connected (Q19) OR paid media running
→ Essential if: $3K+/month paid media (Q7b or higher)
→ Note if early stage: "Install now, use when you have 60+ days of data"

**`ad-copy`**
→ Recommend if: any paid social or search channels selected (Q6)
→ Skip if: no paid advertising

**`email-copy`**
→ Recommend if: email marketing active or planned (Q8)
→ Skip if: Q8 = No

**`direct-response-copy`**
→ Recommend if: has website needing conversion optimization (Q15) OR paid media driving to landing pages
→ Skip if: no website / pure awareness play only

**`brand-storytelling-copy`**
→ Recommend if: no documented brand guidelines (Q13 = No) OR early stage brand building
→ Also recommend if: content marketing / thought leadership planned
→ Skip if: fully established brand with complete voice documentation

**`seo-copy`**
→ Recommend if: SEO content active or planned (Q9 = Yes or Planning)
→ Skip if: purely paid media / no content strategy

**`art-director`**
→ Recommend if: any visual content being created (paid ads, print, OOH, packaging)
→ Skip if: purely text/copy work only

**`graphic-design`**
→ Recommend if: paid social ads running AND design assets needed
→ Skip if: no visual creative work

**`ux-website-designer`**
→ Recommend if: has website with conversion goals (Q15 = Yes)
→ Also recommend if: CRO is a priority
→ Skip if: no website or purely brand awareness

**`cro-orchestrator`**
→ Recommend if: eCommerce or lead gen site (Q15) AND some traffic/data to work with
→ Essential if: growth stage or above (Q2c/d) with paid media
→ Skip if: pre-launch or no website

**`video-content-strategy`**
→ Recommend if: any video content planned (Q10 = Yes to any)
→ Skip if: no video content planned

**`pr-influencer`**
→ Recommend if: influencer marketing planned (Q16) OR PR planned (Q17)
→ Skip if: Q16 = No AND Q17 = No

**`print-design`**
→ Recommend if: print ads, direct mail, or brochures selected (Q14)
→ Skip if: digital-only brand

**`ooh-design`**
→ Recommend if: out-of-home / billboards selected (Q14)
→ Skip if: no OOH planned

**`packaging-brand-design`**
→ Recommend if: physical product (Q3 = Yes) OR trade show/corporate identity selected (Q14)
→ Skip if: digital-only / no physical products

**`retail-design`**
→ Recommend if: branded merchandise (Q4 = Yes or Interested)
→ Skip if: no merchandise planned

**`best-practices`**
→ Recommend if: any paid media active (Q5 = Yes) OR email marketing active
→ Note: "Run monthly review cadence"
→ Skip if: pre-launch / not yet running any channels

---

## Output Format

Produce a team configuration document at `brand-intelligence-center/team-config.md`:

```markdown
# [Brand Name] — Marketing Agent Team Configuration

**Configured:** {{date}}
**Business model:** [type from Q1]
**Stage:** [stage from Q2]

---

## Your Recommended Team

### 🟢 Install Now — Core Team
[List agents with one-line rationale each]

### 🟡 Install When Ready — Activate As You Scale
[List agents with trigger condition — "install when you start running paid ads", etc.]

### ⚪ Skip For Now
[List skipped agents with reason]

---

## Priority Order for Getting Started

1. **[First action]** — [what to do and which agent]
2. **[Second action]**
3. **[Third action]**

---

## Your Starting Workflow

[Describe the first complete workflow this brand should run — e.g., "Run /brand-setup to complete your Brand Intelligence Center, then use /campaign-new to brief your first campaign."]

---

## Team Summary

**Total agents recommended:** [N] of 22
**Channels covered:** [list]
**Gaps to address later:** [any channels/capabilities not yet covered]
```

After delivering the recommendation, ask:
> **Would you like to set up your analytics and data connections next?**
> Running `/analytics-setup` will connect your data sources, audit your historical performance, and establish the benchmarks your Marketing Analytics agent will use.
