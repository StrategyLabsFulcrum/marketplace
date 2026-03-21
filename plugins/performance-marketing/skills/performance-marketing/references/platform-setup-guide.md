# Platform Setup Guide

Campaign configuration standards for each paid media platform. Reference during Step 4 when briefing platform specialists.

---

## Meta (Facebook + Instagram)

### Account Structure Best Practices

**Campaign level:** Set objective. This determines how Meta optimizes delivery.
**Ad Set level:** Set audience, budget, placements, schedule.
**Ad level:** Set creative (image/video + copy + destination URL).

Never mix multiple objectives in one campaign. Never build ad sets so narrow that audience size falls below 2,000,000 for cold traffic (algorithm needs room to find converters).

### Campaign Objectives — When to Use Each

| Objective | Use When |
|-----------|---------|
| Sales (Conversions) | Driving purchases, sign-ups with defined value. Requires sufficient conversion data (50+/week per ad set). |
| Leads | Collecting leads via Meta Lead Form or website form. Lower friction than offsite conversion. |
| Traffic | Driving clicks to site when conversion tracking is not yet set up, or for content/blog traffic. |
| Awareness (Reach) | Upper funnel — maximizing reach within a defined audience. Optimizes for impressions, not actions. |
| Engagement | Promoting posts, generating social proof (likes, comments, shares). Secondary use. |
| App Installs | Driving app downloads via App Store / Play Store. Requires SDK integration. |

**Default:** Use Sales/Conversions objective whenever the pixel has enough conversion data. Switch to Traffic only if pixel has fewer than 50 conversion events in the past 30 days — Meta cannot optimize for an event it has not seen enough of.

### Bid Strategy Selection

| Bid Strategy | When to Use |
|-------------|------------|
| Highest Volume (formerly Lowest Cost) | Default for most campaigns. Let Meta find the lowest CPA without a constraint. |
| Cost Per Result Goal | When you have a specific CPA target. Set at 20–30% above your actual target — setting too tight will restrict delivery. |
| ROAS Goal | E-commerce campaigns. Requires sufficient purchase data. Set at realistic level — too high and Meta won't spend. |
| Bid Cap | Advanced use only. Caps maximum bid per auction. Risks underspending if set too low. |

### Audience Types and Sequencing

**Tier 1 — Warm audiences (highest intent):**
- Website visitors (last 30, 60, 180 days — segment by page visited and recency)
- Video viewers (25%, 50%, 75%, 95% — target higher engagement tiers)
- Customer list upload (existing customers, email subscribers)
- Instagram/Facebook engagers (last 30–365 days)

**Tier 2 — Lookalike audiences:**
- Lookalike of purchasers (1%, 2%, 5% — start tight, expand if volume is low)
- Lookalike of email subscribers
- Lookalike of high-value customers (if segmented in CRM)
- Source audience minimum: 100 people; recommended: 1,000+ for quality lookalikes

