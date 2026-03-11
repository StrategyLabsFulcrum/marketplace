# Dashboard Design System

Complete CSS specification for all 4 dashboard pages. Every page must include these styles inline in a `<style>` tag.

## CSS Custom Properties

```css
:root {
  --dark: #1B2A3D;
  --accent: #D4782F;
  --accent-light: #E89B5A;
  --bg: #F5F0EB;
  --card: #FFFFFF;
  --text: #2D3748;
  --text-light: #718096;
  --border: #E2D9CF;
  --green: #38A169;
  --red: #E53E3E;
  --blue: #3182CE;
  --purple: #805AD5;
  --teal: #319795;
  --yellow: #D69E2E;
}
```

## Base Styles

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}
```

## Site Navigation (all pages)

```css
.site-nav {
  background: #0F1A28;
  display: flex;
  align-items: center;
  padding: 0 32px;
  height: 56px;
  gap: 8px;
  position: sticky;
  top: 0;
  z-index: 1000;
}
.nav-brand {
  color: var(--accent);
  font-weight: 700;
  font-size: 1.1rem;
  margin-right: 32px;
  letter-spacing: 0.5px;
}
.nav-link {
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  padding: 16px 16px;
  font-size: 0.9rem;
  font-weight: 500;
  border-bottom: 3px solid transparent;
  transition: all 0.2s;
}
.nav-link:hover { color: #fff; }
.nav-link.active {
  color: #fff;
  border-bottom-color: var(--accent);
}
```

HTML structure for nav:
```html
<nav class="site-nav">
  <span class="nav-brand">{{BRAND_NAME}}</span>
  <a href="index.html" class="nav-link">Call Intelligence</a>
  <a href="competitor.html" class="nav-link">Competitor Intel</a>
  <a href="site-changes.html" class="nav-link">Site Changes</a>
  <a href="journeys.html" class="nav-link">Customer Journeys</a>
</nav>
```

Set `.active` class on the link matching the current page.

## Page Header

```css
.header {
  background: var(--dark);
  color: white;
  padding: 40px 48px 32px;
}
.header h1 { font-size: 2rem; font-weight: 700; margin-bottom: 8px; }
.header .subtitle { color: rgba(255,255,255,0.7); font-size: 1rem; }
.badge {
  display: inline-block;
  background: var(--accent);
  color: white;
  padding: 4px 14px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-left: 12px;
}
```

## KPI Cards

```css
.kpi-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
  padding: 32px 48px;
  margin-top: -20px;
}
.kpi-card {
  background: var(--card);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border: 1px solid var(--border);
}
.kpi-card .label {
  font-size: 0.8rem;
  color: var(--text-light);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}
