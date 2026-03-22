# The Great PNW — Financial Models, Formulas & Frameworks
**Extracted:** March 2026
**Source:** Accumulated CFO analysis work, QuickBooks exports, Shopify data, Strategy Labs ad spend data

---

## MODEL INDEX

1. [Marketing Efficiency Ratio (MER) Model](#1-marketing-efficiency-ratio-mer-model)
2. [Contribution Margin (CM) Model](#2-contribution-margin-cm-model)
3. [CM Lookup Table (MER Scenario Model)](#3-cm-lookup-table-mer-scenario-model)
4. [Seasonal Revenue Weighting Model](#4-seasonal-revenue-weighting-model)
5. [Target P&L Structure (Profitability Benchmark)](#5-target-pl-structure-profitability-benchmark)
6. [Wholesale Margin Calculator](#6-wholesale-margin-calculator)
7. [Channel Profitability Framework](#7-channel-profitability-framework)
8. [Retail Store Profitability Model](#8-retail-store-profitability-model)
9. [New vs. Returning Customer Economics Model](#9-new-vs-returning-customer-economics-model)
10. [Advertising Elasticity Testing Protocol](#10-advertising-elasticity-testing-protocol)
11. [COGS Cash-to-Accrual Correction Framework](#11-cogs-cash-to-accrual-correction-framework)
12. [Customer Acquisition Cost (CAC) by Channel](#12-customer-acquisition-cost-cac-by-channel)

---

## 1. Marketing Efficiency Ratio (MER) Model

### Purpose
Measure the overall efficiency of paid media spend at the DTC channel level. MER is the preferred metric over platform-reported ROAS because it captures total blended performance without attribution distortions.

### Formula

```
MER = Net DTC Sales (Online Store) ÷ Strategy Labs Media Spend
```

**Note:** MER uses *net* DTC sales (after returns/discounts), not gross. It uses media spend only (not agency fees) in the denominator. Media spend = the amount billed to ad platforms by Strategy Labs.

### Inputs Required
- Net DTC sales (from Shopify "Online Store" channel, monthly or annual)
- Strategy Labs media spend (from SL monthly billing data)

### How It Works
1. Pull net sales for "Online Store" channel from Shopify exports
2. Pull media spend from Strategy Labs ad spend CSV (monthly totals)
3. Divide: `MER = Net Sales / Media Spend`
4. Track trend over time; declining MER signals rising cost-per-revenue or demand softening

### Historical MER (Calculated from Actual Data)

| Year | Online Store Net Sales | SL Media Spend | MER |
|---|---|---|---|
| 2021 | $746,103 | $146,514 | **5.09x** |
| 2022 | $763,362 | $210,293 | **3.63x** |
| 2023 | $765,491 | $302,840 | **2.53x** |
| 2024 | $743,312 | $234,652 | **3.17x** |
| 2025 | $886,763 | $211,972 | **4.18x** |

**Key interpretation:** MER declined sharply from 2021 to 2023 as media spend grew without proportional DTC revenue growth. The partial recovery in 2024–2025 reflects Q1 spend cuts. MER is NOT the same as ROAS — it's a blended, total-channel efficiency measure.

### Outputs
- Single ratio (e.g., 4.2x means every $1 of media spend generated $4.20 in net DTC sales)
- Trend line showing direction of DTC efficiency
- Input into CM model (MER drives how much margin is left after marketing costs)

### Key Assumptions
- "DTC" is defined as the Shopify "Online Store" channel only (excludes Facebook & Instagram channel, which appears separately)
- Media spend = platform spend billed by Strategy Labs (does NOT include agency fees — those are separate)
- No attribution — this is a blended, top-down metric

### Relationship to Target
- Target MER: implied 6.7x+ at 15% ad spend of $1.8M revenue (i.e., 15% spend → $1.8M / $270K = 6.7x)
- More conservative target (8–10% ad spend at current revenue): MER of 8–10x
- 2025 MER of 4.18x shows gap vs. target but meaningful improvement from 2023 trough

---

## 2. Contribution Margin (CM) Model

### Purpose
Measure the true profitability of the DTC channel after all directly attributable marketing costs, before fixed operating expenses (payroll, rent, etc.).

### Precise Definition
```
CM = Net DTC Sales − COGS − Media Spend − Agency Fees
```

**Critical:** This definition is locked. CM does NOT deduct payroll, rent, or other fixed overhead.

### Component Formulas

```
Net DTC Sales         = Gross DTC Sales − Returns − Discounts
COGS                  = Net DTC Sales × ~0.45  (55% gross margin assumption)
Media Spend           = Net DTC Sales ÷ MER
Agency Fee (DTC)      = Media Spend × 0.20    (Strategy Labs bills 20% of media spend)
Total Marketing Cost  = Media Spend + Agency Fee = Media Spend × 1.20

CM $  = Net DTC Sales − COGS − Media Spend − Agency Fee
CM %  = CM $ ÷ Net DTC Sales
```

### Algebraic Simplification (for scenario modeling)

Substituting the above:
```
CM% = Gross Margin% − (1 + Agency Rate) ÷ MER
CM% = 0.55 − (1.20 ÷ MER)
```

This gives CM% directly from MER, with gross margin and agency rate as fixed inputs.

### CM% at Various MER Levels

| MER | Media % of Sales | Agency % | Total Mkt % | CM% |
|---|---|---|---|---|
| 2.0x | 50.0% | 10.0% | 60.0% | -5.0% |
| 2.5x | 40.0% | 8.0% | 48.0% | 7.0% |
| 3.0x | 33.3% | 6.7% | 40.0% | 15.0% |
| 3.5x | 28.6% | 5.7% | 34.3% | 20.7% |
| 4.0x | 25.0% | 5.0% | 30.0% | 25.0% |
| 4.5x | 22.2% | 4.4% | 26.7% | 28.3% |
| 5.0x | 20.0% | 4.0% | 24.0% | 31.0% |
| 6.0x | 16.7% | 3.3% | 20.0% | 35.0% |
| 8.0x | 12.5% | 2.5% | 15.0% | 40.0% |
| 9.0x | 11.1% | 2.2% | 13.3% | 41.7% |
| 10.0x | 10.0% | 2.0% | 12.0% | 43.0% |

### Inputs Required
- Net DTC sales (Shopify Online Store, net of returns/discounts)
- MER (calculated from Model 1, or target scenario)
- Gross margin % (assumed 55% for DTC; actual 54.9% in 2024)
- Agency rate (20% of media spend for DTC — *not* Amazon billing model)

### Outputs
- CM $ (absolute dollars generated by DTC channel after marketing costs)
- CM % (efficiency of DTC marketing investment)

### Key Assumptions Baked In
- Gross margin = 55% (actual 2024: 54.9%; 2025: 52.6% — monitor this)
- Agency fee = 20% of media spend for DTC (Strategy Labs DTC billing structure)
- Amazon agency fee (10% of gross Amazon sales) is a *separate* billing model — NEVER mix with DTC
- Fixed costs (payroll, rent) are excluded from CM by definition

### Benchmarks
- 2025 baseline CM: ~40% (actual)
- Operating target: 42–44%
- Achievable at 20% MER (MER of 5x) — with a price increase that lifts gross margin

---

## 3. CM Lookup Table (MER Scenario Model)

### Purpose
Given a target monthly CM dollar amount and an MER scenario, determine the required net DTC sales, media spend, agency fees, and total marketing cost. Used for budgeting and goal-setting.

### Inputs Required
- Target CM $ (monthly)
- MER scenario: 25% spend rate (4.0x MER), 30% (3.33x MER), or 35% (2.86x MER)
- Gross margin % (55%)
- Agency rate (20% of media)

### Formula
```
Step 1: CM% = 0.55 − (1.20 ÷ MER)
Step 2: Required Net Sales = Target CM $ ÷ CM%
Step 3: Media Spend = Net Sales ÷ MER
Step 4: Agency Fee = Media Spend × 0.20
Step 5: Total Marketing Cost = Media Spend + Agency Fee
Step 6: COGS = Net Sales × 0.45
Step 7: Verify: CM $ = Net Sales − COGS − Media − Agency
```

### Lookup Tables by Scenario

#### Scenario A: MER 25% of Sales (4.0x MER) → CM% = 25.0%

| Monthly CM Target | Req. Net Sales | Media Spend | Agency Fee | Total Mkt Cost |
|---|---|---|---|---|
| $5,000 | $20,000 | $5,000 | $1,000 | $6,000 |
| $10,000 | $40,000 | $10,000 | $2,000 | $12,000 |
| $15,000 | $60,000 | $15,000 | $3,000 | $18,000 |
| $20,000 | $80,000 | $20,000 | $4,000 | $24,000 |
| $25,000 | $100,000 | $25,000 | $5,000 | $30,000 |
| $30,000 | $120,000 | $30,000 | $6,000 | $36,000 |
| $40,000 | $160,000 | $40,000 | $8,000 | $48,000 |
| $50,000 | $200,000 | $50,000 | $10,000 | $60,000 |

#### Scenario B: MER 30% of Sales (3.33x MER) → CM% = 19.0%

| Monthly CM Target | Req. Net Sales | Media Spend | Agency Fee | Total Mkt Cost |
|---|---|---|---|---|
| $5,000 | $26,316 | $7,895 | $1,579 | $9,474 |
| $10,000 | $52,632 | $15,789 | $3,158 | $18,947 |
| $15,000 | $78,947 | $23,684 | $4,737 | $28,421 |
| $20,000 | $105,263 | $31,579 | $6,316 | $37,895 |
| $25,000 | $131,579 | $39,474 | $7,895 | $47,368 |
| $30,000 | $157,895 | $47,368 | $9,474 | $56,842 |
| $40,000 | $210,526 | $63,158 | $12,632 | $75,789 |
| $50,000 | $263,158 | $78,947 | $15,789 | $94,737 |

#### Scenario C: MER 35% of Sales (2.86x MER) → CM% = 13.0%

| Monthly CM Target | Req. Net Sales | Media Spend | Agency Fee | Total Mkt Cost |
|---|---|---|---|---|
| $5,000 | $38,462 | $13,462 | $2,692 | $16,154 |
| $10,000 | $76,923 | $26,923 | $5,385 | $32,308 |
| $15,000 | $115,385 | $40,385 | $8,077 | $48,462 |
| $20,000 | $153,846 | $53,846 | $10,769 | $64,615 |
| $25,000 | $192,308 | $67,308 | $13,462 | $80,769 |
| $30,000 | $230,769 | $80,769 | $16,154 | $96,923 |
| $40,000 | $307,692 | $107,692 | $21,538 | $129,231 |
| $50,000 | $384,615 | $134,615 | $26,923 | $161,538 |

### How It's Been Used
- To determine if monthly DTC revenue targets are realistic at a given ad spend level
- To show how much CM compression occurs as MER increases (more aggressive spend = lower CM %)
- To set monthly ad budgets backward from a target CM rather than forward from a fixed spend

---

## 4. Seasonal Revenue Weighting Model

### Purpose
Distribute annual ad spend (or revenue) targets across months in a way that reflects actual seasonal demand patterns, rather than equal monthly allocation.

### Inputs Required
- Annual total to distribute (e.g., planned annual media spend, or annual revenue target)
- Monthly weighting factors (derived from historical ad spend data below)

### Data Source
Strategy Labs ad spend data, January 2021 through November 2025 (59 months of actuals).

### Blended Monthly Weights (2021–2024 complete years)

| Month | Weight | Notes |
|---|---|---|
| January | 5.11% | Q1 weakness; lowest spend |
| February | 5.13% | Q1 weakness |
| March | 5.73% | Q1 weakness |
| April | 6.60% | Spring ramp begins |
| May | 11.06% | **Peak spring** — largest non-holiday month |
| June | 10.38% | Strong summer |
| July | 9.02% | Summer |
| August | 7.41% | Mid-summer pullback |
| September | 7.22% | Pre-fall softness |
| October | 8.04% | Holiday ramp begins |
| November | 13.38% | **Peak — holiday season** |
| December | 10.92% | Holiday close |
| **Total** | **100.0%** | |

### Year-by-Year Monthly % Detail (for context / weight refinement)

| Month | 2021 | 2022 | 2023 | 2024 | 2025 (thru Nov) |
|---|---|---|---|---|---|
| Jan | 0.8% | 6.5% | 5.2% | 7.9% | 4.8% |
| Feb | 3.6% | 4.9% | 4.8% | 7.2% | 5.0% |
| Mar | 6.8% | 4.9% | 3.6% | 7.7% | 4.4% |
| Apr | 6.6% | 4.7% | 7.7% | 7.5% | 4.6% |
| May | 11.9% | 13.1% | 9.0% | 10.3% | 17.6% |
| Jun | 10.7% | 8.9% | 10.9% | 11.0% | 9.7% |
| Jul | 6.7% | 7.9% | 9.9% | 11.6% | 13.2% |
| Aug | 9.2% | 8.4% | 5.8% | 6.3% | 11.7% |
| Sep | 9.5% | 7.6% | 6.5% | 5.3% | 10.3% |
| Oct | 9.8% | 7.3% | 9.2% | 5.9% | 6.5% |
| Nov | 14.3% | 14.1% | 15.3% | 9.8% | 12.2% |
| Dec | 10.2% | 11.8% | 12.2% | 9.5% | — |

### How to Apply It

```
Step 1: Set annual target (e.g., $200,000 annual media spend)
Step 2: Multiply by monthly weight
        January allocation = $200,000 × 5.11% = $10,220
        May allocation     = $200,000 × 11.06% = $22,120
        November allocation= $200,000 × 13.38% = $26,760
Step 3: Use monthly allocations as spend targets in budget
Step 4: Apply same weights to revenue targets if modeling monthly revenue
```

### Key Observations
- **November is the highest-spend month** (13.38%) — critical to not underspend here
- **Q1 (Jan–Mar)** represents only 15.97% of annual spend — consistent with structural Q1 weakness
- **May is the biggest non-holiday month** — spring outdoor demand peak
- **2021 January was an anomaly** (0.8%) — business was ramping ad spend that year; weight it lightly
- 2025 showed unusual May spike (17.6%) — not yet in blended weights since 2025 is incomplete

### How It's Been Used
- To build monthly P&L projections from annual targets
- To set monthly DTC revenue expectations in the Excel financial model
- To evaluate whether Q1 ad spend (2025 at ~$30K) is proportionally appropriate

---

## 5. Target P&L Structure (Profitability Benchmark)

### Purpose
Define the expense structure required to achieve a 15% net margin at The Great PNW's current revenue level (~$1.8M). Used to identify gaps vs. actuals and prioritize cost reduction.

### Inputs Required
- Annual revenue (or quarterly equivalent)
- Target net margin: 15%
- Historical 2021 data as the proven profitable baseline

### Target P&L at $1.8M Annual Revenue

| Category | Target % | Target Annual $ | 2024 Actual % | 2024 Actual $ | Gap |
|---|---|---|---|---|---|
| Revenue | 100% | $1,800,000 | 100% | $1,817,135 | — |
| COGS | 45% | $810,000 | 45.1% | $819,120 | ✓ On track |
| **Gross Profit** | **55%** | **$990,000** | **54.9%** | **$998,015** | **✓** |
| Advertising | 8–10% | $144–180K | 20.0% | $363,413 | **-$183K over** |
| Payroll | 15–18% | $270–324K | 20.1% | $365,987 | **-$42K over** |
| Rent | 4–5% | $72–90K | 6.3% | $114,709 | **-$25K over** |
| All Other OpEx | 10–12% | $180–216K | 13.2% | $239,953 | **-$24K over** |
| **Total OpEx** | **40%** | **$720,000** | **59.6%** | **$1,083,062** | **-$363K over** |
| **Net Income** | **15%** | **$270,000** | **-4.7%** | **-$85,045** | **-$355K gap** |

### Quarterly Target (for $450K revenue quarter)

| Line Item | Target $ | Target % |
|---|---|---|
| Revenue | $450,000 | 100% |
| COGS | $202,500 | 45% |
| Gross Profit | $247,500 | 55% |
| Advertising | $36,000–$45,000 | 8–10% |
| Payroll | $67,500–$81,000 | 15–18% |
| Rent | $18,000–$22,500 | 4–5% |
| Other OpEx | $45,000–$54,000 | 10–12% |
| **Net Profit** | **$67,500** | **15%** |

### 2021 Profitable Baseline (Proven Historical Reference)

| Metric | 2021 Value |
|---|---|
| Revenue | $1,958,622 |
| Gross Margin | 52.2% |
| Advertising % | 11.2% ($219K) |
| Payroll % | 14.9% ($291K) |
| Rent % | 2.1% ($40K) |
| Total OpEx % | 36.6% ($716K) |
| Net Margin | **15.2% ($298K)** |

**Critical insight from this framework:** Gross margin is healthy and not the problem. The entire profitability gap (~$355K) comes from operating expense creep, with advertising overspend being the single largest lever.

### Dashboard Thresholds (for ongoing monitoring)

| Metric | Green (Target) | Yellow | Red |
|---|---|---|---|
| Gross Margin | 55%+ | 50–54% | <50% |
| Advertising % | 8–10% | 11–15% | >15% |
| Payroll % | 15–18% | 19–22% | >22% |
| Rent % | 4–5% | 5–7% | >7% |
| Net Margin | 15%+ | 5–14% | <5% |

---

## 6. Wholesale Margin Calculator

### Purpose
Calculate the true effective margin on wholesale sales after the sales rep commission and (for licensed products) royalty payments. Used to evaluate whether wholesale is worth continuing.

### Inputs Required
- Wholesale unit price (= 2x manufacturing cost = 50% of retail price)
- Sales rep commission rate: **10%** of wholesale price
- Royalty rate (licensed products only): **10%** of net wholesale revenue

### Step-by-Step Calculation

#### Standard (Non-Licensed) Wholesale Product
```
Retail Price         = $35.00  (example)
Manufacturing Cost   = $8.75   (25% of retail)
Wholesale Price      = $17.50  (50% of retail = 2x mfg cost)
Sales Commission     = $1.75   (10% of wholesale price)
Net Wholesale Revenue= $15.75
COGS                 = $8.75
Gross Profit         = $7.00
Gross Margin         = $7.00 / $15.75 = 44.4%
```

#### Licensed Product Wholesale (Smokey Bear, Rainier Beer)
```
Retail Price         = $35.00
Manufacturing Cost   = $8.75
Wholesale Price      = $17.50
Sales Commission     = $1.75
Net Wholesale Revenue= $15.75
Royalty (10%)        = $1.575
COGS + Royalty       = $10.325
Gross Profit         = $5.425
Gross Margin         = $5.425 / $15.75 = 34.4%
```

#### Vs. DTC Margin on Same Product
```
Retail/DTC Price     = $35.00
COGS                 = $8.75
Gross Profit         = $26.25
Gross Margin         = 75.0%  (before marketing)
```

### Summary Table

| Channel | Net Revenue | COGS | Royalty | Gross Profit | Gross Margin |
|---|---|---|---|---|---|
| DTC (standard) | $35.00 | $8.75 | — | $26.25 | **75.0%** |
| DTC (licensed) | $35.00 | $8.75 | $3.50 | $22.75 | **65.0%** |
| Wholesale (standard) | $15.75 | $8.75 | — | $7.00 | **44.4%** |
| Wholesale (licensed) | $15.75 | $8.75 | $1.58 | $5.42 | **34.4%** |

### Key Assumption
Commission is 10% of wholesale *price*, paid to external sales rep. This is recorded in Cost of Sales as "Commissions" ($20,722 in 2024; $55,875 in 2025 — 2025 spike reflects wholesale recovery).

### How It's Been Used
- To evaluate whether wholesale channel covers its overhead allocation
- To show that DTC generates 1.7x the gross profit dollars per unit vs. wholesale
- To frame the exit/restructure analysis: Wholesale must either increase prices, increase minimums, or be exited

---

## 7. Channel Profitability Framework

### Purpose
Compare DTC, Wholesale, and Retail store on a gross profit basis, and understand how each channel contributes to (or consumes) operating budget.

### Structure

```
Revenue
  − COGS
  = Gross Profit
  − Channel-direct marketing costs (DTC only: media + agency)
  − Channel-direct commissions (Wholesale only)
  − Channel-direct royalties (Licensed products, all channels)
  = Channel Contribution Margin
  − Allocated fixed costs (payroll, rent — if isolating by channel)
  = Channel Net Contribution
```

### Actual Channel Revenue Data (from Shopify + QuickBooks)

| Year | DTC (Online Store) | Retail POS | Wholesale (QBO) | Draft Orders (Shopify) |
|---|---|---|---|---|
| 2020 | $781,553 | $810 | — | $514,378 |
| 2021 | $746,103 | $48,157 | $114,932 | $722,859 |
| 2022 | $763,362 | $324,103 | $12,500 | $657,968 |
| 2023 | $765,491 | $391,939 | $579,463 | $492,812 |
| 2024 | $743,312 | $427,760 | $350,860 | $297,338 |
| 2025 | $886,763 | $283,920 | $400,428 | $353,233 |

**Note:** "Draft Orders" in Shopify ($353K in 2025) are likely manually entered wholesale orders — this is the identified source of the P&L vs. Shopify revenue discrepancy. Investigating whether Draft Orders overlap with or are separate from QBO Wholesale Sales is an open task.

### Gross Margin by Channel (Approximate)

| Channel | Gross Margin | Notes |
|---|---|---|
| DTC | ~55% | After printing, shipping, COGS allocation |
| Retail/POS | ~55% | Similar product mix to DTC; no online shipping |
| Wholesale (standard) | ~44% | After 10% commission |
| Wholesale (licensed) | ~34% | After commission + royalty |

### Blended Historical Gross Margins (Actual, from QuickBooks)

| Year | Revenue | COGS | Gross Margin % |
|---|---|---|---|
| 2021 | $1,958,622 | $937,059 | 52.2% |
| 2022 | $2,102,559 | $1,181,718 | 43.8% |
| 2023 | $2,150,120 | $1,081,721 | 49.7% |
| 2024 | $1,817,135 | $819,120 | 54.9% |
| 2025 | $1,903,839 | $903,561 | 52.6% |

**2022 was the worst gross margin year** (43.8%) — high wholesale volume + cash-basis COGS distortion both contributed.

---

## 8. Retail Store Profitability Model

### Purpose
Determine whether the downtown Spokane retail store opened in 2023 earns its fixed cost commitment on a standalone basis.

### Direct Costs Attributable to Store
- Store rent: **~$42,000/year** (~$3,500/month)
- Retail staff wages: **TBD** — needs extraction from payroll records (currently blended with corporate payroll)
- Store utilities: portion of total $15K+ annual utilities line

### Revenue Data (Shopify POS Channel, Net Sales)

| Year | Net Sales | Orders | AOV | New Cust | Returning | Ret Rate |
|---|---|---|---|---|---|---|
| 2021 | $48,157 | 1,017 | $47.35 | 850 | 52 | 5.8% |
| 2022 | $324,103 | 7,493 | $43.25 | 4,471 | 515 | 10.3% |
| 2023 | $391,939 | 7,548 | $51.93 | 2,603 | 503 | 16.2% |
| 2024 | $427,760 | 8,030 | $53.27 | 1,790 | 460 | 20.4% |
| 2025 | $283,920 | 5,364 | $52.93 | 1,205 | 426 | 26.1% |

**Note:** QBO shows $464,070 for 2024 POS; Shopify shows $427,760. The ~$36K gap likely reflects taxes or platform fee accounting differences.

### Basic Profitability Calculation

```
Retail Store Net Contribution:
  Revenue (Shopify net)    = $427,760  (2024)
  COGS (~45%)              = $192,492
  Gross Profit             = $235,268  (55%)
  Store rent               = ($42,000)
  Retail staff wages       = TBD
  Store-allocated utilities = TBD
  Net Store Contribution   = $235,268 − $42,000 − wages − utilities
```

At $42K rent alone (before wages), the store generates ~$193K above rent at 55% gross margin. The critical question is how much of the $366–419K annual payroll is attributable to retail staff.

### Key Strategic Insight
- Retail returning customer rate is climbing: 5.8% (2021) → 26.1% (2025)
- This signals the store is building a loyal local customer base
- Store AOV ($52–53) is comparable to online AOV
- Store CAC is structurally lower than online DTC (no paid media required)

### Model Status
Partial — waiting on retail staff wage extraction from payroll records to complete standalone P&L.

---

## 9. New vs. Returning Customer Economics Model

### Purpose
Quantify the cost difference between acquiring new customers vs. reactivating returning customers, and model the compounding revenue impact of improving retention.

### Inputs Required
- New customer count by year (from Shopify Sales CSV, "Online Store" channel)
- Returning customer count by year
- Annual media spend (DTC only)
- Average order value by customer type (if available; otherwise use blended AOV)

### Historical Customer Data (Online Store DTC Channel)

| Year | Net Sales | Orders | New Cust | Returning | Ret Rate | AOV |
|---|---|---|---|---|---|---|
| 2020 | $781,553 | 17,592 | 10,618 | 6,480 | 37.9% | $44.43 |
| 2021 | $746,103 | 14,360 | 7,573 | 6,313 | 45.5% | $51.96 |
| 2022 | $763,362 | 13,598 | 7,640 | 5,534 | 42.0% | $56.14 |
| 2023 | $765,491 | 12,954 | 7,039 | 5,447 | 43.6% | $59.09 |
| 2024 | $743,312 | 11,290 | 6,322 | 4,618 | 42.2% | $65.84 |
| 2025 | $886,763 | 12,086 | 6,800 | 4,889 | 41.8% | $73.37 |

### CAC Calculation (New Customers, DTC)

```
DTC CAC = Media Spend ÷ New Customers Acquired (Online Store)

Year | Media Spend | New Cust | DTC CAC
2021 | $146,514    | 7,573    | $19.35
2022 | $210,293    | 7,640    | $27.53
2023 | $302,840    | 7,039    | $43.03
2024 | $234,652    | 6,322    | $37.12
2025 | $211,972    | 6,800    | $31.17
```

**Key observation:** Despite increasing media spend from 2021 to 2023, new customer acquisition went DOWN. More spend = higher CAC, not more customers. This is evidence of demand saturation at current price/product point.

### Returning Customer Reactivation Cost

Estimated reactivation cost is a fraction of new customer CAC because:
- Email marketing to existing list (near-zero marginal cost)
- Organic/brand search (no paid attribution)
- Repeat purchase driven by product satisfaction, not ad spend

**Rough ratio from industry benchmarks:** Reactivation cost ≈ 5–10% of new customer CAC. At 2024 CAC of $37, reactivation cost ≈ $2–4 per customer.

### Compounding Retention Model (Simplified)

```
If returning customer rate improves from 42% to 48% on same new customer base:
  Additional returning customers per year ≈ 6% × total customers
  Revenue impact = Additional customers × AOV × orders/customer
```

**Key finding:** Modest improvements in returning customer rate, sustained over 3–5 years, generate substantial cumulative revenue — larger than the revenue gains from aggressive new customer acquisition via paid media.

### How It's Been Used
- To argue against unconstrained ad spend growth (CAC rising with spend)
- To prioritize email marketing investment (low cost, high-ROI reactivation)
- To support Upper Left Club (subscription) as a retention lever

---

## 10. Advertising Elasticity Testing Protocol

### Purpose
Determine how much DTC revenue declines when paid media spend is reduced, in order to identify the "safe floor" for ad spend without catastrophic revenue loss.

### Protocol Design

**Hypothesis:** Some portion of DTC revenue is organic (brand search, direct, email, word-of-mouth) and would persist even with significantly reduced paid spend. The test quantifies this.

**Test Structure:**
```
Phase 1 (Baseline): 4 weeks at current spend level
  - Measure: DTC revenue, sessions, new customers, conversion rate
  - Establish: Weekly average baseline metrics

Phase 2 (Reduction): 4 weeks at 50% of current spend
  - Measure: Same metrics
  - Isolate: Impact of spend reduction on each metric

Phase 3 (Analysis): Calculate elasticity
  - Revenue Elasticity = % Change in Revenue ÷ % Change in Spend
  - If elasticity < 1: Revenue declined less than spend (positive leverage)
  - If elasticity > 1: Revenue declined more than spend (negative leverage)
```

**Practical formula:**
```
Elasticity = (ΔRevenue / Revenue) ÷ (ΔSpend / Spend)
Example: If spend drops 50% and revenue drops 20%:
  Elasticity = -20% ÷ -50% = 0.4
  (A 1% spend reduction causes 0.4% revenue decline → positive leverage)
```

### Key Metrics to Track During Test
- Weekly net DTC revenue (Shopify)
- Session count (Shopify analytics)
- New customer acquisitions
- Conversion rate (must hold steady — a drop may indicate creative fatigue, not demand)
- Email revenue (should hold independent of ad spend)

### Practical Context (2025 Natural Experiment)
Q1 2025 ad spend was cut to ~$30K (vs. $54K in Q1 2024 — a ~44% reduction). Comparing Q1 2025 vs. Q1 2024 DTC revenue will approximate the elasticity test naturally. This data exists in the Shopify exports and should be analyzed.

### Assumptions
- Test works best in a stable-demand period (avoid Nov/Dec holiday season)
- Email list and organic channels must remain constant during test
- Creative quality must not change (control for confounders)

### Status
Protocol designed; natural Q1 2025 experiment happened organically; formal test execution pending.

---

## 11. COGS Cash-to-Accrual Correction Framework

### Purpose
Correct the distortion caused by recording inventory purchases as COGS at the time of purchase (cash basis) rather than at the time of sale (accrual basis). This creates months that appear artificially unprofitable (large purchase months) and months that appear artificially profitable (high-sales months with no purchases).

### The Problem

```
Cash basis accounting (current):
  Month of large inventory purchase:
    P&L shows: High COGS → Low or negative gross profit
    Reality: Inventory is an asset; COGS should not be expensed until sold

  Month of high sales from existing inventory:
    P&L shows: Low COGS → High gross profit (no purchase recorded)
    Reality: Those units had real cost that was already expensed in a prior month
```

### Correction Formula

```
Correct COGS for Period =
  Beginning Inventory (at cost)
  + Purchases During Period (at cost)
  − Ending Inventory (at cost)
  = Cost of Goods Actually Sold

Adjustment = Correct Accrual COGS − Cash-Basis COGS (as currently recorded)
```

### Required Data Inputs
- Beginning inventory value (at cost) for period
- Ending inventory value (at cost) for period — ideally from physical count or Shopify inventory
- Purchases during period (already in QuickBooks: "Purchases - Resale Items" + production costs)
- Balance sheet inventory values (available: $76,500 in 2021, $37,936 in 2022, $36,021 in 2023, $101,000 in 2024, $101,000 in 2025)

### Impact Assessment

Balance sheet inventory figures show significant swings:
- 2021 year-end: $76,500
- 2022 year-end: $37,936 (↓$38,564 — means ~$38K more COGS was correct than recorded)
- 2023 year-end: $36,021 (↓$1,915 — minimal distortion this year)
- 2024 year-end: $101,000 (↑$64,979 — means ~$65K LESS COGS was correct than recorded; 2024 net income would be ~$65K worse on accrual basis)
- 2025 year-end: $101,000 (flat — no distortion between years)

### Status
Analysis and correction guide completed. Implementation requires accountant to restate monthly QuickBooks entries.

---

## 12. Customer Acquisition Cost (CAC) by Channel

### Purpose
Compare the true cost to acquire a new customer across DTC online, retail store, and wholesale channels to inform investment priorities.

### Formula

```
CAC (DTC Online) = Annual DTC Media Spend ÷ New Online Customers Acquired

CAC (Retail Store) = (Store Rent + Retail Staff Wages) ÷ New Retail Customers Acquired
                   (No paid media cost — store foot traffic is organic)

CAC (Wholesale) = Sales Rep Commission $ ÷ Estimated New End Customers Reached
                  (This is approximate — wholesale CAC is indirect)
```

### DTC Online CAC (Calculated from Actual Data)

| Year | Media Spend | New Online Customers | DTC CAC |
|---|---|---|---|
| 2021 | $146,514 | 7,573 | **$19.35** |
| 2022 | $210,293 | 7,640 | **$27.53** |
| 2023 | $302,840 | 7,039 | **$43.03** |
| 2024 | $234,652 | 6,322 | **$37.12** |
| 2025 | $211,972 | 6,800 | **$31.17** |

**Trend:** CAC rose 2.2x from 2021 to 2023. Partial recovery in 2024–2025 as spend was reduced. Spending more does not produce proportionally more new customers.

### Retail Store CAC (Estimated)

| Year | New Retail Customers | Direct Store Costs | Estimated Retail CAC |
|---|---|---|---|
| 2022 | 4,471 | ~$42K rent | ~$9.40 (rent only) |
| 2023 | 2,603 | ~$42K rent | ~$16.14 (rent only) |
| 2024 | 1,790 | ~$42K rent | ~$23.46 (rent only) |
| 2025 | 1,205 | ~$42K rent | ~$34.87 (rent only) |

**Note:** Retail CAC uses rent only (wages TBD). Even with retail staff costs added, retail CAC is likely comparable to or better than online CAC — without requiring ongoing paid media.

**Important:** The declining new customer count at the store (4,471 in 2022 → 1,205 in 2025) is offset by rising returning customer rate (10.3% → 26.1%) — the store is maturing into a loyal customer channel, not struggling.

### Channel CAC Comparison (2024, approximate)

| Channel | CAC | Key Driver |
|---|---|---|
| DTC Online | $37.12 | Paid media (rising) |
| Retail Store | ~$23–35 | Rent + staff (no media cost) |
| Wholesale | Indirect | Commission to rep |

### How It's Been Used
- To support keeping the retail store even though it adds fixed cost
- To argue that retail is a structurally cheaper customer acquisition channel than online DTC
- To demonstrate that paid media spend growth has not scaled new customers proportionally

---

## APPENDIX: Key Constants and Rates

| Variable | Value | Notes |
|---|---|---|
| Target Gross Margin | 55% | COGS at 45% of revenue |
| Strategy Labs DTC Agency Rate | 20% of media spend | DTC channel only |
| Strategy Labs Amazon Agency Rate | 10% of gross Amazon sales | Amazon only — separate billing |
| Amazon Referral Fee | 17% flat | Corrected from prior incorrect rate |
| Wholesale Sales Commission | 10% of wholesale price | Paid to external sales rep |
| Licensing Royalty (Smokey Bear, Rainier Beer) | 10% of gross licensed sales | Recorded in COGS |
| Target Net Margin | 15% | Based on 2021 profitable baseline |
| Target Advertising % of Revenue | 8–10% | (2024 actual: 20%) |
| Target Payroll % of Revenue | 15–18% | (2024 actual: 20.1%) |
| Target Total OpEx % of Revenue | 40% | (2024 actual: 59.6%) |
| Retail Store Rent | ~$42,000/year | ~$3,500/month |
| Wholesale Keystone | 2x manufacturing cost | 50% of retail price |
| DTC/Retail Keystone | 4x manufacturing cost | 75% gross margin target |
