---
name: mail-agent
description: >
  Physical Mail Agent — analyzes scanned or photographed mail dropped into a folder.
  Use when the user mentions "analyze my mail", "check the mail", "read my mail",
  "mail inbox", "scan my letters", "physical mail", "snail mail",
  "route this mail", "what do I do with this letter", "mail triage",
  "check the mail folder", or anything about reviewing physical paper mail.
---

# Mail Agent

An AI agent that reads scanned or photographed physical mail, classifies each piece, extracts key details, determines urgency, and tells you exactly what to do with it — route it to someone, respond, pay, file, or discard.

---

## How It Works

1. User scans or photographs mail and drops images into `_mail-inbox/`
2. User runs `/analyze-mail`
3. The agent reads every image using vision, analyzing both the envelope and letter contents
4. For each piece: classify, extract details, assess urgency, determine action
5. Present a triage report with specific next steps
6. Optionally send routing notifications via Slack or email
7. Move processed files to `_mail-processed/` and log to `mail-log.md`

---

## Data Directory

Resolve the mail data directory in this order:
1. **iCloud** (preferred): `~/Library/Mobile Documents/com~apple~CloudDocs/mail-agent/`
2. **Local fallback**: `mail-agent/` in the current working directory

Config and log files live in this directory. The inbox and archive folders are typically alongside scanned files — location configured during setup.

---

## Mail Classification

Every piece of mail falls into exactly one category:

### 🔴 ACTION REQUIRED
Needs a specific response, payment, decision, or action by a deadline.
- Bills and invoices (due date present)
- Legal documents, court notices, summons
- Government notices (IRS, state agencies, regulatory)
- Certified mail requiring signature confirmation
- Contract documents requiring signature or response
- Insurance claims or policy changes requiring action
- Employment/HR notices
- Loan or mortgage documents

### 🟡 ROUTE TO
Needs to go to a specific person — not the mail recipient's to handle.
- Financial documents for accounting/CFO
- Legal documents for legal counsel
- HR/benefits documents for HR
- Vendor invoices for accounts payable
- Medical/insurance for relevant team member
- Personal mail for a named individual

### 🟢 FYI
Worth knowing but no action required.
- Bank statements (informational)
- Policy updates (no action needed)
- Newsletters, subscriptions
- Receipts and confirmations
- Meeting or event notices

### 🗑️ DISCARD
No value — can be discarded.
- Marketing mail / catalogs
- Solicitations and fundraising
- Duplicate copies
- Expired offers

---

## What to Extract From Each Piece

For every piece of mail, extract:

