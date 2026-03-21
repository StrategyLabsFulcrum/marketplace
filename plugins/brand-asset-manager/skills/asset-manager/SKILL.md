---
name: asset-manager
description: >
  Brand Asset Manager for building and maintaining a structured, searchable asset library.
  Use when the user mentions "organize assets", "asset library", "asset setup", "brand photos",
  "brand videos", "photo organization", "image catalog", "content library", "asset management",
  "organize images", "rename photos", "tag assets", "find photos", "search assets",
  "new asset workflow", "inbox folder", "add photos", "add videos", "asset folder structure",
  or wants to build, populate, or maintain a structured library of brand visual content.
---

# Brand Asset Manager

A three-phase system for building and maintaining a structured, searchable brand asset library. Handles setup from scratch, initial organization, and an ongoing inbox-based workflow for adding new assets.

---

## Three-Phase System

### Phase 1 — Setup (`/asset-setup`)
Build the folder structure BEFORE assets exist. Interview the brand, propose a custom folder structure, get approval, then create it. Leaves the brand with a ready-to-fill library and a permanent `_inbox/` drop zone.

### Phase 2 — Initial Organization (`/organize-assets`)
Analyze a folder of unorganized existing assets. Scans, analyzes, and proposes organization — then **stops for approval** before copying or renaming anything. After approval, copies (never moves) all assets into the organized structure with descriptive names and generates the manifest.

### Phase 3 — Ongoing Inbox Workflow (`/add-assets`)
The permanent ongoing workflow. Drop new assets into `_inbox/` → run `/add-assets` → Claude analyzes, proposes, waits for approval, then organizes and updates the manifest. Inbox is cleared after successful processing.

---

## Core Principles

1. **Analyze first, act second** — Never copy, rename, or move anything until all assets are analyzed and a full proposal is presented.
2. **Approval required** — Every organization action requires explicit user approval ("approve") before execution.
3. **Copy, never move** — Original source files are never modified, renamed, or deleted. Only the organized copies in `brand-assets/` are renamed.
4. **Inbox is permanent** — `_inbox/` is always created as part of setup and is the standard drop zone for all new assets going forward.
5. **Manifest is always updated** — Every add/organize action regenerates both manifest files.

---

## Brand Context Integration

Before organizing assets, check for a `brand-knowledge-center/` folder.

### If brand knowledge exists:
Read these files:
1. `brand-identity.md` — brand pillars, visual identity, product lines, colors
2. `audience-messaging.md` — audience segments, content pillars, channel strategy
3. `digital-ecosystem.md` — active platforms and channels
4. `business-overview.md` — industry, product types

Use this context to inform category suggestions, channel recommendations, and asset descriptions.

### If brand knowledge does NOT exist:
Ask the user:
1. What does your brand sell? (product types)
2. What channels do you publish on? (Instagram, Facebook, email, website, ads, TikTok, YouTube, etc.)
3. What types of content do you shoot? (product photos, lifestyle, BTS, events, UGC, etc.)
4. Any specific product lines or collections to organize around?
5. What are your brand colors?

---

## Folder Structure

All organized assets live in a `brand-assets/` master folder. Always include `_inbox/` and `_duplicates/`.

### Standard Structure (customized per brand)

```
brand-assets/
├── asset-manifest.csv
├── asset-manifest.md
├── README.md
├── _inbox/                     ← permanent drop zone for new assets
├── _duplicates/                ← flagged duplicates for review
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

1. **Start with defaults**, then ask the user to confirm, edit, add, or remove categories
2. **Product-specific subfolders** — if distinct product lines exist, offer subfolders within `product-photography/`
3. **Channel-specific subfolders** — if active on specific platforms, offer folders like `video/reels/` or `email-headers/`
4. **Depth limit** — no more than 3 levels deep
5. **Empty folders are OK** — create the structure even if unfilled; it guides future shoots
6. **Never remove `_inbox/` or `_duplicates/`** — these are required regardless of customization

---

## Asset Analysis

### Photo Analysis

For each image file (.jpg, .jpeg, .png, .webp, .heic, .tiff):

1. **Subject identification** — What's in the photo?
2. **Product recognition** — Brand products visible, identified by name/type
3. **Shot type** — Close-up, mid-range, wide, flat lay, overhead, lifestyle, candid, posed
4. **Setting/location** — Studio, outdoor, indoor, urban, nature, etc.
5. **Mood/tone** — Adventurous, cozy, energetic, minimal, bold, warm, rugged
6. **Lighting** — Natural, studio, golden hour, overcast, dramatic
7. **Composition quality** — Is this usable for marketing? Flag low-quality, blurry, or poorly lit
8. **Color palette** — Dominant colors, alignment with brand colors
9. **People** — Present? How many? Activity?
10. **Seasonality** — Does this feel seasonal?

### Video Analysis

For each video file (.mp4, .mov, .avi, .mkv, .webm):

1. **Duration** — Length of the video
2. **Content summary** — What happens? Key scenes
3. **Subjects** — Products, people, locations featured
4. **Shot types** — Static, handheld, drone, slow-motion, timelapse
5. **Audio** — Music, voiceover, natural sound, silent
6. **Mood/tone**
7. **Thumbnail candidates** — 2-3 strong frames with timestamps
8. **Platform fit** — Aspect ratio and length suggest platforms

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
**Description:** Lifestyle reel showing three models wearing Fall 2025 collection pieces across PNW locations.
**Scenes:** 0:00-0:15 coffee shop, 0:15-0:30 forest trail, 0:30-0:45 waterfront golden hour
**Mood:** Warm, community, seasonal
**Audio:** Acoustic music, no voiceover
**Tags:** fall, collection, lookbook, flannel, hoodie, PNW, forest
**Suggested Use:** YouTube, Facebook feed, Website collection page
**Thumbnails:** Frame at 0:12 (flannel collar close-up), Frame at 0:38 (golden hour wide shot)
**Quality:** High — professional grade, strong color grading
```

