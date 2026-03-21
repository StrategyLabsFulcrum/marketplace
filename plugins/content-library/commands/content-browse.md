# /content-browse

Browse the full Content Library or a specific category. Use to explore what's available, review library status, or audit for maintenance.

## How to Invoke

**Browse everything:**
```
/content-browse
```

**Browse by section:**
```
/content-browse copy
/content-browse assets
/content-browse ad-copy
/content-browse email-copy
/content-browse evergreen
```

**Browse by status:**
```
/content-browse status:approved
/content-browse status:in-review
/content-browse status:retired
```

**Browse by campaign:**
```
/content-browse campaign:2026-03-spring-launch
/content-browse campaign:evergreen
```

**Library audit (maintenance view):**
```
/content-browse audit
```
Shows: items missing tags, expired licenses, items flagged for review, broken file paths, items that need performance updates.

## What You Get

A structured view of the library contents organized by category, with counts, status breakdowns, and quick links to individual entries. In audit mode, a prioritized list of maintenance actions.

## Recommended Use

- Run `/content-browse` at the start of a campaign planning session to see what's available before briefing copywriters
- Run `/content-browse audit` quarterly to maintain library health
- Run `/content-browse campaign:[slug]` after a campaign completes to identify copy and assets to store
