```markdown
# Nagios Cross-Platform Agent (NCPA) Installation Guide

## Installing NCPA on Debian/Ubuntu-based Systems

### For Debian 11.x amd64:
1. Download the latest NCPA package:
   ```bash
   wget https://assets.nagios.com/downloads/ncpa/ncpa-latest.d11.amd64.deb
   ```
2. Install the package:
   ```bash
   dpkg -i ./ncpa-latest.d11.amd64.deb
   ```

### For Ubuntu i386:
1. Download the latest NCPA package:
   ```bash
   wget https://assets.nagios.com/downloads/ncpa/ncpa-latest.i386.deb
   ```
2. Install the package:
   ```bash
   sudo dpkg -i ./ncpa-latest.i386.deb
   ```

### For Ubuntu amd64:
1. Download the latest NCPA package:
   ```bash
   wget https://assets.nagios.com/downloads/ncpa/ncpa-latest.amd64.deb
   ```
2. Install the package:
   ```bash
   sudo dpkg -i ./ncpa-latest.amd64.deb
   ```

### For Ubuntu 22 amd64:
1. Download the NCPA package for Ubuntu 22:
   ```bash
   wget https://assets.nagios.com/downloads/ncpa/ncpa-latest.u22.amd64.deb
   ```
2. Install the package:
   ```bash
   sudo dpkg -i ./ncpa-latest.u22.amd64.deb
   ```

After installation, proceed to the "Configuring NCPA" section.

## Installing NCPA on MacOS

1. Download the NCPA DMG package:
   ```bash
   curl -L -o ncpa-2.2.1.dmg https://assets.nagios.com/downloads/ncpa/ncpa-2.2.1.dmg
   ```
2. Attach the DMG:
   ```bash
   sudo hdiutil attach ncpa-2.2.1.dmg
   ```
3. Install NCPA:
   ```bash
   cd /Volumes/NCPA-2.2.1
   sudo sh ./install.sh
   ```
4. Detach the DMG after installation:
   ```bash
   cd /
   sudo hdiutil detach /Volumes/NCPA-2.2.1
   ```

If the NCPA listener service does not start after installation, disable the security feature with the following command:
```bash
sudo spctl --master-disable
spctl --status
```

Then, restart the NCPA listener service:
```bash
sudo /usr/local/ncpa/ncpa_listener
```

Verify that NCPA is running:
```bash
sudo launchctl list | grep -Ei 'ncpa'
```

Proceed to the "Configuring NCPA" section.

## Configuring NCPA

1. The NCPA configuration file is located at `/usr/local/ncpa/etc/ncpa.cfg`.
2. Edit the configuration file using `vi`:
   ```bash
   sudo vi /usr/local/ncpa/etc/ncpa.cfg
   ```
3. In `vi`, press `i` to enter insert mode. Modify the line:
   ```bash
   community_string = mytoken
   ```
   Change it to your required token:
   ```bash
   community_string = Str0ngT0k3n
   ```

4. Save and exit `vi` by typing `:wq` and pressing Enter.

5. Restart the `ncpa_listener` service based on your OS:

### For RHEL/CentOS/Oracle Linux 6.x:
```bash
service ncpa_listener restart
```

### For RHEL/CentOS/Oracle Linux 7.x+:
```bash
systemctl restart ncpa_listener.service
```

### For Ubuntu 12.x/13.x/14.x:
```bash
sudo service ncpa_listener restart
```

### For Ubuntu 15.x+:
```bash
sudo systemctl restart ncpa_listener.service
```

### For Debian 7.x:
```bash
service ncpa_listener restart
```

### For Debian 8.x+:
```bash
systemctl restart ncpa_listener.service
```

### For openSUSE/SUSE SLES:
```bash
sudo systemctl restart ncpa_listener.service
```

### For AIX:
```bash
stopsrc -s ncpa_listener
startsrc -s ncpa_listener
```

### For MacOS:
```bash
sudo launchctl stop com.nagios.ncpa.listener
sudo launchctl start com.nagios.ncpa.listener
```

Proceed to the "Configure Firewall" section.

## Configuring the Firewall

### For Linux (RHEL/CentOS/Oracle Linux):

#### RHEL/CentOS/Oracle Linux 5.x/6.x:
```bash
iptables -I INPUT -p tcp --destination-port 5693 -j ACCEPT
service iptables save
ip6tables -I INPUT -p tcp --destination-port 5693 -j ACCEPT
service ip6tables save
```

#### RHEL/CentOS/Oracle Linux 7.x+:
```bash
firewall-cmd --zone=public --add-port=5693/tcp
firewall-cmd --zone=public --add-port=5693/tcp --permanent
```

### For Ubuntu:
```bash
sudo mkdir -p /etc/ufw/applications.d
sudo sh -c "echo '[NCPA]' > /etc/ufw/applications.d/ncpa"
sudo sh -c "echo 'title=Nagios Cross Platorm Agent' >> /etc/ufw/applications.d/ncpa"
sudo sh -c "echo 'description=Nagios Monitoring Agent' >> /etc/ufw/applications.d/ncpa"
sudo sh -c "echo 'ports=5693/tcp' >> /etc/ufw/applications.d/ncpa"
sudo ufw allow NCPA
sudo ufw reload
```

### For Debian:
```bash
iptables -I INPUT -p tcp --destination-port 5693 -j ACCEPT
apt-get install -y iptables-persistent
```

### For SUSE SLES:
#### SUSE SLES 11.x:
```bash
sudo sed -i '/FW_SERVICES_EXT_TCP=/s/\"$/\ 5693\"/' /etc/sysconfig/SuSEfirewall2
sudo /sbin/service SuSEfirewall2_init restart
sudo /sbin/service SuSEfirewall2_setup restart
```

#### SUSE SLES 12.x+:
```bash
sudo /usr/sbin/SuSEfirewall2 open EXT TCP 5693
sudo systemctl restart SuSEfirewall2.service
```

### For MacOS:
The firewall is not enabled by default and allows port 5693.

Proceed to the "Test NCPA" section.

## Testing NCPA

To verify the installation, access the NCPA web interface:

1. Open a web browser and connect to:
   ```
   https://<NCPA IP Address>:5693/
   ```

2. You'll be presented with a security warning. Click **Advanced**, then **Add Exception** or **Proceed** to continue.

3. Log in using the configured token.

That's it! NCPA is now installed, configured, and ready for use.
```

This format uses markdown syntax, appropriate for GitHub README files or documentation, making it easy to follow the installation and configuration steps for different systems.
