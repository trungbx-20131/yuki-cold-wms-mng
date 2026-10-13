---
name: quy-swp-ra-gio-va-ghi-project
description: Quy đổi SWP đã chốt (từ báo cáo HTML của tkm:sun-estimate) sang giờ ước lượng bằng hệ số theo nhóm việc lấy từ issue mẫu được ước giờ trực tiếp không xem SWP, xử lý ngoại lệ ước trực tiếp, rồi ghi SWP và giờ lên trường số của GitHub Project v2 có đọc lại đối chiếu. Dùng sau bước chấm SWP, khi cần trả lời "SWP này là bao nhiêu giờ", điền trường giờ/điểm trên GitHub Project, hoặc kiểm một nhóm epic có bị ước thấp không.
---

# Quy đổi SWP ra giờ và ghi lên GitHub Project

Skill nối tiếp `tkm:sun-estimate`. Skill chấm cho ra SWP (Standard Work Point = Scope × Complexity tra bảng), nhưng
không quy ra giờ và không ghi lên Project (bản V1 chỉ đọc). Skill này làm hai việc đó, theo cách đã dùng và kiểm
chứng ở LAB-5 (backlog 343 work item, 268 leaf task, 1165 SWP, 4.024 giờ).

Thuật ngữ: **leaf task** là issue hoặc sub-issue không có sub-issue con — nơi ghi SWP và giờ; epic và issue cha lấy
tổng của con. **Nhóm việc**: `BE` (API, DB, migration, hạ tầng, tích hợp), `FE-QA` (giao diện, kiểm thử),
`lam-ro` (làm rõ với khách).

## Khi nào dùng

- Đã có báo cáo HTML bản cuối của `tkm:sun-estimate`, người làm đã duyệt issue mẫu (SWP đã chốt).
- Cần giờ ước lượng cho từng leaf task và tổng theo epic, giải thích được cách quy đổi.
- Cần ghi SWP và giờ lên trường số của GitHub Project, chạy lại an toàn.

Không dùng để chấm SWP (dùng `tkm:sun-estimate`) hay ước lượng cả dự án từ RFP/spec (dùng `tkm:estimate`).

## Quy trình

1. **Trích SWP đã chốt** từ payload nhúng của báo cáo (không đọc phần hiển thị):
   `python3 scripts/trich-swp-tu-bao-cao.py <bao-cao.html> -o swp.json`
2. **Ước giờ trực tiếp cho issue mẫu, không cho người ước xem SWP.** Chọn 8–12 issue trải đều các mức SWP và
   đủ ba nhóm việc. Người (hoặc agent) ước giờ từng bước việc: đọc spec, làm, kiểm thử theo DoD, sửa sau review;
   ghi giờ kỳ vọng, khoảng thấp–cao và lý do theo bước. Mẫu prompt và định dạng `mau.json`:
   [references/phuong-phap-va-bai-hoc.md](references/phuong-phap-va-bai-hoc.md) mục 2.
3. **Quy đổi**: `python3 scripts/quy-gio-theo-he-so.py --swp swp.json --mau mau.json --ra gio.json --md gio.md`
   - Hệ số nhóm = tổng giờ mẫu ÷ tổng SWP mẫu; giờ leaf = SWP × hệ số, làm tròn 0,5; cha = tổng con.
   - Đọc tỷ lệ hệ số giữa các nhóm: lệch xa (LAB-5: FE-QA 4,86 so với BE 2,69 giờ/SWP) nghĩa là skill chấm
     đánh giá thấp nhóm đó; một hệ số chung sẽ làm thiếu giờ của nhóm này.
4. **Kiểm nhóm có rủi ro ước thấp bằng ước lại trực tiếp**, không chỉ "theo dõi": chọn các epic chênh lớn nhất so
   với estimate trước (vd estimate báo giá), ước lại trực tiếp toàn bộ leaf task của chúng (cùng cách bước 2, không
   xem SWP và giờ cũ). Nếu người quyết định dùng giờ ước lại, đưa vào `--ngoai-le nl.json` rồi chạy lại bước 3.
5. **Ghi lên GitHub Project** (mặc định chạy khô; thêm `--ghi` để ghi thật):
   ```
   python3 scripts/ghi-truong-so-project.py --owner <login> --project <số> --truong SWP --gia-tri swp.json --khoa swp
   python3 scripts/ghi-truong-so-project.py --owner <login> --project <số> --truong "Giờ ước lượng" --gia-tri gio.json
   ```
   Chỉ ghi SWP **sau khi người duyệt issue mẫu**, không ghi số thô của skill. Script đọc lại toàn bộ; còn lệch
   thì exit 1.
6. **Ghi vào estimate**: cách quy đổi đã chọn và vì sao, bảng hệ số theo nhóm, bảng issue mẫu, bảng ngoại lệ
   (giờ quy từ SWP · giờ ước trực tiếp · khoảng · độ tin cậy).

## Ràng buộc

- Người ước giờ mẫu không được thấy SWP hay giờ cũ — nếu thấy, hệ số chỉ phản chiếu lại điểm của skill.
- Mọi số giờ sinh bằng script từ `swp.json` + `mau.json` (+ `nl.json`); không sửa tay file đầu ra.
- Không ghi đè trường khác trên Project; mỗi lần chạy chỉ ghi một trường số.
- Token do `gh` giữ; cần scope `project`. Script không in token.

## Tài liệu

- [references/phuong-phap-va-bai-hoc.md](references/phuong-phap-va-bai-hoc.md): vì sao chọn hệ số theo nhóm, mẫu
  prompt ước giờ, định dạng file, số liệu kiểm chứng ở LAB-5 và các bẫy đã gặp (hạn mức GraphQL, ghi từng ô quá
  chậm, rủi ro ước thấp nêu quá mức).
