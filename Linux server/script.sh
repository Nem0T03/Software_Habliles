#!/bin/bash

# Đường dẫn tới file chứa mật khẩu SSH
password_file="/home/binh/password.txt"

# Thực hiện rsync với mật khẩu từ file
sudo rsync -avzhe "sshpass -f $password_file ssh"  binh@192.168.30.3:/var/www/html/mywebsite/ /var/www/html/mywebsite/
