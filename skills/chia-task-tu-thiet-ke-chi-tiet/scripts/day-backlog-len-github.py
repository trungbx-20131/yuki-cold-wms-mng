#!/usr/bin/env python3
"""Đẩy backlog JSON lên GitHub: nhãn, issue, quan hệ sub-issue, thêm vào Project v2, Status = Todo.

- Mặc định chạy khô (chỉ đọc, in việc sẽ làm). Thêm --ghi để ghi thật.
- Chạy lại không tạo trùng: dò issue theo mã ở đầu tiêu đề ([E-21], [I-123], [I-123.1]) rồi dùng lại; issue đã có
  chỉ sửa tại chỗ khi tiêu đề, thân hoặc nhãn lệch backlog.
- Status chỉ đặt Todo khi item mới hoặc chưa có Status — không ghi đè trạng thái sprint đã cập nhật.
- Thân issue dựng nguyên văn từ backlog (mục tiêu, spec nguồn, DoD, ràng buộc, phụ thuộc). Mã nội bộ (vd mã quyết định
  chưa công bố) phải được thay trong backlog TRƯỚC khi đẩy, theo từng issue — repo public không được lộ cách gọi nội bộ.
Token do `gh` giữ; cần scope `repo`, `project`. Script không đọc hay in token.

Dùng: python3 day-backlog-len-github.py --backlog backlog.json --repo <owner/name> --project <số>
          [--owner-project <login>] [--nghi 1.0] [--ghi]
"""
import argparse, json, re, subprocess, sys, time
from pathlib import Path

MA_RE = re.compile(r"^\[((?:E|I)-\d+(?:\.\d+)?)\]")
TANG = {"epic": 0, "issue": 1, "sub-issue": 2}
ds = lambda v: v if isinstance(v, list) else ([v] if v else [])  # noqa: E731
chuan = lambda s: (s or "").replace("\r\n", "\n").strip()  # noqa: E731


def gh(*args, nhap=None):
    r = subprocess.run(["gh", *args], input=nhap, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"LỖI gh {' '.join(args[:2])}: {r.stderr.strip()[:300]}")
    return r.stdout


def gql(q, **bien):
    a = ["api", "graphql", "-f", f"query={q}"]
    for k, v in bien.items():
        if v is not None:
            a += ["-F" if isinstance(v, int) else "-f", f"{k}={v}"]
    return json.loads(gh(*a))["data"]


def nhan_cua(x):
    n = ds(x.get("nhan"))
    return n + ["epic"] if x["loai"] == "epic" and "epic" not in n else n


def than(x):
    sn = ds(x.get("spec_nguon"))
    p = ["## Mục tiêu", x.get("muc_tieu") or "(chưa ghi)", "", "## Spec nguồn"] + ([f"- {s}" for s in sn] or ["- (chưa ghi)"])
    p += ["", "## Định nghĩa xong (DoD)"] + [f"- [ ] {d}" for d in ds(x.get("dod"))]
    p += ["", "## Ràng buộc"] + ([f"- {r}" for r in ds(x.get("rang_buoc"))] or ["- Không có"])
    if x.get("phu_thuoc"):
        p += ["", "## Phụ thuộc"] + [f"- {m}" for m in x["phu_thuoc"]]
    return "\n".join(p) + "\n"


def doc_issue(repo):
    o, n = repo.split("/")
    co, sau, trung = {}, None, []
    while True:
        r = gql("""query($o:String!,$n:String!,$s:String){repository(owner:$o,name:$n){
          issues(first:100,after:$s,orderBy:{field:CREATED_AT,direction:ASC}){pageInfo{hasNextPage endCursor}
          nodes{id number url title body parent{id} labels(first:50){nodes{name}}}}}}""", o=o, n=n, s=sau)
        t = r["repository"]["issues"]
        for x in t["nodes"]:
            m = MA_RE.match(x["title"])
            if m:
                (trung.append(f"{m[1]} #{x['number']}") if m[1] in co else co.__setitem__(m[1], x))
        if not t["pageInfo"]["hasNextPage"]:
            return co, trung
        sau = t["pageInfo"]["endCursor"]


