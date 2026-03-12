---
name: brand-setup
description: >
  First-run onboarding wizard for the Local Business Marketing OS. Collects brand details and saves them to brand-config.json so all other skills in this plugin work without brand-specific hardcoding. Trigger on "set up my brand", "brand setup", "configure my restaurant", "onboard my business", "first time setup", "initialize brand config", or any time another skill detects brand-config.json is missing.
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

# Brand Setup — Onboarding Wizard

You are setting up the Local Business Marketing OS for a new brand. This wizard collects all the information the other skills need to operate. At the end, everything is saved to `brand-config.json` in the working directory.

**This only needs to run once.** After setup, all other skills will read from `brand-config.json` automatically.

---

## BEFORE YOU START

Check if `brand-config.json` already exists in the working directory. If it does:

> "I found an existing brand config for **[brand_name]**. Want to update it, or start fresh?"

If starting fresh, proceed with the wizard below. If updating, load the existing config and only ask about sections the user wants to change.

---

## WIZARD FLOW

Walk through each section in order. Use `AskUserQuestion` for each section. Keep questions conversational — this should feel like a 5-minute onboarding call, not a form.

---

### SECTION 1: Business Basics

Ask these together in one message:

> "Let's start with the basics. What's the name of your business, and what type of business is it? (e.g., taco shop, cocktail bar, pizza restaurant, coffee shop)"

Then:

> "What's your address, phone number, and website (if you have one)?"

Then:

> "What are your regular hours? Just the days and times you're typically open."

---

### SECTION 2: The Team

> "Who's the owner? And do you have a general manager or someone who handles the floor day-to-day? I'll use these names when signing review responses and campaign emails."

---

### SECTION 3: Brand Voice

> "How would you describe your brand's personality in a sentence or two? Think about how you'd want a regular customer to describe the vibe — not what you'd put in a press release."

Then:

> "Any words or phrases you'd never want us to use? (Things that sound too corporate, too generic, or just not 'you'?)"

Then:

> "Any phrases, taglines, or expressions that are very 'you' — things your team says, things your regulars say?"

---

### SECTION 4: Menu / Key Products

> "What are the 5–10 items you most want people to know about? These become the anchor for content, campaigns, and review responses. Give me the name and a quick description for each."

Then:

> "Do you have any specials with fixed pricing we should reference in campaigns? (e.g., a lunch special, happy hour deal, weekly deal)"

---

### SECTION 5: Loyalty Program

> "Do you have a loyalty or rewards program? If so, what's it called and what platform does it run on? (e.g., Toast, Square, Lightspeed)"

---

### SECTION 6: Marketing Channels

> "Which channels are you active on? Check all that apply:
> - Email (what platform? Klaviyo, Mailchimp, other?)
> - SMS (same platform as email, or separate?)
> - Instagram
> - Facebook
> - Google Reviews
> - Yelp
> - TikTok
> - Other?"

Then:

> "Any handles or profile links you want us to reference? (e.g., Instagram @yourbrand)"

---

### SECTION 7: Events & Spaces

> "Do you have any private event spaces, upstairs rooms, patios, or separate concepts under the same roof? Describe them briefly if so."

> "Do you do catering or off-site events?"

---

### SECTION 8: Inbox Setup (optional — for inbox-manager skill)

> "The inbox-manager skill can manage your email and calendar. If you'd like to set that up, I need a few things:
> - Your name (so I can draft replies in your voice)
> - Your primary email address
> - Any VIP contacts I should always prioritize (clients, partners, key vendors)
>
> Skip this if you don't plan to use the inbox manager."

---

## SAVING THE CONFIG

After all sections are complete, save the following file as `brand-config.json` in the working directory:

```json
{
  "brand": {
    "name": "",
    "type": "",
    "address": "",
    "phone": "",
    "website": "",
    "hours": ""
  },
  "team": {
    "owner_name": "",
    "manager_name": "",
    "sign_off_default": ""
  },
  "voice": {
    "personality": "",
    "forbidden_words": [],
    "approved_phrases": []
  },
  "menu": {
    "featured_items": [],
    "specials": []
  },
  "loyalty": {
    "program_name": "",
    "platform": ""
  },
  "channels": {
    "email_platform": "",
    "sms_platform": "",
    "instagram": "",
    "facebook": "",
    "google_reviews": "",
    "yelp": "",
    "other": []
  },
  "spaces": {
    "private_event_space": "",
    "patio": false,
    "catering": false
  },
  "inbox": {
    "user_name": "",
    "primary_email": "",
    "vip_contacts": []
  }
}
```

Populate every field from the wizard answers. Leave fields blank ("") if not provided — never make up values.

---

## CONFIRMATION

After saving, present a summary:

> "✅ Brand config saved for **[brand_name]**.
>
> Here's what's set up:
> - Business: [name], [type], [city]
> - Team: [owner] / [manager]
> - Voice: [personality summary]
> - [X] menu items configured
> - Channels: [list active channels]
> - Loyalty: [program name or 'not configured']
>
> All other skills in this plugin will now use this config automatically. Run `/brand-setup` any time to update it."

---

## HOW OTHER SKILLS USE THIS CONFIG

Every other skill in this plugin begins by reading `brand-config.json`:

```
1. Check if brand-config.json exists in the working directory
2. If yes: load it and proceed
3. If no: say "I need to set up your brand first. Running brand-setup now..." and trigger brand-setup
```

This means no other skill will ever need hardcoded brand details.
