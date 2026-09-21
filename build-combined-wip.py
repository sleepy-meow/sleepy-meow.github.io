#!/usr/bin/env python3
"""Combine the indexed notes into one markdown file — work in progress included.

The same job build-combined.py does, with one difference: a page marked "?" in
the page index is a draft and that script leaves it out, while this one keeps
it. So the result is the set the site shows once you flip its "very WIP"
switch: everything marked "!!", drafts and all.

Everything else — the landing page, index order, section headings, wikilink
and image conversion, the table of contents — is build-combined.py's code,
imported from it, so the two can't drift apart.

  python3 build-combined-wip.py                     # -> combined-wip.md
  python3 build-combined-wip.py -o ~/notes.md       # somewhere else
  python3 build-combined-wip.py --no-toc            # skip the table of contents
  python3 build-combined-wip.py --no-landing        # skip the landing page
  python3 build-combined-wip.py --all               # every indexed page, "!!" or not

Nothing here touches files.json or the site — run build-index.py for that.
"""
import importlib.util
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

OUTPUT = "combined-wip.md"


def load_combined():
    """Import build-combined.py. It can't be imported by name — the hyphen
    isn't a legal identifier — so it's loaded from its path."""
    path = os.path.join(ROOT, "build-combined.py")
    spec = importlib.util.spec_from_file_location("build_combined", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"can't load {path} — is it still next to this script?")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    combined = load_combined()
    combined.main(keep=combined.keep_done_or_wip,
                  default_output=OUTPUT,
                  description=__doc__)
