# Lead Outreach

Draft personalized outreach messages for leads in an existing lead list. Generates messages per lead type and channel, using brand voice and specific references to each lead's business.

## Before Starting

1. Check for existing lead lists in `lead-lists/`.
   - If none exist: "No lead lists found. Run `/build-lead-list` first."
   - If multiple exist: "Which lead list do you want to draft outreach for?" (list them)
   - If one exists: Load it automatically.
2. Check for `brand-knowledge-center/` — load brand voice, messaging, and positioning for outreach tone.

---

## Step 1: Load Lead List

Read the selected lead list CSV and summarize:

> "Loaded **[list-name]** with [X] leads:
> - [X] Not Started — ready for outreach drafting
> - [X] Drafted — already have messages
> - [X] Sent/Responded/Other — in progress
>
> Draft outreach for all [Not Started] leads, or select specific lead types?"

---

## Step 2: Outreach Strategy

For each lead type in the list, confirm the outreach approach:

> "Here's my recommended outreach plan:
>
> | Lead Type | Primary Channel | Secondary Channel | Tone |
> |-----------|----------------|-------------------|------|
> | Retail Buyers | Email | Phone | Professional but warm |
> | Influencers | Instagram DM | Email | Casual, authentic |
> | Media/Press | Email | Twitter/X DM | Newsworthy, concise |
>
> Adjust any of these, or proceed?"

---

## Step 3: Draft Messages

For each lead type, generate outreach templates and personalized drafts.

### Template Generation

Create 2-3 template variations per lead type per channel:

**Variation 1: Direct Value**
- Lead with what's in it for them
- Best for: retail buyers, corporate buyers

**Variation 2: Common Ground**
- Lead with shared interests, values, or connections
- Best for: influencers, partners

**Variation 3: Newsworthy Hook**
- Lead with something timely or noteworthy about the brand
- Best for: media, press

### Personalization

For each individual lead, customize the template with:
1. Their name and company
2. Something specific about their business (pulled from research source)
3. Why they specifically are a good fit
4. A relevant product or collaboration angle

### Present for Review

Show drafts grouped by lead type:

> **Retail Buyers — Email Template (Direct Value):**
>
> ---
> **To:** Sarah Chen, Mountain Outfitters
> **Subject:** PNW apparel line for Mountain Outfitters
>
> Hi Sarah,
>
> I've been following Mountain Outfitters' expansion into lifestyle apparel — your curation of PNW brands is exactly the kind of retail environment we love.
>
> We're The Great PNW — a Pacific Northwest lifestyle brand doing heavy-weight flannels, hoodies, and beanies that our customers describe as "finally, PNW gear that doesn't feel like tourist merch." Our price points ($30-$65 retail) fit the sweet spot for your customer base.
>
> Would you be open to a quick look at our wholesale line sheet? Happy to send samples too.
>
> Joel Barbour
> The Great PNW
> ---
>
> **Want to edit this template, approve it, or see another variation?**

### Follow-Up Sequences

For each lead type, draft the follow-up messages:

**Follow-Up 1 (Day 3-5):**
> Short, adds new info or value. "Wanted to share one more thing..."

**Follow-Up 2 (Day 7-10, alternate channel):**
> Try secondary channel. "Reaching out here in case email got buried..."

**Final Follow-Up (Day 14-21):**
> Brief, leave door open. "Totally understand if the timing isn't right..."

---

## Step 4: Save Outreach

After drafts are approved, save to:

### `lead-lists/[list-name]-outreach.md`

Organized by lead type, then by individual lead:

```markdown
# Outreach Drafts: [List Name]

## Summary
- **Total drafts:** 41
- **Lead types covered:** 3
- **Channels:** Email (26), Instagram DM (15)
- **Generated:** 2026-03-19

## Follow-Up Cadence
| Touchpoint | Timing | Action |
|------------|--------|--------|
| Initial | Day 0 | Send personalized message |
| Follow-up 1 | Day 3-5 | Brief follow-up, same channel |
| Follow-up 2 | Day 7-10 | Try alternate channel |
| Final | Day 14-21 | Last touch, leave door open |

---

## Retail Buyers — Email

### L-001: Sarah Chen — Mountain Outfitters
**Subject:** PNW apparel line for Mountain Outfitters
[full message]

**Follow-up 1:**
[message]

**Follow-up 2 (LinkedIn):**
[message]

**Final:**
[message]

---

[...continues for all leads...]
```

### Update Lead Status

Update all drafted leads to `outreach_status: drafted` in the CSV.

---

## Step 5: Completion

```
Outreach Drafts Complete!

✉️  [list-name]
├── 41 personalized messages drafted
├── Email drafts: 26
├── Instagram DM drafts: 15
├── Follow-up sequences: 3 touchpoints per lead
├── Saved to: lead-lists/[list-name]-outreach.md

Lead status updated:
├── 41 leads moved from "Not Started" → "Drafted"

Next steps:
- Review and personalize each draft before sending
- Use /update-leads to mark leads as "Sent" after outreach
- Track responses and update status as replies come in
- Run /update-leads to find net-new leads when ready to expand
```
