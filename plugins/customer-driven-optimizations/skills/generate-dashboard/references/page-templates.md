# Page Templates Reference

Structural HTML blueprints for each dashboard page. The generate-dashboard skill uses these as construction patterns. All pages share the design system from `design-system.md`. Data comes from the analysis files in `customer-driven-optimizations/analysis/`.

Every page is a self-contained HTML file with inline `<style>` and `<script>`. No external dependencies except Chart.js CDN where needed.

---

## Shared Page Shell

Every page wraps in this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{PAGE_TITLE}} — {{BRAND_NAME}}</title>
  <style>
    /* Full design-system CSS inlined here */
    /* Plus any page-specific CSS */
  </style>
</head>
<body>
  <nav class="site-nav">
    <span class="nav-brand">{{BRAND_NAME}}</span>
    <a href="index.html" class="nav-link {{ACTIVE_IF_INDEX}}">Call Intelligence</a>
    <a href="competitor.html" class="nav-link {{ACTIVE_IF_COMPETITOR}}">Competitor Intel</a>
    <a href="site-changes.html" class="nav-link {{ACTIVE_IF_SITECHANGES}}">Site Changes</a>
    <a href="journeys.html" class="nav-link {{ACTIVE_IF_JOURNEYS}}">Customer Journeys</a>
  </nav>

  <!-- Page content here -->

  <script>
    // Page-specific JavaScript here
  </script>
</body>
</html>
```

The active nav link gets class `active` added.

---

## Page 1: Call Intelligence (`index.html`)

### Data Source
`analysis/call-intelligence.md` + all `analysis/raw/call-*.md` files.

### JavaScript Data Object

Embed a `DASHBOARD_DATA` object in a `<script>` block before the main script:

```javascript
const DASHBOARD_DATA = {
  generated: "{{TIMESTAMP}}",
  total_calls: {{TOTAL}},
  summary: {
    call_types: { "Product Inquiry": N, "Technical Support": N, ... },
    issue_categories: { "Fitment Questions": N, "Stock Status": N, ... },
    vehicle_families: { "Polaris RZR": N, "Can-Am Maverick": N, ... },
    top_opportunities: [
      {
        title: "...",
        percentage: N,
        call_count: N,
        avg_sentiment: N,
        resolution_rate: "N%",
        recommendation: "...",
        tags: ["fitment", "nav"]
      }
    ]
  },
  calls: [
    {
      id: N,
      date: "YYYY-MM-DD",
      caller: "Name",
      category: "Category",
      tags: ["tag1", "tag2"],
      sentiment: "positive|negative|neutral|mixed",
      summary: "...",
      pain_points: ["..."],
      competitor_mentions: ["..."],
      action_items: ["..."],
      resolution: "resolved|unresolved|partial"
    }
  ]
};
```

### Body Structure

```
<header>
  <div class="header-content">
    <div class="header-left">
      <h1>{{BRAND_NAME}} Call Intelligence</h1>
      <span class="badge">{{TOTAL_CALLS}} Calls Analyzed</span>
      <span class="date-range">{{DATE_RANGE}}</span>
    </div>
    <div class="header-right">
      <button class="btn btn-accent" onclick="openModal()">
        ⬆ Analyze New Calls
      </button>
      <button class="btn btn-outline" onclick="exportData()">
        📊 Export Data
      </button>
    </div>
  </div>
</header>

