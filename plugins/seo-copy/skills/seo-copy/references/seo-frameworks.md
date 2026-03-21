# SEO Frameworks

On-page optimization requirements, content architecture, and content cluster strategy.

---

## On-Page SEO Requirements Checklist

Every piece of SEO content must satisfy these before delivery:

### Meta Elements
- [ ] **H1 / Page title:** Contains primary keyword; compelling for humans; unique on the site
- [ ] **Meta title:** 50–60 characters; primary keyword near the front; brand name at end if space allows
- [ ] **Meta description:** 150–160 characters; includes primary keyword; has implicit CTA; unique per page
- [ ] **URL slug:** Short; contains primary keyword; no stop words; hyphens not underscores

### Heading Structure
- [ ] One H1 only — the page title
- [ ] H2s for major subtopics — each H2 should represent a distinct topic cluster
- [ ] H3s for detail within H2 sections
- [ ] H4s sparingly — only if needed for deep hierarchical content
- [ ] No skipped heading levels (H1 → H3 skipping H2)

### Keyword Integration
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words (introduction)
- [ ] Primary keyword appears 2–4× more throughout (varies by length)
- [ ] Secondary keywords distributed across relevant sections
- [ ] LSI/semantic terms used naturally (related vocabulary signals topical depth)
- [ ] No keyword stuffing (unnatural repetition = penalty risk)

### Content Quality Signals
- [ ] Unique angle — covers topic better or differently than top 3 results
- [ ] Specific data, examples, or proprietary information included
- [ ] All claims supported or sourced
- [ ] Author/brand expertise established (E-E-A-T)
- [ ] Updated date if content is time-sensitive

### Internal Links
- [ ] 2–4 internal links to related pages
- [ ] Anchor text is descriptive (not "click here" or "read more")
- [ ] Links open in same tab (not new tab for internal)

### Featured Snippet Optimization
- [ ] If targeted keyword has a featured snippet: direct answer paragraph written (40–60 words)
- [ ] Tables and lists formatted in snippet-friendly structure
- [ ] FAQ section addresses People Also Ask questions

---

## Keyword Intent Classification

Before writing, classify the keyword's intent — this determines the entire page strategy.

### Informational Keywords

**Signals:** "how to", "what is", "why", "guide", "tutorial", "tips", "examples"
**Searcher state:** Learning; not ready to buy
**Content strategy:**
- Comprehensive, authoritative answer
- No hard CTAs — soft next-step links to related content
- Long form (1,500–3,000+ words) if competitive
- Educational tone; expertise signals

**Best content types:** How-to guides, explainers, definitions, listicles, FAQs

### Commercial Investigation Keywords

**Signals:** "best", "top", "vs", "alternatives", "review", "comparison", "worth it"
**Searcher state:** Evaluating options; pre-purchase research
**Content strategy:**
- Honest comparison with clear positioning of the brand
- Feature/benefit tables; pros and cons
- Include competitor mentions (transparent, honest, not defamatory)
- CTA at the end when reader has enough information

**Best content types:** Comparison articles, review pages, "best X for Y" listicles, alternative pages

### Transactional Keywords

**Signals:** "buy", "price", "order", "near me", "hire", "book", "discount", "coupon"
**Searcher state:** Ready to purchase or close to it
**Content strategy:**
- Less content, more CTA
- Product/service benefits prominent
- Remove friction: clear pricing, clear next step
- Trust signals (reviews, guarantee)

**Best content types:** Product pages, service pages, location pages, pricing pages

### Navigational Keywords

**Signals:** Brand name, specific product name, "[brand] login", "[brand] contact"
**Searcher state:** Looking for a specific brand/page
**Content strategy:**
- Brand-focused; confirm you're in the right place
- Clear navigation to key actions
- Minimal distractions

---

## Content Cluster Architecture

Single pages do not rank in competitive niches. Content clusters — interconnected topic networks — signal topical authority to Google.

### Hub-and-Spoke Model

```
Hub page (Pillar page)
"Complete Guide to [Broad Topic]"
Primary keyword: [broad head term]

├── Spoke 1: [Subtopic] — [long-tail keyword]
├── Spoke 2: [Subtopic] — [long-tail keyword]
├── Spoke 3: [Subtopic] — [long-tail keyword]
├── Spoke 4: [Subtopic] — [long-tail keyword]
└── Spoke N: [Subtopic] — [long-tail keyword]
```

**Hub (pillar page):**
- Covers the broad topic at high level with deep supporting links
- Links out to all spoke pages
- Typically 2,000–4,000 words
- Targets high-volume, competitive head term

**Spoke (cluster) pages:**
- Deep dive into specific subtopic
- Links back to hub page
- Links to related spokes
- Typically 1,000–2,000 words
- Targets specific long-tail keyword

