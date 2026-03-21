# /add-assets

Add new photos and videos to an existing brand asset library. The recommended workflow is to drop new assets into the `_inbox/` folder and run this command — Claude scans, analyzes, proposes organization, and **waits for your approval before copying or renaming anything**.

## Invoke Options

```
/add-assets                  ← scan _inbox/ folder automatically
/add-assets [folder path]    ← point to a specific folder of new assets
```

---

## Before Starting

1. Check if `brand-assets/` exists with an `asset-manifest.csv`.
   - If it does NOT exist, say: "No asset library found. Run `/asset-setup` to build your folder structure first."
2. Read `asset-manifest.csv` to load the current inventory.
3. Report the current library state:

> "Your asset library currently has **[X] photos** and **[Y] videos** across [Z] categories. Last updated: [date]. Ready to add new assets."

---

## Step 1: Find New Assets

### Default: Check `_inbox/`

If no folder path is provided, check `brand-assets/_inbox/` for files.

If `_inbox/` is empty:
> "The inbox is empty. Drop new photos or videos into `brand-assets/_inbox/` and run `/add-assets` again. Or provide a folder path: `/add-assets [path]`"

If `_inbox/` has files, report:
> "Found **[X] photos** and **[Y] videos** in your inbox. Analyzing before any changes are made..."

### Custom folder path

If a path is provided, scan that folder recursively for image and video files and report what was found.

---

## Step 2: Analyze All New Assets

**Analyze every new asset completely BEFORE proposing any organization.** Do not copy, move, or rename anything in this step.

For each photo:
1. View/read the image
2. Identify: subject, products visible, shot type, setting, mood, lighting, composition quality, colors, people, seasonality
3. Determine the best category/subfolder within the existing structure
4. Generate a descriptive filename (check sequence numbers against existing files in the target folder)
5. Write the full description and tags
6. Assess quality (High / Medium / Low)

For each video:
1. Read the video file
2. Identify: duration, content summary, subjects, shot types, audio, mood, aspect ratio
3. Determine category, generate filename, write description
4. Identify 2-3 thumbnail candidate frames with timestamps
5. Assess quality

---

## Step 3: Duplicate Check

Compare every new asset against the existing manifest:

**Exact duplicate:** Same file size AND same dimensions → flag immediately

**Near duplicate:** Analyze subject and composition, compare against existing manifest entries in the same category. Flag if a new asset appears to be a near-duplicate.

---

## Step 4: Present Proposal — APPROVAL REQUIRED

After analyzing all assets and checking for duplicates, present the full proposal **before doing anything**:

```
New Asset Proposal
─────────────────────────────────────────────

23 photos and 4 videos analyzed from _inbox/.

Proposed organization:
  product-photography/flat-lay/     →  8 assets
  product-photography/on-model/     →  6 assets
  lifestyle/outdoor/                →  7 assets
  campaigns/spring-2026/            →  4 assets
  video/social-clips/               →  4 assets (vertical, <60s)
  _duplicates/                      →  2 assets flagged

Naming examples:
  IMG_7823.jpg  → product-flatlay-trail-runner-black-05.jpg
  IMG_7831.jpg  → lifestyle-outdoor-morning-run-03.jpg
  VID_0042.mp4  → video-social-clips-spring-launch-01.mp4

Duplicates found: 2 files
  IMG_7800.jpg → near-duplicate of product-flatlay-trail-runner-black-02.jpg
  IMG_7801.jpg → exact duplicate of lifestyle-outdoor-morning-run-01.jpg

Quality:
  High: 21  |  Medium: 4  |  Low: 2 (will be organized but flagged)

─────────────────────────────────────────────
Ready to organize. This will:
  ✓ COPY assets from _inbox/ to their organized folders with new names
  ✓ Move duplicate files to _duplicates/
  ✓ Update asset-manifest.csv and asset-manifest.md
  ✓ Clear processed files from _inbox/

Type 'approve' to proceed, or ask questions/request changes first.
```

If the user requests changes (different category, different name, exclude a file), apply changes and re-present.

---

## Step 5: Execute

Only after approval:

1. **Process each approved asset:**
   - Copy from `_inbox/` (or source folder) to the appropriate subfolder with the new name
   - Check existing sequence numbers in the target folder before numbering
   - Copy flagged duplicates to `_duplicates/` with original names
   - Add entry to manifest data

2. **New category detection:** If an asset doesn't fit any existing category, propose creating a new subfolder before proceeding.

3. **Clear inbox:** After successful processing, remove the original files from `_inbox/` (or leave them if the source was a custom folder — never modify files outside `brand-assets/`).

4. Report progress every 15 files.

---

## Step 6: Update Manifest

After all assets are processed:
1. **Append** new entries to `asset-manifest.csv`
2. **Regenerate** `asset-manifest.md` with updated counts and new entries added to their category sections
3. **Update summary counts** at the top of `asset-manifest.md`
4. **Update** `_duplicates/flagged-duplicates.md` if new duplicates were flagged

---

## Step 7: Completion

```
New Assets Added!

Added: 21 photos, 4 videos
Skipped: 2 duplicates (moved to _duplicates/)

Added to:
  Product Photography: 14
  Lifestyle:            7
  Video/Social Clips:   4

Updated library totals:
  Photos: [previous] → [new]
  Videos: [previous] → [new]
  Last updated: [date]

Inbox cleared ✓

Next: Drop more assets in brand-assets/_inbox/ anytime and run /add-assets
```

---

## Inbox Folder Convention

The `_inbox/` folder is the permanent drop zone for the ongoing workflow:

```
New shoot / new content
        ↓
brand-assets/_inbox/     ← drop files here
        ↓
/add-assets              ← run this command
        ↓
Analyze → Propose → Approve → Organize
        ↓
brand-assets/[category]/ ← files land here, named + tagged
```

Assets in `_inbox/` are never modified until approved. If you cancel before approving, all files remain in `_inbox/` unchanged.