<div class="container">

  <!-- KPI Row: 5 cards -->
  <div class="kpiRow">
    <div class="kpi-card">
      <div class="kpi-value">{{TOTAL_CALLS}}</div>
      <div class="kpi-label">Total Calls</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">{{TOP_ISSUE_PCT}}%</div>
      <div class="kpi-label">Top Issue</div>
      <div class="kpi-sublabel">{{TOP_ISSUE_NAME}}</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">{{RESOLUTION_RATE}}%</div>
      <div class="kpi-label">Resolution Rate</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">{{AVG_SENTIMENT}}</div>
      <div class="kpi-label">Avg Sentiment</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-value">{{ACTION_ITEMS_COUNT}}</div>
      <div class="kpi-label">Action Items</div>
    </div>
  </div>

  <!-- Top Opportunities -->
  <h2 class="section-title">Top Opportunities</h2>
  <div class="oppGrid">
    <!-- Repeat for each opportunity, ranked by frequency × impact -->
    <div class="opp-card" onclick="toggleExpand(this)">
      <div class="opp-rank">#{{RANK}}</div>
      <div class="opp-content">
        <h3>{{OPPORTUNITY_TITLE}}</h3>
        <div class="opp-stats">
          <span class="opp-pct">{{PCT}}% of calls</span>
          <span class="opp-count">{{COUNT}} calls</span>
          <span class="opp-sentiment">Sentiment: {{SENTIMENT}}</span>
        </div>
        <div class="opp-tags">
          <span class="tag tag-{{TAG}}">{{TAG}}</span>
        </div>
      </div>
      <div class="opp-expand" style="display:none">
        <p><strong>Recommendation:</strong> {{RECOMMENDATION}}</p>
        <p><strong>Representative quotes:</strong></p>
        <ul>{{QUOTES}}</ul>
      </div>
    </div>
  </div>

  <!-- Charts Row -->
  <div class="charts-row">
    <div class="chart-card">
      <h3>Category Distribution</h3>
      <canvas id="issueChart"></canvas>
    </div>
    <div class="chart-card">
      <h3>Call Volume Trend</h3>
      <canvas id="volumeChart"></canvas>
    </div>
  </div>
  <div class="charts-row">
    <div class="chart-card">
      <h3>Vehicle Families</h3>
      <canvas id="vehicleChart"></canvas>
    </div>
    <div class="chart-card">
      <h3>Call Types</h3>
      <canvas id="callTypeChart"></canvas>
    </div>
  </div>

  <!-- Call Log Table -->
  <h2 class="section-title">Call Log</h2>
  <div class="table-controls">
    <input type="text" id="searchInput" placeholder="Search calls..." onkeyup="filterTable()">
    <select id="categoryFilter" onchange="filterTable()">
      <option value="">All Categories</option>
      <!-- Dynamic options from data -->
    </select>
  </div>
  <table class="data-table" id="callTable">
    <thead>
      <tr>
        <th onclick="sortTable(0)">Date ↕</th>
        <th onclick="sortTable(1)">Caller ↕</th>
        <th onclick="sortTable(2)">Category ↕</th>
        <th>Tags</th>
        <th onclick="sortTable(4)">Sentiment ↕</th>
        <th>Summary</th>
      </tr>
    </thead>
    <tbody>
      <!-- Populated from DASHBOARD_DATA.calls by JS -->
    </tbody>
  </table>
  <div class="pagination">
    <button onclick="prevPage()">← Previous</button>
    <span id="pageInfo">Page 1 of N</span>
    <button onclick="nextPage()">Next →</button>
  </div>

  <!-- Action Items -->
  <h2 class="section-title">Action Items</h2>
  <div class="action-filters">
    <button class="filter-btn active" onclick="filterActions('all')">All</button>
    <button class="filter-btn" onclick="filterActions('critical')">Critical</button>
    <button class="filter-btn" onclick="filterActions('high')">High</button>
    <button class="filter-btn" onclick="filterActions('quick-win')">Quick Win</button>
    <button class="filter-btn" onclick="filterActions('medium')">Medium</button>
  </div>
  <div class="action-progress">
    <div class="progress-bar"><div class="progress-fill" style="width:{{PCT}}%"></div></div>
    <span>{{DONE}}/{{TOTAL}} completed</span>
  </div>
  <div class="action-list">
    <!-- Repeat for each action item -->
    <div class="action-card priority-{{PRIORITY}}">
      <input type="checkbox" class="action-check">
      <div class="action-content">
        <h4>{{ACTION_TITLE}}</h4>
        <p>{{ACTION_DESCRIPTION}}</p>
        <span class="action-source">From: {{CALL_REF}}</span>
      </div>
      <span class="priority-badge {{PRIORITY}}">{{PRIORITY}}</span>
    </div>
  </div>
</div>

<!-- Import Modal -->
<div class="modal-overlay" id="importModal" style="display:none" onclick="closeModal(event)">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Analyze New Calls</h2>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <div class="drop-zone" id="dropZone">
        <div class="drop-icon">📁</div>
        <p>Drop call recordings or transcripts here</p>
        <p class="drop-hint">Supports MP3, WAV, TXT, CSV</p>
        <button class="btn btn-accent">Browse Files</button>
      </div>
      <p class="modal-note">New calls will be analyzed and the dashboard will update automatically.</p>
    </div>
  </div>
