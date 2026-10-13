# Báo cáo dùng AI — LAB-5 (Yuki Cold WMS)

Phạm vi: toàn bộ LAB-5 — chia task từ bộ thiết kế LAB-4, dựng GitHub Project, chấm SWP, quy đổi sang giờ, lập kế hoạch sprint, giả lập Sprint 1 và lập báo cáo tiến độ. Thực hiện 2026-10-12 → 2026-10-13 trên hai máy; công cụ chính là Claude Code.

Mỗi trường hợp AI sai, được giữ nguyên hoặc bị bác đều được ghi vào nhật ký AI ngay khi xảy ra. Báo cáo này tổng hợp từ nhật ký đó: 82 trường hợp, gồm 42 trường hợp AI sai đã sửa, 20 trường hợp nghi sai nhưng kiểm tra xong vẫn giữ, 6 gợi ý bị bác, 8 góp ý của agent review, 4 trường hợp agent không theo đúng hướng dẫn quy trình (vd viết tin nhắn kết thúc bằng tiếng Đức, ghi file nháp ra ngoài chỗ được phép) và 2 lần xin dùng skill Takumi.

Thuật ngữ dùng trong báo cáo: **work item** là một epic, issue hoặc sub-issue trên GitHub Project; **leaf task** là issue hoặc sub-issue không có sub-issue con, nơi ghi SWP và giờ; **SWP** (Standard Work Point) là điểm khối lượng chuẩn của một việc; **DoD** (Definition of Done) là điều kiện để coi một issue là xong; **nhóm epic** là một trong 6 nhóm epic của backlog (nền tảng, nhập kho và tồn kho, xuất kho, lập tuyến và giờ lái, nhiệt độ – truy xuất – báo cáo, quản trị; bảng ở [task-breakdown.md](task-breakdown.md) mục 1.5).

## 1. Skill đã dùng và cách viết prompt cho từng việc

### 1.1 Thử nghiệm của lab này: dùng bộ skill Takumi ở mức tối thiểu

Ở LAB-1 đến LAB-4, bộ skill Takumi được dùng tối đa. LAB-5 thử ngược lại để so chất lượng, thời gian và mức kiểm soát:

- Mặc định không dùng skill hay agent Takumi. Mọi việc làm bằng công cụ cơ bản của Claude Code (đọc, sửa, chạy lệnh), agent `general-purpose`, `gh` CLI, GraphQL của GitHub và script Python viết riêng cho bài.
- Muốn dùng một skill Takumi thì phải hỏi người làm lab trước, nêu dùng gì, để làm gì, vì sao làm tay không đủ.
- Chỉ một skill được duyệt: **`tkm:sun-estimate`** ở bước chấm SWP, vì đề yêu cầu chấm bằng skill. Cuối bài dùng lại skill này một lần để xuất lại báo cáo HTML với câu chữ dễ hiểu hơn (không chấm lại, điểm số giữ nguyên).
- Skill chấm SWP gợi ý nạp thêm hai skill phụ (chấm độ tin cậy, tra cứu chuyên gia). Không nạp, vì skill đã có sẵn định nghĩa độ tin cậy riêng để dùng khi thiếu hai skill này.

### 1.2 Cách giao việc cho agent

- **Năm vai**, mỗi vai có một bản mô tả gồm nhiệm vụ, file được ghi và checklist chất lượng: phân tích spec, chia task, quản lý dự án (vai duy nhất được ghi lên GitHub), đóng gói, review độc lập.
- **Chạy song song theo nhóm epic:** backlog chia thành 6 nhóm epic. Mỗi agent nhận một nhóm với dải mã issue riêng; file gộp chỉ sinh bằng script, không agent nào sửa file gộp.
- **Mẫu prompt cố định** gồm: vai và bản mô tả vai · giai đoạn và việc cần làm (1–3 câu) · file đọc, file được ghi · DoD · ràng buộc (không dùng Takumi, không sửa file của vai khác) · ngôn ngữ. Dòng ngôn ngữ được thêm sau khi một agent viết tin nhắn kết thúc bằng tiếng Đức: đối chiếu 7 agent cùng đợt thì agent đó là prompt duy nhất thiếu dòng "viết bằng tiếng Việt".
- Agent làm xong phải chép checklist vào báo cáo và tự kiểm tra từng dòng kèm bằng chứng. Phiên Claude Code chính (phiên điều phối) chọn ít nhất ba dòng để kiểm tra lại trước khi nhận kết quả.

