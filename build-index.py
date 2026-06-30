#!/usr/bin/env python3
"""Scan the vault for markdown files and write files.json (the site manifest).

GitHub Pages has no directory listing, so the site needs a manifest of which
folders and .md files exist. Re-run this whenever you add, rename, or remove
notes:  python3 build-index.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Folders we never want to publish / index.
IGNORE_DIRS = {".git", ".obsidian", ".github", "node_modules"}
# Files we never want to list (meta / config, not site content).
IGNORE_FILES = {"README.md", "CLAUDE.md"}
# This note is rendered as the landing/welcome page, not listed as a note.
LANDING_FILE = "landing page.md"
# If present, this note defines the whole sidebar: each "# heading" is a
# category and the [[wikilinks]] under it are that category's pages, in order.
INDEX_FILE = "page index.md"
# Sidebar category order (by lowercase name); anything else follows, sorted.
# Only used for the folder-based fallback when there's no INDEX_FILE.
CATEGORY_ORDER = ["practical tools", "learnings", "books"]

# Obsidian inline tag: "#" + tag, where the tag starts with a letter and may
# contain word chars, "-", "_" and "/" (nested tags). Must not follow a word
# char (so "foo#bar" / URL fragments aren't matched) and the char after "#"
# must not be a space (that would be a Markdown heading, not a tag).
TAG_RE = re.compile(r"(?:^|(?<=\s))#([A-Za-z][\w/-]*)")
# Lines inside fenced code blocks shouldn't be scanned for tags.
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def title_from(name: str) -> str:
    """Turn a file/folder name into a display title."""
    stem = name[:-3] if name.endswith(".md") else name
    return stem.replace("-", " ").replace("_", " ").strip()


def extract_tags(path: str) -> list:
    """Collect Obsidian-style tags from a note, in first-seen order.

    Handles inline #tags and a YAML frontmatter `tags:` list/CSV.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError):
        return []

    tags = []

    def add(t):
        t = t.strip().lstrip("#")
        if t and t not in tags:
            tags.append(t)

    lines = text.splitlines()
    # YAML frontmatter (--- ... ---) at the very top.
    body_start = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                body_start = i + 1
                fm = "\n".join(lines[1:i])
                m = re.search(r"^tags:\s*(.*)$", fm, re.MULTILINE)
                if m:
                    inline = m.group(1).strip()
                    if inline and not inline.startswith("#"):
                        # tags: a, b  OR  tags: [a, b]
                        for t in re.split(r"[,\[\]]", inline):
                            add(t)
                    # YAML list form: "- tag" on following lines
                    for ln in fm.splitlines():
                        lm = re.match(r"\s*-\s*(.+)$", ln)
                        if lm:
                            add(lm.group(1))
                break

    in_fence = False
    for ln in lines[body_start:]:
        if FENCE_RE.match(ln):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in TAG_RE.finditer(ln):
            add(m.group(1))

    return tags


