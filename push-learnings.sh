#!/usr/bin/env bash
# Mirror this repo's note folders INTO the Obsidian vault.
#
#     <repo>/learnings/  ──►  main-vault/sleepy/learnings/
#     <repo>/wip/        ──►  main-vault/sleepy/wip/
#
# This is a mirror, not a merge: files that exist in the vault copy but not
# in the repo copy are DELETED. pull-learnings.sh goes the other way.
#
# Usage: ./push-learnings.sh [-n|--dry-run] [-y|--yes]
#   -n   show what would change, write nothing
#   -y   don't ask before deleting (for unattended runs)
set -euo pipefail

FOLDERS="learnings wip"
SRC_ROOT="/Users/laura.koekoek/stuff/docs/vaults/sleepy-meow.github.io"
DST_ROOT="/Users/laura.koekoek/stuff/docs/vaults/main-vault/sleepy"

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
    -h|--help)    sed -n '2,12p' "$0" | cut -c3-; exit 0 ;;
    *) echo "unknown option: $arg (try --help)" >&2; exit 2 ;;
  esac
done

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

synced=""
changed=""
deletions=0
total=0

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

  # No mkdir here: a --dry-run must not create anything. rsync plans a
  # missing destination fine, and the apply loop below creates it.
  "${RSYNC[@]}" --dry-run --itemize-changes "$src/" "$dst/" |
    grep -v ' \./$' > "$tmp/$f.plan" || true

  synced="$synced $f"
  if [ -s "$tmp/$f.plan" ]; then
    changed="$changed $f"
    deletions=$(( deletions + $(grep -c '^\*deleting' "$tmp/$f.plan" || true) ))
    total=$(( total + $(wc -l < "$tmp/$f.plan") ))
  fi
done

if [ -z "$synced" ]; then
  echo "nothing to sync — no usable source folders" >&2
  exit 1
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

for f in $synced; do
  mkdir -p "$DST_ROOT/$f"
  "${RSYNC[@]}" "$SRC_ROOT/$f/" "$DST_ROOT/$f/" >/dev/null
done
echo "pushed$synced → $DST_ROOT"
