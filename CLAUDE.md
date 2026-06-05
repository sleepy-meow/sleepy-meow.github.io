# Project notes for Claude

## Workflow

- **When I say "push changes":** run `python3 build-index.py` first to regenerate
  `files.json`, then stage, commit, and push all changes in the repo.
- **When I say "preview":** serve the site on a local web server (e.g.
  `python3 -m http.server 8099`) and open `http://localhost:8099/` in the browser.
