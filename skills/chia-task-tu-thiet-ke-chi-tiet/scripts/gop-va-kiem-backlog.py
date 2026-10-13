#!/usr/bin/env python3
"""Gộp backlog JSON của các nhóm epic (mỗi agent một file) thành một file và kiểm bằng máy trước khi review.

Mỗi phần tử: {"ma", "loai": epic|issue|sub-issue, "cha", "tieu_de", "muc_tieu", "spec_nguon": [], "dod": [],
"nhan": [], "vai_goi_y", "phu_thuoc": [], "rang_buoc": []} — xem references/khung-backlog-mau.md mục 4.

Kiểm (lỗi → exit 1, file gộp vẫn ghi để xem):
  mã không trùng (kể cả giữa hai file) · loai hợp lệ · cha tồn tại và đúng tầng (issue → epic, sub-issue → issue)
  · phụ thuộc trỏ mã có thật, không tự trỏ, không vòng · tiêu đề không trùng · trường bắt buộc không rỗng
  (tieu_de, muc_tieu, spec_nguon; dod với issue/sub-issue) · leaf task có vai_goi_y.
Cảnh báo (không chặn): leaf task có quá --dod-toi-da dòng DoD (nghi quá to, nên tách) · một vai nhận quá
--tai-he-so (mặc định 1,5) lần trung vị số leaf task của các vai — cân tải ngay lúc chia, đừng đợi lúc xếp sprint.

Dùng: python3 gop-va-kiem-backlog.py <nhom-1.json> [<nhom-2.json> ...] -o backlog.json [--md tom-tat.md]
"""
import argparse, collections, json, sys
from pathlib import Path

TANG = {"epic": None, "issue": "epic", "sub-issue": "issue"}
BAT_BUOC = ("tieu_de", "muc_tieu", "spec_nguon")


def doc(files):
    ra, nguon, loi = [], {}, []
    for f in files:
        for x in json.loads(Path(f).read_text()):
            if x.get("ma") in nguon:
                loi.append(f"{x['ma']}: trùng mã ({nguon[x['ma']]} và {f})")
                continue
            nguon[x.get("ma")] = f
            ra.append(x)
    return ra, loi


def vong(pt):
    """Tìm một vòng phụ thuộc (DFS ba màu); trả danh sách mã của vòng hoặc []."""
    mau, cha = {}, {}

    def di(u):
        mau[u] = 1
        for v in pt.get(u, []):
            if mau.get(v) == 1:
                c, w = [v], u
                while w != v:
                    c.append(w)
                    w = cha[w]
                return c[::-1]
            if not mau.get(v):
                cha[v] = u
                r = di(v)
                if r:
                    return r
        mau[u] = 2
        return []
    sys.setrecursionlimit(10000)
    for u in pt:
        if not mau.get(u):
            r = di(u)
            if r:
                return r
    return []


def kiem(bl, dod_toi_da, tai_he_so):
    loi, canh = [], []
    by = {x["ma"]: x for x in bl}
    con = {x.get("cha") for x in bl if x.get("cha")}
    for x in bl:
        m, lo = x["ma"], x.get("loai")
        if lo not in TANG:
            loi.append(f"{m}: loai '{lo}' không hợp lệ")
            continue
        if TANG[lo] and by.get(x.get("cha"), {}).get("loai") != TANG[lo]:
            loi.append(f"{m}: cha '{x.get('cha')}' không có hoặc không phải {TANG[lo]}")
        thieu = [k for k in BAT_BUOC + (() if lo == "epic" else ("dod",)) if not x.get(k)]
        if thieu:
            loi.append(f"{m}: thiếu {', '.join(thieu)}")
        for p in x.get("phu_thuoc", []):
            if p not in by or p == m:
                loi.append(f"{m}: phụ thuộc '{p}' không có hoặc tự trỏ")
        if m not in con and lo != "epic":
            if not x.get("vai_goi_y"):
                loi.append(f"{m}: leaf task thiếu vai_goi_y")
            if len(x.get("dod", [])) > dod_toi_da:
                canh.append(f"{m}: {len(x['dod'])} dòng DoD — nghi quá to, cân nhắc tách sub-issue")
    td = collections.Counter(x.get("tieu_de") for x in bl)
    loi += [f"tiêu đề trùng: '{t}'" for t, n in td.items() if n > 1]
    c = vong({x["ma"]: [p for p in x.get("phu_thuoc", []) if p in by] for x in bl})
    if c:
        loi.append("vòng phụ thuộc: " + " → ".join(c + c[:1]))
    la = [x for x in bl if x["ma"] not in con and x.get("loai") != "epic"]
    tai = collections.Counter(x.get("vai_goi_y") for x in la)
    gv = sorted(tai.values())
    tv = gv[len(gv) // 2] if gv else 0
    canh += [f"vai {v} nhận {n} leaf task, gấp {n / tv:.1f} lần trung vị {tv} của các vai — cân tải" for v, n in
             tai.most_common() if tv and n > tai_he_so * tv]
    return loi, canh, la, tai


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("files", nargs="+")
    a.add_argument("-o", "--ra", required=True)
    a.add_argument("--md")
    a.add_argument("--dod-toi-da", type=int, default=12)
    a.add_argument("--tai-he-so", type=float, default=1.5)
    g = a.parse_args()
    bl, loi = doc(g.files)
    l2, canh, la, tai = kiem(bl, g.dod_toi_da, g.tai_he_so)
    loi += l2
    Path(g.ra).write_text(json.dumps(bl, ensure_ascii=False, indent=1) + "\n")
    dem = collections.Counter(x.get("loai") for x in bl)
    tom = (f"{dem['epic']} epic · {dem['issue']} issue · {dem['sub-issue']} sub-issue · {len(la)} leaf task · "
           f"lỗi {len(loi)} · cảnh báo {len(canh)}")
    if g.md:
        o = ["# Tóm tắt backlog gộp", "", tom, "", "| Vai gợi ý | Leaf task |", "|---|---|"]
        o += [f"| {v} | {n} |" for v, n in tai.most_common()]
        o += ["", "## Lỗi", ""] + [f"- {e}" for e in loi] + ["", "## Cảnh báo", ""] + [f"- {e}" for e in canh]
        Path(g.md).write_text("\n".join(o) + "\n")
    print(tom)
    for e in loi[:30]:
        print("LỖI", e)
    for e in canh[:15]:
        print("CẢNH BÁO", e)
    sys.exit(1 if loi else 0)


if __name__ == "__main__":
    main()
