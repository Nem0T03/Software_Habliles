# Installing Nagios XI on Linux

## **Prerequisites:**
Before starting the installation, you need to connect to your server via a terminal session. Ensure you are logged in as `root` or a user with `sudo` privileges.

---

## **Nagios XI Installation Methods**
There are multiple ways to install Nagios XI, all of which ensure a full installation.

### **1. Quick Installation**
For a fast installation, run the following command in your terminal:

```bash
curl https://assets.nagios.com/downloads/nagiosxi/install.sh | sh
```

This command will download and install Nagios XI automatically. Once the installation is complete, proceed to the **Post-Installation Steps** section.

---

### **2. Manual Download and Installation**
If you prefer a manual installation, use the following commands:

```bash
cd /tmp
wget https://assets.nagios.com/downloads/nagiosxi/xi-latest.tar.gz
tar xzf xi-latest.tar.gz
cd nagiosxi
./fullinstall
```

> **Note:** If you need a specific version of Nagios XI, visit the following page to obtain the correct download URL:
> - [Nagios XI Versions](https://assets.nagios.com/downloads/nagiosxi/versions.php)

Once the installation is complete, proceed to the **Post-Installation Steps**.

---

## **Post-Installation Steps**
Once the installation is finished, you should see a message similar to:

```
Nagios XI Installation Complete!
```

You can now access the Nagios XI web interface by navigating to:

```
http://<server_address>/nagiosxi
```

---

## **Initial Setup & Configuration**

### **1. System Configuration**
After accessing the Nagios XI interface, the setup wizard will guide you through system configuration options. 

### **2. License Activation**
You will be presented with licensing options:
- **Trial** – 30-day free trial with full features (see "Starting a Nagios XI Trial" for details).
- **Licensed** – Requires a valid license key, Client ID, and Enterprise Key.
- **Free** – Limited to **7 hosts** and **100 checks**.

Select your preferred option and click **Next** to continue.

---

### **3. Admin Account Configuration**
On the next screen, configure the **administrator account** by setting a secure password. The default password is randomly generated, but it is recommended to change it.

Once done, click **Finish Install** to save the settings.

---

### **4. Completing the Installation**
Nagios XI will finalize the configuration. After completion, you will see an **Installation Complete** message displaying the administrator username and password.

Click **Login to Nagios XI** to proceed.

---

### **5. Logging into Nagios XI**
- Enter your **Admin Username** and **Password**, then click **Login**.
- Accept the **License Agreement** when prompted.
- Upon successful login, you will be redirected to the **Nagios XI Dashboard**.

---

## **References**
- [Nagios XI Documentation](https://support.nagios.com/kb/)
- [Nagios Core Installation Guide](https://www.nagios.org/documentation/)
