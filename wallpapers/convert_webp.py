#!/usr/bin/env python3
"""
Convert every .webp in a folder to .png (keeps the originals).
Usage:
    pip install pillow
    python convert_webp.py "C:\\Users\\Merks\\Pictures\\wallpapers"
If no path is given, defaults to the wallpapers folder below.
"""

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Run:  pip install pillow")
    sys.exit(1)

DEFAULT_FOLDER = r"C:\Users\Merks\Pictures\wallpapers"


def main():
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FOLDER)
    if not folder.is_dir():
        print(f"Not a folder: {folder}")
        sys.exit(1)

    webp_files = sorted(folder.glob("*.webp")) + sorted(folder.glob("*.WEBP"))
    if not webp_files:
        print(f"No .webp files found in {folder}")
        return

    converted, failed = 0, []
    for src in webp_files:
        dst = src.with_suffix(".png")
        if dst.exists():
            print(f"skip (already exists): {dst.name}")
            continue
        try:
            with Image.open(src) as img:
                img.convert("RGB").save(dst, "PNG")
            print(f"converted: {src.name} -> {dst.name}")
            converted += 1
        except Exception as e:
            print(f"FAILED: {src.name} ({e})")
            failed.append(src.name)

    print(f"\nDone. {converted} converted, {len(failed)} failed.")
    if failed:
        print("Failed files:", ", ".join(failed))


if __name__ == "__main__":
    main()
