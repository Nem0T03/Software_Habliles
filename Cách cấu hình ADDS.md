### **Hướng Dẫn Cấu Hình Hệ Thống Domain Controller và Client (PC01 & PC02)**  

---

#### **1. Cấu hình Domain Controller (PC01)**  
**Bước 1:** Trên PC01, chuột phải vào biểu tượng card mạng > chọn **Open Network and Sharing Center** > **Change Adapter Settings**.  
**Bước 2:** Chuột phải vào card **External**, chọn **Properties**.  
- Bỏ chọn ô **Internet Protocol Version 6 (TCP/IPv6)**.  
- Chọn **Internet Protocol Version 4 (TCP/IPv4)** > nhấn **Properties**.  

**Bước 3:** Trong ô **Preferred DNS server**, nhập **192.168.1.1** (IP của PC01). Nhấn **OK** hai lần để lưu.  

**Bước 7:** Trong cửa sổ **Select Features**, nhấn **Next** hai lần.  
**Bước 8:** Tại **Confirm installation selections**, nhấn **Install**.  

**Bước 9:** Sau khi cài đặt thành công, chọn **Promote this server to a domain controller** tại cửa sổ **Installation Progress**.  
**Bước 10:** Trong **Deployment Configuration**, chọn **Add a new forest**.  
- Nhập tên miền (VD: `DOM01.LOCAL`) vào **Root domain name**, chọn **Next**.  
- Trong **Domain Controller Options**, nhập mật khẩu **P@ssword**, chọn **Next** bốn lần.  

**Bước 12:** Tại **Prerequisites Check**, chọn **Install**.  
**Bước 13:** Sau khi cài đặt xong, máy sẽ tự động khởi động lại.  
- Đăng nhập với tài khoản: `DOM01\Administrator`.  

---

#### **2. Thêm Máy Trạm Vào Domain (PC02)**  
**Bước 4:** Chuột phải biểu tượng **This PC** trên Desktop > chọn **Properties**.  
**Bước 5:** Trong cửa sổ **System**, chọn **Change settings**.  
**Bước 6:** Trong cửa sổ **System Properties**, chọn **Change**.  
**Bước 7:** Chọn **Domain**, nhập **DOM01.LOCAL**, chọn **OK**.  

**Bước 8:** Hộp thoại **Windows Security** xuất hiện:  
- Nhập `DOM01\Administrator` vào ô **Username**.  
- Nhập **P@ssword** vào ô **Password** > nhấn **OK** ba lần.  
- Nhấn **Close**, chọn **Restart Now** để khởi động lại.  

**Bước 9:** Sau khi khởi động, đăng nhập bằng: `DOM01\Administrator`.  

---

#### **3. Cấu hình Group Policy trên Domain Controller (PC01)**  
**a. Cấu hình cho phép đặt mật khẩu đơn giản:**  
**Bước 1:** Mở **Server Manager**, vào menu **Tools**, chọn **Group Policy Management**.  
**Bước 2:** Truy cập: **Forest: DOM01.LOCAL > Domains > DOM01.LOCAL**. Chuột phải **Default Domain Policy**, chọn **Edit**.  
**Bước 3:** Theo đường dẫn:  
**Computer Configuration > Windows Settings > Security Settings > Account Policy > Password Policy**.  

**Bước 4:** Sửa các giá trị:  
- **Enforce password history:** `0`.  
- **Maximum password age:** `0`.  
- **Minimum password length:** `0`.  
- **Password must meet complexity requirements:** `Disabled`.  

**Bước 5:** Sau khi chỉnh sửa, mở CMD và chạy lệnh: `Gpupdate /Force`.  

---

**b. Cấu hình cho phép Group Users log on trên DC:**  
**Bước 1:** Truy cập: **Forest: DOM01.LOCAL > Domains > DOM01.LOCAL > Domain Controllers**.  
- Chuột phải **Default Domain Controllers Policy**, chọn **Edit**.  
**Bước 2:** Theo đường dẫn:  
**Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User Rights Assignment**.  

**Bước 3:** Double click **Allow log on locally**, chọn **Add User or Group**.  
- Nhập **Users**, nhấn **Check Names**, chọn **OK** hai lần.  

**Bước 4:** Chạy lệnh `Gpupdate /Force` trong CMD.  

---

**c. Tạo User Domain và kiểm tra:**  
**Bước 1:** Mở **Server Manager**, vào menu **Tools**, chọn **Active Directory Users and Computers**.  
**Bước 2:** Chuột phải **Users**, chọn **New > User**.  
**Bước 3:** Nhập thông tin user (VD: `u1`), đặt mật khẩu là `123`, tích chọn **Password never expires**.  
- Nhấn **Next** và **Finish**.  

**Bước 4:** Tạo thêm user `u2` tương tự.  
**Bước 5:** Đăng xuất tài khoản `Administrator` và lần lượt đăng nhập `u1` và `u2` trên PC01.  

---

#### **4. Cài Remote Server Administrator Tools (PC02)**  
**Bước 1:** Đăng nhập tài khoản: `DOM01\Administrator`.  
- Sao chép file **WindowsTH-RSAT_WS_1803-x64** vào ổ C và chạy file.  
**Bước 2:** Chọn **Yes**, sau đó chọn **I accept**.  
**Bước 3:** Sau khi cài đặt xong, nhấn **Close**.  

Kiểm tra tại **Start > Windows Administrative Tools > Active Directory Users and Computers**.  

---

#### **5. Run As Administrator (PC02)**  
**Bước 1:** Đăng nhập tài khoản `DOM01\u1`.  
**Bước 2:** Chuột phải **Active Directory Users and Computers**, chọn **Run as administrator**.  
**Bước 3:** Nhập thông tin `DOM01\Administrator` và mật khẩu **P@ssword**.  
- Thử tạo user mới (VD: `u4`).  

--- 
