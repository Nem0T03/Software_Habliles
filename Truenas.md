
### **1. Yêu cầu hệ thống**
- **Phần cứng:**
  1. CPU: Bộ xử lý 64-bit (khuyến nghị Intel/AMD với hỗ trợ ảo hóa nếu dùng ZFS).
  2. RAM: Tối thiểu 8GB (khuyến nghị 16GB+ nếu dùng ZFS).
  3. Ổ cứng: Tối thiểu 2 ổ đĩa (một cho hệ thống và một cho lưu trữ dữ liệu).
  4. Kết nối mạng: 1 cổng Ethernet (khuyến nghị 2+ để sử dụng tính năng liên kết).

- **Phần mềm:**
  - Tải xuống ISO của TrueNAS từ trang chính thức: [truenas.com](https://www.truenas.com/download-truenas-core/).

---

### **2. Cài đặt TrueNAS**

#### **Bước 1: Tải và chuẩn bị USB Boot**
1. Tải xuống file ISO của TrueNAS.
2. Sử dụng phần mềm như **Rufus**, **Etcher**, hoặc **Balena Etcher** để tạo USB boot từ file ISO.

#### **Bước 2: Cài đặt TrueNAS**
1. Khởi động máy tính từ USB boot:
   - Vào BIOS/UEFI và thiết lập thứ tự khởi động (Boot Order) ưu tiên USB.
2. Chọn **Install/Upgrade** khi giao diện cài đặt xuất hiện.
3. Chọn ổ đĩa để cài đặt hệ thống (ổ này sẽ chỉ dành cho hệ điều hành, không dùng để lưu trữ dữ liệu).
4. Đặt mật khẩu cho tài khoản **root**.
5. Chờ quá trình cài đặt hoàn tất và khởi động lại hệ thống.

---

### **3. Truy cập và cấu hình cơ bản TrueNAS**

#### **Bước 1: Truy cập giao diện web**
1. Sau khi cài đặt, TrueNAS sẽ hiển thị địa chỉ IP để truy cập.  
   Ví dụ: `http://192.168.1.100`.
2. Sử dụng trình duyệt web để truy cập địa chỉ này.

#### **Bước 2: Đăng nhập**
- Sử dụng tài khoản:
  - **Username**: `root`
  - **Password**: Mật khẩu đã đặt trong quá trình cài đặt.

#### **Bước 3: Cấu hình cơ bản**
1. **Đổi hostname**:  
   Vào **System** → **General** → Thay đổi **Hostname** để đặt tên cho hệ thống.
2. **Cấu hình địa chỉ IP tĩnh** (nếu cần):  
   Vào **Network** → **Interfaces** → Chỉnh sửa interface chính để đặt IP tĩnh.

---

### **4. Cấu hình lưu trữ trên TrueNAS**

#### **Bước 1: Thiết lập Pool (dung lượng lưu trữ)**
1. Vào **Storage** → **Pools** → Nhấn **Add**.
2. Chọn **Create a new pool** → Đặt tên cho pool.
3. Thêm các ổ đĩa cứng vào pool:
   - Chọn RAID-Z1, RAID-Z2 hoặc RAID-Z3 tùy nhu cầu.
4. Xác nhận và khởi tạo pool.

#### **Bước 2: Tạo Dataset (phân vùng lưu trữ)**
1. Vào **Storage** → **Pools** → Chọn pool vừa tạo.
2. Nhấn **Add Dataset** để tạo thư mục ảo cho dữ liệu.

#### **Bước 3: Cấu hình chia sẻ dữ liệu**
- **SMB (Windows Share):**
  1. Vào **Sharing** → **Windows Shares (SMB)** → Nhấn **Add**.
  2. Chọn dataset vừa tạo làm thư mục chia sẻ.
  3. Đặt quyền truy cập (Read/Write).
- **NFS (Linux/Unix Share):**
  1. Vào **Sharing** → **Unix Shares (NFS)** → Nhấn **Add**.
  2. Chọn dataset và thiết lập quyền truy cập.
- **iSCSI (Enterprise):**
  1. Vào **Sharing** → **Block (iSCSI)** → Cấu hình Target và Extents.

---

### **5. Cấu hình bảo mật**

1. **Cập nhật TrueNAS:**  
   Vào **System** → **Update** để kiểm tra và cài đặt bản vá mới.
2. **Thiết lập SSL:**  
   Vào **System** → **Certificates** → Tạo hoặc tải lên chứng chỉ SSL.
3. **Quản lý tài khoản người dùng:**  
   - Tạo tài khoản mới qua **Accounts** → **Users**.
   - Phân quyền phù hợp cho từng tài khoản.

---

### **6. Quản lý và bảo trì**

1. **Giám sát hệ thống:**
   - Vào **Reporting** để theo dõi hiệu năng (CPU, RAM, Disk, Network).
2. **Cấu hình cảnh báo (Alert):**
   - Vào **System** → **Alert Settings** để cấu hình email nhận thông báo.
3. **Sao lưu cấu hình:**
   - Vào **System** → **Backup** → Tải xuống file cấu hình để khôi phục khi cần.

---

### **7. Gỡ lỗi và hỗ trợ**
- Kiểm tra nhật ký hệ thống:
  ```bash
  tail -f /var/log/messages
  ```
- Đặt lại mật khẩu root nếu quên:
  ```bash
  boot -s  # Chế độ single-user mode
  passwd root
  ```

---
