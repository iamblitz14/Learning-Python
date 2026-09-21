import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
import os
import subprocess
import crypto_vault

CONFIG_FILE = os.path.join(os.path.dirname(__file__), ".rdp_config.json")

class PortableSharedRDPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shared Multi-RDP Manager")
        self.root.geometry("420x420") # Height increased slightly to fit new management buttons cleanly
        self.root.resizable(False, False)
        
        # 1. Boot up validation routine
        self.master_key = ""
        self.profiles = self.get_saved_profiles()
        
        self.request_and_validate_key()
        
        if not self.master_key:
            self.root.destroy()
            return

        # 2. Dynamic Dropdown Population
        # If the JSON file is blank or new, fallback to your default list
        saved_keys = [k for k in self.profiles.keys() if k != "validation_marker"]
        self.devices = sorted(saved_keys) if saved_keys else ["A", "B", "E", "H", "I", "J", "K", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
        
        self.selected_device = tk.StringVar(value=self.devices[0])
        
        # Dropdown Profile Selector Label
        tk.Label(root, text="Select Device Profile Target:", font=("Arial", 10, "bold")).pack(pady=10)
        
        # Frame to hold Dropdown + Management Buttons inline
        self.profile_mgmt_frame = tk.Frame(root)
        self.profile_mgmt_frame.pack(pady=2)
        
        # Re-built dynamic OptionMenu
        self.dropdown_menu = None
        self.render_dropdown()
        
        self.btn_add_prof = tk.Button(self.profile_mgmt_frame, text="+ Add", bg="#E1E1E1", command=self.add_new_profile)
        self.btn_add_prof.pack(side="left", padx=5)
        
        self.btn_del_prof = tk.Button(self.profile_mgmt_frame, text="🗑 Delete", bg="#FFCDD2", fg="#B71C1C", command=self.delete_current_profile)
        self.btn_del_prof.pack(side="left", padx=5)
        
        tk.Frame(root, height=2, bd=1, relief="groove").pack(fill="x", padx=20, pady=10)
        
        # Form inputs
        tk.Label(root, text="IP Address / Hostname:").pack(anchor="w", padx=20)
        self.entry_ip = tk.Entry(root, width=48)
        self.entry_ip.pack(pady=2, padx=20)
        
        tk.Label(root, text="Username:").pack(anchor="w", padx=20)
        self.entry_user = tk.Entry(root, width=48)
        self.entry_user.pack(pady=2, padx=20)
        
        tk.Label(root, text="Password:").pack(anchor="w", padx=20)
        self.entry_pass = tk.Entry(root, width=48, show="*")
        self.entry_pass.pack(pady=2, padx=20)
        
        # Core Operation Action Triggers
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=20)
        
        self.btn_save = tk.Button(self.btn_frame, text="Save This Profile", width=14, command=self.save_data)
        self.btn_save.pack(side="left", padx=5)
        
        self.btn_connect = tk.Button(self.btn_frame, text="Connect Now", width=14, bg="#4CAF50", fg="white", command=self.connect_rdp)
        self.btn_connect.pack(side="left", padx=5)
        
        # Initial field load sequence execution
        self.load_data()

    def render_dropdown(self):
        """Destroys and recreates the dropdown list to accurately reflect updates."""
        if self.dropdown_menu:
            self.dropdown_menu.pack_forget()
        
        self.dropdown_menu = tk.OptionMenu(self.profile_mgmt_frame, self.selected_device, *self.devices, command=self.change_device)
        self.dropdown_menu.config(width=15)
        self.dropdown_menu.pack(side="left", padx=5)

    def get_saved_profiles(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    return json.load(f)
            except:
                pass
        return {}

    def request_and_validate_key(self):
        attempts = 3
        while attempts > 0:
            key_input = simpledialog.askstring(
                "Shared Deployment Passkey", 
                f"Enter Shared Cryptographic Key:\n(Attempts left: {attempts})", 
                show="*"
            )
            if not key_input:
                return

            if "validation_marker" in self.profiles:
                encrypted_marker = self.profiles["validation_marker"]
                decrypted_marker = crypto_vault.decrypt_password(encrypted_marker, key_input)
                
                if decrypted_marker == "PASSED_INTEGRITY_CHECK":
                    self.master_key = key_input
                    return
                else:
                    attempts -= 1
                    messagebox.showerror("Access Denied", "Incorrect Master Cryptographic Key.")
            else:
                self.master_key = key_input
                return

    def change_device(self, chosen_device):
        self.load_data()

    def load_data(self):
        self.entry_ip.delete(0, tk.END)
        self.entry_user.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)
        
        current = self.selected_device.get()
        device_info = self.profiles.get(current, {})
        
        if device_info:
            self.entry_ip.insert(0, device_info.get("ip", ""))
            self.entry_user.insert(0, device_info.get("user", ""))
            
            encrypted_pw = device_info.get("password", "")
            if encrypted_pw:
                decrypted_pw = crypto_vault.decrypt_password(encrypted_pw, self.master_key)
                self.entry_pass.insert(0, decrypted_pw)

    def save_data(self):
        current = self.selected_device.get()
        ip = self.entry_ip.get().strip()
        user = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()
        
        if not ip or not user or not password:
            messagebox.showwarning("Missing Info", "Please populate all fields before writing execution changes.")
            return

        scrambled_password = crypto_vault.encrypt_password(password, self.master_key)
        
        self.profiles = self.get_saved_profiles()
        self.profiles["validation_marker"] = crypto_vault.encrypt_password("PASSED_INTEGRITY_CHECK", self.master_key)
        
        self.profiles[current] = {
            "ip": ip,
            "user": user,
            "password": scrambled_password
        }
        
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.profiles, f, indent=4)
            
        messagebox.showinfo("Saved!", f"Profile details for '{current}' logged securely.")

    def add_new_profile(self):
        """Asks user for a profile custom label string and appends it to tracking structures."""
        new_name = simpledialog.askstring("Add Profile", "Enter identifier name or letter for new profile:").strip()
        if not new_name:
            return
        
        if new_name in self.devices or new_name == "validation_marker":
            messagebox.showwarning("Duplicate", "A profile with that name already exists.")
            return
            
        # Append name token, sort list structure array entries alphabetically
        self.devices.append(new_name)
        self.devices = sorted(self.devices)
        
        # Switch selection pointer to your newly manufactured target element node context
        self.selected_device.set(new_name)
        self.render_dropdown()
        self.load_data()

    def delete_current_profile(self):
        """Permanently wipes the currently selected node profile array dataset blocks completely."""
        current = self.selected_device.get()
        
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to permanently delete profile '{current}'?")
        if not confirm:
            return
            
        # Drop key entry data structure segment from persistent state dictionary memory contexts
        if current in self.profiles:
            del self.profiles[current]
            with open(CONFIG_FILE, "w") as f:
                json.dump(self.profiles, f, indent=4)
                
        # Drop element from visual active dropdown list array trackers
        self.devices.remove(current)
        
        # Safeguard array continuity metrics: guarantee at least one visual element exists inside layout references
        if not self.devices:
            self.devices = ["A"]
            
        self.selected_device.set(self.devices[0])
        self.render_dropdown()
        self.load_data()
        messagebox.showinfo("Deleted", f"Profile '{current}' has been erased successfully.")

    def connect_rdp(self):
        ip = self.entry_ip.get().strip()
        user = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()
        
        if not ip or not user or not password:
            messagebox.showwarning("Error", "Inputs cannot be empty during launch sequence.")
            return

        cmd_credentials = f"cmdkey /generic:TERMSRV/{ip} /user:{user} /pass:{password}"
        subprocess.run(cmd_credentials, shell=True, stdout=subprocess.DEVNULL)
        subprocess.Popen(f"mstsc /v:{ip}", shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PortableSharedRDPApp(root)
    root.mainloop()
