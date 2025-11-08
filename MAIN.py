import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/LENOVO/Pictures/Screenshots"              #this is folder that need to be backuped 
destination_dir = "E:/Automated backup (project folder)"         #this is folder where backup files going to be stored 

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir, dirs_exist_ok=True)
        print(f"✅Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"⚠️Folder already exists: {dest_dir}")
    

#scheduling for 3:15pm everday
schedule.every().day.at("15:15").do(lambda: copy_folder_to_directory(source_dir, destination_dir))          

copy_folder_to_directory(source_dir, destination_dir)

try:
    while True:
        schedule.run_pending()
        time.sleep(60)
except KeyboardInterrupt:
    print("Scheduler stopped by user")
