# Website Deployment Guide on Linux

## 1. System Requirements
### Install the necessary software:
- **Git**: For source code management.
- **Apache/Nginx**: Web server.
- **PHP** (if deploying a PHP website).
- **MySQL/MariaDB** (if a database is required).
- **Node.js** (if deploying a Node.js application).

## 2. Deployment Steps

### Step 1: Install Required Software
```bash
# Update the system
sudo apt update && sudo apt upgrade -y

# Install Apache or Nginx
sudo apt install apache2 -y
# or
sudo apt install nginx -y

# Install PHP (if needed)
sudo apt install php libapache2-mod-php -y

# Install MySQL/MariaDB (if needed)
sudo apt install mysql-server -y
sudo mysql_secure_installation

# Install Git
sudo apt install git -y
```

### Step 2: Clone the Project from GitHub
```bash
# Create a directory for the project
cd /var/www/html
sudo mkdir mywebsite
sudo chown $USER:$USER mywebsite

# Clone the project
cd mywebsite
git clone https://github.com/username/repository.git .
```

### Step 3: Configure the Web Server
#### For Apache:
- Create a new configuration file:
```bash
sudo nano /etc/apache2/sites-available/mywebsite.conf
```
- Add the following content:
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
- Enable the site and restart Apache:
```bash
sudo a2ensite mywebsite.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

#### For Nginx:
- Create a new configuration file:
```bash
sudo nano /etc/nginx/sites-available/mywebsite
```
- Add the following content:
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
- Enable the site and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/mywebsite /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 4: Configure the Domain Name (if applicable)
- Update DNS records to point your domain to the server's IP address.
- Use Let’s Encrypt to install an SSL certificate:
```bash
sudo apt install certbot python3-certbot-apache
sudo certbot --apache
```

### Step 5: Test the Website
- Open a browser and access `http://<your_IP_address>` or your domain name.

### Step 6: Automation (Optional)
- Use **cron job** to automatically update source code:
```bash
crontab -e
# Add the following line to pull the latest code daily
0 2 * * * cd /var/www/html/mywebsite && git pull
```

---

## 3. Conclusion
You have successfully deployed a website on Linux. If you encounter errors, check the log files at:
- Apache: `/var/log/apache2/error.log`
- Nginx: `/var/log/nginx/error.log`
