# Chia task: epic, issue và sub-issue của backlog

Backlog chia từ bộ thiết kế chi tiết LAB-4 đã nộp, cộng các khác biệt khai ở [PREMISE.md](PREMISE.md). Mã `E-nn` (epic), `I-nnn` (issue), `I-nnn.m` (sub-issue) là mã trong backlog; số issue trên GitHub (`#n`) được điền khi backlog đẩy lên Project. Trỏ `PREMISE:<khoá>` là dòng có khoá đó trong PREMISE.md.

Số đếm (sinh bằng script từ file backlog): **25 epic · 128 issue · 155 sub-issue** — 283 phần việc, trong đó 240 phần việc lá (không có con) là nơi ghi điểm và giờ.

## 1. Nguyên tắc chia task

### 1.1 Độ hạt — chia tới đâu thì dừng

| # | Luật | Kiểm bằng |
|---|---|---|
| G1 | Một issue hoặc sub-issue là một phần việc giao cho **đúng một vai** và xong trong **tối đa 3 ngày công** (24 giờ làm việc) của vai đó | Trường người phụ trách giả định có một giá trị; điểm và giờ kiểm lại khi ước lượng |
| G2 | Màn **mức A** (màn mang luật nghiệp vụ riêng, theo phân loại phạm vi màn của gói thiết kế LAB-4): một issue cha "Dựng màn …" và ít nhất bốn sub-issue theo lớp — `.1` API và hàm DB · `.2` giao diện · `.3` luật nghiệp vụ · `.4` kiểm thử. Lớp nào quá 3 ngày công thì thêm sub-issue **cùng lớp** (`.5`, `.6`…), tách theo endpoint hoặc theo nhóm luật | Không có issue "làm màn X" chung chung cho màn mức A |
| G3 | Màn **mức B** (không mang luật riêng): **một issue** khi việc nằm gọn trong một vai; khi cần cả endpoint mới và giao diện thì **đúng hai sub-issue** `.1` API · `.2` giao diện. Kiểm thử nằm trong định nghĩa xong của từng sub-issue | Màn mức B có 0 hoặc 2 sub-issue, thêm nữa phải có lý do quá 3 ngày công |
| G4 | Phần dùng chung (migration 71 bảng, phân quyền, audit, khung giao diện, job theo lịch, tích hợp ngoài, hàm luật nhiều màn gọi) chỉ có issue ở nhóm nền tảng E-01…E-05. Issue màn ghi phụ thuộc tới issue nền tảng, không làm lại | Không có hai issue cùng làm một thành phần |
| G5 | Ràng buộc giờ lái 2024: mỗi điểm chạm là **một issue riêng** trong epic E-32, nhãn `rang-buoc-gio-lai-2024`; không làm sub-issue của màn lập tuyến hay xuất kho (phần 3) | Đối chiếu bảng truy vết với issue của E-32 |
| G6 | Câu hỏi khách lặp ở nhiều màn: **một** issue làm rõ gốc (nhãn `lam-ro`, `cho-khach`); issue màn chỉ mang thẻ câu hỏi (mục 1.4) | Mỗi câu hỏi lặp có đúng một issue gốc |
| G7 | Câu hỏi khách chỉ ở một màn: **không** tạo issue riêng — issue của màn mang nhãn `cho-khach`, thẻ câu hỏi và một dòng định nghĩa xong nêu giả định đang dùng. Ngoại lệ: chỗ hở mà tiền đề chọn xử lý bằng issue làm rõ (I-075, I-297, I-503, I-504, I-522, I-541), vì câu trả lời đổi thiết kế chứ không chỉ đổi một màn | Mọi issue có thẻ câu hỏi đều có dòng giả định |

**Khi nào dừng tách.** Dừng khi cả ba đúng: phần việc tối đa 3 ngày công cho một vai; có định nghĩa xong kiểm được độc lập; tách thêm chỉ cho ra phần không demo hay kiểm riêng được. Không tạo issue cho đọc tài liệu, họp, review mã, viết tài liệu nội bộ (các việc này nằm trong định nghĩa xong), không tạo issue dự phòng, không tạo issue cho màn ngoài 41 màn.

**Phụ thuộc giữa issue.** Trường phụ thuộc chỉ ghi việc **phải xong trước để bắt đầu**: nền tảng trước màn; trong một màn, API trước giao diện, luật trước kiểm thử. Ba luật đi kèm:

1. Issue đã có giả định tạm **không** phụ thuộc issue làm rõ — chỉ mang nhãn `cho-khach` và thẻ câu hỏi, để việc không bị khoá chờ cuộc họp với khách. Chỉ issue không làm được trước khi có đáp án mới ghi phụ thuộc vào issue làm rõ.
2. Giữa hai nhóm epic: phần tử gọi trực tiếp endpoint, hàm hoặc hộp thoại của nhóm kia thì ghi phụ thuộc ngay ở phần tử đó. Khi chỉ đọc dữ liệu do nhóm kia ghi (bảng đã có ở nền tảng), phụ thuộc đặt ở sub-issue kiểm thử của màn (mức A) hoặc sub-issue API (mức B), để có ca kiểm nối màn. Đọc cấu hình qua hàm đọc phiên bản dùng chung và dữ liệu khởi tạo thì không cần màn cấu hình xong trước.
3. Nhóm nền tảng không bao giờ phụ thuộc nhóm màn; mỗi endpoint có đúng một issue làm chủ, issue khác cần endpoint đó chỉ ghi phụ thuộc.

### 1.2 Định nghĩa xong theo loại

Mỗi issue mang nguyên bộ định nghĩa xong của loại mình (dạng checklist trong thân issue), cộng các mục riêng ở đầu danh sách.

| Loại (nhãn) | Định nghĩa xong |
|---|---|
| Dữ liệu (`du-lieu`) | Migration chạy được trên DB trống và trên bản sao dữ liệu, migration lùi đã chạy thử; khoá, ràng buộc, tập trạng thái, tên bảng và cột khớp thiết kế dữ liệu đích; test hàm Postgres (pgTAP) xanh trong CI; không có dữ liệu thật |
| API, hàm (`api`) | Đúng đặc tả endpoint (tham số, khung phản hồi, mã lỗi theo danh mục); bọc kiểm quyền theo ma trận quyền, 401/403 trả trước mã nghiệp vụ; thao tác ghi nhiều bước trong một hàm Postgres, một giao dịch, audit cùng giao dịch; gửi lại an toàn; mỗi mã lỗi có ca test |
| Giao diện (`giao-dien`) | Đủ mọi biến thể wireframe đúng itemNo; câu lỗi hiện nguyên văn câu API trả; thao tác ẩn hoặc khoá theo vai trò; dùng thành phần giao diện dùng chung; ảnh chụp từng biến thể đính kèm khi đóng |
| Luật nghiệp vụ (`luat`) | Mỗi luật có ca chặn và ca cho qua; giá trị biên có ca test riêng; tham số đọc từ cấu hình có phiên bản; khi thiếu tham số làm đúng hành vi spec của luật quy định — nhóm giờ lái và nhóm HACCP chặn bằng `RULE_PARAMETER_MISSING`, luật khác đi nhánh mặc định an toàn mà spec quy định, không cho qua im lặng; luật chạy trong cùng giao dịch với thao tác ghi |
| Job theo lịch (`job`) | Lịch đăng ký trong DB đúng nhịp spec, không mở route HTTP; mỗi lần chạy có nhật ký; chạy lại không sinh trùng; lần chạy lỗi sinh cảnh báo vận hành; có ca test biên thời gian |
| Hạ tầng (`ha-tang`) | Cấu hình lặp lại được; khoá bí mật không nằm trong mã, log hay bản xem trước; có hướng dẫn vận hành ngắn; đã chạy thử trên môi trường kiểm thử |
| Kiểm thử (`kiem-thu`) | Ca kiểm có mã, bước, dữ liệu, kết quả mong đợi bám spec; chạy tự động trong CI (hoặc ghi lý do kiểm tay); có ca kiểm nối màn theo luồng dữ liệu; lỗi tìm thấy ghi thành issue riêng |
| Làm rõ với khách (`lam-ro`) | Câu hỏi gửi bằng văn bản kèm phương án và giả định đang dùng; đáp án ghi lại kèm ngày nhận; issue liên quan được rà và cập nhật; PREMISE.md cập nhật nếu giả định đổi; đóng khi đáp án đã phản ánh vào backlog hoặc khách xác nhận giữ giả định |
| Epic (`epic`) | Mọi issue con đã đóng; không còn issue làm rõ đang mở chặn epic; phần việc của epic chạy được trên môi trường kiểm thử |

