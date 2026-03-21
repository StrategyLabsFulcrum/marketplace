# Specialist Brief Templates

Complete brief formats for each specialist the Creative Director spawns. Each brief is self-contained — the specialist executes from it plus their own skill knowledge plus brand intelligence. They do not need to read the full campaign brief.

Every brief shares a common header block, then specialist-specific sections.

---

## Common Header Block (all briefs)

```markdown
# [Specialist Name] Brief — {{Campaign Name}}

> **From:** Creative Director
> **To:** {{Specialist name}}
> **Campaign:** {{campaign-slug}}
> **Date issued:** {{date}}
> **Output due:** {{date}}
> **Save output to:** campaigns/{{slug}}/creative/copy/{{filename}}.md
>   (or campaigns/{{slug}}/creative/design/{{filename}}.md for design briefs)

---

## Brand Context
**Brand:** {{brand name}}
**Active brand file:** `brand-intelligence-center/system-prompt.md`
> Read this file first. The brand rules below summarize what's most relevant to this assignment, but the full brand context file is the authority.

## The Creative Concept
**Campaign idea:** {{one sentence — the unifying platform}}
**Campaign line:** "{{the headline or tagline anchoring all executions}}"
**Visual direction:** {{3–5 descriptive words}}
**Tone for this campaign:** {{specific calibration within brand voice}}

## Brand Voice Rules (Most Relevant to This Assignment)
**NEVER:**
{{Paste the 3–5 NEVER rules most relevant to this type of output}}

**ALWAYS:**
{{Paste the 3–5 ALWAYS rules most relevant to this type of output}}

**Preferred vocabulary:**
{{List of use-this / instead-of-that pairs most relevant}}

## Audience
**Segment:** {{who}}
**Journey stage:** {{awareness / consideration / decision / retention}}
**The belief to create:** "{{belief statement}}"
**Psychological lever:** {{Push / Pull / Habit / Anxiety}} — {{brief description}}
**Their language (use this):** {{verbatim phrases from customer.md}}

## The Message
**Core message (must come through):** {{one sentence}}
**Support messages:** {{2–3 bullets}}
**Proof point to lead with:** {{specific — number, quote, or named result}}
**Competitive angle:** {{how we position vs. the primary alternative}}

## Angles to Avoid
{{List — from competitive ad landscape + brand NEVER + campaign brief}}
```

---

## Ad Copywriter Brief

Append after the common header:

```markdown
---

## Your Assignment — Ad Copy

### Platform and Format Specs

{{Repeat this block for each platform/format combination}}

#### {{Platform}} — {{Format}}
| Field | Spec |
|-------|------|
| Format | {{Single image / Video / Carousel / Search / Display}} |
| Primary text / Body | {{character limit}} |
| Headline | {{character limit}} |
| Description | {{character limit, if applicable}} |
| CTA | {{Button options: Shop Now / Learn More / Sign Up / etc.}} |
| Variants needed | {{N}} |

### Variant Strategy
For each platform, deliver variants that test different angles — not just surface-level rewrites. Each variant should approach the core message from a meaningfully different hook.

**Hook angles to cover across variants:**
- {{Hook angle 1 — e.g., "Lead with the pain (Push lever) — what frustrates them about current options"}}
- {{Hook angle 2 — e.g., "Lead with the transformation (Pull lever) — what their life looks like after"}}
- {{Hook angle 3 — e.g., "Lead with proof — the specific number or result that makes skeptics believe"}}
- {{Hook angle 4 — e.g., "Lead with the campaign line — direct, bold, brand-first"}}

### Format Notes by Platform

**Meta (Facebook/Instagram):**
- Primary text reads in the feed before any "See more" truncation — front-load the hook
- Headline is the most-read element after the visual — it must earn the click
- Video copy: primary text is read while video plays — must work without sound context
- Carousel: each card has its own headline — tell a connected story or showcase multiple proof points

**Google Search:**
- Headline 1 = the hook or primary message
- Headline 2 = the proof point or differentiator
- Headline 3 = the CTA or brand qualifier
- Description = expand on the benefit, address an objection, reinforce urgency
- Pin headlines/descriptions when sequence matters

**TikTok / Reels:**
- First 3 seconds are the hook — write the hook line explicitly, not just implied
- Copy accompanies video — write for someone reading with sound OFF
- Captions feel native, not polished — conversational, direct, no corporate tone

**LinkedIn:**
- Longer primary text is accepted — use it to make the argument
- First 2 lines must hook before "See more" cuts off
- Thought leadership tone — authoritative, specific, not salesy

### Output Format

Organize output as:

```
# Ad Copy — {{Campaign Name}}

