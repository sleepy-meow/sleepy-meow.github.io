#!/usr/bin/env python3
"""Stage a copy of a note folder with page-index order prefixes added or removed.

The vault wants its notes to read in the order the page index lists them, so
push-learnings.sh renames them "<section>.<position> <name>.md" on the way in
("1.1 introduction.md"). pull-learnings.sh takes the prefixes back off, so the
repo copy — which the website orders from the index itself — stays clean.

Both modes write into a staging folder and leave the source untouched; the
sync scripts then mirror that folder with rsync.

    prefix-notes.py apply <page index.md> <src dir> <stage dir>
    prefix-notes.py strip <src dir> <stage dir>

Notes that the index doesn't list keep their plain name. Wikilinks are
rewritten to match the new filenames, so links still resolve inside the
vault; image embeds don't match an index entry, so they're left alone.
"""

import os
import re
import shutil
import sys

PREFIX = re.compile(r"^\d+\.\d+ ")
# [[target]], [[target|alias]], [[target#heading]] — target is group 2.
LINK = re.compile(r"(!?\[\[)([^\]|#]+)")


def read_order(index_path):
    """Map note name -> "section.position", numbering in index order.

    Entries commented out with %%…%% still hold their slot: they are part of
    the running order in Obsidian even though the website skips them.
    """
    order = {}
    section = item = 0
    with open(index_path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("# "):
                section += 1
                item = 0
                continue
            for target in LINK.findall(line):
                name = PREFIX.sub("", target[1].strip())
                item += 1
                order.setdefault(name, "%d.%d" % (section, item))
    return order


def rewrite_links(text, order):
    def sub(m):
        name = PREFIX.sub("", m.group(2).strip())
        return m.group(1) + order[name] + " " + name if name in order else m.group(0)
    return LINK.sub(sub, text)


def strip_links(text):
    return LINK.sub(lambda m: m.group(1) + PREFIX.sub("", m.group(2)), text)


def stage(src, dst, rename, transform):
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    renamed = 0
    for dirpath, dirnames, filenames in os.walk(src):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        rel = os.path.relpath(dirpath, src)
        out_dir = dst if rel == "." else os.path.join(dst, rel)
        os.makedirs(out_dir, exist_ok=True)
        for fn in filenames:
            if fn.startswith("."):
                continue
            src_file = os.path.join(dirpath, fn)
            if not fn.endswith(".md"):
                shutil.copy2(src_file, os.path.join(out_dir, fn))
                continue
            new_name = rename(fn)
            if new_name != fn:
                renamed += 1
            with open(src_file, encoding="utf-8") as fh:
                text = fh.read()
            out_file = os.path.join(out_dir, new_name)
            with open(out_file, "w", encoding="utf-8") as fh:
                fh.write(transform(text))
            # Keep the source's timestamp so rsync --times only reports files
            # whose content actually changed.
            st = os.stat(src_file)
            os.utime(out_file, (st.st_atime, st.st_mtime))
    return renamed


def main(argv):
    if len(argv) >= 2 and argv[0] == "apply" and len(argv) == 4:
        order = read_order(argv[1])
        src, dst = argv[2], argv[3]

        def rename(fn):
            name = PREFIX.sub("", fn[:-3])
            return "%s %s.md" % (order[name], name) if name in order else name + ".md"

        n = stage(src, dst, rename, lambda t: rewrite_links(t, order))
        print("%d prefixed" % n)
        return 0

    if len(argv) == 3 and argv[0] == "strip":
        src, dst = argv[1], argv[2]
        n = stage(src, dst, lambda fn: PREFIX.sub("", fn), strip_links)
        print("%d unprefixed" % n)
        return 0

    sys.stderr.write(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
