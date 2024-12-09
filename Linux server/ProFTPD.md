### Điều kiện để cài đặt ProFTPD

Để cài đặt **ProFTPD** trên hệ thống, bạn cần đáp ứng các điều kiện sau:  
1. **Máy chủ Ubuntu 22.04**  
2. **Quyền root** hoặc quyền `sudo` trên máy chủ  

---

### Hướng dẫn cài đặt ProFTPD trên Ubuntu

#### Bước 1: **Cập nhật và nâng cấp hệ thống**
- Cập nhật danh sách gói:
  ```bash
  sudo apt-get update -y
  ```
- Nâng cấp hệ thống:
  ```bash
  sudo apt-get upgrade -y
  ```
- Khởi động lại hệ thống:
  ```bash
  reboot
  ```

#### Bước 2: **Cài đặt ProFTPD**
- Cài đặt ProFTPD:
  ```bash
  sudo apt install proftpd -y
  ```
- Kiểm tra phiên bản để đảm bảo cài đặt thành công:
  ```bash
  sudo proftpd --version
  ```

#### Bước 3: **Kích hoạt dịch vụ ProFTPD**
- Khởi động dịch vụ:
  ```bash
  sudo systemctl start proftpd
  ```
- Kích hoạt dịch vụ khởi động cùng hệ thống:
  ```bash
  sudo systemctl enable proftpd
  ```
- Kiểm tra trạng thái:
  ```bash
  sudo systemctl status proftpd
  ```

---

### Định cấu hình ProFTPD

#### Mở tệp cấu hình:
```bash
sudo nano /etc/proftpd/proftpd.conf
```

#### Chỉnh sửa các chỉ thị quan trọng:
- **Đặt thư mục gốc mặc định**:
  ```conf
  DefaultRoot /home/Linux/Docs
  ```
  Hoặc cấu hình giới hạn quyền truy cập cho từng người dùng:
  ```conf
  DefaultRoot /home/linux Tom
  DefaultRoot / Emma
  ```
- **Đặt tên cho máy chủ FTP**:
  ```conf
  ServerName "My ProFTPD"
  ```

---

### Tạo người dùng cho ProFTPD

#### Tạo người dùng:
```bash
sudo useradd -m username
```

#### Đặt mật khẩu:
```bash
sudo passwd username
```

---

### Cấu hình SSL/TLS cho ProFTPD

#### Cài đặt OpenSSL:
```bash
sudo apt-get install openssl -y
```

#### Tạo chứng chỉ SSL/TLS:
```bash
sudo openssl req -x509 -newkey rsa:1024 -keyout /etc/ssl/private/proftpd.key -out /etc/ssl/certs/proftpd.crt -nodes -days 365
```

#### Cấp quyền cho chứng chỉ:
```bash
sudo chmod 600 /etc/ssl/private/proftpd.key
sudo chmod 600 /etc/ssl/certs/proftpd.crt
```

#### Kích hoạt SSL trong cấu hình:
- Mở tệp cấu hình:
  ```bash
  sudo nano /etc/proftpd/proftpd.conf
  ```
- Bỏ dấu `#` ở dòng:
  ```conf
  Include /etc/proftpd/tls.conf
  ```
- Mở tệp TLS:
  ```bash
  sudo nano /etc/proftpd/tls.conf
  ```
- Bỏ ghi chú (uncomment) các dòng:
  ```conf
  <IfModule mod_tls.c>
  TLSEngine on
  TLSLog /var/log/proftpd/tls.log
  TLSProtocol SSLv23

  TLSRSACertificateFile /etc/ssl/certs/proftpd.crt
  TLSRSACertificateKeyFile /etc/ssl/private/proftpd.key

  TLSOptions AllowClientRenegotiations
  TLSRequired on
  ```

#### Khởi động lại dịch vụ để áp dụng thay đổi:
```bash
sudo systemctl restart proftpd
```

---

### Gỡ cài đặt ProFTPD

#### Dừng dịch vụ:
```bash
sudo systemctl stop proftpd
```

#### Gỡ cài đặt:
```bash
sudo apt-get autoremove proftpd-dev
sudo apt-get purge proftpd-basic
```

Sau khi thực hiện các bước trên, **ProFTPD** sẽ được xóa hoàn toàn khỏi hệ thống.