### 1.3 Từng việc

| Việc | Công cụ | Cách giao / prompt | Đầu ra được kiểm tra bằng |
|---|---|---|---|
| Đọc bộ LAB-4, tìm chỗ hở của spec | 6 agent phân tích (mỗi nhóm epic một agent) + 1 agent tổng hợp | Đọc danh mục spec của nhóm, liệt kê màn hình, endpoint, câu hỏi khách còn mở và chỗ hở; mỗi chỗ hở trích `file:dòng` | Script kiểm tra mọi trích dẫn `file:dòng` (thêm sau hai lần lệch một dòng); agent tổng hợp đối chiếu chéo giữa các nhóm |
| Chia task | 1 agent dựng khung chung trước, rồi 6 agent chia task song song | Khung chung gồm: luật về granularity (chia nhỏ tới đâu thì dừng), động từ mở đầu tiêu đề issue, DoD theo loại việc, các thành phần dùng chung. Mỗi agent chia nhóm epic của mình thành JSON: mục tiêu, spec nguồn, DoD, nhãn, vai gợi ý, phụ thuộc, ràng buộc | Script gộp kiểm tra dải mã, quan hệ cha–con, vòng phụ thuộc, tiêu đề trùng; review đối chiếu hai chiều spec ↔ issue (mục 2.3) |
| Đẩy lên GitHub Project | Script Python + `gh` + GraphQL | Thử trước trên repo nháp; chạy lại không tạo trùng, không ghi đè trạng thái | Đếm trên Project = backlog theo epic, issue, sub-issue; quan hệ cha–con khớp |
| Chấm SWP | `tkm:sun-estimate` + 5 agent chấm theo đợt | Skill đọc Project, chia 268 leaf task thành các đợt khoảng 50 việc. Agent chấm mặc định của skill không đọc được file, phải dán khoảng 460 nghìn ký tự vào prompt; người làm lab chọn thay bằng agent đọc trực tiếp file dữ liệu của đợt và trả JSON theo đúng định dạng của skill | Bước kiểm tra hợp lệ của skill (250/250 leaf task; 18/18 leaf task bổ sung sau); 5 issue mẫu do skill chọn theo luật cố định, đối chiếu với DoD và spec, người làm lab chốt từng issue |
| Ghi SWP lên Project | Phiên Claude Code chính trong vai quản lý dự án, chạy script | Script đọc bảng SWP đã chốt (không đọc số thô của skill), chỉ ghi ô lệch bằng `gh project item-edit`, rồi đọc lại toàn bộ Project; chỉ chạy sau khi người làm lab duyệt issue mẫu | Đọc lại 343 work item, lệch 0. Cùng script ghi trường giờ. Ở bước xếp sprint, ghi từng ô quá chậm (khoảng 3 giây một ô) nên đổi sang gộp 25 ô vào một lệnh GraphQL; đọc lại lệch 0 |
| Quy đổi sang giờ | 1 agent ước giờ trực tiếp + script | Agent ước giờ 10 issue mẫu **không được xem SWP** (tránh bị điểm kéo theo), ghi khoảng và lý do theo từng bước việc; script tính hệ số giờ/SWP theo nhóm việc và quy đổi cho mọi leaf task. Sau đó 30 leaf task của ba epic có chênh lệch lớn nhất với estimate LAB-1 được ước lại trực tiếp (mục 3.2) | Tổng giờ trên Project = file giờ đã chốt, lệch 0 |
| Xếp sprint, giả lập sprint, báo cáo tiến độ | Phiên Claude Code chính + script | Script xếp việc theo phụ thuộc và năng lực từng vai; kịch bản Sprint 1 viết thành file dữ liệu **trước** khi cập nhật Project, mỗi chỗ lệch trỏ tới một câu hỏi khách hoặc chỗ hở có thật; script đọc lại Project để sinh bảng trạng thái, burndown và điền số vào mẫu báo cáo viết tay | Script dừng nếu trạng thái trên Project khác kịch bản hoặc thiếu Iteration, vai |

## 2. Review output của AI

### 2.1 Người review ở đâu

