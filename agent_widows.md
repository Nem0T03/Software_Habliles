### **Hướng Dẫn Cài Đặt NSClient++ Agent cho Nagios XI trên Windows**

Dưới đây là các bước chi tiết để cài đặt **NSClient++ Agent** cho Nagios XI trên một máy chủ Windows.

---

#### **1. Cài Đặt Agent trên Windows**

1. **Đăng nhập vào máy tính Windows** mà bạn muốn cài đặt NSClient++.

2. **Chạy gói cài đặt NSClient++**:
   - Mở tệp cài đặt NSClient++ mà bạn đã tải về.
   - Chạy gói cài đặt để bắt đầu quá trình cài đặt.

3. **Màn hình chào mừng** sẽ xuất hiện, nhấn **Next** để tiếp tục.

4. **Chọn kiểu cài đặt**:
   - Chọn **Generic** và nhấn **Next** để tiếp tục.

5. **Chọn chế độ cài đặt**:
   - Nhấn nút **Typical** để cài đặt theo cấu hình mặc định.
   
6. **Cấu hình NSClient++ Agent**:
   - **Nhập địa chỉ IP của máy chủ Nagios XI** vào ô **Allowed hosts**. Bạn có thể nhập một hoặc nhiều địa chỉ IP (các địa chỉ IP phải được phân tách bằng dấu phẩy, ví dụ: `10.25.5.11, 10.25.5.12`).
   - **Nhập mật khẩu** vào ô **Password**. Đây là mật khẩu dùng để giao tiếp giữa máy chủ Nagios và máy tính Windows (sử dụng plugin `check_nt`).
   - **Bật các plugin kiểm tra thông thường**: Đảm bảo rằng tùy chọn **Enable common check plugins** đã được chọn.
   - **Bật máy chủ NSClient (check_nt)**: Đảm bảo rằng tùy chọn **Enable nsclient server (check_nt)** đã được chọn.
   - Lưu ý: **NRPE** không được chọn trong bước này vì nó không cần thiết khi sử dụng trình hướng dẫn cấu hình NSClient++.

7. **Tiếp tục với cài đặt**:
   - Nhấn **Next** để tiếp tục.

8. **Cài Đặt**:
   - Nhấn nút **Install** trên màn hình tiếp theo để bắt đầu quá trình cài đặt.
   - Bạn có thể sẽ được yêu cầu cấp quyền cho trình cài đặt để thay đổi máy tính của bạn. Nhấn **Yes** để tiếp tục.

9. **Hoàn tất cài đặt**:
   - Chờ trong khi NSClient++ được cài đặt.
   - Sau khi quá trình cài đặt hoàn tất, nhấn **Finish** để hoàn thành quá trình cài đặt.

---

#### **2. Kiểm Tra và Hoàn Thành Cài Đặt**

- **NSClient++ sẽ chạy như một dịch vụ** trên máy tính Windows, có nghĩa là máy tính của bạn đã sẵn sàng để được giám sát bởi Nagios XI.
- Sau khi cài đặt xong, bạn có thể sử dụng **trình hướng dẫn cấu hình NSClient++** để cấu hình thêm, không cần bước cấu hình thủ công.

---

#### **3. Sử Dụng Trình Hướng Dẫn Cấu Hình**
Sau khi cài đặt xong, không cần thực hiện thêm bước nào nữa. Bạn có thể sử dụng **trình hướng dẫn cấu hình NSClient++** để hoàn tất việc cấu hình và giám sát máy tính Windows qua Nagios XI.

**Tài liệu tham khảo thêm**: Để tìm hiểu cách sử dụng trình hướng dẫn cấu hình NSClient++, bạn có thể tham khảo tài liệu **Monitoring Windows Using NSClient++**.

---

### **Tóm Tắt Các Bước Cài Đặt**

1. Tải và chạy tệp cài đặt NSClient++ trên máy Windows.
2. Chọn các cài đặt mặc định: Generic, Typical.
3. Cấu hình địa chỉ IP của máy chủ Nagios và mật khẩu cho kết nối.
4. Bật các plugin kiểm tra và NSClient server (check_nt).
5. Tiến hành cài đặt và chờ hoàn tất.
6. NSClient++ sẽ tự động chạy như một dịch vụ và máy tính Windows của bạn đã sẵn sàng để giám sát qua Nagios XI.

Nếu bạn gặp bất kỳ vấn đề nào trong quá trình cài đặt, hãy tham khảo tài liệu của NSClient++ hoặc liên hệ với bộ phận hỗ trợ của Nagios XI để được trợ giúp thêm.
