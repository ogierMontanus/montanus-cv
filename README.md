# montanus-cv

Academic CV and portfolio website for **Nils Holger Nemeth Berg** (Holger Berg), historian at the University of Southern Denmark (SDU). Built with [Eleventy (11ty)](https://www.11ty.dev/) and deployed to GitHub Pages.

## Project structure

- `content/` — page source files (Nunjucks/Markdown)
- `templates/` — layouts and includes (`_includes`)
- `data/` — YAML data files consumed by templates (CV, publications, editions, museum work, ORCID cache)
- `assets/` — static assets copied as-is to the built site
- `scripts/` — utility scripts, including `sync_orcid.py` for pulling publications from ORCID
- `montanus-webs/` — archived source material from the legacy site, used during migration
- `_site/` — generated output (build artifact, not committed — see below)

## Development

```bash
npm install
npm run serve   # local dev server with live reload
npm run build   # build the static site into _site/
```

To refresh publications from ORCID:

```bash
npm run sync-orcid
```

## Deploying to GitHub Pages

The site is built with Eleventy, which outputs the static site to the **`_site/`** folder (see the `dir.output` setting in `.eleventy.js`). `_site/` is git-ignored and is **not** committed to the repository — it is generated at build time.

The site is served as a GitHub **project page** at `https://<user>.github.io/montanus-cv/`, not at the domain root. Because of this, `.eleventy.js` sets `pathPrefix: "/montanus-cv/"`, and all internal links/asset references in templates use Eleventy's `url` filter (e.g. `{{ '/assets/css/style.css' | url }}`) so they resolve under that subpath instead of 404ing at the domain root. If the site is ever moved to a custom domain or a `<user>.github.io` root repo, update or remove `pathPrefix` accordingly.

Deployment is automated via `.github/workflows/deploy.yml`: on every push to `main`, GitHub Actions runs `npm ci && npm run build` and then publishes the contents of `_site/` to the `gh-pages` branch using [`peaceiris/actions-gh-pages`](https://github.com/peaceiris/actions-gh-pages).

If configuring GitHub Pages manually (e.g. in repository Settings → Pages), set:

- **Source:** Deploy from a branch
- **Branch:** `gh-pages` / `root`

Do not point GitHub Pages at `main` or at the `_site/` folder in `main` — that folder is only ever built inside CI and pushed to `gh-pages`, never committed to `main` directly.

A separate workflow, `.github/workflows/orcid_sync.yml`, runs monthly to sync publications from ORCID and commits small diffs automatically (larger diffs are flagged for manual review).
