# Brand Asset Manager

Organize, rename, describe, and catalog your brand's photos and videos into a searchable, categorized library. Built by Strategy Labs.

## What It Does

The Brand Asset Manager takes a messy folder of photos and videos and turns it into a structured, searchable asset library with:

- **Smart categorization** — Assets sorted into folders based on your brand's products, channels, and content types
- **Descriptive renaming** — `IMG_4392.jpg` becomes `lifestyle-flannel-mountain-trail-01.jpg`
- **Rich descriptions** — Every asset gets a detailed description covering subject, mood, shot type, lighting, and more
- **Channel suggestions** — Each asset is tagged with recommended platforms (Instagram, Meta Ads, Shopify, Email, etc.)
- **Duplicate detection** — Exact and near-duplicate photos/videos are flagged before you waste storage
- **Video thumbnails** — Key frames identified as thumbnail candidates for each video
- **Searchable manifest** — A CSV and markdown index so you can find any asset by keyword, mood, season, channel, or product

## Commands

| Command | Description |
|---------|-------------|
| `/organize-assets` | Set up a new asset library from scratch — full wizard with brand context, folder structure, and batch processing |
| `/add-assets` | Add new photos/videos to an existing library with duplicate checking |

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **Run `/organize-assets`**
3. **Provide brand context** — If you've already set up a Brand Knowledge Center, it loads automatically. Otherwise, answer a few quick questions.
4. **Confirm folder structure** — Review and customize the proposed categories
5. **Point to your assets** — Provide a folder path or upload files
6. **Review results** — Check the manifest, flagged duplicates, and organized folders

## Output Structure

```
brand-assets/
├── asset-manifest.csv          # Searchable spreadsheet of all assets
├── asset-manifest.md           # Human-readable index with descriptions
├── _duplicates/                # Flagged duplicate files + review log
├── product-photography/        # Product shots (flat lay, on-model, detail)
├── lifestyle/                  # Lifestyle and environmental shots
├── team-behind-the-scenes/     # Team, workspace, BTS content
├── ugc-community/              # User-generated content
├── campaigns/                  # Seasonal and launch campaign assets
├── logos-brand-marks/          # Logo files and brand marks
└── video/                      # Video files + generated thumbnails
```

Folder structure is customized per brand based on products, channels, and content types.

## Integration

Works best with the **Brand Knowledge Center** plugin. If a `brand-knowledge-center/` folder exists, the Asset Manager automatically reads your brand identity, products, channels, and content pillars to make smarter categorization and channel suggestions.

## Tips

- **Run Brand Knowledge Center first** for the best results — brand context makes categorization and descriptions significantly more accurate
- **Use the manifest to search** — Open `asset-manifest.md` and search for "Instagram", "fall", "flannel", or any keyword
- **Review duplicates promptly** — Check `_duplicates/flagged-duplicates.md` after each run
- **Add assets incrementally** — Use `/add-assets` as you create new content rather than re-running the full organizer
- **Original files are never modified** — The plugin always copies, never moves or renames your source files
