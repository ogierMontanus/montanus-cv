# Project Memory — montanus-cv

## Site Owner

**Nils Holger Nemeth Berg** (also known as Holger Berg)
Historian, University of Southern Denmark (SDU)
Email: nh@sdu.dk

## ORCID

ORCID ID: `0000-0002-8496-7221`
Public profile: https://orcid.org/0000-0002-8496-7221
API endpoint: https://pub.orcid.org/v3.0/0000-0002-8496-7221/works

Use this ID in `scripts/sync_orcid.py` as `ORCID_ID`.

## Migration Plan

See `migrationplan.md` (original) and `/root/.claude/plans/adapt-and-elaborate-plan-wondrous-knuth.md` (adapted plan with ORCID integration).

### Key decisions

- Hosting: GitHub Pages
- Generator: Eleventy (11ty)
- Publication source: ORCID (replaces Pure)
- Canonical language: English
- Danish and German versions of English pages are ignored during migration
- `montanus-webs/foreign-src/` is excluded from the current migration scope

### English-only source files (in montanus-webs/)

- `curriculumvitae.htm` → `data/cv.yaml`
- `books.htm` → `data/publications.yaml` (book entries)
- `editions.htm` → `data/editions.yaml`
- `museumwork.htm` → `data/museum_work.yaml`

Articles section is populated from ORCID; no English articles.htm exists in the main folder.
