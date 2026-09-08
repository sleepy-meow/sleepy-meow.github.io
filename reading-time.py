#!/usr/bin/env python3
"""Estimate reading time for the notes the site actually shows.

Reads files.json — the same manifest the sidebar is built from — so the set
of pages and their order match what a reader sees. Pages marked "?" in the
page index ("draft": true, the very-WIP ones hidden behind the sidebar
switch) are left out unless you ask for them.

    ./reading-time.py                 visible pages, grouped by section
    ./reading-time.py --all           include the very-WIP pages too
    ./reading-time.py --wpm 200       a slower reader (default 220)
    ./reading-time.py --flat          one list, longest first
    ./reading-time.py --json          machine-readable

Word counts are taken from the prose only: frontmatter, %%comments%%, URLs
and markdown syntax are stripped, and wikilinks count as the text a reader
sees. Bare ``` fences hold quoted prose in these notes, so their contents
count; a fence tagged with a language is treated as code and skipped. Each
embedded image adds a few seconds of looking time.
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SECONDS_PER_IMAGE = 8

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
COMMENT = re.compile(r"%%[\s\S]*?%%|%%[\s\S]*\Z")
# These notes use bare ``` fences to hold quoted prose, not code, so the
# contents count as reading; only the delimiter lines are dropped. A fence
# that names a language is treated as real code and skipped entirely.
CODE_FENCE = re.compile(r"^```[^\n`]+\n.*?^```[ \t]*$", re.M | re.S)
FENCE_MARK = re.compile(r"^```[ \t]*$", re.M)
IMAGE = re.compile(r"!\[\[[^\]]+\]\]|!\[[^\]]*\]\([^)]*\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")
MDLINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
HTML = re.compile(r"<[^>]+>")
CALLOUT = re.compile(r"^>\s*\[![^\]]+\][+-]?", re.M)
MARKS = re.compile(r"[*_`~=]+|^>+\s?|^#{1,6}\s+|^\s*[-+*]\s+|^\s*\d+[.)]\s+", re.M)
WORD = re.compile(r"[^\s]+")


def measure(path):
    """Return (words, images) of readable content, or None if unreadable."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None

    text = FRONTMATTER.sub("", text)
    text = COMMENT.sub("", text)
    text = CODE_FENCE.sub(" ", text)
    text = FENCE_MARK.sub(" ", text)
    images = len(IMAGE.findall(text))
    text = IMAGE.sub(" ", text)
    # A wikilink reads as its alias when it has one, else its target.
    text = WIKILINK.sub(lambda m: m.group(2) or m.group(1), text)
    text = MDLINK.sub(lambda m: m.group(1), text)
    text = HTML.sub(" ", text)
    text = CALLOUT.sub(" ", text)
    text = MARKS.sub(" ", text)
    return len(WORD.findall(text)), images


def seconds(words, images, wpm):
    return words / wpm * 60 + images * SECONDS_PER_IMAGE


def short(sec):
    """Per-page: whole minutes, never rounded down to nothing."""
    return "%d min" % max(1, round(sec / 60))


def long(sec):
    total = int(round(sec / 60))
    return "%dh %02dm" % (total // 60, total % 60) if total >= 60 else "%d min" % total


def collect(manifest, include_drafts):
    pages, missing = [], []
    for folder in manifest.get("folders", []):
        for entry in folder.get("files", []):
            if entry.get("draft") and not include_drafts:
                continue
            path = os.path.join(ROOT, entry["path"])
            got = measure(path)
            if got is None:
                missing.append(entry["path"])
                continue
            words, images = got
            pages.append({
                "section": folder["name"],
                "name": entry["name"],
                "path": entry["path"],
                "draft": bool(entry.get("draft")),
                "words": words,
                "images": images,
            })
    return pages, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--all", action="store_true",
                    help='include the very-WIP ("?") pages')
    ap.add_argument("--wpm", type=int, default=220, help="reading speed (default 220)")
    ap.add_argument("--flat", action="store_true", help="one list, longest page first")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    with open(os.path.join(ROOT, "files.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)

    pages, missing = collect(manifest, args.all)
    for p in pages:
        p["seconds"] = round(seconds(p["words"], p["images"], args.wpm), 1)

    words = sum(p["words"] for p in pages)
    images = sum(p["images"] for p in pages)
    total = sum(p["seconds"] for p in pages)

    if args.as_json:
        json.dump({"wpm": args.wpm, "pages": pages, "missing": missing,
                   "totals": {"pages": len(pages), "words": words,
                              "images": images, "seconds": round(total, 1)}},
                  sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    width = max([len(p["name"]) for p in pages] or [10])
    rows = sorted(pages, key=lambda p: -p["seconds"]) if args.flat else pages
    section = None
    for p in rows:
        if not args.flat and p["section"] != section:
            section = p["section"]
            print("\n  %s" % section.upper())
        mark = " ?" if p["draft"] else ""
        print("    %-*s  %7s  %6d words%s"
              % (width, p["name"], short(p["seconds"]), p["words"], mark))

    print("\n  " + "─" * (width + 26))
    print("    %-*s  %7s  %6d words" % (width, "%d pages" % len(pages), long(total), words))
    if images:
        print("    %-*s  %7s" % (width, "%d images" % images,
                                 long(images * SECONDS_PER_IMAGE)))
    print("\n  at %d wpm%s" % (args.wpm, "" if args.all else "; very-WIP pages excluded"))
    if missing:
        print("\n  listed in files.json but not on disk:")
        for m in missing:
            print("    %s" % m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
