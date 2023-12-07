import os
import shutil

cleanup_dir = r"C:\Users\wikto\OneDrive\Pulpit\Cleanup"
desktop_dir = r"C:\Users\wikto\OneDrive\Pulpit"

if not os.path.exists(cleanup_dir): 
    os.makedirs(cleanup_dir) 
    print ("Creating folder...")

all_files = os.listdir(desktop_dir)

for file in all_files:
    if file != __file__:
        file_dir = desktop_dir + "/" + file
        shutil.move(file_dir, cleanup_dir)
        print ("Moving file...")
