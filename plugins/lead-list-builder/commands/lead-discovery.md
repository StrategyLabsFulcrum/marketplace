# Lead Discovery

Automated research engine that finds net-new leads, detects changes to existing leads, and grows the lead list with deduplicated, scored, and enriched contacts.

## Before Starting

1. Load existing lead lists from `lead-lists/`.
   - If none exist: "No lead lists found. Run `/build-lead-list` to create your first list."
2. Load discovery settings from `lead-lists/.config/discovery-settings.md` if they exist.
3. Load discovery log from `lead-lists/.config/discovery-log.md` if it exists.

---

## First Run — Setup Discovery Settings

If no discovery settings exist, walk the user through configuration:

### Frequency

> "How often should I search for new leads?"
> - **Weekly** (recommended for active prospecting)
> - **Bi-weekly** (moderate pace)
> - **Monthly** (slower, less time-intensive)
> - **Manual only** (only when you run this command)

### Lead Types to Monitor

Pull from existing lead list types:

> "Which lead types should I search for?"
> - [x] Estate/Probate Attorneys — watch for: new firms opening, new attorneys joining existing firms, state bar new admissions
> - [x] Insurance Adjusters / Restoration Companies — watch for: new franchise openings, ownership changes, new hires, new certifications

### Discovery Sources to Activate

> "Which sources should I monitor?"
> - [x] Google Maps — new businesses in target categories
> - [x] Google Search — industry directories, news mentions
> - [x] Professional directories — state bar, trade associations
> - [x] Firm/company websites — team page changes
> - [x] Franchise announcements — new locations from tracked brands
> - [x] Referral prompts — ask converted leads for introductions
> - [ ] LinkedIn — new profiles matching criteria (limited without premium)
> - [ ] Industry events — conference exhibitor/attendee lists

### Geography

Pull from existing list config or ask:

> "Same geography as your current list? ([geo description])"
> - **Same** — Keep searching within current boundaries
> - **Expand** — Add new areas (specify)
> - **Custom** — Define new boundaries for discovery only

Save settings to `lead-lists/.config/discovery-settings.md`.

---

## Discovery Run

### Step 1: Load Current Inventory

```
Loading existing lead list...

Current inventory:
├── 48 total leads (20 attorneys, 28 restoration/adjusters)
├── 32 unique companies
├── 48 unique contacts
├── Geography: Spokane, WA + 40-mile radius
├── Last discovery: [date] ([X] days ago)
```

### Step 2: Execute Source Searches

For each activated discovery source, run targeted searches:

**Google Maps — New Businesses:**
- Search: "[category] near [location]" sorted by newest
- Compare results against known companies list
- Flag any business not in the existing list

**Google Search — Directories & News:**
- Search: "new [lead type] [location] [current year]"
- Search: "[lead type] [location] directory" — compare against known list
- Search: "[industry] [location] news" — look for openings, hires, expansions

**Professional Directories:**
- For attorneys: Search state bar new admissions for relevant practice areas in target counties
- For restoration: Search trade association member lists (Restoration Industry Association, IICRC)
- For adjusters: Search public adjuster licensing databases

**Firm/Company Website Monitoring:**
- For 5-star leads' companies: Check their "Team" or "About" pages for new hires
- Look for new associates, partners, or team members not in the list

**Franchise Monitoring:**
- Search for new franchise openings: "SERVPRO new location [region]", "PuroClean opening [region]"
- Check franchise brand press release pages

**Referral Prompts:**
- For each lead with status "converted": Check if a referral prompt has been issued
- If not, generate a referral ask to present to the user

### Step 3: Categorize Findings

Sort all discoveries into four buckets:

**Bucket 1: Net-New Companies**
Companies not in the existing list at all.

```
🆕 NET-NEW COMPANIES (4 found)

1. Apex Restoration LLC — Water damage restoration
   Opened: February 2026 | Spokane Valley, WA
   Owner: Marcus Webb
   Phone: (509) 555-0199 | Website: apexrestorationspokane.com
   Source: Google Maps (new listing) + WA business filings
   Relevance: ★★★★ (+2 bonus: opened < 6 months, building referral network)
   Suggested channel: Phone — new business owner, likely answers his own phone

2. Northside Estate Law — Estate planning firm
   Opened: January 2026 | North Spokane, WA
   Attorney: Diana Pratt
   Phone: (509) 555-0234 | Website: northsideestatelaw.com
   Source: WA State Bar new admissions + Google Maps
   Relevance: ★★★★★ (+2 bonus: new firm, actively building client base)
   Suggested channel: Email — professional intro

3. [...]
```

**Bucket 2: New Contacts at Existing Companies**
New people at firms already in the list.

```
👤 NEW CONTACTS AT EXISTING COMPANIES (2 found)

1. Jake Morris — Associate Attorney
   Firm: Elevated Estate Planning (you already have Matthew Luedke + Elena Rogers)
   Source: Firm website team page update
   Relevance: ★★★ (associate, not decision-maker, but builds multi-contact coverage)
   Action: Add as additional contact? [Yes / Skip]

2. [...]
```

