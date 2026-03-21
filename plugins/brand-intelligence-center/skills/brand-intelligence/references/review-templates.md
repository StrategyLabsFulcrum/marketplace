# Review Document Templates

Templates for the `/brand-review` command. The review document is written in plain, human-readable language — formatted for team members who are not working in Claude Code. No raw markdown code blocks, no template variable syntax in output.

---

## brand-review-{{date}}.md — Full Template

```markdown
# Brand Review — {{Business Name}}
**Prepared:** {{Month DD, YYYY}}
**Prepared for:** {{Brand Name}} Team
**Active brand:** {{brand name — or "Single brand" if founder mode}}

---

## How to Use This Document

This is a snapshot of your brand intelligence as of {{date}}. Review each section and note anything that's outdated, missing, or should be changed.

**To provide feedback:**
- Add your notes directly below any section using "FEEDBACK:" followed by your comments
- Send your annotated version back, or share in Slack/email
- Someone will run the revision workflow and confirm all changes before they go live

**What happens with your feedback:**
Every change is reviewed and confirmed before it's applied. Nothing gets overwritten without approval. A changelog tracks every revision with what changed and when.

---

## 1. Who We Are

{{Write a clean 2–4 sentence summary of the business: what it is, where it operates, how long it's been around, and what it does. Pull from business.md. Write naturally — not as a bullet list.}}

**Business type:** {{business_type}}
**How we operate:** {{format — e.g., "Dine-in, takeout, and catering" or "Online only, DTC"}}
**Our one-liner:** {{one_liner}}
**Tagline:** {{tagline}}
**Mission:** {{mission}}

**Team:**
{{List owner/key team names and roles in plain text — e.g., "Jane Smith (Owner), Mark Chen (Operations Manager)"}}

**FEEDBACK:**
*(Add any corrections or updates here)*

---

## 2. Our Customer

**Who they are:**
{{Write 2–3 sentences describing the primary customer in human terms. Who are they? What's their life like? Why do they come to us? Pull from customer.md.}}

**Secondary audiences:** {{secondary_audiences — or "Not defined yet"}}

**When they come to us:**
{{List primary occasions in plain English — e.g., "Casual weeknight dinners, weekend date nights, and business lunches."}}

**What they're really hiring us to do** (Jobs to Be Done):
{{List 2–3 JTBD statements in plain language — e.g., "Give me a reliable spot I can bring people to and look good" or "Make it easy to enjoy a great meal without overthinking it."}}

**Why they switch to us** (what frustrates them about alternatives):
{{Pull Push force from customer.md — 1–2 sentences}}

**What might hold them back:**
{{Pull Anxiety force from customer.md — 1–2 sentences}}

**Words our customers actually use to describe us:**
{{List 2–3 verbatim quotes or phrases from customer.md}}

**FEEDBACK:**
*(Does this still accurately describe our customer? Any new segments, occasions, or language to add?)*

---

## 3. Why Customers Choose Us

**What makes us different:**
{{Write 2–3 sentences on the key differentiator. Not a list of features — the real reason customers choose you over alternatives. Pull from differentiation.md.}}

**Why that matters to customers:**
{{1–2 sentences on the customer benefit of the differentiator}}

**Our competitive landscape:**

{{For each competitor in differentiation.md, write a 1–2 line plain-English summary:}}
- **{{Competitor Name}}** — {{their positioning and where they fall short vs. us}}
- **{{Competitor Name}}** — {{their positioning and where they fall short vs. us}}

**Common objections and how we address them:**
{{List 2–3 objections with responses in plain English}}

**Who we're NOT a good fit for:**
{{Anti-persona in plain language}}

**FEEDBACK:**
*(Any new competitors to add? Changes to our positioning? Objections we're hearing more often?)*

---

## 4. Our Brand Voice

**Our personality:**
{{Write 1–2 sentences describing the brand personality as if describing a person — e.g., "We're warm and direct — like a knowledgeable friend who tells you what you actually need to know, not what sounds impressive."}}

**Voice traits in practice:**

| When we write... | We sound like... |
|-----------------|-----------------|
| {{trait}} | {{what it looks like in practice}} |
| {{trait}} | {{what it looks like in practice}} |

**We always:**
{{List the ALWAYS rules in plain English — written as statements about the brand, not instructions to an AI. E.g., "Every piece of content feels like it came from a real person, not a corporation."}}

**We never:**
{{List the NEVER rules in plain English}}

**Preferred vocabulary:**

| We say... | Instead of... |
|-----------|--------------|
| {{preferred}} | {{avoided}} |

**Visual identity:**
- Primary color: {{primary_color or "Not yet defined"}}
- Secondary color: {{secondary_color or "Not yet defined"}}
- Fonts: {{fonts or "Not yet defined"}}

**FEEDBACK:**
*(Does the voice still feel right? Any new vocabulary rules? Anything that's changed visually?)*

---

## 5. Our Proof Points

**Ratings and reviews:**
{{Star rating, review count, platforms — written naturally: e.g., "4.7 stars across 340 Google reviews"}}

**Years in business:** {{years}}

**Recognition and press:**
{{List any awards, press mentions, or notable accolades in plain language}}

**Key numbers we're proud of:**
{{Any metrics, milestones, or proof points from proof-goals.md}}

**Testimonials:**
{{List 1–3 customer quotes that capture what the brand is about}}

**What we want people to do** (primary conversion goal):
{{Primary CTA in plain language — e.g., "Make a reservation" or "Start a free trial"}}

**What we're focused on right now:**
{{Current business focus in plain language — e.g., "Growing catering revenue" or "Acquiring new customers in the Boston market"}}

**FEEDBACK:**
*(Any new proof points to add? Outdated numbers to update? Has the business focus shifted?)*

---

## 6. Our Digital Presence

**Website:** {{website_url}}

**Social media:**
{{List each active platform with its URL and posting frequency — written as a simple list}}

**How customers book/order:**
{{Reservation platforms, ordering systems, etc.}}

**Marketing tools we use:**
- Email/SMS: {{platform or "Not set up"}}
- Analytics: {{platform or "Not set up"}}
- CRM/Loyalty: {{platform or "None"}}
- POS: {{platform or "Not specified"}}

**FEEDBACK:**
*(Any new platforms? Changed posting cadence? New tools added to the stack?)*

---

## 7. Financial Context
{{If financial.md is complete:}}

*Note: Financial details are shared only with team members who need this context.*

**Revenue range:** {{range}}
**Primary revenue streams:** {{list}}
**Growth trend:** {{trend}}
**Current financial focus:** {{goals}}

{{If financial.md is incomplete or skipped:}}
*Financial context has not been set up. Run `/brand-update` to add this information.*

**FEEDBACK:**
*(Any updates to revenue, new streams, or changed financial priorities?)*

---

## 8. What's Changed Since Last Review

{{If changelog.md exists:}}

The following areas have been updated since the previous brand review:

{{List each change from changelog.md since the last review document date:}}
- **{{Date}}** — {{Area}}: {{brief description of what changed}}

{{If no changelog exists or no previous review:}}
*This is the first brand review. Future reviews will show a change history here.*

---

## Summary: Areas That Need Attention

{{Automatically identify and list:}}
- Areas marked as [Not yet completed] in any file
- Areas that haven't been updated in 90+ days (per changelog)
- Fields with placeholder or minimal content

{{If everything is complete:}}
All 8 areas are complete and up to date. No gaps identified.

---

## Team Notes

*Use this section to add general feedback, questions, or notes that don't fit a specific section.*

**From {{team member name}}:**
*(Add notes here)*

**From {{team member name}}:**
*(Add notes here)*

---

*Generated by Brand Intelligence Center on {{date}}.*
*To apply revisions from this document, run `/brand-revise`.*
*To sync updated brand files with your team, run `/brand-sync push`.*
```

