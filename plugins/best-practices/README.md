# Best Practices Updater

Crawls official platform documentation from Meta, Google, Klaviyo, TikTok, LinkedIn, and other platforms to surface changes that should be reflected in agent reference files. Produces structured update reports with before/after text. No reference file edits without approval.

The marketing landscape changes constantly. Platform algorithms update. Character limits change. New ad formats launch. Bidding strategies are renamed or deprecated. Email deliverability standards evolve. This plugin ensures every agent in the system is operating on current, accurate best practices — not documentation that was accurate 18 months ago.

---

## Slash Command

```
/best-practices-review
```

Runs a full review of all platforms and produces a prioritized update report.

**Scope options:**
```
/best-practices-review                      ← all platforms
/best-practices-review meta                 ← specific platform
/best-practices-review email-deliverability ← specific topic
/best-practices-review google               ← specific platform
```

---

## What the Review Produces

A structured update report saved to `best-practices/reports/update-report-{{date}}.md` with three priority tiers:

| Priority | Timeframe | Example |
|----------|-----------|---------|
| 🔴 High | Act within 7 days | Platform deprecates a targeting option agents still recommend |
| 🟡 Medium | Act within 30 days | Character limits change on a platform |
| 🟢 Low / Informational | Update at next review | New ad format launched worth knowing about |

Each recommended change includes:
- The specific change and why it matters
- Source URL and announcement date
- Which reference file to update
- **Exact before/after text** for the recommended edit

---

## Reference Files Maintained

| Reference File | Platform(s) |
|---------------|-------------|
| `ad-copy/skills/ad-copy/references/platform-specs.md` | Meta, Google, TikTok, LinkedIn, Pinterest |
| `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md` | Meta, Google, TikTok, LinkedIn |
| `performance-marketing/skills/performance-marketing/references/audience-targeting-guide.md` | Meta, Google, LinkedIn, TikTok |
| `performance-marketing/skills/performance-marketing/references/tracking-setup-guide.md` | Meta, Google, GA4 |
| `email-copy/skills/email-copy/references/email-frameworks.md` | Klaviyo, general email |
| `marketing-analytics/skills/marketing-analytics/references/analyst-frameworks.md` | All platforms |
| `seo-copy/skills/seo-copy/references/seo-frameworks.md` | Google |
| `art-director/skills/art-director/references/production-specs.md` | All digital platforms |

---

## Approval Flow

No reference files are modified without explicit approval.

After the update report is presented:
- Review each recommended change
- Approve individual changes or all changes at once
- The agent makes the edits and logs every change in `best-practices/skills/best-practices/references/platform-changelog.md`

The changelog is the institutional memory of the system — it records what changed, when, why, and which file was updated, so any agent or human can understand the history.

---

## Recommended Cadence

| Schedule | Scope |
|---------|-------|
| Weekly | Quick scan for breaking announcements only |
| Monthly | Full active platform review |
| Quarterly | Comprehensive review including benchmarks |
| Triggered | When a major platform update is announced |

---

## Platforms Covered

- **Meta** (Facebook/Instagram Ads): Business Help Center, Ads Manager updates, Marketing API changelog
- **Google Ads**: Help Center, Google Ads blog, Performance Max updates, Smart Bidding changes
- **Google Analytics 4**: GA4 changelog, measurement updates
- **Klaviyo**: Product updates blog, deliverability documentation
- **TikTok for Business**: Ads Manager updates, creative best practices
- **LinkedIn Marketing**: Campaign Manager updates, ad format specs
- **Pinterest Ads**: Business help, ad specs
- **General**: Email deliverability (DMARC/SPF/DKIM), iOS privacy changes, cookie deprecation
