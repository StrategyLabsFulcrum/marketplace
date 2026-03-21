# /organize-assets

Analyze, organize, rename, and catalog a folder of unorganized brand photos and videos. Builds the folder structure if one doesn't exist, analyzes every asset, then **stops for your approval before copying or renaming anything**.

> **Starting fresh?** Use `/asset-setup` first — it builds the folder structure before you load assets, which gives you a cleaner starting point.

## Before Starting

1. Check if a `brand-assets/` directory already exists with an `asset-manifest.csv`.
   - If it exists, say: "You already have an organized asset library. Would you like to re-organize from scratch, or use `/add-assets` to add new files to the existing structure?"
   - If re-organizing from scratch over an existing library, back it up by renaming to `brand-assets-backup-[date]/`.
2. Check if a `brand-knowledge-center/` directory exists for brand context.

---

## Step 1: Brand Context

### If `brand-knowledge-center/` exists:

Read these files:
- `brand-identity.md` — Brand pillars, visual identity, product lines, colors
- `audience-messaging.md` — Audience segments, content pillars, channels
- `digital-ecosystem.md` — Active platforms and tools
- `business-overview.md` — Industry, product types

Confirm what was found:

> "I found your Brand Knowledge Center. Here's what I'll use to organize your assets:
> - **Brand:** [name]
> - **Products:** [product types]
> - **Active channels:** [list]
> - **Content pillars:** [list]
>
> Does this look right?"

### If NO brand knowledge exists:

Ask:
1. "What does your brand sell?"
2. "What channels do you publish on?"
3. "What types of content do you shoot?"
4. "Any specific product lines or collections?"
5. "What are your brand colors?"

---

## Step 2: Propose Folder Structure

Based on brand context, propose a tailored folder structure as a visual tree. Always include `_inbox/` and `_duplicates/`.

Ask:
1. "Does this folder structure work? Any categories to add, remove, or rename?"
2. "Do you have specific product lines that should get their own subfolders?"
3. "Any campaign names or seasons to add as subfolders?"

Apply edits and confirm the final structure.

---

## Step 3: Source Assets

Ask where the unorganized assets are:

> "Where are the photos and videos you'd like to organize? Provide a folder path, or upload them directly."

Once the source is identified:
1. Recursively scan for all image files (.jpg, .jpeg, .png, .webp, .heic, .tiff, .gif) and video files (.mp4, .mov, .avi, .mkv, .webm)
2. Report what was found:
   > "Found **87 photos** and **12 videos** in [source folder]."

---

## Step 4: Analyze All Assets

**Analyze every asset BEFORE proposing any organization.** Do not copy, move, or rename anything in this step.

For each photo, determine:
- Subject, products visible, shot type, setting, mood, lighting, composition quality, colors, people, seasonality
- Proposed category and subfolder
- Proposed descriptive filename
- Channel suggestions
- Quality rating (High / Medium / Low)
- Duplicate flags

For each video, determine:
- Duration, content summary, subjects, shot types, audio, aspect ratio, mood
- Proposed category and subfolder
- Proposed descriptive filename
- Thumbnail candidate timestamps
- Quality rating
- Duplicate flags

Process in batches of 25-50 and report progress:
> "Analyzing assets... 40/87 complete."

---

## Step 5: Present Organization Proposal — APPROVAL REQUIRED

After all assets are analyzed, present a complete summary **before doing anything**:

```
Organization Proposal
─────────────────────────────────────────────

87 photos and 12 videos analyzed.

Proposed folder assignments:
  product-photography/flat-lay/       → 18 assets
  product-photography/on-model/       → 12 assets
  product-photography/detail-shots/   →  6 assets
  lifestyle/outdoor/                  → 22 assets
  lifestyle/seasonal/                 →  8 assets
  team-behind-the-scenes/             →  7 assets
  ugc-community/                      →  5 assets
  campaigns/fall-2025/                →  4 assets
  logos-brand-marks/primary/          →  3 assets
  video/lifestyle/                    →  8 assets
  video/social-clips/                 →  4 assets
  _duplicates/                        →  9 assets flagged

Quality breakdown:
  High:    72 assets (will be organized)
  Medium:  18 assets (will be organized, flagged for editing)
  Low:      9 assets (will be organized, flagged for review)

Naming examples:
  IMG_4392.jpg    → product-flatlay-workman-flannel-rust-01.jpg
  DSC_0012.jpg    → lifestyle-outdoor-trail-flannel-fall-01.jpg
  MVI_8834.mp4    → video-lifestyle-fall-lookbook-01.mp4

Duplicate groups found: 3 groups, 9 total files
  Group 1: 4 similar flat-lay variants → keeping best, flagging 3
  Group 2: 3 duplicate lifestyle shots → keeping best, flagging 2
  Group 3: Exact duplicate logo files → keeping 1, flagging 1

─────────────────────────────────────────────
Ready to organize. This will:
  ✓ Create the folder structure in brand-assets/
  ✓ COPY (not move) all assets to organized folders with new names
  ✓ Move duplicate files to _duplicates/
  ✓ Generate asset-manifest.csv and asset-manifest.md
  ✗ Original files will NOT be modified or deleted

Type 'approve' to proceed, or ask questions/request changes first.
```

**Do not proceed until the user types 'approve' or an equivalent confirmation.** If they request changes (different categories, different naming, exclude certain files), apply the changes and re-present the proposal.

---

## Step 6: Execute Organization

Only after approval:

For each asset:
1. Copy to the appropriate subfolder with the new descriptive name
2. Copy flagged duplicates to `_duplicates/` with original names
3. Add entry to manifest data

Report progress every 20 assets:
> "Organized 40/87 photos. So far: 22 product shots, 12 lifestyle, 4 team/BTS. 3 duplicates moved."

---

## Step 7: Generate Manifest

After all assets are copied, generate:

**`asset-manifest.csv`** — with columns:
`file_name, original_name, category, type, description, shot_type, mood, seasonality, tags, suggested_use, quality, duration, aspect_ratio, thumbnail, duplicate, duplicate_of, date_added, notes`

**`asset-manifest.md`** — human-readable index with:
1. Summary section (total counts, category breakdown, duplicate count, date)
2. Quick Search Guide (what keywords to search for)
3. Assets by category with full descriptions

---

## Step 8: Duplicate Report

If any duplicates were flagged, generate `_duplicates/flagged-duplicates.md`:

```markdown
## Duplicate Group 1: Workman Flannel Flat Lay
**Kept:** product-flatlay-workman-flannel-rust-01.jpg (sharpest focus, best composition)
**Flagged:**
- IMG_4393.jpg → Similar angle, slightly overexposed
- IMG_4394.jpg → Same setup, product slightly off-center

**Action needed:** Review and confirm. Delete flagged or move back if preferred.
```

---

## Step 9: Completion

```
Asset Library Complete!

📁 brand-assets/
  72 photos organized across 6 categories
  12 videos organized with thumbnail timestamps noted
  9 duplicate files moved to _duplicates/ (3 groups)
  asset-manifest.csv — searchable spreadsheet
  asset-manifest.md  — human-readable index

Quality breakdown:
  High:   61 | Medium: 18 | Low: 5 (flagged for review)

Next steps:
  → Review flagged duplicates: brand-assets/_duplicates/flagged-duplicates.md
  → Review low-quality assets in the manifest
  → Drop future assets in brand-assets/_inbox/ and run /add-assets
```

Create `brand-assets/_inbox/` if it doesn't already exist, with a `.keep` file and a brief README explaining the inbox workflow.
