#!/usr/bin/env python3
"""Generate batch images using Imagen 4 model."""

import argparse
import json
import sys
from pathlib import Path


def load_api_key():
    config_path = Path.home() / ".gemini-creative-config.json"
    if not config_path.exists():
        print(f"ERROR: Config file not found at {config_path}", file=sys.stderr)
        print("Run the skill setup to save your Gemini API key first.", file=sys.stderr)
        sys.exit(1)
    with open(config_path) as f:
        config = json.load(f)
    key = config.get("api_key", "").strip()
    if not key:
        print("ERROR: api_key is empty in config file.", file=sys.stderr)
        sys.exit(1)
    return key


def main():
    parser = argparse.ArgumentParser(description="Generate batch images with Imagen 4")
    parser.add_argument("--prompt", required=True, help="Text prompt for generation")
    parser.add_argument("--output-dir", required=True, help="Output directory for images")
    parser.add_argument("--count", type=int, default=4, choices=[1, 2, 3, 4],
                        help="Number of images to generate (1-4)")
    parser.add_argument("--aspect-ratio", default="1:1",
                        help="Aspect ratio (1:1, 3:4, 4:3, 9:16, 16:9)")
    parser.add_argument("--size", default="1K", choices=["1K", "2K"],
                        help="Image size")
    args = parser.parse_args()

    api_key = load_api_key()

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("ERROR: google-genai package not installed.", file=sys.stderr)
        print("Run: pip install google-genai Pillow --break-system-packages", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating {args.count} image(s) with Imagen 4...")
    print(f"  Prompt: {args.prompt[:100]}{'...' if len(args.prompt) > 100 else ''}")
    print(f"  Aspect ratio: {args.aspect_ratio}")
    print(f"  Size: {args.size}")

    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=args.prompt,
            config=types.GenerateImagesConfig(
                number_of_images=args.count,
            ),
        )
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    if not response.generated_images:
        print("ERROR: No images were generated.", file=sys.stderr)
        print("The prompt may have triggered safety filters. Try rewording.", file=sys.stderr)
        sys.exit(1)

    # Create a base filename from the prompt
    slug = args.prompt[:50].lower().strip()
    slug = "".join(c if c.isalnum() or c == " " else "" for c in slug)
    slug = slug.strip().replace(" ", "-")
    if not slug:
        slug = "generated"

    saved_files = []
    for i, generated_image in enumerate(response.generated_images):
        if args.count == 1:
            filename = f"{slug}.png"
        else:
            filename = f"{slug}-{i + 1}.png"
        filepath = output_dir / filename
        generated_image.image.save(str(filepath))
        saved_files.append(str(filepath))
        print(f"  Saved: {filepath}")

    print(f"\nDone! Generated {len(saved_files)} image(s) in {output_dir}")


if __name__ == "__main__":
    main()
