# Strategy Labs — Financial Models & Calculation Frameworks
**Compiled:** March 2026
**Purpose:** Portable reference for all financial models, formulas, and analytical frameworks built in this CFO engagement

---

## MODEL INDEX

| # | Model Name | Primary Use |
|---|-----------|-------------|
| 1 | QuickBooks Revenue Extraction & Normalization | Clean periodic revenue from raw QB exports |
| 2 | EBITDA / Operating Income Calculation | True profitability from P&L |
| 3 | Normalized EBITDA (Lender/Investor Version) | Adjusted earnings for deals and valuations |
| 4 | Operating Leverage Model | Margin sensitivity to revenue changes |
| 5 | Revenue Run Rate Calculator | Annualized forward projection from recent months |
| 6 | Multi-Scenario Growth Projection Model | Conservative / moderate / upside cases |
| 7 | EBITDA Multiple Valuation Model | Primary valuation methodology |
| 8 | Valuation Bridge (Counter-Appraisal) | Challenge to Griffiths $4.197M appraisal |
| 9 | Griffiths CCF Model (Reconstructed) | Understanding how the appraiser got to $4.197M |
| 10 | VP Equity Promissory Note Model | Seller-financing structure for VP purchases |
| 11 | Distribution Coverage Ratio | Loan serviceability via profit distributions |
| 12 | Bryan Howell Investor Return Model | IRR, MOIC, equity value over time |
| 13 | Cap Table Dilution Model | Pre/post transaction ownership percentages |
| 14 | Client Concentration Calculator | Revenue concentration risk measurement |
| 15 | Monthly CFO Dashboard Framework | Recurring performance monitoring |

---

## MODEL 1 — QuickBooks Revenue Extraction & Normalization

**Purpose:** Extract accurate period revenue from QuickBooks exports that contain an accrual timing artifact ("Services Previous Month") which inflates apparent revenue if double-counted.

### Inputs Required
- QuickBooks P&L export (any period: monthly, quarterly, annual)
- Must include line items: `Services`, `Services (Previous Month)`, `Creative`, `Sales`

### How the Calculation Works
QuickBooks records two revenue lines due to the billing cycle:
- **"Services"** = current month's retainer billing (billed in the period)
- **"Services (Previous Month)"** = deferred prior-month revenue recognized this period

These are **NOT** additive in a single-period view. The correct treatment is:

```
STEP 1 — For cash-basis periodic reporting:
  Period Revenue = Services (Current) + Creative + Sales + Other

STEP 2 — For accrual-basis periodic reporting:
  Period Revenue = Services (Previous Month) + Creative + Sales + Other
  [Because "Services Previous Month" IS the recognized revenue for the period]

STEP 3 — Annual totals reconciliation:
  Full-year Revenue = Total for Income line (QB calculates correctly)
  Do NOT manually sum monthly "Services" + "Services Previous Month" — this double-counts
```

**Practical Rule:** Always use the `Total for Income` row from QuickBooks for any full-period total. Only decompose sub-lines when you need the component breakdown.

### Outputs
- Clean revenue figure by period (month / quarter / year)
- Revenue mix breakdown: recurring services vs. creative vs. project

### Assumptions
- QuickBooks is the system of record; no manual adjustments outside QB
- Accrual basis is more reliable than cash basis for analysis (confirmed by management and CPA)

### How It's Been Used
- Foundation for all historical P&L analysis (2020–2025)
- Used in valuation challenge to prove correct revenue basis
- Used to build the monthly performance table for banker presentations

---

## MODEL 2 — EBITDA / Operating Income Calculation

**Purpose:** Derive true operating profitability from QuickBooks P&L. QuickBooks reports "Net Operating Income" — this is used as the EBITDA proxy since the company carries no material debt and has minimal D&A.

### Inputs Required
- Total Revenue (from Model 1)
- Total Expenses (from QB: sum of Fixed + People + Variable expense categories)
- Depreciation & Amortization (from tax returns or balance sheet — minimal)
- Interest expense (from QB "Interest Expense" line)

### How the Calculation Works

```
Net Operating Income (QB)      = Total Revenue - Total Expenses

EBITDA (approximate)           = Net Operating Income + D&A + Interest Expense

EBITDA Margin                  = EBITDA ÷ Total Revenue

Operating Margin (as reported) = Net Operating Income ÷ Total Revenue
```

**For Strategy Labs specifically:**
- D&A is minimal (no owned real estate, minimal equipment)
- Interest expense is small (~$8K/year in 2024-2025)
- Therefore: **EBITDA ≈ Net Operating Income** — the difference is immaterial for most analyses

### Key Outputs

| Period | Revenue | NOI | NOI Margin |
|--------|---------|-----|------------|
| 2021 | $2,998,233 | $837,699 | 27.9% |
| 2022 | $3,182,561 | $512,754 | 16.1% |
| 2023 | $4,067,931 | $1,214,267 | 29.8% |
| 2024 | $3,935,476 | $558,098 | 14.2% |
| 2025 YTD (Jan–Sep) | $2,916,240 | $431,462 | 14.8% |
| Q4 2025 (reported) | ~$1,230,000 | ~$348,000 | ~28–30% |

