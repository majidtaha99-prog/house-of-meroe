# House of Meroë static site

Vercel-hosted creator roster site and sponsor-facing media kit assets.

## Live routes

- Home: `https://house-of-meroe.vercel.app/`
- Radi profile: `https://house-of-meroe.vercel.app/radi`
- Radi media kit: `https://house-of-meroe.vercel.app/radimediakit.pdf`
- Ahmed / YourPOP profile: `https://house-of-meroe.vercel.app/yourpop`
- Ahmed / YourPOP media kit: `https://house-of-meroe.vercel.app/yourpopmediakit.pdf`

## Structure

- `index.html` — House of Meroë roster landing page.
- `radi.html` and `radi/index.html` — Radi profile route variants.
- `yourpop/index.html` — Ahmed / YourPOP profile.
- `radimediakit.pdf` — Radi sponsor media kit.
- `yourpopmediakit.pdf` — Ahmed / YourPOP sponsor media kit.
- `media-kit-previews/` — exported preview PNGs for quick QA/reference.

## Deploy

Pushes to `main` deploy through the connected Vercel project. Manual production deploy can also be run with:

```bash
vercel --prod
```
