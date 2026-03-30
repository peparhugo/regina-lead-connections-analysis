# Regina Authority Note

Canonical local project root for Regina Lead is:
- `/root/.openclaw/workspace/projects/regina-lead-github-pages`

Non-canonical salvage location:
- `/root/.openclaw/workspace-main/projects/regina-lead-github-pages`

Rules:
- New Regina project work should land in canonical `workspace`, not `workspace-main`.
- `workspace-main` may be used only as a salvage/reference source when recovering missing artifacts.
- If an artifact exists in both places and differs, treat `workspace` as the active authority unless an explicit governed recovery step says otherwise.
- Public/reviewable project slices should be promoted from canonical `workspace` into `https://github.com/peparhugo/regina-lead-connections-analysis` through bounded commits and pull requests.
