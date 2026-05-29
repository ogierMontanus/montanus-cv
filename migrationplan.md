# Portfolio Website Migration and Modernization Plan

## Project Goal

Migrate and modernize a legacy academic portfolio website originally built on webs.com and preserved through archive.org snapshots.

The new website should:

* preserve the overall tone and information architecture of the original site
* modernize content and presentation
* function as a curated academic CV and portfolio
* be maintainable through Git-based workflows
* support lightweight automated updates for publications
* incur no hosting or subscription costs
* remain understandable to AI tools and future collaborators

The canonical language of the site is English.

When scraping or recovering material from archive.org, always prioritize the English-language version of pages.

---

# Core Technical Decisions

## Hosting

Use GitHub Pages for deployment.

Advantages:

* free hosting
* simple static deployment
* no server maintenance
* Git-native workflow
* broad ecosystem support

---

## Site Generator

Use Eleventy (11ty).

Rationale:

* simple static generation
* minimal framework overhead
* content-first architecture
* easy AI-assisted editing
* future portability

Avoid heavy JavaScript frameworks unless interactive features later become necessary.

---

# Repository Structure

```text
/
├── content/
│   ├── publications/
│   ├── talks/
│   ├── teaching/
│   ├── cv/
│   ├── projects/
│   └── pages/
│
├── assets/
│   ├── images/
│   ├── pdf/
│   └── css/
│
├── data/
│   ├── pure/
│   └── cache/
│
├── scripts/
│   ├── sync_pure.py
│   └── generate_site.py
│
├── templates/
├── docs/
├── .github/
└── README.md
```

---

# Migration Workflow

## Phase 1 — Archive Recovery

Recover:

* page hierarchy
* navigation structure
* images
* downloadable PDFs
* core textual content
* visual tone and layout cues

Do not reproduce obsolete widgets or outdated interactive elements.

Create a migration inventory documenting:

* reusable material
* outdated material
* missing assets
* pages requiring rewrite

---

## Phase 2 — Content Normalization

Convert all reusable material into Markdown files with structured frontmatter.

Example:

```yaml
---
title: "Example Publication"
date: 2024-02-01
type: publication
status: published
category: research
tags:
  - folklore
  - print culture
pure_id: "123456"
selected: true
---
```

The repository itself becomes the canonical source.

Rendered HTML should always be generated from structured content files.

---

# Publication Strategy

## Canonical External Source

Use the university Pure profile as the external authoritative source for publication metadata.

The public website should *not* mirror the full Pure profile automatically.

Instead:

* the website contains a curated subset
* Pure remains the comprehensive bibliography
* the site links outward to the full institutional profile

---

## Curation Pipeline

The synchronization pipeline must support filtering.

Only include:

* peer-reviewed research
* major publications
* selected edited volumes
* significant outputs

Exclude:

* dissemination items
* administrative outputs
* small notices
* low-relevance entries

The filtering process should support:

* automatic filtering by publication type
* manual overrides through metadata flags

Example:

```yaml
selected: true
```

or

```yaml
include_on_site: false
```

---

# Synchronization Workflow

## Preferred Architecture

```text
Pure profile
      ↓
manual or scheduled sync script
      ↓
normalized JSON/YAML
      ↓
manual review layer
      ↓
Eleventy build
      ↓
GitHub Pages deployment
```

---

# Automation Policy

Automation should remain conservative.

Goals:

* avoid brittle scraping
* avoid unexpected content floods
* preserve editorial control

Recommended cadence:

* monthly manual sync
* optional GitHub Actions automation later

Avoid live runtime integrations.

All metadata should be cached locally in the repository.

---

# User Experience Goals

The website should function primarily as:

* academic landing page
* curated scholarly CV
* portfolio overview
* publication showcase

Secondary goals:

* lightweight discoverability
* stable citation URLs
* clean navigation
* long-term maintainability

---

# Features: Required vs Optional

## Required

* responsive design
* publications section
* CV page
* contact page
* project descriptions
* stable URLs
* downloadable CV PDF

## Optional / Later

* full-text search
* faceted publication filters
* BibTeX export
* Zotero integration
* interactive visualizations

These should not shape the initial architecture.

---

# Design Principles

The site should:

* remain lightweight
* privilege readability over visual complexity
* use restrained typography
* avoid animation-heavy design
* preserve a scholarly tone

The original webs.com design should be treated as inspiration rather than a template for literal reproduction.

---

# Documentation for Future AI-Assisted Maintenance

Include machine-readable documentation in `/docs/`.

Suggested files:

```text
site_architecture.md
content_model.md
deployment.md
editorial_rules.md
sync_pipeline.md
```

This enables future chatbot-assisted maintenance and migration work.

---

# Recommended Initial Timeline

## Week 1

* recover archive material
* inventory pages and assets
* classify reusable content

## Week 2

* initialize repository
* configure Eleventy
* configure GitHub Pages deployment
* establish content schema

## Week 3

* migrate core pages
* rewrite outdated material
* establish publication templates

## Week 4

* implement Pure synchronization
* add manual curation workflow
* finalize deployment

```
```
