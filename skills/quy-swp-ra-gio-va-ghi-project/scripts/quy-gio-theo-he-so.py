#!/usr/bin/env python3
"""Quy đổi SWP sang giờ: hệ số giờ/SWP theo nhóm việc, lấy từ issue mẫu được ước giờ trực tiếp KHÔNG xem SWP.

Quy tắc:
- Hệ số nhóm = tổng giờ ước trực tiếp của mẫu trong nhóm ÷ tổng SWP của các mẫu đó (làm tròn 2 chữ số).
- Giờ leaf task = SWP × hệ số nhóm, làm tròn 0,5 giờ (tối thiểu 0,5).
- Ngoại lệ (tuỳ chọn): leaf task có giờ ước trực tiếp từng việc thì dùng giờ đó thay giờ quy từ SWP.
- Epic, issue cha = tổng giờ con (đệ quy theo cha_so).
Giờ là công làm thuần của một người: không gồm dự phòng, chờ khách, quản lý dự án.

Đầu vào:
  --swp       JSON từ trich-swp-tu-bao-cao.py
  --mau       {"mau": [{"issue": "#43", "nhom": "BE"|"FE-QA"|"lam-ro", "swp": 3, "gio": 8, ...}]}
  --ngoai-le  {"viec": [{"issue": "#82", "gio": 29.5, "khoang": [20, 40], ...}]}   (tuỳ chọn)
Đầu ra: --ra gio.json {"he_so", "gio": {số issue: giờ}, "ngoai_le": [...], "tong_leaf"} · --md bảng tóm tắt (tuỳ chọn)

Dùng: python3 quy-gio-theo-he-so.py --swp swp.json --mau mau.json [--ngoai-le nl.json] --ra gio.json [--md gio.md]
"""
import argparse, collections, json, sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def tron(v):
    return max(0.5, float((Decimal(str(v)) * 2).quantize(Decimal("1"), ROUND_HALF_UP) / 2))


def so(s):
    return str(s).lstrip("#")


def he_so(mau):
    t = collections.defaultdict(lambda: [0.0, 0])
    for m in mau:
        t[m["nhom"]][0] += m["gio"]
        t[m["nhom"]][1] += m["swp"]
    return {k: round(g / s, 2) for k, (g, s) in t.items() if s}


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("--swp", required=True)
    a.add_argument("--mau", required=True)
    a.add_argument("--ngoai-le")
    a.add_argument("--ra", required=True)
    a.add_argument("--md")
    g = a.parse_args()
    d = json.loads(Path(g.swp).read_text())
    hs = he_so(json.loads(Path(g.mau).read_text())["mau"])
    nl = {so(x["issue"]): x for x in json.loads(Path(g.ngoai_le).read_text())["viec"]} if g.ngoai_le else {}
    thieu = sorted({v["nhom"] for v in d["viec"]} - set(hs))
    if thieu:
        sys.exit(f"LỖI: nhóm chưa có issue mẫu nên chưa có hệ số: {thieu}")
    la_so = {v["so"] for v in d["viec"]}
    sai = sorted(set(nl) - la_so)
    if sai:
        sys.exit(f"LỖI: ngoại lệ không phải leaf task trong báo cáo: {sai[:10]}")
    gio, theo_hs = {}, {}
    for v in d["viec"]:
        theo_hs[v["so"]] = tron(v["swp"] * hs[v["nhom"]])
        gio[v["so"]] = float(nl[v["so"]]["gio"]) if v["so"] in nl else theo_hs[v["so"]]
    con = collections.defaultdict(list)
    for x in d["viec"] + d["cha"]:
        if x["cha_so"]:
            con[x["cha_so"]].append(x["so"])

    def cong(s):
        if s not in gio:
            gio[s] = sum(cong(c) for c in con[s])
        return gio[s]
    for x in d["cha"]:
        cong(x["so"])
    tong = sum(gio[v["so"]] for v in d["viec"])
    ra = {"he_so": hs, "gio": gio, "ngoai_le": sorted(nl, key=int), "tong_leaf": tong,
          "gio_theo_he_so_cua_ngoai_le": sum(theo_hs[s] for s in nl)}
    Path(g.ra).write_text(json.dumps(ra, ensure_ascii=False, indent=1) + "\n")
    if g.md:
        viet_md(g.md, d, hs, gio, theo_hs, nl, tong)
    print(f"hệ số {hs} · {len(d['viec'])} leaf task · ngoại lệ {len(nl)} · tổng giờ leaf {tong:g} → {g.ra}")


def viet_md(f, d, hs, gio, theo_hs, nl, tong):
    o = [f"# Giờ quy đổi từ SWP — {d['nguon']}", "", f"**Tổng giờ leaf task: {tong:g} giờ** ({len(d['viec'])} việc).", "",
         "| Nhóm | Hệ số (giờ/SWP) | Leaf task | SWP | Giờ |", "|---|---|---|---|---|"]
    for k in sorted(hs):
        v = [x for x in d["viec"] if x["nhom"] == k]
        o.append(f"| {k} | {hs[k]:g} | {len(v)} | {sum(x['swp'] for x in v)} | {sum(gio[x['so']] for x in v):g} |")
    if nl:
        o += ["", "Ngoại lệ ước trực tiếp:", "", "| Issue | Giờ quy từ SWP | Giờ ước trực tiếp | Khoảng |", "|---|---|---|---|"]
        o += [f"| #{s} | {theo_hs[s]:g} | {gio[s]:g} | {'–'.join(f'{k:g}' for k in nl[s].get('khoang', []))} |"
              for s in sorted(nl, key=int)]
    Path(f).write_text("\n".join(o) + "\n")


if __name__ == "__main__":
    main()
