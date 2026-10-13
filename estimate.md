# Ước lượng — Yuki Cold WMS

Báo cáo chấm SWP (HTML): [bao-cao-swp/sun-estimate-yuki-cold-wms-mng-20261012-1709.html](bao-cao-swp/sun-estimate-yuki-cold-wms-mng-20261012-1709.html)

Backlog có 268 việc lá được chấm; epic và issue cha lấy tổng SWP của việc con. Tổng sau khi kiểm issue mẫu: **1165 SWP** (skill chấm ban đầu 1177 SWP).

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

## 2. Cách quy ra giờ

**Cách chọn:** quy ước đổi SWP ra giờ, hệ số theo nhóm việc, lấy từ issue mẫu ước giờ trực tiếp.

**Vì sao:** một hệ số áp cho mọi issue giữ được nhất quán và kiểm lại được bằng phép nhân, thay vì ước tay 268 việc lá. Hệ số lấy từ 10 issue mẫu trải đều các mức SWP và loại việc, được ước giờ trực tiếp từ nội dung issue mà không xem SWP, nên hệ số không bị điểm kéo theo. Mẫu cho thấy giao diện và kiểm thử tốn khoảng 1,8 lần giờ mỗi SWP so với backend, nên dùng hệ số theo nhóm thay vì một hệ số chung.

**Quy tắc:** hệ số nhóm = tổng giờ ước trực tiếp của mẫu trong nhóm ÷ tổng SWP của các mẫu đó. Giờ việc lá = SWP × hệ số nhóm, làm tròn 0,5 giờ (tối thiểu 0,5); epic và issue cha = tổng giờ việc con. Giờ là công làm của một người đúng vai: đọc spec, làm, tự kiểm theo định nghĩa xong, sửa sau review — không gồm dự phòng, chờ khách trả lời, quản lý dự án.

**Áp dụng nhất quán:** một script tính giờ cho mọi việc lá từ SWP đã chốt và ghi lên trường giờ ước lượng của Project; đọc lại trường này so với bảng giờ, lệch 0.

| Nhóm việc | Hệ số (giờ/SWP) | Việc lá | SWP | Giờ |
|---|---|---|---|---|
| Backend, DB, hạ tầng, tích hợp | 2,69 | 147 | 724 | 1.949 |
| Giao diện và kiểm thử | 4,86 | 91 | 390 | 1.898 |
| Làm rõ với khách | 2,5 | 30 | 51 | 127,5 |

Issue mẫu ước giờ trực tiếp:

| Issue | Nhóm | SWP | Giờ ước | Giờ/SWP |
|---|---|---|---|---|
| #77 [I-191] Làm rõ ai được xem đợt kiểm kê và danh sách điều chỉnh với khách | Làm rõ với khách | 1 | 2,5 | 2,5 |
| #43 [I-033] Dựng hàm kiểm quyền theo dòng dùng chung cho tuyến của tài xế và tệp chứng cứ | Backend, DB, hạ tầng, tích hợp | 3 | 8 | 2,67 |
| #41 [I-031] Áp ma trận quyền bảy vai trò và kiểm tự động ma trận với mã nguồn | Backend, DB, hạ tầng, tích hợp | 5 | 14 | 2,8 |
| #172 [I-101.1] Dựng API và hàm DB cho màn danh sách lịch hẹn nhập và quản lý dòng hàng | Backend, DB, hạ tầng, tích hợp | 8 | 24 | 3 |
| #108 [I-326] Dựng hàm phát hành tuyến: khoá tài xế, kiểm lại năm nhóm và ghi sổ giờ | Backend, DB, hạ tầng, tích hợp | 10 | 20 | 2 |
| #47 [I-037] Dựng thành phần giao diện bảng dữ liệu, bộ lọc và ô chọn dữ liệu chủ dùng chung | Giao diện và kiểm thử | 4 | 22 | 5,5 |
| #219 [I-206.2] Dựng giao diện ghi nhận giao hàng cho tài xế | Giao diện và kiểm thử | 6 | 26 | 4,33 |
| #177 [I-102.4] Viết bộ kiểm thử cho màn kiểm hàng nhập từng dòng | Giao diện và kiểm thử | 4 | 20 | 5 |
| #157 [I-010.2] Tạo migration bảng mới miền nhập kho và tồn kho | Backend, DB, hạ tầng, tích hợp | 4 | 13 | 3,25 |
| #3 [I-002] Lập CI chạy migration, test TypeScript và test hàm Postgres cho mỗi lần đẩy mã | Backend, DB, hạ tầng, tích hợp | 5 | 15 | 3 |