**Internal linking rules for clusters:**
- Every spoke links to the hub (anchor: hub's primary keyword)
- Hub links to every spoke (anchor: spoke's primary keyword)
- Related spokes link to each other (3+ per page)

---

## Content Length Guide

Longer is not always better. Match depth to the query intent and competitive landscape.

| Content Type | Typical Length | Why |
|-------------|---------------|-----|
| Pillar page / Ultimate guide | 3,000–6,000+ words | Comprehensive coverage signals authority |
| Long-form how-to / tutorial | 2,000–3,500 words | Needs enough depth to satisfy the full query |
| Comparison / Best-of list | 1,500–2,500 words | Enough to compare fairly; don't pad |
| Shorter informational post | 800–1,500 words | Some queries don't need more |
| FAQ page | 500–1,500 words | Concise answers; structured data format |
| Product/service page | 400–1,000 words | Conversion-focused; clarity over length |
| Programmatic page | 300–600 words | Template content; unique enough per page |

**The right length:** Match or modestly exceed the average length of the top 3 organic results for the target keyword. Do not pad to hit an arbitrary word count.

---

## Featured Snippet Optimization

Featured snippets appear above organic results for specific queries. Winning a featured snippet can double or triple organic CTR.

### Snippet types and how to target them:

**Paragraph snippet** (definition or explanation):
- Write a clear, concise paragraph (40–60 words) answering the query directly
- Place it in the first section of the article or at the top of the relevant section
- Start with the keyword in the first few words: "[Primary keyword] is..."

**List snippet** (steps or items):
- Use a numbered (H-tag → ordered list) or bulleted (H-tag → unordered list) structure
- Each item should be concise (under 40 characters per item)
- Format:
  ```
  ## [H2 containing keyword]
  1. [Step/item]
  2. [Step/item]
  3. [Step/item]
  ```

**Table snippet** (comparison or data):
- Use standard markdown/HTML tables
- Column headers should include keywords naturally
- Keep rows concise

**Video snippet** (for how-to queries):
- Note in brief that a video component may be needed for full snippet eligibility

### Featured snippet paragraph template:

```
**[Primary keyword as defined term/question]** [definition or direct answer in 1–2 sentences, under 60 words total, starting with the defined term]. [Optional: one specific supporting detail or context sentence].
```

---

## Programmatic SEO Content Templates

For large-scale programmatic pages (location pages, comparison pages, category pages), use a template structure with unique variable content.

### Location page template structure:
```
H1: [Service] in [City, State]
Meta: [Service] in [City] — [Benefit] | [Brand]

Section 1: What we offer in [City] — localized benefit paragraph
Section 2: Why [City] businesses/people choose [Brand] — 3 differentiators
Section 3: [City]-specific proof — testimonial from [City] customer if available
Section 4: Service details / process
Section 5: FAQ — [City]-specific questions
CTA: Contact/Book/Get started
```

**Uniqueness requirement for programmatic:** Each programmatic page must have at least one section of genuinely unique content. Google ignores near-duplicate template pages. Minimum unique content: 200 words per page beyond the template.

### "Best X in [city]" / "X alternatives" template:
```
H1: Best [Category] [in City / in 2026] / [Product] Alternatives
Intro: Intent-matching paragraph + summary of what this page covers
Comparison table: Key attributes compared
Item 1 — H2: [Option 1] — in-depth mini-review
Item 2 — H2: [Option 2] — etc.
FAQ: Answers to common questions about this category
Conclusion: Recommendation summary + CTA
```

---

## E-E-A-T Signals Checklist

Google's quality rater guidelines emphasize Experience, Expertise, Authoritativeness, Trustworthiness. Include these signals:

**Experience:**
- [ ] First-person experiences or case examples included
- [ ] Specific scenarios and situations referenced (not theoretical)
- [ ] Author bio or brand context explaining relevant experience

**Expertise:**
- [ ] Accurate, technically correct information
- [ ] Depth that matches the topic's complexity
- [ ] Sources cited for statistics and factual claims
- [ ] Proprietary frameworks, research, or data

**Authoritativeness:**
- [ ] Brand/author mentioned in related authority publications
- [ ] Internal content cluster demonstrates topical coverage
- [ ] External links to reputable sources used

**Trustworthiness:**
- [ ] No misleading claims or clickbait/overstatement
- [ ] Transparent about limitations or trade-offs
- [ ] Updated date if content changes over time
- [ ] Privacy policy and contact information accessible on site

---

## Schema Markup Recommendations

Schema markup is structured data that helps Google understand and display content. Note recommendations for the web team when applicable.

| Content Type | Recommended Schema |
|-------------|-------------------|
| Article / Blog post | Article, BlogPosting |
| FAQ section | FAQPage |
| How-to content | HowTo |
| Product page | Product, Offer |
| Review page | Review, AggregateRating |
| Local business | LocalBusiness |
| Person / Author | Person |
| Organization | Organization |
| Breadcrumbs | BreadcrumbList |

Note schema recommendations in the delivery notes — implementation is the web team's responsibility.
