# 🚀 Guide to Setting Up a Domain on Windows Server 2022

## 📌 Prerequisites
Before setting up a domain, ensure you have the following:
- 🖥️ A Windows Server 2022 machine
- 🔑 Administrator privileges
- 🌐 A static IP address configured on the server

---

## 1️⃣ Install Active Directory Domain Services (AD DS)

1. Open **Server Manager** ➜ Click **Manage** ➜ Select **Add Roles and Features**.
2. Choose **Role-based or feature-based installation** ➜ Click **Next**.
3. Select your server ➜ Click **Next**.
4. In **Server Roles**, check **Active Directory Domain Services** ➜ Click **Next**.
5. Click **Add Features** when prompted ➜ Click **Next**.
6. Proceed with the installation and click **Install**.
7. After installation, click **Close**.

---

## 2️⃣ Promote Server to a Domain Controller

1. In **Server Manager**, click the **flag notification** 🔔 and select **Promote this server to a domain controller**.
2. Select **Add a new forest** and enter your domain name (e.g., `example.local`).
3. Click **Next** and configure:
   - Choose **Domain Functional Level** (default is fine).
   - Set a **DSRM password** (Directory Services Restore Mode).
4. Click **Next** until the **Prerequisites Check** completes.
5. Click **Install**.
6. The server will **restart automatically**.

---

## 3️⃣ Verify Domain Configuration

1. Log in using `Administrator@yourdomain.local`.
2. Open **Command Prompt** (`cmd`) and run:
   ```powershell
   ipconfig /all
   ```
   Ensure the **Primary DNS** is set to the server’s static IP.
3. Open **Active Directory Users and Computers** (`dsa.msc`) to verify the domain setup.

---

## 4️⃣ Configure DNS Settings (Optional but Recommended)

1. Open **DNS Manager** (`dnsmgmt.msc`).
2. Expand your server ➜ Right-click on **Forward Lookup Zones** ➜ Select **New Zone**.
3. Choose **Primary Zone** ➜ Click **Next**.
4. Enter your domain name ➜ Click **Next**.
5. Accept default settings and complete the wizard.
6. Ensure that the **Reverse Lookup Zone** is also configured.

---

## 5️⃣ Add a Client Computer to the Domain

1. On a client machine, open **System Properties** (`sysdm.cpl`).
2. Click **Change settings** under **Computer Name**.
3. Click **Change** ➜ Select **Domain** ➜ Enter your domain name.
4. Enter administrator credentials when prompted.
5. Restart the client machine.

---

## 🎯 Conclusion
You have successfully set up a domain on **Windows Server 2022**! 🎉 Now you can:
- 🏢 Manage users and computers through **Active Directory**.
- 🌍 Use **Group Policy** to enforce security settings.
- 🔍 Monitor domain activity with **Event Viewer**.

For more details, check [Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/) 📚.

