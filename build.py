#!/usr/bin/env python3
"""
build.py — gop index.html + cards/*.html thanh mot file duy nhat.

Dung khi nao:
  - Muon mo trang bang cach nhay doi chuot (file://), luc do fetch() bi chan
    nen cac card se khong hien.
  - Muon gui mot file duy nhat cho ai do.

Cach dung:
  python build.py                 -> tao index_standalone.html
  python build.py -o trang.html   -> tu dat ten file dau ra

Neu chi dat website len GitHub Pages / Netlify / server truong, KHONG can
chay file nay: index.html tu nap cards/ qua fetch va moi thu hoat dong.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SLOT = re.compile(r'[ \t]*<div class="card-slot" data-src="([^"]+)"></div>[ \t]*\n')


def build(out_name: str) -> int:
    index = ROOT / "index.html"
    if not index.exists():
        print("Khong tim thay index.html canh build.py", file=sys.stderr)
        return 1

    html = index.read_text(encoding="utf-8")
    missing = []

    def replace(match: "re.Match[str]") -> str:
        card = ROOT / match.group(1)
        if not card.exists():
            missing.append(match.group(1))
            return ""
        body = card.read_text(encoding="utf-8").rstrip("\n")
        body = "\n".join("    " + line if line.strip() else line
                         for line in body.split("\n"))
        return body + "\n\n"

    html, n = SLOT.subn(replace, html)
    if missing:
        print("Thieu file:", ", ".join(missing), file=sys.stderr)
        return 1

    # bo phan fallback va script nap card vi khong con can nua
    html = re.sub(r'[ \t]*<p id="card-fallback".*?</p>\n', "", html, flags=re.S)
    html = re.sub(r'<script>\n/\* Nap cac card.*?</script>\n\n', "", html, flags=re.S)

    (ROOT / out_name).write_text(html, encoding="utf-8")
    print(f"Da gop {n} card -> {out_name}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="index_standalone.html")
    sys.exit(build(ap.parse_args().output))
