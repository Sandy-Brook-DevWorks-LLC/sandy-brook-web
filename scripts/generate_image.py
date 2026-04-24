#!/usr/bin/env python3
"""Generate or edit images via Gemini 2.5 Flash Image (Nano Banana).

Reads GEMINI_API_KEY from the environment. Writes outputs to
_source-images/ by default so they sit alongside other originals and can
later be passed through the image-optimization pipeline.

Examples:
    # Text-to-image
    python scripts/generate_image.py \\
        --prompt "Minimalist teal & slate icon of a bridge, flat vector" \\
        --out bridge_icon.png

    # Image editing (one or more inputs + prompt)
    python scripts/generate_image.py \\
        --prompt "Same logo but on a transparent background" \\
        --input _source-images/aquorbis_logo.png \\
        --out aquorbis_logo_transparent.png

    # Multi-image composition
    python scripts/generate_image.py \\
        --prompt "Combine these two logos side-by-side on a white card" \\
        --input _source-images/aquorbis_logo.png \\
        --input _source-images/relay_logo.png \\
        --out combined.png
"""
from __future__ import annotations

import argparse
import mimetypes
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT_DIR = REPO_ROOT / "_source-images"
DEFAULT_MODEL = "gemini-2.5-flash-image"


def load_input_parts(paths: list[Path]):
    from google.genai import types

    parts = []
    for p in paths:
        if not p.exists():
            sys.exit(f"error: input image not found: {p}")
        mime, _ = mimetypes.guess_type(p.name)
        if mime is None:
            mime = "image/png"
        parts.append(types.Part.from_bytes(data=p.read_bytes(), mime_type=mime))
    return parts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prompt", "-p", required=True, help="Text prompt describing the image to generate or the edit to apply.")
    ap.add_argument("--out", "-o", required=True, help="Output filename (relative to --out-dir unless absolute).")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help=f"Output directory (default: {DEFAULT_OUT_DIR}).")
    ap.add_argument("--input", "-i", action="append", default=[], type=Path, help="Input image to edit/compose (repeatable).")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini image model (default: {DEFAULT_MODEL}).")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite output file if it already exists.")
    args = ap.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("error: GEMINI_API_KEY is not set in the environment.")

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = Path(args.out_dir) / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.overwrite:
        sys.exit(f"error: {out_path} already exists (use --overwrite to replace).")

    try:
        from google import genai
    except ImportError:
        sys.exit("error: google-genai not installed. Run: pip install -r scripts/requirements.txt")

    client = genai.Client()
    contents: list = [args.prompt]
    if args.input:
        contents.extend(load_input_parts(args.input))

    print(f"> model: {args.model}")
    print(f"> prompt: {args.prompt}")
    if args.input:
        print(f"> inputs: {', '.join(str(p) for p in args.input)}")

    response = client.models.generate_content(model=args.model, contents=contents)

    saved = False
    for part in response.parts or []:
        if getattr(part, "text", None):
            print(f"[model text] {part.text}")
        elif getattr(part, "inline_data", None) is not None:
            part.as_image().save(out_path)
            print(f"> saved: {out_path}")
            saved = True

    if not saved:
        sys.exit("error: model returned no image data. Try a different prompt or check quota.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
