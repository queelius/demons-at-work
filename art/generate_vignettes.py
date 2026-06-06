#!/usr/bin/env python3
"""Generate sumi-e chapter vignettes via DALL-E 3, then process to transparent PNGs."""

import os
import sys
import json
import time
from pathlib import Path
from openai import OpenAI
from PIL import Image
import base64

ART_DIR = Path(__file__).parent
VIGNETTE_DIR = ART_DIR / "vignettes"
VIGNETTE_DIR.mkdir(exist_ok=True)

STYLE_PREFIX = (
    "Minimalist ink wash sketch. Black sumi ink on pure white background. "
    "EXTREMELY sparse and small: the subject is rendered in 3 to 5 brushstrokes maximum, "
    "occupying no more than 15% of the total image area. "
    "Vast empty white space surrounds a tiny centered subject. "
    "Think: the smallest possible gesture that suggests the object. "
    "No text, no characters, no kanji, no seal stamp, no signature, no chop mark. "
    "No shading, no gradients, no wash effects. Just a few black ink lines on white. "
    "No background elements whatsoever. Pure flat white (#FFFFFF) everywhere except the ink strokes. "
    "The aesthetic is closer to a quick notebook sketch than a finished painting."
)

CHAPTERS = [
    ("01-on-paper", "A thin manila file folder, slightly open, a few pages visible inside"),
    ("02-hat", "A plain fedora or trilby hat, resting brim-down as if just set on a surface"),
    ("03-the-canvas", "Two armchairs side by side, one turned slightly away from the other"),
    ("04-fourteen-minutes", "A single wooden floor joist, rough-hewn, with visible grain"),
    ("05-good-acoustics", "A clipboard with a single sheet of paper clipped to it"),
    ("06-six-minutes-early", "A single cracked floorboard, seen from above"),
    ("07-the-garden", "A small garden trellis, leaning and partially collapsed"),
    ("08-cancellation", "A telephone handset, set down off its cradle"),
    ("09-trust-the-process", "A coffee mug turned upside down on a towel"),
    ("10-revised-protocols", "A simple flowchart: one box with two arrows pointing in opposite directions"),
    ("11-wednesday-night", "An attic pull-down ladder, half descended from a ceiling"),
    ("12-middlemarch", "A thick paperback book lying flat, spine cracked, a bookmark visible"),
    ("13-the-report", "A small potted plant, wilted and dead, in a simple clay pot"),
    ("14-eleven-minutes", "A round wall thermostat showing a simple dial"),
    ("15-two-cups", "Two simple tea cups side by side on a surface"),
    ("16-mid-cycle", "A framed motivational poster, hanging slightly crooked on a wall"),
    ("17-the-doorway", "An empty doorway with light falling through it from behind, casting a rectangle of light"),
    ("18-please-address", "A single small Post-it note, slightly curled at one corner"),
    ("19-direct-interface", "The same empty doorway but in darkness, only the faintest outline visible"),
    ("20-meri", "A single sheet of paper with one item circled in ink"),
    ("21-the-field", "A single small checkbox with a checkmark in it"),
    ("22-completion", "A small garden trellis standing upright, tied with a piece of string"),
    ("23-the-next-file", "A coffee mug right side up on a table, as if just set down, still warm"),
]

BG_COLOR = (255, 255, 255)
THRESHOLD = 240


def make_transparent(img_path: Path, out_path: Path):
    """Convert white/near-white pixels to transparent."""
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        if r >= THRESHOLD and g >= THRESHOLD and b >= THRESHOLD:
            new_data.append((r, g, b, 0))
        else:
            new_data.append((r, g, b, a))
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print(f"  Transparent: {out_path.name}")


def generate_vignette(client: OpenAI, chapter_id: str, subject: str):
    """Generate a single vignette via DALL-E 3."""
    raw_path = VIGNETTE_DIR / f"{chapter_id}_raw.png"
    final_path = VIGNETTE_DIR / f"{chapter_id}.png"

    if final_path.exists():
        print(f"  Skip (exists): {final_path.name}")
        return

    prompt = f"{STYLE_PREFIX}\n\nSubject: {subject}"

    print(f"  Generating: {chapter_id} ...")
    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024",
            quality="high",
            n=1,
        )
        img_data = base64.b64decode(response.data[0].b64_json)
        with open(raw_path, "wb") as f:
            f.write(img_data)
        print(f"  Downloaded: {raw_path.name}")

        make_transparent(raw_path, final_path)

    except Exception as e:
        print(f"  ERROR: {chapter_id}: {e}")


def main():
    client = OpenAI()

    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end_idx = int(sys.argv[2]) if len(sys.argv) > 2 else len(CHAPTERS)

    chapters = CHAPTERS[start_idx:end_idx]
    print(f"Generating {len(chapters)} vignettes (idx {start_idx}-{end_idx-1})...")

    for i, (chapter_id, subject) in enumerate(chapters):
        print(f"\n[{start_idx + i + 1}/{len(CHAPTERS)}] {chapter_id}")
        generate_vignette(client, chapter_id, subject)
        if i < len(chapters) - 1:
            time.sleep(1)

    print("\nDone.")


if __name__ == "__main__":
    main()