**Bucket 3: Lead Updates**
Changes to existing leads (promotions, job changes, company updates).

```
🔄 LEAD UPDATES (3 found)

1. L-007 Catherine Kardong — Promoted to Partner at Hunter Kardong Elder Law
   Previous: Associate | Updated: Partner (Dec 2025)
   Action: Already captured in notes. No change needed.

2. L-039 Ronell Bracy-Martin — May have moved to Simon Roofing
   Previous: Business Development Manager at First Onsite
   Found: LinkedIn shows "Regional Account Manager at Simon Roofing" since Jan 2026
   Action: Verify and update. If confirmed, find replacement contact at First Onsite.

3. [...]
```

**Bucket 4: Possible Duplicates**
Fuzzy matches that need human review.

```
⚠️ POSSIBLE DUPLICATES (1 found)

1. "ServiceMaster Fire & Water Restoration" — found on BBB
   Possible match: "ServiceMaster by Compass" (L-023 Fred Anderson)
   Reason: Same address, similar name
   Action: Confirm duplicate and skip? [Yes — same company / No — different]
```

### Step 4: Enrich New Leads

For each confirmed net-new lead, automatically search for:
- LinkedIn profile URL
- Facebook page (company or personal)
- Email address (firm website, directory listings)
- Phone number
- Google review count/rating
- Additional contacts at the company
- Any bonus info (certifications, awards, years in business)

### Step 5: User Confirms

Present all findings with a clear action menu:

```
DISCOVERY SUMMARY — [Date]

Found: 4 net-new companies, 2 new contacts, 3 updates, 1 possible dupe

Actions:
├── Add all 4 net-new companies? [Yes / Select / Skip]
├── Add 2 new contacts at existing companies? [Yes / Select / Skip]
├── Apply 3 lead updates? [Yes / Review each]
├── Resolve 1 possible duplicate? [Review]
```

### Step 6: Update List

After user confirms:
1. Assign new IDs (continuing sequence: L-049, L-050...)
2. Append to existing CSV
3. Regenerate markdown summary
4. Regenerate dashboard
5. Auto-generate CRM export if connections configured
6. Update discovery log

```
Discovery Complete!

Added: 5 new leads (4 companies + 1 new contact)
Updated: 2 existing lead records
Skipped: 1 duplicate
Total leads: 53 (was 48)

Discovery log updated.
Next scheduled discovery: [date based on frequency setting]
```

---

## Referral Chain Discovery

For leads with status "converted," the plugin proactively suggests referral mining:

```
REFERRAL OPPORTUNITIES (2 converted leads without referral prompts)

1. L-012 Kristina Mattson — Converted 3/22
   She's an estate attorney with deep community ties (Spokane Valley Chamber member).
   Suggested referral ask:
   "Kristina, you've been great to work with. Are there any other attorneys
   or professionals in your network who might benefit from a reliable demo partner?"

   Potential referral targets based on her network:
   ├── Other attorneys in her building (1206 N Lincoln St)
   ├── Financial planners who handle estate transitions
   └── Senior living facility administrators

2. L-024 Sandra Teal — Converted 4/01
   She's a Business Development Manager — her entire job is building referral networks.
   Suggested referral ask:
   "Sandra, who else in the restoration/insurance space should I be talking to?"

   Potential referral targets:
   ├── Insurance agents she works with regularly
   ├── Other restoration company owners she's connected to
   └── Property managers in her network
```

---

## List Saturation Monitoring

After each discovery run, calculate and report coverage:

```
LIST SATURATION:

Estate/Probate Attorneys:
├── Known firms in 40-mile radius: ~28
├── Firms in your list: 24 (86% coverage)
├── Status: NEAR SATURATION
├── Recommendation: Expand to 60 miles or add adjacent types
│   (title companies, financial planners, senior care facilities)

Insurance/Restoration Companies:
├── Known companies in 40-mile radius: ~35
├── Companies in your list: 22 (63% coverage)
├── Status: ROOM TO GROW
├── Recommendation: Continue weekly discovery, focus on independent
│   companies and new franchise openings

SUGGESTED NEW LEAD TYPES (based on conversions):
├── Title Companies — Natural referral partners for estate attorneys
├── Home Inspectors — See demo needs during property inspections
├── Bankruptcy Trustees — Property liquidation creates demo work
├── Senior Living Facilities — Estate transitions for residents
├── Financial Planners — Advise clients on estate property disposition
```

---

## Discovery Settings Management

The user can adjust discovery settings anytime:

```
/lead-discovery settings

Current settings:
├── Frequency: Weekly (last run: 3 days ago)
├── Lead types: Estate Attorneys, Insurance/Restoration
├── Geography: Spokane + 40 miles
├── Sources: Google Maps, Google Search, State Bar, Firm websites, Franchise news

What would you like to change?
1. Frequency
2. Add/remove lead types
3. Expand/change geography
4. Add/remove discovery sources
5. View discovery history log
```
