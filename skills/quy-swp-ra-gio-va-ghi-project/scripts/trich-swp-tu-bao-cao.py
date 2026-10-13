#!/usr/bin/env python3
"""Trích SWP đã chốt từ báo cáo HTML của tkm:sun-estimate → JSON làm đầu vào cho bước quy đổi giờ và ghi Project.

Đọc payload nhúng `<script id="report-data" type="application/json">` (nguồn số duy nhất của báo cáo), không đọc
phần hiển thị. Mỗi leaf task (issue/sub-issue được chấm trực tiếp) được gán nhóm việc để quy đổi giờ:
  lam-ro  : workType = investigation (làm rõ với khách)
  FE-QA   : primaryDiscipline UI hoặc QA (giao diện, kiểm thử)
  BE      : còn lại (API, DB, migration, hạ tầng, tích hợp)

Đầu ra: {"nguon", "viec": [leaf], "cha": [epic/issue cha], "swp": {số issue: SWP}} — "swp" gồm cả cha (tổng con).

Dùng: python3 trich-swp-tu-bao-cao.py <bao-cao.html> -o swp.json
"""
import argparse, html, json, re, sys
from pathlib import Path

MA = re.compile(r"^\[([A-Z]+-[\d.]+)\]\s*(.*)$")


def nhom(x):
    if x.get("workType") == "investigation":
        return "lam-ro"
    return "FE-QA" if x.get("primaryDiscipline") in ("UI", "QA") else "BE"


def so(ref):
    return ref.rsplit("#", 1)[1] if ref and "#" in ref else None


def doc_payload(f):
    m = re.search(r'<script id="report-data" type="application/json">(.*?)</script>', f.read_text(), re.S)
    if not m:
        sys.exit(f"LỖI: {f} không có payload report-data (không phải báo cáo của tkm:sun-estimate?)")
    t = m[1].strip()
    return json.loads(html.unescape(t) if t.startswith("&") else t)


def dong(x, la):
    m = MA.match(x.get("title", ""))
    d = {"so": so(x["issueRef"]), "ma": m[1] if m else None, "tieu_de": m[2] if m else x.get("title", ""),
         "cha_so": so(x.get("parentRef")), "swp": x.get("finalSWP")}
    if la:
        d["nhom"] = nhom(x)
    return d


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("bao_cao")
    a.add_argument("-o", "--ra", required=True)
    g = a.parse_args()
    p = doc_payload(Path(g.bao_cao))
    viec = [dong(x, True) for x in p["issues"]]
    cha = [dong(x, False) for x in p["parents"]]
    thieu = [v["so"] for v in viec if not isinstance(v["swp"], (int, float))]
    if thieu:
        sys.exit(f"LỖI: leaf task chưa có SWP chốt: {thieu[:10]}")
    ra = {"nguon": Path(g.bao_cao).name, "viec": viec, "cha": cha,
          "swp": {d["so"]: d["swp"] for d in viec + cha if d["swp"] is not None}}
    Path(g.ra).write_text(json.dumps(ra, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(viec)} leaf task · {len(cha)} cha · tổng SWP leaf {sum(v['swp'] for v in viec)} → {g.ra}")


if __name__ == "__main__":
    main()
