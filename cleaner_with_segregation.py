import os
import shutil
import datetime

def create_dir(cleanup_dir, x):
    cleanup_dir = r"C:\Users\wikto\OneDrive\Pulpit/" + x
    if not os.path.exists(cleanup_dir): 
        os.makedirs(cleanup_dir)
        last_part = cleanup_dir.split("/")
        print ("Creating folder " + last_part[1] + "...")
    return cleanup_dir


desktop_dir = r"C:\Users\wikto\OneDrive\Pulpit"

all_files = os.listdir(desktop_dir)

for file in all_files:

    if file != __file__ and file!= "standard_cleaner.bat":
        file_dir = desktop_dir + "/" + file
        x = ""
        cleanup_dir = create_dir(cleanup_dir, x)
        shutil.move(file_dir, cleanup_dir)
        print ("Moving file " + file + "...")