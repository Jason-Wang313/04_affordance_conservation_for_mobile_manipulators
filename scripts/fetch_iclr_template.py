"""Fetch the official ICLR 2026 LaTeX template into paper/."""

from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
DATA = ROOT / "data"
URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"
AUTHOR_GUIDE = "https://iclr.cc/Conferences/2026/AuthorGuide"


def main() -> int:
    PAPER.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    zip_path = PAPER / "iclr2026.zip"
    extract_dir = PAPER / "iclr2026_template"
    provenance = {
        "template": "ICLR 2026",
        "author_guide": AUTHOR_GUIDE,
        "template_url": URL,
        "status": "started",
        "files_copied": [],
    }
    try:
        response = requests.get(URL, timeout=60)
        response.raise_for_status()
        zip_path.write_bytes(response.content)
        if extract_dir.exists():
            shutil.rmtree(extract_dir)
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(extract_dir)
        wanted = [
            "iclr2026_conference.sty",
            "iclr2026_conference.bst",
            "math_commands.tex",
            "natbib.sty",
        ]
        for name in wanted:
            matches = list(extract_dir.rglob(name))
            if matches:
                shutil.copy2(matches[0], PAPER / name)
                provenance["files_copied"].append(name)
        provenance["status"] = "ok"
    except Exception as exc:
        provenance["status"] = "failed"
        provenance["error"] = str(exc)
        (PAPER / "template_fetch_failure.txt").write_text(f"Template fetch failed: {exc}\n", encoding="utf-8")
    (PAPER / "template_provenance.md").write_text(
        "# ICLR Template Provenance\n\n"
        f"- Author guide: {AUTHOR_GUIDE}\n"
        f"- Template URL: {URL}\n"
        f"- Status: {provenance['status']}\n"
        f"- Files copied: {', '.join(provenance['files_copied']) if provenance['files_copied'] else 'none'}\n",
        encoding="utf-8",
    )
    (DATA / "template_provenance.json").write_text(json.dumps(provenance, indent=2), encoding="utf-8")
    print(json.dumps(provenance, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        PAPER.mkdir(parents=True, exist_ok=True)
        (PAPER / "template_fetch_failure.txt").write_text(f"Template fetch fatal but recorded: {exc}\n", encoding="utf-8")
        print(f"TEMPLATE_FETCH_FAILURE_RECORDED: {exc}")
        raise SystemExit(0)
