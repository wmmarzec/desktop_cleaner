import os
import shutil
import datetime

x = datetime.datetime.now()
x = (x.strftime("%Y" + "-" +"%m" + "-" + "%d"))
dir_name = "Cleanup-" + x

cleanup_dir = r"C:\Users\wikto\OneDrive\Pulpit/" + dir_name
print (cleanup_dir)
desktop_dir = r"C:\Users\wikto\OneDrive\Pulpit"

if not os.path.exists(cleanup_dir): 
    os.makedirs(cleanup_dir)
    last_part = cleanup_dir.split("/")
    print ("Creating folder " + last_part[1] + "...")

all_files = os.listdir(desktop_dir)

for file in all_files:
    if file != __file__ and file != last_part[1]:
        file_dir = desktop_dir + "/" + file
        shutil.move(file_dir, cleanup_dir)
        print ("Moving file " + file + "...")