## 3. Tổng theo epic

| Epic | Số issue (việc lá) | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| E-01 Dựng hạ tầng, môi trường và vận hành | 4 | 24 | 64,5 | 4 issue, 0 sub-issue |
| E-02 Dựng dữ liệu nền: schema đích và dữ liệu khởi tạo | 15 | 77 | 208 | 10 issue, 9 sub-issue |
| E-03 Dựng khung ứng dụng, phân quyền và audit | 12 | 47 | 163 | 12 issue, 0 sub-issue |
| E-04 Dựng job nền và hàm nghiệp vụ dùng chung | 12 | 47 | 138,5 | 7 issue, 7 sub-issue |
| E-05 Dựng tích hợp ngoài và thông báo | 8 | 31 | 83 | 8 issue, 0 sub-issue |
| E-06 Kiểm chứng phi chức năng và kiểm thử hệ thống | 18 | 101 | 435 | 14 issue, 6 sub-issue |
| E-11 Dựng lịch hẹn nhập và nhận hàng có kiểm nhiệt | 13 | 55 | 191,5 | 4 issue, 12 sub-issue |
| E-12 Dựng phân tách số lượng nhận và duyệt chênh lệch | 6 | 25 | 84,5 | 2 issue, 5 sub-issue |
| E-13 Dựng tra cứu tồn kho và cất kho | 6 | 25 | 93,5 | 4 issue, 4 sub-issue |
| E-14 Dựng vòng trạng thái lô: cách ly, giải phóng, tiêu huỷ | 4 | 16 | 60,5 | 1 issue, 4 sub-issue |
| E-15 Dựng kiểm kê mù và điều chỉnh chênh lệch | 9 | 34 | 117 | 4 issue, 7 sub-issue |
| E-21 Dựng đơn xuất và phân bổ | 12 | 47 | 156,5 | 6 issue, 8 sub-issue |
| E-22 Dựng soạn hàng và nạp xe | 8 | 33 | 114,5 | 4 issue, 6 sub-issue |
| E-23 Dựng giao hàng và ghi nhận giao hàng (POD) | 5 | 29 | 99,5 | 1 issue, 5 sub-issue |
| E-24 Dựng lịch sử giao, sự kiện đảo và khiếu nại | 8 | 28 | 92,5 | 6 issue, 4 sub-issue |
| E-31 Dựng lập tuyến và lịch trình tài xế | 11 | 46 | 164,5 | 4 issue, 10 sub-issue |
| E-32 Ràng buộc giờ lái 2024 | 22 | 100 | 330 | 18 issue, 6 sub-issue |
| E-41 Dựng theo dõi nhiệt độ và hàng đợi alarm | 11 | 54 | 186 | 5 issue, 8 sub-issue |
| E-42 Dựng hồ sơ sai lệch và hồ sơ HACCP | 14 | 61 | 213,5 | 4 issue, 12 sub-issue |
| E-43 Dựng truy xuất và thu hồi | 14 | 58 | 215,5 | 3 issue, 14 sub-issue |
| E-44 Dựng báo cáo và gói bằng chứng audit | 8 | 33 | 112 | 3 issue, 7 sub-issue |
| E-51 Dựng cấu hình luật nghiệp vụ | 10 | 39 | 130,5 | 5 issue, 6 sub-issue |
| E-52 Dựng quản lý dữ liệu chủ | 17 | 57 | 199,5 | 7 issue, 16 sub-issue |
| E-53 Dựng chuyển dữ liệu và theo dõi tích hợp | 9 | 42 | 134 | 3 issue, 8 sub-issue |
| E-54 Dựng người dùng, vai trò và nhật ký audit | 4 | 14 | 57 | 3 issue, 2 sub-issue |
| E-55 Dựng lưu giữ dữ liệu, legal hold và purge | 8 | 42 | 130 | 2 issue, 7 sub-issue |
| **Cộng** | **268** | **1165** | **3.974,5** | |

