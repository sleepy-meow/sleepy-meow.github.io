#!/usr/bin/env bash
# Mirror this repo's note folders INTO the Obsidian vault, in page-index
# order, along with the images those notes embed.
#
#     <repo>/learnings/     ──►  main-vault/sleepy/learnings/
#     <repo>/wip/           ──►  main-vault/sleepy/wip/
#     <repo>/pasted images/ ──►  main-vault/sleepy/images/   (referenced only)
#
# Notes are renamed "<section>.<position> <name>.md" on the way in, numbered
# from learnings/page index.md so the vault reads in the same order the site
# does — the count runs across both folders, so a wip note keeps its slot.
# Wikilinks are rewritten to match, so links still resolve in the vault.
# pull-learnings.sh takes the prefixes back off.
#
# This is a mirror, not a merge: files that exist in the vault copy but not
# in the repo copy are DELETED.
#
# Usage: ./push-learnings.sh [-n|--dry-run] [-y|--yes]
#   -n   show what would change, write nothing
#   -y   don't ask before deleting (for unattended runs)
set -euo pipefail

FOLDERS="learnings wip"
SRC_ROOT="/Users/laura.koekoek/stuff/docs/vaults/sleepy-meow.github.io"
DST_ROOT="/Users/laura.koekoek/stuff/docs/vaults/main-vault/sleepy"
IMG_SRC="$SRC_ROOT/pasted images"
IMG_DST="$DST_ROOT/images"
PAGE_INDEX="$SRC_ROOT/learnings/page index.md"
PREFIXER="$SRC_ROOT/prefix-notes.py"

# --times keeps modification dates; --perms is deliberately left off so the
# copies get normal umask permissions instead of inheriting the vault's.
RSYNC=(rsync --recursive --links --times --delete
       --exclude '.DS_Store' --exclude '.obsidian/'
       --exclude '.trash/'   --exclude '.git/')

dry_run=0
assume_yes=0
for arg in "$@"; do
  case "$arg" in
    -n|--dry-run) dry_run=1 ;;
    -y|--yes)     assume_yes=1 ;;
    -h|--help)    sed -n '2,21p' "$0" | cut -c3-; exit 0 ;;
    *) echo "unknown option: $arg (try --help)" >&2; exit 2 ;;
  esac
done

