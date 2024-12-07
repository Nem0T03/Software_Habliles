### **Bước 1: Cài đặt DHCP Server**
1. **Mở Server Manager**:
   - Truy cập từ menu Start, chọn *Server Manager*.
   - Nhấn vào *Add Roles and Features* và chọn *Next*.
   
2. **Chọn Installation Type**:
   - Chọn *Role-Based or Feature-Based Installation*, sau đó nhấn *Next*.

3. **Chọn máy chủ để cài đặt**:
   - Lựa chọn máy chủ từ danh sách, nhấn *Next*.

4. **Thêm vai trò DHCP Server**:
   - Chọn *DHCP Server* từ danh sách vai trò.
   - Thêm *Management Tools* nếu cần, nhấn *Next* và xác nhận.

5. **Xác nhận cài đặt**:
   - Nhấn *Install*. Sau khi hoàn tất, đóng cửa sổ và chuyển sang cấu hình.

---

### **Bước 2: Cấu hình sau triển khai**
1. **Hoàn tất cài đặt sau triển khai**:
   - Trong *Server Manager*, chọn *DHCP*.
   - Nhấp vào cảnh báo vàng và chọn *Complete DHCP Configuration*.
   - Chọn *Skip AD authorization* nếu máy chủ không thuộc Active Directory.

2. **Cấu hình DHCP trong Server Manager**:
   - Truy cập *Tools* > *DHCP* để mở bảng điều khiển DHCP.

---

### **Bước 3: Tạo Scope mới**
1. **Thêm Scope**:
   - Trong bảng điều khiển DHCP, nhấp chuột phải vào *IPv4* > *New Scope*.

2. **Đặt tên Scope**:
   - Nhập tên và mô tả cho Scope, nhấn *Next*.

3. **Thiết lập dải IP**:
   - Nhập *IP bắt đầu* và *IP kết thúc*, mặt nạ mạng con. Nhấn *Next*.

4. **Loại trừ IP (nếu cần)**:
   - Loại trừ các IP cần giữ lại (như máy in, thiết bị mạng khác).

5. **Thiết lập thời gian thuê (Lease Duration)**:
   - Đặt thời gian cho phép mượn IP, nhấn *Next*.

---

### **Bước 4: Cấu hình thêm**
1. **Gateway mặc định (Default Gateway)**:
   - Nhập địa chỉ Gateway, nhấn *Add*, sau đó *Next*.

2. **Domain Name và DNS Servers**:
   - Cung cấp thông tin DNS, nhấn *Next*.

3. **Cài đặt tùy chọn WINS (nếu cần)**:
   - Nhập thông tin WINS Server hoặc bỏ qua.

4. **Kích hoạt Scope**:
   - Chọn kích hoạt ngay hoặc sau, nhấn *Next* và hoàn tất.

---

### **Bước 5: Kiểm tra và xác minh**
1. **Kiểm tra Scope**:
   - Đảm bảo cấu hình Scope đã hoạt động trong bảng điều khiển DHCP.

2. **Cấu hình máy khách DHCP**:
   - Thiết lập các thiết bị trên mạng để nhận IP tự động từ máy chủ DHCP.

---

### **Mở bảng điều khiển DHCP**
- **Cách 1**: Từ *Windows Administrative Tools*.
- **Cách 2**: Truy cập từ menu *Tools* trong *Server Manager*.
- **Cách 3**: Sử dụng lệnh `dhcpmgmt.msc` trong hộp thoại *Run*.
- **Cách 4**: Tìm kiếm trực tiếp từ menu *Start*.

---
