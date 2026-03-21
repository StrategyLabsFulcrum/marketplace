# SEO Copywriter

Writes content that ranks and converts — blog posts, pillar pages, content clusters, comparison pages, and programmatic content. Specialist agent — analyzes SERP intent, builds content architecture, and produces copy with complete on-page optimization metadata.

## What It Does

1. Loads brand voice from brand-intelligence-center
2. Reads the SEO brief from the Creative Director (or direct request)
3. Classifies search intent (informational / commercial / transactional / navigational)
4. Analyzes SERP — top results, featured snippets, People Also Ask
5. Builds content architecture before writing
6. Writes complete content with keyword integration, featured snippet targeting, and FAQ
7. Delivers with full SEO metadata block and internal link recommendations

## Content Types

| Type | Typical Length |
|------|--------------|
| Blog post (informational) | 800–2,500 words |
| Pillar page | 2,000–5,000+ words |
| Comparison / best-of | 1,500–2,500 words |
| Product / service page | 400–1,000 words |
| Location page | 400–700 words |
| Programmatic template | 300–600 words per page |
| FAQ page | 500–1,500 words |

## Output

`campaigns/{{slug}}/creative/copy/seo-[topic].md` or the appropriate content folder.

Delivered with:
- SEO metadata block (meta title, meta description, slug, keyword targets)
- Internal link recommendations with anchor text
- Schema markup recommendations for web team
- Content cluster suggestions if applicable

## Dependencies

- **brand-intelligence-center** (required) — brand voice, NEVER rules, established content authority
- **creative-director** (spawns this agent) — SEO brief with target keyword, intent, word count, internal links
