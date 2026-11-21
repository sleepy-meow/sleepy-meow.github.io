#!/usr/bin/env bash
# Rebuild the note index and serve the site locally.
# Usage: ./serve.sh [port]   (default port: 8000)
set -euo pipefail

cd "$(dirname "$0")"
PORT="${1:-8000}"

python3 build-index.py

URL="http://localhost:$PORT/"
echo "Serving at $URL  (Ctrl+C to stop)"
(sleep 1 && open "$URL") &
python3 -m http.server "$PORT"
