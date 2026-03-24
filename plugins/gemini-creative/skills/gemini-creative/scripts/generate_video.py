#!/usr/bin/env python3
"""Generate videos using Veo 3.1 model."""

import argparse
import json
import sys
import time
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
    parser = argparse.ArgumentParser(description="Generate video with Veo 3.1")
    parser.add_argument("--prompt", required=True, help="Text prompt for video")
    parser.add_argument("--output", required=True, help="Output file path (.mp4)")
    parser.add_argument("--model", default="veo-3.1-generate-preview",
                        choices=["veo-3.1-generate-preview", "veo-3.1-fast"],
                        help="Model to use")
    parser.add_argument("--aspect-ratio", default="16:9",
                        choices=["16:9", "9:16"],
                        help="Aspect ratio")
    parser.add_argument("--resolution", default="1080p",
                        choices=["720p", "1080p", "4k"],
                        help="Video resolution")
    parser.add_argument("--duration", type=int, default=8,
                        choices=[4, 6, 8],
                        help="Video duration in seconds")
    parser.add_argument("--timeout", type=int, default=300,
                        help="Max wait time in seconds (default: 300)")
    args = parser.parse_args()

    api_key = load_api_key()

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("ERROR: google-genai package not installed.", file=sys.stderr)
        print("Run: pip install google-genai --break-system-packages", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating video with {args.model}...")
    print(f"  Prompt: {args.prompt[:100]}{'...' if len(args.prompt) > 100 else ''}")
    print(f"  Aspect ratio: {args.aspect_ratio}")
    print(f"  Resolution: {args.resolution}")
    print(f"  Duration: {args.duration}s")
    print(f"  Timeout: {args.timeout}s")
    print()

    try:
        operation = client.models.generate_videos(
            model=args.model,
            prompt=args.prompt,
            config=types.GenerateVideosConfig(
                aspect_ratio=args.aspect_ratio,
                resolution=args.resolution,
                duration_seconds=str(args.duration),
            ),
        )
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Poll until complete
    start_time = time.time()
    poll_count = 0
    while not operation.done:
        elapsed = time.time() - start_time
        if elapsed > args.timeout:
            print(f"ERROR: Timed out after {args.timeout}s. Video generation can take several minutes.", file=sys.stderr)
            print("Try increasing --timeout or using veo-3.1-fast for quicker results.", file=sys.stderr)
            sys.exit(1)

        poll_count += 1
        wait_time = min(10, 5 + poll_count)  # Start at 5s, ramp to 10s
        print(f"  Waiting... ({int(elapsed)}s elapsed)")
        time.sleep(wait_time)

        try:
            operation = client.operations.get(operation)
        except Exception as e:
            print(f"WARNING: Poll failed ({e}), retrying...", file=sys.stderr)
            continue

    elapsed = time.time() - start_time
    print(f"\nGeneration complete in {int(elapsed)}s")

    # Save the video
    try:
        generated_video = operation.response.generated_videos[0]
        client.files.download(file=generated_video.video)
        generated_video.video.save(str(output_path))
        print(f"Video saved to: {output_path}")
    except Exception as e:
        print(f"ERROR: Failed to save video: {e}", file=sys.stderr)
        sys.exit(1)

    print("Done!")


if __name__ == "__main__":
    main()