Kiểm năng lực: đội làm issue (backend, frontend, kiểm thử, hạ tầng, BrSE) có 611 giờ mỗi sprint, gồm đội hình của estimate LAB-1 và một frontend bổ sung. 3.974,5 giờ ÷ 611 giờ ≈ 6,5 sprint, trong khung 8,6 sprint quy đổi của giai đoạn xây dựng (một sprint trùng nghỉ Tết tính 60 %). Phép chia tổng giờ chưa đủ: khi xếp từng việc theo vai và phụ thuộc, đội hình LAB-1 cần 10 sprint, vì phần frontend chiếm khoảng 93 % năng lực của hai frontend mà màn chỉ dựng được khi API đã bắt đầu. Thêm một frontend toàn thời gian từ Sprint 1 thì kế hoạch vừa 9 sprint, nhưng không còn đệm; phần thêm là 550,4 giờ (68,8 MD) so với đội hình LAB-1. Kế hoạch sprint và rủi ro ở progress-report.md.

## 4. So với estimate LAB-1

Đơn vị: LAB-1 tính ngày công (MD) theo vai, 1 MD = 8 giờ; LAB-5 tính giờ theo issue. Ba lý do chung cho mọi dòng: (1) MD của LAB-1 đã gồm 15 % dự phòng, giờ LAB-5 không có; (2) gói xây dựng của LAB-1 có cột thiết kế giao diện, phần này đã làm xong ở bộ thiết kế chi tiết; (3) LAB-1 tính kiểm thử trong từng gói, LAB-5 gom kiểm thử hệ thống về E-06. Dòng ghi "(ước)" là số LAB-1 chia theo trọng số màn, không phải số WBS nêu thẳng.

