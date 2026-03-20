---
name: asset-manager
description: >
  Brand Asset Manager for organizing, cataloging, and describing brand photos and videos.
  Use when the user mentions "organize assets", "brand photos", "brand videos", "asset library",
  "photo organization", "image catalog", "content library", "asset management", "organize images",
  "rename photos", "tag assets", "find photos", "search assets", "duplicate photos",
  or wants to build a structured, searchable library of brand visual content.
version: 1.0.0
---

# Brand Asset Manager

A framework for organizing brand photos and videos into a searchable, categorized folder structure with descriptive file names, rich metadata, channel usage suggestions, and duplicate detection.

## How It Works

The Brand Asset Manager has three layers:

1. **Brand Context Layer** — Reads brand knowledge files to understand the brand's products, audience, channels, and visual identity. This informs how assets are categorized and described.
2. **Organization Layer** — Scans source assets, analyzes each image/video, categorizes them into subfolders, renames them descriptively, and generates metadata.
3. **Manifest Layer** — Maintains a searchable index of all assets with descriptions, tags, categories, channel suggestions, and duplicate flags.

## Brand Context Integration

Before organizing assets, check for a `brand-knowledge-center/` folder in the user's working directory.

### If brand knowledge exists:
1. Read `brand-identity.md` — for brand pillars, visual identity, product lines
2. Read `audience-messaging.md` — for audience segments, content pillars, channel strategy
3. Read `digital-ecosystem.md` — for active platforms and channels
4. Read `competitive-landscape.md` — for positioning context
5. Use this context to inform category suggestions, channel recommendations, and asset descriptions

### If brand knowledge does NOT exist:
Ask the user:
1. What does your brand sell? (product types)
2. What channels do you post content on? (Instagram, Facebook, email, website, ads, etc.)
3. What types of content do you typically shoot? (product photos, lifestyle, behind-the-scenes, events, etc.)
4. Any specific product lines or collections to organize around?

## Folder Structure

All organized assets live in a `brand-assets/` master folder. The plugin creates categorized subfolders based on brand context and user input.

### Default Structure (customized per brand)