| Bước | Người làm gì |
|---|---|
| Chốt hướng trước khi làm | Người làm lab chọn 4 quyết định gốc (phạm vi chia task, nơi nộp, trường vai giả định, skill chấm SWP) và 6 quyết định thiết kế khi chia task; mỗi câu có 3 phương án kèm ảnh hưởng tới backlog |
| Cổng duyệt 1 — sau khi chia task | Duyệt backlog sau hai lượt review đối chiếu hai chiều |
| Cổng duyệt 2 — chấm SWP | Duyệt từng issue mẫu; sửa một issue (mục 2.4) |
| Giữa chừng | Chọn cách quy đổi sang giờ; duyệt bổ sung epic phi chức năng; chọn thêm một frontend khi kế hoạch không vừa 9 sprint; đòi phương án xử lý cho rủi ro ước thấp thay vì chỉ theo dõi; yêu cầu rà lại câu chữ cho người ngoài đọc hiểu |
| Cổng duyệt 3 — trước khi nộp | Mở repo, Project và báo cáo HTML bằng cửa sổ ẩn danh; duyệt nộp |

### 2.2 Máy kiểm tra trước, agent review sau

Mọi đầu ra phải qua script trước khi giao agent review, và reviewer không kiểm tra lại những gì script đã kiểm:

- script gộp các nhóm epic và đếm;
- script kiểm tra hợp đồng dữ liệu giữa các giai đoạn (một giá trị dùng chung chỉ có một file nguồn);
- cổng repo public: câu chép RFP hoặc đề, khoá bí mật, từ nội bộ, dữ liệu cá nhân, link hỏng;
- đọc lại mọi trường đã ghi lên Project;
- script kiểm tra nhất quán số giữa file nộp và Project (32 chỗ).

Luật review đặt trước lượt đầu: tối đa hai lượt mỗi đầu ra, mỗi phát hiện phải gắn tiêu chí, không chốt luật nghiệp vụ mới để sửa một phát hiện. Cả lab dùng 4 lượt review nội dung bằng agent (backlog hai lượt, bản gửi khách hai lượt) và hai lượt rà văn phong theo yêu cầu của người làm lab, so với 5 lượt chỉ riêng một gói ở LAB-4.

### 2.3 Review bằng agent

- **Backlog:** 6 agent review song song, mỗi agent một nhóm epic, đối chiếu hai chiều: mọi issue có nguồn trong spec, mọi phần spec có issue hoặc có lý do chưa thành issue. Lượt đầu: điểm trung bình 7,3, 4 lỗi Cao (còn 1 sau khi đối chiếu nguồn). Lượt xác nhận sau khi sửa: 8,4, 0 lỗi Cao, đạt cổng nên dừng.
- **Bản gửi khách (README, estimate, báo cáo tiến độ, báo cáo này):** review mù một lần bằng hai agent trên hai model khác nhau, không thấy kết quả của nhau; kết quả ở mục 2.6.
- **Văn phong:** một agent đóng vai biên tập viên tiếng Việt chấm mức dễ hiểu từng file (5–7/10), đề xuất 36 thuật ngữ cần thay và 39 câu viết lại; lượt kiểm tra lại sau khi áp chấm 6–8/10 và chỉ ra thêm 20 chỗ, trong đó 2 câu bị script thay từ làm sai, đã sửa. Bộ thuật ngữ thống nhất được áp cho mọi file bằng một script chạy cuối cùng; script che tiêu đề issue để tiêu đề trong file không lệch với GitHub.

### 2.4 Vấn đề trong output của AI và cách xử lý

