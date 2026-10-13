# Báo cáo dùng AI — LAB-5 (Yuki Cold WMS)

Phạm vi: toàn bộ LAB-5 — break task từ bộ thiết kế LAB-4, dựng GitHub Project, chấm SWP, quy giờ, lập kế hoạch sprint, giả lập Sprint 1 và lập báo cáo tiến độ. Thực hiện 2026-10-12 → 2026-10-13 trên hai máy, công cụ chính là Claude Code. Mỗi ca AI sai, giữ hoặc bác được ghi vào sổ ca ngay khi xảy ra; báo cáo này tổng hợp từ sổ đó: 72 ca, gồm 36 ca AI sai đã sửa, 19 ca nghi sai nhưng kiểm rồi giữ, 6 ca bác gợi ý, 6 góp ý của agent review, 4 ca ngữ cảnh nhiễu và 1 lần hỏi dùng skill Takumi.

## 1. Skill đã dùng và cách viết prompt cho từng việc

### 1.1 Thử nghiệm của lab này: dùng bộ skill Takumi ở mức tối thiểu

Ở LAB-1 đến LAB-4, bộ skill Takumi được dùng tối đa. LAB-5 thử ngược lại để so chất lượng, thời gian và mức kiểm soát:

- Mặc định không dùng skill hay agent Takumi. Việc làm bằng công cụ cơ bản của Claude Code (đọc, sửa, chạy lệnh), agent `general-purpose`, `gh` CLI, GraphQL của GitHub và script Python viết riêng cho bài.
- Muốn dùng một skill Takumi thì phải hỏi người làm lab trước, nêu dùng gì, để làm gì, vì sao làm tay không đủ.
- Chỉ một skill được duyệt: **`tkm:sun-estimate`** ở bước chấm SWP, vì đề bắt chấm bằng skill.
- Skill chấm SWP gợi ý nạp thêm hai skill phụ (chấm độ tin cậy, tra cứu chuyên gia); không nạp, vì skill có sẵn đường lui dùng định nghĩa nội bộ.

### 1.2 Cách giao việc cho agent

- **Năm vai**, mỗi vai một thẻ mô tả nhiệm vụ, file được ghi và checklist chất lượng: phân tích spec, tách task, quản lý dự án (vai duy nhất được ghi lên GitHub), đóng gói, review độc lập.
- **Chạy song song theo lát**: backlog chia 6 lát theo nhóm màn. Mỗi agent một lát với dải mã issue riêng; file gộp chỉ sinh bằng script, không agent nào sửa file gộp.
- **Mẫu prompt cố định**, gồm: vai và thẻ vai · phase và việc (1–3 câu) · file đọc, file được ghi · tiêu chí xong · ràng buộc (không dùng Takumi, không sửa file vai khác) · ngôn ngữ. Dòng ngôn ngữ được thêm sau một ca agent viết tin nhắn kết thúc bằng tiếng Đức: đối chiếu 7 agent cùng đợt, agent đó là prompt duy nhất thiếu dòng "viết bằng tiếng Việt".
- Agent làm xong phải chép checklist vào báo cáo, tự soát từng dòng kèm bằng chứng; phiên chính chạy lại ít nhất ba dòng bất kỳ trước khi nhận.

### 1.3 Từng việc

