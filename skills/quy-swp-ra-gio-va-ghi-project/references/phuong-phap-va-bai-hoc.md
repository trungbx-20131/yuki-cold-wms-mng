# Phương pháp và bài học — quy đổi SWP ra giờ, ghi lên GitHub Project

## 1. Vì sao hệ số theo nhóm, lấy từ ước trực tiếp không xem SWP

SWP đo độ rộng × độ khó của một việc, không phải giờ. Có hai cách ra giờ: ước trực tiếp từng việc (chính xác nhưng
tốn công với hàng trăm việc), hoặc quy ước đổi SWP sang giờ (nhất quán, kiểm lại được bằng phép nhân). Skill dùng
cách thứ hai, nhưng lấy hệ số từ một mẫu được ước trực tiếp, nên hệ số dựa trên công thật chứ không phải con số
tự đặt.

Người ước mẫu không được xem SWP. Nếu thấy điểm, giờ ước sẽ bị điểm kéo theo và hệ số chỉ phản chiếu lại cách
skill chấm. Ở LAB-5, mẫu ước mù cho thấy skill chấm giao diện và kiểm thử thấp hơn công thật so với backend:

| Nhóm | Hệ số (giờ/SWP) | Leaf task | SWP |
|---|---|---|---|
| BE (API, DB, migration, hạ tầng, tích hợp) | 2,69 | 147 | 724 |
| FE-QA (giao diện, kiểm thử) | 4,86 | 91 | 390 |
| lam-ro (làm rõ với khách) | 2,5 | 30 | 51 |

Một hệ số chung cho mọi việc sẽ làm thiếu khoảng 30 % giờ frontend và kiểm thử.

## 2. Mẫu prompt ước giờ trực tiếp (cho agent hoặc người)

```
Ước giờ làm thật cho các issue sau. Mục đích là đo công, nên ước độc lập; không cố khớp con số nào.
Đầu vào: <file danh sách issue: mục tiêu, spec nguồn, DoD — KHÔNG kèm SWP, giờ cũ, estimate cũ>
Được đọc: spec mà issue trỏ tới. Không được đọc: báo cáo chấm SWP, file giờ, estimate cũ.
Giả định đội: <công nghệ, mức kinh nghiệm>. Giờ là công thuần của một người cho đúng việc đó: đọc spec, làm,
kiểm thử theo DoD, sửa sau review; không gồm dự phòng, chờ khách, họp, quản lý dự án.
Mỗi issue ghi: issue, nhom (BE | FE-QA | lam-ro), gio (làm tròn 0,5), khoang [thấp, cao],
ly_do (từng bước kèm giờ), do_tin_cay (cao | vua | thap) và lý do nếu thấp.
```

Định dạng file:

```json
{"mau": [{"issue": "#43", "nhom": "BE", "swp": 3, "gio": 8, "khoang": [6, 11], "ly_do": "Đọc spec 1h; ..."}]}
```

Ngoại lệ (`--ngoai-le`), ví dụ đầu ra của lượt ước lại một nhóm epic:

```json
{"viec": [{"issue": "#82", "gio": 29.5, "khoang": [20, 40], "do_tin_cay": "vua", "ly_do": "..."}]}
```

`swp` của mẫu lấy từ `swp.json` sau khi ước xong (ghép theo số issue), không đưa cho người ước.

## 3. Kiểm chứng ở LAB-5

| Kiểm | Kết quả |
|---|---|
| `trich-swp-tu-bao-cao.py` trên báo cáo bản cuối | 268 leaf task, 75 cha, tổng 1165 SWP — đúng tổng của báo cáo |
| `quy-gio-theo-he-so.py` với 10 mẫu và 30 ngoại lệ | 4.024 giờ; 343/343 work item khớp từng giá trị với bảng giờ đã chốt của bài |
| `ghi-truong-so-project.py` chạy khô trên Project thật | SWP và giờ: 0 ô cần ghi trên 343 item |
| Ghi thật một ô rồi ghi trả giá trị cũ | đọc lại lệch 0 cả hai lần |

Các script này được đóng gói ở bước cuối của LAB-5 từ những script đã dùng khi làm bài (lúc đó viết riêng cho
repo bài, gắn đường dẫn cố định); bản trong skill nhận tham số dòng lệnh để dùng lại cho dự án khác.

## 4. Bẫy đã gặp

- **Hạn mức GraphQL theo giờ.** `gh project item-list --limit 1000` kéo cả thân issue; vài lần đọc toàn Project
  đã làm cạn 5.000 điểm/giờ. Endpoint REST `rate_limit` còn báo sai số điểm còn lại; xem đúng bằng
  `query { rateLimit { remaining resetAt } }`. Script đọc bằng truy vấn gọn chỉ lấy số issue và trường số.
- **Ghi từng ô quá chậm**: `gh project item-edit` mất ~3 giây mỗi ô (729 ô ≈ 35 phút). Gộp 25 ô vào một mutation
  GraphQL bằng bí danh: 505 ô trong khoảng 6 phút.
- **Không ghi số thô của skill.** Chỉ ghi SWP sau khi người duyệt issue mẫu; ở LAB-5 một issue mẫu được hạ 12 → 10
  và quy tắc hiệu chỉnh lan sang 6 issue cùng nhóm.
- **Rủi ro ước thấp nêu bằng chênh lệch với estimate cũ dễ nói quá.** LAB-5 từng ghi "543 giờ có thể ước thấp" ở
  ba epic chỉ vì chênh với estimate báo giá; ước lại trực tiếp 30 leaf task cho 399 → 448,5 giờ (+12 %, khoảng
  328,5–622,5). Đo lại ngay (bước 4 của quy trình) rẻ hơn nhiều so với "theo dõi tới Sprint 3".
- **Kiểm năng lực bằng tổng giờ chia đội chưa đủ.** Tổng giờ ÷ năng lực đội ra "vừa", nhưng xếp từng việc theo
  vai và phụ thuộc thì có thể không vừa (LAB-5: frontend nghẽn, phải thêm một người). Sau khi có giờ, nên xếp thử
  sprint theo phụ thuộc trước khi chốt.
