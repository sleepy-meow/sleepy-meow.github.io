#!/usr/bin/env python3
"""Combine every note listed in the page index into a single markdown file.

Reads `page index.md` — the same note that defines the sidebar — and stitches
its pages together in index order, keeping the index's "# heading" lines as
section headings. Useful for printing, exporting, or handing the whole thing
to something that wants one file.

Each page is separated from the next by a horizontal rule, its own heading,
and an HTML comment naming the note it came from.

  python3 build-combined.py                 # -> combined.md
  python3 build-combined.py -o ~/notes.md   # somewhere else
  python3 build-combined.py --no-toc        # skip the table of contents

Nothing here touches files.json or the site — run build-index.py for that.
"""
import argparse
import os
import re
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))

# Folders we never scan (same set build-index.py ignores).
IGNORE_DIRS = {".git", ".obsidian", ".github", "node_modules"}
# Files that are never notes in their own right.
IGNORE_FILES = {"README.md", "CLAUDE.md"}
LANDING_FILE = "landing page.md"
INDEX_FILE = "page index.md"

TITLE = "lauras learnings"
DEFAULT_OUTPUT = "combined.md"
# Horizontal rule between pages, so one note visibly ends before the next
# begins. Needs a blank line on either side to stay a rule and not turn the
# line above it into a heading.
RULE = "---"

# Heading levels in the combined document. Index sections sit at SECTION_LEVEL,
# note titles one below, and a note's own headings are pushed down to start
# under its title (markdown stops at 6, so deeper ones get clamped).
SECTION_LEVEL = 2
NOTE_LEVEL = SECTION_LEVEL + 1
MAX_LEVEL = 6

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Index entry: [[note]] or [[note|alias]], optionally followed by a state
# marker ("?", "!!", "!!!"). The marker is index bookkeeping, not content.
ENTRY_RE = re.compile(r"\[\[([^\]|#]+)[^\]]*\]\][ \t]*(\?|!{2,})?")
# Obsidian embeds and links, as index.html's renderer understands them.
EMBED_RE = re.compile(r"!\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")
LINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")


def strip_comments(text: str) -> str:
    """Remove Obsidian %%comments%% — paired, and an unclosed %% to the end."""
    text = re.sub(r"%%[\s\S]*?%%", "", text)
    return re.sub(r"%%[\s\S]*$", "", text)


def strip_frontmatter(text: str) -> str:
    """Drop a leading YAML frontmatter block, if there is one."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1:])
    return text


def title_from(name: str) -> str:
    """Turn a file name into a display title."""
    stem = name[:-3] if name.endswith(".md") else name
    return stem.replace("-", " ").replace("_", " ").strip()


def slug(text: str) -> str:
    """GitHub-style anchor slug, so the table of contents and the converted
    wikilinks land on the right heading."""
    s = re.sub(r"[^\w\s-]", "", text.strip().lower())
    return re.sub(r"[\s_]+", "-", s)


def find_notes() -> dict:
    """Map every note in the vault: lowercased name -> path on disk.

    Same scan build-index.py does, so a note linked from the index is found
    wherever it lives, not just in learnings/.
    """
    notes = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in IGNORE_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".md") or fn in IGNORE_FILES:
                continue
            if fn in (LANDING_FILE, INDEX_FILE):
                continue
            notes[title_from(fn).lower()] = os.path.join(dirpath, fn)
    return notes


def find_assets() -> dict:
    """Map every image/attachment in the vault: lowercased file name -> path.

    Embeds name a file without a folder ("![[Pasted image ….png]]"), the way
    Obsidian does, so the folder has to be looked up.
    """
    assets = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in IGNORE_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".md"):
                assets.setdefault(fn.lower(), os.path.join(dirpath, fn))
    return assets


def find_special(name: str):
    """Absolute path of a special note (landing/index), or None."""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in IGNORE_DIRS and not d.startswith(".")]
        if name in filenames:
            return os.path.join(dirpath, name)
    return None


def parse_index(index_path: str, notes: dict):
    """Read the page index into [(section, [(title, path), …]), …].

    "# heading" lines open a section; the [[wikilinks]] under it are its pages,
    in order. Unresolved links and repeats are reported and skipped.
    """
    with open(index_path, encoding="utf-8") as fh:
        text = strip_comments(fh.read())

    sections, current, seen, missing, dupes = [], None, set(), [], []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        h = HEADING_RE.match(s)
        if h:
            current = (h.group(2).strip(), [])
            sections.append(current)
            continue
        for m in ENTRY_RE.finditer(s):
            name = m.group(1).strip()
            key = name.lower()
            path = notes.get(key)
            if path is None:
                missing.append(name)
                continue
            if current is None:
                continue
            if key in seen:
                dupes.append(name)
                continue
            seen.add(key)
            current[1].append((title_from(os.path.basename(path)), path))
    return [s for s in sections if s[1]], missing, dupes


def convert_embeds(text: str, assets: dict, out_dir: str) -> tuple:
    """Rewrite Obsidian image embeds as plain markdown images.

    "![[name.png|420]]" becomes an <img> (to keep the width) or a markdown
    image, with the path made relative to the output file. Returns the text
    and the names that couldn't be found.
    """
    unresolved = []

    def repl(m):
        name, width = m.group(1).strip(), (m.group(2) or "").strip()
        path = assets.get(name.lower())
        if path is None:
            unresolved.append(name)
            return f"*(missing image: {name})*"
        rel = os.path.relpath(path, out_dir)
        url = urllib.parse.quote(rel.replace(os.sep, "/"))
        if width.isdigit():
            return f'<img src="{url}" alt="{name}" width="{width}">'
        return f"![{name}]({url})"

    return EMBED_RE.sub(repl, text), unresolved


def convert_links(text: str, anchors: dict) -> tuple:
    """Rewrite [[wikilinks]] as links to the anchor of the included page.

    A link to a page that isn't in the index has nowhere to point, so it
    degrades to its plain text. Returns the text and the unresolved targets.
    """
    unresolved = []

    def repl(m):
        target, alias = m.group(1).strip(), m.group(2)
        label = (alias or target).strip()
        anchor = anchors.get(target.lower())
        if anchor is None:
            unresolved.append(target)
            return label
        return f"[{label}](#{anchor})"

    return LINK_RE.sub(repl, text), unresolved


def shift_headings(text: str, by: int) -> str:
    """Push a note's own headings down `by` levels so they nest under its
    title. Headings inside fenced code blocks are left alone."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        h = HEADING_RE.match(line) if not in_fence else None
        if h:
            level = min(len(h.group(1)) + by, MAX_LEVEL)
            out.append("#" * level + " " + h.group(2))
        else:
            out.append(line)
    return "\n".join(out)


