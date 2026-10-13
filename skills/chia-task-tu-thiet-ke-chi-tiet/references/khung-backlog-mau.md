# Khung backlog mẫu — chốt trước khi giao chia task

Điền phần trong `<…>` theo dự án. Các luật dưới là bản đã dùng ở LAB-5, viết lại dạng chung.

## 1. Granularity — chia tới đâu thì dừng

| # | Luật | Kiểm bằng |
|---|---|---|
| G1 | Một issue hoặc sub-issue là một việc giao cho **đúng một vai**, xong trong **tối đa 3 ngày công** của vai đó | Trường vai có một giá trị; giờ kiểm lại khi ước lượng |
| G2 | Màn hình **mức A** (mang luật nghiệp vụ riêng): một issue cha "Dựng màn …" và các sub-issue theo lớp — `.1` API và hàm DB · `.2` giao diện · `.3` luật nghiệp vụ · `.4` kiểm thử; lớp nào không có thì bỏ | Màn mức A có đủ lớp cần thiết |
| G3 | Màn hình **mức B** (không mang luật riêng): một issue nếu gọn trong một vai; cần cả endpoint mới và giao diện thì đúng hai sub-issue `.1` API · `.2` giao diện | — |
| G4 | Phần dùng chung (migration, phân quyền, audit, khung giao diện, job theo lịch, tích hợp ngoài, hàm luật nhiều màn gọi) chỉ có issue ở các epic nền tảng | Không màn nào dựng lại phần dùng chung |
| G5 | Ràng buộc đặc thù của đề (vd giới hạn giờ lái xe tải từ 4/2024): mỗi điểm liên quan là một issue riêng trong epic riêng, có nhãn riêng | Đối chiếu bảng truy vết với issue của epic đó |
| G6 | Câu hỏi khách lặp ở nhiều màn: **một** issue làm rõ gốc; issue màn chỉ mang thẻ câu hỏi | Mỗi câu hỏi lặp có đúng một issue gốc |
| G7 | Câu hỏi khách chỉ ở một màn: không tạo issue riêng; issue màn mang nhãn chờ khách và một dòng DoD nêu giả định đang dùng | — |

**Dừng tách** khi cả ba đúng: việc tối đa 3 ngày công cho một vai; có DoD kiểm được độc lập; tách thêm chỉ ra
phần không demo hay kiểm riêng được. Không tạo issue cho đọc tài liệu, họp, review mã.

## 2. DoD theo loại việc (chép nguyên vào thân issue, cộng mục riêng ở đầu)

| Loại (nhãn) | DoD |
|---|---|
| Dữ liệu (`du-lieu`) | Migration chạy được trên DB trống và trên bản sao dữ liệu; migration lùi đã chạy thử; khoá, ràng buộc, tập trạng thái khớp thiết kế dữ liệu đích; test DB xanh trong CI; không có dữ liệu thật |
| API, hàm (`api`) | Đúng đặc tả endpoint (tham số, khung phản hồi, mã lỗi theo danh mục); kiểm quyền theo ma trận, 401/403 trả trước mã nghiệp vụ; thao tác ghi nhiều bước trong một giao dịch, audit cùng giao dịch; gửi lại an toàn |
| Giao diện (`giao-dien`) | Đủ biến thể wireframe; câu lỗi hiện nguyên văn câu API trả; thao tác ẩn hoặc khoá theo vai trò; dùng thành phần giao diện dùng chung; ảnh chụp từng biến thể khi đóng |
| Luật nghiệp vụ (`luat`) | Mỗi luật có test case chặn và test case cho qua; giá trị biên có test case riêng; tham số đọc từ cấu hình có phiên bản; thiếu tham số thì xử lý đúng như spec của luật quy định, không cho qua im lặng |
| Job theo lịch (`job`) | Lịch đăng ký đúng nhịp spec; mỗi lần chạy có nhật ký; chạy lại không sinh trùng; lần chạy lỗi sinh cảnh báo vận hành |
| Hạ tầng (`ha-tang`) | Cấu hình lặp lại được; khoá bí mật không nằm trong mã, log; có hướng dẫn vận hành ngắn; đã chạy thử trên môi trường kiểm thử |
| Kiểm thử (`kiem-thu`) | Test case có mã, bước, dữ liệu, kết quả mong đợi bám spec; chạy tự động trong CI (hoặc ghi lý do kiểm tay); có test case nối màn theo luồng dữ liệu; lỗi tìm thấy ghi thành issue riêng |
| Làm rõ với khách (`lam-ro`) | Câu hỏi gửi bằng văn bản kèm phương án và giả định đang dùng; đáp án ghi kèm ngày nhận; issue liên quan được rà và cập nhật; tài liệu tiền đề cập nhật nếu giả định đổi |
| Epic (`epic`) | Mọi issue con đã đóng; không còn issue làm rõ đang mở chặn epic; phần việc của epic chạy được trên môi trường kiểm thử |

## 3. Tiêu đề

`[MÃ] Động từ + đối tượng`, ví dụ `[I-101.1] Dựng API và hàm DB cho màn danh sách lịch hẹn nhập`. Động từ trong một
bộ cố định (Dựng, Tạo migration, Áp, Viết bộ kiểm thử, Làm rõ, Lập…). Mã: `E-nn` epic, `I-nnn` issue,
`I-nnn.m` sub-issue; mỗi nhóm epic một dải mã riêng để các agent không đụng nhau.

## 4. Trường JSON của mỗi work item

| Trường | Bắt buộc | Ghi chú |
|---|---|---|
| `ma` | có | Duy nhất toàn backlog |
| `loai` | có | `epic` · `issue` · `sub-issue` |
| `cha` | issue, sub-issue | issue → epic; sub-issue → issue |
| `tieu_de` | có | Không kèm mã (script thêm `[MÃ]` khi đẩy) |
| `muc_tieu` | có | Một câu: xong thì người dùng hoặc hệ thống có được gì |
| `spec_nguon` | có | Danh sách chuỗi `file §mục` hoặc `file:dòng`; dòng tiền đề nếu khác thiết kế |
| `dod` | issue, sub-issue | Danh sách dòng; mục riêng ở đầu, rồi bộ DoD của loại |
| `nhan` | nên có | Theo bộ nhãn cố định của khung |
| `vai_goi_y` | leaf task | Một vai; cân tải ngay lúc chia |
| `phu_thuoc` | tuỳ | Chỉ việc **phải xong trước để bắt đầu**; issue có giả định tạm không phụ thuộc issue làm rõ |
| `rang_buoc` | tuỳ | Vd `cho-khach:<mã câu hỏi>`, `<ràng buộc đặc thù>` |

## 5. Hướng phụ thuộc

- Nền tảng trước màn hình; trong một màn: API trước giao diện, luật trước kiểm thử.
- Nhóm nền tảng không bao giờ phụ thuộc nhóm màn hình.
- Gọi trực tiếp endpoint, hàm hoặc hộp thoại của nhóm khác thì ghi phụ thuộc ngay ở work item đó; chỉ đọc dữ liệu
  nhóm khác ghi thì đặt phụ thuộc ở sub-issue kiểm thử.
- Kiểm thử tải, kiểm thử hệ thống chạy trên bản dựng đầy đủ: xếp cuối.