def folder_note_order(path: str):
    """If `path` is a folder note (its non-empty lines are all wikilinks),
    return the ordered list of linked note names (lowercased). Else None.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except (OSError, UnicodeDecodeError):
        return None

    targets, has_prose = [], False
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("%%"):
            continue
        links = re.findall(r"\[\[([^\]|#]+)", s)
        for l in links:
            targets.append(l.strip().lower())
        # Whatever remains after removing links and list markers — if there's
        # real text, this isn't a pure index/folder note.
        rest = re.sub(r"\[\[[^\]]*\]\]", "", s)
        rest = re.sub(r"^[-*+]|\d+[.)]", "", rest).strip()
        if rest:
            has_prose = True
    return targets if targets and not has_prose else None


def order_files(files: list, order: list) -> None:
    """Sort `files` by the order list (matched on lowercased name); names not
    listed keep to the end, alphabetically."""
    def key(f):
        name = f["name"].lower()
        return (order.index(name) if name in order else len(order), name)
    files.sort(key=key)


def strip_comments(text: str) -> str:
    """Remove Obsidian %%comments%% — paired, and an unclosed %% to the end."""
    text = re.sub(r"%%[\s\S]*?%%", "", text)
    return re.sub(r"%%[\s\S]*$", "", text)


def find_note_index():
    """Build a map of every publishable note: lowercased name -> info dict.

    Excludes meta files, the landing page, and the index note itself. Notes in
    the wip/ folder aren't copied to the site, so they won't appear here.
    """
    notes = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".md") or fn in IGNORE_FILES:
                continue
            if fn in (LANDING_FILE, INDEX_FILE):
                continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, ROOT).replace(os.sep, "/")
            notes[title_from(fn).lower()] = {
                "name": title_from(fn),
                "path": rel,
                "tags": extract_tags(fpath),
            }
    return notes


def folders_from_index(index_path: str, notes: dict):
    """Parse the page-index note into ordered categories.

    "# heading" lines start a category; [[wikilinks]] beneath become its pages
    (resolved against `notes`, unresolved links skipped). Returns None if the
    file can't be read.
    """
    try:
        with open(index_path, encoding="utf-8") as fh:
            text = strip_comments(fh.read())
    except (OSError, UnicodeDecodeError):
        return None

    folders, current = [], None
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        h = re.match(r"#{1,6}\s+(.+)$", s)
        if h:
            current = {"name": h.group(1).strip(), "files": []}
            folders.append(current)
            continue
        for target in re.findall(r"\[\[([^\]|#]+)", s):
            note = notes.get(target.strip().lower())
            if note and current is not None and note not in current["files"]:
                current["files"].append(note)
    return [f for f in folders if f["files"]]


def find_special(name: str):
    """Return the site-relative path of a special note (landing/index), or None."""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
        if name in filenames:
            return os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, "/")
    return None


def main() -> None:
    landing = find_special(LANDING_FILE)

    # Preferred: build the sidebar from the page-index note, if present.
    index_path = find_special(INDEX_FILE)
    if index_path:
        folders = folders_from_index(os.path.join(ROOT, index_path), find_note_index())
        write_manifest(folders, landing)
        return

    # Fallback: derive categories from the folder structure.
    folders = []
    for entry in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, entry)
        if not os.path.isdir(full) or entry in IGNORE_DIRS or entry.startswith("."):
            continue

        files = []
        order = None
        for dirpath, dirnames, filenames in os.walk(full):
            dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")]
            for fn in sorted(filenames):
                if not fn.endswith(".md") or fn in IGNORE_FILES:
                    continue
                fpath = os.path.join(dirpath, fn)
                rel = os.path.relpath(fpath, ROOT)
                if fn == LANDING_FILE:
                    landing = rel.replace(os.sep, "/")
                    continue
                # A folder note (an all-wikilinks index) at the category root
                # defines note order and is itself hidden from the list.
                if order is None and dirpath == full:
                    fn_order = folder_note_order(fpath)
                    if fn_order is not None:
                        order = fn_order
                        continue
                files.append({
                    "name": title_from(fn),
                    "path": rel.replace(os.sep, "/"),
                    "tags": extract_tags(fpath),
                })

        if files:
            if order:
                order_files(files, order)
            else:
                files.sort(key=lambda f: f["name"].lower())
            folders.append({"name": title_from(entry), "files": files})

    # Also pick up any top-level markdown files (outside a subfolder).
    loose = []
    for fn in sorted(os.listdir(ROOT)):
        if fn.endswith(".md") and fn not in IGNORE_FILES and os.path.isfile(os.path.join(ROOT, fn)):
            if fn == LANDING_FILE:
                landing = fn
                continue
            loose.append({
                "name": title_from(fn),
                "path": fn,
                "tags": extract_tags(os.path.join(ROOT, fn)),
            })
    if loose:
        folders.insert(0, {"name": "Notes", "files": loose})

    # Order categories: those in CATEGORY_ORDER first (in that order), rest A–Z.
    def cat_key(folder):
        name = folder["name"].lower()
        rank = CATEGORY_ORDER.index(name) if name in CATEGORY_ORDER else len(CATEGORY_ORDER)
        return (rank, name)

    folders.sort(key=cat_key)

    write_manifest(folders, landing)


def write_manifest(folders, landing) -> None:
    manifest = {"title": "lauras learnings", "folders": folders}
    if landing:
        manifest["landing"] = landing
    with open(os.path.join(ROOT, "files.json"), "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    total = sum(len(fo["files"]) for fo in folders)
    print(f"Wrote files.json — {len(folders)} folder(s), {total} file(s).")


if __name__ == "__main__":
    main()
