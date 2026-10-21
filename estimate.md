# Ước lượng — Yuki Cold WMS

Báo cáo chấm SWP (HTML): [bao-cao-swp/estimate-swp-yuki-cold-wms-mng-20261021-0606.html](bao-cao-swp/estimate-swp-yuki-cold-wms-mng-20261021-0606.html)

Thuật ngữ: SWP (Standard Work Point) là điểm khối lượng chuẩn của một việc; leaf task là issue hoặc sub-issue không có sub-issue con, nơi ghi SWP và giờ; buffer là khoảng thời gian còn trống giữa ngày dự kiến xong và mốc, dùng để bù khi trễ; MD là ngày công (1 MD = 8 giờ); DoD (Definition of Done) là điều kiện để coi một issue là xong; BrSE là kỹ sư cầu nối với khách Nhật; UAT là kiểm thử chấp nhận do khách thực hiện; BCP là kế hoạch duy trì hoạt động khi có sự cố; FEFO là xuất lô hết hạn trước; HACCP là hệ thống kiểm soát mối nguy an toàn thực phẩm (bắt buộc ở Nhật từ 6/2021); POD là xác nhận giao hàng tại điểm nhận; legal hold là giữ dữ liệu không cho xoá vì lý do pháp lý; purge là xoá dữ liệu hết hạn lưu giữ. Mã `E-nn`, `I-nnn` dẫn tới issue trên GitHub.

Backlog có 310 leaf task được chấm; epic và issue cha lấy tổng SWP của việc con. Tổng sau khi kiểm issue mẫu: **1215 SWP** (skill chấm ban đầu 1235 SWP).

## 1. Issue mẫu được kiểm

Công cụ chấm (skill `tkm:estimate-swp`, tên trước đây `tkm:sun-estimate`) chọn 5 issue mẫu theo quy tắc cố định (nhỏ nhất, trung vị, lớn nhất, lệch xa trung vị, độ tin cậy thấp nhất). Mỗi issue được đối chiếu với DoD và spec nguồn, rồi chốt mức khó và điểm. Scope là độ rộng công việc (1, 2, 3, 5, 8, 13), Complexity là độ khó bên trong (0, 1, 2, 3, 5, 8); SWP tra từ bảng cố định Scope × Complexity.

