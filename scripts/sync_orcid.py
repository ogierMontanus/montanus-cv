#!/usr/bin/env python3
"""Fetch publications from ORCID public API and produce data/publications.yaml.

Usage:
  python3 scripts/sync_orcid.py           # full run
  python3 scripts/sync_orcid.py --dry-run  # print diff, no write
  python3 scripts/sync_orcid.py --force    # overwrite even if cache unchanged
"""

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import yaml

ORCID_ID = "0000-0002-8496-7221"
ORCID_BASE = f"https://pub.orcid.org/v3.0/{ORCID_ID}"
HEADERS = {"Accept": "application/json"}

ACCEPTED_TYPES = {
    "journal-article",
    "book",
    "book-chapter",
    "edited-book",
    "dissertation",
}

ROOT = Path(__file__).parent.parent
CACHE_FILE = ROOT / "data" / "orcid_cache.json"
OVERRIDES_FILE = ROOT / "data" / "orcid_overrides.yaml"
OUTPUT_FILE = ROOT / "data" / "publications.yaml"


def fetch_works():
    print(f"Fetching works summary for ORCID {ORCID_ID} ...")
    r = requests.get(f"{ORCID_BASE}/works", headers=HEADERS, timeout=30)
    r.raise_for_status()
    summary = r.json()

    put_codes = []
    for group in summary.get("group", []):
        for ws in group.get("work-summary", []):
            put_codes.append(ws["put-code"])

    print(f"  Found {len(put_codes)} works. Fetching full records ...")
    full_works = []
    for i, pc in enumerate(put_codes, 1):
        time.sleep(0.2)
        wr = requests.get(f"{ORCID_BASE}/work/{pc}", headers=HEADERS, timeout=30)
        wr.raise_for_status()
        full_works.append(wr.json())
        if i % 10 == 0:
            print(f"  {i}/{len(put_codes)}")

    return full_works


def extract_external_ids(work):
    ids = {}
    for eid in work.get("external-ids", {}).get("external-id", []):
        ids[eid["external-id-type"]] = eid["external-id-value"]
    return ids


def get_nested(d, *keys, default=None):
    for k in keys:
        if not isinstance(d, dict):
            return default
        d = d.get(k, {})
    return d if d != {} else default


def transform_work(raw):
    work_type = raw.get("type", "")
    if work_type not in ACCEPTED_TYPES:
        return None

    title_val = get_nested(raw, "title", "title", "value") or ""
    subtitle_val = get_nested(raw, "title", "subtitle", "value")
    year_val = get_nested(raw, "publication-date", "year", "value")
    journal_val = get_nested(raw, "journal-title", "value")
    ext_ids = extract_external_ids(raw)

    contributors = []
    for c in raw.get("contributors", {}).get("contributor", []):
        name = get_nested(c, "credit-name", "value")
        if name:
            contributors.append(name)

    return {
        "orcid_put_code": str(raw["put-code"]),
        "title": title_val,
        "subtitle": subtitle_val,
        "year": int(year_val) if year_val else None,
        "type": work_type,
        "container_title": journal_val,
        "doi": ext_ids.get("doi"),
        "isbn": ext_ids.get("isbn"),
        "contributors": contributors or None,
        "selected": False,
        "include_on_site": True,
    }


def load_overrides():
    if not OVERRIDES_FILE.exists():
        return []
    with open(OVERRIDES_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def merge(transformed, overrides):
    override_map = {}
    manual_entries = []
    for o in overrides:
        pc = o.get("orcid_put_code")
        if pc:
            override_map[str(pc)] = o
        else:
            manual_entries.append(o)

    merged = []
    for item in transformed:
        pc = item.get("orcid_put_code")
        if pc and pc in override_map:
            patch = override_map[pc]
            # never clear protective flags set in overrides
            merged_item = {**item}
            for k, v in patch.items():
                if k in ("selected", "include_on_site") and merged_item.get(k) in (True, False):
                    # override wins only if it is more restrictive
                    if k == "include_on_site" and v is False:
                        merged_item[k] = False
                    elif k == "selected" and v is True:
                        merged_item[k] = True
                else:
                    merged_item[k] = v
            merged.append(merged_item)
        else:
            merged.append(item)

    merged.extend(manual_entries)
    merged.sort(key=lambda x: (-(x.get("year") or 0), x.get("title", "")))
    return merged


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        full_works = fetch_works()
    except Exception as e:
        print(f"ERROR fetching from ORCID: {e}", file=sys.stderr)
        sys.exit(1)

    # write raw cache
    if not args.dry_run:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(full_works, f, indent=2, ensure_ascii=False)
        print(f"Wrote {CACHE_FILE}")

    # transform
    transformed = [t for w in full_works if (t := transform_work(w)) is not None]
    print(f"  {len(transformed)} works accepted after type filter "
          f"({len(full_works) - len(transformed)} discarded)")

    # merge overrides
    overrides = load_overrides()
    result = merge(transformed, overrides)

    yaml_out = yaml.dump(result, allow_unicode=True, default_flow_style=False,
                         sort_keys=False)

    if args.dry_run:
        print("\n--- publications.yaml (dry run) ---")
        print(yaml_out[:3000])
        if len(yaml_out) > 3000:
            print(f"... ({len(yaml_out)} chars total)")
        return

    if OUTPUT_FILE.exists() and not args.force:
        existing = OUTPUT_FILE.read_text(encoding="utf-8")
        if existing == yaml_out:
            print("No changes to publications.yaml.")
            return

    OUTPUT_FILE.write_text(yaml_out, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE} ({len(result)} entries)")


if __name__ == "__main__":
    main()
