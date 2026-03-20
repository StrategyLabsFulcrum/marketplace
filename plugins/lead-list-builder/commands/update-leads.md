# Update Leads

Track lead status, add outreach notes, discover net-new leads, and refresh an existing lead list. This is the ongoing management command for lead lists.

## Before Starting

1. Check for existing lead lists in `lead-lists/`.
   - If none exist: "No lead lists found. Run `/build-lead-list` first."
   - If multiple exist: "Which lead list do you want to update?" (list them)
   - If one exists: Load it automatically.

---

## Main Menu

After loading the list, present the current state and options:

> "**Lead List: [list-name]**
> Last updated: [date]
>
> | Status | Count |
> |--------|-------|
> | Not Started | X |
> | Drafted | X |
> | Sent | X |
> | Responded | X |
> | Converted | X |
> | Declined | X |
> | Stale | X |
> | **Total** | **X** |
>
> What would you like to do?
>
> 1. **Update status** — Mark leads as sent, responded, converted, etc.
> 2. **Add notes** — Add outreach notes or follow-up details
> 3. **Find new leads** — Research net-new leads to add to this list
> 4. **Refresh stale leads** — Re-research leads marked as stale
> 5. **Bulk status update** — Update multiple leads at once
> 6. **Regenerate dashboard** — Update the dashboard with current data"

Route to the appropriate section below.

---

## Option 1: Update Status

Ask which lead(s) to update:

> "Which lead do you want to update? Enter the lead ID (e.g., L-001) or search by name/company."

After identifying the lead, show current state:

> "**L-001: Sarah Chen — Buyer, Mountain Outfitters**
> - Current status: `drafted`
> - Last updated: 2026-03-19
> - Notes: Initial email drafted
>
> New status?"
> - Sent
> - Responded (positive / neutral / negative)
> - Converted
> - Declined
> - Stale

After the user selects:
1. Update `outreach_status` in the CSV
2. Prompt for a note: "Any notes to add? (e.g., 'Sent intro email 3/20, waiting for reply')"
3. Update `outreach_notes` and `last_updated`
4. Confirm the update

Ask: "Update another lead, or back to main menu?"

---

## Option 2: Add Notes

Same lead selection as Option 1. After identifying the lead:

> "**L-001: Sarah Chen — Mountain Outfitters**
> - Current notes: [existing notes]
>
> Add a note:"

Append the new note with a timestamp:
```
[2026-03-20] Sent intro email with wholesale line sheet. She replied asking for samples — sending Friday.
[2026-03-19] Initial email drafted.
```

Update `last_updated` and save.

---

## Option 3: Find New Leads

Research net-new leads to add to the existing list.

### Step 1: Load Existing List

Read the current CSV and extract all existing:
- Company names
- Contact names
- Locations covered

### Step 2: Confirm Search Criteria

> "Your current list has [X] leads across these types: [list types].
> Geography: [current geo].
>
> For new leads, do you want to:
> - **Same criteria** — Find more of the same types in the same areas
> - **Expand geography** — Same types, new locations
> - **New lead type** — Add a type you haven't searched yet
> - **Custom** — Specify exactly what you're looking for"

### Step 3: Research with Deduplication

Execute research with the existing list as an exclusion filter:

1. Build search queries based on selected criteria
2. For every lead found, check against existing list:
   - **Same name + same company** → skip (exact duplicate)
   - **Same company, new contact** → flag as "new contact at existing company"
   - **Same name, different company** → flag as "possible job change"
   - **Similar company name** → flag for review (fuzzy match)
3. Only present truly net-new leads

### Step 4: Present Net-New Leads

> "**Net-New Lead Research Results:**
>
> Found **14 new leads** not in your current list:
> - 8 new companies
> - 3 new contacts at companies already in your list
> - 3 flagged for review (possible duplicates)
>
> **New Companies:**
> | # | Name | Title | Company | Location | Relevance |
> |---|------|-------|---------|----------|-----------|
> | 1 | ... | ... | ... | ... | ⭐⭐⭐⭐ |
>
> **New Contacts at Existing Companies:**
> | # | Name | Title | Company | Existing Contact |
> |---|------|-------|---------|------------------|
> | 1 | ... | ... | ... | Sarah Chen (Buyer) |
>
> **Flagged for Review:**
> | # | Found | Possible Match | Reason |
> |---|-------|----------------|--------|
> | 1 | Mountain Outfitters LLC | Mountain Outfitters | Similar name |
>
> Which leads do you want to add?"

### Step 5: Add Confirmed Leads

1. Assign new IDs continuing the sequence (if last was L-041, new starts at L-042)
2. Append to the existing CSV
3. Regenerate the markdown summary with updated counts
4. Offer to draft outreach: "Want me to draft outreach for the new leads? (Run `/lead-outreach`)"

---

## Option 4: Refresh Stale Leads

Re-research leads that have been marked as stale:

1. Filter all leads with `outreach_status: stale`
2. For each stale lead:
   - Re-search the person/company to check if they're still in the same role
   - Check for new contact info
   - Check for new activity (recent posts, new products, company changes)
3. Present findings:
   > "**Stale Lead Refresh:**
   >
   > - **L-005: Mike Torres** — Still at Cascadia Goods, recently posted about expanding inventory. Worth retrying with a new angle.
   > - **L-012: Jessica Park** — Left Mountain Gear Co. Now at Trailhead Supply (updated).
   > - **L-018: Ryan Diaz** — Company appears closed. Recommend removing.
   >
   > Update these leads?"
4. Update records based on user confirmation

---

## Option 5: Bulk Status Update

For updating multiple leads at once:

> "Select leads to update:
> - **By type:** Update all [lead type] leads
> - **By current status:** Update all [status] leads
> - **By ID range:** Update L-001 through L-010
> - **By list:** Enter specific IDs (e.g., L-001, L-005, L-012)"

After selection, apply the same status change to all selected leads. Prompt for a shared note if relevant.

---

## Option 6: Regenerate Dashboard

Regenerate the HTML dashboard with current data:

1. Read the latest CSV
2. Rebuild the dashboard HTML with updated status counts, notes, and any new leads
3. Overwrite the existing dashboard file
4. Confirm: "Dashboard updated at `lead-lists/[list-name]-dashboard.html`"

---

## After Any Update

After every update action:
1. Save the updated CSV
2. Update the markdown summary file (status counts, last updated date)
3. Ask: "Want to regenerate the dashboard too?"
4. Return to main menu or exit