```
brand-assets/
├── asset-manifest.csv
├── asset-manifest.md
├── _duplicates/
│   └── flagged-duplicates.md
├── product-photography/
│   ├── flat-lay/
│   ├── on-model/
│   ├── detail-shots/
│   └── lifestyle-product/
├── lifestyle/
│   ├── outdoor/
│   ├── urban/
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

### Folder Generation Rules

1. **Start with defaults** based on brand context, then ask the user to confirm, edit, add, or remove categories
2. **Product-specific subfolders** — if the brand has distinct product lines (e.g., flannels, hoodies, beanies), offer to create subfolders within `product-photography/` for each
3. **Channel-specific subfolders** — if the brand is active on specific platforms, offer folders like `social-clips/instagram-reels/` or `email-headers/`
4. **Depth limit** — no more than 3 levels deep to keep things navigable
5. **Empty folders are OK** — create the structure even if no assets fill it yet; it guides future shoots

## Asset Analysis

When processing each asset, analyze and extract the following:

### Photo Analysis

For each image file (.jpg, .jpeg, .png, .webp, .heic, .tiff):

1. **Subject identification** — What's in the photo? (product, person, location, object, flat lay, etc.)
2. **Product recognition** — If brand products are visible, identify them by name/type if possible
3. **Shot type** — Close-up, mid-range, wide, flat lay, overhead, lifestyle, candid, posed
4. **Setting/location** — Studio, outdoor, indoor, urban, nature, PNW-specific landmarks
5. **Mood/tone** — Adventurous, cozy, energetic, minimal, bold, warm, rugged
6. **Lighting** — Natural, studio, golden hour, overcast, dramatic
7. **Composition quality** — Is this usable for marketing? Flag low-quality, blurry, or poorly lit images
8. **Color palette** — Dominant colors, does it align with brand colors?
9. **People** — Are people present? How many? Approximate age range, activity
10. **Seasonality** — Does this feel seasonal? (fall, winter, summer, spring)

### Video Analysis

For each video file (.mp4, .mov, .avi, .mkv, .webm):

1. **Duration** — Length of the video
2. **Content summary** — What happens in the video? Describe key scenes
3. **Subjects** — Products, people, locations featured
4. **Shot types** — Static, handheld, drone, slow-motion, timelapse
5. **Audio** — Music, voiceover, natural sound, silent
6. **Mood/tone** — Same as photos
7. **Thumbnail candidates** — Identify 2-3 strong frames as potential thumbnails
8. **Platform fit** — Aspect ratio and length suggest which platforms (Reels = vertical + <90s, YouTube = horizontal + longer)

### Photo Description Format

```
**File:** lifestyle-flannel-mountain-trail-01.jpg
**Category:** lifestyle/outdoor
**Description:** A man in his 30s wearing a rust-colored flannel, hiking a mossy Pacific Northwest trail. Morning fog visible in the background, natural lighting filtering through tall evergreens.
**Shot Type:** Mid-range, candid
**Mood:** Adventurous, authentic, rugged
**Lighting:** Natural, overcast/fog
**Seasonality:** Fall
**Tags:** flannel, hiking, PNW, outdoor, forest, fog, fall, men, trail
**Suggested Use:** Instagram feed, Meta Ads (lifestyle), Website hero banner
**Quality:** High — sharp focus, strong composition, on-brand
```

### Video Description Format

```
**File:** fall-collection-lookbook-01.mp4
**Category:** video/lifestyle
**Duration:** 45 seconds
**Aspect Ratio:** 16:9 (horizontal)
**Description:** Lifestyle reel showing three models wearing Fall 2025 collection pieces (flannel, hoodie, beanie) across PNW locations: coffee shop interior, forest trail, waterfront dock. Upbeat acoustic soundtrack. Cuts between locations with smooth transitions.
**Scenes:** 0:00-0:15 coffee shop (warm, cozy), 0:15-0:30 forest trail (adventurous), 0:30-0:45 waterfront (reflective, golden hour)
**Mood:** Warm, community, seasonal
**Audio:** Acoustic music, no voiceover
**Tags:** fall, collection, lookbook, flannel, hoodie, beanie, PNW, coffee, forest, waterfront
**Suggested Use:** YouTube, Facebook feed, Website collection page
**Thumbnails:** Frame at 0:12 (flannel collar close-up, mountain backdrop), Frame at 0:38 (waterfront golden hour wide shot)
**Quality:** High — professional grade, strong color grading, on-brand
```

## File Naming Convention

### Naming Rules

Original files are never modified. Duplicates are created in the organized structure with new names.

**Pattern:** `{category}-{subject}-{detail}-{sequence}.{ext}`

**Examples:**
| Original | Renamed |
|----------|---------|
| IMG_4392.jpg | lifestyle-flannel-mountain-trail-01.jpg |
| DSC_0012.jpg | product-flatlay-workman-flannel-charcoal-01.jpg |
| MVI_8834.mp4 | video-lifestyle-fall-lookbook-01.mp4 |
| Screenshot 2024-03-12.png | brand-mark-primary-logo-dark-01.png |

**Naming rules:**
1. All lowercase, hyphens between words
2. No spaces, underscores, or special characters
3. Category prefix matches the folder it lives in
4. Subject describes what's in the asset
5. Detail adds specificity (product name, color, location)
6. Two-digit sequence number at the end (01, 02, 03...)
7. Preserve original file extension
8. Maximum 60 characters for the filename (excluding extension)

## Duplicate Detection

### How Duplicates Are Flagged

The plugin checks for duplicates at two levels:

**Level 1: Exact duplicates**
- Same file size AND same dimensions = likely exact duplicate
- Flag and move to `_duplicates/` folder
- Keep the higher-quality version in the main structure

**Level 2: Near duplicates**
- Same subject, very similar composition, same shoot session
- Example: 5 photos of the same flannel flat lay with minor angle changes
- Flag as "near duplicates" in the manifest
- Keep the best one in the main folder, move others to `_duplicates/`
- Log all near duplicates in `_duplicates/flagged-duplicates.md` with side-by-side descriptions so the user can review

### Flagged Duplicates Log Format

```markdown
## Duplicate Group 1: Workman Flannel Flat Lay
**Kept:** product-flatlay-workman-flannel-rust-01.jpg (sharpest focus, best composition)
**Flagged:**
- IMG_4393.jpg → Similar angle, slightly overexposed
- IMG_4394.jpg → Same setup, product slightly off-center
- IMG_4395.jpg → Same setup, minor blur

