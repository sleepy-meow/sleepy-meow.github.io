#!/usr/bin/env bash
# Copy the Obsidian notes into the website and regenerate the manifest.
#
# Layout: each subfolder of the tools vault becomes its own sidebar category
# (e.g. "books", "practical tools"); the loose root notes become the
# "learnings" category. The "wip" subfolder is skipped.
set -euo pipefail

SITE="/Users/laura.koekoek/stuff/docs/vaults/sleepy-meow.github.io"
SRC="/Users/laura.koekoek/stuff/docs/vaults/knowledge-hub/tools"
IMG_SRC="/Users/laura.koekoek/stuff/docs/vaults/knowledge-hub/pasted images"

# 1. Remove previously-synced category folders so renamed/removed/wip'd notes
#    disappear. Keep the repo, Obsidian config, and the images folder.
find "$SITE" -mindepth 1 -maxdepth 1 -type d \
  ! -name '.git' ! -name '.obsidian' ! -name 'pasted images' \
  -exec rm -rf {} +

# 2. Loose root notes → the "learnings" category.
mkdir -p "$SITE/learnings"
cp "$SRC"/*.md "$SITE/learnings/"

# 3. Each subfolder (except wip) → its own category of the same name.
for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  [ "$name" = "wip" ] && continue
  mkdir -p "$SITE/$name"
  cp "$dir"*.md "$SITE/$name/" 2>/dev/null || true
done

# 4. Copy the Obsidian attachment folder so embedded images resolve.
rm -rf "$SITE/pasted images"
[ -d "$IMG_SRC" ] && cp -R "$IMG_SRC" "$SITE/pasted images"

python3 "$SITE/build-index.py"
echo "Synced notes + images from the vault → $SITE and rebuilt files.json"