| Việc | Công cụ | Cách giao / prompt | Đầu ra được kiểm bằng |
|---|---|---|---|
| Đọc bộ LAB-4, tìm chỗ hở | 6 agent phân tích (mỗi lát một agent) + 1 agent tổng hợp | Đọc danh mục spec của lát, liệt kê màn, endpoint, câu hỏi khách còn mở và chỗ hở; mỗi chỗ hở trích `file:dòng` | Script kiểm mọi trích dẫn `file:dòng` (thêm sau hai ca lệch một dòng); agent tổng hợp đối chiếu chéo giữa lát |
| Break task | 1 agent dựng khung chung trước, rồi 6 agent tách task song song | Khung gồm luật độ hạt, động từ tiêu đề, định nghĩa xong theo loại việc, phần dùng chung. Mỗi agent tách lát của mình thành JSON: mục tiêu, spec nguồn, định nghĩa xong, nhãn, vai gợi ý, phụ thuộc, ràng buộc | Script gộp: dải mã, cha–con, vòng phụ thuộc, trùng tiêu đề; review parity hai chiều spec ↔ issue (mục 2.3) |
| Đẩy lên GitHub Project | Script Python + `gh` + GraphQL | Thử trước trên repo nháp; chạy lại không tạo trùng, không ghi đè trạng thái | Đếm Project = backlog theo epic, issue, sub-issue; cha–con khớp |
| Chấm SWP | `tkm:sun-estimate` + 5 agent chấm theo lô | Skill đọc Project, chia 268 việc lá thành lô ~50 việc; mỗi agent đọc file lô và trả JSON theo hợp đồng của skill. Người làm lab chọn agent đọc file thay cho agent chấm không có công cụ của skill (agent kia cần dán khoảng 460 nghìn ký tự vào prompt) | Bộ kiểm hợp lệ của skill (250/250 việc lá; 18/18 việc lá bổ sung sau); 5 issue mẫu do skill chọn theo luật cố định, đối chiếu với định nghĩa xong và spec, người làm lab chốt từng issue |
| **Agent ghi SWP lên Project** | Phiên Claude Code chính trong vai quản lý dự án, chạy script | Script đọc bảng SWP đã chốt (không đọc số thô của skill), chỉ ghi ô lệch bằng `gh project item-edit`, rồi đọc lại toàn bộ Project; chỉ chạy sau khi người làm lab duyệt issue mẫu | Đọc lại 343 phần tử, lệch 0. Cùng script ghi trường giờ. Ở bước xếp sprint, ghi tuần tự quá chậm (~3 giây một ô) nên đổi sang gộp 25 ô vào một lệnh GraphQL; 729 ô, đọc lại lệch 0 |
| Quy giờ | 1 agent ước giờ trực tiếp + script | Agent ước giờ 10 issue mẫu **không được xem SWP** (tránh bị điểm kéo theo), ghi khoảng và lý do theo từng bước việc; script tính hệ số giờ/SWP theo nhóm và quy cho mọi việc lá | Tổng giờ trên Project = file giờ chốt, lệch 0 |
| Xếp sprint, giả lập sprint, báo cáo tiến độ | Phiên chính + script | Script xếp việc theo phụ thuộc và năng lực từng vai; kịch bản Sprint 1 viết thành file dữ liệu **trước** khi cập nhật Project, mỗi chỗ lệch trỏ một câu hỏi khách hoặc chỗ hở thật; script đọc lại Project để sinh bảng trạng thái, burndown và điền số vào mẫu báo cáo viết tay | Script dừng nếu trạng thái trên Project khác kịch bản hoặc thiếu Iteration, vai |

## 2. Review output của AI

### 2.1 Người review ở đâu

| Bước | Người làm gì |
|---|---|
| Chốt hướng trước khi làm | Người làm lab chọn 4 quyết định gốc (phạm vi break, nơi nộp, trường vai giả định, skill chấm SWP) và 6 quyết định thiết kế khi break, mỗi câu có 3 phương án và ảnh hưởng tới backlog |
| Cổng G1 — sau break task | Duyệt backlog sau hai lượt review parity |
| Cổng G2 — chấm SWP | Duyệt từng issue mẫu; sửa một issue (mục 2.4) |
| Giữa chừng | Chọn cách quy giờ; duyệt bổ sung epic phi chức năng; chọn thêm một frontend khi kế hoạch không vừa 9 sprint |
| Cổng G3 — trước khi nộp | Mở repo, Project và báo cáo HTML bằng cửa sổ ẩn danh; duyệt nộp |

### 2.2 Máy kiểm trước, agent review sau

Mọi đầu ra phải qua script trước khi giao agent review, và reviewer không kiểm lại những gì script đã kiểm:

- script gộp lát và đếm;
- script kiểm hợp đồng dữ liệu giữa các phase (một giá trị dùng chung chỉ có một file nguồn);
- cổng repo public: câu chép RFP hoặc đề, khoá bí mật, từ nội bộ, dữ liệu cá nhân, link hỏng;
- đọc lại mọi trường đã ghi lên Project.

Luật review đặt trước lượt đầu: tối đa hai lượt mỗi đầu ra, mỗi phát hiện phải gắn tiêu chí, không chốt luật nghiệp vụ mới để sửa một phát hiện. Cả lab dùng 3 lượt review bằng agent, so với 5 lượt chỉ riêng một gói ở LAB-4.

### 2.3 Review bằng agent

- **Backlog:** 6 agent review song song, mỗi agent một lát, kiểm parity hai chiều (mọi issue có nguồn trong spec, mọi phần spec có issue hoặc có lý do chưa thành issue). Lượt đầu: điểm trung bình 7,3, 4 lỗi Cao (còn 1 sau khi đối chiếu nguồn). Lượt xác nhận sau khi sửa: 8,4, 0 lỗi Cao, đạt cổng nên dừng.
- **Bản gửi khách (README, estimate, báo cáo tiến độ, báo cáo này):** review mù một lần bằng hai agent trên hai model khác nhau, không thấy kết quả của nhau; kết quả ở mục 2.6.

### 2.4 Vấn đề trong output của AI và cách xử lý