Mục riêng bắt buộc theo ngữ cảnh: issue có giả định chờ khách có dòng "Theo giả định tạm …, chờ khách trả lời <mã câu hỏi>"; issue cha của màn mức A có "bốn sub-issue theo lớp đã đóng" và "màn chạy hết luồng của spec trên môi trường kiểm thử"; issue giờ lái có dòng nêu nhóm giới hạn mà issue kiểm.

### 1.3 Dùng ba tầng epic, issue, sub-issue trên GitHub Project

- **Ba tầng, không có tầng thứ tư.** Epic là một issue GitHub mang nhãn `epic`; issue là sub-issue của epic; sub-issue là sub-issue của issue. Mọi epic, issue, sub-issue đều nằm trên Project.
- **Người phụ trách (giả định)** lấy từ vai gợi ý của từng phần việc (BE-n, FE-n, QA-n, Designer, Infra, BrSE — đội giả định, không phải người thật).
- **Điểm (point) và giờ** ghi ở phần việc lá: issue đã có sub-issue thì điểm và giờ nằm ở sub-issue, issue cha không chấm thêm; epic không chấm. Điểm của issue cha bằng tổng điểm con.
- **Iteration** xếp theo phụ thuộc: nền tảng trước màn, API trước giao diện, luật trước kiểm thử; issue làm rõ đi sớm để đáp án về kịp trước khi màn liên quan đóng.
- **Nhãn cố định (12 nhãn):** loại — `du-lieu`, `api`, `giao-dien`, `luat`, `job`, `ha-tang`, `kiem-thu`, `lam-ro`; đặc tính — `muc-a`, `rang-buoc-gio-lai-2024`, `cho-khach`, `epic`. Mỗi phần việc mang đúng một nhãn loại.
- **Thẻ câu hỏi:** phần việc có giả định chờ khách ghi mã câu hỏi trong thân issue (vd `cho-khach:KH-L4-30`) để lọc ra mọi phần việc chịu ảnh hưởng khi khách trả lời.

### 1.4 Câu hỏi khách lặp ở nhiều màn → issue gốc

Cột cuối liệt kê phần việc mang thẻ câu hỏi (sinh bằng script; sub-issue được gom về issue cha khi cha cùng mang thẻ).

| Câu hỏi | Nội dung | Issue gốc | Phần việc mang thẻ |
|---|---|---|---|
| KH-L4-01 | Nghĩa của quy tắc 1/3 (tập quán thương mại về hạn giao) | I-291 | I-202, I-501.5 |
| KH-L4-02 | Khoá so của 日付逆転禁止 (cấm giao lô có hạn sớm hơn lô khách đã nhận): theo khách hay theo điểm nhận | I-292 | I-202, I-203, I-205, I-206, I-209, I-540.6 |
| KH-L4-03 | Điểm chặn 消費期限 (hạn sử dụng an toàn): lúc nạp xe, lúc ghi nhận giao hàng hay cả hai | I-293 | I-205, I-206 |
| KH-L4-09 | Vai và bước xử lý sai lệch nhiệt, hồ sơ HACCP, hàng trả về | I-491 | I-054.4, I-102, I-106, I-108, I-202, I-208, I-210, I-401, I-402, I-404, I-405 |
| KH-L4-16 | Cách hiểu điều kiện ước tính di chuyển vượt 24 giờ | I-393 | I-327, I-328 |
| KH-L4-18 | Ai được xem đợt kiểm kê | I-191 | I-109, I-110 |
| KH-L4-20 | Ai được xem phiếu soạn hàng | I-294 | I-202, I-204 |
| KH-L4-22 | Chủ dữ liệu chủ và quyền xem bản ghi | I-591 | I-511.1, I-512.1 |
| KH-L4-30 | Giờ ca, nhịp hồ sơ vệ sinh và nhật ký ra vào | I-492 | I-052, I-055.2, I-402, I-405, I-501.6 |
| KH-L4-32 | Vòng đời tuyến, xe nạp hàng và xe của tuyến | I-391 | I-205, I-206, I-301.3, I-301.5, I-302.1, I-320.1, I-329 |
| KH-L4-35 | Ngày bắt đầu và ngày cuối hiệu lực của phiên bản cấu hình, dữ liệu chủ | I-505 | I-325, I-501.3, I-510.1, I-511.3 |
| KH-L4-36 | Đơn vị sức chứa vị trí, lô nằm một vị trí | I-192 | I-104, I-106, I-202, I-511.3 |
| KH-L4-40 | Hạn nạp CSV của logger nhiệt, số đo nạp muộn | I-493 | I-055.2, I-401, I-402, I-405 |
| KH-L4-44 | Giao khác thứ tự, hàng bị chặn tại điểm nhận | I-295 | I-205, I-206 |
| KH-L4-45 | Gốc so của phép cấm đảo ngày hạn: lần nhận gần nhất hay hạn lớn nhất | I-296 | I-202, I-203, I-205, I-206, I-209 |
| KH-L4-48 | Mức đo nhiệt hàng khi nạp xe | I-193 | I-103, I-205 |
| KH-L4-49 | Vị trí đặt lô cách ly khi dải nhiệt chưa khai ô cách ly | I-194 | I-102, I-104, I-105, I-106 |
| Q4 | Đặc tả file đơn ERP và cách chuyển file | I-074 | I-070, I-071, I-201, I-521.1 |
| Q5 | Chính sách MFA, khoá tài khoản | I-045 | I-035, I-530, I-531.1 |
| Q9 | Leo thang và người nhận thư nội bộ | I-494 | I-102, I-106, I-108, I-202, I-208, I-402, I-403, I-404, I-408 |
| Q12 | Mẫu tám báo cáo chưa dựng, quyền xem báo cáo (kèm câu phụ về cách ngắt chuỗi lái liên tục) | I-495 | I-303.2, I-324, I-333, I-409 |
| Q16 | Giá trị ba khoá giờ lái chưa có số | I-392 | I-018, I-321.2, I-323, I-324, I-333 |
| Q24 | Giá trị ngưỡng ban đầu (kiểm nhiệt, duyệt hai cấp kiểm kê) | I-195 | I-103, I-110, I-205, I-504 |

