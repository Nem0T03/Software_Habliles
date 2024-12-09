### **Cài Đặt Agent NRPE cho Linux (Nagios XI)**

Dưới đây là hướng dẫn chi tiết về cách cài đặt **Linux NRPE Agent** cho Nagios XI trên các bản phân phối hỗ trợ, bao gồm RHEL/CentOS/Oracle Linux/CloudLinux, Fedora, SLES, OpenSUSE, Ubuntu và Debian.

---

#### **1. Các bản phân phối hỗ trợ**
- RHEL/CentOS/Oracle Linux/CloudLinux 5+
- Fedora 14+
- SLES 11+
- OpenSUSE 11+
- Ubuntu 12+
- Debian 6+

#### **2. Cài Đặt Agent trên Linux**

1. **Tải về Linux NRPE Agent**  
   Truy cập vào thư mục `/tmp` trên máy chủ Linux mà bạn muốn giám sát, rồi tải về tệp cài đặt từ Nagios:

   ```bash
   cd /tmp
   wget https://assets.nagios.com/downloads/nagiosxi/agents/linux-nrpe-agent.tar.gz
   ```

2. **Giải nén tệp tải về**

   Sau khi tải tệp `.tar.gz`, giải nén tệp:

   ```bash
   tar xzf linux-nrpe-agent.tar.gz
   ```

3. **Chuyển vào thư mục con vừa tạo**

   Đổi thư mục sang thư mục vừa giải nén:

   ```bash
   cd linux-nrpe-agent
   ```

4. **Chạy script cài đặt**

   Tiến hành cài đặt bằng cách chạy script dưới quyền root. Nếu bạn sử dụng Ubuntu, bạn cần chạy với quyền sudo (hoặc sử dụng `sudo -i` để chuyển sang root):

   ```bash
   ./fullinstall
   ```

#### **3. Lựa chọn chế độ cài đặt**
- Bạn có thể chọn chế độ cài đặt cho NRPE bằng cách sử dụng tùy chọn `-m`. Có hai chế độ cài đặt:
  - **xinetd mode**: Cài đặt NRPE dưới hệ thống init `xinetd`.
  - **daemon mode**: Cài đặt NRPE dưới hệ thống `systemd`.

  Lưu ý:
  - Các bản phân phối mới hơn như CentOS Stream 9 có thể không hỗ trợ gói `xinetd`. Trong trường hợp này, hệ thống sẽ tự động cài đặt dưới chế độ `daemon`.

#### **4. Cài đặt yêu cầu**
Khi chạy script `fullinstall`, nó sẽ tự động:
- Cập nhật các kho phần mềm của hệ điều hành.
- Cài đặt các gói phần mềm cần thiết.
- Tạo người dùng và nhóm cần thiết.
- Định nghĩa các dịch vụ cho `xinetd` (nếu sử dụng).
- Biên dịch và cài đặt agent và các plugin.
- Cấu hình tường lửa.
- Cấu hình agent.

#### **5. Cấu hình kết nối**
Khi script chạy, nó sẽ yêu cầu bạn nhập địa chỉ IP của máy chủ giám sát Nagios của bạn. Bạn có thể nhập:
- Một địa chỉ duy nhất.
- Một danh sách các địa chỉ, phân cách bằng dấu cách.
- Một dải địa chỉ với định dạng CIDR, ví dụ: `10.25.0.0/16`.

Điều này sẽ cấu hình daemon `xinetd` để cho phép kết nối từ các địa chỉ này tới quá trình agent.

---

#### **Lưu ý:**
- Khi nâng cấp Agent trên các hệ thống đã được giám sát, bạn có thể cần phải xóa cấu hình `xinetd` hoặc `systemd` hiện tại nếu bạn đã thay đổi chế độ cài đặt qua các lần nâng cấp.

### **Tóm tắt các bước cài đặt**
1. Tải tệp cài đặt từ link của Nagios.
2. Giải nén và vào thư mục cài đặt.
3. Chạy script cài đặt với quyền root (`./fullinstall`).
4. Cấu hình địa chỉ IP của máy chủ giám sát khi được yêu cầu.
5. Chọn chế độ cài đặt (`xinetd` hoặc `daemon`).
6. Quá trình cài đặt sẽ tự động hoàn tất.

Hy vọng hướng dẫn này giúp bạn dễ dàng cài đặt và cấu hình Agent NRPE cho Nagios XI trên máy chủ Linux của mình. Nếu có bất kỳ câu hỏi hoặc vấn đề gì trong quá trình cài đặt, đừng ngần ngại yêu cầu trợ giúp thêm.