## Meta

### Variant 1 — [Hook angle name]
**Primary text:**
[copy]

**Headline:**
[copy]

**Description:**
[copy]

**CTA:** [button text]

---

### Variant 2 — [Hook angle name]
...

## Google Search

### Ad Set 1 — [Theme]
**Headline 1:** [copy] ([char count]/30)
**Headline 2:** [copy] ([char count]/30)
**Headline 3:** [copy] ([char count]/30)
**Description 1:** [copy] ([char count]/90)
**Description 2:** [copy] ([char count]/90)

---

[Additional ad sets]
```

Include the character count for every field that has a limit. Annotate which hook angle each variant uses. Do not explain the copy — let it speak for itself, but flag any variant where you made a significant creative choice worth the Creative Director's attention.
```

---

## Email Copywriter Brief

Append after the common header:

```markdown
---

## Your Assignment — Email Copy

### Sequence Overview
**Type:** {{Welcome / Nurture / Promotional / Winback / Lifecycle / Newsletter}}
**Number of emails:** {{N}}
**Platform:** {{Klaviyo / Mailchimp / etc.}}
**Audience trigger / segment:** {{what event or segment triggers this sequence}}
**Send cadence:** {{e.g., Day 0, Day 2, Day 5, Day 10}}

### Per-Email Assignments

{{Repeat this block for each email in the sequence}}

#### Email {{N}} — [Role in sequence]
| Field | Spec |
|-------|------|
| Send timing | {{Day N after trigger, or specific date}} |
| Goal | {{what this email must accomplish}} |
| Subject line | Deliver 3 options |
| Preview text | {{character limit, recommend 40–90 chars}} |
| Body length | {{short (150–300w) / medium (300–500w) / long (500–800w)}} |
| Primary CTA | {{specific action — not just "click here"}} |
| Secondary CTA | {{if applicable}} |
| Personalization tokens | {{list any tokens available — first_name, product_viewed, etc.}} |

**Email {{N}} strategic notes:**
{{Specific direction for this email — what it must accomplish, what emotional note to hit, what objection to address, what proof point to use}}

### Sequence Arc
The sequence should follow this emotional and logical progression:
{{Describe the arc — e.g., "Email 1 opens the door and makes a bold brand statement. Email 2 proves the claim with a specific customer result. Email 3 addresses the main objection. Email 4 creates urgency and asks for the conversion. Email 5 is the last-chance follow-up for non-openers."}}

### Output Format

```
# Email Sequence — {{Campaign Name}}

## Email 1 — [Role]
**Send timing:** Day 0
**Segment:** [segment]

**Subject line options:**
1. [option 1]
2. [option 2]
3. [option 3]

**Preview text:** [copy]

