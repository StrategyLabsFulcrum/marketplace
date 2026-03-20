# Lead Dashboard

Generate or regenerate an interactive HTML dashboard for a lead list. The dashboard provides a visual, filterable, searchable interface for managing and tracking leads.

## Before Starting

1. Check for existing lead lists in `lead-lists/`.
   - If none exist: "No lead lists found. Run `/build-lead-list` first."
   - If multiple exist: "Which lead list do you want to create a dashboard for?" (list them)
   - If one exists: Load it automatically.
2. Check if a dashboard already exists for this list.
   - If it exists: "A dashboard already exists. Regenerate with latest data?"

---

## Step 1: Load Data

Read the lead list CSV and compute summary metrics:

- Total leads by type
- Leads by status (with percentages)
- Leads by location
- Relevance score distribution
- Outreach pipeline (not_started → drafted → sent → responded → converted)
- Response rate (responded / sent)
- Conversion rate (converted / total)
- Stale/declined rate
- Average relevance score
- Leads added over time (by date_added)

---

## Step 2: Brand Styling (Optional)

If `brand-knowledge-center/brand-identity.md` exists, pull brand colors and fonts to style the dashboard:

- Primary color for headers and accents
- Secondary color for backgrounds
- Brand fonts for headings and body
- Brand name and logo reference in the header

If no brand knowledge, use a clean default theme (dark navy + white + accent blue).

---

## Step 3: Generate Dashboard HTML

Create a single-file HTML dashboard at `lead-lists/[list-name]-dashboard.html`.

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[List Name] — Lead Dashboard</title>
  <style>
    /* All CSS inline — no external dependencies */
    /* Responsive grid layout */
    /* Brand colors if available */
    /* Print-friendly media queries */
  </style>
</head>
<body>

  <!-- HEADER -->
  <!-- Brand name, list name, date, total leads, status summary bar -->

  <!-- SUMMARY CARDS -->
  <!-- Total leads, by type (bar), by status (pie), relevance distribution -->
  <!-- Pipeline funnel: not_started → drafted → sent → responded → converted -->
  <!-- Response rate, conversion rate -->

  <!-- FILTER BAR -->
  <!-- Dropdowns: Lead Type, Location, Relevance, Status, Channel -->
  <!-- Search box: searches name, company, title, tags -->
  <!-- Sort: Relevance, Date Added, Status, Company, Location -->
  <!-- Reset filters button -->

  <!-- LEAD TABLE -->
  <!-- Sortable columns: ID, Name, Title, Company, Location, Type, Relevance, Status, Channel, Date Added -->
  <!-- Color-coded relevance badges (5=green, 4=blue, 3=yellow, 2=orange, 1=gray) -->
  <!-- Color-coded status badges -->
  <!-- Click row to expand: full details, outreach notes, suggested message, source URL -->
  <!-- Quick action: status dropdown to update (updates in-page, not persisted to CSV) -->

  <!-- OUTREACH TRACKER -->
  <!-- Follow-ups due (leads where status=sent and days since > follow-up cadence) -->
  <!-- Recent activity timeline (last 10 status changes by date) -->
  <!-- Stale leads alert (leads with no update in 30+ days) -->

  <!-- LOCATION BREAKDOWN -->
  <!-- Grouped list of leads by city/state with counts -->

  <!-- EXPORT -->
  <!-- Button: Download current filtered view as CSV -->
  <!-- Button: Print-friendly view -->

  <script>
    // All data embedded as JSON
    const leadData = [ /* ... lead records ... */ ];

    // Filter logic
    // Sort logic
    // Search logic
    // Expand/collapse row logic
    // Export to CSV logic
    // Summary chart rendering (CSS-only bar charts, no chart library needed)
  </script>

</body>
</html>
```

### Dashboard Features

**Summary Cards (top section):**
- Total leads count (large number)
- Leads by type — horizontal bar chart (CSS-based)
- Status breakdown — color-coded horizontal bar showing proportion in each status
- Pipeline funnel — visual flow from not_started through converted with counts at each stage
- Key metrics: Response rate %, Conversion rate %, Average relevance score

**Filter Bar:**
- Lead Type dropdown (multi-select)
- Location dropdown (multi-select, grouped by state)
- Relevance Score dropdown (1-5)
- Status dropdown (multi-select)
- Suggested Channel dropdown
- Free-text search (searches across name, company, title, tags, notes)
- Date range filter (date added)
- "Reset Filters" button
- Active filter count badge

**Lead Table:**
- Sortable by clicking column headers (toggle asc/desc)
- Relevance shown as colored dots or stars
- Status shown as colored pill badges:
  - Not Started = gray
  - Drafted = blue
  - Sent = yellow
  - Responded = green
  - Converted = dark green
  - Declined = red
  - Stale = orange
- Row click expands to show:
  - Full description and all fields
  - Outreach notes (chronological)
  - Suggested outreach message (if drafted)
  - Source URL (clickable link)
  - Tags
- Table footer: showing "X of Y leads" based on active filters

**Outreach Tracker (bottom section):**
- **Follow-ups due:** Leads where status is "sent" and enough time has passed for next follow-up
- **Recently updated:** Last 10 leads with status changes, sorted by last_updated
- **Stale alerts:** Leads with no update in 30+ days that aren't in a terminal state (converted/declined)

**Export:**
- "Export CSV" button — downloads current filtered view as a CSV file
- "Print" button — reformats page for print (hides filters, shows all expanded)

### Technical Requirements

- **Zero dependencies** — All CSS and JS inline in a single HTML file
- **No chart libraries** — Use CSS-based bar charts and progress bars
- **Responsive** — Works on desktop (full table) and mobile (card layout)
- **Data as JSON** — All lead data embedded in a `<script>` tag as a JSON array
- **Client-side only** — All filtering, sorting, and searching happens in-browser
- **File size** — Keep under 500KB even with 500+ leads

---

## Step 4: Completion

```
Dashboard Generated!

📊 lead-lists/[list-name]-dashboard.html

Features:
- [X] total leads displayed
- Filterable by type, location, relevance, status, channel
- Full-text search across all lead fields
- Sortable table with expandable detail rows
- Pipeline funnel visualization
- Outreach tracker with follow-up alerts
- CSV export of filtered views

Open the HTML file in any browser to use.
Regenerate anytime with /lead-dashboard after updating leads.
```
