# /pr-pitch

Write a press release or journalist pitch for a product launch, brand announcement, milestone, or news hook. Produces media-ready copy with story angle development and a prioritized target publication list.

## How to Invoke

**Press release from a campaign brief:**
```
/pr-pitch campaigns/2026-03-spring-launch/brief.md
```

**Standalone with inline description:**
```
/pr-pitch new product launch — sustainable activewear collection, April 15 launch date
```

**Journalist pitch email:**
```
/pr-pitch email pitch for [outlet or journalist name] re: spring launch
```

**Both press release and pitch:**
```
/pr-pitch full package — press release + outreach emails for spring launch
```

## What You Get

- Story angle analysis (3 potential angles, ranked by media appeal)
- Press release in AP style (newsworthy headline, inverted pyramid structure, boilerplate, media contact)
- Journalist pitch email template (customizable per outlet)
- Target publication list (Tier 1–4 breakdown with specific outlets and relevant beat journalists where identifiable)
- Outreach cadence recommendation

## Output Location

Files saved to `campaigns/[slug]/pr-influencer/`:
```
press-release.md
media-pitch-template.md
media-target-list.md
```
