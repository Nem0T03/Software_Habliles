# **Installation Guide for ProFTPD on Ubuntu**

## **Prerequisites** ✅
To install **ProFTPD** on your system, ensure you meet the following requirements:
1. **Ubuntu 22.04 Server** 🖥️
2. **Root access** or `sudo` privileges 🔑

---

## **Steps to Install ProFTPD** 📌

### **Step 1: Update and Upgrade the System** 🔄
- Update package lists:
  ```bash
  sudo apt-get update -y
  ```
- Upgrade system packages:
  ```bash
  sudo apt-get upgrade -y
  ```
- Reboot the system:
  ```bash
  reboot
  ```

### **Step 2: Install ProFTPD** 🛠️
- Install ProFTPD:
  ```bash
  sudo apt install proftpd -y
  ```
- Verify installation:
  ```bash
  sudo proftpd --version
  ```

### **Step 3: Start and Enable ProFTPD Service** ⚙️
- Start the service:
  ```bash
  sudo systemctl start proftpd
  ```
- Enable it at boot:
  ```bash
  sudo systemctl enable proftpd
  ```
- Check service status:
  ```bash
  sudo systemctl status proftpd
  ```

---

## **Configure ProFTPD** ⚡

### **Edit Configuration File** ✏️
```bash
sudo nano /etc/proftpd/proftpd.conf
```

### **Modify Key Directives** 🔧
- **Set default root directory**:
  ```conf
  DefaultRoot /home/Linux/Docs
  ```
  Or restrict access per user:
  ```conf
  DefaultRoot /home/linux Tom
  DefaultRoot / Emma
  ```
- **Set FTP server name**:
  ```conf
  ServerName "My ProFTPD"
  ```

---

## **Create a User for ProFTPD** 👤

### **Create a New User**
```bash
sudo useradd -m username
```

### **Set Password** 🔐
```bash
sudo passwd username
```

---

## **Enable SSL/TLS for ProFTPD** 🔒

### **Install OpenSSL**
```bash
sudo apt-get install openssl -y
```

### **Generate SSL Certificate** 🛡️
```bash
sudo openssl req -x509 -newkey rsa:1024 -keyout /etc/ssl/private/proftpd.key -out /etc/ssl/certs/proftpd.crt -nodes -days 365
```

### **Set Permissions**
```bash
sudo chmod 600 /etc/ssl/private/proftpd.key
sudo chmod 600 /etc/ssl/certs/proftpd.crt
```

### **Enable SSL in Configuration**
- Open the config file:
  ```bash
  sudo nano /etc/proftpd/proftpd.conf
  ```
- Uncomment the following line:
  ```conf
  Include /etc/proftpd/tls.conf
  ```
- Open TLS config file:
  ```bash
  sudo nano /etc/proftpd/tls.conf
  ```
- Uncomment and modify:
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

### **Restart ProFTPD Service** 🔄
```bash
sudo systemctl restart proftpd
```

---

## **Uninstall ProFTPD** ❌

### **Stop the Service** 🚫
```bash
sudo systemctl stop proftpd
```

### **Remove ProFTPD** 🗑️
```bash
sudo apt-get autoremove proftpd-dev
sudo apt-get purge proftpd-basic
```

After completing these steps, **ProFTPD** will be completely removed from the system.

