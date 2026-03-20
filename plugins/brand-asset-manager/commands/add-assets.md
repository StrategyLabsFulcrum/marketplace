# Add Assets

Add new photos and videos to an existing brand asset library. Checks for duplicates against the current manifest, analyzes new assets, organizes them into the established folder structure, and updates the manifest.

## Before Starting

1. Check if a `brand-assets/` directory exists with an `asset-manifest.csv`.
   - If it exists, proceed with this command.
   - If it does NOT exist, inform the user: "No existing asset library found. Run `/organize-assets` first to set up your library."
2. Read the existing `asset-manifest.csv` to load the current inventory.

---

## Step 1: Load Existing Library

Read and report the current state:

> "Your current asset library has:
> - **[X] photos** and **[Y] videos** across [Z] categories
> - Last updated: [date]
> - Folder structure: [list top-level folders]
>
> Ready to add new assets."

---

## Step 2: Source New Assets

Ask the user where the new assets are:

"Where are the new photos/videos? Provide a folder path, or upload them directly."

### Scanning

1. Recursively scan for all image and video files
2. Report what was found:
   > "Found **23 new photos** and **4 new videos**. Checking for duplicates before organizing..."

---

## Step 3: Duplicate Check

Compare every new asset against the existing manifest:

### Exact Duplicate Check
- Compare file size and dimensions against every entry in `asset-manifest.csv`
- If an exact match is found, flag it immediately

### Near Duplicate Check
- Analyze the new asset's subject, composition, and context
- Compare description against existing manifest descriptions in the same category
- Flag if a new asset appears to be a near-duplicate of an existing one

### Report Duplicates Before Proceeding

If duplicates are found:

> "Duplicate check complete. Found:
> - **3 exact duplicates** (identical to files already in your library)
> - **2 near duplicates** (very similar to existing assets)
>
> **Exact duplicates:**
> 1. `IMG_5501.jpg` → matches `product-flatlay-workman-flannel-rust-01.jpg`
> 2. `IMG_5502.jpg` → matches `lifestyle-forest-trail-flannel-03.jpg`
> 3. `DSC_0098.jpg` → matches `product-onmodel-ridgeline-hoodie-01.jpg`
>
> **Near duplicates:**
> 1. `IMG_5510.jpg` → similar to `product-flatlay-workman-flannel-rust-01.jpg` (same product, slightly different angle)
> 2. `MVI_1002.mp4` → similar to `video-product-beanie-showcase-01.mp4` (same subject, different edit)
>
> How would you like to handle these?
> - **Skip all duplicates** — don't add them
> - **Add near duplicates, skip exact** — keep the maybes, skip the identical ones
> - **Add all anyway** — organize everything, I'll sort it out later
> - **Let me review each one** — I'll show you side by side"

Process based on user's choice.

---

## Step 4: Process New Assets

For each new non-duplicate asset, follow the same analysis workflow as `/organize-assets`:

1. **Analyze** — Subject, shot type, mood, quality, etc.
2. **Categorize** — Assign to existing folder structure
3. **Name** — Generate descriptive filename
4. **Check sequence numbers** — Read existing files in the target folder to continue the numbering sequence (if `lifestyle-flannel-mountain-trail-03.jpg` exists, the next one is `-04.jpg`)
5. **Copy** — Duplicate to the appropriate subfolder with the new name
6. **Video thumbnails** — Generate for any new videos

### New Category Detection

If a new asset doesn't fit any existing category:

> "This asset doesn't fit your current folder structure:
> - `IMG_5520.jpg` — Aerial drone shot of a mountain landscape
>
> Would you like to:
> - Create a new subfolder? (e.g., `lifestyle/aerial/`)
> - Put it in an existing folder? (suggest closest match)
> - Skip it for now?"

---

## Step 5: Update Manifest

After all new assets are processed:

1. **Append** new entries to `asset-manifest.csv`
2. **Regenerate** `asset-manifest.md` with updated counts and new entries
3. **Update** `_duplicates/flagged-duplicates.md` if new duplicates were flagged
4. **Update summary counts** at the top of `asset-manifest.md`

---

## Step 6: Completion

Present what was added:

```
New Assets Added!

Added: 18 photos, 4 videos
Skipped: 3 exact duplicates, 2 near duplicates

New assets by category:
- Product Photography: 8
- Lifestyle: 6
- Video/Social Clips: 4
- Team/BTS: 4

Updated totals:
- Total library: 90 photos, 16 videos (was 72 photos, 12 videos)
- Manifest updated: asset-manifest.csv + asset-manifest.md

Next steps:
- Search asset-manifest.md for your new assets
- Review any flagged duplicates in _duplicates/
```
