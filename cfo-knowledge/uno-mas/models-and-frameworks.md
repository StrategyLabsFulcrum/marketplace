# Uno Más Tacos & Tequila — Financial Models & Calculation Logic
*Complete reference for all frameworks built in this project*

---

## Table of Contents

1. [Net Sales Calculation](#1-net-sales-calculation)
2. [Labor % Model — Tip-Adjusted](#2-labor--model--tip-adjusted)
3. [Prime Cost Model](#3-prime-cost-model)
4. [COGS Reconciliation Framework](#4-cogs-reconciliation-framework)
5. [Normalized EBITDA Model](#5-normalized-ebitda-model)
6. [DSCR / SBA Underwriting Model](#6-dscr--sba-underwriting-model)
7. [SBA Loan Consolidation & Cash Flow Model](#7-sba-loan-consolidation--cash-flow-model)
8. [Day-of-Week Performance Framework](#8-day-of-week-performance-framework)
9. [Open Day Average Framework](#9-open-day-average-framework)
10. [Payroll Buckets Framework](#10-payroll-buckets-framework)
11. [Vendor Mapping & Transaction Categorization Framework](#11-vendor-mapping--transaction-categorization-framework)
12. [Catering Allocation Model](#12-catering-allocation-model)
13. [Wednesday Break-Even Framework](#13-wednesday-break-even-framework)
14. [Depreciation Add-Back Framework (SBA)](#14-depreciation-add-back-framework-sba)
15. [Key Thresholds & Flag Rules](#15-key-thresholds--flag-rules)

---

## 1. Net Sales Calculation

**Purpose:** Establish the correct revenue denominator for all percentage-based metrics. All labor %, prime cost %, and COGS % calculations must use net sales, never gross.

### Inputs
- Gross Sales (from Square POS daily export)
- Discounts (comps, voids, promo codes)
- Returns / Refunds

### Calculation
```
Net Sales = Gross Sales − Discounts − Returns
```

### Outputs
- Net Sales per day
- Net Sales per period (week / month / YTD)

### Assumptions
- Source data is Square POS exports for the Monroe location
- Days with Gross Sales ≤ $100 are treated as **closed** days and excluded from operational averages
- Mondays are always excluded (restaurant closed)
- Catering sales are tracked separately; combined with Monroe net sales only when calculating the Monroe + Catering view

### How It's Been Used
- Base denominator for every labor %, COGS %, and prime cost % calculation in this project
- Cross-referenced against Sales Tax Report (Square) to validate monthly net sales figures
- Used to flag anomalous days in day-of-week analysis

---

## 2. Labor % Model — Tip-Adjusted

**Purpose:** Calculate true restaurant-funded labor as a percentage of net sales, stripping out customer-funded tip pass-through that artificially inflates reported labor costs.

### Inputs
- Total Gross Payroll (from Square Payroll exports, Jan–Oct 2025)
- Total Tips Paid Out via Payroll (~$152,000 annualized)
- Net Sales (Monroe only; or Monroe + Catering combined)

### Calculation — Step by Step

**Step 1: Calculate reported labor %**
```
Reported Labor % = Total Gross Payroll ÷ Net Sales × 100
```

**Step 2: Back out tip pass-through**
```
Restaurant-Funded Labor = Total Gross Payroll − Tips Paid Out via Payroll
```

**Step 3: Calculate tip-adjusted labor %**
```
Tip-Adjusted Labor % = Restaurant-Funded Labor ÷ Net Sales × 100
```

**Step 4: Produce dual view**
- View A: Monroe Only → uses Monroe Net Sales as denominator
- View B: Monroe + Catering → adds monthly catering revenue to denominator

### Outputs
- Reported Labor % (before tip adjustment) — for payroll tax / compliance reference
- Tip-Adjusted Labor % Monroe Only — primary operational KPI
- Tip-Adjusted Labor % Monroe + Catering — strategic view showing catering's dilutive benefit to labor %
- Dollar gap between reported and adjusted (the tip pass-through amount)

### Assumptions
- Tip pass-through runs entirely through Square Payroll as wage payments
- Annual tip pass-through estimated at ~$152,000 (~$12,667/month)
- Tips are customer-funded and should not count against restaurant-funded labor targets
- **Maraya Lindo's compensation is included in labor (W-2 employee, not owner-operator)**

### Critical Rule
> Always calculate labor % using **NET SALES**, never gross sales. Always provide **both** Monroe-only and Monroe + Catering views.

### How It's Been Used
- Every monthly P&L version (v5 through v8) uses this framework
- Identified that reported labor % was inflated by ~16 percentage points vs. tip-adjusted
- Used to set realistic labor targets: 25% goal, 30% ceiling (tip-adjusted basis)

---

## 3. Prime Cost Model

**Purpose:** Calculate the combined food + labor cost as a percentage of net sales. The primary operational health metric for a restaurant.

### Inputs
- Food COGS (reconciled — see Model 4)
- Alcohol COGS (Southern Glazer + Columbia Distributors)
- Restaurant-Funded Labor (tip-adjusted — see Model 2)
- Net Sales

### Calculation
```
Prime Cost = Food COGS + Alcohol COGS + Restaurant-Funded Labor

Prime Cost % = Prime Cost ÷ Net Sales × 100
```

### Outputs
- Prime Cost in dollars
- Prime Cost % (target: ≤55%)
- COGS % component (target: 25–30%)
- Labor % component (target: 25%, ceiling 30%)
- Gap to 55% target (positive = over target, negative = buffer)

### Assumptions
- When COGS is not fully reconciled, food cost is estimated at 25–26% based on fast-casual Mexican benchmarks
- Alcohol COGS tracked separately from food COGS but combined for prime cost
- Labor uses tip-adjusted restaurant-funded figure, not gross payroll

### How It's Been Used
- Reported prime cost ~55.3% against 55% target — at the edge of acceptable
- Used to frame the operational improvement case in SBA forecast
- The 55% target is the primary constraint that governs all staffing and purchasing decisions

---

## 4. COGS Reconciliation Framework

**Purpose:** Build a true picture of food and alcohol costs, because QuickBooks alone significantly undercaptures COGS due to miscoding of payments.

### The Problem
QuickBooks GL shows COGS as understated because:
1. US Foods/US Foodservice payments were coded to bank account registers (not COGS expense accounts)
2. AMEX Plum Card and Chase Ink 5273 charges were tracked as liability balances (not categorized expenses)
3. "Smart Food Service" (US Foods Chef's Store — direct pickup) was not always linked to the US Foods vendor total

### Inputs
- QuickBooks GL export (starting point, known to be incomplete)
- Primary Checking account transactions (vendor payments)
- COGS Checking account transactions (dedicated food vendor payments)
- Secondary Checking account transactions
- AMEX Plum Card transactions (full year 2025, categorized)
- Chase Ink 5273 transactions (full year 2025 + Oct–Dec, categorized)
- Vendor mapping JSON files (3 versions: Primary, COGS, Primary+Secondary)

### Calculation — Step by Step

**Step 1: Export all transactions from all 5 sources**
- QB GL (as baseline)
- Primary Checking
- COGS Checking
- AMEX Plum
- Chase 5273

**Step 2: Apply vendor mapping to each transaction**
```
For each transaction:
  1. Normalize vendor string (lowercase, strip punctuation)
  2. Attempt exact match against vendor_mapping.json keys
  3. If no exact match → attempt contains match (vendor tokens appear in description)
  4. Assign category: COGS-Food, COGS-Alcohol, Labor-Payroll, Rent, Utilities, etc.
  5. Flag unmatched as "Needs-Review"
```

**Step 3: Deduplicate across sources**
- Transactions that appear in both QB and bank exports must be identified and counted once
- QB entries that originate from bank feeds will overlap with direct bank exports

**Step 4: Aggregate COGS by sub-category**
```
Food COGS = Sum of all COGS-Food transactions across all 5 sources (deduplicated)
Alcohol COGS = Sum of all COGS-Alcohol transactions across all 5 sources (deduplicated)
Total COGS = Food COGS + Alcohol COGS
```

**Step 5: US Foods consolidation (confirmed by Ramsey)**
```
Total US Foods COGS = "US FOODS" entries + "US FOODSERVICE" entries + "SMART FOOD SERVICE" entries
                    ≈ $246,000 for 2025 (~$20,500/month average)
                    ≈ 82% of total food COGS
```

### COGS Category Taxonomy (from vendor_mapping.json)
| Category | Examples |
|---|---|
| COGS-Food | US Foods, Smart Food Service, Sysco, Charlie's Produce, Cash & Carry, Albertsons, DeLeon Foods |
| COGS-Alcohol | Southern Glazer, Columbia Distributors, Western Beverage, Hayden Beverage, King Beverage, Young's Market, Vehrs, Uprise Brewing |
| COGS (uncategorized) | Triple B Corp / Consolidated Collection |
| Exclude-Revenue | Square Inc Monroe, Square Inc SQ, Deposits |
| Exclude-Transfer | FIB, internal account transfers |
| Labor-Payroll | Square Inc Payroll DD, Square Inc Payr |
| Labor-Payroll Tax | Square Inc Payr Tax |

### Outputs
- True food COGS (reconciled)
- True alcohol COGS (reconciled)
- COGS % of net sales (more accurate than QB alone)
- Uncategorized transaction list for manual review
- Coverage % (mapped transactions / total transactions)

### Assumptions
- Smart Food Service in QB GL = US Foods Chef's Store = same vendor (confirmed by Ramsey)
- No double-counting: QB bank feed transactions are identified and excluded from bank export totals
- The COGS Checking account is used primarily for US Foods and food vendor payments

### How It's Been Used
- Built 3 vendor mapping JSON files (Primary, COGS, Primary+Secondary combined)
- Quantified US Foods at ~$246K / ~82% of food COGS / ~$20,500/month
- Used as the basis for COGS inputs in all P&L versions v5–v8
- Disclosed COGS capture issue proactively to SBA banker

---

## 5. Normalized EBITDA Model

**Purpose:** Calculate the cash-flow-adjusted earnings figure that represents the true earnings power of the business, as would be presented to an SBA lender.

### Critical Rule
> **Normalized EBITDA must always be higher than reported EBITDA.** If it is not, there is a formula error. Non-recurring add-backs only increase EBITDA; they never decrease it.

### Inputs
- Net Income (from reconstructed P&L)
- Interest Expense (MOFI loans + TI loan + credit card interest)
- Taxes (payroll taxes, business taxes)
- Depreciation & Amortization (from Fixed Asset Register)
- Owner-Operator Compensation (Karissa + Thomas — not Maraya Lindo)
- Non-recurring / One-time Expenses (Wonder Building overlap, transition costs)
- Ramsey's management fee / compensation (if paid and not yet deducted)

### Calculation — Step by Step

**Step 1: Start with Net Income**
```
Net Income = Revenue − COGS − Labor − Occupancy − Operating Expenses − Interest − Depreciation
```

**Step 2: Add back to reach EBITDA**
```
EBITDA = Net Income
       + Interest Expense
       + Taxes
       + Depreciation & Amortization
```

**Step 3: Add back owner-related items**
```
EBITDA + Owner-Operator Comp (Karissa)
       + Owner-Operator Comp (Thomas)
       [NOT Maraya Lindo — she is W-2 labor, not an owner]
```

**Step 4: Add back non-recurring items**
```
       + Wonder Building overlap costs (non-recurring, location now closed)
       + One-time transition / legal / restructuring costs
       + Any other documented non-recurring expenses
```

**Step 5: Result = Normalized EBITDA**
```
Normalized EBITDA ≈ $168,850 (as of P&L v8, full-year 2025)
```

### Verification Check
```
IF Normalized EBITDA < Reported EBITDA → FORMULA ERROR
IF Normalized EBITDA > Reported EBITDA → CORRECT (add-backs increased it)
```

### Outputs
- Reported EBITDA (before add-backs)
- Normalized EBITDA (after add-backs)
- Add-back schedule (itemized list with amounts)
- EBITDA margin % (Normalized EBITDA ÷ Net Sales)

### Assumptions
- Owner-operator comp for Karissa and Thomas is included as add-back for SBA purposes
- Maraya Lindo's comp is explicitly **excluded** from add-backs (W-2 employee)
- Wonder Building costs are treated as non-recurring (location permanently closed)
- Depreciation uses MACRS schedules from Fixed Asset Register (QIP = 15-year, equipment = 5-year, FF&E = 7-year)

### Common Errors Corrected in This Project
- **v5 → v6 revision:** Early models were missing rent and management compensation from the cost stack, making them closer to contribution margin than EBITDA. All cost lines must be included before calculating EBITDA, then add-backs applied on top.
- **Add-back sign error:** Adding back owner comp to an already-inflated EBITDA (where comp wasn't deducted) produces double-counting.

### How It's Been Used
- Core output of P&L reconstruction (v5 through v8)
- ~$168,850 Normalized EBITDA is the numerator in the DSCR calculation
- Disclosed to SBA banker with itemized add-back schedule

---

## 6. DSCR / SBA Underwriting Model

**Purpose:** Calculate the Debt Service Coverage Ratio to demonstrate loan repayment capacity to SBA lender. SBA minimum: 1.15× (standard 7(a)); internal lender threshold typically 1.25×+.

### Inputs
- Normalized EBITDA (from Model 5)
- Annual Debt Service on proposed SBA loan (principal + interest)
- Any remaining debt service on non-consolidated obligations

### Calculation — Step by Step

**Step 1: Confirm Normalized EBITDA**
```
Normalized EBITDA = ~$168,850 (2025 reconstructed)
```

**Step 2: Subtract unfunded CapEx reserve**
```
CapEx Reserve = 2–5% of revenue (restaurant industry benchmark)
               ≈ $18,000–$45,000 annually at current revenue levels
Adjusted EBITDA = Normalized EBITDA − CapEx Reserve
```
> Note: In the current model, CapEx reserve was conservatively held low given the recent TI build-out. Lender may require explicit documentation.

**Step 3: Calculate proposed annual debt service**
```
Monthly SBA Payment   = ~$7,000
Annual Debt Service   = $7,000 × 12 = $84,000
```

**Step 4: Calculate DSCR**
```
DSCR = Adjusted EBITDA (or Normalized EBITDA) ÷ Annual Debt Service

DSCR = $168,850 ÷ $84,000 ≈ 2.01×
```

**Step 5: Stress test**
```
DSCR at −15% EBITDA = ($168,850 × 0.85) ÷ $84,000 = 1.71× (still well above 1.25×)
DSCR at −20% EBITDA = ($168,850 × 0.80) ÷ $84,000 = 1.61× (still above threshold)
```

### Outputs
- Base DSCR: ~2.01×
- Stress-tested DSCR (−15%, −20%)
- Coverage cushion above SBA minimum (2.01× vs. 1.15× minimum = 74% buffer)
- Monthly debt service as % of normalized monthly EBITDA

### Assumptions
- SBA loan: ~$550,000 at ~9.11% APR, ~10-year term → ~$7,000/month
- All existing debt (MOFI + TI loan + credit cards) is fully consolidated; no residual debt service post-close
- Normalized EBITDA ~$168,850 is a conservative 2025 figure (Wonder Building year; ongoing business should perform better)
- SBA standard 7(a) minimum DSCR = 1.15×; most preferred lenders require 1.25× internally

### SBA Depreciation Note (from project reference doc)
- All depreciation (MACRS, Section 179, bonus) is added back to net income; method is irrelevant to DSCR
- The real scrutiny is the **unfunded CapEx subtraction** — lenders will model whether the restaurant can sustain operations without significant reinvestment
- Restaurant equipment = 5-year MACRS (Asset Class 57.0); QIP = 15-year; FF&E = 7-year

### How It's Been Used
- Primary output of UnoMas_SBA_Forecast_v3.xlsx
- 2.01× DSCR is the centerpiece of the SBA application narrative
- Used to frame the loan as low-risk for the banker

---

## 7. SBA Loan Consolidation & Cash Flow Model

**Purpose:** Model the before/after cash flow impact of replacing the existing fragmented debt stack with a single SBA term loan.

### Inputs — Current Debt Stack
| Obligation | Balance | Current Monthly Payment | Rate |
|---|---|---|---|
| MOFI Term Loan 1 | ~$220,000 | TBD from schedule | ~varies |
| MOFI Term Loan 2 | ~$120,000 | TBD from schedule | ~varies |
| TI Loan (landlord) | ~$80,000 | ~$2,000+ (estimated) | TBD |
| AMEX Plum Card balance | ~$53,000 | min payment or payoff | high-rate |
| Chase Ink 5273 balance | ~$53,000 | min payment or payoff | high-rate |
| **Total** | **~$526,000** | | |

### Inputs — Proposed SBA Loan
- Loan Amount: ~$550,000
- APR: ~9.11%
- Term: ~10 years (120 months)
- Monthly Payment: ~$7,000

### Calculation — Step by Step

**Step 1: Monthly amortization formula**
```
M = P × [r(1+r)^n] ÷ [(1+r)^n − 1]

Where:
  P = $550,000 (principal)
  r = 9.11% ÷ 12 = 0.7592% monthly rate
  n = 120 months

M ≈ $7,000/month
```

**Step 2: Calculate current total monthly debt service**
```
Current Monthly Debt Service = MOFI 1 payment + MOFI 2 payment + TI loan payment + card minimums
                             ≈ [sum of existing payments]
```

**Step 3: Calculate monthly cash flow relief**
```
Cash Flow Relief = Current Monthly Debt Service − $7,000 (proposed SBA payment)
```

**Step 4: Calculate total interest cost comparison**
```
Total SBA Interest = ($7,000 × 120) − $550,000
                   = $840,000 − $550,000 = $290,000 over 10 years

Total Current Interest = sum of remaining interest across all existing loans
```

**Step 5: Trade-off analysis**
```
IF Cash Flow Relief is significant AND DSCR clears 1.25× AND total interest delta is acceptable
→ SBA consolidation is the correct decision
```

### Outputs
- Monthly cash flow relief (before vs. after)
- Annual debt service before and after
- Total interest cost comparison (10-year horizon)
- DSCR before and after (current debt stack vs. SBA loan)
- Payoff timeline for each existing obligation

### Assumptions
- All 5 obligations (MOFI 1, MOFI 2, TI loan, AMEX, Chase) are fully retired at close
- No prepayment penalties on MOFI loans (verify before close)
- TI loan (~$80K with landlord/MCDC) can be retired; landlord consent may be required
- SBA 7(a) loan, not SBA 504 (no real estate component)
- Higher total interest expense is acceptable trade-off for cash flow simplicity and TI loan elimination

### How It's Been Used
- Primary strategic rationale for the SBA application
- Monthly cash flow relief is the key selling point to Karissa and Thomas
- MOFI amortization schedule (MOFI_Loans_Schedule_2025.xlsx) feeds the current debt service inputs

---

## 8. Day-of-Week Performance Framework

**Purpose:** Identify structural performance patterns by day of week to guide staffing, scheduling, and operational decisions.

### Inputs
- Daily net sales from Square POS (Monroe Sales by Day export, Jan–Sep 2025)
- Daily labor cost from Square Payroll exports
- Day-of-week classification for each date
- Closed day flags (gross ≤ $100 or Monday)

### Calculation — Step by Step

**Step 1: Classify each date**
```
For each date in range:
  IF Monday → Closed (exclude)
  IF Gross Sales ≤ $100 → Closed (exclude)
  ELSE → assign Day_of_Week (Tuesday, Wednesday, ... Sunday)
```

**Step 2: For each day-of-week bucket, calculate averages**
```
Avg_Sales[DOW]    = Sum(Net Sales for all [DOW] in period) ÷ Count([DOW] open days)
Avg_Labor[DOW]    = Sum(Labor Cost for all [DOW] in period) ÷ Count([DOW] open days)
Labor_Pct[DOW]    = Avg_Labor[DOW] ÷ Avg_Sales[DOW] × 100
```

**Step 3: Flag problem days**
```
IF Labor_Pct[DOW] > 30% → ⚠️ Flag
IF Avg_Sales[DOW] < $2,800 → ⚠️ Flag
IF both → 🚨 Critical
```

**Step 4: Rank days by contribution**
```
Day Contribution = Avg_Sales[DOW] × Count([DOW] open days in period)
Days ranked: Saturday > Friday > Sunday > Thursday > Tuesday > Wednesday
```

### Outputs
- Day-of-week table: Avg Sales | Avg Labor | Labor % | Flag status
- Best performing day: Saturday / Friday (~$4,500–$5,500)
- Worst performing day: Wednesday (~$2,219 avg, ~45% labor)
- Period total open days by day-of-week

### Assumptions
- Mondays always excluded (closed)
- Days with ≤$100 gross treated as closed (holiday, emergency closure, etc.)
- Labor assigned to day it was incurred (payroll period alignment may require proration for some analyses)

### Known Findings
| Day | Avg Net Sales | Avg Labor % | Status |
|---|---|---|---|
| Wednesday | ~$2,219 | ~45% | 🚨 Critical |
| Thursday | ~$2,800–$3,200 | ~30–35% | ⚠️ Watch |
| Tuesday | ~$2,500–$3,000 | ~32–38% | ⚠️ Watch |
| Friday | ~$4,500–$5,000 | ~22–26% | ✅ Strong |
| Saturday | ~$4,800–$5,500 | ~20–24% | ✅ Strong |
| Sunday | ~$3,000–$3,800 | ~26–30% | ✅ Acceptable |

### How It's Been Used
- Core finding: Wednesday is structurally unprofitable at current volume
- Identified "two restaurants in one" dynamic: viable weekend vs. challenged mid-week
- Informs staffing decisions: reduce minimum Wednesday crew, evaluate lunch closure

---

## 9. Open Day Average Framework

**Purpose:** Produce a clean average revenue / labor figure that excludes closed days, holidays, and Mondays — giving a true picture of operational performance.

### Inputs
- All daily net sales records for a period
- Day-of-week for each date
- Closed day threshold (gross ≤ $100)

### Calculation
```
Open Days = Count of days in period where:
  - Day ≠ Monday
  - Gross Sales > $100

Average Per Open Day = Total Net Sales ÷ Open Days
Average Labor Per Open Day = Total Labor Cost ÷ Open Days
```

### Outputs
- Open day count for the period
- Average daily net sales (Monroe only)
- Average daily net sales (Monroe + Catering allocation)
- Average daily labor cost
- Average daily labor %

### Assumptions
- Mondays are never included in open day counts regardless of sales
- $100 gross threshold catches partial days, system errors, and holiday closures without manual day-by-day review
- Catering is allocated evenly across open days when computing blended averages (see Model 12)

### How It's Been Used
- Every period analysis report uses this as the primary "how are we performing" metric
- Prevents anomalous closed days from distorting averages and masking trends

---

## 10. Payroll Buckets Framework

**Purpose:** Decompose total payroll into meaningful operational categories to understand true restaurant-funded labor by role type and separate tip pass-through.

### Inputs
- Square Payroll export: Paycheck details by employee (Jan–Oct 2025)
- Employee role / classification (Kitchen, FOH, Management, Owner-Operator)
- Tip amounts paid out via payroll (by employee, by period)

### Calculation — Step by Step

**Step 1: Classify each employee**
```
Bucket A: Kitchen Labor (cooks, prep, dishwashers)
Bucket B: FOH Labor (servers, bartenders, hosts)
Bucket C: Management Labor (hourly/salaried managers, not owners)
Bucket D: Owner-Operator Compensation (Karissa, Thomas)
Bucket E: Tips Paid Out (customer-funded — back out for true labor)
[Maraya Lindo → Bucket C or separate "Exec Chef" line — always W-2 labor, never Bucket D]
```

**Step 2: Calculate restaurant-funded labor by bucket**
```
For each bucket:
  Restaurant-Funded Labor[Bucket] = Gross Wages[Bucket] − Tips Paid[Bucket]
```

**Step 3: Calculate % of net sales for each bucket**
```
Bucket % = Restaurant-Funded Labor[Bucket] ÷ Net Sales × 100
```

**Step 4: Reconcile to total**
```
Total Restaurant-Funded Labor = Sum(Buckets A + B + C + D) − Total Tips
Total Labor % = Total Restaurant-Funded Labor ÷ Net Sales × 100
```

### Outputs
- Labor cost by role bucket ($ and %)
- Tip pass-through total (~$152K annual, ~$12,667/month)
- True restaurant-funded labor % (excluding tips)
- Owner-operator comp as % of revenue (~18–19% for management/owner tier at current volume)
- Sensitivity: labor % impact of $10K/month revenue increase

### Key Finding
At current revenue levels (~$75–90K/month), management-tier labor (owners + managers) alone consumes ~18–19% of revenue. This leaves very limited room for variable (kitchen/FOH) labor within the 30% ceiling. The math only works cleanly at ≥$100K/month.

### Assumptions
- Maraya Lindo classified as W-2 labor in all buckets, never as owner-operator
- Owner-operator comp for Karissa and Thomas is a legitimate add-back for SBA but a real cost for operational analysis
- Tips are verified against Square Payroll tip reports, not estimated

### How It's Been Used
- Built as UnoMas_2025_Payroll_Buckets_v2.xlsx
- Fed labor inputs into all P&L versions v5–v8
- Used to explain the "management cost % sensitivity" finding
- Owner-operator comp amounts flow into EBITDA add-back schedule (Model 5)

---

## 11. Vendor Mapping & Transaction Categorization Framework

**Purpose:** Automate the categorization of bank and card transactions to build a complete picture of expenses across all accounts, compensating for QuickBooks' undercapture.

### Inputs
- Bank/card transaction export (CSV) — columns: date, description/vendor, amount
- vendor_mapping.json — canonical vendor name → expense category dictionary

### Calculation — Step by Step

**Step 1: Normalize vendor string**
```
vendor_normalized = lower(strip_punctuation(description_field))
```

**Step 2: Exact match**
```
IF vendor_normalized in mapping_keys (case-insensitive) → assign category
```

**Step 3: Contains match (if exact fails)**
```
For each mapping_key:
  IF mapping_key tokens appear in vendor_normalized (with flexible spacing/hyphens)
  → assign category
```

**Step 4: Flag unknowns**
```
IF no match found → category = "Needs-Review"
```

**Step 5: Generate outputs**
```
transactions_mapped.csv — all transactions with category column added
transactions_uncategorized.csv — only rows where category is empty
coverage_summary — Total | Mapped | Uncategorized | Coverage %
top_20_unknown_vendors — frequency-ranked list of unmatched vendor strings
```

### Category Taxonomy
| Category | Description |
|---|---|
| COGS-Food | Food vendor purchases |
| COGS-Alcohol | Alcohol/beverage purchases |
| Labor-Payroll | Square payroll direct deposits |
| Labor-Payroll Tax | Square payroll tax payments |
| Rent | Landlord payments (Market Hall, Appfolio) |
| Utilities | Avista, Comcast, Spokane Garbage |
| Marketing | Google, Meta, Canva, Jaden Anderson |
| Technology | Square Weebly, Stratex, Ring, Intuit |
| Operating-Linens | UniFirst, Cintas |
| Operating-Bank Fees | Service charges, overdraft fees |
| Insurance | State Farm |
| Taxes | IRS, WA Dept Revenue, Montana DOR |
| Liability-CC Payment | AMEX, Chase payments (inter-account) |
| Liability-Loan Payment | MCDC loan payment |
| Exclude-Transfer | Inter-account transfers (FIB, internal) |
| Exclude-Revenue | Square sales deposits (revenue, not expense) |
| Needs-Review | Unmatched / requires manual review |

### Three Mapping Files Built
1. `UnoMas_vendor_mapping_Checking_Primary_11_1_25_final.json` — Primary checking only
2. `UnoMas_vendor_mapping_Checking_COGs_11_1_25_final.json` — COGS checking only
3. `UnoMas_vendor_mapping_Checking_Primary-Secondary_11_2_25_final.json` — Combined primary + secondary

### Outputs
- Fully categorized transaction file for each account
- Identified COGS amounts missing from QuickBooks
- Running "Mapping Intake" document for new unknown vendors

### Assumptions
- "Exclude-Revenue" transactions (Square deposits) are stripped from expense totals to avoid double-counting with POS data
- "Exclude-Transfer" transactions are stripped to avoid inflating expenses with inter-account moves
- Smart Food Service = US Foods (confirmed); both map to COGS-Food

### How It's Been Used
- Foundation for the COGS reconciliation (Model 4)
- AMEX and Chase card data categorized using same taxonomy
- Identified vendor categories missing from QB GL entirely

---

## 12. Catering Allocation Model

**Purpose:** Incorporate catering revenue into daily/period analysis even though catering doesn't generate a daily Square POS entry.

### Inputs
- Monthly catering revenue total
- Number of open days in the month (using Open Day Framework from Model 9)

### Calculation
```
Daily Catering Allocation = Monthly Catering Revenue ÷ Open Days in Month
```

For labor % calculations:
```
Combined Net Sales = Monroe Net Sales + Monthly Catering Revenue
Combined Labor % = Restaurant-Funded Labor ÷ Combined Net Sales × 100
```

### Outputs
- Two labor % views side-by-side:
  - Monroe Only: Labor ÷ Monroe Net Sales
  - Monroe + Catering: Labor ÷ (Monroe + Catering Net Sales)
- The catering dilution effect: how much catering reduces the blended labor %

### Assumptions
- Catering revenue currently ~$3,467/month average (~4% of total)
- Catering labor is assumed low-incremental (uses existing staff, no dedicated headcount added yet)
- As catering scales to $8,000+/month, a catering-specific labor allocation should be built out separately

### How It's Been Used
- Every P&L analysis produces both views
- The catering premium is used to motivate scaling: each $1K of catering growth reduces blended labor % by ~0.2–0.3pp at current labor levels

---

## 13. Wednesday Break-Even Framework

**Purpose:** Identify the minimum revenue level at which Wednesday becomes operationally viable, and the staffing model required to achieve it.

### Inputs
- Wednesday fixed labor (minimum staffable crew × hourly rates)
- Wednesday variable labor (additional staff added for volume)
- Wednesday average net sales (~$2,219)
- Labor % target ceiling (30%)

### Calculation

**Step 1: Calculate minimum Wednesday labor cost**
```
Minimum Crew Cost = (Number of required staff) × (avg hourly rate) × (shift hours)
```

**Step 2: Find break-even revenue at target labor %**
```
Break-Even Revenue = Minimum Crew Cost ÷ Target Labor %

Example at 30% target:
  IF minimum Wednesday labor = $750
  Break-Even Revenue = $750 ÷ 0.30 = $2,500

  IF minimum Wednesday labor = $900
  Break-Even Revenue = $900 ÷ 0.30 = $3,000
```

**Step 3: Compare to actual Wednesday average**
```
Gap = Break-Even Revenue − Actual Wednesday Avg Sales
    = $2,500–$3,000 − $2,219 = ~$300–$800 gap
```

**Step 4: Options analysis**
- Option A: Close Wednesday lunch (reduce hours to dinner only)
- Option B: Reduce minimum crew to bring break-even below $2,219
- Option C: Drive Wednesday sales above $2,800 threshold via programming/catering

### Outputs
- Break-even revenue at various labor % targets
- Dollar gap to profitability at current staffing
- Staffing reduction required to break even at current volume

### Assumptions
- Current Wednesday labor ~45% = ~$998 labor on ~$2,219 sales
- Target: reduce to <35% labor (short-term), <30% (medium-term)
- Minimum required staff not yet formally modeled (requires shift-by-shift schedule data)

### How It's Been Used
- Framed the "structurally unprofitable" diagnosis
- Identified as Immediate Priority (0–30 days) in project brief
- Informs the menu change discussion for March

---

## 14. Depreciation Add-Back Framework (SBA)

**Purpose:** Correctly calculate the depreciation add-back for SBA underwriting using restaurant-specific MACRS schedules.

### Asset Classes & Recovery Periods

| Asset Category | IRS Class | MACRS Life | Method |
|---|---|---|---|
| QIP / Leasehold improvements | QIP §168(e)(3)(E)(vii) | 15 years | Straight-line |
| Kitchen equipment, POS hardware | 57.0 | 5 years | 200% Declining Balance |
| FF&E (tables, chairs, booths) | 00.11 | 7 years | 200% Declining Balance |
| Land improvements (parking, patio) | 00.3 | 15 years | 150% Declining Balance |
| General HVAC | Real property | 39 years | Straight-line |

### Calculation
```
Annual Depreciation = Sum of annual depreciation for each asset on the register

For SBA EBITDA:
  EBITDA = Net Income + Interest + Taxes + Depreciation + Amortization
  (All depreciation is added back regardless of MACRS method used)
```

### Collateral Valuation Rule
```
Without appraisal: Equipment collateral value = Net Book Value × 50%
With appraisal:    Equipment collateral value = Orderly Liquidation Value × 80%
```

### Critical SBA Note
The depreciation **method** (MACRS vs. straight-line) has zero effect on DSCR calculation because all depreciation is added back. The real scrutiny is the **unfunded CapEx subtraction** — lenders will ask whether the restaurant can maintain operations without significant cash reinvestment.

```
Recommended CapEx Reserve (restaurant industry) = 2–5% of revenue
At $900K revenue: $18,000–$45,000/year
```

### How It's Been Used
- Fixed Asset Register (UnoMas_Fixed_Asset_Register.xlsx) built to support this add-back
- Depreciation add-back included in Normalized EBITDA calculation (Model 5)
- Reference document in project explains SBA lender treatment in detail

---

## 15. Key Thresholds & Flag Rules

**Purpose:** Decision rules used consistently across all analyses to flag days, periods, or metrics that require attention.

### Daily Flag Rules
| Condition | Flag | Action |
|---|---|---|
| Labor % > 30% | ⚠️ Warning | Review staffing; identify cause |
| Labor % > 40% | 🚨 Critical | Immediate scheduling review |
| Net Sales < $2,800 | ⚠️ Warning | Track pattern; evaluate hours |
| Net Sales < $2,000 | 🚨 Critical | Consider closure / reduced hours |
| Gross Sales ≤ $100 | Closed Day | Exclude from all averages |
| Day = Monday | Closed Day | Exclude always |
| Both labor >30% AND sales <$2,800 | 🚨 Critical | Priority attention |

### Monthly Target Thresholds
| Metric | Target | Warning | Critical |
|---|---|---|---|
| Prime Cost % | ≤55% | 55–58% | >58% |
| Labor % (tip-adjusted) | 25% | 25–30% | >30% |
| COGS % | 25–30% | 30–33% | >33% |
| Catering Revenue | $3,467+ (current) | <$3,000 | <$2,000 |

### DSCR Thresholds (SBA)
| Level | DSCR | Interpretation |
|---|---|---|
| SBA minimum (7(a) >$350K) | 1.15× | Floor — won't be approved below this |
| Practical lender minimum | 1.25× | Most preferred lenders require this |
| Strong approval zone | 1.50× | Fast-track approval |
| Current model | ~2.01× | Comfortable cushion |
| Stress test floor (−20% EBITDA) | ~1.61× | Still well above all thresholds |

### Catering Growth Milestones
| Stage | Monthly Revenue | % of Total (est.) |
|---|---|---|
| Current | ~$3,467 | ~4% |
| Short-term target | $6,000 | ~7% |
| Medium-term target | $8,000 | ~9% |
| Strategic goal | $10,000+ | ~11%+ |

---

*Document compiled: March 2026*
*All figures based on 2025 reconstructed financials for Uno Mas LLC — Monroe Street, Spokane WA*
*Managing Member: Ramsey Pruchnic*
