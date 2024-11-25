import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Function to perform file backup
def backup_files():
    # Ask user to select the source folder (files to backup)
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    if not source_folder:
        return  # If no source folder is selected, exit function
    
    # Ask user to select the destination folder (backup location)
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_folder:
        return  # If no destination folder is selected, exit function

    try:
        # Get the folder name from the source path
        folder_name = os.path.basename(source_folder)

        # Create the destination path
        destination_path = os.path.join(destination_folder, folder_name)

        # Initialize progress bar
        total_files = sum([len(files) for _, _, files in os.walk(source_folder)])
        processed_files = 0
        progress_bar['maximum'] = total_files
        progress_bar['value'] = 0
        root.update_idletasks()

        # Perform the backup (copy the files)
        for root_dir, _, files in os.walk(source_folder):
            for file_name in files:
                # Define the full path of the file
                source_file = os.path.join(root_dir, file_name)
                relative_path = os.path.relpath(source_file, source_folder)
                destination_file = os.path.join(destination_path, relative_path)

                # Create subdirectories in the destination if needed
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)

                # Copy the file to the backup destination
                shutil.copy2(source_file, destination_file)
                processed_files += 1

                # Update progress bar
                progress_bar['value'] = processed_files
                root.update_idletasks()

        # Success message
        status_label.config(text="Backup Successful!", fg="green")
        messagebox.showinfo("Success", f"Backup completed successfully!\nFiles backed up: {total_files}")

    except Exception as e:
        # Handle any error that occurs during the backup
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="Backup Failed", fg="red")
        progress_bar['value'] = 0

# GUI Setup
root = tk.Tk()
root.title("File Backup Tool")
root.geometry("600x350")
root.configure(bg="#f0f0f0")  # Light grey background

# Header Label
header_label = tk.Label(root, text="File Backup Tool", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
header_label.pack(pady=15)

# Instruction Label
instruction_label = tk.Label(
    root, 
    text="Select the source and destination folders to backup files.", 
    font=("Arial", 12), 
    bg="#f0f0f0", 
    fg="#555"
)
instruction_label.pack(pady=10)

# Button to trigger backup
backup_button = tk.Button(
    root, 
    text="Select Folders and Start Backup", 
    command=backup_files, 
    font=("Arial", 10), 
    bg="#4CAF50",  # Green background
    fg="black", 
    activebackground="#45a049",  # Slightly darker green when clicked
    padx=10, 
    pady=5
)
backup_button.pack(pady=20)

# Progress bar for backup process
progress_bar = ttk.Progressbar(root, length=450, mode='determinate')
progress_bar.pack(pady=10)

# Status label to display messages
status_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f0f0", fg="#555")
status_label.pack(pady=5)

# Footer Label
footer_label = tk.Label(
    root, 
    text="Developed by Abhinandan | File Backup Tool", 
    font=("Arial", 8), 
    bg="#f0f0f0", 
    fg="#888"
)
footer_label.pack(side="bottom", pady=15)

root.mainloop()