Một mã nữa đi riêng: I-297 hỏi về huỷ đơn xuất (câu hỏi chỉ ở một màn, nhưng tiền đề chọn xử lý bằng issue làm rõ — `PREMISE:QĐ-E`).

### 1.5 Số lượng và lý do vượt khoảng dự kiến

Số lượng không phải thước đo; khoảng dự kiến lập lúc chốt nguyên tắc chỉ để phát hiện chia quá thô hoặc quá vụn. Cột "Sub-issue thêm" đếm sub-issue cùng lớp sinh ra vì một lớp quá 3 ngày công (G2) hoặc vượt hai sub-issue của màn mức B (G3).

| Nhóm epic | Issue | Dự kiến | Sub-issue | Dự kiến | Sub-issue thêm |
|---|---|---|---|---|---|
| Nền tảng (E-01…E-05) | 39 | 35–45 | 7 | 4–8 | 3 |
| Nhập kho, tồn kho (E-11…E-15) | 15 | 15–18 | 32 | 26–32 | 4 |
| Xuất kho (E-21…E-24) | 17 | 16–20 | 23 | 18–22 | 3 |
| Lập tuyến và giờ lái (E-31…E-32) | 22 | 10–16 | 16 | 10–14 | 2 |
| Nhiệt độ, truy xuất, báo cáo (E-41…E-44) | 15 | 15–18 | 38 | 32–38 | 4 |
| Quản trị (E-51…E-55) | 20 | 19–23 | 39 | 26–32 | 7 |

Lý do vượt:

- **Lập tuyến và giờ lái (E-31, E-32):** số issue vượt vì G5 bắt mỗi điểm chạm giờ lái là một issue riêng thay vì một sub-issue luật của màn; thêm ba issue làm rõ (I-391…I-393). Sub-issue vượt vì màn lập tuyến có thêm sub-issue API sửa tuyến đã phát hành và sub-issue mở rộng danh mục xe, khung giờ giao. Đây là chủ đích: việc chịu ràng buộc riêng của đề phải nhìn thấy và theo dõi được tách bạch.
- **Nhiệt độ, truy xuất, báo cáo (E-41…E-44):** sub-issue chạm cận trên vì tám trên chín màn ở mức A (bốn lớp mỗi màn); ba màn tách lớp API thành hai sub-issue đọc và ghi, một màn tách thêm lớp giao diện.
- **Quản trị (E-51…E-55):** sub-issue vượt vì ba màn mức A rất lớn có lớp quá 3 ngày công — màn cấu hình luật (tám endpoint phiên bản), màn chuyển dữ liệu (sáu loại dữ liệu nạp), màn lưu giữ và purge (xoá hồ sơ qua hơn 20 bảng) — cộng sáu sub-issue của ba loại dữ liệu chủ mới (tài xế, xe, khung giờ giao — `PREMISE:QĐ-B`).
- **Nhập kho, tồn kho (E-11…E-15):** sub-issue chạm cận trên vì bốn màn mức A có thêm một sub-issue API (endpoint đọc và ghi độc lập, gộp lại quá 3 ngày công).
- **Xuất kho (E-21…E-24):** sub-issue vượt một đơn vị vì màn phân bổ có thêm sub-issue API chạy phân bổ và sub-issue luật cấm đảo ngày hạn, màn ghi nhận giao hàng có thêm sub-issue API ghi giao hàng.

## 2. Spec → issue

Bảng phủ đủ 41 màn và mọi tài liệu nền tảng của gói thiết kế LAB-4 (ADR, sơ đồ luồng, thiết kế dữ liệu, danh mục API, quyết định trong PREMISE.md của LAB-4…). Cột Issue ghi `I-102 (.1–.5)` khi issue có sub-issue. Một issue có thể phục vụ nhiều màn.

### 2.1 Màn hình