[ -f "$PAGE_INDEX" ] || { echo "page index missing: $PAGE_INDEX" >&2; exit 1; }
[ -f "$PREFIXER" ]   || { echo "helper missing: $PREFIXER" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Every image embedded by a note in $FOLDERS, as a bare filename. Covers
# Obsidian's ![[name.png]] (with an optional |size) and markdown ![](path).
collect_images() {
  local f
  for f in $FOLDERS; do
    [ -d "$SRC_ROOT/$f" ] || continue
    find "$SRC_ROOT/$f" -type f -name '*.md' -print0 |
      xargs -0 grep -hoE '!\[\[[^]]+\]\]|!\[[^]]*\]\([^)]+\)' 2>/dev/null || true
  done |
    sed -E 's/^!\[\[//; s/\]\]$//; s/\|[^|]*$//' |
    sed -E 's/^!\[[^]]*\]\(//; s/\)$//' |
    sed -E 's/.*\///; s/%20/ /g' |
    grep -iE '\.(png|jpe?g|gif|webp|svg|avif)$' |
    sort -u
}

synced=""
changed=""
deletions=0
total=0

# ---- notes ----------------------------------------------------------------
for f in $FOLDERS; do
  src="$SRC_ROOT/$f"
  dst="$DST_ROOT/$f"

  if [ ! -d "$src" ]; then
    echo "skipping $f/ — no such folder: $src" >&2
    continue
  fi
  # A folder that lost its notes would silently empty its counterpart, so
  # it is skipped rather than mirrored. Delete the other side by hand.
  if [ -z "$(find "$src" -maxdepth 1 -name '*.md' -print -quit)" ]; then
    echo "skipping $f/ — no .md files in $src (would empty $dst)" >&2
    continue
  fi

  # Renamed copies are staged in a temp folder; the repo is never touched.
  python3 "$PREFIXER" apply "$PAGE_INDEX" "$src" "$tmp/$f" >/dev/null

  # No mkdir of $dst here: a --dry-run must not create anything. rsync plans
  # a missing destination fine, and the apply loop below creates it.
  "${RSYNC[@]}" --dry-run --itemize-changes "$tmp/$f/" "$dst/" |
    grep -vE ' \./$|^created directory ' > "$tmp/$f.plan" || true

  synced="$synced $f"
  if [ -s "$tmp/$f.plan" ]; then
    changed="$changed $f"
    deletions=$(( deletions + $(grep -c '^\*deleting' "$tmp/$f.plan" || true) ))
    total=$(( total + $(wc -l < "$tmp/$f.plan") ))
  fi
done

# ---- images those notes embed ---------------------------------------------
# Staged the same way, so the mirror carries exactly the images that are
# still referenced — one no longer embedded gets deleted from the vault
# copy, just like a deleted note.
stage="$tmp/.images"
mkdir -p "$stage"
staged=0
missing=""

if [ -d "$IMG_SRC" ]; then
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    if [ -f "$IMG_SRC/$name" ]; then
      ln "$IMG_SRC/$name" "$stage/$name" 2>/dev/null || cp "$IMG_SRC/$name" "$stage/$name"
      staged=$(( staged + 1 ))
    else
      missing="$missing  $name
"
    fi
  done <<< "$(collect_images)"
else
  echo "skipping images — no such folder: $IMG_SRC" >&2
fi

images=0
if [ "$staged" -gt 0 ]; then
  images=1
  "${RSYNC[@]}" --dry-run --itemize-changes "$stage/" "$IMG_DST/" |
    grep -vE ' \./$|^created directory ' > "$tmp/images.plan" || true
  synced="$synced images"
  if [ -s "$tmp/images.plan" ]; then
    changed="$changed images"
    deletions=$(( deletions + $(grep -c '^\*deleting' "$tmp/images.plan" || true) ))
    total=$(( total + $(wc -l < "$tmp/images.plan") ))
  fi
elif [ -d "$IMG_SRC" ]; then
  echo "skipping images — no embedded images found (would empty $IMG_DST)" >&2
fi

# ---- report ---------------------------------------------------------------
if [ -z "$synced" ]; then
  echo "nothing to sync — no usable source folders" >&2
  exit 1
fi

if [ -n "$missing" ]; then
  echo "referenced but not found in $IMG_SRC:" >&2
  printf '%s' "$missing" >&2
  echo >&2
fi

if [ -z "$changed" ]; then
  echo "already in sync:$synced"
  exit 0
fi

for f in $changed; do
  echo "$f/"
  awk '{
    flag = $1; rest = $0; sub(/^[^ ]+[ ]+/, "", rest)
    if (flag == "*deleting")   printf "  delete  %s\n", rest
    else if (flag ~ /\+\+\+/)  printf "  new     %s\n", rest
    else                       printf "  update  %s\n", rest
  }' "$tmp/$f.plan"
done

echo
echo "$total change(s) — $deletions deletion(s) — into $DST_ROOT"
[ "$images" -eq 1 ] && echo "($staged image(s) referenced by the notes)"

if [ "$dry_run" -eq 1 ]; then
  echo "(dry run — nothing written)"
  exit 0
fi

if [ "$deletions" -gt 0 ] && [ "$assume_yes" -eq 0 ]; then
  if [ -t 0 ]; then
    read -r -p "Delete $deletions file(s) from the vault? [y/N] " reply
    case "$reply" in [yY]*) ;; *) echo "aborted"; exit 1 ;; esac
  else
    echo "refusing to delete without confirmation; re-run with -y" >&2
    exit 1
  fi
fi

# ---- apply ----------------------------------------------------------------
for f in $synced; do
  if [ "$f" = "images" ]; then
    mkdir -p "$IMG_DST"
    "${RSYNC[@]}" "$stage/" "$IMG_DST/" >/dev/null
  else
    mkdir -p "$DST_ROOT/$f"
    "${RSYNC[@]}" "$tmp/$f/" "$DST_ROOT/$f/" >/dev/null
  fi
done
echo "pushed$synced → $DST_ROOT"