| AI sai gì | Phát hiện bằng gì | Xử lý |
|---|---|---|
| **Ba lần đề xuất phương án trái RFP** làm phương án khuyến nghị: chọn bộ quy tắc giờ lái theo ngày chạy tuyến thay vì phiên bản hiệu lực lúc phát hành; chỉ gửi thư cảnh báo, bỏ thư phê duyệt và báo cáo; tải file đơn tay thay vì nhận theo lịch. Người làm lab đã chọn theo đề xuất | Agent viết tiền đề và agent review đối chiếu lại RFP | Chốt lại ba quyết định, sửa tiền đề và cập nhật mọi issue dùng tới cùng thực thể dữ liệu; thêm vào checklist: đối chiếu từng phương án với RFP trước khi trình |
| **Backlog thiếu cả mảng phi chức năng** (kiểm thử tải, WCAG, diễn tập khôi phục, kiểm thử hệ thống, quét bảo mật), dù kế hoạch đã chốt phải phủ; hai lượt review đối chiếu không bắt được | So giờ với estimate LAB-1 theo vai, lúc chưa bổ sung: kiểm thử thấp hơn 538 giờ, hạ tầng thấp hơn 191 giờ | Bổ sung epic phi chức năng (21 work item), chấm SWP cho phần mới bằng cùng luật |
| **Kiểm tra năng lực bằng cách chia tổng giờ** ra "7,3 sprint, vừa khung 8,6 sprint". Lúc đó tính 547 giờ mỗi sprint cho các vai làm issue của đội LAB-1; số hiện hành trong estimate.md là 611 giờ, đã gồm frontend bổ sung | Script xếp từng việc theo vai và phụ thuộc: đội hình LAB-1 cần 10 sprint, vì frontend chỉ dựng màn hình được khi API đã bắt đầu | Người làm lab chọn thêm một frontend toàn thời gian; sửa đội hình ở file nguồn và cập nhật estimate.md |
| Phiên chính báo "đội LAB-1 cần 11 sprint" từ một bản thử tính xấp xỉ | Thêm tuỳ chọn để con số chạy lại được bằng script; kết quả là 10 | Sửa về 10 ở mọi chỗ, báo lại người làm lab |
| **Rủi ro ước thấp nêu quá mức**: AI ghi "khoảng 543 giờ (14 %) có thể ước thấp" ở ba epic, chỉ kèm hành động theo dõi | Người làm lab đòi phương án xử lý. Ước lại trực tiếp 30 leaf task của ba epic: chỉ cao hơn 49,5 giờ (+12 %); 543 giờ là chênh lệch với LAB-1, không phải mức ước thấp | Người làm lab chọn cập nhật giờ chính thức (3.974,5 → 4.024 giờ), cho backend hỗ trợ viết kiểm thử tự động, xếp lại sprint (Sprint 1 giữ nguyên); rủi ro còn lại ghi đúng mức |
| Skill chấm migration 8 bảng là 12 SWP (cao nhất backlog) | Kiểm tra issue mẫu với DoD: tám bảng của một miền là một đợt migration có kiểm soát | Hạ 12 → 10, áp cùng luật cho 6 issue migration cùng nhóm |
| AI nhẩm năng lực cả đội LAB-1 (gồm quản lý dự án và thiết kế) là 654 giờ mỗi sprint | Script cộng lại cùng bảng | 654 → 616 (sau khi thêm một frontend: 680); ghi luôn phép cộng vào bảng để người đọc tự kiểm tra |
| Script đẩy backlog bản đầu đặt lại mọi trạng thái về Todo mỗi lần chạy lại | Chạy lần hai trên repo nháp sau khi đặt tay một trạng thái | Chỉ đặt trạng thái khi work item mới tạo hoặc trạng thái còn trống |
| Trích dẫn `file:dòng` lệch một dòng (hai lần), trích vào dòng lịch sử thay đổi thay vì thân spec (ba chỗ), ghi số liệu từ trí nhớ | Kiểm tra chéo bằng `grep -n`, in lại dòng thật | Thêm bước kiểm tra mọi trích dẫn bằng script vào checklist |
| Email commit của repo nộp tự ghép từ tên máy và tên miền công ty | Kiểm tra tác giả commit khi một lần commit lỗi | Đổi sang mã học viên và email ẩn danh của GitHub, viết lại hai commit đầu |
| Tên vai nội bộ lọt vào báo cáo HTML nộp | Cổng repo public | Sửa câu chữ, xuất lại báo cáo |
| Câu chữ dùng từ tự đặt (`việc lá`, `độ hạt`, `lát`, `ca kiểm`…), người ngoài khó hiểu | Người làm lab chỉ ra; agent rà văn phong đếm và đề xuất | Đổi sang thuật ngữ IT thông dụng (leaf task, granularity, nhóm epic, test case…), áp thống nhất bằng script |

### 2.5 Trường hợp giữ nguyên hoặc bác sau khi kiểm tra

