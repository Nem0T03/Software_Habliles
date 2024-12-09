---

### 1. Cấu trúc thư mục:
```plaintext
network-automation-ansible/
├── ansible.cfg
├── inventory/
│   └── hosts
├── playbooks/
│   ├── etherchannel.yml
│   ├── vtp.yml
│   ├── vlan.yml
│   ├── svi_hsrp.yml
│   ├── dhcp.yml
│   ├── firewall.yml
│   ├── router_l3.yml
│   └── dhcp_snooping.yml
├── roles/
└── README.md
```

---

### 2. Cài đặt Ansible

#### **Bước 1: Cài đặt Ansible trên máy điều khiển**
1. **Cài đặt Ansible trên Linux**:
   ```bash
   sudo apt update
   sudo apt install -y ansible
   ```

2. **Kiểm tra phiên bản**:
   ```bash
   ansible --version
   ```

#### **Bước 2: Cài đặt các gói cần thiết**
Cài đặt các thư viện hỗ trợ thiết bị mạng:
   ```bash
   pip install paramiko netmiko ansible[network]
   ```

#### **Bước 3: Tạo môi trường làm việc**
Tạo thư mục để chứa file cấu hình và playbook:
   ```bash
   mkdir -p ansible/networking
   cd ansible/networking
   ```

---

### 3. Cấu hình file `ansible.cfg`
```ini
[defaults]
inventory = inventory/hosts
host_key_checking = False
log_path = ansible.log
```

---

### 4. Cấu hình các thiết bị

#### **Bước 1: Tạo file `hosts` để liệt kê các thiết bị mạng**
Tạo file `inventory/hosts` với các thiết bị như sau:

```ini
[routers]
R5 ansible_host=192.168.1.5 ansible_user=admin ansible_password=admin ansible_network_os=ios
R6 ansible_host=192.168.1.6 ansible_user=admin ansible_password=admin ansible_network_os=ios

[switches]
R1 ansible_host=192.168.1.1 ansible_user=admin ansible_password=admin ansible_network_os=ios
R2 ansible_host=192.168.1.2 ansible_user=admin ansible_password=admin ansible_network_os=ios
R7 ansible_host=192.168.1.7 ansible_user=admin ansible_password=admin ansible_network_os=ios
R8 ansible_host=192.168.1.8 ansible_user=admin ansible_password=admin ansible_network_os=ios

[firewalls]
FW1 ansible_host=192.168.1.10 ansible_user=admin ansible_password=admin ansible_network_os=fortios
FW2 ansible_host=192.168.1.11 ansible_user=admin ansible_password=admin ansible_network_os=fortios
```

---

### 5. Tạo các Playbook Ansible

#### **5.1. Playbook cấu hình EtherChannel**
Tạo file `playbooks/etherchannel.yml`:

```yaml
---
- name: Configure EtherChannel
  hosts: routers
  tasks:
    - name: Configure EtherChannel on interfaces
      ios_config:
        lines:
          - switchport trunk encapsulation dot1q
          - switchport mode trunk
          - channel-group 1 mode on
        parents: interface range Ethernet1/0-1

    - name: Assign IP to Port-Channel
      ios_config:
        lines:
          - ip address 192.168.10.1 255.255.255.0
          - no shutdown
        parents: interface Port-channel1
```

---

#### **5.2. Playbook cấu hình VTP**
Tạo file `playbooks/vtp.yml`:

```yaml
---
- name: Configure VTP
  hosts: switches
  tasks:
    - name: Configure VTP domain and mode
      ios_config:
        lines:
          - vtp domain abc.com
          - vtp mode server
          - vtp password 123

    - name: Create VLANs
      ios_config:
        lines:
          - vlan 10
          - vlan 20
        when: inventory_hostname == 'R1'
```

---

#### **5.3. Playbook cấu hình SVI VLAN và HSRP**
Tạo file `playbooks/svi_hsrp.yml`:

```yaml
---
- name: Configure SVI and HSRP
  hosts: routers
  tasks:
    - name: Enable IP routing
      ios_config:
        lines:
          - ip routing

    - name: Configure VLAN 10
      ios_config:
        lines:
          - ip address 172.16.10.1 255.255.255.0
          - no shutdown
          - standby 1 ip 172.16.10.3
          - standby 1 priority 20
          - standby 1 preempt
        parents: interface Vlan10
        when: inventory_hostname == 'R5'

    - name: Configure VLAN 30
      ios_config:
        lines:
          - ip address 172.16.30.2 255.255.255.0
          - no shutdown
          - standby 3 ip 172.16.30.3
          - standby 3 priority 20
          - standby 3 preempt
        parents: interface Vlan30
        when: inventory_hostname == 'R6'
```

---

#### **5.4. Playbook cấu hình DHCP**
Tạo file `playbooks/dhcp.yml`:

```yaml
---
- name: Configure DHCP
  hosts: routers
  tasks:
    - name: Configure DHCP pools
      ios_config:
        lines:
          - network 172.16.10.0 255.255.255.0
          - default-router 172.16.10.3
          - dns-server 8.8.8.8
        parents: ip dhcp pool Vlan1
        when: inventory_hostname == 'R5'
```

---

#### **5.5. Playbook cấu hình Firewall**
Tạo file `playbooks/firewall.yml`:

```yaml
---
- name: Configure Firewall Interfaces
  hosts: firewalls
  tasks:
    - name: Configure port3
      fortios_config:
        vdom: "root"
        config: "system interface"
        state: "present"
        settings:
          name: "port3"
          mode: "static"
          ip: "{{ '192.168.109.10' if inventory_hostname == 'FW1' else '192.168.109.11' }}"
          allowaccess: "http https ping telnet ssh"
```

---

### 6. Triển khai Playbook

#### **Bước 1: Kiểm tra kết nối với các thiết bị**
```bash
ansible -i inventory/hosts all -m ping
```

#### **Bước 2: Chạy các Playbook lần lượt**
Chạy các playbook theo thứ tự:
```bash
ansible-playbook -i inventory/hosts playbooks/etherchannel.yml
ansible-playbook -i inventory/hosts playbooks/vtp.yml
ansible-playbook -i inventory/hosts playbooks/svi_hsrp.yml
ansible-playbook -i inventory/hosts playbooks/dhcp.yml
ansible-playbook -i inventory/hosts playbooks/firewall.yml
```

---
