# Cài Đặt Nagios XI trên Linux

### Yêu Cầu:
Trước khi bắt đầu cài đặt, bạn cần kết nối với máy chủ qua phiên terminal. Bạn cần đăng nhập vào máy chủ với quyền root (hoặc một người dùng có quyền root).

### Cài Đặt Nagios XI

Có nhiều phương pháp để cài đặt Nagios XI, tất cả đều thực hiện cài đặt đầy đủ.

#### 1. Cài Đặt Nhanh

Chạy lệnh sau trong phiên terminal của bạn:

```bash
curl https://assets.nagios.com/downloads/nagiosxi/install.sh | sh
```

Lệnh này sẽ tải về và cài đặt Nagios XI. Sau khi cài đặt xong, bạn có thể tiếp tục với phần **Hoàn Tất Cài Đặt**.

#### 2. Tải Về và Cài Đặt Thủ Công

Nếu bạn muốn cài đặt thủ công, bạn có thể sử dụng các lệnh sau:

```bash
cd /tmp
wget https://assets.nagios.com/downloads/nagiosxi/xi-latest.tar.gz
tar xzf xi-latest.tar.gz
cd nagiosxi
./fullinstall
```

Lưu ý: Nếu bạn cần cài đặt phiên bản cụ thể của Nagios XI, bạn có thể truy cập trang web sau để lấy URL phiên bản và sử dụng URL đó trong lệnh `wget`:

[Trang phiên bản Nagios XI](https://assets.nagios.com/downloads/nagiosxi/versions.php)

Sau khi cài đặt xong, bạn có thể tiếp tục với phần **Hoàn Tất Cài Đặt**.

---

## Hoàn Tất Cài Đặt

Khi cài đặt hoàn tất, bạn sẽ thấy thông báo tương tự như sau:

```
Nagios XI Installation Complete!
```

Bạn có thể truy cập giao diện web của Nagios XI bằng cách vào:

```
http://<server_address>/nagiosxi
```

Truy cập vào giao diện người dùng qua URL được cung cấp trong phiên terminal. Bạn sẽ thấy màn hình cài đặt Nagios XI. Đầu tiên, bạn sẽ được yêu cầu cấu hình các cài đặt hệ thống chung.

### Cấu Hình Cài Đặt Hệ Thống

1. **Chọn cấu hình hệ thống**: Bạn có thể điều chỉnh các tùy chọn cấu hình hệ thống.
2. **Cài Đặt Giấy Phép**: 
   - **Trial** – Dùng thử (thông tin chi tiết xem ở phần "Starting a Nagios XI Trial").
   - **Licensed** – Nhập mã bản quyền, Client ID và Enterprise Key.
   - **Free** – Giới hạn tối đa 7 nút và 100 kiểm tra host/service.

Sau khi chọn xong, nhấn **Next** để tiếp tục.

### Cấu Hình Tài Khoản Admin

Trên trang tiếp theo, bạn sẽ có các tùy chọn cấu hình tài khoản quản trị viên. Điều quan trọng nhất là bạn cần thay đổi mật khẩu quản trị viên (bạn không cần sử dụng mật khẩu được tạo ngẫu nhiên).

Sau khi điều chỉnh xong, nhấn **Finish Install** để lưu cài đặt.

### Hoàn Tất Cài Đặt

Trang sẽ hiển thị logo quay trong khi nó áp dụng các cài đặt cho Nagios XI.

Khi cài đặt hoàn tất, bạn sẽ thấy màn hình **Installation Complete** với tên người dùng và mật khẩu cần thiết để đăng nhập vào Nagios XI. Nhấn **Login to Nagios XI** để bắt đầu.

### Đăng Nhập vào Nagios XI

Khi màn hình đăng nhập hiện ra, nhập thông tin tài khoản và mật khẩu của bạn, rồi nhấn **Login**.

Bạn sẽ cần chấp nhận thỏa thuận giấy phép để tiếp tục.

Sau khi đăng nhập thành công, bạn sẽ được chuyển đến màn hình chính của Nagios XI.

---

**Nguồn tham khảo:**
- [Tài liệu cài đặt Nagios Core](https://www.nagios.org/documentation/)
- [Tài liệu Nagios XI](https://support.nagios.com/kb/)