- **Giữ:** một câu DoD sai cần thay ở 36 chỗ; agent kiểm tra từng chỗ và giữ nguyên 1 chỗ vì ở đó câu cũ đúng với luật giờ lái, nên chỉ thay 35 chỗ.
- **Giữ:** nghi `gh` không tạo được trường Iteration và sub-issue nên đã chuẩn bị cách làm tay; chạy thử trên repo nháp thì GraphQL làm được cả hai.
- **Giữ:** reviewer gợi ý khai việc thêm epic phi chức năng vào PREMISE.md; không thêm, vì epic này có nguồn ngay trong bộ thiết kế LAB-4 (mục yêu cầu phi chức năng của kiến trúc), không phải khác biệt so với LAB-4.
- **Giữ:** chữ "chỗ hở" không đổi khi chuẩn hoá thuật ngữ, vì đề LAB-5 dùng đúng từ này cho phần bắt buộc.
- **Bác:** reviewer đòi ghi phụ thuộc từ mọi issue tới issue câu hỏi khách; bác vì quyết định đã chốt là chỉ gắn thẻ câu hỏi, để việc đã có giả định tạm không bị khoá chờ cuộc họp với khách.
- **Bác:** agent ánh xạ estimate LAB-1 định chia màn hình lập tuyến nửa cho epic lập tuyến, nửa cho epic giờ lái theo tỷ lệ tự đặt; bác vì không có nguồn, ghi số LAB-1 của epic giờ lái là cận dưới.
- **Bác:** agent tổng hợp bác kết luận "purge sổ giờ là chỗ hở" của một agent phân tích, vì spec đã có ngoại lệ cho sổ giờ.

### 2.6 Một góp ý review cụ thể và cách xử lý

Ở lượt review đối chiếu đầu tiên, reviewer của nhóm epic nền tảng chỉ ra quyết định "chỉ gửi thư cảnh báo" trái RFP: điểm tích hợp thư của RFP gồm cả thư phê duyệt và thư báo cáo. Phiên chính in lại dòng RFP để kiểm tra và xác nhận đúng. Người làm lab chốt lại: giữ ba loại thư, người nhận theo giả định tạm (PREMISE.md P2-03), thêm một issue làm rõ với khách. Khi sửa, hai agent chia task liệt kê các chỗ liên quan theo thực thể dữ liệu và thấy danh sách giao sửa còn sót ba hàng đợi duyệt; cả ba được duyệt bổ sung.

Review mù bản gửi khách: hai agent trên hai model (Opus, Sonnet), không thấy nhau, cùng chấm 7,5/10. Cả hai cùng bắt một lỗi của AI ở báo cáo tiến độ: burndown gán phần chậm của ngày 09/12 cho chuỗi migration, trong khi nguyên nhân là issue đăng nhập bị chặn vì chờ câu hỏi Q5. Lỗi Cao duy nhất do agent Sonnet nêu: work item Sprint 1 chuyển sang (88,5 giờ backend, 64 giờ frontend) không vừa chỗ trống của Sprint 2, nhưng báo cáo chỉ ghi "lập lại kế hoạch Sprint 2". Xử lý: thêm chế độ xếp lại thử sau Sprint 1 vào script xếp sprint và viết lại dòng rủi ro theo hai kịch bản (việc chưa xong còn 25–50 % giờ, hoặc phải làm lại toàn bộ).

Lượt xác nhận (một agent Opus, chỉ đọc vùng đã đổi) chấm 8,0 và bắt chính lỗi của phiên chính khi sửa: số việc phải dời của hai kịch bản bị gán lẫn nhau. Từ đó script xếp lại tự in các số này, và script kiểm tra nhất quán so chúng với báo cáo để lần sau máy bắt được.

## 3. Điểm đặc biệt: chỗ hiệu quả, chỗ cần cải thiện

### 3.1 Takumi tối thiểu so với LAB-4

| Tiêu chí | LAB-4 (Takumi tối đa) | LAB-5 (Takumi tối thiểu) |
|---|---|---|
| Skill Takumi dùng | Nhiều skill quy trình và agent của bộ kit | 1 skill (`tkm:sun-estimate`), hỏi trước mỗi lần dùng (2 lần) |
| Giờ có tương tác với AI | 24,0 giờ (17 phiên, 487 prompt) | _điền khi chốt giờ_ (mục 3.4) |
| Trường hợp ghi trong nhật ký AI | 406 (256 sửa) | 82 (42 sửa, 20 giữ, 6 bác, 8 góp ý review, 4 không theo hướng dẫn, 2 xin dùng Takumi) |
| Số lượt review nội dung bằng agent | 5 lượt cho một gói, điểm không tăng | 4 lượt cho cả lab, có cổng dừng đặt trước |
| Mức kiểm soát | Quy trình của kit quyết định nhiều bước | Mỗi bước do script hoặc người quyết; mọi số trên Project đọc lại được |

