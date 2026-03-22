# /asset-setup

Set up a brand asset library from scratch. This wizard creates your folder structure first — before any assets exist — then guides you through loading, analyzing, and organizing your assets with a full approval gate before anything is moved or copied.

Run this once when starting a new brand asset library. Use `/add-assets` for all ongoing additions afterward.

## How to Invoke

```
/asset-setup
```

---

## What Happens

### Phase 1: Brand Context Interview

The wizard starts by understanding your brand so the folder structure fits how you actually shoot and publish content.

**If a `brand-knowledge-center/` folder exists**, reads brand context automatically and confirms:
- Brand name and product types
- Active publishing channels
- Content types you produce
- Product lines or collections

**If no brand knowledge exists**, asks:
1. What does your brand sell? (product types, categories)
2. What channels do you publish on? (Instagram, TikTok, website, Meta Ads, email, YouTube, etc.)
3. What types of content do you typically create? (product photos, lifestyle, BTS, UGC, campaigns, events, etc.)
4. Do you have distinct product lines or collections that should get their own subfolders?
5. What are your brand colors? (for color-match notes in descriptions)

---

### Phase 2: Propose Folder Structure

Based on brand context, the wizard proposes a tailored folder structure. Presents it as a visual tree:

```
brand-assets/
├── asset-manifest.csv
├── asset-manifest.md
├── _inbox/                     ← Drop new assets here for ongoing review
├── _duplicates/                ← Flagged duplicates for review
├── product-photography/
│   ├── flat-lay/
│   ├── on-model/
│   ├── detail-shots/
│   └── lifestyle-product/
├── lifestyle/
│   ├── outdoor/
│   └── seasonal/
├── team-behind-the-scenes/
├── ugc-community/
├── campaigns/
│   ├── seasonal/
│   └── launches/
├── logos-brand-marks/
│   ├── primary/
│   ├── secondary/
│   └── icons/
└── video/
    ├── product/
    ├── lifestyle/
    ├── social-clips/
    └── thumbnails/
```

Always includes `_inbox/` and `_duplicates/` regardless of customization.

**Customization prompt:**

> "Does this folder structure work for your brand? You can:
> - Add product line subfolders (e.g., `product-photography/hoodies/`)
> - Add campaign subfolders (e.g., `campaigns/summer-2026/`)
> - Rename any folder
> - Remove folders you won't use
> - Add channel-specific folders (e.g., `video/reels/`, `email-headers/`)
>
> Reply with any changes, or say **'approved'** to create this structure."

Apply all requested edits, show the revised structure, and confirm once more before proceeding.

---

### Phase 2.5: File Handling Mode

Before building the structure, establish how approved assets should be handled:

> "When I organize and rename your assets, what should happen to the original files?"
>
> **Option A — Duplicate (non-destructive, recommended)**
> - A renamed, organized copy goes into `brand-assets/[category]/` with the new descriptive name and embedded metadata
> - The original file stays exactly where it is — in `_inbox/`, on your drive, or wherever it came from — with its original name, untouched
> - Best for: users who want to preserve originals as a backup, or who pull from a camera card or external drive they'll reformat later
>
> **Option B — Move and rename**
> - The file is moved directly from its source location into `brand-assets/[category]/` with the new descriptive name
> - The source location no longer has the file after processing — `_inbox/` is cleared, source folders are emptied of approved files
> - Best for: users who want a single clean organized copy with no duplicates taking up storage
>
> Note: Files marked **Skip** are always left in their source location regardless of this setting. Files marked **Delete** are always moved to `brand-assets/_delete/` — never permanently deleted.

Save choice to `brand-assets/asset-config.md`:

```markdown
# Brand Asset Manager — Config

## File Handling Mode
- Mode: duplicate | move
- Description: [Originals preserved in source location / Originals moved to organized library]
- Set during: /asset-setup on [date]
```

This setting applies to all future `/add-assets` and `/organize-assets` sessions. It can be changed anytime by editing `brand-assets/asset-config.md` directly or saying "change my file handling mode."

---

### Phase 3: Create Folder Structure

**Only after explicit approval**, create the full folder structure in the user's working directory.

For each folder in the approved structure:
1. Create the directory
2. Add a `.keep` file so empty folders are tracked in git

Create a `brand-assets/README.md` that documents the structure:

```markdown
# Brand Asset Library

Created: [date]
Brand: [brand name]

## Folder Guide

| Folder | What goes here |
|--------|---------------|
| _inbox/ | Drop new unorganized assets here for review |
| _duplicates/ | Flagged duplicate files — review before deleting |
| product-photography/ | All product shots |
| lifestyle/ | Lifestyle and environmental content |
| team-behind-the-scenes/ | Team, workspace, and BTS content |
| ugc-community/ | User-generated and community content |
| campaigns/ | Campaign-specific assets by name/season |
| logos-brand-marks/ | Logo files and brand marks |
| video/ | All video content |

## How to Add New Assets

1. Drop files into `brand-assets/_inbox/`
2. Run `/add-assets` — Claude will analyze, organize, rename, and tag them
3. Review the manifest at `brand-assets/asset-manifest.md`

## File Naming Convention

`{category}-{subject}-{detail}-{sequence}.{ext}`

Examples:
- `lifestyle-flannel-mountain-trail-01.jpg`
- `product-flatlay-hoodie-navy-01.jpg`
- `video-lifestyle-fall-lookbook-01.mp4`
```

Confirm when folders are created:

> "✓ Folder structure created at `brand-assets/`. Here's what was built:
> [list of folders created]
>
> The `_inbox/` folder is your ongoing drop zone — add any new assets there and run `/add-assets` to organize them."

---

### Phase 4: Load Initial Assets

Ask how the user wants to load their existing unorganized assets:

> "Great — your library structure is ready. How would you like to load your existing assets?
>
> **Option A — Drop into inbox:** Move or copy your existing photos and videos into `brand-assets/_inbox/`, then run `/add-assets` to have them analyzed and organized.
>
> **Option B — Point to a folder:** Tell me the path to a folder of unorganized assets and I'll scan, analyze, and propose organization for them now.
>
> **Option C — Start fresh:** The structure is ready. Add assets to `_inbox/` whenever you're ready and use `/add-assets` to process them.
>
> Which option works best?"

**If Option B**, proceed directly into the full analysis workflow (same as `/organize-assets` starting at Step 3). The folder structure is already built — skip Steps 1 and 2.

**If Option A or C**, close the wizard:

> "Your asset library is ready. Whenever you have photos or videos to organize:
> 1. Drop them into `brand-assets/_inbox/`
> 2. Run `/add-assets`
>
> That's it — I'll handle analysis, naming, tagging, and cataloging."

---

## Outputs

| File / Folder | Created when |
|---------------|-------------|
| `brand-assets/` + all subfolders | Phase 3 (after approval) |
| `brand-assets/README.md` | Phase 3 |
| `brand-assets/_inbox/` | Phase 3 (always) |
| `brand-assets/asset-config.md` | Phase 3 (stores file handling mode preference) |
| `brand-assets/asset-manifest.csv` | After first asset batch is processed |
| `brand-assets/asset-manifest.md` | After first asset batch is processed |

---

## After Setup

Once the library is built, the ongoing workflow is:

```
New assets → drop in brand-assets/_inbox/ → run /add-assets → review + approve → organized
```