---

## Formatting Rules for Review Generation

When generating the review document, apply these rules:

1. **Write in third person about the brand** — "The brand" or the brand name, not "you"
2. **No raw markdown syntax visible in the document** — headings use `#` but no `{{template}}` variables, no code blocks, no frontmatter
3. **Preserve actual field values** — do not paraphrase or editorialize brand content; render it as written in the area files
4. **For missing fields** — write "Not yet defined" or "Not yet completed" rather than leaving blank
5. **For the JTBD and ALWAYS/NEVER lists** — write as complete sentences, not raw bullet fragments
6. **Quotes from customer.md** — preserve verbatim, in quotation marks
7. **Competitor table** — write each competitor as a human-readable sentence, not a table of raw fields
8. **Tone of the review document itself** — professional and neutral. This is a reference document, not content.

---

## Changelog Entry Format

```markdown
## {{YYYY-MM-DD}} — {{N}} change(s) applied

**Revised by:** {{team_member name from config, or "Team"}}
**Source:** {{"/brand-revise" | "brand-review feedback" | "setup update"}}
**Areas updated:** {{comma-separated list}}

### Changes

**{{Area Name}} — {{Field Name}}**
- Before: {{previous value, or "New field — no previous value"}}
- After: {{new value}}

**{{Area Name}} — {{Field Name}}**
- Before: {{previous value}}
- After: {{new value}}

---
```