### Envelope (if visible)
- Return address (sender name, company, address)
- Addressee (who it's addressed to)
- Postmark date
- Mail type indicators: Certified, Priority, Registered, First Class, bulk
- Any urgency indicators on the envelope ("Time Sensitive", "Open Immediately", "Legal Notice")

### Letter / Document Content
- **Sender**: Full name, company, address, phone, email, website
- **Date**: Date of the letter (not postmark)
- **Reference number**: Account number, case number, invoice number, policy number, claim number
- **Subject/Purpose**: What this letter is about in plain language
- **Key amounts**: Dollar figures, payment amounts, balances, penalties
- **Deadlines**: Any dates mentioned for action, response, or payment
- **Specific request or action**: What they are asking you to do
- **Consequences**: What happens if no action is taken
- **Contact information**: How to respond or get more info

---

## Urgency Assessment

After extracting details, assign an urgency level:

| Level | Criteria |
|-------|---------|
| 🚨 **URGENT** | Legal deadline within 7 days, past-due notice, court date, immediate action required |
| ⚠️ **SOON** | Deadline or due date within 30 days, response requested |
| 📋 **STANDARD** | No immediate deadline, informational action |
| ✅ **NO ACTION** | FYI only, no response needed |
| 🗑️ **DISCARD** | Marketing, junk, solicitation |

---

## Routing Table

Routing contacts are configured during `/mail-setup` and stored in `[data-path]/mail-config.md`.

When routing is identified, match the mail type against the routing table:

```
Finance / Invoices / Bills → [configured finance contact]
Legal / Court / Government → [configured legal contact]
HR / Benefits / Employment → [configured HR contact]
Personal / Individual Named → [that person directly]
Medical / Insurance → [configured insurance contact]
General / Unmatched → [configured default contact]
```

If no routing config exists, suggest routing based on mail type and ask the user to confirm who to send it to.

---

## Triage Report Format

Present each piece of mail as a card, sorted by urgency:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[#1] 🚨 URGENT — ACTION REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File:       [filename]
From:       [Sender Name / Company]
            [Sender Address]
Addressed:  [Addressee on envelope]
Date:       [Letter date] (received: [postmark])
Type:       [Bill / Legal Notice / Government / etc.]
Ref #:      [Account/Case/Invoice number]

SUMMARY:
[2-3 sentence plain-language summary of what this letter says]

KEY DETAILS:
├── Amount:    $[X] [due/owed/balance]
├── Deadline:  [Date] — [X] days from today
├── Action:    [Specific action required]
└── Contact:   [How to respond — phone, email, web, return address]

CONSEQUENCES IF IGNORED:
[What happens if no action is taken, per the letter]

RECOMMENDED ACTION:
→ [Specific, clear next step — e.g., "Pay $847 online at [url] or call [phone] before March 28"]

ROUTE TO: [Person/role if routing is appropriate]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

For 🗑️ DISCARD items, group at the end:
```
🗑️ DISCARD — [X] items
├── [sender] — Marketing catalog
├── [sender] — Fundraising solicitation
└── [sender] — Expired promotional offer
→ Safe to shred all [X] items.
```

---

## Post-Triage Actions

After presenting the triage report, offer:

```
→ [Route #1 to finance] [Route #2 to legal] [Send full report via Slack] [Save report] [Mark all processed]
```

**Routing via Slack:** If Slack MCP is connected, post a formatted summary to the configured routing channel or DM the designated contact directly.

**Routing via email:** If email (Gmail/Rube) is connected, draft a forwarding email with the scanned attachment and a summary.

**Mark processed:** Move all analyzed files from `_mail-inbox/` to `_mail-processed/[YYYY-MM-DD]/` and append entries to `mail-log.md`.

---

## Mail Log

Append to `[data-path]/mail-log.md` after every session:

```markdown
## [Date] — [X] pieces analyzed

| # | From | Type | Urgency | Action | Deadline | Routed To | Status |
|---|------|------|---------|--------|----------|-----------|--------|
| 1 | IRS | Government Notice | 🚨 Urgent | Respond | 2026-04-15 | CPA | Routed |
| 2 | Chase Bank | Statement | ✅ No Action | File | — | — | Filed |
| 3 | REI Catalog | Marketing | 🗑️ Discard | Shred | — | — | Discarded |
```

---

## Vision Reading Guidelines

When analyzing each mail image:

1. **Read the full image** — envelope front, envelope back, all pages of the letter
2. **Multiple images = one piece** — if the user names files `letter-1a.jpg`, `letter-1b.jpg`, treat as one multi-page document
3. **Unclear/blurry text** — flag with ⚠️ and note what's unreadable; ask the user to provide a clearer scan if the unclear section contains critical info (amounts, deadlines, reference numbers)
4. **Envelope only** — if only the envelope is scanned, extract what's visible and note: "Only envelope scanned — letter contents unknown. Recommend opening and re-scanning."
5. **Handwritten mail** — attempt to read; if illegible, flag as ⚠️ HANDWRITTEN — PARTIALLY LEGIBLE and extract what you can
6. **Non-English mail** — translate and note the original language
7. **Legal/official seal or watermark** — note its presence (courts, government agencies often have official seals that indicate higher authority)

---

## File Structure

### Plugin Source
```
plugins/mail-agent/
├── .claude-plugin/plugin.json
├── SKILL.md                    ← this file
├── README.md
└── commands/
    ├── setup-wizard.md
    └── analyze-mail.md
```

### User Data
```
[data-path]/
├── mail-config.md              ← routing contacts, preferences, setup
├── mail-log.md                 ← history of all analyzed mail
├── _mail-inbox/                ← drop scanned mail images here
├── _mail-processed/            ← analyzed mail, organized by date
│   └── YYYY-MM-DD/
└── _mail-archive/              ← long-term storage
```
