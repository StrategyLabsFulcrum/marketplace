# Video Content Strategist

Plans, structures, and scripts video content across all formats — YouTube strategy, TikTok/Reels content plans, video ad scripts, content calendars, and series development.

This agent produces strategy documents and scripts — the intellectual layer that directs video production. It does not produce video files.

---

## What This Agent Does

| Mode | Use Case |
|------|----------|
| `channel-strategy` | Full YouTube or TikTok channel positioning, pillars, series |
| `content-calendar` | Monthly or quarterly publishing plan |
| `script` | Full script or outline for a specific video |
| `video-ad` | Paid video ad scripts with hook variations |
| `series` | Multi-episode series concept and arc |
| `ugc-brief` | Creator briefs for UGC-style content |

---

## Slash Commands

| Command | Use |
|---------|-----|
| `/video-script` | Full script for any video format — organic, paid, or UGC brief |
| `/video-calendar` | Monthly or quarterly content calendar |
| `/channel-strategy` | Complete YouTube or TikTok channel strategy |

---

## Platform Approach

### YouTube
Search engine + subscription platform. Requires consistent publishing on focused topics. Evergreen content compounds. The channel positioning must be specific enough to earn subscribers.

### TikTok
Discovery platform. The algorithm serves content to non-followers. Every video must earn attention in the first 2 seconds — there is no brand loyalty to rely on.

### Instagram Reels
Reels reach non-followers; feed posts reach followers. Reels for growth, feed for community. Higher aesthetic polish expected versus TikTok.

### Paid Video Ads
Viewers are actively trying to skip. The hook must land in the first 3 seconds. Structure and CTA clarity matter more than production value.

---

## Integration with the Campaign System

```
Campaign Strategist → Campaign Brief
        ↓
Video Content Strategist → Scripts + Content Calendar
        ↓
Art Director → Thumbnail design + visual direction for video
Graphic Design Agent → Motion graphics specs, title cards
        ↓
Performance Marketing Agent → Deploys video ads (receives ad script + creative brief)
        ↓
Marketing Analytics → Reviews video performance (view rate, completion, CVR)
        ↓
Content Library → Stores top-performing scripts for future reuse
```

---

## Output Structure

```
campaigns/[slug]/video-strategy/
├── scripts/
│   └── [video-slug]-script.md
├── content-calendar-[month].md
└── ugc-video-brief.md

brand-assets/video-strategy/
└── channel-strategy-[platform].md
```
