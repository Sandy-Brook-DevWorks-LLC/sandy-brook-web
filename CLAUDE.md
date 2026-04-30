# CLAUDE.md

Guidance for Claude Code when working in this repo. See `README.md` for the user-facing overview.

## What this is

Static landing site for **Sandy Brook DevWorks LLC** (`sandybrookdevworks.com`). Sibling repo `~/repos/sandy-brook-labs` hosts `sandybrook.io` (projects lab). This site is the company/LLC face; the lab site is the product/apps face. Cross-link, don't duplicate.

## Stack

- Plain HTML5 + Tailwind CSS 4 via the browser CDN (`<script src="https://unpkg.com/@tailwindcss/browser@4">`). **No build step, no bundler, no framework.**
- Inter font from Google Fonts.
- Formspree for the contact form; Google Calendar deep link for booking.
- GitHub Pages hosting (see `CNAME`).

## Editing conventions

- All pages share the same `<nav>` and `<footer>` markup. If you change one, change all five: `index.html`, `contact.html`, `thank-you.html`, `privacy.html`, `terms.html`.
- Theme toggle logic and Tailwind `@theme` block are duplicated per page. That's intentional — keep them in sync.
- Brand color accents: use `<span class="text-brand">` inside headings to apply the teal highlight (see hero H1 for the canonical pattern).
- Dark mode uses system preference + `localStorage.theme` override; `.dark` class on `<html>`.

## Image pipeline

Originals live in `_source-images/` (gitignored). The committed WebPs at the repo root are what the HTML references. To add or replace an image:

1. Generate or drop the source PNG/JPG into `_source-images/`. For AI-generated assets use `scripts/generate_image.py` (see `README.md`).
2. Convert to WebP at the repo root:
   ```python
   from PIL import Image
   with Image.open('_source-images/foo.png') as im:
       im = im.convert('RGB')
       # Cap longest side at 1600px for hero/section images
       # Logos: resize to 256x256 (retina-friendly for ≤128px display)
       im.save('foo.webp', 'WEBP', quality=85, method=6)
   ```
3. Keep favicons and `apple-touch-icon` as JPG for compat; everything else WebP.
4. The HTML already references the WebP filenames — no markup change needed if you reuse a name.

Full playbook in memory: `feedback_image_optimization.md`.

## Do not

- Add a build step (Vite, Webpack, etc.) without asking — the site's simplicity is intentional.
- Introduce `<picture>` fallbacks unless specifically asked; WebP support is >96% and the audience doesn't need legacy Safari/IE coverage.
- Commit anything from `_source-images/` or `.venv/` (both gitignored).
- Change the Google Calendar link, Formspree action, or the hidden `_subject` field without user confirmation — these are live integrations.

## Related memory

- `project_domains.md` — .com vs .io split and cross-linking guidance
- `project_positioning.md` — current positioning (neighborly tech partner, not Fractional CTO)
- `feedback_image_optimization.md` — Pillow-based optimization recipe
- `reference_asset_generation.md` — Gemini Nano Banana script usage
