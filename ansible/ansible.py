import os
import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import psutil  # To get network interfaces

class AnsibleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ansible Playbook Executor")
        self.root.geometry("500x600")
        self.root.config(bg="#f4f4f9")

        self.ansible_path = ""  # Path to playbook files
        self.hosts_file = ""    # Hosts file path
        self.playbook_file = ""  # Playbook file path
        self.network_card = ""  # Selected network card
        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#ffffff", bd=10, relief="solid", padx=20, pady=20)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = tk.Label(main_frame, text="Chạy Playbook Ansible", font=("Arial", 18, "bold"), bg="#ffffff")
        self.title_label.pack(pady=10)

        # Hosts file selection
        self.hosts_label = tk.Label(main_frame, text="Chọn tệp hosts:", font=("Arial", 12), bg="#ffffff")
        self.hosts_label.pack(pady=5)
        self.hosts_button = tk.Button(main_frame, text="Chọn tệp hosts", command=self.select_hosts,
                                      bg="#4CAF50", fg="white", font=("Arial", 12), relief="flat", bd=0)
        self.hosts_button.pack(pady=5, fill=tk.X)

        # Playbook file selection
        self.playbook_label = tk.Label(main_frame, text="Chọn tệp playbook:", font=("Arial", 12), bg="#ffffff")
        self.playbook_label.pack(pady=5)
        self.playbook_button = tk.Button(main_frame, text="Chọn tệp playbook", command=self.select_playbook,
                                         bg="#4CAF50", fg="white", font=("Arial", 12), relief="flat", bd=0)
        self.playbook_button.pack(pady=5, fill=tk.X)

        # Playbook selection dropdown
        self.playbook_var = tk.StringVar()
        self.playbook_dropdown = tk.OptionMenu(main_frame, self.playbook_var,
                                                "etherchannel.yml", "vtp.yml", 
                                                "svi_hsrp.yml", "dhcp.yml", 
                                                "firewall.yml")
        self.playbook_dropdown.config(bg="#ffffff", font=("Arial", 12), relief="flat")
        self.playbook_dropdown.pack(pady=10, fill=tk.X)

        # Configuration type dropdown
        self.config_var = tk.StringVar()
        self.config_dropdown = tk.OptionMenu(main_frame, self.config_var, 
                                              "Cấu hình 1", "Cấu hình 2", "Cấu hình 3")
        self.config_dropdown.config(bg="#ffffff", font=("Arial", 12), relief="flat")
        self.config_dropdown.pack(pady=10, fill=tk.X)

        # Network card dropdown
        self.network_var = tk.StringVar()
        self.network_dropdown = tk.OptionMenu(main_frame, self.network_var, *self.get_network_cards())
        self.network_dropdown.config(bg="#ffffff", font=("Arial", 12), relief="flat")
        self.network_dropdown.pack(pady=10, fill=tk.X)

        # Run Button
        self.run_button = tk.Button(main_frame, text="Chạy Playbook", command=self.run_playbook, 
                                    bg="#4CAF50", fg="white", font=("Arial", 12), relief="flat", bd=0)
        self.run_button.pack(pady=20, fill=tk.X)

        # Status label
        self.status_label = tk.Label(main_frame, text="Trạng thái: Chưa chạy", font=("Arial", 12), fg="blue", bg="#ffffff")
        self.status_label.pack(pady=10)

    def get_network_cards(self):
        """Get a list of network interfaces available on the system."""
        network_cards = []
        for interface, addrs in psutil.net_if_addrs().items():
            network_cards.append(interface)
        return network_cards

    def select_hosts(self):
        """Select hosts file"""
        file_path = filedialog.askopenfilename(filetypes=[("INI Files", "*.ini"), ("All Files", "*.*")])
        if file_path:
            self.hosts_file = file_path
            self.hosts_label.config(text=f"Đường dẫn tệp hosts: {self.hosts_file}")

    def select_playbook(self):
        """Select playbook file"""
        file_path = filedialog.askopenfilename(filetypes=[("YAML Files", "*.yml"), ("All Files", "*.*")])
        if file_path:
            self.playbook_file = file_path
            self.playbook_label.config(text=f"Đường dẫn tệp playbook: {self.playbook_file}")

    def run_playbook(self):
        if not self.hosts_file:
            messagebox.showerror("Lỗi", "Vui lòng chọn tệp hosts")
            return
        if not self.playbook_file:
            messagebox.showerror("Lỗi", "Vui lòng chọn tệp playbook")
            return

        # Choose configuration from dropdown
        config_type = self.config_var.get()
        if not config_type:
            messagebox.showerror("Lỗi", "Vui lòng chọn kiểu cấu hình")
            return

        # Choose network card from dropdown
        network_card = self.network_var.get()
        if not network_card:
            messagebox.showerror("Lỗi", "Vui lòng chọn card mạng")
            return

        self.status_label.config(text="Trạng thái: Đang chạy...", fg="orange")

        # Command to run playbook
        command = f"ansible-playbook -i {self.hosts_file} {self.playbook_file} --extra-vars \"config_type={config_type} network_card={network_card}\""
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.status_label.config(text="Trạng thái: Hoàn thành", fg="green")
            messagebox.showinfo("Thành công", f"Playbook {self.playbook_file} đã được chạy thành công!")
        except subprocess.CalledProcessError as e:
            self.status_label.config(text="Trạng thái: Lỗi", fg="red")
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chạy playbook:\n{e.stderr.decode()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnsibleGUI(root)
    root.mainloop()