**Action needed:** Review and confirm. Delete flagged or move back if preferred.
```

### Duplicate Rules
1. Never auto-delete — always flag and let the user decide
2. Move flagged duplicates to `_duplicates/` with a clear log
3. The manifest marks duplicates with a `duplicate: true` flag and links to the kept version
4. When adding new assets, always check against existing manifest before organizing

## Manifest

The manifest is the searchable index of all organized assets. It's generated in two formats:

### CSV Format (`asset-manifest.csv`)

Columns:
- `file_name` — Renamed file name
- `original_name` — Original file name before renaming
- `category` — Folder path within brand-assets/
- `type` — photo or video
- `description` — Full description of the asset
- `shot_type` — Close-up, mid-range, wide, flat lay, etc.
- `mood` — Mood/tone tags
- `seasonality` — Season if applicable
- `tags` — Comma-separated searchable tags
- `suggested_use` — Recommended channels/placements
- `quality` — High, Medium, Low
- `duration` — Video duration (blank for photos)
- `aspect_ratio` — Video aspect ratio
- `thumbnail` — Video thumbnail frame reference
- `duplicate` — true/false
- `duplicate_of` — If duplicate, which file it duplicates
- `date_added` — Date the asset was organized
- `notes` — Any additional notes

### Markdown Format (`asset-manifest.md`)

A human-readable version of the manifest organized by category, with full descriptions and tags. Includes a summary section at the top:

```markdown
# Brand Asset Manifest

## Summary
- **Total assets:** 127
- **Photos:** 108
- **Videos:** 19
- **Categories:** 8
- **Duplicates flagged:** 12
- **Last updated:** 2026-03-19

## Quick Search Guide
Search this file for:
- Channel names: "Instagram", "Meta Ads", "Email", "Shopify"
- Moods: "adventurous", "cozy", "bold", "minimal"
- Seasons: "fall", "winter", "summer", "spring"
- Shot types: "flat lay", "lifestyle", "close-up", "wide"
- Products: specific product names
- Tags: any keyword

---

## Product Photography

### product-flatlay-workman-flannel-rust-01.jpg
- **Original:** IMG_4392.jpg
- **Description:** Flat lay of Workman Flannel in rust colorway on reclaimed wood surface. Clean composition with flannel folded showing collar and button detail.
- **Tags:** flannel, product, flat lay, rust, wood, workman
- **Suggested Use:** Shopify PDP, Email hero, Pinterest
- **Quality:** High

[...continues for all assets...]
```

## Channel Suggestion Logic

When suggesting where to use an asset, apply these rules:

| Asset Characteristics | Suggested Channels |
|----------------------|-------------------|
| Square/vertical, lifestyle, bright, people | Instagram feed, Instagram Stories/Reels |
| Horizontal, high-quality, hero-worthy | Website banners, Email headers |
| Flat lay, clean background, product-focused | Shopify PDP, Email product blocks, Pinterest |
| Action shot, bold, eye-catching, high contrast | Meta Ads, Google Ads display |
| Vertical video, <60s, casual/energetic | Instagram Reels, TikTok, YouTube Shorts |
| Horizontal video, >60s, polished | YouTube, Facebook feed, Website |
| Behind-the-scenes, casual, authentic | Instagram Stories, TikTok, Community posts |
| UGC/customer photos | Social proof, Reviews, Instagram reposts |
| Logo files, brand marks | All platforms as needed |
| Team photos, workspace | About page, Email signatures, LinkedIn |

Adjust suggestions based on which channels the brand is actually active on (from `digital-ecosystem.md` or user input).

## Processing Workflow

### Initial Organization (first run)

1. **Load brand context** — Read brand-knowledge-center/ or ask questions
2. **Propose folder structure** — Suggest categories, get user approval
3. **Scan source folder** — List all image and video files found
4. **Report summary** — "Found 142 photos and 23 videos. Ready to organize?"
5. **Process batch** — For each asset:
   a. Analyze the asset (subject, mood, quality, etc.)
   b. Determine category
   c. Generate descriptive filename
   d. Check for duplicates against already-processed assets
   e. Copy (not move) to appropriate subfolder with new name
   f. Add entry to manifest
6. **Generate thumbnails** — For each video, identify thumbnail frames
7. **Write manifest** — Generate both .csv and .md versions
8. **Duplicate report** — Write flagged-duplicates.md if any found
9. **Summary** — Report what was organized, categories used, duplicates found

### Adding New Assets (subsequent runs)

1. **Load existing manifest** — Read asset-manifest.csv to know what's already organized
2. **Scan new source** — List new files
3. **Check for duplicates** — Compare new assets against existing manifest (filename, size, description similarity)
4. **Flag duplicates** — If a new asset appears to duplicate an existing one, flag it before organizing
5. **Process new assets** — Same analysis, naming, and categorization as initial run
6. **Update manifest** — Append new entries, update summary counts
7. **Report** — Show what was added, what was flagged as duplicate

## Quality Flags

Each asset gets a quality assessment:

- **High** — Sharp focus, good composition, proper exposure, usable for marketing as-is
- **Medium** — Decent quality but may need minor editing (cropping, color correction)
- **Low** — Blurry, poorly lit, bad composition, or too small resolution for marketing use

Low-quality assets are still organized but flagged in the manifest so the user can review and decide whether to keep or remove them.
