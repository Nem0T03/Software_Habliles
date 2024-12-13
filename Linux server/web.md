---

# Hướng Dẫn Triển Khai Website Trên Linux

## 1. Yêu Cầu Hệ Thống
### Cài đặt các phần mềm cần thiết:
- **Git**: Để quản lý mã nguồn.
- **Apache/Nginx**: Máy chủ web.
- **PHP** (nếu là trang PHP).
- **MySQL/MariaDB** (nếu cần cơ sở dữ liệu).
- **Node.js** (nếu là ứng dụng Node.js).

## 2. Các Bước Triển Khai

### Bước 1: Cài Đặt Các Phần Mềm Cần Thiết
```bash
# Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# Cài đặt Apache hoặc Nginx
sudo apt install apache2 -y
# hoặc
sudo apt install nginx -y

# Cài đặt PHP (nếu cần)
sudo apt install php libapache2-mod-php -y

# Cài đặt MySQL/MariaDB (nếu cần)
sudo apt install mysql-server -y
sudo mysql_secure_installation

# Cài đặt Git
sudo apt install git -y
```

### Bước 2: Clone Dự Án Từ GitHub
```bash
# Tạo thư mục chứa dự án
cd /var/www/html
sudo mkdir mywebsite
sudo chown $USER:$USER mywebsite

# Clone dự án
cd mywebsite
git clone https://github.com/username/repository.git .
```

### Bước 3: Cấu Hình Máy Chủ Web
#### Với Apache:
- Tạo file cấu hình mới:
```bash
sudo nano /etc/apache2/sites-available/mywebsite.conf
```
- Thêm nội dung sau:
```apache
<VirtualHost *:80>
    ServerAdmin admin@example.com
    DocumentRoot /var/www/html/mywebsite
    ServerName example.com
    ServerAlias www.example.com

    <Directory /var/www/html/mywebsite>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- Kích hoạt site và khởi động lại Apache:
```bash
sudo a2ensite mywebsite.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

#### Với Nginx:
- Tạo file cấu hình mới:
```bash
sudo nano /etc/nginx/sites-available/mywebsite
```
- Thêm nội dung sau:
```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    root /var/www/html/mywebsite;
    index index.html index.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```
- Kích hoạt site và khởi động lại Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/mywebsite /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Bước 4: Cấu Hình Tên Miền (nếu có)
- Cập nhật DNS để trỏ tên miền tới địa chỉ IP của server.
- Sử dụng Let’s Encrypt để cài đặt chứng chỉ SSL:
```bash
sudo apt install certbot python3-certbot-apache
sudo certbot --apache
```

### Bước 5: Kiểm Tra Website
- Mở trình duyệt và truy cập `http://<địa_chỉ_IP>` hoặc tên miền của bạn.

### Bước 6: Tự Động Hóa (Tùy chọn)
- Sử dụng **cron job** để cập nhật mã nguồn tự động:
```bash
crontab -e
# Thêm dòng sau để pull mã nguồn mỗi ngày
0 2 * * * cd /var/www/html/mywebsite && git pull
```

---

## 3. Kết Luận
Bạn đã triển khai thành công website trên Linux. Nếu gặp lỗi, kiểm tra file log ở:
- Apache: `/var/log/apache2/error.log`
- Nginx: `/var/log/nginx/error.log`

--- 