| Spec | Epic | Issue/sub-issue | Phần spec chưa thành issue — lý do |
|---|---|---|---|
| SCR-REC-01 Danh sách lịch hẹn nhập (mức B) | E-11 | I-101 (.1–.2) | Nạp lịch hẹn tự động từ ERP hoặc thông báo giao hàng điện tử: ngoài phạm vi theo giả định (`PREMISE:NH-28`), lịch hẹn nhập tay |
| SCR-REC-02 Kiểm hàng nhập từng dòng (mức A) | E-11 | I-102 (.1–.5) | Máy quét mã vạch: không có việc riêng, máy quét gõ vào cùng ô nhập (kiểm trong DoD giao diện) |
| SCR-REC-03 Xử lý accept/reject/hold (mức A) | E-12 | I-104 (.1–.5) | Màn quản trị mã lý do phân tách: mã lý do là bảng hằng, không có màn. Thao tác từ chối của người duyệt: spec không có, chờ khách |
| SCR-INV-01 Tồn kho theo vị trí & dải nhiệt (mức B) | E-13 | I-105, I-107.1 | — |
| SCR-INV-02 Cất kho (gợi ý vị trí) (mức B) | E-13 | I-106 (.1–.2) | Cất hoặc chuyển một phần lô: chưa hỗ trợ (mỗi lô một vị trí), hỏi khách ở I-192 |
| SCR-INV-03 Cách ly / giải phóng / tiêu huỷ (mức A) | E-14 | I-108 (.1–.4) | Nhánh chờ hồ sơ sai lệch đóng rồi mới giải phóng, tiêu huỷ: không làm theo giả định tạm, hỏi khách ở I-491, I-494 |
| SCR-INV-04 Kiểm kê mù (mức B) | E-15 | I-109 (.1–.2) | — |
| SCR-INV-05 Điều chỉnh chênh lệch (mức A) | E-15 | I-110 (.1–.5) | — |
| SCR-INV-06 Tra cứu tồn đa tiêu chí (mức B) | E-13 | I-107 (.1–.2) | Tra theo mã lô của nhà cung cấp: thuộc màn tra ngược nguồn gốc (I-406) |
| SCR-INV-07 Kiểm nhiệt & tạo sai lệch khi nhập/xuất (mức A) | E-11 | I-103 (.1–.5) | Ngưỡng nhiệt riêng từng SKU: spec chọn không có, ngưỡng đọc từ bảng dải nhiệt |
| SCR-OUT-01 Danh sách đơn xuất (mức B) | E-05, E-21 | I-074, I-201 (.1–.2) | Nhận file đơn ERP tự động: làm ở nhóm tích hợp nền tảng (I-070, I-071, `PREMISE:QĐ-A`); màn chỉ đọc lô nhập |
| SCR-OUT-02 Phân bổ + lý do loại trừ (mức A) | E-21, E-22, E-24 | I-202 (.1–.6), I-203, I-291, I-292, I-294, I-296, I-297 | Huỷ đơn, lối thoát cho đơn không còn lô: ngoài phạm vi (`PREMISE:QĐ-E`), hỏi khách ở I-297. Khai cửa sổ hạn giao, loại hạn: thuộc màn cấu hình luật (E-51) |
| SCR-OUT-03 Danh sách phiếu soạn hàng (mức B) | E-22 | I-204 (.1–.2), I-294 | — |
| SCR-OUT-04 Kiểm & nạp xe (mức A) | E-21, E-22 | I-203, I-205 (.1–.4), I-292, I-293, I-296 | Hộp thoại đo nhiệt thuộc E-11 (I-103.2, I-103.5); hồ sơ sai lệch khi nạp thuộc E-42. Đối chiếu xe nạp với xe của tuyến: không làm theo giả định (`PREMISE:NH-07`), hỏi khách ở I-391 |
| SCR-OUT-05 Ghi nhận POD (mức A) | E-21, E-22, E-23, E-24 | I-203, I-206 (.1–.5), I-292, I-293, I-295 | Giao không thành (đổi lô, trả hàng về kho): ngoài phạm vi (`PREMISE:QĐ-E`), hỏi khách ở I-295. Màn cấu hình bộ chứng cứ POD: không có màn, nạp bằng dữ liệu khởi tạo (I-018) |
| SCR-OUT-06 Khiếu nại / trả hàng (mức B) | E-24 | I-208 (.1–.2), I-210, I-295 | Đưa hàng trả vào tồn: ngoài phạm vi (`PREMISE:QĐ-E`), hỏi khách ở I-491. Đổi trạng thái lô: thuộc màn cách ly (I-108) |
| SCR-MST-04 Tra cứu lịch sử giao hàng (mức B) | E-21, E-24 | I-203, I-209 (.1–.2), I-211, I-292, I-296 | Ghi dòng tóm tắt gốc so khi purge: thuộc hàm purge (I-540.6) |
| SCR-SCH-01 Lập tuyến giao hàng (mức A) | E-31, E-32 | I-301 (.1–.6), I-327, I-332, I-333, I-391, I-392, I-393 | Phần giờ lái của màn là issue riêng ở E-32 (I-327, I-332, I-333). Xem trước kết quả kiểm khi sửa tuyến đã phát hành: thiết kế không có, hạn chế ghi trong DoD |
| SCR-SCH-02 Kiểm năm nhóm ràng buộc thời gian làm việc tài xế (mức A) | E-31, E-32 | I-320 (.1–.4), I-323, I-324, I-325, I-327, I-331, I-391, I-392, I-393 | Lớp luật của màn là các issue giờ lái riêng (I-322…I-331), không làm sub-issue luật |
| SCR-SCH-03 Lịch trình tài xế (mức B) | E-31, E-32 | I-302 (.1–.2), I-328, I-329, I-331, I-391, I-393 | — |
| SCR-SCH-04 Ghi sự cố ngoài dự kiến (mức B) | E-31 | I-303 (.1–.2) | Báo cáo chậm trễ theo nguyên nhân sự cố: thuộc nhóm báo cáo chưa dựng (`PREMISE:NH-16`) |
| SCR-SCH-05 Sổ giờ tích lũy của tài xế (mức A) | E-32 | I-321 (.1–.4), I-330, I-392 | Nạp số dư đầu kỳ sổ giờ: nạp bằng dữ liệu khởi tạo theo giả định tạm (I-018), hỏi khách ở I-522 |
| SCR-TEMP-01 Nạp CSV datalogger (mức A) | E-41 | I-401 (.1–.4), I-493 | Job đối soát, hàm gom đợt, hàm cách ly lô: thuộc nhóm nền tảng (I-053, I-054, I-055) |
| SCR-TEMP-02 Bảng theo dõi nhiệt & hàng đợi alarm (mức A) | E-04, E-41, E-42 | I-054.4, I-402 (.1–.4), I-403, I-491, I-494 | Chỉ số mục tiêu về tỷ lệ xem xét trễ: đo ngoài hệ thống. Mức nghiêm trọng của alarm: khách chưa định nghĩa, hỏi ở I-491 |
| SCR-TEMP-03 Hồ sơ sai lệch (deviation/HACCP) (mức A) | E-42 | I-404 (.1–.5), I-491 | Tạo hồ sơ từ alarm bằng endpoint riêng: thiết kế đích không có màn gọi, hồ sơ tự mở cùng alarm |
| SCR-TEMP-04 Bảng đầy đủ hồ sơ HACCP (mức A) | E-41, E-42 | I-405 (.1–.6), I-492, I-493 | Báo cáo hồ sơ HACCP còn thiếu: thuộc nhóm báo cáo chưa dựng (`PREMISE:NH-16`) |
| SCR-TRC-01 Tra ngược nguồn gốc (mức A) | E-43 | I-406 (.1–.4) | — |
| SCR-TRC-02 Bảng case thu hồi + đối soát (mức A) | E-43 | I-407 (.1–.5) | — |
| SCR-TRC-03 Soạn & duyệt thông báo thu hồi (mức A) | E-41, E-43 | I-408 (.1–.4), I-494 | Gửi lại thư thông báo lỗi: thuộc màn theo dõi tích hợp (I-521.1) |
| SCR-RPT-01 Trung tâm báo cáo (mức B) | E-44 | I-409 (.1–.2), I-495 | Tám báo cáo chưa có mẫu: chưa có việc để giao, giữ trong danh mục ở trạng thái chưa dựng; hỏi khách ở I-495 |
| SCR-RPT-02 Xuất bằng chứng audit (mức A) | E-44 | I-410 (.1–.4) | Lần xuất theo lịch lưu giữ: ngoài phạm vi theo giả định (`PREMISE:NH-15`) |
| SCR-EXP-01 Cấu hình luật hạn, cửa sổ hạn giao & ngưỡng nhiệt (mức A) | E-32, E-51 | I-392, I-501 (.1–.6), I-504, I-505 | Kiểm giờ lái khi phát hành tuyến: thuộc E-32. Lịch hai ca vệ sinh: hàm lịch ca dùng chung (I-052). Sửa hàm phân bổ theo quy tắc 1/3: thuộc I-202.3 |
| SCR-MST-01 Danh sách dữ liệu chủ (mức B) | E-51, E-52 | I-505, I-510 (.1–.2) | Danh mục đơn vị đóng gói đầy đủ: nạp bằng dữ liệu khởi tạo, chờ tệp SKU của khách |
| SCR-MST-02 Chi tiết & chỉnh sửa master (mức A) | E-51, E-52 | I-503, I-511 (.1–.4), I-513 (.1–.2), I-514 (.1–.2), I-515 (.1–.2), I-591 | Lối vào màn cho nhân viên kho: chỉ có quyền gọi API (`PREMISE:NH-23`) |
| SCR-MST-03 Hàng đợi duyệt master (mức A) | E-52 | I-512 (.1–.4), I-513 (.1–.2), I-514 (.1–.2), I-515 (.1–.2), I-591 | Duyệt sự kiện đảo lịch sử giao: thuộc màn lịch sử giao (I-211) |
| SCR-MIG-01 Bảng điều khiển migration (mức A) | E-53 | I-520 (.1–.6), I-522 | — |
| SCR-INT-01 Bảng theo dõi tích hợp ngoài (mức B) | E-03, E-53 | I-036, I-521 (.1–.2) | Hàng dịch vụ bản đồ: spec loại trừ có lý do. Theo dõi phiên định danh: thuộc khung ứng dụng (I-036, `PREMISE:NH-17`) |
| SCR-SEC-01 Đăng nhập (mức B) | E-03, E-54 | I-036, I-530 | Theo dõi phiên định danh: thuộc khung ứng dụng (I-036); đăng nhập OIDC và MFA ở I-035 |
| SCR-SEC-02 Quản lý người dùng & vai trò (mức B) | E-54 | I-531 (.1–.2) | — |
| SCR-SEC-03 Nhật ký audit (mức B) | E-54 | I-532 | Chế độ chỉ thêm của nhật ký audit: thuộc I-017 |
| SCR-SEC-04 Chính sách lưu giữ, legal hold, purge (mức A) | E-32, E-55 | I-335, I-540 (.1–.7), I-541 | Nhóm hồ sơ đào tạo không có bảng: chỉ khai thời hạn, hỏi khách ở I-541. Job đề xuất purge: I-056 |

