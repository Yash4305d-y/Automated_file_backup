import os
import shutil
import datetime
import schedule
import time
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    os.makedirs(dest_dir, exist_ok=True)

    for root_dir, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root_dir, source)
        dest_path = os.path.join(dest_dir, rel_path)
        os.makedirs(dest_path, exist_ok=True)
        for file in files:
            src_file = os.path.join(root_dir, file)
            dest_file = os.path.join(dest_path, file)
            try:
                shutil.copy2(src_file, dest_file)
            except PermissionError:
                print(f"⚠️ Skipped (Access Denied): {src_file}")
            except Exception as e:
                print(f"❌ Error copying {src_file}: {e}")

    print(f"✅ Folder copied to {dest_dir}")
    messagebox.showinfo("Backup Completed", f"Backup successfully saved to:\n{dest_dir}")

def ask_yes_no(title, question):
    temp = tk.Tk()
    temp.withdraw()
    temp.after(100, lambda: temp.lift())  # ensure focus
    temp.attributes('-topmost', True)
    answer = messagebox.askyesno(title, question, parent=temp)
    temp.destroy()
    return answer

def main():
    root = tk.Tk()
    root.withdraw()

    print("📁 Select the folder you want to back up:")
    source_dir = filedialog.askdirectory(title="Select Source Folder", parent=root)
    if not source_dir:
        print("❌ No source folder selected.")
        return

    print("📦 Select where to save backups:")
    destination_dir = filedialog.askdirectory(title="Select Destination Folder", parent=root)
    if not destination_dir:
        print("❌ No destination folder selected.")
        return

    time_input = simpledialog.askstring("Backup Time", "Enter backup time (HH:MM, 24-hour format):", parent=root)
    if not time_input:
        print("❌ No time entered.")
        return

    user_choice = ask_yes_no(
        "Backup Option",
        "Do you want to schedule it for later?\n\n✅ Yes → Schedule daily backups\n❌ No → Run one immediate backup"
    )

    if user_choice:
        schedule.every().day.at(time_input).do(lambda: copy_folder_to_directory(source_dir, destination_dir))
        print(f"⏰ Backup scheduled daily at {time_input}")
        messagebox.showinfo("Scheduled", f"Backup scheduled daily at {time_input}.\nKeep this window open.")
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print("🛑 Scheduler stopped by user.")
    else:
        copy_folder_to_directory(source_dir, destination_dir)

if __name__ == "__main__":
    main()
