# Tracking Setup Guide

End-to-end tracking configuration for every campaign. Tracking is not optional — it is the foundation that makes optimization possible. A campaign without proper tracking is a campaign you cannot improve.

---

## Tracking Architecture Overview

Every campaign needs three layers of tracking working together:

```
Layer 1: UTM Parameters
  → Tag every paid URL → passes source data to GA4

Layer 2: Platform Pixels / Tags
  → Installed on website → fires events → feeds platform optimization algorithms

Layer 3: Conversion Events
  → Defined in each platform → tells the algorithm what you're optimizing for
```

All three must be in place and verified before launch. Weakness in any layer corrupts the data across the entire system.

---

## Layer 1: UTM Parameters

### Standard UTM Structure

Every paid link in every ad and email must carry UTM parameters. No exceptions.

| Parameter | Purpose | Values |
|-----------|---------|--------|
| `utm_source` | Which platform sent the traffic | `meta`, `google`, `linkedin`, `tiktok`, `email`, `klaviyo` |
| `utm_medium` | What type of paid media | `paid-social`, `cpc`, `display`, `email`, `sms` |
| `utm_campaign` | Which campaign | `{{campaign-slug}}` — always use the folder slug |
| `utm_content` | Which specific ad or email | `{{creative-identifier}}` — descriptive, no spaces |
| `utm_term` | Keyword (Search) or audience (Social) | `{{keyword}}` or `{{audience-name}}` — optional |

### UTM Naming Conventions

**utm_source values (lowercase, no spaces):**
```
meta
google
linkedin
tiktok
pinterest
email
klaviyo
mailchimp
sms
organic (for non-paid, tracking only)
```

**utm_medium values:**
```
paid-social    ← Meta, LinkedIn, TikTok, Pinterest
cpc            ← Google Search, Microsoft Search
display        ← Google Display, programmatic
email          ← all email marketing
sms            ← text/SMS campaigns
```

**utm_content format:**
```
{{format}}-{{hook-type}}-{{version}}

Examples:
static-beforeafter-v1
video-problemfirst-v2
carousel-social-proof-v1
email-subject-discount-v1
```

**utm_campaign:** Always match the campaign folder slug exactly:
```
2026-03-spring-launch
2026-04-customer-retention
```

### Building UTM URLs

Manual URL builder pattern:
```
https://yourdomain.com/landing-page
  ?utm_source=meta
  &utm_medium=paid-social
  &utm_campaign=2026-03-spring-launch
  &utm_content=static-beforeafter-v1
```

Full example:
```
https://acmeco.com/spring-offer?utm_source=meta&utm_medium=paid-social&utm_campaign=2026-03-spring-launch&utm_content=static-beforeafter-v1&utm_term=lookalike-purchasers-1pct
```

### UTM Parameter Table

Generate a complete table for every ad variant and email in the campaign.

Save to `campaigns/{{slug}}/activation/utm-parameters.md`.

Format:
```markdown
# UTM Parameters — {{Campaign Name}}

## Meta Ads

| Ad Name | Destination URL | Full Tagged URL |
|---------|----------------|----------------|
| {{Ad 1 name}} | {{base URL}} | {{full URL with UTMs}} |
| {{Ad 2 name}} | {{base URL}} | {{full URL with UTMs}} |

## Google Ads

| Ad Group | Ad Variant | Destination URL | Full Tagged URL |
|---------|-----------|----------------|----------------|
| {{Ad Group}} | {{Ad}} | {{URL}} | {{full URL with UTMs}} |

## Email

| Email Name | Link Description | Full Tagged URL |
|-----------|----------------|----------------|
| {{Email 1}} | CTA button | {{full URL with UTMs}} |
| {{Email 1}} | Image link | {{full URL with UTMs}} |
```

**Note on Google Ads:** Google Search auto-tags with `gclid` for its own reporting. Still use UTMs for GA4 attribution — they work alongside `gclid`. In Google Ads, add UTMs in the "Final URL suffix" field at campaign or ad group level to avoid overriding manually set UTMs per ad.

---

## Layer 2: Platform Pixels and Tags

### Meta Pixel

**Installation:**
1. Go to Meta Events Manager → Data Sources → Add Data Source → Web
2. Get the Pixel ID
3. Install via one of three methods:

   **Method A — Direct code installation:**
   Paste base code in `<head>` of every page. Add event codes on specific pages.

   **Method B — Google Tag Manager:**
   Install Meta Pixel template in GTM → enter Pixel ID → fire on All Pages trigger.
   Add custom event tags for conversion events.

   **Method C — Platform native integration:**
   Shopify, WordPress, Squarespace have native Meta Pixel integrations — simplest method if on these platforms.

