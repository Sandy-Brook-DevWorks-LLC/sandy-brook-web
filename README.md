# Sandy Brook DevWorks LLC | Landing Site

Landing site for **Sandy Brook DevWorks LLC**, an independent software company in Round Rock, Texas that builds and maintains its own consumer applications.

## 🚀 Overview

This repository contains the company website at **sandybrookdevworks.com**. It introduces the company and its apps, and provides a contact channel for app support and feedback. Product details and download links live at [Sandy Brook Labs](https://sandybrook.io), with Relay at [relayconnect.net](https://relayconnect.net). The company does not offer consulting or custom development services.

The site is hosted on GitHub Pages and deploys when changes are pushed to the configured publishing branch.

## 🛠️ Tech Stack

- **HTML5** — Semantic structure.
- **Tailwind CSS 4** — Modern, utility-first styling with a custom Teal/Slate palette.
- **Inter Font** — Clean, professional typography.
- **JavaScript (ES6+)** — AJAX-based contact form submission and dark mode toggle.
- **Formspree** — Backend integration for the contact form.

## ✨ Key Features

- **Consumer App Focus**: Introduces the independent company behind our apps.
- **Responsive Design**: Fully mobile-friendly layout.
- **Dark Mode Support**: System-preference-aware theme toggling.
- **App Discovery**: Features **KnowItOwl!** and **Aquorbis**, with a secondary link to **Relay**. Links to the product sites for details.
- **Integrated Contact Flow**:
  - Custom AJAX form submission with loading states and error handling.
  - Dedicated "Thank You" confirmation page.

## 📂 Project Structure

- `index.html` — The main landing page.
- `contact.html` — App support and feedback form with FAQs.
- `thank-you.html` — Form submission confirmation page.
- `privacy.html`, `terms.html` — Legal pages.
- `css/` — Shared site styles (`site.css`) and policy-page styles (`policy.css`).
- `js/` — Theme toggle (`theme.js`) and contact-form handler (`contact.js`).
- `images/` — All site images (logos, section illustrations, favicons).
- `_source-images/` — Original high-res source files (gitignored).
- `scripts/generate_image.py` — CLI helper for generating/editing assets via the Gemini image API.

## 🧑‍💻 Local Development

No build step — open `index.html` directly, or serve the folder for realistic asset paths:

```bash
python3 -m http.server 8000 --directory .
# then visit http://localhost:8000
```

### Asset generation (Gemini "Nano Banana")

One-time setup:

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
export GEMINI_API_KEY=...  # or set in ~/.bashrc
```

Generate or edit an image:

```bash
.venv/bin/python scripts/generate_image.py \
  -p "Minimalist teal icon, flat vector" \
  -o bridge_icon.png
```

Outputs land in `_source-images/` (gitignored). Convert to WebP at the repo root using the Pillow recipe in `CLAUDE.md`.

---
© 2026 Sandy Brook DevWorks LLC. All rights reserved.
