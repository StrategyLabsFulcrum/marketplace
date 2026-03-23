# /analyze-mail

Read and triage every piece of mail in the inbox folder. Analyzes each image using vision, extracts key details, assesses urgency, determines what to do with it, and presents a full triage report.

**Invoke options:**
```
/analyze-mail                   ← process everything in configured _mail-inbox/
/analyze-mail [file path]       ← analyze a specific image or PDF
/analyze-mail [folder path]     ← analyze all images in a specific folder
```

---

## Before Starting

1. **Resolve data path:** Check for iCloud config first: `~/Library/Mobile Documents/com~apple~CloudDocs/mail-agent/mail-config.md`. If not found, check `mail-agent/mail-config.md` locally. If neither exists:
   > "No Mail Agent config found. Run `/mail-setup` to configure your inbox folder and routing contacts first."

2. **Load config:** Read `inbox_path`, routing contacts, notification method, urgency threshold, and preferences.

3. **Find files:** Scan the inbox folder (or specified path) for image files: `.jpg`, `.jpeg`, `.png`, `.heic`, `.tiff`, `.pdf`, `.webp`.

4. **Report what was found:**
   > "Found [X] files in your mail inbox. Analyzing now..."

   If inbox is empty:
   > "Your mail inbox at [path] is empty. Drop scanned or photographed mail there and run `/analyze-mail` again."

---

## Step 1: Group Related Files

Before analyzing, group files that belong to the same piece of mail:

**Grouping rules:**
- Files with the same numeric prefix are one piece: `letter-01-envelope.jpg` + `letter-01-page1.jpg` + `letter-01-page2.jpg` = one letter
- Files with no prefix pattern: treat each as a separate piece unless the content makes clear they're related
- PDFs: each PDF is typically one piece (may be multi-page)

Report groupings if useful:
> "I'm reading these as [X] separate pieces of mail. Let me know if any should be grouped differently."

---

## Step 2: Analyze Each Piece

For each piece of mail, read ALL images associated with it (envelope + all pages) before making determinations. **Do not skip the envelope** — the return address, postmark date, and mail type indicators on the envelope are often critical context.

For each piece, extract:

### Envelope
- Sender name and return address
- Addressee (who it's to)
- Postmark date
- Mail type: Certified / Priority / Registered / Standard / Bulk
- Any urgency text on the envelope ("Time Sensitive", "Legal Notice", "Open Immediately")

### Letter Content
- Date of the letter
- Sender's full contact info (company, address, phone, email, website)
- Reference / account / case / invoice number
- Subject or purpose (in plain language)
- Key dollar amounts (balance, amount due, penalty)
- All dates mentioned (due dates, deadlines, response windows)
- Exactly what they are asking you to do
- Consequences if no action is taken
- Any enclosures or attachments mentioned

### Classification
Assign ONE category: 🔴 ACTION REQUIRED / 🟡 ROUTE TO / 🟢 FYI / 🗑️ DISCARD

### Urgency
Assign ONE urgency: 🚨 URGENT / ⚠️ SOON / 📋 STANDARD / ✅ NO ACTION / 🗑️ DISCARD

### Routing
Match against routing contacts in config. If no match, suggest based on mail type.

### Recommended Action
Write a specific, plain-language next step. Not "consider responding" — "Call [phone] or log into [url] and pay $[amount] before [date]."

---

## Step 3: Present Triage Report

Sort all pieces: 🚨 URGENT first → ⚠️ SOON → 📋 STANDARD → 🟢 FYI → 🗑️ DISCARD last.

```
📬 MAIL TRIAGE — [Date]
[X] pieces analyzed · [X] action required · [X] to route · [X] FYI · [X] discard

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#1] 🚨 URGENT — ACTION REQUIRED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File:        [filename(s)]
From:        [Sender Name]
             [Sender Company, Address]
Addressed:   [Addressee]
Letter Date: [Date]  |  Postmark: [Date]
Type:        [Legal Notice / Bill / Government / etc.]
Ref #:       [Reference number if present]

SUMMARY:
[2–3 sentence plain-language description of what this letter is and what it says]

KEY DETAILS:
├── Amount:       $[X] [due / owed / penalty]
├── Deadline:     [Date] — [X] days from today
├── Action:       [Specific ask from the sender]
└── If ignored:   [Stated consequences]

HOW TO RESPOND:
→ [Specific actionable instruction — phone number, URL, return address, what to say/send]

ROUTE TO: [Name / Role] via [Slack / email / in-person]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#2] ⚠️ SOON — ACTION REQUIRED
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#3] 🟡 ROUTE TO — [Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
File:     [filename]
From:     [Sender]
Type:     [Invoice / HR Document / etc.]
Ref #:    [number]

SUMMARY:
[What this is and why it's being routed]

ROUTE TO: [Name / Role]
→ [Forward scanned copy to their email / post in #channel / hand deliver]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[#4–5] 🟢 FYI — No Action Required
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
├── [#4] Chase Bank — Monthly statement (March 2026). Balance: $12,847.
└── [#5] USAA — Annual policy renewal notice. No changes. Renewal auto-processed.

→ [File both]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗑️ DISCARD — 3 items
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
├── [#6] Williams-Sonoma — Spring catalog
├── [#7] ASPCA — Donation solicitation
└── [#8] Geico — Promotional insurance quote

→ Safe to shred all 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT NEXT?
→ [Route #1 to legal] [Route #3 to accounting] [Send report via Slack] [Mark all processed]
```

---

## Step 4: Handle Routing and Notifications

### If user approves routing:

**Via Slack** (if Slack MCP connected):
- DM the designated contact with: the mail summary + key details + recommended action
- Attach the scanned image if possible
- Format:
  ```
  📬 Mail routed to you — [Mail Type] from [Sender]
  [Summary]
  Key details: [amounts, deadlines, ref numbers]
  Action needed: [specific ask]
  Scanned files: [attached or note "files in shared folder at [path]"]
  ```

**Via email** (if Gmail/Rube connected):
- Draft a forwarding email to the routing contact with the scan attached and a summary in the body
- Present for approval before sending

**No connection — manual routing:**
> "Slack and email aren't connected. To route manually: forward the scanned file at [path] to [contact] at [email] and reference the summary above."

### If notification delivery is configured:
After presenting the triage, send the full report via the configured method (Slack DM, channel, or email digest).

---

## Step 5: Mark Processed

After the user confirms they've reviewed the report:

1. Move all analyzed files from `_mail-inbox/` to `_mail-processed/[YYYY-MM-DD]/`
2. Create the date folder if it doesn't exist
3. Append all pieces to `mail-log.md`

**Log format:**
```markdown
## [YYYY-MM-DD] — [X] pieces

| # | From | Type | Urgency | Action | Deadline | Routed To | Status |
|---|------|------|---------|--------|----------|-----------|--------|
| 1 | IRS | CP2000 Notice | 🚨 Urgent | Respond | 2026-04-15 | CPA | Routed |
| 2 | Chase | Statement | ✅ FYI | File | — | — | Filed |
| 3 | REI | Catalog | 🗑️ Discard | Shred | — | — | Discarded |
```

Confirm:
> "✓ [X] pieces processed. Files moved to `_mail-processed/[date]/`. Mail log updated."

---

## Edge Cases

**Only envelope scanned (no letter):**
> "Only the envelope was scanned for piece #[X] (from [sender]). I can see it came from [return address] and is addressed to [addressee] — but I can't read the letter contents. Recommend opening and re-scanning the letter before taking action."

**Blurry / unreadable critical section:**
> "⚠️ The [amount / deadline / reference number] in piece #[X] is not clearly legible in the scan. I can see approximately [what's partially visible]. Recommend re-scanning this section before acting."

**Clearly threatening or legal notice:**
> "⚠️ This appears to be a [court summons / attorney demand letter / government enforcement notice]. Do not ignore this. Recommended: route to legal counsel immediately, even before the stated deadline."

**Foreign language mail:**
Translate fully. Note the original language. Flag if official government documents from a foreign jurisdiction (may have legal implications).

**Check or payment instrument:**
> "This appears to be a [check / money order / payment] for $[amount] from [sender]. Action: deposit or route to finance immediately. Do not leave in the mail inbox."
