### Hướng dẫn thiết lập NIC Teaming trên Windows Server

#### **Thiết lập NIC Teaming qua GUI (Graphical User Interface):**

1. **Mở Server Manager**:
   - Truy cập **Server Manager** từ menu Start hoặc thanh taskbar.
   - Chọn **Local Server**.

2. **Bật NIC Teaming**:
   - Tìm mục **Properties** trong Server Manager.
   - Chọn **NIC Teaming** > trạng thái **Disabled** > nhấn để mở cửa sổ cấu hình.

3. **Chọn Network Adapter**:
   - Trong cửa sổ NIC Teaming, nhìn góc dưới bên phải, tại phần **Adapters and Interfaces**.
   - Chọn các card mạng bạn muốn thêm vào nhóm NIC Team.

4. **Tạo Team**:
   - Nhấn vào **TASKS** > chọn **Add to New Team**.

5. **Cấu hình Team**:
   - Một hộp thoại mới xuất hiện, hiển thị các bộ điều hợp mạng và các thành viên.
   - **Nhập tên** cho nhóm NIC Team.

6. **Cấu hình bổ sung**:
   - Chọn **Additional Properties** ở dưới cùng:
     - **Switch Independent**: Hoạt động độc lập với switch.
     - **Static**: Phụ thuộc vào cấu hình tĩnh trên switch.
     - **LACP (Link Aggregation Control Protocol)**: Hỗ trợ cấu hình động trên switch.
   - **Chế độ cân bằng tải**: Chọn **Dynamic** để đạt hiệu suất tốt nhất.

7. **Hoàn tất**:
   - Nhấn **OK** để hoàn thành. Nhóm NIC Team mới sẽ được tạo.

---

#### **Thiết lập NIC Teaming bằng PowerShell:**

1. **Mở PowerShell**:
   - Gõ **PowerShell** vào thanh tìm kiếm và nhấn Enter.

2. **Kiểm tra các Network Adapter**:
   - Nhập lệnh:
     ```powershell
     Get-NetAdapter
     ```
   - Danh sách các card mạng hiện tại sẽ hiển thị.

3. **Tạo NIC Team**:
   - Sử dụng lệnh sau:
     ```powershell
     New-NetLbfoTeam "Team1" "NIC1", "NIC2"
     ```
     - **"Team1"**: Tên nhóm NIC Team.
     - **"NIC1", "NIC2"**: Tên các card mạng đã chọn. Bạn có thể thêm nhiều card mạng nếu cần.

4. **Xác minh cấu hình**:
   - Sử dụng lệnh:
     ```powershell
     Get-NetLbfoTeam
     ```
   - Hiển thị thông tin nhóm vừa tạo.

5. **Kiểm tra trạng thái nhóm**:
   - Sử dụng lệnh sau để kiểm tra trạng thái nhóm và các thành viên:
     ```powershell
     Get-NetLbfoTeam -Name Team1
     Get-NetAdapter -Name Team1
     ```

   - Trạng thái của nhóm sẽ hiển thị **Up/Active** hoặc **Up/Standby**.

---

### **Lưu ý**:
- **Switch Independent** phù hợp nếu không sử dụng switch hỗ trợ LACP.
- **Dynamic** được khuyến nghị để tối ưu hóa cân bằng tải và hiệu suất.
- Đảm bảo các card mạng được kết nối và hoạt động ổn định trước khi cấu hình.