</div>
```

### JavaScript Functions

The page script must include:
- `renderTable(page)` — Populates call log from `DASHBOARD_DATA.calls`, paginated (15 per page).
- `sortTable(colIndex)` — Sorts by column, toggles ascending/descending.
- `filterTable()` — Filters by search text and category dropdown.
- `prevPage()` / `nextPage()` — Pagination navigation.
- `toggleExpand(el)` — Shows/hides opportunity card expanded section.
- `filterActions(priority)` — Filters action items by priority level.
- `openModal()` / `closeModal()` — Import modal show/hide.
- Chart.js initialization for all 4 charts (doughnut for categories, line for volume trend, bar for vehicles, doughnut for call types).

---

## Page 2: Competitor Ad Intelligence (`competitor.html`)

### Data Source
`analysis/competitor-intel.md`

### Body Structure

```
<header class="comp-header">
  <!-- Gradient background using brand dark color -->
  <h1>Competitor Ad Intelligence</h1>
  <p class="subtitle">Competitive analysis from {{TOTAL_CALLS}} customer conversations</p>
  <div class="header-badges">
    <span class="badge">{{COMPETITOR_COUNT}} Competitors Tracked</span>
    <span class="badge">{{DATE_RANGE}}</span>
  </div>
</header>

<div class="container">

  <!-- Competitor Tab Navigation (sticky) -->
  <div class="comp-tabs">
    <!-- One tab per competitor, colored with competitor brand colors -->
    <button class="comp-tab active" onclick="showCompetitor('{{COMP_ID}}')"
            style="--tab-color: {{COMP_COLOR}}">
      {{COMPETITOR_NAME}}
    </button>
    <!-- Repeat for each competitor -->
  </div>

  <!-- Overview Stats Row -->
  <div class="stat-row">
    <div class="stat-card">
      <div class="stat-value">{{TOTAL_MENTIONS}}</div>
      <div class="stat-label">Total Mentions</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{{POSITIVE_PCT}}%</div>
      <div class="stat-label">Positive Sentiment</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{{NEGATIVE_PCT}}%</div>
      <div class="stat-label">Negative Sentiment</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">{{WIN_RATE}}%</div>
      <div class="stat-label">Win Rate vs Brand</div>
    </div>
  </div>

  <!-- Per-Competitor Sections (shown/hidden by tabs) -->
  <div class="comp-section" id="comp-{{COMP_ID}}">

    <!-- Competitor Card Grid -->
    <div class="comp-grid">
      <div class="comp-card" style="border-top: 4px solid {{COMP_COLOR}}">
        <h3>{{COMPETITOR_NAME}}</h3>
        <div class="comp-mention-count">{{MENTIONS}} mentions</div>
        <div class="comp-sentiment-bar">
          <div class="sent-positive" style="width:{{POS_PCT}}%"></div>
          <div class="sent-negative" style="width:{{NEG_PCT}}%"></div>
        </div>
        <h4>What Customers Say</h4>
        <ul class="comp-quotes">
          <li>"{{QUOTE}}" <span class="quote-sentiment {{SENT}}">{{SENT}}</span></li>
        </ul>
        <h4>Messaging Themes</h4>
        <div class="comp-themes">
          <span class="theme-tag">{{THEME}}</span>
        </div>
      </div>
    </div>

    <!-- Counter-Positioning Recommendations -->
    <div class="counter-section">
      <h3>Counter-Positioning: {{BRAND_NAME}} vs {{COMPETITOR_NAME}}</h3>
      <div class="counter-grid">
        <div class="counter-card win">
          <h4>Where {{BRAND_NAME}} Wins</h4>
          <ul>{{WIN_POINTS}}</ul>
        </div>
        <div class="counter-card lose">
          <h4>Where {{COMPETITOR_NAME}} Wins</h4>
          <ul>{{LOSE_POINTS}}</ul>
        </div>
        <div class="counter-card action">
          <h4>Recommended Actions</h4>
          <ul>{{ACTIONS}}</ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Comparison Matrix Table -->
  <h2 class="section-title">Side-by-Side Comparison</h2>
  <table class="matrix-table">
    <thead>
      <tr>
        <th>Dimension</th>
        <th>{{BRAND_NAME}}</th>
        <th>{{COMP_1}}</th>
        <th>{{COMP_2}}</th>
        <!-- etc -->
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{DIMENSION}}</td>
        <td>{{BRAND_RATING}}</td>
        <td>{{COMP_1_RATING}}</td>
        <!-- etc -->
      </tr>
    </tbody>
  </table>

  <!-- Strategic Recommendations -->
  <h2 class="section-title">Strategic Recommendations</h2>
  <div class="rec-grid">
    <div class="rec-card priority-{{PRIORITY}}">
      <div class="rec-number">{{N}}</div>
      <h3>{{REC_TITLE}}</h3>
      <p>{{REC_DESCRIPTION}}</p>
      <div class="rec-impact">Impact: {{IMPACT}}</div>
    </div>
  </div>
