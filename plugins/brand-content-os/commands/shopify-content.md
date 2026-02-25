---
description: Generate Shopify product pages, collection pages, and blog posts using brand knowledge
allowed-tools: Read, Write, Glob, Grep, AskUserQuestion
argument-hint: "<product name or content type>"
---

# Shopify Content — Product Pages, Collections & Blog

Generate on-brand Shopify content including product page copy, collection page introductions, and SEO-optimized blog posts. Automatically applies brand knowledge and platform best practices.

## Before Generating

1. **Load brand knowledge**: Read all files from the `brand-os/` directory. If missing, suggest running `/brand-setup` first.
2. **Load the system prompt**: Read `brand-os/system-prompt.md` as foundational context.
3. **Load references**:
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/platform-prompts.md` (Shopify section)
   - `${CLAUDE_PLUGIN_ROOT}/skills/brand-os/references/best-practices.md` (Shopify section)

## Gather Inputs

Ask the user what they need:

1. **Content type**:
   - Full Product Page (short desc + long desc + specs + brand recommendation + SEO meta)
   - Collection Page Introduction
   - Blog Post (800+ words, educational, with product integration)

2. **Product or collection name** (Use `$ARGUMENTS` if provided.)

3. **Additional context** (varies by type):
   - Product Page: Key features, specs, what problem it solves, compatible models/categories
   - Collection Page: What segment this collection serves, key products in it
   - Blog Post: Topic angle, which content pillar it falls under, products to feature

## Generation Process

1. Select the appropriate prompt template from platform-prompts reference
2. Populate auto-variables from brand knowledge
3. Check for segment-specific messaging in `brand-os/key-messages.md` — if the product falls into a defined segment, apply that segment's RTB and vocabulary
4. Generate content following brand voice rules
5. NEVER list check
6. Quality filter check
7. For product pages: Verify the Brand Recommendation section is included
8. For blogs: Verify 800+ word count and content pillar alignment
9. Generate SEO meta (title tag + meta description) for all web content

## Output Format

### Product Page:

```
## Product Page — [Product Name]

### Short Description (above fold)
[1-2 sentence brand-promise summary]

### Long Description
[Full product description — experience first, specs second]

### Spec Bullets
- [Benefit] — [Spec detail]
- [Benefit] — [Spec detail]
- [Benefit] — [Spec detail]

### Brand Recommendation
[Why the brand carries this — expert POV]

### SEO Meta
- **Title**: [max 60 chars]
- **Meta Description**: [max 155 chars]
- **Suggested Alt Text**: [for hero image]

---
**Brand Voice Check**: ✓ No NEVER list violations | ✓ Quality filter passed
```

### Collection Page:

```
## Collection Page — [Collection Name]

[2-3 paragraph introduction]

### SEO Meta
- **Title**: [max 60 chars]
- **Meta Description**: [max 155 chars]

---
**Brand Voice Check**: ✓ No NEVER list violations
```

### Blog Post:

```
## Blog — [Title]
**Content Pillar**: [Which pillar this aligns to]
**Word Count**: [X] words

[Full blog post with headings, brand recommendation section, product links]

### SEO Meta
- **Title**: [max 60 chars]
- **Meta Description**: [max 155 chars]
- **Primary Keyword**: [suggested keyword]
- **Internal Links**: [suggested product/collection links]

---
**Brand Voice Check**: ✓ No NEVER list violations | ✓ Quality filter passed
```

## Follow-Up

After presenting:
- For product pages: Offer to generate matching collection page intro or blog post
- For blogs: Offer to create matching social content or email using `/content-multiply`
- Offer to generate for another product or collection
