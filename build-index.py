#!/usr/bin/env python3
"""Scan the vault for markdown files and write files.json (the site manifest).

GitHub Pages has no directory listing, so the site needs a manifest of which
folders and .md files exist. Re-run this whenever you add, rename, or remove
notes:  python3 build-index.py
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Folders we never want to publish / index.
IGNORE_DIRS = {".git", ".obsidian", ".github", "node_modules"}
# Files we never want to list.
IGNORE_FILES = {"README.md"}


def title_from(name: str) -> str:
    """Turn a file/folder name into a display title."""
    stem = name[:-3] if name.endswith(".md") else name
    return stem.replace("-", " ").replace("_", " ").strip()


def main() -> None:
    folders = []
    for entry in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, entry)
        if not os.path.isdir(full) or entry in IGNORE_DIRS or entry.startswith("."):
            continue

        files = []
        for dirpath, dirnames, filenames in os.walk(full):
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
            for fn in sorted(filenames):
                if not fn.endswith(".md") or fn in IGNORE_FILES:
                    continue
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                files.append({"name": title_from(fn), "path": rel.replace(os.sep, "/")})

        if files:
            files.sort(key=lambda f: f["name"].lower())
            folders.append({"name": title_from(entry), "files": files})

    # Also pick up any top-level markdown files (outside a subfolder).
    loose = []
    for fn in sorted(os.listdir(ROOT)):
        if fn.endswith(".md") and fn not in IGNORE_FILES and os.path.isfile(os.path.join(ROOT, fn)):
            loose.append({"name": title_from(fn), "path": fn})
    if loose:
        folders.insert(0, {"name": "Notes", "files": loose})

    manifest = {"title": "Sleepy Meow", "folders": folders}
    with open(os.path.join(ROOT, "files.json"), "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    total = sum(len(fo["files"]) for fo in folders)
    print(f"Wrote files.json — {len(folders)} folder(s), {total} file(s).")


if __name__ == "__main__":
    main()
