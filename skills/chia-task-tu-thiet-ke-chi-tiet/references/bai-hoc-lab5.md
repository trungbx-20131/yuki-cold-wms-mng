# Kiểm chứng và bài học từ LAB-5

## 1. Kiểm chứng script trên dữ liệu thật

| Kiểm | Kết quả |
|---|---|
| `gop-va-kiem-backlog.py` trên backlog bản cuối | 26 epic · 144 issue · 173 sub-issue · 268 leaf task, 0 lỗi; 9 cảnh báo DoD dài; cảnh báo một backend nhận 54 leaf task, gấp 2,7 lần trung vị |
| Cùng script, cố ý cài 4 lỗi (trùng mã, phụ thuộc không có, cha sai tầng, vòng phụ thuộc) | Bắt đủ 4, exit 1 |
| `day-backlog-len-github.py` chạy khô trên repo và Project đang dùng (343 work item) | 0 issue mới · 343 dùng lại · 0 sửa tại chỗ · 0 nối cha · 0 thêm Project · 0 đặt Todo |

Hai script được đóng gói ở bước cuối của LAB-5 từ các script đã dùng khi làm bài (lúc đó gắn đường dẫn và quy
ước của repo bài); bản trong skill nhận tham số dòng lệnh để dùng cho dự án khác.

## 2. Bài học

- **Chốt khung trước khi giao chia.** Một câu DoD sai trong khung (áp chặn thiếu tham số cho mọi luật) đã bị 5
  nhóm chép nguyên văn vào 36 chỗ trước khi khung được sửa; phải giao sửa theo danh sách từng nhóm.
- **Review đối chiếu phải kèm yêu cầu phi chức năng của RFP.** Hai lượt review spec ↔ issue không bắt được backlog
  thiếu cả mảng phi chức năng (kiểm thử tải, WCAG, diễn tập khôi phục, kiểm thử hệ thống, quét bảo mật), vì các
  yêu cầu đó nằm ở RFP chứ không ở spec màn hình. Lộ ra muộn khi so giờ với estimate báo giá theo vai.
- **Cân tải theo vai ngay lúc chia.** Vai gợi ý dồn cho một backend khoảng 700 giờ; tới lúc xếp sprint, 157/268
  leaf task phải đổi người. Cảnh báo theo trung vị trong `gop-va-kiem-backlog.py` sinh ra từ bài học này.
- **Đối chiếu phương án với RFP trước khi trình.** AI ba lần khuyến nghị phương án trái RFP (chọn bộ quy tắc giờ
  lái theo ngày chạy thay vì phiên bản hiệu lực lúc phát hành; chỉ gửi thư cảnh báo; tải file đơn tay thay vì nhận
  theo lịch) và người quyết đã chọn theo; phải chốt lại và lan sửa sau đó.
- **Liệt kê điểm cần sửa theo thực thể, không theo màn hình được nêu tên.** Một quyết định về hàng đợi duyệt bị
  sót ba hàng đợi vì danh sách giao sửa chỉ ghi các màn được nhắc trong quyết định.
- **Kiểm mọi trích dẫn `file:dòng` bằng script.** Hai lần lệch một dòng, ba lần trích vào dòng lịch sử thay đổi
  thay vì thân spec.
- **Đẩy lên GitHub phải chạy lại an toàn.** Bản đầu của script đặt lại Status = Todo mỗi lần chạy, xoá trạng thái
  sprint; bản trong skill chỉ đặt cho item mới hoặc chưa có Status. Thử trên repo nháp trước.
- **Thuật ngữ cho người ngoài.** Chốt bảng thuật ngữ trước khi viết task-breakdown; tránh từ tự đặt ("việc lá",
  "lát", "độ hạt"), dùng leaf task, nhóm epic, granularity và giải nghĩa lần đầu.
