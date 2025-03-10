
### **Steps to Create a Microsoft 365 Developer Account:**  
1. **Visit the Microsoft 365 Developer Program** website.  
2. Click **“Join Now”** to begin.  
3. Sign in with an existing Microsoft account or create a new one.  
4. Enter a company name (any name is acceptable).  
5. Select the default options and click **Next**.  
6. **Select “Set up E5 subscription”**.  
7. Enter the required information and click **Continue**.  
8. Enter your phone number and click **“Send Code”**.  
9. Enter the verification code and complete the setup process.  
10. The E5 account will be active for 3 months and can be automatically renewed if used regularly.  

---

### **Manage and Configure the Account:**  
1. Go to **admin.microsoft.com** and sign in with your admin account.  
2. Add new users under **User management**.  
3. To increase OneDrive storage to 5TB:  
   - Navigate to **OneDrive > Storage used > Edit**.  
   - If the **Edit** button is not available, log in to **portal.office.com/onedrive** to activate OneDrive.  

---

### **Add a Custom Domain:**  
1. Visit **https://aka.ms/SPORenameAddDomain** and sign in with your admin account.  
2. Add your custom domain and follow the DNS configuration steps.  
3. Rename the domain using **SharePoint Online Management Shell**:  
   - Connect to **SPOService**.  
   - Use the command:  
     ```powershell
     Start-SPOTenantRename -DomainName "<DomainName>" -ScheduledDateTime "<YYYY-MM-DDTHH:MM:SS>"
     ```  

---

### **Add a Custom Domain via Admin Center:**  
1. Go to **admin.microsoft.com** and select **“Go to guided setup”**.  
2. Under **“Install Office”**, click **“Continue”**.  
3. Enter the domain name and verify it via **Cloudflare** or another DNS provider.  
4. Add the required DNS records to complete the verification process.  

