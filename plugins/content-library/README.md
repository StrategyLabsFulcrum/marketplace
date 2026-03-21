# Content Library

The indexed backlog of all approved marketing copy and the searchable catalogue of brand visual assets. The retrieval layer for the entire creative system.

**The golden rule: create nothing that already exists.** Before any copywriter writes new ad copy, before any designer sources photography, the Content Library is checked first. Reusing approved, proven content is faster and consistently better than starting from scratch.

---

## Two Functions

### 1. Copy Library

An organized backlog of all approved marketing copy — ad copy, email sequences, landing page copy, social captions, brand storytelling, and SEO content — indexed by type, channel, campaign, and status.

**The copy index lives at:** `content-library/copy/index.md`

Each entry includes a preview of the copy, full file path, approval status, and searchable tags. Performance tags are added after campaigns run to identify what has proven results.

### 2. Asset Library

A searchable catalogue of all brand visual assets — photography, video, graphics, illustrations, logos — integrated with the brand-asset-manager plugin. The Content Library does not store the asset files; it maintains the metadata that makes them findable.

**The asset index lives at:** `content-library/assets/index.md`

Each entry includes a natural-language description (for semantic search), license terms, model release status, channel approval, and tags.

---

## Slash Commands

| Command | Use |
|---------|-----|
| `/content-find` | Search by type, channel, campaign, tag, or keyword |
| `/content-store` | Add approved copy or asset references to the library |
| `/content-browse` | View the full library, a category, or run a maintenance audit |

---

## Copy Library Structure

```
content-library/copy/
├── index.md                     ← master searchable index
├── ad-copy/
│   ├── meta/
│   ├── google/
│   ├── tiktok/
│   ├── linkedin/
│   └── evergreen/
├── email-copy/
│   ├── welcome-series/
│   ├── promotional/
│   ├── abandoned-cart/
│   ├── nurture/
│   └── evergreen/
├── landing-pages/
│   ├── [campaign-slug]/
│   └── evergreen/
├── social-copy/
│   ├── organic/
│   └── captions/
├── brand-copy/
│   ├── about-page.md
│   ├── manifesto.md
│   └── [other permanent brand copy]
└── seo-content/
    └── [topic].md
```

---

## Asset Library Structure

```
content-library/assets/
└── index.md                     ← master asset catalogue
```

Asset files are stored and managed by brand-asset-manager in `brand-assets/`. The Content Library only maintains the searchable index.

---

## How It Fits in the Workflow

```
Campaign Strategist → Campaign Brief
        ↓
[Content Library checked first]
        ↓
Found? → Deliver existing copy/assets
Not found? → Brief specialist agents (Ad Copy, Email Copy, Graphic Design, etc.)
        ↓
New copy approved → /content-store to add to library
New assets approved → /content-store asset to catalogue
        ↓
Campaign runs → /content-store performance-update to tag results
```

---

## Performance Tagging

After campaigns complete, return to the copy index and add performance tags:

- `high-performer` — above benchmark CTR/CVR
- `top-variant` — won A/B test
- `fatigued` — high frequency; do not reuse without refresh
- `tested-[date]` — confirms the copy has campaign history

Performance-tagged copy is the most valuable in the library. It has proof of what works.

---

## First-Time Setup

If the library is being built for the first time, use the Content Library skill in `build` mode:

1. Crawl all `campaigns/` folders for existing copy outputs
2. Crawl `brand-assets/` for existing asset files
3. Create index entries for each found item with best-effort tagging
4. Flag all items as 🔄 In review until human confirmation of approval status
5. Present the draft index for review before marking items ✅ Approved

---

## Integration with Brand Asset Manager

The brand-asset-manager plugin manages asset files. The Content Library adds the discovery layer:

- brand-asset-manager: file storage, versioning, delivery
- content-library: metadata, search index, license tracking, model release tracking, channel approval

When assets are added to brand-asset-manager, they should also be catalogued in the Content Library's asset index for full searchability across the creative system.
