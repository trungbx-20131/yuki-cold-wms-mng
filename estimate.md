# Ước lượng — Yuki Cold WMS

Báo cáo chấm SWP (HTML): [bao-cao-swp/sun-estimate-yuki-cold-wms-mng-20261012-1631.html](bao-cao-swp/sun-estimate-yuki-cold-wms-mng-20261012-1631.html)

Backlog có 250 việc lá được chấm; epic và issue cha lấy tổng SWP của việc con. Tổng sau khi kiểm issue mẫu: **1064 SWP** (skill chấm ban đầu 1076 SWP).

## 1. Issue mẫu được kiểm

Skill chọn 5 issue mẫu theo quy tắc cố định (nhỏ nhất, trung vị, lớn nhất, lệch xa trung vị, độ tin cậy thấp nhất). Mỗi issue được đối chiếu với định nghĩa xong (DoD) và spec nguồn, rồi chốt mức khó và điểm. Scope là độ rộng công việc (1, 2, 3, 5, 8, 13), Complexity là độ khó bên trong (0, 1, 2, 3, 5, 8); SWP tra từ bảng cố định Scope × Complexity.

| Issue | Vì sao được chọn | Skill chấm: Scope × Complexity → SWP | Bạn chốt | Lý do |
|---|---|---|---|---|
| #44 I-034 — Dựng hàm chặn người đề xuất tự duyệt bản ghi của chính mình | issue nhỏ nhất | 1 × 1 → 1 | 1 × 1 → 1 | Giữ 1: DoD chỉ có một phép so người lập với người duyệt và một mã lỗi; việc gắn hàm vào từng luồng duyệt nằm ở issue của luồng đó. |
| #234 I-302.2 — Dựng giao diện màn lịch trình tài xế và phiên bản tuyến | mức trung vị | 3 × 1 → 4 | 3 × 1 → 4 | Giữ 4: một màn nhiều biến thể nhưng chỉ hiển thị kết quả API trả về; phần kiểm giờ lái thuộc issue riêng trong epic giờ lái. |
| #160 I-012.1 — Tạo migration sửa bảng prototype miền xuất kho và lịch sử giao | issue lớn nhất | 8 × 2 → 12 | 8 × 1 → 10 | Hạ 12 → 10: tám bảng cùng một miền là một đợt migration có kiểm soát, chưa tới mức nhiều hệ thống con; phần khó thật là chạy trên dữ liệu đang có và phải lùi được. Áp cho các issue migration cùng nhóm. |
| #108 I-326 — Dựng hàm phát hành tuyến: khoá tài xế, kiểm lại năm nhóm và ghi sổ giờ | lệch xa trung vị | 5 × 3 → 10 | 5 × 3 → 10 | Giữ 10: khoá dòng tài xế để hai tuyến phát hành song song không ghi đè sổ giờ, kiểm lại năm nhóm và ghi sổ trong một giao dịch; phần tính từng nhóm gọi hàm của issue khác. |
| #105 I-323 — Áp giới hạn thời gian ràng buộc, làm thêm giờ và nghỉ giữa ca khi kiểm tuyến | độ tin cậy thấp nhất | 3 × 3 → 6 | 3 × 3 → 6 | Giữ 6: năm phép so có biên và cộng dồn theo kỳ trong một hàm luật; độ tin cậy trung bình vì mốc giờ làm chuẩn còn chờ khách trả lời (Q16) — chỗ chờ này không làm tăng điểm. |

Điều chỉnh ở issue mẫu được áp cho 6 issue cùng nhóm (cùng loại việc, cùng kiểu phạm vi và độ khó), mỗi issue hạ đúng số bậc như issue mẫu:

| Issue | Skill chấm | Sau điều chỉnh |
|---|---|---|
| #33 I-013 — Tạo migration miền tuyến giao, tài xế và xe | 8 | 6 |
| #34 I-014 — Tạo migration miền chất lượng và truy xuất | 6 | 5 |
| #35 I-015 — Tạo migration cấu hình có phiên bản và vòng đời dữ liệu chủ | 8 | 6 |
| #156 I-010.1 — Tạo migration sửa bảng prototype miền nhập kho và tồn kho | 8 | 6 |
| #158 I-011.1 — Tạo migration sửa bảng prototype miền nhiệt độ và hồ sơ HACCP | 8 | 6 |
| #162 I-016.1 — Tạo migration bảng người dùng, audit và hàng đợi thông báo | 5 | 4 |

Khi chốt một điểm, skill tự quy điểm về ô Scope × Complexity gần đánh giá ban đầu nhất (ít bậc dịch nhất); vì vậy điểm 10 của issue mẫu migration được ghi là độ khó hạ một bậc.