**Base Pixel code (for direct installation):**
```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<!-- End Meta Pixel Code -->
```

**Verification:** Install Meta Pixel Helper browser extension → visit site → confirm Pixel is firing and PageView is recording.

### Meta Conversion API (CAPI)

The Pixel fires from the browser. CAPI sends the same events from the server — this is the redundancy layer that preserves data when users block cookies or use iOS privacy features.

Meta recommends running both Pixel + CAPI with the same events for best signal quality.

CAPI setup: Meta Events Manager → Data Sources → your Pixel → Settings → Conversions API → Set Up. Use GTM partner integration or platform native (Shopify, WooCommerce) for simplest setup.

**Event Match Quality (EMQ):** Score 6+ is good. Score 8+ is excellent. Improve EMQ by sending hashed customer data with events (email address, phone number, name, external ID). These are hashed client-side — never sent in plain text.

### Google Tag (formerly Global Site Tag / gtag.js)

**Installation:**
1. Go to Google Ads → Tools → Conversions → Google Tag
2. Get the Google Tag ID (format: AW-XXXXXXXXX)
3. Install via:

   **Method A — Google Tag Manager:** Add Google Ads Conversion Tracking template to GTM → enter Conversion ID and Label → trigger on conversion page.

   **Method B — Direct code:**
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXX');
</script>
```

**Verification:** Google Tag Assistant (browser extension) → visit site → confirm tag fires.

### GA4 (Google Analytics 4)

**Installation:**
1. Create GA4 property in Google Analytics → get Measurement ID (format: G-XXXXXXXXXX)
2. Install via:

   **Method A — Google Tag Manager (recommended):** GA4 Configuration tag → enter Measurement ID → All Pages trigger.

   **Method B — Google Site Kit (WordPress):** Plugin handles installation.

   **Method C — Direct code:**
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**GA4 and Google Ads linking:** Link GA4 property to Google Ads account. This enables:
- GA4 conversion imports into Google Ads
- Google Ads dimensions in GA4 reports
- Audiences built in GA4 available for Google Ads targeting

---

## Layer 3: Conversion Events

### Meta Conversion Events

**Standard Events (use these — avoid custom events when a standard event fits):**

| Event | When It Fires | Parameters |
|-------|--------------|------------|
| `PageView` | Every page | (automatic from base code) |
| `ViewContent` | Product/landing page | `content_id`, `content_name`, `content_type`, `value`, `currency` |
| `AddToCart` | Cart add | `content_id`, `content_name`, `value`, `currency` |
| `InitiateCheckout` | Checkout page load | `value`, `currency`, `num_items` |
| `AddPaymentInfo` | Payment step | `value`, `currency` |
| `Purchase` | Order confirmation | `value`, `currency`, `content_ids`, `num_items` |
| `Lead` | Form submission | `value` (optional), `currency` |
| `CompleteRegistration` | Account/signup completion | `status` |
| `Contact` | Contact form / inquiry | — |
| `Subscribe` | Email list join | — |

**Event code example (Purchase event — paste on order confirmation page):**
```html
<script>
fbq('track', 'Purchase', {
  value: ORDER_TOTAL,    // Replace with dynamic order value
  currency: 'USD',
  content_ids: [PRODUCT_ID],
  content_type: 'product',
  num_items: QUANTITY
});
</script>
```

**Optimization event selection:**
- Campaign objective is Conversions → select the event you want Meta to optimize for
- Use the **lowest-funnel event that has enough volume** (50+ per week per ad set for learning phase)
- If Purchase has <50/week: optimize for AddToCart or InitiateCheckout instead → switch to Purchase once volume increases

### Google Ads Conversion Actions

Create a conversion action for each key event:

1. Google Ads → Goals → Conversions → + New Conversion Action → Website
2. Settings:
   - **Category:** Purchase, Lead, Page view, Sign-up, etc.
   - **Value:** Use the same value for each conversion / Use input values / Don't use values
   - **Count:** One (for purchases — avoid counting duplicate conversions) or Every (for leads if multiple leads from one person are valuable)
   - **Click-through conversion window:** 30 days (default); 90 days for longer consideration cycles
   - **View-through conversion window:** 1 day (default)
   - **Attribution model:** Data-driven (if available); Linear otherwise

3. Tag the conversion action using GTM or direct code
4. Mark the most important conversion action as "Primary" — this is what smart bidding optimizes for
5. Mark secondary actions (page views, add-to-cart) as "Secondary" — they inform reporting but don't drive optimization

**Enhanced conversions:** Upload hashed customer data (email) with conversions → improves match rate → required for accurate measurement post-iOS privacy changes. Enable in Google Ads conversion settings → follow setup instructions for your platform.

### GA4 Events as Conversions

In GA4:
1. Configure → Events — find or create the key event
2. Toggle "Mark as conversion" → it becomes available for Google Ads import
3. In Google Ads → Tools → Conversions → Google Analytics 4 properties → import

Key events to mark as conversions in GA4:
- `purchase`
- `generate_lead`
- `sign_up`
- `begin_checkout`
- Custom events for significant engagement milestones

---

## Tracking Verification Checklist

Save completed checklist to `campaigns/{{slug}}/activation/tracking-verification.md`.

```markdown
# Tracking Verification — {{Campaign Name}}
**Completed by:** Performance Marketing Agent
**Date:** {{date}}
**Status:** ✅ Verified / ⚠️ Issues / ❌ Blocked