### 2.2 Tài liệu nền tảng

| Spec | Epic | Issue/sub-issue | Phần spec chưa thành issue — lý do |
|---|---|---|---|
| adr/ADR-001-delivery-history-bat-bien.md | E-02 | I-017 | — |
| adr/ADR-002-nguong-va-gio-lai-la-cau-hinh.md | E-02, E-04 | I-015, I-018, I-051 | — |
| adr/ADR-003-ghi-nhieu-buoc-trong-ham-postgres.md | E-01, E-03 | I-002, I-032 | — |
| adr/ADR-004-phan-quyen-o-tang-api.md | E-01, E-03 | I-001, I-030, I-031, I-033, I-035 | — |
| architecture/luong-1-nhap-hang-kiem-nhiet-cach-ly.mmd | E-04 | I-053 | — |
| architecture/luong-2-phan-bo-cong-dau-6-buoc.mmd; architecture/luong-3-nap-xe-pod-ghi-lich-su-giao.mmd | E-21, E-22, E-23 | I-202.3, I-202.5, I-202.6, I-203, I-205.1, I-205.3, I-206.3, I-206.5 | Luồng phân bổ, nạp xe, ghi nhận giao hàng nằm gọn trong issue của màn xuất kho; không có issue riêng cho sơ đồ |
| architecture/luong-4-phat-hanh-tuyen-gio-lai-2024.mmd | E-32 | I-322, I-323, I-324, I-325, I-327, I-330, I-335 | Luồng phát hành tuyến theo giờ lái là epic E-32 (phần 3); sơ đồ còn mô tả bản dựng thử nên không dùng làm nguồn (phần 4, dòng sơ đồ luồng 4) |
| architecture/luong-5-csv-nhiet-alarm-sai-lech-haccp.mmd | E-04 | I-053, I-054 (.1–.4), I-055 (.1–.3) | — |
| architecture/luong-6-truy-xuat-3-lan-thu-hoi.mmd | E-43 | I-406 (.1–.4), I-407 (.1–.5), I-408 (.1–.4) | Truy xuất ba làn và thu hồi nằm gọn trong issue của màn truy xuất |
| database-diagram/erd-thiet-ke-dich-nguoi-dung-cau-hinh.mmd — 19 bảng | E-02, E-03 | I-015, I-016, I-035 | — |
| database-diagram/erd-thiet-ke-dich-xuat-tuyen.mmd — 22 bảng | E-02 | I-012, I-013 | — |
| database-diagram/erd-thiet-ke-dich-bao-cao.mmd — 1 bảng | E-02 | I-016 | — |
| database-diagram/erd-thiet-ke-dich-chat-luong-truy-xuat.mmd — 8 bảng | E-02 | I-014 | — |
| database-diagram/erd-thiet-ke-dich-nhiet.mmd — 11 bảng | E-02 | I-011 | — |
| database-diagram/erd-thiet-ke-dich-nhap-ton.mmd — 11 bảng | E-02 | I-010 | — |
| _common/api-list.md §2 (EP-01…EP-49) | E-01, E-03 | I-003, I-036, I-037, I-040 | — |
| _common/api-list.md §3.1 | E-11, E-12, E-13, E-14, E-15 | I-101.1, I-102.1, I-102.5, I-103.1, I-103.5, I-104.1, I-104.5, I-106.1, I-107.1, I-108.1, I-109.1, I-110.1, I-110.5 | Endpoint làm trong sub-issue API của từng màn nhập kho, tồn kho |
| _common/api-list.md §3.2 | E-21, E-22, E-23, E-24, E-31, E-32 | I-201.1, I-202.1, I-202.5, I-204.1, I-205.1, I-206.1, I-206.5, I-208.1, I-209.1, I-301.1, I-301.5, I-301.6, I-302.1, I-303.1, I-320.1, I-321.1, I-326, I-328, I-329, I-331 | Endpoint làm trong sub-issue API của từng màn xuất kho, lập tuyến |
| _common/api-list.md §3.3; _common/api-list.md §3.4; _common/api-list.md §3.6 | E-41, E-42, E-43, E-44 | I-401.1, I-402.1, I-404.1, I-404.5, I-405.1, I-405.5, I-406.1, I-407.1, I-407.5, I-408.1, I-409.1, I-410.1 | Endpoint làm trong sub-issue API của từng màn nhiệt độ, truy xuất, báo cáo |
| _common/api-list.md §3.5 | E-51, E-52, E-53, E-54, E-55 | I-501.1, I-501.5, I-502, I-510.1, I-511.1, I-512.1, I-513.1, I-514.1, I-515.1, I-520.1, I-520.5, I-520.6, I-521.1, I-531.1, I-540.1, I-540.5, I-540.6, I-540.7 | Endpoint làm trong sub-issue API của từng màn quản trị (bảng nền ở I-015, I-016) |
| _common/api-list.md §4 | E-04 | I-050, I-054 (.1–.4), I-055 (.1–.3), I-056 | — |
| _common/api-list.md §5 | E-03 | I-040 | — |
| PREMISE.md của LAB-4 — QĐ1, QĐ2, QĐ12, QĐ15 | E-11, E-12, E-13, E-14, E-21 | I-102 (.1–.5), I-104 (.1–.5), I-106 (.1–.2), I-108 (.1–.4), I-202.3 | Quyết định của màn nhập kho, tồn kho (QĐ1, QĐ2 chạm cả bước loại trừ của phân bổ): thành DoD của issue màn |
| PREMISE.md của LAB-4 — QĐ3 | E-23 | I-206 (.1–.5) | Ghi nhận giao hàng đổi trạng thái tuyến: thành DoD của issue POD; màn lập tuyến chỉ đọc |
| PREMISE.md của LAB-4 — QĐ4, QĐ5, QĐ8 | E-04 | I-053 | — |
| PREMISE.md của LAB-4 — QĐ6 | E-31, E-32 | I-301.3, I-326 | Chặn phát hành tuyến khi đơn chưa đủ phân bổ: thành DoD của hàm phát hành |
| PREMISE.md của LAB-4 — QĐ7, QĐ9, QĐ14 | E-21, E-22, E-31 | I-202 (.1–.6), I-205 (.1–.4), I-301.3, I-391 | Quyết định của màn phân bổ, nạp xe: thành DoD của issue màn |
| PREMISE.md của LAB-4 — QĐ10 | E-11, E-42 | I-103.1, I-103.5, I-404.1 | Hồ sơ sai lệch gắn lô từ dòng nhập lệch nhiệt: thành DoD của issue đo nhiệt và màn hồ sơ sai lệch |
| PREMISE.md của LAB-4 — QĐ11 | E-04 | I-055.1 | — |
| PREMISE.md của LAB-4 — QĐ13 | E-04 | I-054.1 | — |
| PREMISE.md của LAB-4 — QĐ16 | E-04 | I-052 | — |
| architecture/thanh-phan.mmd; architecture/kien-truc.md §1 | E-01, E-03 | I-001, I-030 | — |
| architecture/kien-truc.md §1.2 | E-03 | I-032 | — |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:143 | E-03 | I-035, I-045 | — |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:144 | E-05 | I-070, I-071, I-074 | — |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:145 | — | — | Không có việc riêng: máy quét gõ vào cùng ô nhập, không đổi API |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:146 | E-04, E-41 | I-054.1, I-055.1, I-401.1 | Hàm nạp CSV nhiệt thuộc màn nạp CSV; nền tảng cấp hàm gom đợt và hàm ghi mục thiếu số đo |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:147 | E-05 | I-072, I-075 | — |
| architecture/diem-tich-hop.mmd; architecture/kien-truc.md:148 | E-05 | I-073 | — |
| architecture/kien-truc.md §4 | E-02 | I-017 | — |
| architecture/kien-truc.md §3.7 | E-02, E-03 | I-019, I-034 | — |
| architecture/kien-truc.md §3.8 | E-02, E-04 | I-016, I-056 | — |
| architecture/kien-truc.md §9 | E-02, E-03 | I-019, I-034 | — |
| architecture/kien-truc.md §10 | E-02 | I-010, I-011, I-012, I-013, I-014, I-015, I-016 | — |
| architecture/kien-truc.md §11 | E-01, E-04 | I-003, I-004, I-050 | — |
| _common/error-codes.md | E-03 | I-030, I-038 | — |
| _common/hop-dong-api-prototype.md | E-03 | I-030, I-038 | — |
| database-diagram/ma-tran-quyen-that.md | E-03 | I-031 | — |
| database-diagram/schema-that.md | E-02 | I-010, I-011, I-012, I-013, I-014, I-015, I-016 | — |
| database-diagram/migration-list.txt; schema-live.txt; schema-live.json; giai-thich-lech.json | E-01 | I-002 | — |
| database-diagram/erd-prototype-that-*.mmd (7 file) | — | — | Sơ đồ đối chiếu của bản dựng thử; migration dựng theo sơ đồ thiết kế đích |
| database-diagram/erd-thiet-ke-dich-tong.mmd | E-02 | I-010, I-011, I-012, I-013, I-014, I-015, I-016 | — |
| database-diagram/chenh-lech-thiet-ke-prototype.md | E-02 | I-010, I-011, I-012, I-013, I-014, I-015, I-016 | — |
| system-design/database-design/receiving-inventory/RCV_INV_DB.md | E-02 | I-010 | — |
| system-design/database-design/outbound-routing/OUT_ROUTE_DB.md | E-02 | I-012, I-013 | — |
| system-design/database-design/temperature-haccp/TEMP_HACCP_DB.md | E-02 | I-011 | — |
| system-design/database-design/quality-traceability/QUAL_TRACE_DB.md | E-02 | I-014 | — |
| system-design/database-design/admin-settings/ADMIN_SET_DB.md | E-02 | I-015, I-016 | — |
| system-design/database-design/reporting/RPT_DB.md | E-02 | I-016 | — |
| premise/gia-tri-nghiep-vu.md | E-02 | I-018 | — |
| premise/pham-vi-man-lab4.md | — | — | Nguồn của mức A/B dùng cho luật G2, G3; không phải việc |
| premise/cau-hoi-khach-bo-sung-lab4.md | E-03, E-05 | I-045, I-074, I-075 | — |
| PREMISE.md của LAB-4 §1, §2.1, §3, §4, §5 | — | — | Tiền đề đọc khi chia; giả định mới đi vào PREMISE.md của bài này |
| wireframe/index.md | E-03 | I-036, I-039 | — |
| _index.md | — | — | Trạng thái tài liệu; ba màn đang xem xét được ghi giả định (`PREMISE:NH-25`) |