.kpi-card .value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--dark);
}
.kpi-card .detail {
  font-size: 0.85rem;
  color: var(--text-light);
  margin-top: 4px;
}
```

## Opportunity Cards

```css
.section { padding: 0 48px 40px; }
.section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--dark);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.opp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 20px;
}
.opp-card {
  background: var(--card);
  border-radius: 12px;
  border: 1px solid var(--border);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.opp-header {
  display: flex;
  align-items: center;
  padding: 20px 24px;
  gap: 16px;
  cursor: pointer;
}
.opp-rank {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--accent);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  flex-shrink: 0;
}
.opp-title { font-weight: 600; font-size: 1rem; flex: 1; }
.opp-pct {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent);
}
.opp-body { padding: 0 24px 20px; }
.opp-stats {
  display: flex;
  gap: 24px;
  margin-bottom: 16px;
  font-size: 0.85rem;
  color: var(--text-light);
}
.opp-stats strong { color: var(--text); }
.opp-tags { display: flex; gap: 6px; flex-wrap: wrap; }
.opp-rec {
  background: #F7F4F0;
  border-top: 1px solid var(--border);
  padding: 20px 24px;
  display: none; /* toggled via JS */
}
.opp-rec.show { display: block; }
.opp-rec h4 {
  font-size: 0.85rem;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 8px;
  letter-spacing: 0.5px;
}
```

## Tag System

```css
.tag {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}
.tag-fitment { background: #EBF5FB; color: var(--blue); }
.tag-stock { background: #FDF2E9; color: var(--accent); }
.tag-custom { background: #F4ECF7; color: var(--purple); }
.tag-pricing { background: #E8F8F5; color: var(--teal); }
.tag-install { background: #FEF9E7; color: var(--yellow); }
.tag-info { background: #F0F0F0; color: #666; }
.tag-shipping { background: #E8F5E9; color: var(--green); }
.tag-returns { background: #FFEBEE; color: var(--red); }
.tag-nav { background: #E3F2FD; color: #1565C0; }
.tag-other { background: #F5F5F5; color: #888; }
```

## Charts

```css
.charts-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  padding: 0 48px 40px;
}
.chart-card {
  background: var(--card);
  border-radius: 12px;
  padding: 24px;
  border: 1px solid var(--border);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.chart-card h3 {
  font-size: 1.1rem;
  margin-bottom: 16px;
  color: var(--dark);
}
.chart-container {
  position: relative;
  height: 280px;
}
```

Use Chart.js CDN: `<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>`

Chart color palette order: `var(--accent)`, `var(--blue)`, `var(--green)`, `var(--purple)`, `var(--teal)`, `var(--yellow)`, `var(--red)`.

## Data Table

```css
.table-controls {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
  align-items: center;
}
.search-input {
  padding: 10px 16px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.9rem;
  flex: 1;
  max-width: 300px;
  outline: none;
}
.search-input:focus { border-color: var(--accent); }
.filter-select {
  padding: 10px 16px;
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 0.9rem;
  background: white;
  cursor: pointer;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
.data-table th {
  text-align: left;
  padding: 12px 16px;
  background: #F7F4F0;
  font-weight: 600;
  color: var(--dark);
  border-bottom: 2px solid var(--border);
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}
.data-table th:hover { color: var(--accent); }
.data-table th .sort-icon { margin-left: 4px; opacity: 0.4; }
.data-table th.sorted .sort-icon { opacity: 1; color: var(--accent); }
.data-table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}
.data-table tr:hover { background: rgba(212,120,47,0.04); }
.data-table .expand-btn {
  background: none;
  border: none;
  color: var(--accent);
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 500;
}
.data-table .detail-row { background: #FAFAF8; }
.data-table .detail-row td { padding: 16px 24px; }

.page-nav {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 20px;
}
.page-btn {
  padding: 8px 14px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: white;
  cursor: pointer;
  font-size: 0.85rem;
}
.page-btn.active {
  background: var(--accent);
  color: white;
  border-color: var(--accent);
}
```

## Action Items

```css
.ac-controls {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.ac-filter-btn {
  padding: 8px 16px;
  border: 1px solid var(--border);
  border-radius: 20px;
  background: white;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s;
}
.ac-filter-btn.active,
.ac-filter-btn:hover {
  background: var(--dark);
  color: white;
  border-color: var(--dark);
}

.ac-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 16px;
}
.ac-card {
  background: var(--card);
  border-radius: 12px;
  border: 1px solid var(--border);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.ac-card .priority-bar {
  height: 4px;
}
.ac-card .priority-bar.critical { background: var(--red); }
.ac-card .priority-bar.high { background: var(--accent); }
.ac-card .priority-bar.quick-win { background: var(--green); }
.ac-card .priority-bar.medium { background: var(--blue); }

.ac-card-body {
  padding: 20px 24px;
}
.ac-card-header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
.ac-checkbox {
  width: 20px;
  height: 20px;
  border: 2px solid var(--border);
  border-radius: 4px;
  cursor: pointer;
  flex-shrink: 0;
  margin-top: 2px;
  accent-color: var(--accent);
}
.ac-title { font-weight: 600; flex: 1; }
.ac-priority-badge {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  letter-spacing: 0.5px;
}
.ac-priority-badge.critical { background: #FEE2E2; color: var(--red); }
.ac-priority-badge.high { background: #FFF3E0; color: var(--accent); }
.ac-priority-badge.quick-win { background: #E6F4EA; color: var(--green); }
.ac-priority-badge.medium { background: #E3F2FD; color: var(--blue); }

.ac-meta {
  display: flex;
  gap: 16px;
  margin-top: 12px;
  font-size: 0.8rem;
  color: var(--text-light);
}
.ac-detail {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  display: none;
  font-size: 0.9rem;
  color: var(--text-light);
}
.ac-detail.show { display: block; }
```

## Modal (Import / Upload)

```css
.modal-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  z-index: 2000;
  align-items: center;
  justify-content: center;
}
.modal-overlay.show { display: flex; }
.modal-content {
  background: white;
  border-radius: 16px;
  padding: 40px;
  max-width: 560px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.modal-content h2 { margin-bottom: 8px; color: var(--dark); }
.modal-content .modal-subtitle {
  color: var(--text-light);
  margin-bottom: 24px;
}
.drop-zone {
  border: 2px dashed var(--border);
  border-radius: 12px;
  padding: 48px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
}
.drop-zone:hover {
  border-color: var(--accent);
  background: rgba(212,120,47,0.04);
}
.drop-zone .upload-icon { font-size: 2.5rem; margin-bottom: 12px; }
.drop-zone .upload-text { font-size: 0.95rem; color: var(--text-light); }
.drop-zone .browse-link {
  color: var(--accent);
  font-weight: 600;
  text-decoration: underline;
}
.modal-close {
  margin-top: 16px;
  text-align: right;
}
.modal-close button {
  background: none;
  border: 1px solid var(--border);
  padding: 8px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
}
```

## Hero Header (site-changes, journeys pages)

```css
.hero {
  background: linear-gradient(135deg, var(--dark) 0%, #2C3E50 100%);
  color: white;
  padding: 60px 48px 48px;
  text-align: center;
}
.hero h1 { font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; }
.hero .hero-sub { color: rgba(255,255,255,0.75); font-size: 1.05rem; max-width: 600px; margin: 0 auto; }

.stats-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  padding: 0 48px;
  margin-top: -30px;
  margin-bottom: 40px;
}
.stat-card {
  background: var(--card);
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  border: 1px solid var(--border);
}
.stat-card .stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--dark);
}
.stat-card .stat-label {
  font-size: 0.85rem;
  color: var(--text-light);
  margin-top: 4px;
}
```

## Site Changes Components

```css
.change-section {
  background: var(--card);
  border-radius: 16px;
  padding: 40px;
  margin: 0 48px 40px;
  border: 1px solid var(--border);
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.change-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--accent);
  color: white;
  font-weight: 700;
  margin-right: 12px;
}
.change-title { font-size: 1.4rem; font-weight: 700; color: var(--dark); }

/* Problem / Solution cards */
.ps-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin: 24px 0;
}
.ps-card {
  padding: 20px 24px;
  border-radius: 10px;
  background: #FAFAF8;
}
.ps-card.problem { border-left: 4px solid var(--red); }
.ps-card.solution { border-left: 4px solid var(--green); }
.ps-card h4 {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}
.ps-card.problem h4 { color: var(--red); }
.ps-card.solution h4 { color: var(--green); }

/* Call count badge */
.call-count {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFF3E0;
  color: var(--accent);
  padding: 6px 14px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.85rem;
  margin: 16px 0;
}

/* Competitor examples */
.example-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 20px;
  margin: 24px 0;
}
.example-card {
  background: #FAFAF8;
  border-radius: 10px;
  border: 1px solid var(--border);
  overflow: hidden;
}
.example-card .screenshot-area {
  background: #E8E0D8;
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-light);
  font-size: 0.85rem;
}
.example-card .example-info { padding: 16px 20px; }
.example-card h5 { font-size: 0.95rem; margin-bottom: 6px; }

/* Proposed mockup */
.mockup-section {
  background: var(--card);
  border: 2px dashed var(--accent);
  border-radius: 12px;
  padding: 32px;
  margin: 24px 0;
  text-align: center;
}
.mockup-section h4 {
  color: var(--accent);
  margin-bottom: 16px;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.mockup-svg {
  max-width: 100%;
  border-radius: 8px;
}

/* Implementation card */
.impl-card {
  background: linear-gradient(135deg, var(--dark) 0%, #2C3E50 100%);
  color: white;
  border-radius: 12px;
  padding: 32px;
  margin: 24px 0;
}
.impl-card h4 {
  font-size: 1rem;
  margin-bottom: 16px;
  color: var(--accent-light);
}
.impl-step {
  display: flex;
  gap: 12px;
  margin-bottom: 12px;
  align-items: flex-start;
}
.impl-step-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  color: var(--accent-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.8rem;
  flex-shrink: 0;
}
.impact-badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 16px;
}
.impact-badge.high { background: rgba(232,155,90,0.2); color: var(--accent-light); }
.impact-badge.medium { background: rgba(49,130,206,0.2); color: #63B3ED; }

/* Section dividers */
.section-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 40px 48px;
  position: relative;
}
.section-divider::before {
  content: '';
  position: absolute;
  left: 0; right: 0; top: 50%;
  border-top: 1px solid var(--border);
}
.section-divider .divider-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--bg);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 1;
  font-size: 1.1rem;
}
```

## Competitor Page Components

```css
/* Tab navigation */
.comp-tabs {
  display: flex;
  gap: 4px;
  padding: 0 48px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}
.comp-tab {
  padding: 12px 24px;
  border-radius: 8px 8px 0 0;
  border: 1px solid var(--border);
  border-bottom: none;
  background: white;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s;
}
.comp-tab.active {
  background: var(--dark);
  color: white;
  border-color: var(--dark);
}

/* Competitor sections */
.comp-section { display: none; padding: 0 48px 40px; }
.comp-section.active { display: block; }

/* Comparison table */
.comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  background: var(--card);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border);
}
.comparison-table th {
  background: var(--dark);
  color: white;
  padding: 14px 20px;
  text-align: left;
  font-weight: 600;
}
.comparison-table td {
  padding: 14px 20px;
  border-bottom: 1px solid var(--border);
}
.comparison-table tr:last-child td { border-bottom: none; }
.comparison-table tr:nth-child(even) { background: #FAFAF8; }
```

Competitor brand colors — assign from this palette or use known colors:
- SuperATV: `#E8B100`
- RevZilla: `#FF3300`
- FourWheel / 4 Wheel Parts: `#1A73E8`
- CageWRX: `#333333`
- Default palette for unknown competitors: `#D4782F`, `#3182CE`, `#38A169`, `#805AD5`, `#319795`

## Journey Page Components

```css
/* Persona cards */
.persona-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 0 48px 40px;
}
.persona-card {
  background: var(--card);
  border-radius: 12px;
  padding: 28px;
  border: 1px solid var(--border);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border-top: 4px solid var(--accent);
}
.persona-card h3 { font-size: 1.1rem; margin-bottom: 12px; color: var(--dark); }
.persona-card .persona-desc {
  font-size: 0.9rem;
  color: var(--text-light);
  line-height: 1.6;
}

/* Journey flowcharts */
.journey-flow {
  display: flex;
  align-items: flex-start;
  gap: 0;
  overflow-x: auto;
  padding: 20px 48px;
  margin-bottom: 40px;
}
.journey-stage {
  min-width: 180px;
  text-align: center;
  position: relative;
}
.journey-stage .stage-box {
  background: var(--card);
  border: 2px solid var(--border);
  border-radius: 10px;
  padding: 16px;
  margin-bottom: 12px;
}
.journey-stage .stage-box h4 {
  font-size: 0.85rem;
  color: var(--dark);
  margin-bottom: 4px;
}
.journey-stage .stage-box p {
  font-size: 0.8rem;
  color: var(--text-light);
}
.journey-stage .pain-point {
  background: #FEE2E2;
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 0.75rem;
  color: var(--red);
  margin-top: 8px;
}
.journey-stage .opportunity {
  background: #E6F4EA;
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 0.75rem;
  color: var(--green);
  margin-top: 6px;
}
.journey-arrow {
  display: flex;
  align-items: center;
  padding: 0 4px;
  color: var(--border);
  font-size: 1.5rem;
  margin-top: 20px;
}
```

## Responsive Breakpoints

```css
@media (max-width: 1024px) {
  .kpi-row { grid-template-columns: repeat(3, 1fr); }
  .charts-row { grid-template-columns: 1fr; }
  .ps-grid { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
  .kpi-row { grid-template-columns: repeat(2, 1fr); }
  .opp-grid, .ac-grid { grid-template-columns: 1fr; }
  .header, .section, .stats-row, .change-section { padding-left: 24px; padding-right: 24px; }
  .site-nav { padding: 0 16px; overflow-x: auto; }
}
@media (max-width: 480px) {
  .kpi-row { grid-template-columns: 1fr; }
  .header h1, .hero h1 { font-size: 1.5rem; }
}
```

## Buttons

```css
.btn-primary {
  background: var(--accent);
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s;
}
.btn-primary:hover { background: var(--accent-light); }
.btn-outline {
  background: transparent;
  color: var(--dark);
  border: 1px solid var(--border);
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  font-size: 0.9rem;
}
.btn-outline:hover { border-color: var(--accent); color: var(--accent); }
```

## Recommendation Cards (shared across pages)

```css
.rec-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 20px;
}
.rec-card {
  background: var(--card);
  border-radius: 12px;
  padding: 24px;
  border: 1px solid var(--border);
  border-left: 4px solid var(--accent);
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.rec-card h4 { font-size: 1rem; margin-bottom: 8px; color: var(--dark); }
.rec-card p { font-size: 0.9rem; color: var(--text-light); line-height: 1.6; }
.rec-card .rec-priority {
  margin-top: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}
```