---

## UTM Parameters
- [ ] UTM parameter table complete (utm-parameters.md)
- [ ] All destination URLs tagged
- [ ] UTMs verified to pass through to GA4 (test using UTM Builder + visit URL → check GA4 real-time)
- [ ] Campaign name matches slug exactly

---

## Meta Pixel
- [ ] Pixel ID: {{ID}}
- [ ] Base code installed on all pages (verified with Pixel Helper)
- [ ] PageView fires on page load
- [ ] {{Purchase / Lead / CompleteRegistration}} event fires on conversion page
- [ ] Event parameters correct (value, currency, content_id)
- [ ] Conversions API (CAPI) configured: Yes / No / In progress
- [ ] Event Match Quality score: {{score}} (target: 6+)

**Issues found:** {{None / describe issues}}

---

## Google Tag
- [ ] Google Tag ID: AW-{{ID}}
- [ ] Tag fires on all pages (verified with Tag Assistant)
- [ ] Conversion action created: {{name}}
- [ ] Conversion tag fires on confirmation page
- [ ] Conversion value captured correctly
- [ ] Enhanced conversions configured: Yes / No
- [ ] GA4 property linked to Google Ads

**Issues found:** {{None / describe issues}}

---

## GA4
- [ ] Measurement ID: G-{{ID}}
- [ ] GA4 receiving page view data (verified in real-time report)
- [ ] Key events marked as conversions: {{list events}}
- [ ] UTM parameters appearing in Traffic Acquisition report (test with tagged URL)
- [ ] Source/medium correctly attributed (not showing as direct)

**Issues found:** {{None / describe issues}}

---

## Pre-Launch Decision
- All tracking verified: ✅ / ❌
- Known issues (non-blocking): {{list or none}}
- Blocking issues: {{list or none}}
- **Launch cleared:** Yes / No — {{reason if No}}
```

---

## Common Tracking Issues and Fixes

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| UTM parameters not appearing in GA4 | URL redirect stripping UTMs | Add UTMs after the redirect target URL; check with GA4 real-time while visiting tagged URL |
| Meta Pixel not firing | Code in wrong location | Move pixel code to `<head>` section; or GTM trigger firing too late |
| Purchase event not firing | Event code on wrong page | Verify event is on confirmation/thank-you page, not checkout page |
| Meta shows conversions but GA4 doesn't | Platform attribution difference | Expected — Meta uses click + view attribution; GA4 uses session-based. Compare within each platform, not across. |
| Google Ads conversion count much lower than GA4 | Attribution window difference | Check conversion window settings; verify GA4 import is correctly configured |
| Conversion value showing $0 | Dynamic value not being passed | Check the `value` parameter in the event code; ensure it pulls from order total variable |
| All traffic in GA4 shows as Direct | UTM parameters being stripped | Check for URL redirects; check tag fires before redirect; test with direct UTM URL |
| Meta Event Match Quality below 6 | Missing customer data parameters | Add hashed email/phone to event code; configure Conversions API |

---

## Ongoing Tracking Maintenance

After launch:

**Week 1 check:** Verify all events are firing in production (test actual purchase/lead submission if possible). Confirm data is flowing to all platforms.

**Ongoing:** Check for tracking breakage after site updates, platform migrations, or theme changes. A broken pixel is often discovered weeks later when performance appears to drop — but the campaign was actually running fine and just not tracking.

**Flag to Marketing Analytics:** If tracking breaks mid-campaign, flag immediately. Data from the period without tracking must be noted in the analytics report with appropriate caveats.