**Tier 3 — Cold interest/behavior audiences:**
- Interest targeting (stack 2–5 related interests; avoid over-narrowing)
- Behavior targeting (online buyers, engaged shoppers)
- Broad targeting (no interest targeting — let Meta's algorithm find the audience; works well with strong creative and sufficient budget)

**Audience exclusions (always apply):**
- Exclude recent purchasers from acquisition campaigns (30–90 days depending on repurchase cycle)
- Exclude existing customers from new customer acquisition campaigns
- Exclude audiences already in a conversion stage from awareness campaigns

### Budget Minimums

| Use Case | Minimum Daily Budget (per ad set) |
|---------|----------------------------------|
| Conversion campaign (learning phase) | $30–50/day — below this, learning phase is too slow |
| Traffic campaign | $10–15/day minimum viable |
| Retargeting (warm audiences) | $10–20/day (audiences are smaller, less budget needed) |
| Testing (A/B creative test) | Equal budget per variation; minimum $20/day per variation |

**Learning phase:** Meta ad sets enter learning phase when first launched or after significant edits. During learning phase (first 50 optimization events), do NOT change budgets, audiences, or creative — each change resets the learning phase. Plan for 1–2 week learning period before drawing conclusions.

### Placement Strategy

**Advantage+ Placements (automatic):** Default recommendation. Meta allocates across Feed, Stories, Reels, Audience Network, Messenger based on performance signals.

**Manual placements — when to use:**
- Instagram only: if brand skews Instagram; or for Stories/Reels-specific creative
- Feed only: if you only have static image creative (not optimized for vertical Reels)
- Exclude Audience Network: if brand safety is a concern; Audience Network placements are off-Meta properties

**Never exclude placements without a reason.** Fewer placements = less inventory = higher CPMs.

### Creative Testing Framework

Isolate one variable per test. Do not change audiences and creative simultaneously.

**Creative test structure:**
- 1 ad set
- 2–4 ad variations
- Equal budget split
- Same audience, placements, bid strategy
- Run for minimum 7 days or 100 link clicks per variation before reading results

**What to test (in priority order):**
1. Hook / opening frame (first 1–3 seconds or first line)
2. Format (video vs. static; carousel vs. single image)
3. Copy angle (benefit vs. social proof vs. fear vs. curiosity)
4. CTA (button text, destination)
5. Visual approach (lifestyle vs. product; dark vs. light)

---

## Google Ads

### Campaign Types — When to Use

| Campaign Type | Use When |
|--------------|---------|
| Search | Intent-based — people actively searching for your product/category/solution |
| Performance Max | Broad reach across all Google inventory with a single campaign; requires conversion data; good for e-commerce |
| Display | Awareness and retargeting; visual ads across the Google Display Network |
| Shopping | E-commerce product ads in search results; requires product feed |
| YouTube | Video advertising; in-stream, bumper, in-feed |
| Demand Gen | Social-like discovery across YouTube, Gmail, Discover; replaces old Discovery campaign type |

**Default recommendation for most advertisers:**
- Start with Search (branded + non-branded keywords) for intent capture
- Add retargeting Display to recapture site visitors
- Add Performance Max when you have sufficient conversion history (100+ conversions in 30 days)

### Search Campaign Structure

**Match type strategy:**
- **Exact match:** Highest control, lowest volume. Use for proven, high-intent keywords.
- **Phrase match:** Middle ground. Triggers for searches containing the phrase in order. Good default.
- **Broad match:** Highest volume, least control. Only use with Smart Bidding (Target CPA or Target ROAS) — requires conversion data for Google to optimize broad queries effectively.

**Negative keywords — always add at launch:**
- Competitor brand names (unless you're running conquesting)
- Irrelevant verticals that share your keywords
- Informational queries if you're optimizing for purchase intent ("how to", "what is", "free")
- Your own brand terms in non-brand campaigns (to prevent cross-contamination)

**Ad Group organization:**
- Group keywords by tight semantic theme (not just category — theme)
- 5–15 keywords per ad group is ideal
- Each ad group should have 2–3 RSAs (Responsive Search Ads)
- Ad copy should directly mirror the keyword theme — high relevance = higher Quality Score = lower CPC

### Bidding Strategy Progression

**New campaigns — limited conversion data:**
1. Start with Maximize Clicks or Manual CPC — generate traffic and initial conversion data
2. After 30+ conversions: switch to Target CPA (set at ~20% above your actual observed CPA)
3. After 100+ conversions/month: consider Target ROAS if revenue optimization is primary goal

**Established campaigns:**
- Target CPA is the standard for lead generation and app install campaigns
- Target ROAS is standard for e-commerce with conversion values
- Maximize Conversion Value is a good alternative to Target ROAS with a known budget constraint

### Quality Score Factors

Quality Score (1–10) affects your cost per click and ad rank. Improve it by:
- **Expected CTR:** Write compelling headlines with clear value proposition and keyword inclusion
- **Ad relevance:** Ensure ad copy directly addresses the keyword theme in each ad group
- **Landing page experience:** Landing page should match the keyword intent; fast load time; mobile-friendly

Target: Quality Score 7+ for priority keywords. Below 5 is a problem worth diagnosing.

### Performance Max Configuration

Performance Max (PMax) runs across all Google inventory with a single campaign. Setup requires:
- **Asset groups:** Organize by product/theme/audience. Include all asset types (headlines, descriptions, images, videos, logos, callouts)
- **Audience signals:** Not targeting, but signals to help Google find your best customers faster. Include: customer match list, website visitors, in-market segments relevant to your product
- **URL expansion:** Allow (Google selects landing pages) or restrict (you define landing pages per asset group)
- **Brand exclusions:** Exclude your own brand terms from PMax if running a separate Brand Search campaign

PMax requires patience — it needs 4–6 weeks and significant conversion volume to optimize. Do not judge early results.

### Budget Minimums

| Campaign Type | Minimum Daily Budget |
|--------------|-------------------|
| Search (brand only) | $10–15/day |
| Search (non-brand) | $30–50/day (needs impression/click volume to optimize) |
| Display (retargeting) | $10–15/day |
| Performance Max | $50–75/day minimum; $100+/day recommended |
| Shopping | $20–30/day minimum |

---

## Email Platforms

### Klaviyo

**Campaign setup:**
1. Create campaign → Name (internal), Subject line, Preview text
2. Select recipients: list or segment
3. Set exclusions: unsubscribers, suppressed contacts, recent purchasers if needed
4. Choose send time: specific time or Klaviyo Smart Send (sends at each recipient's optimal time based on engagement history)
5. A/B test option: subject line, content, send time — 20–20–60 split is standard (20% to each variant, 60% to winner after test window)

**Flow (sequence) setup:**
1. Create flow → Choose trigger: list join, segment entry, date property, metric (placed order, abandoned cart, etc.)
2. Build email sequence with delay nodes between emails
3. Add conditional splits: if/else logic based on opens, clicks, conversions, profile properties
4. Set exit conditions: purchase, opt-out, or time limit

**Segment best practices:**
- Engagement segments: highly engaged (opened last 30 days), engaged (last 90 days), unengaged (not opened in 90+ days)
- Suppress unengaged contacts from promotional sends — protects deliverability
- Never send to an unengaged list without a re-engagement campaign first

**Deliverability checklist:**
- [ ] Custom sending domain configured (not shared Klaviyo domain)
- [ ] SPF record set for sending domain
- [ ] DKIM record set for sending domain
- [ ] DMARC policy configured
- [ ] List imported from verified opt-in source only
- [ ] Unsubscribe link present and functional
- [ ] Physical mailing address in footer (CAN-SPAM requirement)
- [ ] Preview renders correctly on mobile and desktop (test in Klaviyo or Litmus)

### Mailchimp

Similar structure to Klaviyo. Key differences:
- Automations (sequences) are built in "Customer Journeys"
- Audience segments are called "Tags" or "Segments"
- Deliverability tools are under "Domain Verification" in Settings
- A/B testing: up to 3 variants in campaigns

---

## LinkedIn Ads

### When to Use LinkedIn

LinkedIn is expensive (CPM 3–5× Meta) but reaches a professional audience. Worth the premium when:
- B2B offer with job title, company size, or industry as key targeting criteria
- High ACV (average contract value) deal where CPL of $100–500 is acceptable
- Recruiting or employer brand campaigns
- Content targeting decision-makers in specific industries

### Campaign Structure

**Campaign Groups:** Top-level containers. Organize by campaign objective or audience tier.
**Campaigns:** Set objective, budget, bidding, targeting.
**Ads:** Individual creative units.

### Targeting Options (LinkedIn's differentiation)

| Attribute | Notes |
|-----------|-------|
| Job Title | Exact match — use multiple titles; titles vary by company size and industry |
| Job Function + Seniority | Broader reach; good when job titles are inconsistent |
| Company Size | Key for B2B — segment SMB vs. mid-market vs. enterprise |
| Industry | 150+ industry categories |
| Skills | Self-reported; use for technical targeting |
| Company Name | Specific account list — ABM (Account-Based Marketing) |
| LinkedIn Groups | Members of specific professional groups |
| Education | Degree, field of study, school |
| Interests | LinkedIn interest categories |
| Lookalike | Lookalike of uploaded contact or company list |

**Minimum audience:** 300,000 members recommended. Below 50,000 risks limited delivery.

### Budget Minimums

| Use Case | Minimum Daily Budget |
|---------|-------------------|
| Any LinkedIn campaign | $10/day (platform minimum) |
| Effective brand awareness | $50–75/day |
| Lead generation | $75–150/day (CPL is high; need sufficient spend) |

### LinkedIn Ad Formats

| Format | Best For |
|--------|---------|
| Single Image | Standard feed ads; most common |
| Carousel | Multiple product/feature showcase |
| Video | Storytelling, brand awareness, demos |
| Document Ads | Gated content (whitepapers, reports) — in-feed download |
| Conversation Ads | Direct InMail-style; higher cost but high intent |
| Thought Leader Ads | Boost posts from individual employees' profiles — authentic feel |
| Lead Gen Forms | Native forms; high completion rate (pre-filled from LinkedIn profile) |

---

## TikTok Ads

### Account Structure

**Campaign:** Objective. TikTok objectives: Reach, Traffic, App Installs, Video Views, Lead Generation, Community Interaction, Website Conversions, Product Sales.
**Ad Group:** Targeting, budget, placement, optimization goal.
**Ad:** Creative (video required for most formats), copy, CTA.

### Creative Requirements

TikTok is a video-first platform. Static images can run but perform significantly worse.

**Video specs:**
- 9:16 vertical — required
- 1080×1920px
- 15–60 seconds (15–30s performs best)
- Native-looking content outperforms polished ads — raw, UGC-style, direct-to-camera

**Hook rules:**
- First 1–3 seconds determine retention — this is where most viewers decide to scroll
- Open with motion, dialogue, or a surprising visual — never a logo
- Sound-on audience: music and voiceover matter significantly more than on Meta

### Targeting

| Option | Notes |
|--------|-------|
| Interest targeting | Broad categories; TikTok's algorithm is powerful — broad works well with strong creative |
| Behavioral targeting | In-app behaviors (video interactions, hashtag follows) |
| Custom Audience | Website visitors, app users, engagement audiences |
| Lookalike | From custom audience seed |
| Broad (no targeting) | Let algorithm optimize; requires strong creative; can be most efficient at scale |

**TikTok's algorithm is particularly good at finding relevant audiences with minimal targeting.** Trust it more than on Meta. Overly narrow targeting often hurts delivery.

### Budget Minimums

| Level | Minimum |
|-------|---------|
| Campaign daily budget | $50/day |
| Ad Group daily budget | $20/day |

---

## Cross-Platform Budget and Pacing

### Budget Pacing Rules

**Daily vs. lifetime budgets:**
- Daily budget: More control over spend per day; recommended for ongoing campaigns
- Lifetime budget: Platform handles pacing; useful for fixed-end campaigns; less control day-to-day

**Pacing watch:**
- Check spend daily for first 1–2 weeks of a new campaign
- If underspending (<80% of daily budget): audience too narrow, bid too low, or creative rejected. Diagnose and fix.
- If overspending (>110% of daily budget): platform allowing overdelivery. Common on Meta (up to 25% overspend in a day, balanced over a week). Normal; monitor weekly total.

### Learning Phase Management

All major platforms have a learning/optimization phase. Rules:
- **Meta:** 50 optimization events per ad set. Avoid edits during this phase.
- **Google Smart Bidding:** 30–90 conversions per month minimum for Target CPA to work. 100+ for Target ROAS.
- **TikTok:** 50 optimization events per ad group.
- **LinkedIn:** 100 clicks or 5,000 impressions before reading results.

**During learning phase:** Do not make budget changes above 20% per edit. Do not change targeting or creative. Watch delivery but do not optimize aggressively. Let the algorithm learn.
