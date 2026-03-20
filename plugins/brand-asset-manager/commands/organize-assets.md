# Organize Assets

Set up a brand asset library from scratch. Analyzes all photos and videos, organizes them into categorized folders, renames files descriptively, generates metadata, suggests channel usage, and flags duplicates.

## Before Starting

1. Check if a `brand-assets/` directory already exists in the user's working folder.
   - If it exists and has files, inform the user: "You already have an organized asset library. Would you like to re-organize from scratch, or use `/add-assets` to add new files to the existing structure?"
   - If starting fresh over an existing library, back up by renaming to `brand-assets-backup-[date]/`.
2. Check if a `brand-knowledge-center/` directory exists for brand context.

---

## Step 1: Brand Context

### If `brand-knowledge-center/` exists:

Read the following files and extract relevant context:
- `brand-identity.md` — Brand pillars, visual identity, product lines, colors
- `audience-messaging.md` — Audience segments, content pillars, channels
- `digital-ecosystem.md` — Active platforms and tools
- `business-overview.md` — Industry, product types

Summarize what was found:
> "I found your Brand Knowledge Center. Here's what I'll use to organize your assets:
> - **Brand:** [name]
> - **Products:** [product types]
> - **Active channels:** [list]
> - **Content pillars:** [list]
> - **Brand colors:** [colors]
> Does this look right?"

### If NO brand knowledge exists:

Ask the user these questions:
1. "What does your brand sell?" (product types, categories)
2. "What channels do you post content on?" (Instagram, Facebook, email, website, ads, TikTok, YouTube, etc.)
3. "What types of content do you typically shoot?" (product photos, lifestyle, behind-the-scenes, events, UGC, etc.)
4. "Any specific product lines or collections?" (names, categories)
5. "What are your brand colors?" (hex codes or descriptions)

---

## Step 2: Folder Structure

Based on brand context, propose a folder structure. Tailor it to the brand's actual products, channels, and content types.

### Proposal Format

Present the proposed structure as a tree:

```
brand-assets/
├── asset-manifest.csv
├── asset-manifest.md
├── _duplicates/
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
└── video/
    ├── product/
    ├── lifestyle/
    ├── social-clips/
    └── thumbnails/
```

### Customization Questions

After proposing the structure, ask:

1. "Does this folder structure work? Any categories to add, remove, or rename?"
2. "Do you have specific product lines that should get their own subfolders?" (e.g., `product-photography/flannels/`, `product-photography/hoodies/`)
3. "Any campaign names or seasons to add as subfolders?" (e.g., `campaigns/fall-2025/`, `campaigns/black-friday/`)

Apply edits and confirm the final structure before proceeding.

---

## Step 3: Source Assets

Ask the user where their unorganized assets are:

"Where are the photos and videos you'd like to organize? Provide a folder path, or upload them directly."

### Scanning

Once the source is identified:

1. Recursively scan for all image files (.jpg, .jpeg, .png, .webp, .heic, .tiff, .gif) and video files (.mp4, .mov, .avi, .mkv, .webm)
2. Report what was found:
   > "Found **87 photos** and **12 videos** in [source folder]. Ready to start organizing?"
3. If the count is large (>200 files), suggest processing in batches:
   > "That's a lot of files. Want me to process them all at once, or in batches of 50?"

---

## Step 4: Process Assets

For each asset, perform the full analysis described in the SKILL.md. Process in this order:

### 4a: Analyze

For each photo:
1. View/read the image
2. Identify: subject, products visible, shot type, setting, mood, lighting, composition quality, colors, people, seasonality
3. Determine the best category/subfolder
4. Generate a descriptive filename following the naming convention
5. Write the full description

For each video:
1. Read the video file
2. Identify: duration, content summary, subjects, shot types, audio, mood, aspect ratio
3. Determine the best category/subfolder
4. Generate a descriptive filename
5. Write the full description
6. Identify 2-3 thumbnail candidate frames with timestamps

### 4b: Check Duplicates

As each asset is processed, compare against all previously processed assets:

**Exact duplicate check:**
- Same file size AND same dimensions → flag as exact duplicate

**Near duplicate check:**
- Same category + very similar description + similar composition → flag as near duplicate
- Example: 5 nearly identical flat lay shots from the same shoot session

**Duplicate handling:**
- Copy the best version to the main folder
- Copy flagged duplicates to `_duplicates/` with their original names
- Log all duplicate groups in `_duplicates/flagged-duplicates.md`

### 4c: Organize

For each non-duplicate asset:
1. Copy (never move) the original file to the appropriate subfolder with the new descriptive name
2. Add an entry to the manifest data

Present progress updates every 20 files or so:
> "Processed 40/87 photos. So far: 22 product shots, 12 lifestyle, 4 team/BTS, 2 logos. 3 duplicates flagged."

---

## Step 5: Video Thumbnails

For each video processed:
1. Identify the 2-3 strongest frames based on composition, clarity, and subject visibility
2. Note the timestamps in the manifest
3. If possible, extract and save thumbnail images to `video/thumbnails/` with names like:
   `thumb-fall-lookbook-01-frame-0012.jpg`

---

## Step 6: Generate Manifest

After all assets are processed, generate both manifest files:

### asset-manifest.csv

Create with columns:
`file_name, original_name, category, type, description, shot_type, mood, seasonality, tags, suggested_use, quality, duration, aspect_ratio, thumbnail, duplicate, duplicate_of, date_added, notes`

### asset-manifest.md

Create the human-readable version with:
1. **Summary section** — Total counts, category breakdown, duplicate count, date
2. **Quick Search Guide** — What keywords to search for
3. **Assets by category** — Full descriptions organized by folder

---

## Step 7: Duplicate Report

If any duplicates were flagged, generate `_duplicates/flagged-duplicates.md`:

1. Group duplicates by similarity
2. For each group, show:
   - Which file was kept (and why)
   - Which files were flagged (and what's different)
   - Action prompt: "Review and confirm. Delete flagged or move back if preferred."
3. Summary at the top: "X duplicate groups found, Y total files flagged"

---

## Step 8: Completion

Present the final summary:

```
Asset Library Complete!

📁 brand-assets/
├── 72 photos organized across 6 categories
├── 12 videos organized with thumbnails generated
├── 3 duplicate groups flagged (8 files)
├── asset-manifest.csv (searchable spreadsheet)
└── asset-manifest.md (human-readable index)

Top categories:
- Product Photography: 34 assets
- Lifestyle: 22 assets
- Video: 12 assets
- Team/BTS: 4 assets

Quality breakdown:
- High: 61 assets
- Medium: 18 assets
- Low: 5 assets (flagged for review)

Next steps:
- Review flagged duplicates in _duplicates/flagged-duplicates.md
- Review low-quality assets and decide whether to keep
- Use /add-assets when you have new photos or videos to organize
- Search asset-manifest.md for assets by channel, mood, season, or product
```