| AI sai gì | Phát hiện bằng gì | Xử lý |
|---|---|---|
| **Ba lần đề xuất phương án trái RFP** làm phương án khuyến nghị: chọn bộ quy tắc giờ lái theo ngày chạy tuyến thay vì phiên bản hiệu lực lúc phát hành; chỉ gửi thư cảnh báo, bỏ thư phê duyệt và báo cáo; tải file đơn tay thay vì nhận theo lịch. Người làm lab đã chọn theo đề xuất | Agent viết tiền đề và agent review đối chiếu lại RFP | Chốt lại ba quyết định, sửa tiền đề và lan tới mọi issue chạm thực thể; thêm vào checklist: đối chiếu từng phương án với RFP trước khi trình |
| **Backlog thiếu cả mảng phi chức năng** (kiểm thử tải, WCAG, diễn tập khôi phục, kiểm thử hệ thống, quét bảo mật), dù kế hoạch đã chốt phải phủ; hai lượt review parity không bắt được | So giờ với estimate LAB-1 theo vai, lúc chưa bổ sung: kiểm thử thấp hơn 538 giờ, hạ tầng thấp hơn 191 giờ | Bổ sung epic phi chức năng (21 phần tử), chấm SWP lại cho phần mới bằng cùng luật |
| **Kiểm năng lực theo tổng giờ** ra "7,3 sprint, vừa khung 8,6 sprint" (lúc đó tính 547 giờ mỗi sprint cho các vai làm issue của đội LAB-1; số hiện hành trong estimate.md là 611 giờ, đã gồm frontend bổ sung) | Script xếp từng việc theo vai và phụ thuộc: đội hình LAB-1 cần 10 sprint vì frontend chỉ dựng màn được khi API đã bắt đầu | Người làm lab chọn thêm một frontend toàn thời gian; sửa đội hình ở file nguồn và lan sang estimate.md |
| Phiên chính báo "đội LAB-1 cần 11 sprint" từ một bản thử tính xấp xỉ | Thêm tuỳ chọn để con số chạy lại được bằng script; kết quả là 10 | Sửa về 10 ở mọi chỗ, báo lại người làm lab |
| Skill chấm migration 8 bảng là 12 SWP (cao nhất backlog) | Kiểm issue mẫu với định nghĩa xong: tám bảng một miền là một đợt migration có kiểm soát | Hạ 12 → 10, áp cùng luật cho 6 issue migration cùng nhóm |
| AI nhẩm năng lực cả đội LAB-1 (gồm quản lý dự án, thiết kế) là 654 giờ mỗi sprint | Script cộng lại cùng bảng | 654 → 616 (sau khi thêm một frontend: 680); ghi luôn phép cộng vào bảng để người đọc tự kiểm |
| Script đẩy backlog bản đầu đặt lại mọi trạng thái về Todo mỗi lần chạy lại | Chạy lần hai trên repo nháp sau khi đặt tay một trạng thái | Chỉ đặt trạng thái khi item mới hoặc trạng thái rỗng |
| Trích dẫn `file:dòng` lệch một dòng (hai lần), trích vào dòng lịch sử thay đổi thay vì thân spec (ba chỗ), ghi số liệu từ trí nhớ | Kiểm chéo bằng `grep -n`, in lại dòng thật | Thêm bước kiểm mọi trích dẫn bằng script vào checklist cho mọi lượt sau |
| Email commit của repo nộp tự ghép từ tên máy và tên miền công ty | Kiểm tác giả commit khi một lần commit lỗi | Đổi sang mã học viên và email ẩn danh của GitHub, viết lại hai commit đầu |
| Tên vai nội bộ lọt vào báo cáo HTML nộp | Cổng repo public | Sửa câu chữ, xuất lại báo cáo |

### 2.5 Ca giữ nguyên hoặc bác sau khi kiểm

- **Giữ:** giao thay 36 chỗ một câu định nghĩa xong sai; agent kiểm từng chỗ và giữ 1 chỗ vì ở đó câu cũ đúng với luật giờ lái (36 → 35 chỗ thay).
- **Giữ:** nghi `gh` không tạo được trường Iteration và sub-issue nên đã chuẩn bị đường lui làm tay; chạy thử trên repo nháp thì GraphQL làm được cả hai.
- **Bác:** reviewer đòi ghi phụ thuộc từ mọi issue tới issue câu hỏi khách; bác vì quyết định đã chốt là chỉ gắn thẻ câu hỏi, để việc có giả định tạm không bị khoá chờ cuộc họp với khách.
- **Bác:** agent ánh xạ estimate LAB-1 định chia màn lập tuyến nửa cho epic lập tuyến, nửa cho epic giờ lái theo tỷ lệ tự đặt; bác vì không có nguồn, ghi số LAB-1 của epic giờ lái là cận dưới.
- **Bác:** agent tổng hợp bác kết luận "purge sổ giờ là chỗ hở" của agent lát, vì spec đã có ngoại lệ cho sổ giờ.

### 2.6 Một góp ý review cụ thể và cách xử lý

