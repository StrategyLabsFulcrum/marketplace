#!/usr/bin/env python3
"""Generate or edit images using Gemini Flash Image models."""

import argparse
import json
import sys
import os
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
    parser = argparse.ArgumentParser(description="Generate images with Gemini")
    parser.add_argument("--prompt", required=True, help="Text prompt for generation")
    parser.add_argument("--output", required=True, help="Output file path (.png)")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview",
                        choices=["gemini-3.1-flash-image-preview",
                                 "gemini-3-pro-image-preview",
                                 "gemini-2.5-flash-image"],
                        help="Model to use")
    parser.add_argument("--aspect-ratio", default="1:1",
                        help="Aspect ratio (e.g., 1:1, 16:9, 9:16, 4:3, 3:4, 4:5, 5:4)")
    parser.add_argument("--resolution", default="1K",
                        choices=["512", "1K", "2K", "4K"],
                        help="Output resolution")
    parser.add_argument("--input-image", default=None,
                        help="Path to input image for editing mode")
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

    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio=args.aspect_ratio,
            image_size=args.resolution,
        ),
    )

    # Build the content — text only or text + image for editing
    if args.input_image:
        from PIL import Image
        input_img = Image.open(args.input_image)
        contents = [args.prompt, input_img]
    else:
        contents = args.prompt

    print(f"Generating image with {args.model}...")
    print(f"  Prompt: {args.prompt[:100]}{'...' if len(args.prompt) > 100 else ''}")
    print(f"  Aspect ratio: {args.aspect_ratio}")
    print(f"  Resolution: {args.resolution}")

    try:
        response = client.models.generate_content(
            model=args.model,
            contents=contents,
            config=config,
        )
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract and save the image
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    saved = False
    text_response = []
    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(str(output_path))
            print(f"Image saved to: {output_path}")
            saved = True
        elif part.text:
            text_response.append(part.text)

    if text_response:
        print(f"Model response: {' '.join(text_response)}")

    if not saved:
        print("ERROR: No image was generated. The model may have returned only text.", file=sys.stderr)
        print("Try a different prompt or check if the prompt triggered safety filters.", file=sys.stderr)
        sys.exit(1)

    print("Done!")


if __name__ == "__main__":
    main()
