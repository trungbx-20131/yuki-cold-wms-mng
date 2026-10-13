---
name: chia-task-tu-thiet-ke-chi-tiet
description: Chia bộ thiết kế chi tiết (screen spec, ADR, ERD, danh mục API) ra các epic, issue và sub-issue trên GitHub Project — lập khung chung trước (granularity, DoD theo loại việc, quy ước tiêu đề, luật phụ thuộc), chia theo nhóm epic cho nhiều agent làm song song, gộp và kiểm bằng máy, review đối chiếu hai chiều spec ↔ issue, rồi đẩy lên GitHub chạy lại không tạo trùng. Dùng khi cần break task từ detail design, dựng backlog cho GitHub Project, hoặc kiểm một backlog đã có (thiếu cha, vòng phụ thuộc, trùng tiêu đề, dồn tải một vai).
---

# Chia task từ thiết kế chi tiết lên GitHub Project

Quy trình đã dùng ở LAB-5 để chia bộ thiết kế chi tiết của một hệ thống WMS (41 màn hình và tài liệu nền tảng)
thành 26 epic · 144 issue · 173 sub-issue (268 leaf task), đẩy lên GitHub Project và giữ 0 lệch giữa file và
Project. **Leaf task** là issue hoặc sub-issue không có sub-issue con — nơi ghi điểm và giờ.

## Khi nào dùng

- Có bộ thiết kế chi tiết (spec màn hình, ADR, thiết kế dữ liệu, danh mục API) và cần backlog để ước lượng, xếp sprint.
- Có backlog JSON (của mình hoặc agent sinh) và cần kiểm cấu trúc trước khi review hay đẩy lên.

Không dùng để chấm điểm (dùng `tkm:sun-estimate`, rồi skill `quy-swp-ra-gio-va-ghi-project` để ra giờ) hay để
viết thiết kế chi tiết.

## Quy trình

1. **Lập danh mục spec**: mỗi màn hình (kèm mức A — mang luật nghiệp vụ riêng, mức B — không), mỗi tài liệu nền
   tảng, câu hỏi khách còn mở, chỗ hở (spec thiếu hoặc mâu thuẫn). Mỗi chỗ hở trích `file:dòng` và kiểm trích dẫn
   bằng script (`grep -n`), không tin trí nhớ.
2. **Lập khung chung TRƯỚC khi chia** ([references/khung-backlog-mau.md](references/khung-backlog-mau.md)):
   luật granularity, DoD theo loại việc, quy ước tiêu đề và trường JSON, bộ nhãn, danh sách epic, cách xử lý câu
   hỏi khách lặp ở nhiều màn hình, hướng phụ thuộc. Chốt khung rồi mới giao chia — sửa khung sau khi các nhóm đã
   chép là phải sửa lan nhiều chỗ.
3. **Chia theo nhóm epic** (vd nền tảng, nhập kho, xuất kho…): mỗi agent một nhóm, một dải mã riêng, ghi một file
   JSON. Prompt giao việc có: vai, khung, danh mục spec của nhóm, file được ghi, tiêu chí xong, dòng ngôn ngữ.
4. **Gộp và kiểm bằng máy** trước mọi review:
   `python3 scripts/gop-va-kiem-backlog.py nhom-*.json -o backlog.json --md tom-tat.md`
   Lỗi (exit 1): trùng mã, sai tầng cha–con, phụ thuộc không có hoặc vòng, trùng tiêu đề, thiếu trường bắt buộc.
   Cảnh báo: DoD quá dài (nghi việc quá to), một vai nhận quá 1,5 lần trung vị số leaf task (cân tải ngay lúc chia).
5. **Review đối chiếu hai chiều** bằng agent độc lập, mỗi agent một nhóm: (a) mọi issue có nguồn trong spec hoặc
   dòng tiền đề; (b) mọi phần spec có issue hoặc có lý do chưa thành issue; (c) **danh sách yêu cầu phi chức năng
   của RFP** (tải, khả năng truy cập, khôi phục, bảo mật, kiểm thử hệ thống) đều có issue. Tối đa hai lượt, phát
   hiện phải gắn tiêu chí, đặt cổng dừng trước.
6. **Đẩy lên GitHub** (mặc định chạy khô; `--ghi` để ghi thật):
   `python3 scripts/day-backlog-len-github.py --backlog backlog.json --repo <owner/name> --project <số> [--ghi]`
   Chạy lại không tạo trùng (dò theo mã ở đầu tiêu đề), sửa tại chỗ khi lệch, nối sub-issue bằng GraphQL, chỉ đặt
   Status = Todo cho item mới hoặc chưa có Status. Thử trước trên repo và Project nháp.
7. **Viết task-breakdown**: nguyên tắc chia (granularity, DoD, cách dùng ba tầng), bảng spec → issue kèm phần
   chưa thành issue và lý do, việc chịu ràng buộc đặc thù, chỗ hở và cách xử lý.

## Ràng buộc

- File gộp chỉ sinh bằng script; sai thì sửa file của nhóm rồi gộp lại.
- Mỗi endpoint, hàm dùng chung có đúng một issue làm chủ; issue khác chỉ ghi phụ thuộc.
- Mã nội bộ (mã quyết định chưa công bố…) thay trong backlog, theo từng issue, trước khi đẩy lên repo public.
- Trước khi trình phương án cho người quyết, đối chiếu từng phương án với RFP; phương án trái RFP không được làm
  khuyến nghị.

## Tài liệu

- [references/khung-backlog-mau.md](references/khung-backlog-mau.md): khung mẫu — granularity, DoD theo loại việc,
  trường JSON, nhãn, phụ thuộc, câu hỏi khách.
- [references/bai-hoc-lab5.md](references/bai-hoc-lab5.md): số liệu kiểm chứng và bài học từ LAB-5.