---

## File Naming Convention

Original files are never modified. Copies in the organized structure use descriptive names.

**Pattern:** `{category}-{subject}-{detail}-{sequence}.{ext}`

| Original | Renamed |
|----------|---------|
| IMG_4392.jpg | lifestyle-flannel-mountain-trail-01.jpg |
| DSC_0012.jpg | product-flatlay-workman-flannel-charcoal-01.jpg |
| MVI_8834.mp4 | video-lifestyle-fall-lookbook-01.mp4 |
| Screenshot 2024-03-12.png | brand-mark-primary-logo-dark-01.png |

**Rules:**
1. All lowercase, hyphens between words
2. No spaces, underscores, or special characters
3. Category prefix matches the folder it lives in
4. Subject describes what's in the asset
5. Detail adds specificity (product name, color, location)
6. Two-digit sequence number at the end (01, 02, 03...)
7. Check existing files in the target folder before assigning sequence numbers
8. Preserve original file extension
9. Maximum 60 characters for filename (excluding extension)

---

## Duplicate Detection

### Exact Duplicates
- Same file size AND same dimensions = likely exact duplicate
- Flag, copy to `_duplicates/` folder
- Keep the higher-quality version in the main structure

### Near Duplicates
- Same subject, very similar composition, same shoot session
- Flag as "near duplicates" in the manifest
- Keep the best one in the main folder, flag others to `_duplicates/`
- Log all near duplicates in `_duplicates/flagged-duplicates.md`

### Flagged Duplicates Log Format

```markdown
## Duplicate Group 1: Workman Flannel Flat Lay
**Kept:** product-flatlay-workman-flannel-rust-01.jpg (sharpest focus, best composition)
**Flagged:**
- IMG_4393.jpg → Similar angle, slightly overexposed
- IMG_4394.jpg → Same setup, product slightly off-center

**Action needed:** Review and confirm. Delete flagged or move back if preferred.
```

### Duplicate Rules
1. **Never auto-delete** — always flag and let the user decide
2. Move flagged duplicates to `_duplicates/` with original names
3. Mark duplicates in manifest with `duplicate: true` and link to kept version
4. When adding new assets, always check against existing manifest before organizing

---

## Manifest

The manifest is maintained in two formats after every organize or add operation.

### CSV Format (`asset-manifest.csv`)

Columns:
`file_name, original_name, category, type, description, shot_type, mood, seasonality, tags, suggested_use, quality, duration, aspect_ratio, thumbnail, duplicate, duplicate_of, date_added, notes`

### Markdown Format (`asset-manifest.md`)

```markdown
# Brand Asset Manifest

## Summary
- **Total assets:** 127
- **Photos:** 108
- **Videos:** 19
- **Categories:** 8
- **Duplicates flagged:** 12
- **Last updated:** [date]

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
[assets listed with full descriptions]
```

---

## Channel Suggestion Logic

| Asset Characteristics | Suggested Channels |
|----------------------|-------------------|
| Square/vertical, lifestyle, bright, people | Instagram feed, Stories/Reels |
| Horizontal, high-quality, hero-worthy | Website banners, Email headers |
| Flat lay, clean background, product-focused | Shopify PDP, Email product blocks, Pinterest |
| Action shot, bold, high contrast | Meta Ads, Google Ads display |
| Vertical video, <60s, casual/energetic | Instagram Reels, TikTok, YouTube Shorts |
| Horizontal video, >60s, polished | YouTube, Facebook feed, Website |
| Behind-the-scenes, casual, authentic | Instagram Stories, TikTok, Community posts |
| UGC/customer photos | Social proof, Reviews, Instagram reposts |
| Logo files, brand marks | All platforms as needed |
| Team photos, workspace | About page, Email signatures, LinkedIn |

Adjust suggestions based on which channels the brand is actually active on.

---

## Quality Flags

- **High** — Sharp focus, good composition, proper exposure, usable for marketing as-is
- **Medium** — Decent quality but may need minor editing (cropping, color correction)
- **Low** — Blurry, poorly lit, bad composition, or too small resolution for marketing use

Low-quality assets are still organized but flagged in the manifest for user review.

---

## Ongoing Inbox Workflow

The standard ongoing workflow after initial setup:

```
New photos/videos from shoot or download
              ↓
   brand-assets/_inbox/      ← drop files here
              ↓
        /add-assets           ← run this command
              ↓
   Analyze all new assets     ← no changes made yet
              ↓
   Present full proposal      ← shows organization plan
              ↓
   User types 'approve'       ← explicit gate
              ↓
   Copy + rename + tag        ← files organized
              ↓
   Update manifest            ← both .csv and .md
              ↓
   Clear _inbox/              ← cleaned up
```

**_inbox/ rules:**
- Files in `_inbox/` are never modified until approved
- If the user cancels before approving, all files remain in `_inbox/` unchanged
- After successful processing, inbox files are removed (they now exist in organized folders)
- The `_inbox/` folder itself is never deleted — it persists as the permanent drop zone
