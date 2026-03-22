# Brand Asset Manager

Set up a structured brand asset library, organize existing photos and videos, and manage an ongoing inbox-based workflow for adding new assets. Built by Strategy Labs.

---

## What It Does

- **Setup wizard** — Builds a custom folder structure before any assets exist, tailored to your brand's products, channels, and content types
- **Smart analysis** — Reads every photo and video and writes a full description covering subject, mood, shot type, lighting, seasonality, and channel fit
- **Approval gate** — Presents the full organization plan for review before copying or renaming anything
- **Descriptive renaming** — `IMG_4392.jpg` becomes `lifestyle-flannel-mountain-trail-01.jpg`
- **Searchable manifest** — CSV and markdown index so you can find any asset by keyword, mood, season, channel, or product
- **Duplicate detection** — Exact and near-duplicate files are flagged before you waste storage
- **Inbox workflow** — Drop new assets into `_inbox/` and run `/add-assets` — Claude handles the rest

---

## Commands

| Command | When to Use |
|---------|-------------|
| `/asset-setup` | Starting from scratch — builds folder structure first, then guides asset loading |
| `/organize-assets` | Have an existing messy folder of assets to organize for the first time |
| `/add-assets` | Ongoing — add new photos/videos from `_inbox/` or a folder to an existing library |
| `/import-from-photos` | Pull photos/videos directly from Apple Photos into `_inbox/` by album, date, keyword, person, or favorites |

---

## Getting Started

### New brand (no library yet)

1. Run `/asset-setup`
2. Answer a few questions about your brand (or it reads Brand Knowledge Center automatically)
3. Review and approve the proposed folder structure
4. Folders are created — including a permanent `_inbox/` drop zone
5. Drop existing assets into `_inbox/` and run `/add-assets`, or point to an existing folder

### Have existing unorganized assets

1. Run `/organize-assets`
2. Provide brand context (or reads Brand Knowledge Center)
3. Review and approve the proposed folder structure and organization plan
4. Assets are copied (originals untouched) into the organized structure with new names

### Adding new assets (ongoing)

```
New photos/videos from a shoot
      ↓
Option A: Drop files into brand-assets/_inbox/
Option B: Run /import-from-photos to pull from Apple Photos
      ↓
/add-assets             ← run this
      ↓
Choose batch size → HTML review page → approve → organized + tagged
```

### Importing from Apple Photos

```
/import-from-photos album "Spring Campaign"   ← by album
/import-from-photos recent 14                 ← last 14 days
/import-from-photos favorites                 ← all favorited photos
/import-from-photos keyword "product"         ← by keyword/tag
```

Requires `osxphotos`: `pip3 install osxphotos`

---

## Folder Structure

```
brand-assets/
├── asset-manifest.csv          ← searchable spreadsheet of all assets
├── asset-manifest.md           ← human-readable index with full descriptions
├── README.md                   ← library guide
├── _inbox/                     ← drop new assets here for processing
├── _duplicates/                ← flagged duplicate files + review log
│   └── flagged-duplicates.md
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
│   └── [season or campaign name]/
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

Folder structure is customized per brand. Product lines, channel-specific folders, and campaign subfolders are added based on your brand context.

---

## How the Approval Gate Works

No files are ever copied, moved, or renamed without your explicit approval.

1. Claude analyzes all assets and builds the full organization plan
2. A complete summary is presented: folder assignments, naming examples, duplicate groups, quality breakdown
3. You type **"approve"** (or request changes first)
4. Only then does Claude execute — copying files, updating the manifest, clearing the inbox

If you cancel before approving, all source files remain exactly where they were.

---

## Integration

Works best with the **Brand Knowledge Center** plugin. If a `brand-knowledge-center/` folder exists, the Asset Manager automatically reads your brand identity, products, channels, and content pillars to make smarter categorization and channel suggestions.

---

## Tips

- **Run Brand Knowledge Center first** — brand context makes categorization and descriptions significantly more accurate
- **Use `_inbox/` consistently** — it's the permanent drop zone; always drop new content there before running `/add-assets`
- **Original files are never modified** — copies are created in the organized structure; your source files are untouched
- **Search the manifest** — open `asset-manifest.md` and search for "Instagram", "fall", "flannel", or any keyword to find assets instantly
- **Review duplicates promptly** — check `_duplicates/flagged-duplicates.md` after each run