**Body:**
[Full email body — use line breaks naturally, as they'd appear in an email client]

**Primary CTA:** [button text] → [destination]

---

## Email 2 — [Role]
...
```

Write the full body of each email, not a description of what it should say. Annotate subject line strategy briefly (e.g., "Option 1 — curiosity gap. Option 2 — direct benefit. Option 3 — social proof.")
```

---

## Direct Response Copywriter Brief

Append after the common header:

```markdown
---

## Your Assignment — Direct Response Copy

### Page / Asset Type
**Type:** {{Landing page / Sales page / VSL script / Webinar registration page / Long-form email}}
**URL destination:** {{where this page will live}}
**Traffic source:** {{where visitors are coming from — cold paid, email list, retargeting, organic}}
**Visitor awareness level:** {{Problem-unaware / Problem-aware / Solution-aware / Product-aware / Most aware}}

### The Offer
**What we're offering:** {{specific product, service, or outcome}}
**Price / commitment:** {{cost, free trial, no credit card, etc.}}
**Guarantee / risk reversal:** {{any guarantee, return policy, or risk reduction}}
**Urgency / scarcity:** {{deadline, limited quantity, or none}}

### Page Structure

Write the following sections in order:

| Section | Goal | Length |
|---------|------|--------|
| Hero (Headline + Subheadline) | Stop the scroll. Make the promise. | Headline: 10 words max. Subheadline: 1–2 sentences. |
| Problem agitation | Make the reader feel understood. Describe their pain in their own words. | 100–200 words |
| Solution introduction | Position the offer as the natural answer. Not features — transformation. | 100–200 words |
| Proof section | Make skeptics believe. Specific evidence. | {{N}} proof points: [specify: testimonials, stats, case study, etc.] |
| Features-to-benefits bridge | Connect what it does to what they get | {{N}} key benefits — not a feature list |
| Objection handling | Address the 2–3 most common reasons someone wouldn't buy | {{List the objections from differentiation.md}} |
| Primary CTA | Ask for the conversion. Clearly. | CTA copy + supporting micro-copy |
| Secondary proof / reassurance | Last reinforcement before close | 1 testimonial or guarantee reminder |
| Final CTA | Repeat the ask. | CTA copy |

### Copy Constraints
- Do not use the brand NEVER terms (listed above)
- Proof points must be specific — never generic ("great results" → rejected; "47% lower CAC in 90 days" → accepted)
- CTA copy must be action-forward and specific — not "Submit" or "Click Here"
- Hero headline must not match the campaign line exactly — it should execute the same idea in a different form

### Output Format

```
# Landing Page Copy — {{Campaign Name}}

---

## HERO

**Headline:**
[copy]

**Subheadline:**
[copy]

**CTA (above fold):**
[button copy] / [supporting micro-copy]

---

## PROBLEM

[Full section copy]

---

## SOLUTION

[Full section copy]

---

[Continue through all sections]
```

Write full copy for every section, not placeholders or descriptions. Include notes in brackets [like this] where image, video, or design direction matters.
```

---

## Brand Storytelling Copywriter Brief

Append after the common header:

```markdown
---

## Your Assignment — Brand Story Copy

### Piece Type
**Type:** {{About page / Founder story / Brand essay / Thought leadership article / Brand manifesto / Newsletter}}
**Destination:** {{where this will live / be published}}
**Target reader:** {{who reads this — brand-new audience, existing customers, press, etc.}}
**Reading context:** {{how they'll encounter it — browsing site, email, LinkedIn, etc.}}

### The Story
**What this piece is about:** {{central topic or question the piece explores}}
**The emotional arc:** {{where the reader starts emotionally and where they end up}}
**The brand truth to reveal:** {{the authentic brand belief or origin this piece should surface}}
**Connection to the campaign:** {{how this piece fits the larger campaign narrative, if applicable}}

### Structure
| Section | Purpose | Length |
|---------|---------|--------|
| Opening | Hook. Drop the reader into a scene, a tension, or a bold statement. | 50–100 words |
| Context / backstory | Establish the why. The problem, the origin, or the moment that matters. | 200–300 words |
| The turn | The insight, decision, or belief that changed things. | 150–200 words |
| What we stand for | The brand position, stated with conviction. | 150–200 words |
| Proof / evidence | Stories, moments, specifics that make it real. Not claims. | 200–300 words |
| Close | Land on the belief. End with something that stays with the reader. | 75–100 words |

**Total target length:** {{N}} words

### Voice Notes
This piece specifically should emphasize: {{which voice traits from voice-identity.md — e.g., "storytelling and evocative" + "culturally authentic"}}
Avoid in this piece: {{any voice traits that would clash with the storytelling format}}

### Output Format

Deliver the full piece as clean, formatted prose. No section headers in the final output unless they're intentional editorial choices. Include a note at the top with the strategic intent, then the piece itself.
```

---

## SEO Copywriter Brief

Append after the common header:

```markdown
---

## Your Assignment — SEO Copy

### Target
**Primary keyword:** {{keyword}}
**Secondary keywords:** {{2–4 related terms to include naturally}}
**Search intent:** {{Informational / Navigational / Commercial / Transactional}}
**SERP competition level:** {{Low / Medium / High — from SEO audit data if available}}

### Content Specs
**Content type:** {{Blog post / Pillar page / Programmatic template / Category page / FAQ}}
**Target word count:** {{N}} words
**Target URL slug:** {{/path/to/page}}

### On-Page SEO Requirements
| Element | Requirement |
|---------|------------|
| Title tag | Primary keyword near the front, 50–60 characters |
| Meta description | Includes primary keyword, benefit-forward, 150–160 characters |
| H1 | Contains primary keyword, matches search intent |
| H2s | Cover secondary keywords and key subtopics |
| Internal links | Link to {{N}} related pages — list: {{pages}} |
| Image alt text | Describe images including keyword where natural |

### Content Structure
| Section | Purpose | Length |
|---------|---------|--------|
| Introduction | Hook + primary keyword in first 100 words. State what the reader will learn. | 100–150 words |
| {{Main section 1}} | {{topic}} | {{N}} words |
| {{Main section 2}} | {{topic}} | {{N}} words |
| {{Main section 3}} | {{topic}} | {{N}} words |
| FAQ | Answer 3–5 related questions in {{People Also Ask}} format | 200–300 words |
| Conclusion + CTA | Summarize, transition to action | 100–150 words |

### Voice Balance
SEO content still carries the brand voice — it is not generic web copy. Apply the voice rules above. The writing should be authoritative and helpful, in the brand's voice, optimized for search — not robotic keyword stuffing.

### Output Format

```
# SEO Content — {{Campaign Name or Standalone}}

## SEO Metadata
**Title tag:** [copy] ([char count]/60)
**Meta description:** [copy] ([char count]/160)
**Target URL:** /[slug]

---

## Article

### [H1]

[Introduction]

### [H2 — Section 1]

[Body]

### [H2 — Section 2]

[Body]

### Frequently Asked Questions

**[Question]**
[Answer]

**[Question]**
[Answer]

### [Conclusion H2]

[Conclusion + CTA]
```

---

## Graphic Design Agent Brief

Append after the common header:

```markdown
---

## Your Assignment — Design Direction

Your role is to produce a detailed design brief and asset specifications that any designer or design tool (including Canva and AI image generation) can execute from. You are producing direction, not the final pixels.

### Visual Identity Reference
Read `brand-intelligence-center/voice-identity.md` for the brand's visual identity section:
- Primary color: {{color}}
- Secondary color: {{color}}
- Accent color: {{color}}
- Heading font: {{font}}
- Body font: {{font}}
- Logo description: {{description}}

### Creative Direction (from Creative Concept)
**Visual direction:** {{from creative concept}}
**Tone:** {{from creative concept}}

### Asset Requirements

{{Repeat for each channel/format}}

#### {{Channel}} — {{Format Name}}
| Field | Spec |
|-------|------|
| Dimensions | {{W x H px}} |
| File format | {{JPG / PNG / MP4 / GIF}} |
| Max file size | {{size}} |
| Safe zones | {{any platform-specific safe zone requirements}} |
| Text overlay | {{yes/no — if yes, what copy goes on the asset}} |
| Quantity | {{N variants}} |

**Creative direction for this format:**
{{Specific art direction — what the image should depict, mood, composition, color treatment, model/lifestyle vs. product, etc.}}

**Copy on asset:** {{paste exact copy that goes on this asset from the ad copy brief}}

### Image Generation Prompts

For each asset, produce a detailed prompt usable in Midjourney, DALL-E, Firefly, or similar:

```
Asset: {{format name}}
Prompt: {{detailed image generation prompt — describe subject, style, lighting, composition, color, mood, aspect ratio}}
Negative prompt: {{what to exclude}}
Style reference: {{any specific style keywords}}
```

### Canva Direction

If Canva is the production tool:
- Template category: {{Social media / Presentation / Print / Custom}}
- Recommended starting template: {{describe or name if known}}
- Brand kit elements to apply: {{fonts, colors, logo}}
- Key design decisions: {{what to change from the template}}

### Design Review Criteria

Before delivering, verify:
- [ ] Brand colors applied correctly (no off-brand color usage)
- [ ] Correct fonts used (no system font substitutions)
- [ ] Logo usage follows brand guidelines (correct placement, clear space)
- [ ] Text overlay copy matches exactly what was provided
- [ ] All required format variants delivered at correct dimensions
- [ ] Visual direction from creative concept is reflected
```

---

## UX / Website Designer Brief

Append after the common header:

```markdown
---

## Your Assignment — UX Direction

Produce a detailed UX brief covering page structure, user flow, wireframe description, and UX copy recommendations. Output should be detailed enough for a developer or UX designer to build from.

### Page / Flow Type
**Type:** {{Landing page / Homepage redesign / Signup flow / Onboarding flow / Product page}}
**URL:** {{where this lives}}
**Device priority:** {{Mobile-first / Desktop-first / Equal}}
**Traffic source:** {{cold paid / email / organic / direct}}

### User Goal
**What the user wants to accomplish:** {{their goal on this page/flow}}
**What we want them to do:** {{primary conversion action}}
**Tension to resolve:** {{the gap between user goal and conversion action — how do we bridge it?}}

### Page Structure

Describe each section in order. For each:
- What the section contains
- Its job in the conversion flow
- Key UX copy (headlines, labels, microcopy)
- Any interaction or functional element

| Section | Job | Key Elements |
|---------|-----|-------------|
| Hero | First impression. Communicate value in 5 seconds. | Headline, subheadline, primary CTA, hero image/video |
| {{Section}} | {{job}} | {{elements}} |
| {{Section}} | {{job}} | {{elements}} |
| CTA / Conversion | Ask for the action. Remove final friction. | CTA button, trust signals, form (if applicable) |

### UX Copy

Provide specific copy recommendations for key UX elements:

**Page title (H1):** {{copy}}
**Primary CTA button:** {{copy}} — Note: not "Submit" or "Click here"
**Form labels:** {{list field labels}}
**Error states:** {{copy for common errors}}
**Success state:** {{copy for after conversion}}
**Trust signals:** {{what to show near the CTA — guarantee, reviews, security badge}}

### Wireframe Description

Describe the wireframe as if explaining it to a developer over the phone. Be specific about layout, hierarchy, and interaction.

**Mobile layout:**
{{Describe the mobile wireframe section by section — what's stacked, what's prioritized, what's hidden}}

**Desktop layout:**
{{Describe the desktop wireframe — column structure, sidebar vs. full-width, sticky elements}}

### CRO Hypotheses

Based on the page goal and audience, list 2–3 A/B test hypotheses worth running after launch:

1. **Hypothesis:** {{if we [change], then [metric] will [direction] because [reason]}}
2. **Hypothesis:** {{...}}
```

---

## Copy Editor Brief

Append after the common header:

```markdown
---

## Your Assignment — Copy Review

You are the final quality gate before the creative package is assembled. Review all copy outputs listed below against the brand voice rules and creative concept. You are not rewriting — you are editing for brand alignment and flagging strategic issues.

### Copy Files to Review

{{List all copy files to review with their paths}}
- `campaigns/{{slug}}/creative/copy/ad-copy.md` — Meta and Google ad variants
- `campaigns/{{slug}}/creative/copy/email-copy.md` — {{N}}-email sequence
- `campaigns/{{slug}}/creative/copy/landing-page-copy.md` — landing page

### Review Criteria

For each file, assess and edit against:

**1. Brand NEVER rules (hard failures — must fix):**
{{List NEVER rules from voice-identity.md}}

**2. Brand ALWAYS rules (required — flag if missing):**
{{List ALWAYS rules from voice-identity.md}}

**3. Vocabulary (preferred / avoided terms):**
{{List from voice-identity.md}}

**4. Creative concept alignment:**
- Does the copy reflect the campaign idea?
- Is the campaign line present or echoed in the right places?
- Is the tone calibration ("{{tone}}") consistently applied?

**5. Specificity check:**
- Flag any vague proof points ("great results," "high quality," "trusted by customers")
- Ensure the designated lead proof point appears where required

**6. CTA check:**
- Verify every execution ends with the correct CTA
- Flag any generic CTA copy ("Submit," "Click here," "Learn more" without context)

**7. Cross-piece consistency:**
- Flag vocabulary drift (the same thing called different names across pieces)
- Flag tone inconsistency (one piece significantly more formal or casual than others)
- Note overused words or phrases appearing across 3+ pieces

### Output Format

For each file:

```
## [File Name] Review

**Brand Voice Score:** Pass / Pass with notes / Revise required

**Edits Made:**
[List specific edits with before → after]

**Flags for Creative Director:**
[Any issues that require a strategic decision, not just a word change]

**Patterns across all copy:**
[Observations about consistency, overused words, tone drift — only in the final file's section]
```

Make edits directly in the copy where they are clear improvements within the brand voice. Flag (don't fix) anything that requires a strategic decision or specialist input.
```
