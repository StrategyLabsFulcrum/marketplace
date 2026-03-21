# Audience Targeting Guide

How to translate the Campaign Strategist's audience brief into platform-specific targeting configurations. The audience brief defines *who* — this guide defines *how to reach them* on each platform.

---

## Reading the Audience Brief

The Campaign Strategist's `campaign-brief.md` includes an audience section with:
- **Primary audience:** Core target (demographics, psychographics, behaviors, pain points)
- **Secondary audience:** Expansion segment
- **Audience insight:** The key truth about why this audience behaves as they do
- **Targeting signals:** Specific attributes that identify this audience in ad platforms

Use these as your raw material. Your job is to translate each attribute into platform targeting syntax.

---

## Audience Tiering Framework

Structure all campaigns around three audience tiers. Allocate budget and tailor creative for each.

### Tier 1 — Retargeting (Warmest)

People who have already engaged with the brand. Highest intent, smallest audience, highest conversion rate.

**Build from:**
- Website visitors (all pages: 30/60/90/180 days)
- High-intent page visitors (product, pricing, checkout pages — 30 days)
- Add-to-cart / Initiated checkout (7–14 days — most urgent)
- Video viewers (25%+, 50%+, 75%+ watch time)
- Social engagers (page likers, post interactors, DM senders — 30/60/90 days)
- Email subscribers (upload list)
- Past purchasers (for repurchase / cross-sell campaigns)

**Targeting approach:** Narrow — these audiences are already self-identified. Keep creative specific to their stage (abandoned cart → urgency; high-intent page visitor → social proof and objection handling).

**Budget allocation:** 15–25% of total paid social budget. Higher ROAS, smaller volume.

**Exclusions within Tier 1:** Exclude recent purchasers from acquisition ad sets (unless cross-sell/upsell is the goal). Exclude converted leads from lead gen ad sets.

### Tier 2 — Lookalike (Middle)

Platform-generated audiences that statistically resemble your best existing customers. Good balance of intent and scale.

**Build from (in priority order):**
1. Purchaser lookalike (seed: customer purchase list) — 1%, 2%, 5%
2. High LTV customer lookalike (seed: top 20% customers by revenue) — if segmented
3. Email subscriber lookalike (seed: active subscriber list, 1,000+ minimum)
4. Website visitor lookalike (seed: all visitors, 30–60 days)

**Lookalike percentage guidance:**
- 1%: Most similar; smaller audience; higher CPC but higher relevance. Start here.
- 2–3%: Slightly broader; good middle ground for scaling
- 5–10%: Broad lookalike; more like interest targeting; useful when 1–3% exhausted

**Platform notes:**
- **Meta:** 1% lookalike = approximately 2M in US market. Start with 1%. Move to 2–3% if 1% shows frequency > 2.5 or declining performance.
- **Google:** Similar Audiences (now Optimized Targeting in PMax). Upload customer list to Google Ads; Google generates similar audiences automatically.
- **LinkedIn:** Lookalike from company or contact list; minimum 300 matched members in seed.
- **TikTok:** Lookalike from custom audience seed. TikTok lookalikes work particularly well.

### Tier 3 — Cold Interest/Behavior (Coldest)

Reaching new audiences who haven't interacted with the brand. Highest volume, lowest conversion rate, requires the strongest creative.

**Building cold audiences on Meta:**
- Interest targeting: Select 2–5 related interests. Stack interests within the same ad set (OR logic — reach anyone who has any of these). Do not cross-stack unrelated interests.
- Behavior targeting: Online buyers (digital activities), frequent travelers, small business owners, etc.
- Broad targeting: No interests or behaviors — just age, gender, location. Counter-intuitive but increasingly effective with strong creative; let Meta's algorithm do the work.
- Demographics: Age range, gender (if product skews strongly), income/household (via Detailed Targeting)

**Building cold audiences on Google:**
- In-Market audiences: Google identifies people actively researching a category. Use as audience signal or layered targeting.
- Custom Segments: Build from keywords (people who searched for X), URLs (people who visited competitor sites), or apps.
- Affinity audiences: Broader lifestyle categories; good for awareness, not conversion.

**Building cold audiences on LinkedIn:**
- Job Title + Company Size: Most precise B2B targeting
- Job Function + Seniority: Broader reach when job titles are inconsistent
- Industry + Seniority: Good for vertical targeting without title specificity
- Skills: Self-reported; useful for technical roles

**Cold audience sizing guidance:**

| Platform | Recommended Cold Audience Size |
|---------|-------------------------------|
| Meta | 2M–15M (US); below 1M and CPMs spike; above 20M and relevance drops |
| Google Display | 5M+ recommended for meaningful reach |
| LinkedIn | 300K+ minimum; 500K–2M ideal for most B2B campaigns |
| TikTok | 1M+ preferred; broad targeting with algorithm is often best |

---

## Translating Audience Brief Attributes to Platform Targeting

### Age and Gender

**If targeting skews female (70%+):**
- Meta: Set gender targeting to Female in ad set settings
- Google: Demographics → Gender → Female only
- LinkedIn: Gender targeting available but avoid unless very strong skew (limits reach significantly)

**Age range:**
- Meta: Age range in ad set demographics
- Google: Demographic bid adjustments (not exclusions unless budget is very tight)
- LinkedIn: Age targeting available; overlap with Seniority is often more precise for B2B

**Default:** Do not restrict age unless there is a strong, data-backed reason. Age restriction reduces audience size and raises CPMs. Let the algorithm optimize.