Hai lab khác loại việc (thiết kế chi tiết và chia task), nên bảng chỉ cho thấy xu hướng, không phải phép đo đối chứng. Điều thấy rõ: khi bỏ các skill quy trình, phải tự viết lại phần khung (bản mô tả vai, mẫu prompt, luật review, cổng kiểm tra), nhưng đổi lại biết chính xác từng bước kiểm tra cái gì.

### 3.2 Chỗ tin là hiệu quả

- **Script trước, người sau:** mọi số trong file nộp sinh từ một file nguồn bằng script, mọi lần ghi lên Project đều đọc lại. Nhờ vậy SWP, giờ và trạng thái giữa file và Project lệch 0.
- **Đặt luật review trước lượt đầu** giúp dừng đúng lúc: backlog đạt cổng sau hai lượt, không lặp tình trạng 5 lượt như LAB-4.
- **Kịch bản giả lập viết trước rồi mới cập nhật Project**, mỗi chỗ lệch trỏ tới một câu hỏi khách hoặc chỗ hở có thật, nên báo cáo tiến độ không phải bịa nguyên nhân.
- **Ước giờ mà không cho xem SWP** hai lần mang lại thông tin thật. Lần đầu (10 issue mẫu) cho thấy skill chấm giao diện và kiểm thử thấp hơn công thật (4,3–5,5 giờ/SWP so với 2–3,3 của backend); nếu dùng một hệ số chung, giờ frontend và kiểm thử thiếu khoảng 30 %. Lần hai (30 leaf task của ba epic) cho thấy chênh lệch lớn với LAB-1 chủ yếu nằm ở cách LAB-1 phân bổ giờ, LAB-5 chỉ ước thấp khoảng 12 %.
- **Chạy thử kế hoạch bằng script với từng phương án** trước khi chọn cách xử lý rủi ro: tăng giờ ba epic thì kế hoạch chậm khoảng 4 ngày; cho backend hỗ trợ viết kiểm thử tự động thì vẫn xong Sprint 9.

### 3.3 Chỗ chưa tốt, khi làm thật cần cải thiện

- **AI ba lần khuyến nghị phương án trái RFP** và người làm lab chọn theo. Khi làm thật, mỗi phương án phải được đối chiếu với RFP trước khi trình, không chỉ sau khi đã chọn.
- **Review đối chiếu chỉ kiểm tra chiều spec ↔ issue**, nên bỏ sót yêu cầu phi chức năng nằm trong RFP mà không nằm trong spec màn hình. Cần thêm danh sách yêu cầu phi chức năng của RFP vào phạm vi đối chiếu.
- **Kiểm tra năng lực bằng cách chia tổng giờ cho đội** cho kết luận sai; nên xếp thử theo phụ thuộc ngay khi quy đổi sang giờ, không đợi tới bước xếp sprint.
- **Rủi ro nên đi kèm số đo ngay từ đầu:** AI nêu rủi ro ước thấp bằng chênh lệch với LAB-1 rồi chỉ đề nghị theo dõi; ước lại trực tiếp chỉ mất vài phút và cho con số đúng mức.
- **Vai gợi ý lúc chia task không cân tải:** một backend nhận 700 giờ, nên khi xếp sprint 157/268 leaf task phải đổi người. Lúc chia task nên kiểm tra tải theo vai.
- **Câu chữ:** AI dùng từ tự đặt quen trong quá trình làm (`việc lá`, `lát`, `độ hạt`), người ngoài khó hiểu. Nên chốt bảng thuật ngữ trước khi viết file nộp, không đợi rà ở cuối.
- **Đo giờ còn thiếu sót:** công cụ tính giờ coi khoảng lặng trên 20 phút là nghỉ, nên lượt AI chạy dài bị tính thiếu; một đoạn khoảng 30 phút không được ghi vì tệp cấu hình ghi nhật ký bị xoá khỏi thư mục làm việc, phải bù từ bản ghi hội thoại.
- **Ghi lên GitHub từng ô một** mất khoảng 3 giây mỗi ô, và đọc cả Project kèm thân issue làm cạn hạn mức GraphQL theo giờ; nên gộp nhiều ô vào một lệnh và chỉ đọc đúng các trường cần ngay từ đầu.

### 3.4 Giờ làm thật

_Chốt ở cuối phiên._