Ở lượt review parity đầu, reviewer lát nền tảng chỉ ra quyết định "chỉ gửi thư cảnh báo" trái RFP: điểm tích hợp thư của RFP gồm cả thư phê duyệt và thư báo cáo. Phiên chính in lại dòng RFP để kiểm, xác nhận đúng. Người làm lab chốt lại: giữ ba loại thư, người nhận theo giả định tạm (PREMISE.md P2-03), thêm một issue làm rõ với khách. Khi sửa, hai agent tách task lập điểm chạm theo thực thể và thấy danh sách giao sửa còn sót ba hàng đợi duyệt; cả ba được duyệt bổ sung.

Review mù bản gửi khách (phase cuối): _điền sau khi chạy._

## 3. Điểm đặc biệt: chỗ hiệu quả, chỗ cần cải thiện

### 3.1 Takumi tối thiểu so với LAB-4

| Tiêu chí | LAB-4 (Takumi tối đa) | LAB-5 (Takumi tối thiểu) |
|---|---|---|
| Skill Takumi dùng | Nhiều skill quy trình và agent của bộ kit | 1 skill (`tkm:sun-estimate`), hỏi trước khi dùng |
| Giờ có tương tác với AI | 24,0 giờ (17 phiên, 487 prompt) | _điền khi chốt giờ_ (mục 3.4) |
| Ca ghi trong sổ | 406 (256 sửa) | 72 (36 sửa, 19 giữ, 6 bác, 6 góp ý review, 4 nhiễu, 1 hỏi Takumi) |
| Số lượt review bằng agent | 5 lượt cho một gói, điểm không tăng | 3 lượt cho cả lab, có cổng dừng đặt trước |
| Mức kiểm soát | Quy trình của kit quyết định nhiều bước | Mỗi bước do script hoặc người quyết; mọi số trên Project đọc lại được |

Hai lab khác loại việc (thiết kế chi tiết và break task), nên bảng chỉ cho thấy xu hướng, không phải phép đo đối chứng. Điều thấy rõ: khi bỏ các skill quy trình, phải tự viết lại phần khung (thẻ vai, mẫu prompt, luật review, cổng kiểm), nhưng đổi lại biết chính xác từng bước kiểm cái gì.

### 3.2 Chỗ tin là hiệu quả

- **Script trước, người sau:** mọi số trong file nộp sinh từ một file nguồn bằng script, mọi lần ghi lên Project có đọc lại. Nhờ vậy số SWP, giờ và trạng thái giữa file và Project lệch 0.
- **Đặt luật review trước lượt đầu** giúp dừng đúng lúc: backlog đạt cổng sau hai lượt, không lặp tình trạng 5 lượt như LAB-4.
- **Kịch bản giả lập viết trước rồi mới cập nhật Project**, mỗi chỗ lệch trỏ một câu hỏi khách hoặc chỗ hở có thật, nên báo cáo tiến độ không phải bịa nguyên nhân.
- **Ước giờ mẫu mà không cho xem SWP** cho thấy skill chấm giao diện và kiểm thử thấp hơn công thật (4,3–5,5 giờ/SWP so với 2–3,3 của backend); nếu dùng một hệ số chung, giờ frontend và kiểm thử thiếu khoảng 30 %.

### 3.3 Chỗ chưa tốt, khi làm thật cần cải thiện

- **AI ba lần khuyến nghị phương án trái RFP** và người làm lab chọn theo. Khi làm thật, mỗi phương án phải được đối chiếu với RFP trước khi trình, không chỉ sau khi đã chọn.
- **Review parity chỉ kiểm chiều spec ↔ issue** nên bỏ sót yêu cầu phi chức năng nằm trong RFP mà không nằm trong spec màn. Cần thêm danh sách yêu cầu phi chức năng của RFP vào phạm vi parity.
- **Kiểm năng lực bằng tổng giờ chia đội** cho kết luận sai; nên xếp thử theo phụ thuộc ngay khi quy giờ, không đợi tới bước xếp sprint.
- **Vai gợi ý lúc break không cân tải**: một backend nhận 700 giờ, nên khi xếp sprint 157/268 việc lá phải đổi người. Lúc break nên kiểm tải theo vai.
- **Đo giờ còn hở:** công cụ tính giờ coi khoảng lặng trên 20 phút là nghỉ, nên lượt AI chạy dài bị tính thiếu; một đoạn khoảng 30 phút không được ghi vì tệp cấu hình ghi nhật ký bị xoá khỏi thư mục làm việc, phải bù từ bản ghi hội thoại.
- **Ghi lên GitHub từng ô một** mất khoảng 3 giây mỗi ô; nên gộp nhiều ô vào một lệnh ngay từ đầu.

### 3.4 Giờ làm thật

_Chốt ở cuối phiên._
