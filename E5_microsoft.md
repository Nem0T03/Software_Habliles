### Các bước tạo tài khoản Microsoft 365 Developer:
1. **Truy cập Microsoft 365 Developer Program**.
2. Chọn **“Join Now”** để bắt đầu.
3. Đăng nhập bằng tài khoản Microsoft sẵn có hoặc đăng ký mới.
4. Nhập tên công ty (bất kỳ tên nào).
5. Chọn các tùy chọn mặc định và nhấn **Next**.
6. **Chọn “Set up E5 subscription”**.
7. Nhập các thông tin yêu cầu và nhấn **Continue**.
8. Nhập số điện thoại và chọn **“Send Code”**.
9. Nhập mã xác nhận và hoàn tất quá trình cấu hình.
10. Tài khoản E5 sẽ hoạt động trong 3 tháng, sau đó có thể gia hạn tự động nếu tài khoản hoạt động bình thường.

### Quản lý và cấu hình tài khoản:
1. Truy cập **admin.microsoft.com** và đăng nhập bằng tài khoản quản trị.
2. Thêm người dùng mới trong mục **User management**.
3. Để nâng cấp dung lượng OneDrive lên 5TB:
   - Vào mục **OneDrive > Storage used > Edit**.
   - Nếu không thấy nút **Edit**, đăng nhập vào **portal.office.com/onedrive** để kích hoạt OneDrive.

### Thêm tên miền tùy chỉnh:
1. Truy cập **https://aka.ms/SPORenameAddDomain** và đăng nhập vào tài khoản quản trị.
2. Thêm tên miền tùy chỉnh và thực hiện các bước cấu hình DNS.
3. Đổi tên miền bằng **SharePoint Online Management Shell**:
   - Kết nối với **SPOService**.
   - Sử dụng lệnh: `Start-SPOTenantRename -DomainName "<DomainName>" -ScheduledDateTime "<YYYY-MM-DDTHH:MM:SS>"`.

### Thêm domain riêng:
1. Truy cập **admin.microsoft.com** và chọn **“Go to guided setup”**.
2. Tại mục **“Install Office”**, chọn **“Continue”**.
3. Nhập tên miền và thực hiện xác minh qua **Cloudflare** hoặc dịch vụ DNS khác.
4. Thêm các bản ghi DNS cần thiết để hoàn tất xác minh.