</div>
```

### Competitor Brand Colors

Assign colors from known set or auto-assign:

| Competitor | Color |
|-----------|-------|
| SuperATV | `#E8B100` |
| RevZilla | `#FF3300` |
| Four Wheel Parts | `#1A73E8` |
| CageWRX | `#333333` |
| Default palette | `#6366F1`, `#EC4899`, `#14B8A6`, `#F59E0B`, `#8B5CF6` |

### JavaScript Functions

- `showCompetitor(id)` — Tab switching, shows/hides competitor sections.
- Chart.js mention frequency chart (optional bar chart).

---

## Page 3: Site Changes (`site-changes.html`)

### Data Source
`analysis/site-changes.md`

### Body Structure

```
<header class="hero-header">
  <!-- Centered layout with gradient background -->
  <h1>Website Optimization Recommendations</h1>
  <p class="hero-subtitle">Based on {{TOTAL_CALLS}} customer conversations</p>
  <div class="hero-badges">
    <span class="badge">{{REC_COUNT}} Recommendations</span>
    <span class="badge">{{DATE_RANGE}}</span>
  </div>
</header>

<!-- Stats Row (overlaps hero with negative top margin) -->
<div class="stats-row">
  <div class="stat-card">
    <div class="stat-value">{{CALLS_WITH_SITE_ISSUES}}</div>
    <div class="stat-label">Calls Mentioning Website</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{{TOP_ISSUE}}</div>
    <div class="stat-label">Most Common Issue</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{{EST_IMPACT}}</div>
    <div class="stat-label">Estimated Impact</div>
  </div>
</div>

<div class="container">
  <!-- Repeat for each site change recommendation -->

  <div class="change-section">
    <div class="change-number">{{N}}</div>
    <h2 class="change-title">{{CHANGE_TITLE}}</h2>

    <!-- Problem / Solution Grid -->
    <div class="ps-grid">
      <div class="ps-card problem">
        <h3>The Problem</h3>
        <p>{{PROBLEM_DESCRIPTION}}</p>
        <div class="call-count">
          <span class="count-badge">{{CALL_COUNT}} calls</span>
          mentioned this issue
        </div>
        <div class="quotes">
          <blockquote>"{{CUSTOMER_QUOTE}}"</blockquote>
        </div>
      </div>
      <div class="ps-card solution">
        <h3>The Solution</h3>
        <p>{{SOLUTION_DESCRIPTION}}</p>
      </div>
    </div>

    <!-- Competitor Examples -->
    <div class="competitor-examples">
      <h3>How Competitors Handle This</h3>
      <div class="example-grid">
        <div class="example-card">
          <h4>{{COMPETITOR_NAME}}</h4>
          <p>{{WHAT_THEY_DO}}</p>
          <!-- Optional: SVG wireframe mockup of competitor approach -->
          <div class="mockup-preview">
            <svg viewBox="0 0 400 250">
              <!-- Wireframe SVG elements -->
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Proposed Mockup -->
    <div class="mockup-section">
      <h3>Proposed Change</h3>
      <div class="mockup-container">
        <svg viewBox="0 0 800 500" class="wireframe">
          <!-- SVG wireframe of the recommended change -->
          <!-- Use rect, text, line elements to create schematic layouts -->
          <!-- Color scheme: light gray backgrounds, accent color highlights -->
        </svg>
      </div>
    </div>

    <!-- Implementation Card -->
    <div class="impl-card">
      <h3>Implementation</h3>
      <div class="impl-steps">
        <div class="impl-step">
          <span class="step-num">1</span>
          <p>{{STEP_DESCRIPTION}}</p>
        </div>
        <!-- Repeat for each step -->
      </div>
      <div class="impl-badges">
        <span class="impact-badge high">High Impact</span>
        <span class="effort-badge medium">Medium Effort</span>
        <span class="timeline-badge">~{{DAYS}} days</span>
      </div>
    </div>
  </div>

  <!-- Section divider between recommendations -->
  <div class="section-divider"></div>
</div>
```

