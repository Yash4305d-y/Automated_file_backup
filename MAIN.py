import os
import shutil
import datetime
import schedule
import time
import tkinter as tk
from tkinter import filedialog, simpledialog

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, dest_dir, dirs_exist_ok=True)
        print(f"✅ Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"⚠️ Folder already exists: {dest_dir}")

def main():
    root = tk.Tk()
    root.withdraw()
    print("📁 Select the folder you want to back up:")
    source_dir = filedialog.askdirectory(title="Select Source Folder")
    if not source_dir:
        print("❌ No source folder selected.")
        return

    print("📦 Select where to save backups:")
    destination_dir = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_dir:
        print("❌ No destination folder selected.")
        return

    time_input = simpledialog.askstring("Backup Time", "Enter backup time (HH:MM, 24-hour format):")
    if not time_input:
        print("❌ No time entered.")
        return

    schedule.every().day.at(time_input).do(lambda: copy_folder_to_directory(source_dir, destination_dir))
    print(f"⏰ Backup scheduled daily at {time_input}")
    copy_folder_to_directory(source_dir, destination_dir)

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Scheduler stopped by user.")

if __name__ == "__main__":
    main()