### Assumptions
- S-Corporation; no corporate income tax at the entity level (flows to owners)
- Distributions paid are NOT operating expenses — they are equity distributions and do not reduce NOI
- Owner compensation (Ramsey: $135–187K/yr) IS included in expenses

### How It's Been Used
- Primary metric for all valuation work (EBITDA multiple method)
- Monthly performance monitoring
- Basis for EBITDA goal-setting ($1.2M → $2.4M trajectory)

---

## MODEL 3 — Normalized EBITDA (Lender/Investor Version)

**Purpose:** Adjust raw EBITDA for one-time, non-recurring, or extraordinary items to produce a "clean" earnings figure that represents sustainable earning power. Critical for valuations and bank lending.

### Inputs Required
- Raw EBITDA (from Model 2) for each year
- List of known one-time items with dollar amounts

### How the Calculation Works

```
Normalized EBITDA = Raw EBITDA
  + One-time expenses (non-recurring, won't repeat)
  - One-time income (non-recurring, won't repeat)
  + Add back: D&A
  + Add back: Interest expense
  ± Rent normalization (if related-party rent differs from market rate)
  - Capital maintenance (recurring capex proxy)
```

**Specific Adjustments Identified for Strategy Labs:**

| Year | Raw NOI | Adj: IRC §174* | Adj: WA DOR Refund | Adj: Rent | Normalized EBITDA |
|------|---------|----------------|--------------------|-----------|--------------------|
| 2021 | $837,699 | — | — | ($15,000) | ~$823,307 |
| 2022 | $512,754 | — | — | — | ~$512,739 |
| 2023 | $1,214,267 | ($198,964) | — | — | ~$1,015,303 |
| 2024 | $558,098 | ($343,049) | ($168,672) | — | ~$235,608 |
| 2025 YTD | ~$543,762* | — | — | — | ~$552,197 |

*IRC Section 174: Software development costs required to be capitalized/amortized under TCJA (2022–2024). Reversed in 2025 under new law. These deductions temporarily depressed 2023 and 2024 net income — they represent a tax timing issue, not a real economic cost, and are added back in normalized EBITDA.

**Our Counter-Argument to Griffiths (Key Normalization Dispute):**
- Griffiths used a **weighted average cash flow margin of 15.41%** (years 2021–2025)
- Our position: This weights 2024 (6.60% margin) heavily due to the IRC §174 distortion
- Correct normalized margins: 2021 (22%), 2022 (13%), 2023 (20%), **Q4 2025 (28–30%)**
- Correct normalized EBITDA for forward projection: **$1.2M+** (based on Q4 2025 run rate)

### Output
- Single "banker-ready" normalized EBITDA figure per year
- 3-year weighted average normalized EBITDA (preferred by lenders)

### How It's Been Used
- Core input for valuation challenge against Griffiths appraisal
- Used in Bryan Howell investment memo as valuation anchor
- Will be used for RiverBank lending package once Q4 2025 actuals are uploaded

---

## MODEL 4 — Operating Leverage Model

**Purpose:** Quantify how incremental revenue translates to disproportionate profit growth given a largely fixed cost structure.

