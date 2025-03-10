### **Guide to Installing and Configuring a DNS Server on Windows Server 2022**

#### **I. Preparation Before Installation**

1. **System Requirements**:
   - **Hardware**:
     - Processor: 64-bit support.
     - RAM: Minimum 2GB (recommended 4GB or more).
     - Storage: At least 32GB of free space.
   - **Software**:
     - Windows Server 2022 installed and fully updated.

2. **Set a Static IP**:
   - Necessary to ensure:
     - **Stability and consistency**: Devices on the network can always access the DNS Server.
     - **Easier management**: Avoid reconfiguring when the IP changes.
     - **Enhanced security**: Reduces risks of confusion and attacks from dynamic IPs.

---

#### **II. Installing the DNS Server**

1. **Open Server Manager**:
   - Access **Server Manager** from the Start menu or taskbar.

2. **Add the DNS Server Role**:
   - Click **Add roles and features**.
   - In the **Add Roles and Features Wizard**:
     - In **Before you begin**:
       - Check **“Skip this page by default”** to bypass the introduction page in future installations.
     - In **Installation Type**:
       - Select **“Role-based or feature-based installation”**.
     - In **Server Selection**:
       - Choose **“Select a server from the server pool”** and select the current server from the list.
     - In **Server Roles**:
       - Check **“DNS Server”**.

3. **Additional Configuration**:
   - In **Features**, leave default settings and click **Next**.
   - In the **DNS Server Introduction** window, click **Next**.

4. **Confirm and Install**:
   - In the **Confirmation** step:
     - Check **“Restart the destination server automatically if required”** to allow automatic reboot if needed.
     - Click **Install** to start the installation.

---

#### **III. Verify Installation**

1. **Check in Server Manager**:
   - After successful installation, **DNS Server** will appear in the **Server Group** list.

2. **Access DNS Manager**:
   - **Option 1**: From **Server Manager** > **Tools** > select **DNS**.
   - **Option 2**: Press **Windows** > search for **DNS**.

3. **Configure the DNS Server**:
   - Use DNS Manager to create and manage zones, records, and perform necessary configurations.

---

### **IV. Configure DNS Forwarder**
A DNS Forwarder helps forward DNS queries that cannot be resolved internally to another DNS server (e.g., Google DNS, Cloudflare DNS).

1. **Open DNS Manager**:
   - Press **Windows + R**, type `dnsmgmt.msc`, and press **Enter**.

2. **Add a DNS Forwarder**:
   - In DNS Manager, right-click the DNS server name (hostname).
   - Select **Properties** > Switch to the **Forwarders** tab.
   - Click **Edit** and enter the IP addresses of external DNS servers:
     - Google DNS: `8.8.8.8`, `8.8.4.4`
     - Cloudflare DNS: `1.1.1.1`, `1.0.0.1`
   - Click **OK** to save.

3. **Verify Forwarder Configuration**:
   - Open **Command Prompt** (`cmd`).
   - Run the command:
     ```powershell
     nslookup google.com
     ```
   - If it returns Google’s IP addresses, the configuration is successful.

---

### **V. Configure Reverse Lookup Zone**  
The Reverse Lookup Zone maps an IP address to a domain name (opposite of the Forward Lookup Zone).

1. **Open DNS Manager**:
   - In **Server Manager**, go to **Tools** > **DNS**.

2. **Create a Reverse Lookup Zone**:
   - In DNS Manager, expand **Forward Lookup Zones**.
   - Right-click **Reverse Lookup Zones** > Select **New Zone**.
   - Click **Next** on the introduction screen.

3. **Select Zone Type**:
   - Choose **Primary Zone** if this is the main server.
   - Check **Store the zone in Active Directory** if the server is a Domain Controller.
   - Click **Next**.

4. **Enter the IP Range for the Reverse Zone**:
   - Choose **IPv4 Reverse Lookup Zone**.
   - Enter the network portion of the IP address (e.g., `192.168.1` for a `192.168.1.x` network).
   - Click **Next**.

5. **Select Dynamic Update Mode**:
   - If using **Active Directory**, select **Allow only secure dynamic updates**.
   - If not, select **Do not allow dynamic updates**.
   - Click **Next** and **Finish**.

6. **Create a Pointer (PTR) Record**:
   - Open **Reverse Lookup Zones** > Select the newly created zone.
   - Right-click, select **New Pointer (PTR)**.
   - Enter the server’s IP address and its corresponding domain name.
   - Click **OK** to save.

7. **Verify Reverse Lookup**:
   - Open **Command Prompt** (`cmd`).
   - Run:
     ```powershell
     nslookup 192.168.1.10
     ```
   - If it returns the correct domain name, the configuration is successful.

---

### **VI. Verify and Test DNS Server**

1. **Check if the DNS service is running**:
   ```powershell
   Get-Service -Name DNS
   ```

2. **Test DNS Forwarding**:
   ```powershell
   nslookup google.com
   ```

3. **Test Reverse Lookup**:
   ```powershell
   nslookup 192.168.1.10
   ```

---

### **VII. Conclusion**  
- Configuring a **DNS Forwarder** optimizes external DNS query resolution.  
- Setting up a **Reverse Lookup Zone** helps manage IP-to-Domain mapping efficiently.  
- Testing and verification ensure the DNS Server is functioning properly.  

Let me know if you need additional details! 🚀
