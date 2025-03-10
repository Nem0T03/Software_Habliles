# **Guide to Configuring Domain Controller (2022) and Clients (PC01 & PC02)**

---

## 🖥️ **1. Configuring Domain Controller (PC01)**

### 🔹 **Step 1: Configure Network Settings**
1. Right-click the **network icon** > select **Open Network and Sharing Center** > **Change Adapter Settings**.
2. Right-click the **External** network adapter > select **Properties**.
   - Uncheck **Internet Protocol Version 6 (TCP/IPv6)**.
   - Select **Internet Protocol Version 4 (TCP/IPv4)** > click **Properties**.
3. In the **Preferred DNS server** field, enter **192.168.1.1** (IP of PC01) > Click **OK** twice to save.

### 🔹 **Step 2: Install Active Directory Domain Services (AD DS)**
4. Open **Server Manager** > Click **Manage** > Select **Add Roles and Features**.
5. In the **Before You Begin** window, click **Next**.
6. Choose **Role-based or Feature-based Installation** > Click **Next**.
7. In **Select Features**, click **Next** twice.
8. In **Confirm Installation Selections**, click **Install**.

### 🔹 **Step 3: Promote to Domain Controller**
9. Once installation is complete, click **Promote this server to a domain controller** in the **Installation Progress** window.
10. In **Deployment Configuration**, select **Add a new forest**.
    - Enter the domain name (e.g., `DOM01.LOCAL`) in **Root domain name** > Click **Next**.
    - In **Domain Controller Options**, set the password to **P@ssword** > Click **Next** four times.
11. In **Prerequisites Check**, click **Install**.
12. Once completed, the system will **automatically restart**.
    - Log in with **DOM01\Administrator**.

---

## 🖥️ **2. Adding Workstation to Domain (PC02)**

### 🔹 **Step 1: Change System Settings**
1. Right-click **This PC** on the Desktop > Select **Properties**.
2. In the **System** window, select **Change settings**.
3. In **System Properties**, click **Change**.

### 🔹 **Step 2: Join the Domain**
4. Select **Domain**, enter **DOM01.LOCAL**, and click **OK**.
5. The **Windows Security** prompt will appear:
   - Enter **DOM01\Administrator** in **Username**.
   - Enter **P@ssword** in **Password** > Click **OK** three times.
   - Click **Close**, then **Restart Now**.
6. After restarting, log in using **DOM01\Administrator**.

---

## 🔧 **3. Configuring Group Policy on Domain Controller (PC01)**

### 🛡️ **a. Allow Simple Passwords**
1. Open **Server Manager** > Go to **Tools** > Select **Group Policy Management**.
2. Navigate to: **Forest: DOM01.LOCAL > Domains > DOM01.LOCAL**.
3. Right-click **Default Domain Policy** > Click **Edit**.
4. Navigate to:
   - **Computer Configuration > Windows Settings > Security Settings > Account Policy > Password Policy**.
5. Modify these values:
   - **Enforce password history:** `0`
   - **Maximum password age:** `0`
   - **Minimum password length:** `0`
   - **Password must meet complexity requirements:** `Disabled`
6. Open **Command Prompt** and run: `Gpupdate /Force`.

### 👥 **b. Allow Group Users to Log On to DC**
1. Navigate to: **Forest: DOM01.LOCAL > Domains > DOM01.LOCAL > Domain Controllers**.
2. Right-click **Default Domain Controllers Policy** > Click **Edit**.
3. Go to:
   - **Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User Rights Assignment**.
4. Double-click **Allow log on locally** > Click **Add User or Group**.
   - Enter **Users** > Click **Check Names** > Click **OK** twice.
5. Run `Gpupdate /Force` in Command Prompt.

### 🆕 **c. Create Domain Users and Verify**
1. Open **Server Manager** > Go to **Tools** > Select **Active Directory Users and Computers**.
2. Right-click **Users** > Select **New > User**.
3. Enter user details (e.g., `u1`) > Set the password as `123` > Check **Password never expires**.
   - Click **Next** > **Finish**.
4. Create another user (`u2`) using the same steps.
5. Log out from `Administrator` and log in using `u1` and `u2` on PC01.

---

## 📦 **4. Installing Remote Server Administration Tools (RSAT) on PC02**

1. Log in as **DOM01\Administrator**.
   - Copy the **WindowsTH-RSAT_WS_1803-x64** file to drive C and run it.
2. Click **Yes** > Select **I accept**.
3. After installation, click **Close**.
4. Verify installation at **Start > Windows Administrative Tools > Active Directory Users and Computers**.

---

## 🚀 **5. Running Active Directory as Administrator (PC02)**

1. Log in as **DOM01\u1**.
2. Right-click **Active Directory Users and Computers** > Select **Run as administrator**.
3. Enter **DOM01\Administrator** credentials.
4. Try creating a new user (e.g., `u4`).

---

✅ **Congratulations! You have successfully set up a Domain Controller and configured clients to join the domain.** 🎉
