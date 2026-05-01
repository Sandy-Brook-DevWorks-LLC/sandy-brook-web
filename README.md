# Sandy Brook DevWorks LLC | Landing Site

Landing site for **Sandy Brook DevWorks LLC** — the tech neighbor for small and medium businesses in Round Rock, Texas. Custom automation, AI-powered tools, and .NET solutions that bring enterprise-quality software down to a small-business budget.

## 🚀 Overview

This repository contains the source code for the Sandy Brook DevWorks landing page. The site is positioned around a warm, approachable "tech neighbor" persona — someone who brings 15+ years of enterprise software experience to businesses that don't have (or need) an in-house engineering department.

## 🛠️ Tech Stack

- **HTML5** — Semantic structure.
- **Tailwind CSS 4** — Modern, utility-first styling with a custom Teal/Slate palette.
- **Inter Font** — Clean, professional typography.
- **JavaScript (ES6+)** — AJAX-based contact form submission and dark mode toggle.
- **Formspree** — Backend integration for the contact form.

## ✨ Key Features

- **Neighborly Positioning**: Focused on automation, AI, and .NET solutions for small and medium businesses — not executive consulting.
- **Responsive Design**: Fully mobile-friendly layout.
- **Dark Mode Support**: System-preference-aware theme toggling.
- **Projects Lab Section**: Showcases internal projects — **KnowItOwl!**, **Aquorbis**, and **Relay** — that link out to the sibling lab site at [sandybrook.io](https://sandybrook.io).
- **Integrated Contact Flow**:
  - Custom AJAX form submission with loading states and error handling.
  - Dedicated "Thank You" confirmation page.
- **Direct Scheduling**: Integration with Google Calendar for free 30-minute discovery calls.

## 📂 Project Structure

- `index.html` — The main landing page.
- `contact.html` — Contact form and FAQ section.
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