## 3. Việc chịu ràng buộc riêng của đề: giới hạn giờ lái xe tải từ 4/2024

Từ tháng 4/2024, giờ làm việc của tài xế xe tải bị giới hạn chặt hơn theo 改善基準告示 (tiêu chuẩn cải thiện điều kiện làm việc của tài xế ô tô) bản sửa đổi, hiệu lực 4/2024 — bối cảnh mà ngành gọi là 物流2024年問題 (vấn đề logistics năm 2024). Các nhóm giới hạn hệ thống phải kiểm: 拘束時間 (thời gian ràng buộc, tính từ lúc bắt đầu tới lúc kết thúc ca, gồm cả nghỉ), 休息期間 (thời gian nghỉ giữa hai ca), 運転時間 (giờ lái), 連続運転 (lái liên tục, phải ngắt bằng nghỉ), 時間外労働 (làm thêm giờ). Tuyến từng chạy được trước đây có thể không còn hợp lệ, nên mọi điểm chạm được gom vào epic riêng **E-32 Ràng buộc giờ lái 2024**, mỗi điểm chạm một issue mang nhãn `rang-buoc-gio-lai-2024`, không gộp vào issue màn lập tuyến hay xuất kho. Giá trị giới hạn là tham số có phiên bản, không viết cứng, và phải đối chiếu lại với văn bản chính thức trước khi chốt.

Truy vết trên toàn gói thiết kế ra 64 điểm chạm (bảng, endpoint, mã lỗi, màn, tài liệu kiến trúc). 18 issue của E-32:

| Ràng buộc | Issue | Vì sao tách riêng |
|---|---|---|
| 拘束時間, 時間外労働, 休息期間, 運転時間, 連続運転 — kiểm năm nhóm và phát hành tuyến (màn kiểm giờ) | I-320 (.1–.4) | Cả màn là phép kiểm theo quy định mới; tách khỏi màn lập tuyến để khối lượng và tiến độ của ràng buộc đo được riêng |
| 拘束時間, 時間外労働, 運転時間 — sổ giờ tích luỹ theo tháng, năm, bình quân 2 ngày, 2 tuần (màn sổ giờ) | I-321 (.1–.4) | Sổ giờ là bằng chứng tuân thủ theo chu kỳ tháng, năm; đổi theo đáp án ba khoá chưa có số |
| 拘束時間, 時間外労働, 運転時間 — hàm tổng sổ giờ dùng chung | I-322 | Mọi kết luận tuân thủ đọc từ một con số; sai ở đây làm sai mọi phép kiểm nên cần ước lượng và kiểm thử riêng |
| 拘束時間, 時間外労働, 休息期間 — phép so thời gian ràng buộc ngày, tháng, năm, làm thêm giờ năm, nghỉ giữa ca | I-323 | Nhóm giới hạn có giá trị biên riêng và phụ thuộc ba khoá chưa có số; tách để đổi tham số không chạm phép so khác |
| 運転時間, 連続運転 — phép so giờ lái bình quân và lái liên tục theo chặng | I-324 | Tính trên chặng của tuyến, cách ngắt chuỗi lái liên tục còn chờ khách |
| 拘束時間, 時間外労働, 休息期間, 運転時間, 連続運転 — chọn và gắn bộ quy tắc đang hiệu lực lúc phát hành | I-325 | Quy định hoặc tham số đổi sau khi phát hành thì tuyến đã phát hành giữ bộ đã gắn, tuyến phát hành sau áp bộ đang hiệu lực lúc đó |
| 拘束時間, 時間外労働, 休息期間, 運転時間, 連続運転 — hàm phát hành: khoá tài xế, kiểm lại, ghi sổ giờ | I-326 | Phát hành là điểm chặn duy nhất buộc tuân thủ; khoá tài xế và ghi sổ giờ trong một giao dịch |
| 運転時間 — chặn phát hành khi ước tính di chuyển vượt mức hoặc chưa có | I-327 | Tuyến không khả thi trong giới hạn lái thì không được giao cho tài xế; phụ thuộc dịch vụ bản đồ nên rủi ro riêng |
| 拘束時間, 時間外労働, 休息期間, 運転時間, 連続運転 — kiểm lại khi phát hành phiên bản mới của tuyến | I-328 | Sửa tuyến sau phát hành có thể làm tuyến vượt giới hạn; phải kiểm lại và đảo bút toán cũ |
| 拘束時間, 時間外労働, 運転時間 — bút toán đảo khi huỷ tuyến đã phát hành | I-329 | Huỷ tuyến phải trả lại giờ đã ghi, không thì tổng tháng, năm bị thừa |
| 拘束時間, 時間外労働, 運転時間 — hàm ghi và đảo bút toán sổ giờ | I-330 | Một quy ước ghi và đảo cho ba thao tác; sổ giờ không được sửa |
| 拘束時間, 時間外労働, 休息期間, 運転時間, 連続運転 — mã bộ quy tắc trong phản hồi chi tiết tuyến, kết quả kiểm, lịch trình | I-331 | Người xem phải biết tuyến được kiểm theo bộ quy tắc nào khi quy định đổi |
| 拘束時間, 運転時間, 連続運転 — hợp đồng dữ liệu giữa API cấu hình và màn lập tuyến | I-332 | Nơi khai tham số và nơi tạm tính thuộc hai nhóm việc khác nhau; kiểm riêng để thay đổi một bên không làm sai tạm tính |
| 拘束時間, 運転時間, 連続運転 — tạm tính giờ lái khi nhập chặng trên màn lập tuyến | I-333 | Người lập thấy nguy cơ vượt giới hạn ngay khi nhập chặng, trước bước phát hành |
| 拘束時間, 時間外労働, 運転時間 — chế độ chỉ thêm của sổ giờ | I-334 | Sổ giờ là bằng chứng tuân thủ nên chỉ thêm, không sửa, không xoá |
| 拘束時間, 時間外労働 — điều kiện xoá sổ giờ khi dọn dữ liệu hết hạn | I-335 | Dọn dữ liệu hết hạn không được làm thiếu giờ của năm còn tính trần thời gian ràng buộc năm |
| 時間外労働, 連続運転 — câu hỏi giá trị ba khoá giờ lái chưa có số | I-392 | Ba khoá ảnh hưởng mọi phép kiểm; một issue theo dõi đáp án cho bốn màn |
| 運転時間 — câu hỏi cách hiểu ước tính di chuyển vượt 24 giờ | I-393 | Một cách hiểu chung cho cảnh báo lúc lưu nháp và hai điểm chặn phát hành |

Điểm chạm nằm ngoài E-32 (không tách thêm issue):

| Ràng buộc | Issue | Vì sao không tách thêm |
|---|---|---|
| Ca làm, chặng lái, nghỉ và làm việc của tuyến (dữ liệu đầu vào của phép kiểm) | I-301.1, I-301.2, I-301.5 (E-31) | Là việc lập, sửa tuyến chung; phần kiểm giờ lái của màn đã tách ở I-327, I-332, I-333 |
| Lịch trình tài xế, phiên bản tuyến | I-302.1, I-302.2 (E-31) | Chỉ hiển thị; kiểm lại và bút toán đảo nằm ở I-328, I-329 |
| Xe, khung giờ giao cho lập tuyến | I-301.6 (E-31), I-514, I-515 (E-52) | Dữ liệu chủ dùng chung cho nhiều màn, không chỉ cho giờ lái |
| Bảng sổ giờ, bộ tham số khởi tạo (13 khoá), hàm đọc cấu hình có phiên bản | I-013, I-015, I-018, I-051 (nền tảng) | Cơ chế dùng chung với nhóm tham số HACCP; giờ lái chỉ đọc |
| Khai và duyệt bộ tham số giờ lái | I-501.5, I-501.6 (E-51) | Màn cấu hình chung cho mọi nhóm tham số; không kiểm giờ |
| Ghi nhận giao hàng chuyển tuyến sang đang chạy, hoàn tất | I-206.3 (E-23) | Thuộc luồng giao hàng; I-302.1, I-329 phụ thuộc issue này |
| Vòng đời tuyến (đang chạy, hoàn tất, huỷ tuyến đang chạy) quyết định giờ được giữ hay đảo | I-391 (E-31) | Câu hỏi chung cho xuất kho và lập tuyến nên đặt ở E-31; issue giờ lái liên quan mang thẻ câu hỏi |
| Dọn dữ liệu hết hạn có sổ giờ | I-540.6 (E-55) | Thuộc lưu giữ dữ liệu; gọi điều kiện xoá của I-335 |

## 4. Chỗ hở, mâu thuẫn trong spec LAB-4 tìm thấy lúc chia

Mỗi dòng có đúng một cách xử lý: sửa thiết kế hoặc giả định (kèm khoá dòng trong PREMISE.md), issue làm rõ (kèm mã issue), hoặc để mở kèm lý do. Tên spec viết tắt theo tên file màn trong gói thiết kế (vd `OUT_01` = màn danh sách và tạo đơn xuất).

