# House of Meroë Search / Indexing Checklist

Production domain: https://houseofmeroe.com
Sitemap: https://houseofmeroe.com/sitemap.xml
Robots: https://houseofmeroe.com/robots.txt
Preferred canonical: https://houseofmeroe.com/ (`www` redirects to apex)

## 1. Google Search Console

1. Open https://search.google.com/search-console
2. Add a new property.
3. Recommended: choose **Domain** property for `houseofmeroe.com` if Vercel gives you the DNS TXT verification flow.
   - Because the domain is on Vercel DNS, add the TXT verification record inside Vercel → Domains → `houseofmeroe.com` → DNS Records.
4. Faster fallback: choose **URL prefix** property for `https://houseofmeroe.com/`.
   - If Google offers HTML file verification, download the file, place it in the site root, commit, push, wait for deploy, then click Verify.
5. After verified, go to **Sitemaps** and submit: `https://houseofmeroe.com/sitemap.xml`.
6. Use **URL Inspection** for:
   - `https://houseofmeroe.com/`
   - `https://houseofmeroe.com/radi`
   - `https://houseofmeroe.com/yourpop`
7. Click **Request indexing** for each important URL.

## 2. Already implemented on the site

- `robots.txt` allows crawling and points to the sitemap.
- `sitemap.xml` includes homepage, Radi, and YourPOP pages.
- Canonical URLs point to the apex domain.
- `www.houseofmeroe.com` redirects to `https://houseofmeroe.com/`.
- Open Graph and Twitter card metadata are present.
- Favicons, app icons, and web manifest are present.
- JSON-LD structured data is present on the main pages.

## 3. Optional Google Business Profile

Use Google Business Profile only if House of Meroë should have a public business listing with a real public location or service area.

Suggested setup:
- Business name: House of Meroë
- Category: Talent agency / Marketing agency / Media company (choose the closest available)
- Website: https://houseofmeroe.com
- Service area: remote/global or the actual target markets
- Add brand logo and short description

Avoid using a home address publicly unless intended.

## 4. Post-launch validation tools

- Google Rich Results Test: https://search.google.com/test/rich-results
- Google PageSpeed Insights: https://pagespeed.web.dev/
- Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
- LinkedIn Post Inspector: https://www.linkedin.com/post-inspector/
- X/Twitter Card Validator docs: https://developer.x.com/en/docs/x-for-websites/cards/overview/summary-card-with-large-image

## 5. Notes

Search indexing can take days to weeks. Submitting the sitemap and requesting indexing speeds discovery but does not guarantee immediate ranking.