### Income and Household

**Meta:**
- Detailed Targeting → Demographics → Financial → Income
- Top 10% household income, top 25%, etc. (available in some markets)

**Google:**
- Household Income targeting: Top 10%, 11–20%, 21–30%, Lower 50% — available in Demographics section
- Useful for luxury products or price-sensitive audiences to ensure targeting right segment

### Geographic Targeting

**National campaigns:**
- Meta: Country + exclude specific states if needed
- Google: Country level; use bid adjustments by state/city for performance optimization
- LinkedIn: Country level

**Local/regional campaigns:**
- Meta: DMA (Designated Market Area), city, radius (as small as 1 mile from a location)
- Google: City, state, DMA, radius
- LinkedIn: Metro area, state, country

**Exclusion by location:**
- Always exclude locations where the product/service is unavailable
- For delivery-dependent products: exclude states with legal restrictions or service gaps

### Behavioral Attributes

**Purchase intent signals:**
- Meta → Detailed Targeting → Behaviors → Purchase Behavior
- Google → In-Market Audiences (people actively researching the category)
- Google Custom Segments → keyword-based (build from high-intent search queries)

**Device behaviors:**
- Meta: Device type (mobile vs. desktop), operating system (iOS vs. Android), connection type
- Google: Device targeting (mobile, tablet, desktop), bid adjustments by device

**Technology / platform use:**
- Meta: Behaviors → Digital Activities (Facebook Page admins, Instagram Business profiles, etc.)

### Professional Attributes (B2B)

LinkedIn is the primary platform for professional attribute targeting. On other platforms:

**Meta:**
- Job Title targeting: Detailed Targeting → Demographics → Work → Job titles (limited selection)
- Industry: Detailed Targeting → Demographics → Work → Industries
- Employer: Detailed Targeting → Demographics → Work → Employers (specific companies)
- B2B behavioral audiences: Purchased from ecommerce, SMB owners, etc.

**Google:**
- Professional Audiences: In-Market (Business Services, Enterprise Technology, etc.)
- Custom Segments by URL: People who visit competitor sites or industry publications
- Customer Match: Upload existing B2B contact list

**LinkedIn (primary B2B platform):**
- Job Title: Most precise; use multiple variations of the same role
- Job Function: Broader; use when titles are inconsistent across company sizes
- Seniority: VP, Director, Manager, C-Suite, Owner — combine with Function for best results
- Company Size: 1–10, 11–50, 51–200, 201–500, 501–1000, 1001–5000, 5001–10000, 10001+
- Industry: Select from LinkedIn's 150+ industry categories
- Company: Specific companies for ABM targeting (upload company list)

---

## Audience Overlap Management

Running multiple ad sets targeting the same or overlapping audiences creates auction competition between your own campaigns (you bid against yourself) and inflated frequency.

**How to avoid overlap:**

**Meta audience overlap tool:**
- In Ads Manager → Audiences → select multiple audiences → Actions → Show Audience Overlap
- If overlap > 20–30% between ad sets in the same campaign, consolidate or add exclusions

**Exclusion strategy:**
- If running a lookalike campaign: exclude your retargeting audiences (Tier 1) from lookalike ad sets
- If running cold interest targeting: exclude both Tier 1 and Tier 2 lookalike audiences
- This creates a clean funnel structure where each tier reaches a distinct audience

**Budget and tiering alignment:**

| Tier | Audience | Exclusions | Creative Focus |
|------|---------|-----------|---------------|
| Tier 1 — Retargeting | Warm (visitors, engagers, list) | None needed within tier | Stage-specific — urgency, objection handling, social proof |
| Tier 2 — Lookalike | Platform-generated lookalike | Exclude Tier 1 audiences | Benefit-focused — introduce the offer to a warm-ish audience |
| Tier 3 — Cold | Interest, broad, behavior | Exclude Tier 1 + Tier 2 | Awareness-building — hook, problem, story |

---

## Audience Build Checklist

Before launching any campaign, verify:

- [ ] Tier 1 retargeting audiences built and have sufficient size (minimum 1,000 members for Meta custom audiences to deliver)
- [ ] Lookalike sources have minimum audience size (1,000 people for Meta lookalike seed)
- [ ] Cold audiences sized appropriately (not too narrow for the platform)
- [ ] Exclusions applied between tiers
- [ ] Recent purchasers excluded from acquisition campaigns
- [ ] Unsubscribers excluded from email acquisition lists
- [ ] Geographic targeting matches where the product/service is available
- [ ] Age/gender restrictions are justified by data (not assumption)
- [ ] Audience overlap checked for campaigns targeting similar people

---

## Audience Scaling Signals

When to expand audiences:

| Signal | Action |
|--------|--------|
| Frequency exceeding 3.5 on Meta | Expand to larger lookalike % or add new interest audiences |
| Audience size below 20% of available | Broaden targeting parameters |
| CPM rising without performance improvement | Audience saturation; expand or refresh |
| Lookalike 1% exhausted | Test 2%, 3%, 5% |
| All warm audiences converting well | Scale budget; add new lookalike seeds |

When to narrow audiences:

| Signal | Action |
|--------|--------|
| CPA significantly above target | Test narrowing to higher-intent segments |
| Audience overlap above 30% | Restructure with exclusions |
| Broad targeting not converting after 4+ weeks | Add interest layer to provide algorithm with signals |
| Very large audience with low relevance score | Narrow to more qualified segment |
