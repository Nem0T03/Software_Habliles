md### Hướng dẫn cài đặt và cấu hình DNS Server trên Windows Server 2022

#### **I. Chuẩn bị trước khi cài đặt**

1. **Yêu cầu hệ thống**:
   - **Phần cứng**:
     - Bộ xử lý: Hỗ trợ 64-bit.
     - RAM: Tối thiểu 2GB (khuyến nghị 4GB hoặc nhiều hơn).
     - Dung lượng ổ cứng: Tối thiểu 32GB trống.
   - **Phần mềm**:
     - Windows Server 2022 đã được cài đặt và cập nhật đầy đủ.

2. **Đặt IP tĩnh**:
   - Cần thiết để đảm bảo:
     - **Tính ổn định và nhất quán**: Các thiết bị trong mạng luôn có thể truy cập vào DNS Server.
     - **Quản lý dễ dàng**: Tránh phải cấu hình lại khi IP thay đổi.
     - **Tăng cường an ninh**: Giảm nguy cơ nhầm lẫn và tấn công từ IP động.

---

#### **II. Cài đặt DNS Server**

1. **Mở Server Manager**:
   - Truy cập **Server Manager** từ menu Start hoặc thanh taskbar.

2. **Thêm vai trò DNS Server**:
   - Nhấn **Add roles and features**.
   - Tại bảng **Add roles and features Wizard**:
     - Ở mục **Before you begin**:
       - Tick chọn **“Skips this page by default”** để bỏ qua trang giới thiệu trong lần cài đặt sau.
     - Ở mục **Installation Type**:
       - Chọn **“Role-based or feature-based installation”**.
     - Ở mục **Server Selection**:
       - Chọn **“Select a server from the server pool”** và chọn máy chủ hiện tại từ danh sách.
     - Ở mục **Server Roles**:
       - Tick chọn **“DNS Server”**.

3. **Cấu hình bổ sung**:
   - Tại mục **Features**, để mặc định và nhấn **Next**.
   - Tại bảng giới thiệu **DNS Server**, nhấn **Next**.

4. **Xác nhận và cài đặt**:
   - Ở mục **Confirmation**:
     - Tick chọn **“Restart the destination server automatically if required”** để tự khởi động lại máy chủ nếu cần.
     - Nhấn **Install** để bắt đầu cài đặt.

---

#### **III. Kiểm tra kết quả**

1. **Xác minh trong Server Manager**:
   - Sau khi cài đặt thành công, **DNS Server** sẽ xuất hiện trong danh sách **Server Group**.

2. **Truy cập DNS Manager**:
   - **Cách 1**: Từ **Server Manager** > **Tools** > chọn **DNS**.
   - **Cách 2**: Nhấn **Windows** > tìm kiếm **DNS**.

3. **Cấu hình DNS Server**:
   - Sử dụng DNS Manager để tạo và quản lý các vùng (zones), bản ghi (records), và thực hiện các cấu hình cần thiết.

---

### **Lưu ý**:
- Đảm bảo rằng IP tĩnh đã được đặt chính xác trước khi cấu hình DNS.
- Nếu xảy ra lỗi, kiểm tra trạng thái dịch vụ DNS bằng lệnh:
  ```powershell
  Get-Service -Name DNS
  ```
- Khởi động lại dịch vụ DNS nếu cần:
  ```powershell
  Restart-Service -Name DNS
  ```