### Inputs Required
- Monthly fixed expenses (baseline, doesn't change with revenue)
- Monthly variable expenses (changes with revenue — subcontractors, some bonuses)
- Monthly revenue

### How the Calculation Works

```
Fixed Monthly Expenses  ≈ $200,000–$220,000
  (Payroll, rent, software, accounting, insurance)

Variable Monthly Expenses ≈ $50,000–$80,000
  (Subcontractors, travel, variable comp, meals)

Total Monthly Expense ≈ $260,000–$300,000

Break-Even Revenue     = Total Monthly Expenses ÷ (1 - Variable Cost %)
                       ≈ $270,000–$290,000/month

Operating Leverage     = Contribution Margin % ÷ Operating Margin %
                       (High leverage = small revenue increase → large margin increase)

Marginal Profit Rate   = 1 - Variable Cost % as % of Revenue
                       ≈ 70–80¢ profit per $1 of revenue above break-even
```

**Observed Real-World Validation:**

| Month | Revenue | Expenses | NOI | Marginal Observation |
|-------|---------|----------|-----|---------------------|
| Jan 2025 | $309K | $299K | $10K | Near break-even |
| Feb 2025 | $251K | $302K | ($51K) | Below break-even; fixed costs remain |
| May 2025 | $355K | $257K | $97K | +$46K over Jan on +$46K revenue → ~100% marginal |
| June 2025 | $388K | $259K | $129K | Peak profitability; expenses barely moved |

### Output
- Break-even revenue threshold (~$270–290K/month)
- Marginal profit rate above break-even
- Margin forecast at any given revenue level

### Assumptions
- Fixed costs don't flex meaningfully within the current headcount (26 employees)
- Major cost inflection only occurs if headcount grows materially
- The cost structure holds unless a new hire is added

### How It's Been Used
- Explains why Q1 looks weak but Q2/Q4 look exceptional (same cost base, different revenue)
- Used to argue the $4.197M appraisal is backwards-looking and not forward-predictive
- Core of the "run rate" argument: 3 good months ≠ same as 3 bad months

---

## MODEL 5 — Revenue Run Rate Calculator

**Purpose:** Annualize recent performance to produce a current-state revenue figure more accurate than prior-year actuals.

### Inputs Required
- Most recent N months of revenue (typically 3 months = one quarter)
- Or single most recent month

### How the Calculation Works

```
Quarterly Run Rate  = Most Recent Quarter Revenue × 4

Monthly Run Rate    = Most Recent Month Revenue × 12

Blended Run Rate    = Average of (Last 3 Months Revenue) × 12

Preferred Method    = Q4 Run Rate (captures seasonality peak and validates model)
```

**Current Calculations:**
```
Q4 2025 Revenue    = ~$1,230,000
Q4 2025 Run Rate   = $1,230,000 × 4 = $4,920,000

Preferred Forward Run Rate = $4.9M–$5.5M (using Q4 2025 as base)

Jan–Feb 2026 Monthly Avg = ~$315,000
Jan–Feb 2026 Run Rate    = $315,000 × 12 = $3,780,000
  (Note: seasonally soft; not representative of full year)
```

### Output
- Annualized revenue figure for any period
- Comparison to prior year actuals to show growth trajectory

### Assumptions
- Q4 is representative of the "at scale" performance — not an anomaly
- January/February are structurally soft; don't annualize them for forward projections
- Use Q4 as the "ceiling" and Jan/Feb as the "floor" — annual average falls between

### How It's Been Used
- Establishing "$5.5M run rate" claim in investor and banker materials
- Countering the Griffiths appraisal which used a $4.80M forward revenue estimate (below actual Q4 run rate)

---

## MODEL 6 — Multi-Scenario Growth Projection Model

**Purpose:** Project revenue, EBITDA, and implied valuation across three scenarios over a 5-year horizon.

### Inputs Required
- Base year revenue (2025 actual, ~$5.5M)
- Base year EBITDA margin (target: 28–30%)
- Growth rate assumption per scenario
- EBITDA margin assumption per scenario
- Valuation multiple assumption (typically 10x EBITDA)

### How the Calculation Works

```
Revenue(Year N)  = Revenue(Year N-1) × (1 + Growth Rate)
EBITDA(Year N)   = Revenue(Year N) × EBITDA Margin %
Valuation(Year N)= EBITDA(Year N) × Multiple
```

### Three Scenarios (From Bryan Howell Proposal)

**Conservative Case (15% Growth / 25% Margin)**

| Year | Revenue | EBITDA | Valuation @10x |
|------|---------|--------|----------------|
| 2026 | $4.8M | $1.20M | $12.0M |
| 2027 | $5.5M | $1.38M | $13.8M |
| 2028 | $6.3M | $1.58M | $15.8M |
| 2029 | $7.3M | $1.83M | $18.3M |
| 2030 | $8.4M | $2.10M | $21.0M |

**Internal EBITDA Goal Case (Internal targets, 15% growth)**

| Year | EBITDA Target |
|------|--------------|
| 2026 | $1,200,000 |
| 2027 | $1,380,000 |
| 2028 | $1,587,000 |
| 2029 | $1,825,050 |
| 2030 | $2,098,807 |
| 2031 | $2,413,629 |

*Implied growth rate: ~15% annually on EBITDA*

**Upside Case (20% Growth / 30% Margin)**

| Year | Revenue | EBITDA | Valuation @10x |
|------|---------|--------|----------------|
| 2030 | $10.5M | $3.15M | $31.5M+ |

### Outputs
- Revenue, EBITDA, and valuation table by year per scenario
- Bryan's equity value per year (20% × Valuation)
- VP equity value per year (5% × Valuation per VP)

### Assumptions
- Growth rates are compounding (applied to prior year's revenue, not base year)
- EBITDA margin is applied to top-line revenue (no separate expense modeling in this version)
- Valuation multiple held constant at 10x (conservative; premium agencies trade 10–12x)
- No new capital required to achieve growth (organic growth from existing client base)

### How It's Been Used
- Bryan Howell investment memo (primary returns table)
- VP equity program pitch materials
- Board-level strategic planning reference
- Valuation defense: "Even at 10x conservative case, $8M is well-supported by 2026 forward EBITDA"

---

## MODEL 7 — EBITDA Multiple Valuation Model

**Purpose:** Primary valuation methodology for all equity transactions at Strategy Labs.

### Inputs Required
- Normalized EBITDA (from Model 3) — choose which year(s) to use
- Appropriate EBITDA multiple range (based on industry benchmarks)
- Any premium/discount adjustments

### How the Calculation Works

```
Enterprise Value = Normalized EBITDA × Multiple

Valuation Range  = Normalized EBITDA × (Low Multiple) to Normalized EBITDA × (High Multiple)
```

**Benchmark Multiple Framework:**

| Company Type | Multiple Range | Rationale |
|-------------|---------------|-----------|
| Average digital marketing agency | 8–10x | Standard market |
| Premium agency (95% recurring, >25% margins) | 10–12x | Quality premium |
| SaaS / software company | 4–5x ARR | Comparable if valued as ARR |
| Strategy Labs justified range | 10–11x | Premium justified by recurring rev + margins |

**Valuation Calculations at Different EBITDA Anchors:**

| EBITDA Basis | Amount | @ 8x | @ 10x | @ 12x |
|-------------|--------|------|-------|-------|
| 2023 Actual | $1,214,267 | $9.7M | $12.1M | $14.6M |
| 2025 Target | $1,200,000 | $9.6M | $12.0M | $14.4M |
| Q4 2025 Annualized | ~$1,392,000 | $11.1M | $13.9M | $16.7M |
| Griffiths Normalized | $762,000 | $6.1M | $7.6M | $9.1M |
| Our Normalized (corrected) | $1,100,000+ | $8.8M | $11.0M | $13.2M |

**Per-Unit Price for Equity Transactions:**
```
Price per 1% = Enterprise Value ÷ 100
Price per 5% = Enterprise Value × 5%
Price per 20% = Enterprise Value × 20%

At $8M valuation:
  1% = $80,000
  5% (each VP) = $400,000
  20% (Bryan) = $1,600,000

At $12.5M valuation:
  1% = $125,000
  5% = $625,000
  20% (Bryan) = $2,500,000
```

### Output
- Point estimate or range of enterprise value
- Per-percentage-point equity price
- Valuation at various multiples (sensitivity table)

### Assumptions
- No material long-term debt (enterprise value ≈ equity value)
- S-Corp structure; no corporate tax applies to the entity value calculation
- No minority discount applies to Bryan (strategic partner) — supported by governance rights and distributions history
- EBITDA multiple is appropriate because cash flows are the primary value driver

### How It's Been Used
- Set VP transaction price at $8M ($400K per 5% block)
- Set Bryan Howell transaction price at $12.5M ($2.5M for 20%)
- Counter-argument to Griffiths $4.197M: our multiple range produces $8M–$12M+

---

## MODEL 8 — Valuation Bridge (Counter-Appraisal Framework)

**Purpose:** Quantify the specific adjustments that move from the Griffiths $4.197M appraisal to the correct $8M+ fair value. Each line item is a documented, defensible argument.

### Inputs Required
- Griffiths appraisal methodology and assumptions (from the January 5, 2026 report)
- Actual company financial data (Q4 2025 actuals, corrected margins)
- Industry data on recurring revenue premiums

### How the Calculation Works (Bridge Structure)

```
Griffiths Starting Value:                       $4,197,000

Adjustment 1: Correct Margin Assumption
  Griffiths used: 15.41% weighted avg margin
  Actual Q4 2025 margin: 28–30%
  Correct forward EBITDA: $1.2M vs. Griffiths' $762K
  Value impact (÷ same 22.09% cap rate):       +$1,994,000

Adjustment 2: Correct Revenue Forecast
  Griffiths used: $4.80M (management projection)
  Actual Q4 2025 run rate: $4.92M–$5.5M
  Value impact (incremental revenue × margin):  +$200,000–$400,000

Adjustment 3: Recurring Revenue Premium
  Griffiths applied: 0% premium for 95% recurring
  Market evidence: 95% recurring agencies trade at 10–12x vs. 8x avg
  Premium value:                                +$800,000–$1,600,000

Adjustment 4: IRC §174 Distortion
  2024 margins artificially depressed by $343K
  Griffiths weighted this year in the average
  Corrected weight reduces downward bias:        +$300,000–$500,000

Adjustment 5: Comparable Transaction Weight
  Griffiths relied on Jason Wilson's $200K / 5% transaction
  Implied $4.0M valuation — based on 2022 price (stale)
  Q4 2025 performance makes this anchor obsolete: +$800,000

CORRECTED VALUE RANGE:                          $8.0M–$10.0M
```

### Output
- Line-by-line valuation bridge table
- Corrected value range: $8M–$10M
- Recommended formal challenge document structure (27 questions addressed)

### Assumptions
- Capitalization rate (22.09% from Griffiths) is accepted; we dispute the earnings base, not the rate
- Market multiples research (First Page Sage, Agencies.co, Raincatcher) supports 10–12x premium
- IRC §174 normalization is standard practice; appraiser could have applied it

### How It's Been Used
- Formal written challenge response to Griffiths, Dreher & Evans (27 questions)
- Banker presentation to explain the valuation gap
- Will be resubmitted with Q4 2025 actuals as the anchor

---

## MODEL 9 — Griffiths CCF Model (Reconstructed for Counter-Analysis)

**Purpose:** Fully understand how Griffiths arrived at $4.197M in order to attack the specific inputs that are wrong. This is their model — reconstructed from the appraisal report.

### Their Methodology: Capitalization of Cash Flows (CCF)

```
STEP 1 — Calculate After-Tax Free Cash Flow per year:
  Net Income Per Books
  + Adj #1: Owner's Compensation (no adjustment made)
  + Adj #2: Payroll Taxes (no adjustment)
  + Adj #3: Discretionary/One-Time Expenses
  + Adj #4: Rent Normalization
  + Adj #5: Interest (add back)
  + Adj #6: IRC §174 (pre-tax deduction, added back)
  = Before-Tax Normalized Net Income
  × (1 - Tax Rate of ~21%)
  = Normalized Net Income After Tax
  + Adj #7: IRC §174 Post-Tax
  + Adj #8: D&A (add back)
  - Adj #9: Capital Maintenance ($7,345/year)
  = After-Tax Free Cash Flow to MVIC

STEP 2 — Weight the years:
  2021: Weight 1   (22.34% FCF/Sales)
  2022: Weight 2   (12.85%)
  2023: Weight 3   (20.12%)
  2024: Weight 1   (6.60%) ← heavily penalized by IRC §174
  2025 YTD: Weight 3 (13.02%) ← partial year, underweights strong H2
  Weighted Average:  15.41%

STEP 3 — Apply to forecasted revenue:
  Forecasted Revenue = $4,944,000
  × 15.41% = $762,000 projected After-Tax FCF

STEP 4 — Capitalize:
  Cap Rate = 22.09% (Duff & Phelps Build-Up Method: 25.09% cost of equity - 3% long-term growth)
  Value = $762,000 ÷ 22.09% = $3,450,000 (income approach)

STEP 5 — Market Approach:
  Used Jason Wilson's $200K / 5% transaction (Jan 1, 2025) → $3,992,000 implied value
  Applied forward revenue multiple: 0.98x × $4,845,000 forecasted = ~$4,750,000

STEP 6 — Synthesis:
  Income Approach: $3,450,000
  Market Approach: ~$4,750,000
  Weighted conclusion: $4,197,000
```

### Where the Model Is Attackable
1. **Weighted average margin:** 2024 is catastrophically understated (6.60%) due to IRC §174 — a timing issue, not an economic one. Weighting it equally with 2023 (20%) destroys the average.
2. **2025 partial year:** Only Jan–Oct 2025 included. Missing Oct–Dec 2025 which were the strongest months in company history (28–30% margins).
3. **Forecasted revenue:** Griffiths used $4.80M management projection. Actual Q4 2025 run rate exceeds this.
4. **Jason Wilson transaction anchor:** Used a 2022-era pricing calculation. Acknowledged to be "calculated as of his hire date (April 11, 2022)" — effectively a 3-year-old price.

---

## MODEL 10 — VP Equity Promissory Note Model

**Purpose:** Structure seller financing for VP equity purchases that (1) doesn't require third-party appraisal, (2) produces manageable monthly payments, and (3) is covered by the VP's own profit distributions.

### Inputs Required
- Purchase price per VP: $400,000 (5% of $8M valuation)
- Loan term: 15 years (180 months)
- Interest rate: 6% annually (0.5% monthly)
- Down payment: $0 (full financed, or negotiable)

### How the Calculation Works

**Standard Amortizing Loan Formula:**
```
M = P × [r(1+r)^n] ÷ [(1+r)^n - 1]

Where:
  M = Monthly payment
  P = Principal ($400,000)
  r = Monthly interest rate (6% ÷ 12 = 0.5% = 0.005)
  n = Number of payments (15 × 12 = 180)

Calculation:
  M = 400,000 × [0.005 × (1.005)^180] ÷ [(1.005)^180 - 1]
  M = 400,000 × [0.005 × 2.4540] ÷ [2.4540 - 1]
  M = 400,000 × [0.01227] ÷ [1.4540]
  M = 400,000 × 0.008439
  M ≈ $2,953/month per VP
```

**Total cost of financing:**
```
Total Paid     = $2,953 × 180 = $531,540
Total Interest = $531,540 - $400,000 = $131,540
Effective Cost = 32.9% premium over purchase price (over 15 years)
```

**Amortization Schedule (Key Milestones):**

| Period | Payment | Principal | Interest | Balance |
|--------|---------|-----------|----------|---------|
| Month 1 | $2,953 | $953 | $2,000 | $399,047 |
| Year 1 end | $2,953/mo | ~$11,700 | ~$23,700 | ~$388,300 |
| Year 5 end | $2,953/mo | ~$71,000 | ~$106,100 | ~$329,000 |
| Year 10 end | $2,953/mo | ~$174,000 | ~$181,000 | ~$226,000 |
| Year 15 end | $2,953/mo | ~$400,000 total | ~$131,500 total | $0 |

### Output
- Monthly payment: **$2,953/VP**
- Total for all 3 VPs simultaneously: **$8,859/month**
- Total interest paid per VP over term: ~$131,540

### Assumptions
- No prepayment penalties (VPs may pay off early if desired)
- Interest rate: 6% (reasonable for related-party seller financing; below bank rates for illiquid assets)
- 15-year term chosen to maximize cash flow cover ratio (see Model 11)
- Payments begin immediately upon closing

### How It's Been Used
- Primary financing structure for VP equity program
- Presented to RiverBank as alternative to traditional bank loan
- Used to demonstrate payments are easily covered by distributions

---

## MODEL 11 — Distribution Coverage Ratio

**Purpose:** Prove that each VP's loan payment ($2,953/month) is comfortably covered by the profit distributions they receive as equity holders — making the loans self-liquidating.

### Inputs Required
- Company EBITDA (annual or monthly)
- VP ownership percentage: 5%
- VP monthly loan payment: $2,953
- Distribution policy: quarterly (or as available)

### How the Calculation Works

```
Annual EBITDA                    = Variable (use scenario)
VP Annual Distribution (5%)      = Annual EBITDA × 5%
VP Monthly Distribution Equivalent = VP Annual Distribution ÷ 12
VP Monthly Loan Payment          = $2,953

Coverage Ratio                   = VP Monthly Distribution ÷ VP Monthly Payment
                                 = (Annual EBITDA × 5% ÷ 12) ÷ $2,953
```

**Coverage at Key EBITDA Levels:**

| Annual EBITDA | 5% Distribution | Monthly Equiv. | Monthly Payment | Coverage Ratio |
|--------------|-----------------|----------------|-----------------|---------------|
| $600,000 | $30,000 | $2,500 | $2,953 | 0.85× ❌ |
| $750,000 | $37,500 | $3,125 | $2,953 | 1.06× ✅ |
| $900,000 | $45,000 | $3,750 | $2,953 | 1.27× ✅ |
| $1,200,000 | $60,000 | $5,000 | $2,953 | 1.69× ✅ |
| $1,400,000 | $70,000 | $5,833 | $2,953 | 1.97× ✅ |

**Break-Even EBITDA for Coverage:**
```
Minimum EBITDA for 1.0× coverage = ($2,953 × 12) ÷ 5%
                                  = $35,436 ÷ 0.05
                                  = $708,720/year

At 2025 target EBITDA ($1.2M):
  Coverage = $60,000 annual distribution ÷ $35,436 annual payment = 1.69×
  VP retains: $60,000 - $35,436 = $24,564/year net after loan service
```

### Output
- Coverage ratio by EBITDA scenario
- Minimum EBITDA threshold for loan serviceability: **$708,720**
- Net annual benefit to each VP after loan payment at target EBITDA

### Assumptions
- Distributions are actually paid (company has historically paid distributions — $790K in 2021, $764K in 2022, $990K in 2023, $391K in 2024)
- 100% of net income available for distribution (S-Corp, all passes through)
- No bank covenant restricts distributions
- EBITDA = distributable cash (minimal D&A, no debt service at company level)

### How It's Been Used
- Core argument in RiverBank loan package
- Demonstrates self-liquidating structure to any lender or skeptic
- Shows VPs this isn't a financial burden — it's largely self-funding

---

## MODEL 12 — Bryan Howell Investor Return Model

**Purpose:** Project total return (cash distributions + equity appreciation) for Bryan's $2.5M investment in Strategy Labs over a 5-year horizon.

### Inputs Required
- Investment: $2.5M for 20% equity at $12.5M pre-money valuation
- Annual EBITDA growth rate (15% conservative, 20% upside)
- EBITDA margin on revenue
- Distribution rate: % of EBITDA paid out annually
- Exit multiple: 10x EBITDA at sale/liquidity event

### How the Calculation Works

```
Year 0:
  Bryan invests: $2,500,000
  Implied valuation: $12,500,000
  Bryan's stake: 20%

Each Year:
  Revenue(N)       = Revenue(N-1) × (1 + growth rate)
  EBITDA(N)        = Revenue(N) × EBITDA margin
  Distributions(N) = EBITDA(N) × distribution rate × 20%
  Equity Value(N)  = EBITDA(N) × exit multiple × 20%
  Total Return(N)  = Cumulative Distributions + Equity Value(N)
  MOIC(N)          = Total Return(N) ÷ $2,500,000
```

**Return Table (Conservative: 15% growth, 25% margin, 100% distribution of EBITDA):**

| Year | EBITDA | Bryan Annual Dist. | Cumulative Dist. | Equity Value | Total Return | MOIC |
|------|--------|-------------------|------------------|--------------|--------------|------|
| 2026 | $1.20M | $240,000 | $240,000 | $2.40M | $2.64M | 1.06× |
| 2027 | $1.38M | $276,000 | $516,000 | $2.76M | $3.28M | 1.31× |
| 2028 | $1.59M | $317,400 | $833,400 | $3.17M | $4.01M | 1.60× |
| 2029 | $1.82M | $365,010 | $1,198,410 | $3.65M | $4.85M | 1.94× |
| 2030 | $2.10M | $419,761 | $1,618,172 | $4.20M | $5.82M | 2.33× |
| 2031 | $2.41M | $482,726 | $2,100,898 | $4.82M | $6.92M | 2.77× |

**Key Return Metrics:**
```
IRR (conservative case):    23–26% annually
Cash Payback Period:        ~6 years from distributions alone
5-Year MOIC:               ~2.3×
6-Year MOIC:               ~2.8×

Cash Payback Check:
  Cumulative distributions reach $2.5M in approximately year 8–9
  But equity value alone exceeds investment by year 3
```

### Output
- Annual and cumulative distribution table
- Equity value by year at assumed exit multiple
- IRR and MOIC summary
- Comparison to alternatives (PE funds, market returns)

### Assumptions
- 100% of EBITDA paid as distributions (S-Corp pass-through; historically confirmed: $990K paid in 2023)
- Exit multiple held at 10x (conservative; could be 11–12x for premium agency at scale)
- No dilutive events during the projection period
- Bryan's $1.2M DPP contract continues — if lost, returns decline; if secured by contract, returns are enhanced

### How It's Been Used
- Primary investor pitch for Bryan Howell
- Return table included in `Proposal_for_Bryan.pdf`
- Anchor for the strategic premium argument ("PE-level returns plus operational control")

---

## MODEL 13 — Cap Table Dilution Model

**Purpose:** Track ownership percentages through all proposed transactions and ensure no unintended dilution or structural issues.

### How the Calculation Works

Equity is transferred (existing shares sold), not newly issued. Total shares outstanding remain constant at **10,527**.

```
Current shares outstanding:    10,527
Shares per 1%:                 10,527 ÷ 100 = 105.27
Shares per 5%:                 527 shares (per VP)
Shares per 20% (Bryan):        2,105 shares
```

**Pre-Transaction Cap Table:**
| Owner | Shares | % |
|-------|--------|---|
| Ramsey Pruchnic | 4,999 | 47.49% |
| Tyler Lafferty | 2,500.5 | 23.75% |
| T. Nick Murto | 2,500.5 | 23.75% |
| Jason Wilson | 527 | 5.01% |
| **Total** | **10,527** | **100%** |

**Post VP Program (3 VPs × 5%):**

Each seller (Ramsey, Nick, Tyler) sells shares proportionally:
```
Ramsey sells: 527 × (47.49% / 95%) × 3 = ~790 shares total (across 3 VPs)
  Resulting: 4,999 - 790 = 4,209 shares → ~39.98%
Tyler sells:  527 × (23.75% / 95%) × 3 = ~395 shares total
  Resulting: 2,500.5 - 395 = 2,105.5 shares → ~20.00%
Nick sells:   same as Tyler → ~20.00%
Jason: unchanged → 5.01%
```

**Post VP Program Cap Table:**
| Owner | Shares | % |
|-------|--------|---|
| Ramsey Pruchnic | ~4,209 | 39.98% |
| Tyler Lafferty | ~2,105 | 20.00% |
| T. Nick Murto | ~2,105 | 20.00% |
| Jason Wilson | 527 | 5.01% |
| Buyer 1 (VP) | 527 | 5.01% |
| Buyer 2 (VP) | 527 | 5.01% |
| Buyer 3 (VP) | 527 | 5.01% |
| **Total** | **10,527** | **100%** |

**Post Bryan Howell Investment (20% additional):**
*(Requires separate modeling — Bryan's 20% would come from existing holders)*
```
If Bryan purchases 20% post-VP-program:
  Bryan buys: 2,105 shares from Ramsey, Tyler, Nick proportionally
  Ramsey: 39.98% - (20% × 39.98%/85%) ≈ 30.4%
  [Full waterfall calculation needed when transaction terms are finalized]
```

### Output
- Pre/post cap table for each transaction
- Ramsey's retained control percentage at each stage
- Confirmation that Jason Wilson's 5% is undisturbed

### How It's Been Used
- VP program structure (from Griffiths appraisal exhibit — confirms the 3 VP structure)
- Bryan Howell proposal cap table
- Ramsey's "floor" control check — ensuring he retains majority through VP program

---

## MODEL 14 — Client Concentration Calculator

**Purpose:** Monitor revenue concentration risk and track progress toward the <20% target.

### Inputs Required
- Total quarterly revenue
- Revenue per client (or client group) for the same period

### How the Calculation Works

```
Client Concentration % = Client Revenue ÷ Total Revenue × 100

HHI (Herfindahl-Hirschman Index) — optional:
  HHI = Σ (Client %)²
  HHI > 2,500 = highly concentrated
  HHI < 1,500 = diversified
```

**Current Concentrations (Q2 2025 Actual):**

| Client | Q2 2025 Revenue | % of Revenue |
|--------|----------------|-------------|
| Diesel Power Products (DPP) | $290,522 | 26.0% |
| City Post | $144,854 | 13.0% |
| High Desert Medical | $117,014 | 10.5% |
| Complete Performance | $111,456 | 10.0% |
| LDS / FamilySearch | $73,250 | 6.6% |
| Toolbox Widget | $69,728 | 6.3% |
| Pacbrake | $56,500 | 5.1% |
| All Others | ~$253,000 | ~22.7% |
| **Total** | **~$1,116,000** | **100%** |

**DPP Concentration Reduction Formula:**
```
To get DPP to <20%:
  Current DPP revenue:  ~$300K/quarter
  Required total revenue at <20%: $300K ÷ 20% = $1,500K/quarter
  Gap to close:  $1,500K - $1,116K = $384K/quarter in new revenue needed
  (Or DPP contract reduces while others grow)
```

### Output
- Concentration % per client
- Flag when any client exceeds 20% threshold
- Quarterly trend showing concentration improving or worsening

### How It's Been Used
- Bryan Howell proposal risk section (DPP concentration = risk + mitigation opportunity)
- Quarterly CFO monitoring dashboard
- Banker package risk disclosure

---

## MODEL 15 — Monthly CFO Dashboard Framework

**Purpose:** Standardized monthly analysis template for rapid performance assessment and board reporting.

### Template Structure

```
MONTHLY CFO DASHBOARD
Period: [Month] [Year]

═══ REVENUE ═══
Current Month Revenue:          $___,___
Prior Month Revenue:            $___,___   MoM Change: ___.__%
Prior Year Same Month:          $___,___   YoY Change: ___.__%
YTD Revenue:                    $___,___
YTD vs. Prior Year:             $___,___   Change: ___.__%
Full-Year Run Rate:             $___,___

═══ PROFITABILITY ═══
Current Month NOI:              $___,___
Current Month NOI Margin:       ___.__%
YTD NOI:                        $___,___
YTD NOI Margin:                 ___.__%
Target Margin:                  28–30%
Gap to Target:                  ___.__%

═══ EXPENSE MONITOR ═══
Total Monthly Expenses:         $___,___
Fixed Expenses:                 $___,___
People Expenses:                $___,___
Variable Expenses:              $___,___
Break-Even Revenue:             ~$280,000
Months Above Break-Even:        ___/___

═══ EBITDA TRACKER ═══
YTD EBITDA:                     $___,___
Annual EBITDA Run Rate:         $___,___
Full-Year Target:               $1,200,000
% to Target:                    ___.__%

═══ DEAL STATUS ═══
Bryan Howell:                   [status]
VP Equity Program:              [status]
Valuation Challenge:            [status]
RiverBank Financing:            [status]

═══ CLIENT HEALTH ═══
DPP Concentration:              ___.__%   (Target: <20%)
Top 5 Client Revenue:           $___,___
New Client Revenue:             $___,___
Churned Revenue:                $___,___

═══ KEY RISKS & OPPORTUNITIES ═══
[Bullet list of 3–5 items]
```

### Key Formulas Used in Dashboard
```
MoM Change     = (Current - Prior) ÷ Prior
YoY Change     = (Current Year - Prior Year) ÷ Prior Year
Run Rate       = YTD Revenue ÷ Months Elapsed × 12
NOI Margin     = NOI ÷ Revenue
EBITDA Target  = $1,200,000 (2026) escalating per EBITDA goals table
```

### How It's Been Used
- Framework for monthly CFO reporting to Ramsey
- Structure for banker updates
- Basis for detecting margin compression early

---

## QUICK REFERENCE FORMULAS

```
═══ VALUATION ═══
Enterprise Value          = EBITDA × Multiple
Per 1% equity            = Enterprise Value ÷ 100
Break-even multiple check: $8M ÷ $1.2M EBITDA = 6.7× (very conservative)

═══ PROMISSORY NOTE ═══
Monthly Payment           = P × [r(1+r)^n] ÷ [(1+r)^n - 1]
At $400K, 6%, 15yr       = $2,953/month
Coverage ratio           = (EBITDA × 5% ÷ 12) ÷ $2,953
Min EBITDA for 1× cover  = $708,720

═══ REVENUE ═══
YoY Growth                = (Current Year - Prior Year) ÷ Prior Year
Run Rate (quarterly)      = Quarter Revenue × 4
Quarterly Break-Even      = ~$850,000 (3 × $283K monthly)
Monthly Break-Even        = ~$280,000–$290,000

═══ MARGINS ═══
NOI Margin                = Net Operating Income ÷ Revenue
Target                    = 28–30%
2025 H2 Demonstrated      = 27–33% (May, June, September)
Griffiths Assumption (wrong): 15.41%

═══ INVESTOR RETURNS ═══
Annual Distribution (Bryan) = EBITDA × 20%
IRR (approximate, conservative) = 23–26%
5-Year MOIC (conservative)  = 2.3×
Cash payback period         = ~6 years
```

---

*Document compiled March 2026. All models derived from QuickBooks exports, third-party appraisal analysis, and the Bryan Howell investment proposal. For use by Ramsey Pruchnic and authorized CFO advisors only.*
