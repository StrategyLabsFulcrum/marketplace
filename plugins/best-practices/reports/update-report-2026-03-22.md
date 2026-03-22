# Best Practices Update Report
**Review date:** 2026-03-22
**Platforms reviewed:** Meta, Google Ads, TikTok, Email (Gmail/Yahoo/Microsoft/Klaviyo)
**Reviewed by:** Best Practices Updater (automated crawl)
**Status:** Awaiting approval before applying changes

---

## How These Were Originally Generated

The reference files were **hand-authored at initial plugin build time** — written from knowledge, not crawled from live documentation. No reviews have ever been run. The platform changelog confirms: "no entries yet — this is a new system." Based on content, the files were written approximately late 2024. Several platforms have made significant changes since then.

---

## 🔴 High Priority Updates (Act within 7 days)

---

### Google Ads — Similar Audiences Fully Deprecated (CRITICAL)

**What changed:** Google fully removed Similar Audiences from all campaigns in **August 2023**. The feature stopped generating new audiences in May 2023 and was removed from all existing campaigns in August 2023. As of March 2026, even the replacement (Lookalike Segments for Demand Gen) is shifting from hard targeting constraints to AI signals.

**Source:** [Google SA360 Help](https://support.google.com/sa360/answer/13388565) | [Google Ads Lookalike Segments](https://support.google.com/google-ads/answer/13541369) | [ALM Corp March 2026](https://almcorp.com/blog/google-lookalike-audiences-ai-signals-demand-gen-march-2026/)

**Date effective:** August 2023 (deprecation); March 2026 (Lookalike Segments shift to AI signals)

**Impact:** 🚨 The reference file instructs agents to build "Similar Audiences" on Google — a feature that no longer exists. Any campaign setup following this guidance will fail.

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/audience-targeting-guide.md`

**Before:**
```
- **Google:** Similar Audiences (now Optimized Targeting in PMax). Upload customer list to Google Ads; Google generates similar audiences automatically.
```

**After:**
```
- **Google:** Similar Audiences were fully deprecated August 2023 and no longer exist. Replacements:
  - **Optimized Targeting** (Search/Display/PMax): Automatically enabled on all campaigns. Include first-party data segments (Customer Match lists, website visitors) as signals — Google AI finds new audiences based on them. No manual lookalike setup required.
  - **Lookalike Segments** (Demand Gen campaigns only): Upload a seed audience (Customer Match, website visitors, YouTube engagers) with minimum 100 users. As of March 2026, these function as AI signals rather than hard targeting constraints — the reach level and seed list guide the algorithm but no longer restrict reach to a fixed similarity percentage.
  - **Customer Match** is now the primary first-party tool across all campaign types. The quality of your CRM/customer list is the primary competitive advantage.
```

---

### Email — MAGY Sender Requirements Now Enforced (CRITICAL)

**What changed:** Gmail and Yahoo began enforcing bulk sender authentication requirements in **February 2024**. Microsoft (Outlook/Hotmail/Live) joined in **May 2025**. Together these four inbox providers (Microsoft, Apple, Gmail, Yahoo — "MAGY") cover 90%+ of typical email lists. Requirements are no longer best practices — they are enforced with bounces and rejections.

**Source:** [PowerDMARC](https://powerdmarc.com/google-and-yahoo-email-authentication-requirements/) | [Klaviyo Gmail/Yahoo Update](https://www.klaviyo.com/blog/gmail-update) | [Klaviyo MAGY Article](https://www.klaviyo.com/blog/magy-enforcing-authentication-standards)

**Date effective:** February 2024 (Gmail/Yahoo); May 2025 (Microsoft); November 2025 (Gmail increased rejections)

**Impact:** 🚨 The current deliverability checklist is incomplete. Missing: Microsoft enforcement, one-click unsubscribe within 2 days (not just present), spam rate thresholds, no @gmail/@yahoo from addresses, branded sending domain requirement.

**Affected reference file:** `email-copy/skills/email-copy/references/email-frameworks.md` (compliance checklist) AND `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md` (Klaviyo deliverability checklist)

**Before (email-frameworks.md compliance section):**
```
**General deliverability:**
- [ ] Avoid spam trigger words in subject: "FREE", "GUARANTEED", "ACT NOW", "!!!", all caps
- [ ] Plain text version matches HTML version (required for some ISPs)
- [ ] Image-to-text ratio: do not send emails that are primarily one large image with minimal text
- [ ] From name is recognizable and consistent (not a random email address)
```

**After:**
```
**MAGY Authentication Requirements (Gmail, Yahoo, Microsoft, Apple — enforced, not optional):**
- [ ] SPF record configured for sending domain
- [ ] DKIM record configured (minimum 1024-bit key; 2048-bit recommended)
- [ ] DMARC policy configured (minimum p=none; p=quarantine or p=reject preferred)
- [ ] "From" address uses your own domain — never @gmail.com or @yahoo.com
- [ ] Branded sending domain configured (required for lists over 5,000 profiles)
- [ ] One-click unsubscribe header present AND requests honored within 2 days
- [ ] Spam rate below 0.10% (monitor via Google Postmaster Tools); above 0.30% = sending blocked
- [ ] Microsoft enforcement active as of May 2025 — same SPF/DKIM/DMARC requirements apply to Outlook/Hotmail/Live recipients

**General deliverability:**
- [ ] Avoid spam trigger words in subject: "FREE", "GUARANTEED", "ACT NOW", "!!!", all caps
- [ ] Plain text version matches HTML version (required for some ISPs)
- [ ] Image-to-text ratio: do not send emails that are primarily one large image with minimal text
- [ ] From name is recognizable and consistent (not a random email address)
```

---

### Meta — 20% Text Overlay Rule Removed

**What changed:** Meta removed the 20% text overlay rule and the overlay tool. Ads with any amount of text are no longer rejected or reach-restricted based on image text percentage. The tool no longer exists. The reference file still instructs agents to keep text "under 20% of image area for best delivery" — referencing a policy that no longer exists in that form.

**Source:** [Search Engine Journal](https://www.searchenginejournal.com/facebook-removes-the-20-text-limit-on-ad-images/381844/) | [Social Media Today](https://www.socialmediatoday.com/social-networks/facebooks-changed-20-ad-image-text-overlay-rule)

**Date effective:** 2021 (rule relaxed); 2023 (tool fully removed)

**Impact:** ⚠️ Agents referencing the 20% rule may incorrectly advise clients their ads will be penalized. The guidance should reflect current reality while preserving the underlying performance truth (less text still performs better).

**Affected reference file:** `ad-copy/skills/ad-copy/references/platform-specs.md`

**Before:**
```
- Text overlay: Under 20% of image area for best delivery
```

**After:**
```
- Text overlay: The 20% text rule was removed by Meta in 2021–2023. Ads are no longer rejected or reach-restricted based on image text percentage. However, Meta's own performance data shows ads with minimal text still outperform heavy-text images — keep overlays minimal for performance reasons, not policy reasons.
```

---

### TikTok — In-Feed Video Duration Extended to 10 Minutes

**What changed:** As of July 2025, TikTok updated In-Feed Ad specs to support video duration up to **10 minutes** (previously 60 seconds). Spark Ads have no duration restriction. The reference file still states "15–60 seconds" as the max.

**Source:** [QuickFrame TikTok Specs 2026](https://quickframe.mountain.com/blog/tiktok-video-ad-specs/) | [TikAdSuite](https://tikadsuite.com/blog/tiktok-ad-specs/)

**Date effective:** July 2025

**Impact:** ⚠️ Production teams and creative briefs following the old spec will unnecessarily limit video length for long-form content.

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md` and `art-director/skills/art-director/references/production-specs.md`

**Before:**
```
- 15–60 seconds (15–30s performs best)
```

**After:**
```
- Up to 10 minutes (updated July 2025). 15–30 seconds still performs best for most ads — higher completion rates and FYP distribution. Longer format only warranted for in-depth storytelling or product demos. Spark Ads have no duration restriction.
```

---

## 🟡 Medium Priority Updates (Act within 30 days)

---

### Google Ads — Performance Max Now Has Campaign-Level Negative Keywords

**What changed:** Campaign-level negative keywords (up to 10,000 terms) are now available to all PMax advertisers. Channel performance reporting is now available to all campaigns (previously beta only). Age-based demographic exclusions and device targeting are in beta.

**Source:** [Google Blog: New PMax Features 2025](https://blog.google/products/ads-commerce/new-performance-max-features-2025/) | [WordStream 2025 Updates](https://www.wordstream.com/blog/2025-google-ads-updates)

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`

**Before:**
```
- **Brand exclusions:** Exclude your own brand terms from PMax if running a separate Brand Search campaign
```

**After:**
```
- **Negative keywords:** Campaign-level negative keywords now available to all advertisers (up to 10,000 terms). Blocks Search and Shopping inventory only — does not prevent ads on Display, YouTube, Gmail, or Discover.
- **Brand exclusions:** Exclude your own brand terms from PMax if running a separate Brand Search campaign. Granular brand exclusions now available for retail advertisers — can apply to Search ads only while keeping branded Shopping traffic.
- **Channel performance reporting:** Now available to all campaigns — shows clicks, conversions, cost broken down by YouTube, Display, Search, Discover, Gmail, Maps.
- **Demographic exclusions:** Age-based demographic exclusions in beta — contact Google Ads support to enroll.
```

---

### Meta — Campaign Objectives Renamed (ODAX) + Advantage+ Now Default

**What changed:** Meta completed the ODAX framework rollout. The 6 current objectives are: **Awareness, Traffic, Engagement, Leads, App Promotion, Sales**. "Sales (Conversions)" is now just "Sales." "Awareness (Reach)" is now "Awareness." Advantage+ is now the default operating system — consolidated campaigns are the new best practice over siloed funnel stages. New placements added: Threads and Facebook Notifications.

**Source:** [Jon Loomer: 83 Changes 2025](https://www.jonloomer.com/meta-advertising-changes-2025/) | [WordStream Facebook Ad Objectives 2026](https://www.wordstream.com/blog/facebook-ad-objectives)

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`

**Before:**
```
| Sales (Conversions) | Driving purchases, sign-ups with defined value... |
| Awareness (Reach) | Upper funnel — maximizing reach within a defined audience... |
```

**After:**
```
| Sales | Driving purchases, sign-ups with defined value... (formerly "Sales/Conversions") |
| Awareness | Upper funnel — maximizing reach within a defined audience... (formerly "Awareness/Reach") |

**Advantage+ note:** Advantage+ is now Meta's default campaign operating system, strongly applied to Sales, Leads, and App Promotion objectives. Meta's best practice (2025–2026) is one consolidated campaign rather than separate top/middle/bottom funnel campaigns — consolidation accelerates learning and improves optimization. New placements added: Threads and Facebook Notifications.
```

---

### Google Ads — Broad Match + Smart Bidding Is Now the Primary Recommendation

**What changed:** Google's recommended search campaign setup is now **Broad Match + Smart Bidding + RSA** as the primary trifecta. The current file lists broad match as "use with Smart Bidding" but doesn't reflect that Google now actively recommends it as the default for established campaigns. For accounts under $2K/month or <15 conversions/month, manual CPC is still appropriate.

**Source:** [Google: Broad Match + Smart Bidding](https://support.google.com/google-ads/answer/10195720) | [Search Scientists 2025](https://www.searchscientists.com/broad-match-smart-bidding-2025/)

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`

**Before:**
```
- **Broad match:** Highest volume, least control. Only use with Smart Bidding (Target CPA or Target ROAS) — requires conversion data for Google to optimize broad queries effectively.
```

**After:**
```
- **Broad match:** Highest volume, most AI-optimized. Google's current recommended default for established campaigns — pair with Smart Bidding (Target CPA or Target ROAS) and RSA. Advertisers switching phrase keywords to broad match see ~25% more conversions on average per Google's data. Requires robust conversion tracking and negative keyword lists to work effectively. **Exception:** Accounts spending under $2,000/month or with fewer than 15 conversions/month should stay on Manual CPC until volume supports Smart Bidding.
```

---

### TikTok — TopView Moved to CPM Buying; New Search Ads Available

**What changed:** TopView moved from Reservation to CPM buying model. TikTok Search Ads are now available — targeting intent-driven users on TikTok's search function. These are significant for bottom-of-funnel targeting.

**Source:** [AdManage.ai TikTok Specs 2026](https://admanage.ai/blog/tiktok-ad-specs) | [ALM Corp TikTok 2026](https://almcorp.com/blog/tiktok-ads-guide-2026-creator-economy-opportunity/)

**Affected reference file:** `performance-marketing/skills/performance-marketing/references/platform-setup-guide.md`

---

## 🟢 Low Priority / Informational

### Meta — Attribution Window Shortened; Incremental Attribution Added

Engaged-view attribution threshold dropped from 10 seconds to 5 seconds (2025). Incremental Attribution (measures only conversions that wouldn't have happened without the ad) introduced. No immediate reference file update needed — relevant when interpreting Meta reporting.

### Google — Smart Bidding Exploration (New Feature)

Google introduced Smart Bidding Exploration — allows flexible ROAS targets to explore new traffic. Campaigns using it see ~18% increase in unique query categories with conversions. Note when briefing Google campaigns for growth objectives.

### Google Ads — Call-Only Ads Being Deprecated February 2026

Google is ending Call Ads in February 2026 and shifting advertisers to RSA format with call assets. The `platform-specs.md` includes a "Call-Only Ad" section that will become obsolete.

**Source:** [PPC Land](https://ppc.land/google-ends-call-ads-in-february-2026-shifts-advertisers-to-rsa-format/)

### TikTok CPM Benchmarks Need Updating

Current reference shows TikTok CPMs at $8–15. Current data shows $2.60–$6.60 typical range (seasonal peaks $8–10). Consider updating the analyst-frameworks.md benchmark table.

---

## Summary

| Priority | Count | Reference Files Requiring Updates |
|---|---|---|
| 🔴 High | 4 | audience-targeting-guide.md, email-frameworks.md, platform-setup-guide.md (Klaviyo section), ad-copy/platform-specs.md, art-director/production-specs.md |
| 🟡 Medium | 4 | platform-setup-guide.md (Meta objectives, PMax controls, broad match), platform-setup-guide.md (TikTok) |
| 🟢 Low / Informational | 4 | No immediate action required |

**Next recommended review:** 2026-06-22 (quarterly)

---

*Report generated: 2026-03-22. Sources crawled: Meta Business, Google Ads Help, TikTok Ads documentation, Gmail/Yahoo sender requirement pages, Klaviyo Help Center, industry publications.*
