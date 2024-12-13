# Hướng Dẫn Cài Đặt SSL Cho Website `nkbinh.shop` Trên Apache

## 1. Cài Đặt Let's Encrypt và Certbot
Đầu tiên, cài đặt Certbot và module SSL cho Apache:
```bash
sudo apt update
sudo apt install certbot python3-certbot-apache
```

## 2. Cấu Hình Apache Cho HTTP và HTTPS

### Bước 1: Cập Nhật File `000-default.conf` Cho HTTP
Sửa file cấu hình mặc định để hỗ trợ Let's Encrypt:
```bash
sudo nano /etc/apache2/sites-enabled/000-default.conf
```

Thêm nội dung sau:
```apache
<VirtualHost *:80>
    ServerName nkbinh.shop
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    # Logging
    LogLevel warn
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Allow access to the .well-known directory for Certbot
    <Directory "/var/www/html/.well-known/acme-challenge">
        AllowOverride None
        Options None
        Require all granted
    </Directory>
</VirtualHost>
```

Kiểm tra cấu hình và khởi động lại Apache:
```bash
sudo apache2ctl configtest
sudo systemctl restart apache2
```

### Bước 2: Tạo File Xác Thực Let's Encrypt (Tùy Chọn)
Kiểm tra quyền truy cập thư mục `.well-known`:
```bash
echo "test" | sudo tee /var/www/html/.well-known/acme-challenge/test
```
Mở trình duyệt truy cập `http://nkbinh.shop/.well-known/acme-challenge/test` để kiểm tra.

---

## 3. Cấp SSL Bằng Let's Encrypt
Chạy lệnh sau để tự động cấp SSL và cập nhật cấu hình Apache:
```bash
sudo certbot --apache -d nkbinh.shop
```

Certbot sẽ tự động:
1. Xác thực quyền sở hữu tên miền.
2. Cập nhật file cấu hình Apache cho HTTPS.
3. Tự động khởi động lại Apache.

---

## 4. Kiểm Tra File Cấu Hình HTTPS
Sau khi cài SSL, Certbot sẽ tạo file cấu hình HTTPS (ví dụ: `/etc/apache2/sites-available/nkbinh.shop.conf`). Nội dung file mẫu:
```apache
<VirtualHost *:443>
    ServerName nkbinh.shop
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/nkbinh.shop/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/nkbinh.shop/privkey.pem

    <Directory "/var/www/html/.well-known/acme-challenge">
        AllowOverride None
        Options None
        Require all granted
    </Directory>
</VirtualHost>
```

Kiểm tra cấu hình và khởi động lại Apache:
```bash
sudo apache2ctl configtest
sudo systemctl restart apache2
```

---

## 5. Gia Hạn Chứng Chỉ SSL
Chứng chỉ SSL của Let's Encrypt có hiệu lực trong 90 ngày. Để gia hạn tự động, thêm cron job:
```bash
sudo crontab -e
```

Thêm dòng sau để kiểm tra và gia hạn hàng ngày:
```cron
0 3 * * * certbot renew --quiet
```

---

## 6. Kiểm Tra Hoạt Động SSL
- Truy cập `https://nkbinh.shop` để kiểm tra.
- Sử dụng công cụ [SSL Labs](https://www.ssllabs.com/ssltest/) để đánh giá cấu hình SSL.

---
