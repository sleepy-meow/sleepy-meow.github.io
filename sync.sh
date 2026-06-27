#!/usr/bin/env bash
# Copy the Obsidian notes into the website and regenerate the manifest.
set -euo pipefail

SITE="/Users/laura.koekoek/stuff/docs/vaults/sleepy-meow.github.io"
SRC="/Users/laura.koekoek/stuff/docs/vaults/knowledge-hub/tools"

# Mirror only the root-level notes (not the wip/ subfolder): clear out any
# stale copies first, then copy the current root .md files.
rm -f "$SITE/learnings/"*.md
cp "$SRC"/*.md "$SITE/learnings/"
python3 "$SITE/build-index.py"
echo "Synced root notes from $SRC → $SITE/learnings and rebuilt files.json"
