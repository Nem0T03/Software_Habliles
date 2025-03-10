### **Step 1: Install DHCP Server**
1. **Open Server Manager**:
   - Access *Server Manager* from the Start menu.
   - Click *Add Roles and Features* and select *Next*.

2. **Choose Installation Type**:
   - Select *Role-Based or Feature-Based Installation*, then click *Next*.

3. **Select the Target Server**:
   - Choose the server from the list and click *Next*.

4. **Add DHCP Server Role**:
   - Select *DHCP Server* from the list of roles.
   - Add *Management Tools* if needed, click *Next*, and confirm.

5. **Confirm Installation**:
   - Click *Install*. Once completed, close the window and proceed to configuration.

---

### **Step 2: Post-Installation Configuration**
1. **Complete DHCP Configuration**:
   - In *Server Manager*, select *DHCP*.
   - Click the yellow warning icon and select *Complete DHCP Configuration*.
   - Choose *Skip AD authorization* if the server is not part of Active Directory.

2. **Configure DHCP in Server Manager**:
   - Navigate to *Tools* > *DHCP* to open the DHCP console.

---

### **Step 3: Create a New Scope**
1. **Add a Scope**:
   - In the DHCP console, right-click *IPv4* > *New Scope*.

2. **Define Scope Name**:
   - Enter a name and description for the Scope, then click *Next*.

3. **Set IP Range**:
   - Enter the *Start IP* and *End IP*, along with the subnet mask. Click *Next*.

4. **Exclude IP Addresses (Optional)**:
   - Exclude any reserved IPs (e.g., for printers, network devices).

5. **Set Lease Duration**:
   - Define the lease duration for assigned IP addresses, then click *Next*.

---

### **Step 4: Additional Configuration**
1. **Default Gateway**:
   - Enter the gateway address, click *Add*, then *Next*.

2. **Domain Name and DNS Servers**:
   - Provide DNS information, then click *Next*.

3. **Configure WINS (if needed)**:
   - Enter WINS Server details or skip this step.

4. **Activate the Scope**:
   - Choose to activate immediately or later, then click *Next* to complete setup.

---

### **Step 5: Verification and Testing**
1. **Check Scope Status**:
   - Ensure the Scope is active and properly configured in the DHCP console.

2. **Configure DHCP Clients**:
   - Set client devices to obtain an IP address automatically from the DHCP server.

---

### **Ways to Open the DHCP Console**
- **Method 1**: Via *Windows Administrative Tools*.
- **Method 2**: Navigate to *Tools* in *Server Manager*.
- **Method 3**: Run `dhcpmgmt.msc` in the *Run* dialog.
- **Method 4**: Search for *DHCP* in the Start menu.

---

