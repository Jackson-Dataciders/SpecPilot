#!/usr/bin/env python3
"""Lightweight consistency checks for the SpecPilot docs vault.

Validates the conventions the framework relies on, with no third-party
dependencies. Run from the repository root:

    python scripts/lint_docs.py

Exits non-zero if any violation is found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path("docs")
SPECS = DOCS / "specs"
ADRS = DOCS / "adr"
TEMPLATES = DOCS / "_templates"

SPEC_NAME = re.compile(r"^\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
ADR_NAME = re.compile(r"^\d{4}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")

SPEC_STATUS = {"backlog", "ready", "planned", "in-progress", "done"}
ADR_STATUS = {"proposed", "accepted", "superseded", "deprecated"}

errors: list[str] = []


def err(path: Path, msg: str) -> None:
    errors.append(f"{path.as_posix()}: {msg}")


def frontmatter(text: str) -> dict[str, str]:
    """Parse a flat top-level YAML frontmatter block into scalar strings."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def check_markdown_files() -> None:
    for md in DOCS.rglob("*.md"):
        if TEMPLATES in md.parents:
            continue
        text = md.read_text(encoding="utf-8")
        if WIKILINK.search(text):
            err(md, "contains a wikilink ([[...]]); use relative Markdown links instead")


def check_specs() -> None:
    if not SPECS.exists():
        return
    for md in SPECS.glob("*.md"):
        if not SPEC_NAME.match(md.name):
            err(md, "spec filename must match NNN-kebab-title.md")
        fm = frontmatter(md.read_text(encoding="utf-8"))
        status = fm.get("status")
        if status is not None and status not in SPEC_STATUS:
            err(md, f"invalid status '{status}'; expected one of {sorted(SPEC_STATUS)}")
        created = fm.get("created", "")
        if created and not DATE.match(created):
            err(md, f"created '{created}' is not YYYY-MM-DD")


def check_adrs() -> None:
    if not ADRS.exists():
        return
    for md in ADRS.glob("*.md"):
        if not ADR_NAME.match(md.name):
            err(md, "ADR filename must match NNNN-kebab-title.md")
        fm = frontmatter(md.read_text(encoding="utf-8"))
        status = fm.get("status")
        if status is not None and status not in ADR_STATUS:
            err(md, f"invalid status '{status}'; expected one of {sorted(ADR_STATUS)}")
        date = fm.get("date", "")
        if date and not DATE.match(date) and date != "YYYY-MM-DD":
            err(md, f"date '{date}' is not YYYY-MM-DD")


def main() -> int:
    if not DOCS.exists():
        print("No docs/ directory found; run from the repository root.", file=sys.stderr)
        return 2
    check_markdown_files()
    check_specs()
    check_adrs()
    if errors:
        print(f"Docs lint found {len(errors)} issue(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Docs lint passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