| Phần (epic) | LAB-1 MD | LAB-1 giờ | LAB-5 giờ | Chênh giờ | Vì sao |
|---|---|---|---|---|---|
| E-02 Dựng dữ liệu nền: schema đích và dữ liệu khởi tạo | — | — | 208 | — | LAB-1 không có gói dựng bảng riêng: công dựng dữ liệu nằm rải trong cột Backend của từng gói chức năng. LAB-5 gom việc dựng toàn bộ bảng thiết kế đích về một epic nền nên không gán số LAB-1. |
| E-04 Dựng job nền và hàm nghiệp vụ dùng chung | — | — | 138,5 | — | LAB-1 không có gói riêng: các hàm dùng chung (cách ly, gom đợt alarm, lịch ca HACCP, đề xuất purge) nằm trong cột Backend của gói gọi chúng. LAB-5 tách thành một epic để mỗi hàm chỉ dựng một lần; phần này làm các epic chức năng thấp hơn LAB-1. |
| E-05 Dựng tích hợp ngoài và thông báo | 51,75 | 414 | 83 | -331 | Gói 3.2 tính sáu giao diện tích hợp kể cả phần chờ khách trả lời câu hỏi tích hợp. LAB-5 chuyển đăng nhập doanh nghiệp sang E-03, nạp CSV logger sang E-41, màn theo dõi tích hợp sang E-53, hàm xếp thông báo sang E-04; E-05 chỉ còn nhận file ERP qua SFTP theo lịch (PREMISE.md P1-01), job gửi thư cho ba loại sự kiện (P1-05, P1-06) và làm rõ đặc tả file. |
| E-11 Dựng lịch hẹn nhập và nhận hàng có kiểm nhiệt | 46 | 368 | 191,5 | -176,5 | Số LAB-1 là phần chia của gói 2.2 và 2.3 theo trọng số màn (ước). Hàm cách ly dùng chung tính ở E-04; giả định nhập kho của PREMISE.md P2-16, P2-17 giữ phạm vi màn như bộ thiết kế, không thêm việc. |
| E-12 Dựng phân tách số lượng nhận và duyệt chênh lệch | 21,16 | 169,28 | 84,5 | -84,78 | Phần chia của gói 2.2 theo trọng số màn (ước). Nguồn thông báo duyệt chênh lệch (P1-06) thêm một ít việc nhưng hàm xếp thông báo tính ở E-04. |
| E-13 Dựng tra cứu tồn kho và cất kho | 21,39 | 171,12 | 93,5 | -77,62 | Phần chia của gói 2.3 theo trọng số màn (ước). Giả định một lô một vị trí (PREMISE.md P2-18) làm luật cất kho đơn giản hơn. |
| E-14 Dựng vòng trạng thái lô: cách ly, giải phóng, tiêu huỷ | 14,26 | 114,08 | 60,5 | -53,58 | Phần chia của gói 2.3 theo trọng số màn (ước); hàm cách ly dùng chung tính ở E-04. |
| E-15 Dựng kiểm kê mù và điều chỉnh chênh lệch | 21,39 | 171,12 | 117 | -54,12 | Phần chia của gói 2.3 theo trọng số màn (ước). Ngưỡng duyệt hai cấp theo giả định tạm (PREMISE.md P2-15) không thêm việc. |
| E-21 Dựng đơn xuất và phân bổ | 82,8 | 662,4 | 156,5 | -505,9 | LAB-1 cho E-21 trọn cột Backend và QA của gói Rule Engine 2.4 (55,20 MD) — bộ luật hạn, FEFO, cấm đảo ngày hạn, cửa sổ giao — cộng phần chia của gói 2.5. Ở LAB-5 các hàm luật nằm ở E-21 nhưng kiểm thử hệ thống ở E-06 và cấu hình luật có phiên bản ở E-51; nên so cặp E-21 + E-51. |
| E-22 Dựng soạn hàng và nạp xe | 27,6 | 220,8 | 114,5 | -106,3 | Phần chia của gói 2.5 theo trọng số màn (ước). |
| E-23 Dựng giao hàng và ghi nhận giao hàng (POD) | 18,4 | 147,2 | 99,5 | -47,7 | Phần chia của gói 2.5 theo trọng số màn (ước). Ba luồng ngoại lệ xuất kho chưa làm, chờ khách (PREMISE.md P2-02), nên ít việc hơn. |
| E-24 Dựng lịch sử giao, sự kiện đảo và khiếu nại | 16,67 | 133,36 | 92,5 | -40,86 | Phần chia của gói 2.1 và 2.5 (ước). Lịch sử giao bất biến dùng cơ chế chỉ thêm dựng chung ở E-02. |
| E-31 Dựng lập tuyến và lịch trình tài xế | 35,93 | 287,44 | 164,5 | -122,94 | LAB-1 chia gói 2.6 theo trọng số màn và tính trọn phần giờ lái của màn lập tuyến, lịch trình tài xế cho E-31; LAB-5 tách hết phần giờ lái sang E-32. So cặp E-31 + E-32 thì hai bản gần khớp. |
| E-32 Ràng buộc giờ lái 2024 | 28,47 | 227,76 | 330 | 102,24 | Cao hơn LAB-1 vì nhận phần giờ lái mà LAB-1 tính ở E-31 (xem dòng E-31), cộng việc mới do tiền đề: chọn bộ quy tắc theo thời điểm phát hành, không hồi tố (PREMISE.md P1-03, P3-02), số dư đầu kỳ của sổ giờ (P2-06), cách so nghỉ giữa ca khi chỉ một phía có ca (P2-21). |
| E-41 Dựng theo dõi nhiệt độ và hàng đợi alarm | 31,05 | 248,4 | 186 | -62,4 | Phần chia của gói 2.7 (ước). Job đối soát và gom đợt alarm tính ở E-04; thông báo alarm quá hạn xem xét là việc mới (PREMISE.md P1-06, P2-04) nhưng nhỏ. |
| E-42 Dựng hồ sơ sai lệch và hồ sơ HACCP | 31,05 | 248,4 | 213,5 | -34,9 | Phần chia của gói 2.7 (ước); hàm lịch ca HACCP tính ở E-04. Hai nhóm hồ sơ chỉ khai thời hạn lưu (PREMISE.md P2-08) không thêm màn. |
| E-43 Dựng truy xuất và thu hồi | 54,05 | 432,4 | 215,5 | -216,9 | Gói 2.8 tính trọn truy xuất và thu hồi. LAB-5 thu hẹp case thu hồi về một lô mỗi case (PREMISE.md P2-20); kiểm thời gian truy xuất lô 3 năm chuyển sang E-06. |
| E-44 Dựng báo cáo và gói bằng chứng audit | 50,6 | 404,8 | 112 | -292,8 | LAB-1 tính đủ 12 loại báo cáo (khoảng 0,9 MD mỗi loại); bộ thiết kế chi tiết dựng 4 loại, hai báo cáo tách sang nhóm chờ khách (PREMISE.md P2-10), lần xuất bằng chứng theo lịch lưu giữ chưa làm (P2-09). |
| E-51 Dựng cấu hình luật nghiệp vụ | 10,35 | 82,8 | 130,5 | 47,7 | LAB-1 chỉ cho E-51 cột Frontend và thiết kế của gói 2.4 (10,35 MD); LAB-5 gồm cả API và hàm của cấu hình luật có phiên bản, thay việc sửa thẳng cấu hình (PREMISE.md P1-08). Xem cùng E-21. |
| E-52 Dựng quản lý dữ liệu chủ | 37,38 | 299,04 | 199,5 | -99,54 | Phần chia của gói 2.1 (ước). Bảo trì tài xế, xe, khung giờ giao là việc mới (PREMISE.md P1-02, P2-01) nhưng không bù phần dự phòng và thiết kế của LAB-1; lịch sử giao bất biến tính ở E-24. |
| E-53 Dựng chuyển dữ liệu và theo dõi tích hợp | 48,3 | 386,4 | 134 | -252,4 | Gói 4.1 gồm hai lần diễn tập và lần tải chính thức — việc vận hành giai đoạn chuyển đổi, không phải issue xây dựng; backlog chỉ có công cụ chuyển dữ liệu, màn đối soát và màn theo dõi tích hợp (cột tệp nguồn theo giả định PREMISE.md P2-07). |
| E-55 Dựng lưu giữ dữ liệu, legal hold và purge | 12 | 96 | 130 | 34 | LAB-1 tách 12,00 MD theo ghi chú WBS cho lưu giữ dữ liệu; LAB-5 làm đủ legal hold, purge có duyệt và hàm xoá theo từng nhóm hồ sơ (8 việc lá) nên cao hơn. |
| E-01 + E-03 + E-06 + E-54 (so một dòng) | 82,3 | 658,4 | 719,5 | 61,1 | Gói 3.1 phần còn lại và 3.3 (bảo mật, hiệu năng, BCP, giám sát, WCAG, bản địa hoá) so một dòng với hạ tầng, khung ứng dụng, kiểm chứng phi chức năng và quản trị người dùng. Sau khi bổ sung E-06 hai bản gần khớp. |
| **Cộng phần so được** | **742,9** | **5.943,2** | **3.974,5** | **-1.968,7** | Tách theo vai ở bảng dưới: dự phòng 15 % và thiết kế chiếm phần lớn khoảng chênh; phần còn lại do LAB-5 ước theo việc lá (không gồm phối hợp, sửa lỗi sau kiểm thử hệ thống) và các thu hẹp phạm vi đã nêu ở PREMISE.md. |
| Gói không có issue (1.1, 5.1, 5.2, 5.3, 6.1) | 313,95 | 2.511,6 | không có issue | — | Thiết kế cơ bản, hỗ trợ UAT, đào tạo, hypercare và quản lý dự án không có issue trong backlog xây dựng. |

Tách khoảng chênh theo vai (các gói so được):

| Vai | LAB-1 giờ (MD × 8) | LAB-1 giờ bỏ dự phòng 15 % | LAB-5 giờ | Chênh sau khi bỏ dự phòng |
|---|---|---|---|---|
| Backend (gồm DB, tích hợp) | 2.833,6 | 2.464 | 1.841,5 | -622,5 |
| Frontend | 1.214,4 | 1.056 | 1.046 | -10 |
| Thiết kế giao diện | 377,2 | 328 | 0 | -328 |
| Kiểm thử | 1.223,6 | 1.064 | 852 | -212 |
| Hạ tầng | 294,4 | 256 | 107,5 | -148,5 |
| Làm rõ với khách (BrSE) | 0 | 0 | 127,5 | 127,5 |
| **Cộng** | **5.943,2** | **5.168** | **3.974,5** | **-1.193,5** |