### SVG Wireframe Guidelines

Mockup SVGs should be schematic, not pixel-perfect:
- Use `rect` for layout blocks (light gray fill `#F0F0F0`, 1px border `#DDD`).
- Use `text` for labels (12-14px, `#666`).
- Use accent color (`#D4782F`) for highlighted/changed elements.
- Use `line` for separators.
- Keep viewBox proportional to a typical web page section.
- Include a legend indicating "Current" vs "Proposed" if showing before/after.

### JavaScript Functions

Minimal JS needed — mostly static content. Optional:
- Smooth scroll between sections.
- Expand/collapse for long quote lists.

---

## Page 4: Customer Journeys (`journeys.html`)

### Data Source
`analysis/customer-journeys.md`

### Body Structure

```
<header class="journey-header">
  <!-- Gradient background -->
  <h1>Customer Journey Intelligence</h1>
  <p class="subtitle">Journey patterns from {{TOTAL_CALLS}} conversations</p>
</header>

<div class="container">

  <!-- Summary Bar -->
  <div class="summary-bar">
    <div class="summary-item">
      <div class="summary-value">{{JOURNEY_COUNT}}</div>
      <div class="summary-label">Journey Patterns</div>
    </div>
    <div class="summary-item">
      <div class="summary-value">{{PERSONA_COUNT}}</div>
      <div class="summary-label">Personas Identified</div>
    </div>
    <div class="summary-item">
      <div class="summary-value">{{FRICTION_COUNT}}</div>
      <div class="summary-label">Friction Points</div>
    </div>
    <div class="summary-item">
      <div class="summary-value">{{OPPORTUNITY_COUNT}}</div>
      <div class="summary-label">Opportunities</div>
    </div>
  </div>

  <!-- Persona Cards -->
  <h2 class="section-title">Customer Personas</h2>
  <div class="persona-grid">
    <div class="persona-card">
      <div class="persona-icon">{{EMOJI}}</div>
      <h3>{{PERSONA_NAME}}</h3>
      <p class="persona-desc">{{DESCRIPTION}}</p>
      <div class="persona-traits">
        <span class="trait">{{TRAIT}}</span>
      </div>
      <div class="persona-stats">
        <span>{{PCT}}% of callers</span>
        <span>Avg sentiment: {{SENTIMENT}}</span>
      </div>
    </div>
  </div>

  <!-- Journey Flowcharts -->
  <h2 class="section-title">Journey Patterns</h2>

  <!-- Repeat for each major journey pattern -->
  <div class="journey-block">
    <div class="journey-header-bar">
      <h3>{{JOURNEY_NAME}}</h3>
      <span class="journey-freq">{{FREQ}}% of customers</span>
    </div>

    <!-- Horizontal Flowchart -->
    <div class="flowchart">
      <!-- Repeat for each stage -->
      <div class="flow-step">
        <div class="step-label">{{STAGE_NAME}}</div>
        <div class="step-detail">{{STAGE_DESCRIPTION}}</div>
        <!-- Pain points at this stage -->
        <div class="step-pain" title="{{PAIN_POINT}}">⚠ {{PAIN_SHORT}}</div>
        <!-- Opportunities at this stage -->
        <div class="step-opp" title="{{OPPORTUNITY}}">💡 {{OPP_SHORT}}</div>
      </div>
      <!-- Arrow connector between steps (CSS ::after pseudo-element) -->
    </div>

    <!-- Page Preview Cards (mini browser mockups) -->
    <div class="preview-grid">
      <div class="page-preview">
        <div class="preview-chrome">
          <span class="preview-dot red"></span>
          <span class="preview-dot yellow"></span>
          <span class="preview-dot green"></span>
          <div class="urlbar">{{PAGE_URL}}</div>
        </div>
        <div class="preview-body">
          <p>{{WHAT_HAPPENS_HERE}}</p>
        </div>
        <div class="preview-label">{{PAGE_NAME}}</div>
      </div>
    </div>
  </div>

  <!-- Journey Insights -->
  <h2 class="section-title">Key Insights</h2>
  <div class="insights-grid">
    <div class="insight-card">
      <div class="insight-icon">{{ICON}}</div>
      <h4>{{INSIGHT_TITLE}}</h4>
      <p>{{INSIGHT_DESCRIPTION}}</p>
    </div>
  </div>

  <!-- Cross-Competitor Journey Comparison -->
  <h2 class="section-title">Journey Comparison</h2>
  <table class="comparison-table">
    <thead>
      <tr>
        <th>Journey Stage</th>
        <th>{{BRAND_NAME}}</th>
        <th>{{COMP_1}}</th>
        <th>{{COMP_2}}</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{STAGE}}</td>
        <td>{{BRAND_EXPERIENCE}}</td>
        <td>{{COMP_1_EXPERIENCE}}</td>
        <td>{{COMP_2_EXPERIENCE}}</td>
      </tr>
    </tbody>
  </table>

  <!-- Recommendations -->
  <h2 class="section-title">Journey Optimization Recommendations</h2>
  <div class="rec-grid">
    <div class="rec-card priority-{{PRIORITY}}">
      <div class="rec-number">{{N}}</div>
      <h3>{{REC_TITLE}}</h3>
      <p>{{REC_DESCRIPTION}}</p>
      <div class="rec-meta">
        <span class="rec-impact">Impact: {{IMPACT}}</span>
        <span class="rec-stage">Stage: {{STAGE}}</span>
      </div>
    </div>
  </div>
</div>
```

