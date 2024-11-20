import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox, Style
import threading
import subprocess
import os
import sys
import serial.tools.list_ports



class OTAUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ESP32 OTA & Serial Uploader")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # カラーテーマの設定
        self.primary_color = "#2c3e50"
        self.secondary_color = "#34495e"
        self.accent_color = "#1abc9c"
        self.text_color = "#ecf0f1"
        self.entry_bg = "#ffffff"
        self.entry_fg = "#000000"

        self.root.configure(bg=self.primary_color)

        # スタイルの設定
        style = Style()
        style.theme_use("clam")
        style.configure("TLabel", background=self.primary_color, foreground=self.text_color)
        style.configure("TButton", background=self.accent_color, foreground=self.text_color)
        style.configure("TEntry", fieldbackground=self.entry_bg, foreground=self.entry_fg)
        style.configure("TCombobox", fieldbackground=self.entry_bg, foreground=self.entry_fg)

        # フレームの作成
        self.frame = tk.Frame(root, bg=self.primary_color)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # OTA Section
        tk.Label(self.frame, text="OTA Update", font=("Arial", 12, "bold"), bg=self.primary_color, fg=self.accent_color).grid(row=0, column=0, sticky="w", pady=5)

        # File selection for OTA
        self.file_button = tk.Button(self.frame, text="Browse", command=self.browse_file, bg=self.accent_color, fg=self.text_color)
        self.file_button.grid(row=1, column=0, sticky="w", padx=5)
        self.file_label = tk.Label(self.frame, text="No firmware.bin selected", bg=self.primary_color, fg=self.text_color, anchor="w")
        self.file_label.grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

        # IP address input
        self.ip_label = tk.Label(self.frame, text="Enter ESP32 IP address:", bg=self.primary_color, fg=self.text_color)
        self.ip_label.grid(row=2, column=0, sticky="w", pady=2)
        self.ip_entry = tk.Entry(self.frame, width=30, bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.entry_fg)
        self.ip_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=5)

        # OTA Update button
        self.update_button = tk.Button(self.frame, text="OTA Update", command=self.start_ota_upload, bg=self.accent_color, fg=self.text_color)
        self.update_button.grid(row=3, column=0, columnspan=3, sticky="w", pady=10)

        # Serial Section
        tk.Label(self.frame, text="Serial Update", font=("Arial", 12, "bold"), bg=self.primary_color, fg=self.accent_color).grid(row=4, column=0, sticky="w", pady=5)

        # Serial file selection
        self.bootloader_button = tk.Button(self.frame, text="Browse", command=self.browse_bootloader, bg=self.accent_color, fg=self.text_color)
        self.bootloader_button.grid(row=5, column=0, sticky="w", padx=5)
        self.bootloader_label = tk.Label(self.frame, text="No bootloader.bin selected", bg=self.primary_color, fg=self.text_color, anchor="w")
        self.bootloader_label.grid(row=5, column=1, columnspan=2, sticky="w", padx=5)

        self.partitions_button = tk.Button(self.frame, text="Browse", command=self.browse_partitions, bg=self.accent_color, fg=self.text_color)
        self.partitions_button.grid(row=6, column=0, sticky="w", padx=5)
        self.partitions_label = tk.Label(self.frame, text="No partitions.bin selected", bg=self.primary_color, fg=self.text_color, anchor="w")
        self.partitions_label.grid(row=6, column=1, columnspan=2, sticky="w", padx=5)

        self.firmware_button = tk.Button(self.frame, text="Browse", command=self.browse_firmware, bg=self.accent_color, fg=self.text_color)
        self.firmware_button.grid(row=7, column=0, sticky="w", padx=5)
        self.firmware_label = tk.Label(self.frame, text="No firmware.bin selected", bg=self.primary_color, fg=self.text_color, anchor="w")
        self.firmware_label.grid(row=7, column=1, columnspan=2, sticky="w", padx=5)

        # Serial port selection
        self.serial_label = tk.Label(self.frame, text="Select COM Port:", bg=self.primary_color, fg=self.text_color)
        self.serial_label.grid(row=8, column=0, sticky="w", pady=2)
        self.serial_combobox = Combobox(self.frame, values=self.get_serial_ports(), state="readonly", width=15)
        self.serial_combobox.grid(row=8, column=1, sticky="w", padx=5)

        self.refresh_ports_button = tk.Button(self.frame, text="Refresh", command=self.refresh_ports, bg=self.accent_color, fg=self.text_color)
        self.refresh_ports_button.grid(row=8, column=2, sticky="w", padx=10)

        # Baud rate selection
        self.baud_label = tk.Label(self.frame, text="Select Baud Rate:", bg=self.primary_color, fg=self.text_color)
        self.baud_label.grid(row=9, column=0, sticky="w", pady=2)
        self.baud_combobox = Combobox(self.frame, values=[9600, 115200], state="readonly", width=15)
        self.baud_combobox.grid(row=9, column=1, sticky="w", padx=5)
        self.baud_combobox.set(115200)

        # Serial Update button
        self.serial_update_button = tk.Button(self.frame, text="Serial Update", command=self.start_serial_upload, bg=self.accent_color, fg=self.text_color)
        self.serial_update_button.grid(row=10, column=0, columnspan=3, sticky="w", pady=10)

        # Log text box
        self.log_label = tk.Label(self.frame, text="Log:", bg=self.primary_color, fg=self.text_color)
        self.log_label.grid(row=11, column=0, sticky="w", pady=2)
        self.log_text = tk.Text(self.frame, height=10, width=60, state="disabled", bg=self.secondary_color, fg=self.text_color, wrap="none")
        self.log_text.grid(row=12, column=0, columnspan=3, pady=5, sticky="w")
        self.log_scrollbar = tk.Scrollbar(self.frame, command=self.log_text.yview, bg=self.primary_color)
        self.log_scrollbar.grid(row=12, column=3, sticky="ns")
        self.log_text.config(yscrollcommand=self.log_scrollbar.set)

        self.bootloader_file = None
        self.partitions_file = None
        self.firmware_file = None
        self.selected_file = None

    def browse_file(self):
        self.selected_file = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])
        if self.selected_file:
            self.file_label.config(text=f"Selected File: {self.selected_file}")

    def browse_bootloader(self):
        self.bootloader_file = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])
        if self.bootloader_file:
            self.bootloader_label.config(text=f"Selected: {self.bootloader_file}")

    def browse_partitions(self):
        self.partitions_file = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])
        if self.partitions_file:
            self.partitions_label.config(text=f"Selected: {self.partitions_file}")

    def browse_firmware(self):
        self.firmware_file = filedialog.askopenfilename(filetypes=[("Binary files", "*.bin")])
        if self.firmware_file:
            self.firmware_label.config(text=f"Selected: {self.firmware_file}")

    def refresh_ports(self):
        ports = self.get_serial_ports()
        self.serial_combobox["values"] = ports
        if ports:
            self.serial_combobox.set(ports[0])
        else:
            self.serial_combobox.set("")
        self.update_log("COM ports updated.")

    def get_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def start_ota_upload(self):
        ip_address = self.ip_entry.get()
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a .bin file.")
            return
        if not ip_address:
            messagebox.showerror("Error", "Please enter the ESP32 IP address.")
            return
        self.update_log("Starting OTA update...", clear=True)
        threading.Thread(target=self.upload_firmware_ota, args=(ip_address,), daemon=True).start()

    def upload_firmware_ota(self, ip_address):
        try:
            current_dir = os.path.dirname(os.path.abspath(sys.executable))
            espota_path = os.path.join(current_dir, "espota.exe")

            if not os.path.exists(espota_path):
                self.update_log(f"Error: espota.exe not found in {current_dir}")
                messagebox.showerror("Error", "espota.exe not found.")
                return

            command = [
                espota_path,
                "--ip", ip_address,
                "--port", "3232",
                "--file", self.selected_file
            ]

            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )

            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    self.update_log(output.strip())

            process.wait()

            if process.returncode == 0:
                self.update_log("OTA Update completed successfully.")
                messagebox.showinfo("Success", "OTA Update successful.")
            else:
                self.update_log("OTA Update failed.")
                messagebox.showerror("Error", "OTA Update failed.")

        except Exception as e:
            self.update_log(f"Error: {e}")
            messagebox.showerror("Error", f"Failed to execute OTA update: {e}")

    def start_serial_upload(self):
        com_port = self.serial_combobox.get()
        baud_rate = self.baud_combobox.get()
        if not all([self.bootloader_file, self.partitions_file, self.firmware_file]):
            messagebox.showerror("Error", "Please select all required .bin files.")
            return
        if not com_port:
            messagebox.showerror("Error", "Please select a COM port.")
            return
        self.update_log(f"Starting Serial update at {baud_rate} baud...", clear=True)
        threading.Thread(target=self.upload_firmware_serial, args=(com_port, baud_rate), daemon=True).start()

    def upload_firmware_serial(self, com_port, baud_rate):
        try:
            # `esptool.exe` を直接参照
            esptool_path = os.path.join(os.path.dirname(sys.executable), "esptool.exe")
            if not os.path.exists(esptool_path):
                self.update_log(f"Error: esptool.exe not found.")
                messagebox.showerror("Error", "esptool.exe not found.")
                return

            commands = [
                [esptool_path, "--port", com_port, "--baud", baud_rate, "write_flash", "0x0000", self.bootloader_file],
                [esptool_path, "--port", com_port, "--baud", baud_rate, "write_flash", "0x8000", self.partitions_file],
                [esptool_path, "--port", com_port, "--baud", baud_rate, "write_flash", "0x10000", self.firmware_file],
            ]

            for command in commands:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
                while True:
                    output = process.stdout.readline()
                    if output == "" and process.poll() is not None:
                        break
                    if output:
                        self.update_log(output.strip())

                process.wait()
                if process.returncode != 0:
                    self.update_log("Serial Update failed.")
                    messagebox.showerror("Error", "Serial Update failed.")
                    return

            self.update_log("Serial Update completed successfully.")
            messagebox.showinfo("Success", "Serial Update successful.")

        except Exception as e:
            self.update_log(f"Error: {e}")
            messagebox.showerror("Error", f"Failed to execute Serial update: {e}")

    def update_log(self, message, clear=False):
        self.log_text.config(state="normal")
        if clear:
            self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = OTAUploaderApp(root)
    root.mainloop()
