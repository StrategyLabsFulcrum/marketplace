# Platform Best Practices Changelog

Running log of all platform updates that have been reviewed and applied to agent reference files. Maintained by the Best Practices Updater.

---

## How to Read This Log

Each entry records:
- The platform that changed
- What specifically changed
- The source URL
- Which reference file was updated
- The date it was applied

This is the institutional memory of the best practices system. Use it to understand why reference files contain the guidance they do, and to track when an update is no longer current.

---

## Changelog Entries

## 2026-03-22 — First Review (Full Platform Crawl)

### Google Ads — Similar Audiences Fully Deprecated
**Source:** https://support.google.com/sa360/answer/13388565 | https://support.google.com/google-ads/answer/13541369
**Announced/Effective:** May 2023 (stopped generating) → August 2023 (removed from all campaigns) → March 2026 (Lookalike Segments shift to AI signals)
**Applied to:** `performance-marketing/skills/performance-marketing/references/audience-targeting-guide.md`
**Summary:** Similar Audiences no longer exist on Google Ads. Replaced by Optimized Targeting (auto-enabled on all campaigns) and Lookalike Segments (Demand Gen only). As of March 2026, Lookalike Segments function as AI signals rather than hard targeting constraints. First-party data quality is now the primary competitive advantage on Google.

---

### Email — MAGY Sender Requirements Now Enforced
**Source:** https://powerdmarc.com/google-and-yahoo-email-authentication-requirements/ | https://www.klaviyo.com/blog/magy-enforcing-authentication-standards
**Announced/Effective:** Gmail/Yahoo Feb 2024 → Microsoft May 2025 → Gmail increased rejections Nov 2025
**Applied to:** `email-copy/skills/email-copy/references/email-frameworks.md` | `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`
**Summary:** Gmail, Yahoo, Microsoft (Outlook/Hotmail/Live), and Apple Mail — covering 90%+ of inboxes — now enforce SPF, DKIM, DMARC, branded sending domain (5K+ lists), one-click unsubscribe honored within 2 days, and spam rates below 0.10%. Non-compliant mail is bounced. Updated compliance checklists in both files.

---

### Meta — 20% Text Overlay Rule Removed
**Source:** https://www.searchenginejournal.com/facebook-removes-the-20-text-limit-on-ad-images/381844/
**Announced/Effective:** 2021 (rule relaxed) → 2023 (enforcement tool removed)
**Applied to:** `art-director/skills/art-director/references/production-specs.md`
**Summary:** The 20% image text rule no longer exists. No rejections or reach restrictions based on image text percentage. Performance guidance (less text still outperforms) preserved; policy framing removed.

---

### Meta — Campaign Objective Names (ODAX) + Advantage+ Default
**Source:** https://www.jonloomer.com/meta-advertising-changes-2025/ | https://www.wordstream.com/blog/facebook-ad-objectives
**Announced/Effective:** 2022–2025 (ODAX rollout); 2025 (Advantage+ as default OS)
**Applied to:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`
**Summary:** ODAX framework complete. Objectives renamed: "Sales/Conversions" → "Sales"; "Awareness/Reach" → "Awareness"; "App Installs" → "App Promotion". Advantage+ is now the default operating system for Sales/Leads/App Promotion. Consolidated single campaigns are the new best practice over siloed funnel campaigns. New placements: Threads, Facebook Notifications.

---

### Google — Performance Max New Controls
**Source:** https://blog.google/products/ads-commerce/new-performance-max-features-2025/
**Announced/Effective:** 2025 (various rollouts); March 2026 (Ads Editor 2.12)
**Applied to:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`
**Summary:** PMax now has campaign-level negative keywords (up to 10,000 terms, Search/Shopping only), channel performance reporting for all accounts, granular brand exclusions for retail, high-value new customer acquisition mode, and age/device targeting in beta. The platform is significantly more transparent and controllable than at launch.

---

### Google — Broad Match + Smart Bidding Now Primary Recommendation
**Source:** https://support.google.com/google-ads/answer/10195720 | https://www.searchscientists.com/broad-match-smart-bidding-2025/
**Announced/Effective:** 2025
**Applied to:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`
**Summary:** Google's current recommended default for established Search campaigns is Broad Match + Smart Bidding + RSA. Switching phrase keywords to broad match yields ~25% more conversions on average per Google data. Requires enhanced conversions and negative keyword lists. Exception: accounts under $2K/month or <15 conversions/month stay on Manual CPC.

---

### TikTok — In-Feed Video Duration Extended to 10 Minutes
**Source:** https://quickframe.mountain.com/blog/tiktok-video-ad-specs/ | https://tikadsuite.com/blog/tiktok-ad-specs/
**Announced/Effective:** July 2025
**Applied to:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md` | `art-director/skills/art-director/references/production-specs.md`
**Summary:** In-Feed Ad max duration updated from 60 seconds to 10 minutes. 15–30 seconds remains optimal for performance. Spark Ads have no duration restriction.

---

### TikTok — TopView Moved to CPM; Search Ads Launched
**Source:** https://admanage.ai/blog/tiktok-ad-specs | https://almcorp.com/blog/tiktok-ads-guide-2026-creator-economy-opportunity/
**Announced/Effective:** 2025
**Applied to:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`
**Summary:** TopView moved from Reservation to CPM buying model. TikTok Search Ads launched — intent-based ads in TikTok search results, strong for bottom-of-funnel. CPM benchmarks updated: $2.60–$6.60 typical (was $8–15 in prior reference).

---

*Next recommended review: 2026-06-22*

---

## Reference Files Index

The following reference files are maintained by the Best Practices Updater:

| File | Platform(s) | Last reviewed |
|------|------------|--------------|
| `ad-copy/skills/ad-copy/references/platform-specs.md` | Meta, Google, TikTok, LinkedIn, Pinterest | Initial |
| `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md` | Meta, Google, TikTok, LinkedIn | 2026-03-22 |
| `performance-marketing/skills/performance-marketing/references/audience-targeting-guide.md` | Meta, Google, LinkedIn, TikTok | 2026-03-22 |
| `performance-marketing/skills/performance-marketing/references/tracking-setup-guide.md` | Meta, Google, GA4 | Initial |
| `email-copy/skills/email-copy/references/email-frameworks.md` | Klaviyo, general email | 2026-03-22 |
| `marketing-analytics/skills/marketing-analytics/references/analyst-frameworks.md` | All platforms | Initial |
| `seo-copy/skills/seo-copy/references/seo-frameworks.md` | Google | Initial |
| `art-director/skills/art-director/references/production-specs.md` | All digital platforms | 2026-03-22 |

---

## Known Platform Update Sources

Quick reference for the Best Practices Updater:

| Platform | Official update source |
|---------|----------------------|
| Meta Ads | business.facebook.com/news + developers.facebook.com/docs/marketing-api/changelog |
| Google Ads | ads.google.com blog + support.google.com/google-ads |
| GA4 | support.google.com/analytics |
| Klaviyo | klaviyo.com/blog + help.klaviyo.com |
| TikTok for Business | tiktok.com/business/blog + ads.tiktok.com help |
| LinkedIn Marketing | business.linkedin.com/marketing-solutions/blog |
| Pinterest Ads | business.pinterest.com/blog |
| Email deliverability | litmus.com/blog + mailtrap.io/blog (secondary research) |
| SEO / Google Search | developers.google.com/search/updates + searchcentral.googleblog.com |