| Spec | Chỗ hở/mâu thuẫn | Xử lý |
|---|---|---|
| OUT_01, INT_01; điểm tích hợp ERP ở tài liệu kiến trúc | Không có job hay endpoint nhận file đơn ERP; chưa có đặc tả file; nơi chạy job trái nguyên tắc một nơi giữ khoá bí mật (ADR-004) | đã sửa thiết kế (`PREMISE:QĐ-A`) |
| Danh mục API (hàng đợi thông báo), INT_01 | Hàng đợi thông báo có nơi đưa vào và nơi gửi lại nhưng không có tiến trình gửi thư; không nơi nào lập thông báo khi alarm quá hạn xem xét | đã sửa thiết kế (`PREMISE:QĐ-F`) |
| TEMP_02, TRC_03 | Hai giả định khác nhau về người nhận thư nội bộ; "ma trận leo thang" không có bảng hay endpoint | giả định (`PREMISE:NH-03`) |
| MST_01, MST_02, SCH_01, OUT_05 | Tài xế, xe, khung giờ giao, hợp đồng khách × SKU, bộ chứng cứ POD, vị trí cách ly của dải nhiệt không có màn hay endpoint bảo trì | đã sửa thiết kế (`PREMISE:QĐ-B`) |
| Nhiều màn (bảng ở mục 1.4) | Một câu hỏi khách được giả định lặp ở nhiều spec, khách đổi đáp án thì phải sửa nhiều nơi; khi chia phát hiện thêm Q16, KH-L4-16, KH-L4-35 lặp mà chưa có issue gốc | tạo issue làm rõ (I-045, I-074, I-191…I-195, I-291…I-296, I-391…I-393, I-491…I-495, I-505, I-591) |
| TEMP_04, EXP_01, ADR-002 | Lịch hai ca vệ sinh HACCP nằm trong hàm SQL, không phải khoá tham số; đổi giờ ca phải sửa mã | để mở: giữ theo quyết định QĐ16 của LAB-4 (ngoại lệ có chủ đích của ADR-002); hàm lịch ca là I-052, giờ ca thật hỏi khách ở I-492 |
| OUT_04, SCH_01 | Xe nạp hàng có phải là xe của tuyến không: thiết kế không đối chiếu | giả định (`PREMISE:NH-07`) |
| INV_03 | Cách ly tay có đổi vị trí lô không | để mở: đã xử lý ở quyết định QĐ15 của LAB-4 (chỉ đổi trạng thái, giữ vị trí), không còn việc |
| MST_04, OUT_06 | Màn xếp mức B nhưng mang luật (sự kiện đảo cần hai người; hai trạng thái độc lập có audit riêng) | để mở: không đổi mức trong gói thiết kế; phần luật tách issue riêng (I-210, I-211) để ước lượng theo luật |
| OUT_02, OUT_05, OUT_06 | Giao không thành, huỷ đơn, đưa hàng trả về tồn chưa được thiết kế | giả định (`PREMISE:QĐ-E`) |
| SCH_02 mục 2.6, danh mục API EP-30, EP-31 | Thời điểm chọn bộ quy tắc giờ lái khác nhau giữa màn (ngày hiện tại) và danh mục API (ngày chạy của tuyến), trong khi tài liệu yêu cầu của khách gắn bộ hiệu lực lúc phát hành | đã sửa thiết kế (`PREMISE:QĐ-C`): theo thời điểm phát hành, đổi phiên bản bộ sau đó không hồi tố |
| Danh mục API EP-29, EP-30, EP-D41 | Phản hồi thiếu mã bộ quy tắc áp dụng mà màn kiểm giờ và màn lịch trình phải hiển thị | đã sửa thiết kế (`PREMISE:NH-12`) |
| SCH_01 mục 4.11, danh mục API EP-16 | Màn lập tuyến đọc tham số giờ lái từ `data.parameters`, trong khi API cấu hình trả danh sách bộ `parameter_sets[]` | đã sửa thiết kế (`PREMISE:TH-03`) |
| Danh mục API (cột Màn gọi), EP-27 | Cột Màn gọi thiếu màn ghi sự cố; danh sách tuyến không lọc theo tài xế | để mở: không đổi danh mục API — phụ thuộc lấy theo cột Item gọi của spec màn (I-303.2), lọc theo tài xế làm ở trình duyệt (I-321.2) |
| SCH_01, SCH_03 | Không xem trước được kết quả kiểm năm nhóm khi sửa tuyến đã phát hành | để mở: hạn chế đã biết, lỗi lộ ở bước phát hành phiên bản mới; ghi trong DoD I-301.2, I-301.5, I-328 |
| MIG_01, SCH_05 | Chuyển dữ liệu không có loại hồ sơ số dư đầu kỳ sổ giờ; chưa có đặc tả cột tệp nguồn từng loại | tạo issue làm rõ (I-522) |
| SEC_04, thiết kế dữ liệu quản trị §4.11 | Nhóm hồ sơ đào tạo không có bảng; nhật ký audit không thuộc nhóm lưu giữ nào | tạo issue làm rõ (I-541) |
| RPT_02, SEC_04 | Lần xuất audit theo lịch lưu giữ không có đường ghi | giả định (`PREMISE:NH-15`) |
| TEMP_04, SCH_04, RPT_01 | Màn khác giao việc cho báo cáo thuộc nhóm chưa dựng (hồ sơ HACCP còn thiếu, chậm trễ giao hàng theo nguyên nhân); chỉ số tỷ lệ xem xét trễ không có báo cáo | giả định (`PREMISE:NH-16`) |
| RPT_01, SCH_01, SCH_02 | Mã câu hỏi Q12 dùng với hai nghĩa: mẫu báo cáo chưa dựng (RPT_01) và câu phụ về cách ngắt chuỗi lái liên tục (SCH_01, SCH_02) | tạo issue làm rõ (I-495) |
| SEC_01, INT_01 | Theo dõi phiên định danh doanh nghiệp bị hai màn trỏ vòng cho nhau | đã sửa thiết kế (`PREMISE:NH-17`) |
| REC_03, INV_05, SEC_04 | Luồng người lập khác người duyệt cần ít nhất hai tài khoản mỗi vai duyệt; ca một tài khoản mang hai vai chưa nói | giả định (`PREMISE:NH-18`) |
| SEC_01, EXP_01 | Vai lập kế hoạch giao hàng duyệt bộ tham số giờ lái nhưng không thuộc nhóm bắt buộc MFA | đã sửa thiết kế (`PREMISE:QĐ-D`) |
| EXP_01, OUT_02 | Bản dựng thử hiểu quy tắc 1/3 là lô còn từ 1/3 thời hạn, thiết kế đích là còn từ 2/3 | để mở: làm theo thiết kế đích (sửa hàm phân bổ ở I-202.3); nghĩa chốt với khách ở I-291 |
| MST_03, REC_02, OUT_02 | SKU mới duyệt xong có thể chưa có phiên bản loại hạn; nhập kho và phân bổ xử lý ra sao chưa nói (trong lúc chờ, issue nhập kho và phân bổ dùng giả định tạm `PREMISE:TH-02`) | tạo issue làm rõ (I-503) |
| Danh mục API EP-17, EP-18, EP-19 | Route sửa thẳng ngưỡng nhiệt, loại hạn, quy tắc hợp đồng còn trong danh mục, đi vòng qua bước duyệt | đã sửa thiết kế (`PREMISE:NH-22`) |
| MST_02 | Nhân viên kho có quyền xem nhưng không có lối vào màn | giả định (`PREMISE:NH-23`) |
| Sơ đồ luồng 4; tài liệu kiến trúc §3.4, §3.7, §3.8 | Sơ đồ kiến trúc thiếu luồng 7, 8; luồng 4 còn mô tả bản dựng thử | để mở: không sửa gói thiết kế; issue lấy nguồn từ tài liệu kiến trúc §3.4, §3.7, §3.8 và danh mục API |
| REC_03, INV_02, INV_05 | Ba màn còn trạng thái đang xem xét, phạm vi có thể đổi | giả định (`PREMISE:NH-25`) |
| REC_03 | Cụm "khớp số báo" dễ lẫn hai phép so tổng | để mở: xử lý trong issue giao diện I-104.2 (nhãn tách rõ số thực nhận và số báo) |
| INV_05, EXP_01 | Ngưỡng duyệt hai cấp của điều chỉnh kiểm kê chưa có giá trị và không có nơi khai | tạo issue làm rõ (I-504) |
| REC_01, REC_02, REC_03, INV_05 | Giả định tạm chờ khách chỉ nằm ở một màn nhập kho (lịch hẹn nhập tay, dòng bò chờ rà soát, mã lý do phân tách…) | giả định (`PREMISE:NH-28`) |
