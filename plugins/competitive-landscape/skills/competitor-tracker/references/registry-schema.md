# Competitor Registry Schema Reference

Complete field definitions, validation rules, and examples for the competitor registry.

---

## Registry File: `competitors/registry.json`

### Top-Level Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `last_updated` | string (ISO date) | yes | Date of last modification |
| `brand` | object | yes | The user's own brand info |
| `competitors` | array | yes | List of competitor entries |

### Brand Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | yes | Brand name |
| `website` | string | yes | Brand homepage URL |
| `industry` | string | no | Industry vertical (e.g., "powersports", "ecommerce", "SaaS") |

### Competitor Entry

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `id` | string | yes | — | URL-safe slug (lowercase, hyphens only) |
| `name` | string | yes | — | Display name |
| `website` | string | yes | — | Homepage URL (include https://) |
| `status` | enum | yes | `"active"` | `"active"` or `"inactive"` |
| `added` | string (ISO date) | yes | today | Date competitor was added |
| `color` | string (hex) | yes | auto-assign | Primary brand color |
| `colorDark` | string (hex) | yes | auto-derive | Darker variant (15% less lightness) |
| `notes` | string | no | `""` | Why this competitor is being tracked |
| `categories` | array of strings | yes | `["direct"]` | One or more of: `direct`, `indirect`, `aspirational` |
| `meta_ads_library_url` | string | no | auto-generate | Facebook Ad Library search URL |
| `google_ads_transparency_url` | string | no | `""` | Google Ads Transparency Center URL |

---

## Slug Generation Rules

1. Convert name to lowercase.
2. Replace spaces and underscores with hyphens.
3. Remove all characters except `a-z`, `0-9`, and `-`.
4. Collapse multiple hyphens to single.
5. Trim leading/trailing hyphens.

**Examples**:
- `"Super ATV"` → `super-atv`
- `"4 Wheel Parts"` → `4-wheel-parts`
- `"RevZilla (Cycle Gear)"` → `revzilla-cycle-gear`

---

## Meta Ads Library URL Pattern

Auto-generate from competitor name:
```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q={{url_encoded_name}}
```

If the user provides a Facebook Page ID, use:
```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&view_all_page_id={{page_id}}
```

---

## Google Ads Transparency URL Pattern

Requires an advertiser ID (not always available). If unknown, leave blank:
```
https://adstransparency.google.com/advertiser/{{advertiser_id}}
```

The user can find this by searching for the brand at `https://adstransparency.google.com`.

---

## Validation Rules

1. **Unique IDs**: No two competitors may share the same `id`.
2. **Unique colors**: Warn if two active competitors share the same `color`.
3. **URL format**: `website` must start with `http://` or `https://`.
4. **Active minimum**: Warn if fewer than 2 active competitors (analysis is more valuable with comparison).
5. **Category required**: At least one category must be assigned.

---

## Example Registry

```json
{
  "last_updated": "2026-03-17",
  "brand": {
    "name": "Rugged Terrain",
    "website": "https://ruggedterrain.com",
    "industry": "powersports"
  },
  "competitors": [
    {
      "id": "super-atv",
      "name": "SuperATV",
      "website": "https://www.superatv.com",
      "status": "active",
      "added": "2026-03-17",
      "color": "#E8B100",
      "colorDark": "#B89000",
      "notes": "Largest direct competitor in UTV parts. Frequently mentioned by customers.",
      "categories": ["direct"],
      "meta_ads_library_url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=SuperATV",
      "google_ads_transparency_url": ""
    },
    {
      "id": "revzilla",
      "name": "RevZilla",
      "website": "https://www.revzilla.com",
      "status": "active",
      "added": "2026-03-17",
      "color": "#FF3300",
      "colorDark": "#CC2900",
      "notes": "Motorcycle/powersports gear. Strong content marketing and customer experience.",
      "categories": ["indirect", "aspirational"],
      "meta_ads_library_url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=RevZilla",
      "google_ads_transparency_url": ""
    }
  ]
}
```

---

## Directory Structure Per Competitor

When a competitor is added, create:

```
competitive-landscape/competitors/{{id}}/
├── profile.md          # Overview and key observations
├── ads/                # Ad analysis snapshots (populated by ad-analyzer)
│   ├── meta/
│   └── google/
└── journeys/           # Journey analysis (populated by journey-mapper)
```