### Flowchart CSS Pattern

The horizontal flowchart uses flexbox with arrow connectors:

```css
.flowchart {
  display: flex;
  align-items: flex-start;
  gap: 0;
  overflow-x: auto;
  padding: 2rem 0;
}
.flow-step {
  flex: 0 0 180px;
  background: white;
  border-radius: 12px;
  padding: 1.2rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  position: relative;
  margin-right: 40px;
}
.flow-step::after {
  content: '→';
  position: absolute;
  right: -30px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.5rem;
  color: var(--accent);
}
.flow-step:last-child::after {
  display: none;
}
.flow-step:last-child {
  margin-right: 0;
}
```

### Browser Preview Chrome CSS Pattern

```css
.preview-chrome {
  background: #E8E8E8;
  border-radius: 8px 8px 0 0;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.preview-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.preview-dot.red { background: #FF5F57; }
.preview-dot.yellow { background: #FFBD2E; }
.preview-dot.green { background: #28CA41; }
.urlbar {
  flex: 1;
  background: white;
  border-radius: 4px;
  padding: 4px 8px;
  font-size: 0.75rem;
  color: #666;
  margin-left: 8px;
}
.preview-body {
  background: white;
  padding: 1rem;
  min-height: 80px;
  border: 1px solid #E2D9CF;
  border-top: none;
  border-radius: 0 0 8px 8px;
}
```

### JavaScript Functions

Minimal JS:
- Optional tab/filter for journey patterns.
- Scroll-based animations for flowchart steps.

---

## Netlify Deployment Files

### `_headers`
```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
```

### `_redirects`
```
# SPA-style fallback not needed for static multi-page site
# But redirect root to index
/  /index.html  200
```

---

## Data Interpolation Rules

When generating pages from analysis data:

1. **Counts and percentages**: Calculate from the analysis markdown files. Parse structured sections.
2. **Quotes**: Extract verbatim quotes from raw call files. Limit to 2-3 per section.
3. **Tags**: Use the standard tag vocabulary. Map to CSS classes: `.tag-fitment`, `.tag-stock`, etc.
4. **Sentiment colors**: positive → green, negative → red, neutral → gray, mixed → yellow.
5. **Priority mapping**: critical → red left-border, high → orange, quick-win → teal, medium → blue.
6. **Brand name**: Always read from `brand-context.md`. Fallback: "Customer Intelligence".
7. **Date range**: Extract from the earliest and latest call dates in the raw files.
8. **Charts**: Use Chart.js 4.4.1 from CDN. Initialize after DOM load. Use the design system color palette.