| Issue | Vì sao được chọn | Skill chấm: Scope × Complexity → SWP | Điểm chốt sau kiểm tra | Lý do |
|---|---|---|---|---|
| [#44](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/44) I-034 — Dựng hàm chặn người đề xuất tự duyệt bản ghi của chính mình | issue nhỏ nhất | 1 × 1 → 1 | 1 × 1 → 1 | Giữ 1: DoD chỉ có một phép so người lập với người duyệt và một mã lỗi; việc gắn hàm vào từng luồng duyệt nằm ở issue của luồng đó. |
| [#213](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/213) I-204.2 — Dựng giao diện danh sách phiếu soạn hàng và chi tiết phiếu | mức trung vị | 3 × 1 → 4 | 3 × 1 → 4 | Giữ 4: một màn danh sách có lọc và chi tiết phiếu, thành phần quét dùng chung; luật soạn hàng nằm ở issue API. |
| [#160](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/160) I-012.1 — Tạo migration sửa bảng prototype miền xuất kho và lịch sử giao | issue lớn nhất | 8 × 2 → 12 | 5 × 2 → 8 | Hạ độ rộng 8 → 5, giữ độ khó 2 (12 → 8): tám bảng cùng một miền là một đợt migration có kiểm soát, chưa tới mức nhiều hệ thống con; phần khó thật là chạy trên dữ liệu đang có và phải lùi được nên giữ độ khó. Áp cho các issue migration cùng nhóm. |
| [#2](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/2) I-001 — Dựng ba môi trường phát triển, kiểm thử, chạy thật và quản lý khoá bí mật | lệch xa trung vị | 5 × 2 → 8 | 5 × 2 → 8 | Giữ 8: ba môi trường độc lập và quản lý khoá bí mật là phạm vi cả hệ thống; độ khó vừa vì cấu hình theo mẫu quen thuộc. |
| [#105](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/105) I-323 — Áp giới hạn thời gian ràng buộc, làm thêm giờ và nghỉ giữa ca khi kiểm tuyến | độ tin cậy thấp nhất | 3 × 3 → 6 | 3 × 3 → 6 | Giữ 6: năm phép so trong một luật, độ khó nằm ở chồng giờ với tuyến đã phát hành và số dư đầu kỳ; skill đã chấm đúng. |

Điều chỉnh ở issue mẫu được áp cho 6 issue cùng nhóm (cùng loại việc, cùng kiểu phạm vi và độ khó), mỗi issue hạ đúng số bậc như issue mẫu:

| Issue | Skill chấm | Sau điều chỉnh |
|---|---|---|
| [#33](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/33) I-013 — Tạo migration miền tuyến giao, tài xế và xe | 8 | 5 |
| [#34](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/34) I-014 — Tạo migration miền chất lượng và truy xuất | 6 | 4 |
| [#35](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/35) I-015 — Tạo migration cấu hình có phiên bản và vòng đời dữ liệu chủ | 8 | 5 |
| [#156](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/156) I-010.1 — Tạo migration sửa bảng prototype miền nhập kho và tồn kho | 8 | 5 |
| [#158](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/158) I-011.1 — Tạo migration sửa bảng prototype miền nhiệt độ và hồ sơ HACCP | 8 | 5 |
| [#162](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/162) I-016.1 — Tạo migration bảng người dùng, audit và hàng đợi thông báo | 5 | 3 |

Điểm chốt 8 của issue mẫu migration (#160) ứng với hạ một bậc độ rộng (Scope 8 → 5) và giữ độ khó, đúng lý do ở bảng trên; các issue cùng nhóm ở bảng này cũng hạ một bậc độ rộng, giữ độ khó.

Lượt chấm lại 2026-10-21 (sau review bài nộp): các việc mới và các phần tách từ việc quá 24 giờ được chấm bằng cùng skill; phần tách lấy đánh giá đã duyệt của việc gốc làm mốc. Issue mẫu được chọn lại trên toàn bộ leaf task theo cùng quy tắc và người làm lab duyệt lại; chi tiết ở mục Lưu ý của báo cáo HTML.

## 2. Cách quy ra giờ

**Cách chọn:** giờ = SWP × hệ số của nhóm việc; hệ số lấy từ 40 việc được ước giờ trực tiếp từ nội dung issue.

**Vì sao:** một hệ số theo nhóm việc giữ được nhất quán và kiểm lại được bằng phép nhân, thay vì ước tay 310 leaf task. Lần đầu hệ số lấy từ 10 issue mẫu và gộp giao diện với kiểm thử thành một nhóm. Khi ước lại trực tiếp 30 việc của ba epic chênh nhiều nhất với estimate LAB-1, giờ ước trực tiếp lệch có hướng theo loại việc so với hệ số cũ: việc API, hàm và luật cao hơn khoảng 30 %, việc kiểm thử cao hơn khoảng 22 %, việc giao diện thấp hơn khoảng 20 %. Vì vậy hệ số được tính lại từ cả 40 việc và tách giao diện, kiểm thử thành hai nhóm riêng; mỗi việc mẫu giữ SWP tại thời điểm được ước giờ, nên hệ số không bị điểm chấm sau đó kéo theo.

**Quy tắc:** hệ số nhóm = tổng giờ ước trực tiếp của các việc mẫu trong nhóm ÷ tổng SWP của chúng. Giờ leaf task = SWP × hệ số nhóm, làm tròn 0,5 giờ (tối thiểu 0,5); epic và issue cha = tổng giờ việc con. Giờ là công làm của một người đúng vai: đọc spec, làm, tự kiểm theo DoD, sửa sau review — không gồm dự phòng, chờ khách trả lời, quản lý dự án. Leaf task nào quá 24 giờ (3 ngày công) sau khi quy giờ thì tách tiếp (luật G1 ở task-breakdown.md).

**Áp dụng nhất quán:** một script tính giờ cho mọi leaf task từ SWP đã chốt (trừ hai loại ngoại lệ nêu dưới bảng) và ghi lên trường giờ ước lượng của Project; đọc lại trường này so với bảng giờ, lệch 0.

| Nhóm việc | Hệ số (giờ/SWP) | Việc mẫu | Leaf task | SWP | Giờ (đã gồm ngoại lệ) |
|---|---|---|---|---|---|
| Backend, DB, hạ tầng, tích hợp | 3,24 | 20 | 165 | 748 | 2.380 |
| Giao diện | 4,18 | 8 | 58 | 226 | 939 |
| Kiểm thử | 5,71 | 4 | 55 | 182 | 1.037,5 |
| Làm rõ với khách | 2,45 | 8 | 32 | 59 | 147 |

**Ngoại lệ 1 — giờ ước trực tiếp:** 26 leaf task của ba epic có chênh lớn nhất với estimate LAB-1 ([E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15), [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25), [E-44](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/24)) được ước lại trực tiếp từng việc, theo từng bước (đọc spec, làm, kiểm thử theo DoD, sửa sau review), không xem SWP và giờ cũ; giờ ước trực tiếp thay giờ quy từ SWP: 332,5 giờ → 334,5 giờ (khoảng 244,5–465,5 giờ). Bốn việc khác trong đợt ước lại đã được tách sau đó, nên phần tách dùng hệ số. Việc có độ tin cậy thấp là chỗ spec còn để ngỏ, nêu ở rủi ro của progress-report.md.

**Ngoại lệ 2 — Sprint 1 đã chạy:** 32 leaf task của Sprint 1 giữ giờ ước lúc lập kế hoạch (389,5 giờ; theo hệ số mới là 417 giờ), vì việc đã làm xong hoặc đang làm thì không ước lại. Hai việc trong số này quá 24 giờ ([I-012.1](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/160), [I-036](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/46)) nhưng không tách vì đang làm hoặc đã xong.

| Việc | Giờ quy từ SWP | Giờ ước trực tiếp | Khoảng | Độ tin cậy |
|---|---|---|---|---|
| [#84](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/84) I-203 Dựng hàm kiểm cấm đảo ngày hạn dùng chung | 13 | 15 | 11–21 | vừa |
| [#92](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/92) I-291 Làm rõ nghĩa quy tắc 1/3 với khách | 2,5 | 3 | 2–5 | cao |
| [#93](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/93) I-292 Làm rõ đơn vị so sánh của cấm đảo ngày hạn: theo khách hay theo điểm nhận | 2,5 | 3 | 2–5 | vừa |
| [#97](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/97) I-296 Làm rõ mốc so sánh của phép cấm đảo ngày hạn | 2,5 | 2,5 | 2–4 | cao |
| [#135](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/135) I-495 Làm rõ mẫu tám báo cáo chưa dựng và quyền xem báo cáo với khách | 7,5 | 5 | 3,5–8 | vừa |
| [#137](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/137) I-502 Sửa API cấu hình luật: bỏ ba route sửa thẳng ngưỡng nhiệt, loại hạn và quy tắc hợp đồng | 9,5 | 5 | 4–8 | cao |
| [#138](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/138) I-503 Làm rõ cách xử lý SKU mới duyệt xong nhưng chưa có phiên bản loại hạn | 2,5 | 3 | 2–4,5 | cao |
| [#139](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/139) I-504 Làm rõ nơi khai ngưỡng duyệt hai cấp của điều chỉnh kiểm kê | 2,5 | 2,5 | 2–4 | cao |
| [#140](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/140) I-505 Làm rõ ngày bắt đầu và ngày cuối hiệu lực của phiên bản cấu hình và dữ liệu chủ | 2,5 | 3 | 2–5 | cao |
| [#204](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/204) I-201.1 Mở rộng API danh sách, tạo đơn xuất và dựng API lô nhập ERP | 13 | 17 | 13–23 | vừa |
| [#205](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/205) I-201.2 Dựng giao diện danh sách và tạo đơn xuất | 12,5 | 12,5 | 9–17 | cao |
| [#206](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/206) I-202.1 Mở rộng API chi tiết đơn xuất và dựng API chốt số lượng giao | 16 | 18 | 14–25 | vừa |
| [#207](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/207) I-202.2 Dựng giao diện phân bổ lô và lý do loại trừ | 21 | 24 | 18–32 | vừa |
| [#210](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/210) I-202.5 Dựng API chạy phân bổ và ghi vết lần đánh giá | 19,5 | 22,5 | 16–30 | vừa |
| [#211](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/211) I-202.6 Áp bước cấm đảo ngày hạn và thứ tự FEFO, FIFO vào hàm phân bổ | 9,5 | 10 | 7–14 | cao |
| [#277](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/277) I-409.1 Dựng API và hàm DB cho màn trung tâm báo cáo | 19,5 | 21 | 15–28 | vừa |
| [#278](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/278) I-409.2 Dựng giao diện cho màn trung tâm báo cáo | 16,5 | 11 | 8–15 | cao |
| [#280](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/280) I-410.2 Dựng giao diện cho màn xuất bằng chứng audit | 16,5 | 16 | 12–22 | vừa |
| [#281](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/281) I-410.3 Áp luật manifest ổn định và loại gói lệch manifest cho màn xuất bằng chứng audit | 9,5 | 16,5 | 11–26 | thấp |
| [#282](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/282) I-410.4 Viết bộ kiểm thử cho màn xuất bằng chứng audit | 17 | 19,5 | 14–27 | vừa |
| [#283](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/283) I-410.5 Dựng API và hàm DB liệt kê, tải và tái tạo gói cho màn xuất bằng chứng audit | 16 | 13,5 | 10–19 | vừa |
| [#284](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/284) I-501.1 Dựng API đọc cấu hình luật và phiên bản ngưỡng nhiệt, loại hạn của SKU | 26 | 20 | 15–27 | vừa |
| [#285](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/285) I-501.2 Dựng giao diện khối ngưỡng nhiệt và loại hạn SKU cho màn cấu hình luật nghiệp vụ | 16,5 | 15 | 11–20 | vừa |
| [#286](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/286) I-501.3 Áp luật vòng đời phiên bản cấu hình: lập khác duyệt, không chồng hiệu lực | 16 | 22,5 | 16–30 | vừa |
| [#288](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/288) I-501.5 Dựng API phiên bản quy tắc cửa sổ hạn giao và bộ tham số giờ lái, HACCP | 26 | 18 | 13–24 | vừa |
| [#289](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/289) I-501.6 Dựng giao diện khối cửa sổ hạn giao và hai bộ tham số cho màn cấu hình luật nghiệp vụ | 16,5 | 15,5 | 12–22 | vừa |

40 việc ước giờ trực tiếp dùng để tính hệ số:

| Issue | Nguồn | Nhóm | SWP lúc ước | Giờ ước | Giờ/SWP |
|---|---|---|---|---|---|
| [#77](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/77) [I-191] Làm rõ ai được xem đợt kiểm kê và danh sách điều chỉnh với khách | 10 issue mẫu (phase 05) | Làm rõ với khách | 1 | 2,5 | 2,5 |
| [#43](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/43) [I-033] Dựng hàm kiểm quyền theo dòng dùng chung cho tuyến của tài xế và tệp chứng cứ | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 3 | 8 | 2,67 |
| [#41](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/41) [I-031] Áp ma trận quyền bảy vai trò và kiểm tự động ma trận với mã nguồn | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 14 | 2,8 |
| [#172](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/172) [I-101.1] Dựng API và hàm DB cho màn danh sách lịch hẹn nhập và quản lý dòng hàng | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 8 | 24 | 3 |
| [#108](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/108) [I-326] Dựng hàm phát hành tuyến: khoá tài xế, kiểm lại năm nhóm và ghi sổ giờ | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 10 | 20 | 2 |
| [#47](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/47) [I-037] Dựng thành phần giao diện bảng dữ liệu, bộ lọc và ô chọn dữ liệu chủ dùng chung | 10 issue mẫu (phase 05) | Giao diện | 4 | 22 | 5,5 |
| [#219](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/219) [I-206.2] Dựng giao diện ghi nhận giao hàng cho tài xế | 10 issue mẫu (phase 05) | Giao diện | 6 | 26 | 4,33 |
| [#177](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/177) [I-102.4] Viết bộ kiểm thử cho màn kiểm hàng nhập từng dòng | 10 issue mẫu (phase 05) | Kiểm thử | 4 | 20 | 5 |
| [#157](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/157) [I-010.2] Tạo migration bảng mới miền nhập kho và tồn kho | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 4 | 13 | 3,25 |
| [#3](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/3) [I-002] Lập CI chạy migration, test TypeScript và test hàm Postgres cho mỗi lần đẩy mã | 10 issue mẫu (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 15 | 3 |
| [#204](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/204) [I-201.1] Mở rộng API danh sách, tạo đơn xuất và dựng API lô nhập ERP | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 4 | 17 | 4,25 |
| [#205](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/205) [I-201.2] Dựng giao diện danh sách và tạo đơn xuất | 30 việc ước lại (phase 05) | Giao diện | 3 | 12,5 | 4,17 |
| [#206](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/206) [I-202.1] Mở rộng API chi tiết đơn xuất và dựng API chốt số lượng giao | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 18 | 3,6 |
| [#207](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/207) [I-202.2] Dựng giao diện phân bổ lô và lý do loại trừ | 30 việc ước lại (phase 05) | Giao diện | 5 | 24 | 4,8 |
| [#208](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/208) [I-202.3] Áp các bước loại trừ hạn, dải nhiệt, cách ly và cửa sổ hạn giao vào hàm phân bổ | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 8 | 24,5 | 3,06 |
| [#209](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/209) [I-202.4] Viết bộ kiểm thử cho màn phân bổ lô và lý do loại trừ | 30 việc ước lại (phase 05) | Kiểm thử | 6 | 30 | 5 |
| [#210](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/210) [I-202.5] Dựng API chạy phân bổ và ghi vết lần đánh giá | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 6 | 22,5 | 3,75 |
| [#211](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/211) [I-202.6] Áp bước cấm đảo ngày hạn và thứ tự FEFO, FIFO vào hàm phân bổ | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 3 | 10 | 3,33 |
| [#84](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/84) [I-203] Dựng hàm kiểm cấm đảo ngày hạn dùng chung | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 4 | 15 | 3,75 |
| [#92](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/92) [I-291] Làm rõ nghĩa quy tắc 1/3 với khách | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 3 | 3 |
| [#93](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/93) [I-292] Làm rõ đơn vị so sánh của cấm đảo ngày hạn: theo khách hay theo điểm nhận | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 3 | 3 |
| [#97](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/97) [I-296] Làm rõ mốc so sánh của phép cấm đảo ngày hạn | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 2,5 | 2,5 |
| [#277](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/277) [I-409.1] Dựng API và hàm DB cho màn trung tâm báo cáo | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 6 | 21 | 3,5 |
| [#278](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/278) [I-409.2] Dựng giao diện cho màn trung tâm báo cáo | 30 việc ước lại (phase 05) | Giao diện | 4 | 11 | 2,75 |
| [#279](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/279) [I-410.1] Dựng API và hàm DB tạo và dựng gói cho màn xuất bằng chứng audit | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 32 | 6,4 |
| [#280](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/280) [I-410.2] Dựng giao diện cho màn xuất bằng chứng audit | 30 việc ước lại (phase 05) | Giao diện | 4 | 16 | 4 |
| [#281](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/281) [I-410.3] Áp luật manifest ổn định và loại gói lệch manifest cho màn xuất bằng chứng audit | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 3 | 16,5 | 5,5 |
| [#282](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/282) [I-410.4] Viết bộ kiểm thử cho màn xuất bằng chứng audit | 30 việc ước lại (phase 05) | Kiểm thử | 3 | 19,5 | 6,5 |
| [#283](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/283) [I-410.5] Dựng API và hàm DB liệt kê, tải và tái tạo gói cho màn xuất bằng chứng audit | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 13,5 | 2,7 |
| [#135](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/135) [I-495] Làm rõ mẫu tám báo cáo chưa dựng và quyền xem báo cáo với khách | 30 việc ước lại (phase 05) | Làm rõ với khách | 3 | 5 | 1,67 |
| [#284](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/284) [I-501.1] Dựng API đọc cấu hình luật và phiên bản ngưỡng nhiệt, loại hạn của SKU | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 8 | 20 | 2,5 |
| [#285](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/285) [I-501.2] Dựng giao diện khối ngưỡng nhiệt và loại hạn SKU cho màn cấu hình luật nghiệp vụ | 30 việc ước lại (phase 05) | Giao diện | 4 | 15 | 3,75 |
| [#286](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/286) [I-501.3] Áp luật vòng đời phiên bản cấu hình: lập khác duyệt, không chồng hiệu lực | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 5 | 22,5 | 4,5 |
| [#287](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/287) [I-501.4] Viết bộ kiểm thử cho màn cấu hình luật nghiệp vụ | 30 việc ước lại (phase 05) | Kiểm thử | 4 | 27,5 | 6,88 |
| [#288](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/288) [I-501.5] Dựng API phiên bản quy tắc cửa sổ hạn giao và bộ tham số giờ lái, HACCP | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 8 | 18 | 2,25 |
| [#289](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/289) [I-501.6] Dựng giao diện khối cửa sổ hạn giao và hai bộ tham số cho màn cấu hình luật nghiệp vụ | 30 việc ước lại (phase 05) | Giao diện | 4 | 15,5 | 3,88 |
| [#137](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/137) [I-502] Sửa API cấu hình luật: bỏ ba route sửa thẳng ngưỡng nhiệt, loại hạn và quy tắc hợp đồng | 30 việc ước lại (phase 05) | Backend, DB, hạ tầng, tích hợp | 3 | 5 | 1,67 |
| [#138](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/138) [I-503] Làm rõ cách xử lý SKU mới duyệt xong nhưng chưa có phiên bản loại hạn | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 3 | 3 |
| [#139](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/139) [I-504] Làm rõ nơi khai ngưỡng duyệt hai cấp của điều chỉnh kiểm kê | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 2,5 | 2,5 |
| [#140](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/140) [I-505] Làm rõ ngày bắt đầu và ngày cuối hiệu lực của phiên bản cấu hình và dữ liệu chủ | 30 việc ước lại (phase 05) | Làm rõ với khách | 1 | 3 | 3 |

## 3. Tổng theo epic

| Epic | Số issue (leaf task) | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| [E-01](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/1) Dựng hạ tầng, môi trường và vận hành | 4 | 24 | 68 | 4 issue, 0 sub-issue |
| [E-02](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/6) Dựng dữ liệu nền: schema đích và dữ liệu khởi tạo | 18 | 83 | 260 | 11 issue, 13 sub-issue |
| [E-03](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/7) Dựng khung ứng dụng, phân quyền và audit | 12 | 47 | 162,5 | 12 issue, 0 sub-issue |
| [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8) Dựng job nền và hàm nghiệp vụ dùng chung | 13 | 53 | 183 | 8 issue, 7 sub-issue |
| [E-05](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/9) Dựng tích hợp ngoài và thông báo | 8 | 31 | 95 | 8 issue, 0 sub-issue |
| [E-06](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/323) Kiểm chứng phi chức năng và kiểm thử hệ thống | 31 | 111 | 522 | 14 issue, 24 sub-issue |
| [E-11](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/10) Dựng lịch hẹn nhập và nhận hàng có kiểm nhiệt | 14 | 57 | 213,5 | 4 issue, 13 sub-issue |
| [E-12](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/11) Dựng phân tách số lượng nhận và duyệt chênh lệch | 7 | 26 | 96,5 | 2 issue, 6 sub-issue |
| [E-13](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/12) Dựng tra cứu tồn kho và cất kho | 7 | 25 | 90,5 | 4 issue, 5 sub-issue |
| [E-14](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/13) Dựng vòng trạng thái lô: cách ly, giải phóng, tiêu huỷ | 4 | 16 | 65 | 1 issue, 4 sub-issue |
| [E-15](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/14) Dựng kiểm kê mù và điều chỉnh chênh lệch | 9 | 34 | 125 | 4 issue, 7 sub-issue |
| [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) Dựng đơn xuất và phân bổ | 14 | 50 | 199,5 | 6 issue, 10 sub-issue |
| [E-22](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/16) Dựng soạn hàng và nạp xe | 9 | 33 | 122 | 4 issue, 7 sub-issue |
| [E-23](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/17) Dựng giao hàng và ghi nhận giao hàng (POD) | 7 | 31 | 116,5 | 1 issue, 7 sub-issue |
| [E-24](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/18) Dựng lịch sử giao, sự kiện đảo và khiếu nại | 8 | 28 | 95 | 6 issue, 4 sub-issue |
| [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19) Dựng lập tuyến và lịch trình tài xế | 12 | 48 | 178 | 4 issue, 11 sub-issue |
| [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20) Ràng buộc giờ lái 2024 | 27 | 104 | 386 | 18 issue, 12 sub-issue |
| [E-41](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/21) Dựng theo dõi nhiệt độ và hàng đợi alarm | 15 | 58 | 220 | 5 issue, 12 sub-issue |
| [E-42](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/22) Dựng hồ sơ sai lệch và hồ sơ HACCP | 16 | 64 | 240 | 4 issue, 14 sub-issue |
| [E-43](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/23) Dựng truy xuất và thu hồi | 15 | 60 | 239 | 3 issue, 15 sub-issue |
| [E-44](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/24) Dựng báo cáo và gói bằng chứng audit | 9 | 34 | 121,5 | 3 issue, 8 sub-issue |
| [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25) Dựng cấu hình luật nghiệp vụ | 11 | 41 | 138,5 | 5 issue, 7 sub-issue |
| [E-52](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/26) Dựng quản lý dữ liệu chủ | 17 | 57 | 211,5 | 7 issue, 16 sub-issue |
| [E-53](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/27) Dựng chuyển dữ liệu và theo dõi tích hợp | 10 | 44 | 153,5 | 3 issue, 9 sub-issue |
| [E-54](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/28) Dựng người dùng, vai trò và nhật ký audit | 4 | 14 | 53,5 | 3 issue, 2 sub-issue |
| [E-55](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/29) Dựng lưu giữ dữ liệu, legal hold và purge | 9 | 42 | 148 | 2 issue, 8 sub-issue |
| **Cộng** | **310** | **1215** | **4.503,5** | |

Kiểm năng lực:

- Đội làm issue (backend, frontend, kiểm thử, hạ tầng, BrSE) có 739 giờ mỗi sprint: đội hình estimate LAB-1 cộng một frontend (FE-2, từ Sprint 1) và hai backend (BE-4, BE-5, từ Sprint 2).
- Chia tổng giờ: 4.503,5 ÷ 739 ≈ 6,1 sprint, nằm trong 8,6 sprint quy đổi của giai đoạn xây dựng (Sprint 3 trùng kỳ nghỉ đầu năm của Nhật 29/12–3/1 nên tính 60 %).
- Phép chia này chưa đủ: giờ tính cho người đúng vai, nên khi xếp từng việc theo phụ thuộc chỉ chuyển việc trong cùng chuyên môn (backend với backend, frontend với frontend); ngoại lệ là backend viết kiểm thử tự động, trưởng nhóm backend làm hạ tầng, trưởng nhóm frontend làm hệ thống thiết kế, quản lý dự án thay BrSE làm rõ với khách. Với luật này đội hình LAB-1 cần 13 sprint; thêm FE-2 còn 13 sprint; thêm FE-2 và một backend còn 11 sprint.
- Thêm FE-2 từ Sprint 1 và BE-4, BE-5 từ Sprint 2 (thêm 1.523,2 giờ, tức 190,4 MD so với đội hình LAB-1) thì kế hoạch vừa 9 sprint: việc cuối xong ngày làm việc thứ 87,1 trên 90 (buffer khoảng 2,9 ngày); Sprint 9 dùng 56 % năng lực backend, 26 % frontend, 67 % kiểm thử. Sprint 1 đã chạy trước khi thêm hai backend nên giữ nguyên cách giao việc lúc đó (frontend làm một số migration khi chưa có API để dựng màn).
- Sprint của từng issue xem ở trường Iteration trên GitHub Project; tình hình sau Sprint 1 và rủi ro trễ ở progress-report.md.

## 4. So với estimate LAB-1

Đơn vị: LAB-1 tính ngày công (MD) theo vai, 1 MD = 8 giờ; LAB-5 tính giờ theo issue. Ba lý do chung cho mọi dòng: (1) MD của LAB-1 đã gồm 15 % dự phòng, giờ LAB-5 không có; (2) gói xây dựng của LAB-1 có cột thiết kế giao diện, phần này đã làm xong ở bộ thiết kế chi tiết; (3) LAB-1 tính kiểm thử trong từng gói, LAB-5 gom kiểm thử hệ thống về [E-06](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/323). Dòng ghi "(ước)" là số LAB-1 chia theo trọng số màn, không phải số WBS nêu thẳng.

| Phần (epic) | LAB-1 MD | LAB-1 giờ | LAB-5 giờ | Chênh giờ | Vì sao |
|---|---|---|---|---|---|
| [E-02](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/6) Dựng dữ liệu nền: schema đích và dữ liệu khởi tạo | — | — | 260 | — | LAB-1 không có gói dựng bảng riêng: công dựng dữ liệu nằm rải trong cột Backend của từng gói chức năng. LAB-5 gom việc dựng toàn bộ bảng thiết kế đích về một epic nền nên không gán số LAB-1. |
| [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8) Dựng job nền và hàm nghiệp vụ dùng chung | — | — | 183 | — | LAB-1 không có gói riêng: các hàm dùng chung (cách ly, gom đợt alarm, lịch ca HACCP, đề xuất purge) nằm trong cột Backend của gói gọi chúng. LAB-5 tách thành một epic để mỗi hàm chỉ dựng một lần; phần này làm các epic chức năng thấp hơn LAB-1. |
| [E-05](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/9) Dựng tích hợp ngoài và thông báo | 51,75 | 414 | 95 | -319 | Gói 3.2 tính sáu giao diện tích hợp kể cả phần chờ khách trả lời câu hỏi tích hợp. LAB-5 chuyển đăng nhập doanh nghiệp sang [E-03](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/7), nạp CSV logger sang [E-41](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/21), màn theo dõi tích hợp sang [E-53](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/27), hàm xếp thông báo sang [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8); [E-05](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/9) chỉ còn nhận file ERP qua SFTP theo lịch (PREMISE.md P1-01), job gửi thư cho ba loại sự kiện (P1-05, P1-06) và làm rõ đặc tả file. |
| [E-11](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/10) Dựng lịch hẹn nhập và nhận hàng có kiểm nhiệt | 46 | 368 | 213,5 | -154,5 | Số LAB-1 là phần chia của gói 2.2 và 2.3 theo trọng số màn (ước). Hàm cách ly dùng chung tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8); giả định nhập kho của PREMISE.md P2-16, P2-17 giữ phạm vi màn như bộ thiết kế, không thêm việc. |
| [E-12](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/11) Dựng phân tách số lượng nhận và duyệt chênh lệch | 21,16 | 169,28 | 96,5 | -72,78 | Phần chia của gói 2.2 theo trọng số màn (ước). Nguồn thông báo duyệt chênh lệch (P1-06) thêm một ít việc nhưng hàm xếp thông báo tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8). |
| [E-13](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/12) Dựng tra cứu tồn kho và cất kho | 21,39 | 171,12 | 90,5 | -80,62 | Phần chia của gói 2.3 theo trọng số màn (ước). Giả định một lô một vị trí (PREMISE.md P2-18) làm luật cất kho đơn giản hơn. |
| [E-14](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/13) Dựng vòng trạng thái lô: cách ly, giải phóng, tiêu huỷ | 14,26 | 114,08 | 65 | -49,08 | Phần chia của gói 2.3 theo trọng số màn (ước); hàm cách ly dùng chung tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8). |
| [E-15](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/14) Dựng kiểm kê mù và điều chỉnh chênh lệch | 21,39 | 171,12 | 125 | -46,12 | Phần chia của gói 2.3 theo trọng số màn (ước). Ngưỡng duyệt hai cấp theo giả định tạm (PREMISE.md P2-15) không thêm việc. |
| [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) Dựng đơn xuất và phân bổ | 82,8 | 662,4 | 199,5 | -462,9 | LAB-1 cho [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) trọn cột Backend và QA của gói Rule Engine 2.4 (55,20 MD) — bộ luật hạn, FEFO, cấm đảo ngày hạn, cửa sổ giao — cộng phần chia của gói 2.5. Ở LAB-5 các hàm luật nằm ở [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) nhưng kiểm thử hệ thống ở [E-06](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/323) và cấu hình luật có phiên bản ở [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25); nên so cặp [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) + [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25). |
| [E-22](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/16) Dựng soạn hàng và nạp xe | 27,6 | 220,8 | 122 | -98,8 | Phần chia của gói 2.5 theo trọng số màn (ước). |
| [E-23](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/17) Dựng giao hàng và ghi nhận giao hàng (POD) | 18,4 | 147,2 | 116,5 | -30,7 | Phần chia của gói 2.5 theo trọng số màn (ước). Ba luồng ngoại lệ xuất kho chưa làm, chờ khách (PREMISE.md P2-02), nên ít việc hơn. |
| [E-24](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/18) Dựng lịch sử giao, sự kiện đảo và khiếu nại | 16,67 | 133,36 | 95 | -38,36 | Phần chia của gói 2.1 và 2.5 (ước). Lịch sử giao bất biến dùng cơ chế chỉ thêm dựng chung ở [E-02](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/6). |
| [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19) Dựng lập tuyến và lịch trình tài xế | 35,93 | 287,44 | 178 | -109,44 | LAB-1 chia gói 2.6 theo trọng số màn và tính trọn phần giờ lái của màn lập tuyến, lịch trình tài xế cho [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19); LAB-5 tách hết phần giờ lái sang [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20). So cặp [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19) + [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20) thì hai bản gần khớp. |
| [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20) Ràng buộc giờ lái 2024 | 28,47 | 227,76 | 386 | 158,24 | Cao hơn LAB-1 vì nhận phần giờ lái mà LAB-1 tính ở [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19) (xem dòng [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19)), cộng việc mới do tiền đề: chọn bộ quy tắc theo thời điểm phát hành, không hồi tố (PREMISE.md P1-03, P3-02), số dư đầu kỳ của sổ giờ (P2-06), cách so nghỉ giữa ca khi chỉ một phía có ca (P2-21). Số LAB-1 của [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20) là phần chia (ước) của gói 2.6 nên chỉ là cận dưới; so cặp [E-31](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/19) + [E-32](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/20) mới có ý nghĩa: LAB-1 515,2 giờ, LAB-5 564 giờ. |
| [E-41](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/21) Dựng theo dõi nhiệt độ và hàng đợi alarm | 31,05 | 248,4 | 220 | -28,4 | Phần chia của gói 2.7 (ước). Job đối soát và gom đợt alarm tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8); thông báo alarm quá hạn xem xét là việc mới (PREMISE.md P1-06, P2-04) nhưng nhỏ. |
| [E-42](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/22) Dựng hồ sơ sai lệch và hồ sơ HACCP | 31,05 | 248,4 | 240 | -8,4 | Phần chia của gói 2.7 (ước); hàm lịch ca HACCP tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8). Hai nhóm hồ sơ chỉ khai thời hạn lưu (PREMISE.md P2-08) không thêm màn. |
| [E-43](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/23) Dựng truy xuất và thu hồi | 54,05 | 432,4 | 239 | -193,4 | Gói 2.8 tính trọn truy xuất và thu hồi. LAB-5 thu hẹp case thu hồi về một lô mỗi case (PREMISE.md P2-20); kiểm thời gian truy xuất lô 3 năm chuyển sang [E-06](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/323). |
| [E-44](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/24) Dựng báo cáo và gói bằng chứng audit | 50,6 | 404,8 | 121,5 | -283,3 | LAB-1 tính đủ 12 loại báo cáo (khoảng 0,9 MD mỗi loại); bộ thiết kế chi tiết dựng 4 loại, hai báo cáo tách sang nhóm chờ khách (PREMISE.md P2-10); job xuất bằng chứng theo lịch lưu giữ tính ở [E-04](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/8) (P1-14). Dự phòng 15 % giải thích khoảng 53 giờ, việc bớt 8 loại báo cáo khoảng 58 giờ (8 × 0,9 MD); phần còn lại không truy được về một thay đổi phạm vi cụ thể. Bất định lớn nhất nằm ở màn xuất bằng chứng audit (rủi ro ở progress-report.md). |
| [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25) Dựng cấu hình luật nghiệp vụ | 10,35 | 82,8 | 138,5 | 55,7 | LAB-1 chỉ cho [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25) cột Frontend và thiết kế của gói 2.4 (10,35 MD); LAB-5 gồm cả API và hàm của cấu hình luật có phiên bản, thay việc sửa thẳng cấu hình (PREMISE.md P1-08). Xem cùng [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15). Cặp [E-21](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/15) + [E-51](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/25): LAB-1 93,15 MD (745,2 giờ), LAB-5 338 giờ, chênh -407,2 giờ, trong đó dự phòng 15 % của LAB-1 khoảng 97 giờ. Hai epic này có nhiều việc ước giờ trực tiếp (mục 2); vì ước từng việc vẫn ra mức này, phần chênh còn lại nhiều khả năng nằm ở cách LAB-1 phân bổ cả gói 2.4 theo trọng số màn, không phải LAB-5 bỏ sót việc. |
| [E-52](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/26) Dựng quản lý dữ liệu chủ | 37,38 | 299,04 | 211,5 | -87,54 | Phần chia của gói 2.1 (ước). Bảo trì tài xế, xe, khung giờ giao là việc mới (PREMISE.md P1-02, P2-01) nhưng không bù phần dự phòng và thiết kế của LAB-1; lịch sử giao bất biến tính ở [E-24](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/18). |
| [E-53](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/27) Dựng chuyển dữ liệu và theo dõi tích hợp | 48,3 | 386,4 | 153,5 | -232,9 | Gói 4.1 gồm hai lần diễn tập và lần tải chính thức — việc vận hành giai đoạn chuyển đổi, không phải issue xây dựng; backlog chỉ có công cụ chuyển dữ liệu, màn đối soát và màn theo dõi tích hợp (cột tệp nguồn theo giả định PREMISE.md P2-07). |
| [E-55](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/29) Dựng lưu giữ dữ liệu, legal hold và purge | 12 | 96 | 148 | 52 | LAB-1 tách 12,00 MD theo ghi chú WBS cho lưu giữ dữ liệu; LAB-5 làm đủ legal hold, purge có duyệt và hàm xoá theo từng nhóm hồ sơ (9 leaf task) nên cao hơn. |
| [E-01](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/1) + [E-03](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/7) + [E-06](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/323) + [E-54](https://github.com/trungbx-20131/yuki-cold-wms-mng/issues/28) (so một dòng) | 82,3 | 658,4 | 806 | 147,6 | Gói 3.1 phần còn lại và 3.3 (bảo mật, hiệu năng, BCP, giám sát, WCAG, bản địa hoá) so một dòng với hạ tầng, khung ứng dụng, kiểm chứng phi chức năng và quản trị người dùng: LAB-5 chênh 147,6 giờ (khoảng 22 %), chủ yếu vì hệ số giờ kiểm thử đã hiệu chỉnh và các việc kiểm chứng phi chức năng được tách nhỏ (PREMISE.md P1-15). |
| **Cộng phần so được** | **742,9** | **5.943,2** | **4.503,5** | **-1.439,7** | Tách theo vai ở bảng dưới: dự phòng 15 % và thiết kế chiếm phần lớn khoảng chênh; phần còn lại do LAB-5 ước theo leaf task (không gồm phối hợp, sửa lỗi sau kiểm thử hệ thống) và các thu hẹp phạm vi đã nêu ở PREMISE.md. |
| Gói không có issue (1.1, 5.1, 5.2, 5.3, 6.1) | 313,95 | 2.511,6 | không có issue | — | Thiết kế cơ bản, hỗ trợ UAT, đào tạo, hypercare và quản lý dự án không có issue trong backlog xây dựng. |

Tách khoảng chênh theo vai (các gói so được):

| Vai | LAB-1 giờ (MD × 8) | LAB-1 giờ bỏ dự phòng 15 % | LAB-5 giờ | Chênh sau khi bỏ dự phòng |
|---|---|---|---|---|
| Backend (gồm DB, tích hợp) | 2.833,6 | 2.464 | 2.260,5 | -203,5 |
| Frontend | 1.214,4 | 1.056 | 939 | -117 |
| Thiết kế giao diện | 377,2 | 328 | 0 | -328 |
| Kiểm thử | 1.223,6 | 1.064 | 1.037,5 | -26,5 |
| Hạ tầng | 294,4 | 256 | 119,5 | -136,5 |
| Làm rõ với khách (BrSE) | 0 | 0 | 147 | 147 |
| **Cộng** | **5.943,2** | **5.168** | **4.503,5** | **-664,5** |
