# Mail Agent

Read and triage your physical mail using AI vision. Drop scanned or photographed letters into a folder, run `/analyze-mail`, and get a full triage report — what every piece is, what you need to do with it, who to route it to, and by when.

## How It Works

1. Scan or photograph your mail and drop the images into your configured inbox folder
2. Run `/analyze-mail`
3. The agent reads every piece — envelope and letter — using vision
4. You get a prioritized triage report: urgency, key details, routing, and specific next steps
5. Route directly via Slack or email, then mark everything as processed

## Commands

| Command | What It Does |
|---------|-------------|
| `/mail-setup` | First-time setup: inbox folder, routing contacts, notifications |
| `/analyze-mail` | Process all mail in the inbox folder |
| `/analyze-mail [path]` | Analyze a specific file or folder |

## What It Detects

- **Bills and invoices** — amount due, deadline, how to pay
- **Legal notices** — court documents, attorney letters, summons
- **Government mail** — IRS, state agencies, regulatory notices
- **Certified mail** — flagged as urgent automatically
- **Bank and financial statements** — FYI, routed to finance
- **HR and employment documents** — routed to HR contact
- **Insurance correspondence** — routed to appropriate contact
- **Checks and payment instruments** — flagged for immediate deposit
- **Marketing and junk** — grouped and marked safe to shred

## Setup

Run `/mail-setup` once to configure:
- Inbox folder location (where you'll drop scans)
- Routing contacts by mail type (finance, legal, HR, etc.)
- Notification delivery (Slack, email, or conversation-only)
- Urgency thresholds and preferences

## Scanning Tips

- Scan or photograph the envelope AND the letter separately
- Good lighting, phone held directly above — no angle
- Name files with matching prefixes for multi-page letters: `letter-01-envelope.jpg`, `letter-01-page1.jpg`, `letter-01-page2.jpg`
- Minimum 200 DPI for readable text
