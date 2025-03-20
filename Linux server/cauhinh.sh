#!/bin/bash

# Kiểm tra thông tin hệ thống
echo "===== THÔNG TIN HỆ THỐNG ====="
uname -a

echo -e "\n===== THÔNG TIN CPU ====="
lscpu | grep "Model name"

echo -e "\n===== THÔNG TIN RAM ====="
free -h

echo -e "\n===== DUNG LƯỢNG Ổ ĐĨA ====="
df -h /

echo -e "\n===== ĐỊA CHỈ IP ====="
ip a | grep inet | grep -v "127.0.0.1"

echo -e "\n===== TRẠNG THÁI DỊCH VỤ QUAN TRỌNG ====="
systemctl is-active sshd
systemctl is-active apache2 2>/dev/null || systemctl is-active httpd 2>/dev/null

echo -e "\n===== THÔNG TIN ĐĨA CỨNG ====="
lsblk

echo -e "\n===== KIỂM TRA CÁC CỔNG MỞ ====="
netstat -tulnp | grep LISTEN
