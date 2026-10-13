#!/usr/bin/env python3
"""Ghi một trường số (SWP, giờ ước lượng…) lên GitHub Project v2 cho từng issue, rồi đọc lại đối chiếu.

- Mặc định chạy khô: chỉ đọc và in số ô cần ghi. Thêm --ghi để ghi thật.
- Đọc Project bằng một truy vấn GraphQL gọn (số issue + giá trị trường số; ~1 điểm hạn mức mỗi 100 item).
  `gh project item-list` kéo cả thân issue, tốn hàng trăm điểm mỗi lần và có thể làm cạn hạn mức 5.000 điểm/giờ.
- Chỉ ghi ô lệch; gộp 25 ô vào một mutation (ghi từng ô mất ~3 giây/ô). Chạy lại an toàn.
- Sau khi ghi, đọc lại toàn bộ: còn lệch thì exit 1.
Token do `gh` giữ; script không đọc hay in token. Cần scope `project` (`gh auth refresh -s project`).

Đầu vào --gia-tri: JSON có khoá --khoa (mặc định "gio") là {số issue: giá trị}, ví dụ đầu ra của
quy-gio-theo-he-so.py (khoá "gio") hoặc trich-swp-tu-bao-cao.py (khoá "swp").

Dùng: python3 ghi-truong-so-project.py --owner <login> --project <số> --truong "Giờ ước lượng" --gia-tri gio.json [--khoa gio] [--ghi]
"""
import argparse, json, subprocess, sys, time
from pathlib import Path

LO = 25
Q_PJ = """query($o: String!, $n: Int!) { %s(login: $o) { projectV2(number: $n) { id
  fields(first: 50) { nodes { ... on ProjectV2Field { id name dataType } } } } } }"""
Q_ITEM = """query($id: ID!, $sau: String) { node(id: $id) { ... on ProjectV2 { items(first: 100, after: $sau) {
  pageInfo { hasNextPage endCursor } nodes { id content { ... on Issue { number } }
  fieldValues(first: 30) { nodes { ... on ProjectV2ItemFieldNumberValue { number field { ... on ProjectV2FieldCommon { name } } } } } } } } } }"""


def gh_graphql(q, **bien):
    a = ["gh", "api", "graphql", "-f", f"query={q}"]
    for k, v in bien.items():
        a += ["-F" if isinstance(v, int) else "-f", f"{k}={v}"]
    for lan in range(3):
        r = subprocess.run(a, capture_output=True, text=True)
        if r.returncode == 0:
            return json.loads(r.stdout)["data"]
        if "rate limit" in r.stderr.lower():
            sys.exit("LỖI: hết hạn mức GraphQL theo giờ — chờ tới lúc đặt lại (query { rateLimit { resetAt } })")
        time.sleep(2 * (lan + 1))
    sys.exit(f"LỖI gh api graphql: {r.stderr.strip()[:300]}")


def tim_project(owner, so):
    for loai in ("user", "organization"):
        r = subprocess.run(["gh", "api", "graphql", "-f", f"query={Q_PJ % loai}", "-f", f"o={owner}", "-F", f"n={so}"],
                           capture_output=True, text=True)
        if r.returncode == 0 and (json.loads(r.stdout).get("data") or {}).get(loai):
            return json.loads(r.stdout)["data"][loai]["projectV2"]
    sys.exit(f"LỖI: không đọc được Project {owner}/{so} (sai tên, sai số, hoặc token thiếu scope project)")


def doc_item(pj_id, truong):
    ra, sau = {}, None
    while True:
        bien = {"id": pj_id, **({"sau": sau} if sau else {})}
        t = gh_graphql(Q_ITEM, **bien)["node"]["items"]
        for x in t["nodes"]:
            if not (x.get("content") or {}).get("number"):
                continue
            gt = next((f["number"] for f in x["fieldValues"]["nodes"] if f and f.get("field", {}).get("name") == truong), None)
            ra[str(x["content"]["number"])] = (x["id"], gt)
        if not t["pageInfo"]["hasNextPage"]:
            return ra
        sau = t["pageInfo"]["endCursor"]


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    for k in ("--owner", "--project", "--truong", "--gia-tri"):
        a.add_argument(k, required=True)
    a.add_argument("--khoa", default="gio")
    a.add_argument("--ghi", action="store_true")
    g = a.parse_args()
    muon = {str(k).lstrip("#"): float(v) for k, v in json.loads(Path(g.gia_tri).read_text())[g.khoa].items()}
    pj = tim_project(g.owner, int(g.project))
    tr = next((f for f in pj["fields"]["nodes"] if f and f.get("name") == g.truong), None)
    if not tr or tr.get("dataType") != "NUMBER":
        sys.exit(f"LỖI: Project không có trường số tên '{g.truong}'")
    hien = doc_item(pj["id"], g.truong)
    thieu = sorted(set(muon) - set(hien), key=int)
    if thieu:
        sys.exit(f"LỖI: issue không có trên Project: {thieu[:10]}")
    can = [s for s in sorted(muon, key=int) if hien[s][1] != muon[s]]
    print(f"{len(muon)} giá trị · item Project {len(hien)} · ô cần ghi {len(can)}" + ("" if g.ghi else " (chạy khô)"))
    if not g.ghi:
        return
    for i in range(0, len(can), LO):
        phan = [f'o{j}: updateProjectV2ItemFieldValue(input: {{projectId: "{pj["id"]}", itemId: "{hien[s][0]}", '
                f'fieldId: "{tr["id"]}", value: {{number: {muon[s]:g}}}}}) {{ clientMutationId }}' for j, s in enumerate(can[i:i + LO])]
        gh_graphql("mutation {\n" + "\n".join(phan) + "\n}")
        print(f"  đã ghi {min(i + LO, len(can))}/{len(can)}")
        time.sleep(1)
    hien = doc_item(pj["id"], g.truong)
    lech = [s for s in muon if hien[s][1] != muon[s]]
    print(f"Đọc lại: lệch {len(lech)} ô")
    sys.exit(1 if lech else 0)


if __name__ == "__main__":
    main()
