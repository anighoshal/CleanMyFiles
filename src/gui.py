# src/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from main import setup_target_folders, scan_files, map_files_to_categories, organize_files

def run_gui():
    # Create main window
    window = tk.Tk()
    window.title("CleanMyFiles - File Organizer")
    window.geometry("500x250")
    window.resizable(False, False)

    # Label
    label = tk.Label(window, text="Select a folder to organize:", font=("Arial", 12))
    label.pack(pady=10)

    # Folder path display
    folder_path_var = tk.StringVar()
    folder_entry = tk.Entry(window, textvariable=folder_path_var, width=50)
    folder_entry.pack(pady=5)

    # Browse button
    def browse_folder():
        selected_folder = filedialog.askdirectory()
        folder_path_var.set(selected_folder)

    browse_btn = tk.Button(window, text="Browse", command=browse_folder)
    browse_btn.pack(pady=5)

    # Organize button
    def organize_action():
        path = folder_path_var.get()
        if not path:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return

        setup_target_folders(path)
        files = scan_files(path)
        file_map = map_files_to_categories(files, path)
    
        # ✅ Only call organize_files once and capture the return value
        moved_count = organize_files(file_map)
    
        messagebox.showinfo("Done", f"Organized {moved_count} files.")


    organize_btn = tk.Button(window, text="Organize Files", command=organize_action, bg="#4CAF50", fg="white")
    organize_btn.pack(pady=20)

    # Start GUI loop
    window.mainloop()
