mdDưới đây là hướng dẫn cài đặt Nagios XI trên Ubuntu 22.04. Hướng dẫn được cấu trúc để có thể áp dụng trong môi trường GitHub, bao gồm các bước chi tiết và cấu hình cần thiết:

---

# Cài Đặt Nagios XI trên Ubuntu 22.04

## Bước 1: Cập Nhật Các Gói Hệ Thống

Trước khi tiến hành cài đặt Nagios XI, bạn cần cập nhật các gói hệ thống để đảm bảo các phần mềm mới nhất được cài đặt.

```bash
sudo apt update && sudo apt upgrade -y
```

## Bước 2: Cài Đặt Các Gói Cần Thiết

Tiến hành cài đặt các gói phụ trợ cần thiết cho NagioXI và các thư viện phụ thuộc:

```bash
sudo apt install -y autoconf bc gawk dc build-essential gcc libc6 make wget unzip apache2 php libapache2-mod-php libgd-dev libmcrypt-dev make libssl-dev snmp libnet-snmp-perl gettext
```

## Bước 3: Tải Về và Giải Nén NagiosXI

Tạo một thư mục chứa mã nguồn và tải NagiosXI:

```bash
mkdir nagioscore
cd nagioscore
sudo wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.13.tar.gz
tar -xvf nagios-4.4.13.tar.gz
```

## Bước 4: Cài Đặt Nagios Core

Chuyển vào thư mục chứa mã nguồn và biên dịch Nagios:

```bash
cd /tmp
rm -rf nagiosxi xi*.tar.gz
wget http://assets.nagios.com/downloads/nagiosxi/xi-latest.tar.gz
tar xzf xi-latest.tar.gz
cd nagiosxi
./upgrade
```

Tạo user và group cho Nagios và thêm user Apache vào group Nagios:

```bash
make install-groups-users
usermod -a -G nagios www-data
make install
```

Cài đặt các script cho Nagios daemon và cấu hình Apache:

```bash
make install-daemoninit
make install-init
make install-config
make install-webconf
a2enmod rewrite cgi
```

Tạo tài khoản admin cho Nagios:

```bash
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
```

## Bước 5: Cài Đặt và Cấu Hình Plugin Nagios và NRPE

Cài đặt các plugin giám sát Nagios và NRPE:

```bash
sudo apt install monitoring-plugins nagios-nrpe-plugin -y
```

Cấu hình các plugin bằng cách chỉnh sửa các tập tin cấu hình của Nagios:

```bash
cd /usr/local/nagios/etc/
mkdir servers
vi nagios.cfg
```

Mở dòng cấu hình `cfg_dir=/usr/local/nagios/etc/servers` và chỉnh sửa các tệp `resource.cfg` và `objects/contacts.cfg`. Thêm đường dẫn plugin giám sát:

```bash
$USER1$=/usr/lib/nagios/plugins
```

Chỉnh sửa file `objects/commands.cfg`:

```bash
define command{
        command_name check_nrpe
        command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}
```

## Bước 6: Mở Port Trên Firewall

Mở các port cần thiết cho Nagios qua firewall:

```bash
sudo ufw enable
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 22
sudo ufw reload
sudo ufw status
```

## Bước 7: Khởi Động Lại Dịch Vụ và Kiểm Tra Trạng Thái

Khởi động lại dịch vụ Nagios và Apache:

```bash
sudo systemctl restart apache2
sudo systemctl restart nagios4
```

Thiết lập các dịch vụ tự động khởi động khi hệ thống khởi động lại:

```bash
sudo systemctl enable apache2
sudo systemctl enable nagios4
```

Kiểm tra trạng thái của các dịch vụ:

```bash
sudo systemctl status apache2
sudo systemctl status nagios4
```

## Bước 8: Truy Cập Web Nagios

Để truy cập giao diện web Nagios, bạn có thể sử dụng trình duyệt web trên máy tính local của mình. Trong thanh địa chỉ, nhập địa chỉ IP hoặc tên miền của máy chủ Ubuntu theo cú pháp sau:

```
http://your_server_ip/nagios
```

Hoặc

```
http://your_domain/nagios
```

---

### Tham Khảo:

- **Tài liệu chính thức Nagios Core**: [Nagios Documentation](https://www.nagios.org/documentation/)
- **Nagios XI Documentation**: [Nagios XI Documentation](https://support.nagios.com/kb/)

---

Cách tiếp cận này giúp bạn có thể dễ dàng triển khai và quản lý Nagios trên Ubuntu 22.04.