def build(sections, assets, out_dir: str, toc: bool) -> tuple:
    """Render the combined document. Returns the text and a warnings list."""
    warnings = []

    # Anchors have to be known before any body is converted, so a link from
    # the first page can point at the last one.
    anchors = {}
    for _, pages in sections:
        for title, _path in pages:
            anchors[title.lower()] = slug(title)

    parts = [f"# {TITLE}", ""]

    if toc:
        parts += ["## contents", ""]
        for section, pages in sections:
            parts.append(f"- **{section}**")
            for title, _path in pages:
                parts.append(f"  - [{title}](#{slug(title)})")
        parts.append("")

    for section, pages in sections:
        if parts[-2:] != [f"# {TITLE}", ""]:
            parts += [RULE, ""]
        parts += ["#" * SECTION_LEVEL + f" {section}", ""]
        for i, (title, path) in enumerate(pages):
            # Pages inside a section are only told apart by their title, so
            # they get a rule between them; the first one already has the
            # section heading above it.
            if i:
                parts += [RULE, ""]
            with open(path, encoding="utf-8") as fh:
                body = strip_comments(strip_frontmatter(fh.read()))
            body, missing_imgs = convert_embeds(body, assets, out_dir)
            body, missing_links = convert_links(body, anchors)
            body = shift_headings(body, NOTE_LEVEL).strip()

            for name in missing_imgs:
                warnings.append(f"{title}: image not found — {name}")
            for name in sorted(set(missing_links)):
                warnings.append(f"{title}: link to a page outside the index — [[{name}]]")

            # The source path is an HTML comment: invisible once rendered,
            # but it makes the raw file easy to trace back to a note.
            source = os.path.relpath(path, ROOT).replace(os.sep, "/")
            parts += [f"<!-- {source} -->", "",
                      "#" * NOTE_LEVEL + f" {title}", "", body, ""]

    return "\n".join(parts).rstrip() + "\n", warnings


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-o", "--output", default=os.path.join(ROOT, DEFAULT_OUTPUT),
                    help=f"where to write the combined file (default: {DEFAULT_OUTPUT})")
    ap.add_argument("--no-toc", dest="toc", action="store_false",
                    help="leave out the table of contents")
    args = ap.parse_args()

    index_path = find_special(INDEX_FILE)
    if not index_path:
        raise SystemExit(f"{INDEX_FILE} not found — nothing to combine.")

    notes = find_notes()
    sections, missing, dupes = parse_index(index_path, notes)
    if not sections:
        raise SystemExit(f"{INDEX_FILE} lists no notes that exist.")

    out_path = os.path.abspath(args.output)
    out_dir = os.path.dirname(out_path) or "."
    text, warnings = build(sections, find_assets(), out_dir, args.toc)

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    pages = sum(len(p) for _, p in sections)
    words = len(text.split())
    rel = os.path.relpath(out_path, ROOT)
    print(f"Wrote {rel} — {len(sections)} section(s), {pages} page(s), {words} words.")

    for name in missing:
        warnings.insert(0, f"{INDEX_FILE}: [[{name}]] has no matching note — skipped")
    for name in dupes:
        warnings.insert(0, f"{INDEX_FILE}: [[{name}]] listed more than once — included once")
    for w in warnings:
        print(f"  warning: {w}")


if __name__ == "__main__":
    main()