def doc_project(owner, so):
    for loai in ("user", "organization"):
        muc, sau, pid = {}, None, None
        while True:
            r = subprocess.run(["gh", "api", "graphql", "-f", "query=query($l:String!,$p:Int!,$s:String){%s(login:$l){projectV2(number:$p){id "
                                "items(first:100,after:$s){pageInfo{hasNextPage endCursor} nodes{id content{... on Issue{id}} "
                                "fieldValueByName(name:\"Status\"){... on ProjectV2ItemFieldSingleSelectValue{name}}}}}}}" % loai,
                                "-f", f"l={owner}", "-F", f"p={so}"] + (["-f", f"s={sau}"] if sau else []), capture_output=True, text=True)
            d = (json.loads(r.stdout).get("data") or {}).get(loai) if r.returncode == 0 else None
            if not d:
                break
            pj = d["projectV2"]
            pid = pj["id"]
            for x in pj["items"]["nodes"]:
                if x["content"]:
                    muc[x["content"]["id"]] = (x["id"], (x["fieldValueByName"] or {}).get("name"))
            if not pj["items"]["pageInfo"]["hasNextPage"]:
                return pid, muc
            sau = pj["items"]["pageInfo"]["endCursor"]
    sys.exit(f"LỖI: không đọc được Project {owner}/{so} (sai tên/số hoặc token thiếu scope project)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--backlog", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--project", type=int, required=True)
    ap.add_argument("--owner-project")
    ap.add_argument("--nghi", type=float, default=1.0)
    ap.add_argument("--ghi", action="store_true")
    a = ap.parse_args()
    bl = json.loads(Path(a.backlog).read_text())
    chu = a.owner_project or a.repo.split("/")[0]
    print(f"{'CHẠY THẬT' if a.ghi else 'CHẠY KHÔ'} · repo {a.repo} · Project {chu}/{a.project} · {len(bl)} work item")
    dem = dict.fromkeys(["nhãn mới", "issue mới", "dùng lại", "sửa tại chỗ", "nối cha", "thêm Project", "đặt Todo"], 0)

    def ghi(loai, mo_ta, *args, nhap=None):
        dem[loai] += 1
        print(("  " if a.ghi else "  [khô] ") + mo_ta)
        return gh(*args, nhap=nhap) if a.ghi else None
    co, trung = doc_issue(a.repo)
    if trung:
        print("CẢNH BÁO mã trùng trên GitHub (dùng issue tạo trước):", ", ".join(trung))
    nhan_co = set(gh("label", "list", "-R", a.repo, "--limit", "500", "--json", "name", "-q", ".[].name").split("\n"))
    for n in sorted({n for x in bl for n in nhan_cua(x)} - nhan_co):
        ghi("nhãn mới", f"tạo nhãn {n}", "label", "create", n, "-R", a.repo, "--color", "ededed")
    viec = sorted(bl, key=lambda x: (TANG[x["loai"]], [int(s) for s in re.findall(r"\d+", x["ma"])]))
    for x in viec:
        td, b, cu = f"[{x['ma']}] {x['tieu_de']}", than(x), co.get(x["ma"])
        if cu is None:
            nh = sum([["--label", n] for n in nhan_cua(x)], [])
            url = ghi("issue mới", f"tạo issue {td}", "issue", "create", "-R", a.repo, "--title", td, "--body-file", "-", *nh, nhap=b)
            co[x["ma"]] = {"id": None, "number": "?", "parent": None}
            if url:
                r = gql("query($u:URI!){resource(url:$u){... on Issue{id number}}}", u=url.strip())["resource"]
                co[x["ma"]].update(id=r["id"], number=r["number"])
                time.sleep(a.nghi)
            continue
        dem["dùng lại"] += 1
        thieu = [n for n in nhan_cua(x) if n not in {l["name"] for l in cu["labels"]["nodes"]}]
        if cu["title"] != td or chuan(cu["body"]) != chuan(b) or thieu:
            ghi("sửa tại chỗ", f"sửa #{cu['number']} {td}", "issue", "edit", str(cu["number"]), "-R", a.repo, "--title", td,
                "--body-file", "-", *sum([["--add-label", n] for n in thieu], []), nhap=b)
    for x in viec:
        con, cha = co[x["ma"]], co.get(x.get("cha"))
        if not cha or (con["id"] and cha["id"] and (con.get("parent") or {}).get("id") == cha["id"]):
            continue
        q = f'mutation{{addSubIssue(input:{{issueId:"{cha["id"]}",subIssueId:"{con["id"]}",replaceParent:true}}){{issue{{number}}}}}}'
        ghi("nối cha", f"nối {x['cha']} (#{cha['number']}) → {x['ma']} (#{con['number']})", "api", "graphql", "-f", f"query={q}")
    pid, muc = doc_project(chu, a.project)
    st = next(f for f in json.loads(gh("project", "field-list", str(a.project), "--owner", chu, "--format", "json"))["fields"]
              if f["name"] == "Status")
    todo = next(o["id"] for o in st["options"] if o["name"] == "Todo")
    for x in viec:
        i = co[x["ma"]]
        item, trang_thai = muc.get(i["id"], (None, None)) if i["id"] else (None, None)
        if item is None:
            out = ghi("thêm Project", f"thêm {x['ma']} (#{i['number']}) vào Project", "project", "item-add", str(a.project),
                      "--owner", chu, "--url", f"https://github.com/{a.repo}/issues/{i['number']}", "--format", "json")
            item = out and json.loads(out)["id"]
        if trang_thai is None:
            ghi("đặt Todo", f"Status = Todo cho {x['ma']}", "project", "item-edit", "--project-id", pid, "--id", str(item),
                "--field-id", st["id"], "--single-select-option-id", todo)
    print("Kết quả:", " · ".join(f"{k} {v}" for k, v in dem.items()))
    if a.ghi:
        sau, _ = doc_issue(a.repo)
        print(f"Đọc lại: {sum(1 for m in sau if m in {x['ma'] for x in bl})}/{len(bl)} mã backlog có issue")


if __name__ == "__main__":
    main()
