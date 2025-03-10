# Guide to Installing SSL for the Website `nkbinh.shop` on Apache

## 1. Install Let's Encrypt and Certbot
First, install Certbot and the SSL module for Apache:
```bash
sudo apt update
sudo apt install certbot python3-certbot-apache
```

## 2. Configure Apache for HTTP and HTTPS

### Step 1: Update the `000-default.conf` File for HTTP
Modify the default configuration file to support Let's Encrypt:
```bash
sudo nano /etc/apache2/sites-enabled/000-default.conf
```

Add the following content:
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

Check the configuration and restart Apache:
```bash
sudo apache2ctl configtest
sudo systemctl restart apache2
```

### Step 2: Create a Verification File for Let's Encrypt (Optional)
Check access to the `.well-known` directory:
```bash
echo "test" | sudo tee /var/www/html/.well-known/acme-challenge/test
```
Open a browser and access `http://nkbinh.shop/.well-known/acme-challenge/test` to verify.

---

## 3. Obtain SSL from Let's Encrypt
Run the following command to automatically obtain SSL and update the Apache configuration:
```bash
sudo certbot --apache -d nkbinh.shop
```

Certbot will automatically:
1. Verify domain ownership.
2. Update the Apache configuration file for HTTPS.
3. Restart Apache automatically.

---

## 4. Verify the HTTPS Configuration File
After installing SSL, Certbot will create an HTTPS configuration file (e.g., `/etc/apache2/sites-available/nkbinh.shop.conf`). Example file content:
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

Check the configuration and restart Apache:
```bash
sudo apache2ctl configtest
sudo systemctl restart apache2
```

---

## 5. Renew SSL Certificates
Let's Encrypt SSL certificates are valid for 90 days. To enable automatic renewal, add a cron job:
```bash
sudo crontab -e
```

Add the following line to check and renew the certificate daily:
```cron
0 3 * * * certbot renew --quiet
```

---

## 6. Verify SSL Functionality
- Access `https://nkbinh.shop` to check.
- Use the [SSL Labs](https://www.ssllabs.com/ssltest/) tool to evaluate the SSL configuration.

