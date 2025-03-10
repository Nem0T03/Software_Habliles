
### **Guide to Setting Up NIC Teaming on Windows Server**  

#### **Setting Up NIC Teaming via GUI (Graphical User Interface):**  

1. **Open Server Manager:**  
   - Access **Server Manager** from the Start menu or taskbar.  
   - Select **Local Server**.  

2. **Enable NIC Teaming:**  
   - Locate the **Properties** section in Server Manager.  
   - Click **NIC Teaming** > Status **Disabled** > click to open the configuration window.  

3. **Select Network Adapters:**  
   - In the NIC Teaming window, look at the **Adapters and Interfaces** section in the bottom right.  
   - Select the network adapters you want to add to the NIC Team.  

4. **Create a Team:**  
   - Click **TASKS** > select **Add to New Team**.  

5. **Configure the Team:**  
   - A new dialog box will appear, listing the available network adapters and members.  
   - **Enter a name** for the NIC Team.  

6. **Additional Configuration:**  
   - Select **Additional Properties** at the bottom:  
     - **Switch Independent**: Works independently of the switch.  
     - **Static**: Requires static configuration on the switch.  
     - **LACP (Link Aggregation Control Protocol)**: Supports dynamic configuration with a compatible switch.  
   - **Load Balancing Mode**: Select **Dynamic** for optimal performance.  

7. **Complete the Setup:**  
   - Click **OK** to finalize. The new NIC Team will be created.  

---

#### **Setting Up NIC Teaming via PowerShell:**  

1. **Open PowerShell:**  
   - Type **PowerShell** in the search bar and press Enter.  

2. **Check Available Network Adapters:**  
   - Run the command:  
     ```powershell
     Get-NetAdapter
     ```  
   - This will display a list of all available network adapters.  

3. **Create a NIC Team:**  
   - Use the following command:  
     ```powershell
     New-NetLbfoTeam "Team1" "NIC1", "NIC2"
     ```  
     - **"Team1"**: The name of the NIC Team.  
     - **"NIC1", "NIC2"**: The names of the selected network adapters (you can add more if needed).  

4. **Verify the Configuration:**  
   - Run the command:  
     ```powershell
     Get-NetLbfoTeam
     ```  
   - This will display details about the created NIC Team.  

5. **Check Team Status:**  
   - Use the following command to check the status of the team and its members:  
     ```powershell
     Get-NetLbfoTeam -Name Team1
     Get-NetAdapter -Name Team1
     ```  
   - The team's status will show **Up/Active** or **Up/Standby**.  

---

### **Notes:**  
- **Switch Independent** mode is recommended if your switch does not support LACP.  
- **Dynamic** load balancing is recommended for optimal performance.  
- Ensure all network adapters are properly connected and functioning before configuring NIC Teaming.  

Let me know if you need further refinements! 🚀
