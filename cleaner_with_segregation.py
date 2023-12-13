import os
import shutil

def create_dir(cleanup_dir):
    if not os.path.exists(cleanup_dir): 
        os.makedirs(cleanup_dir)
        last_part = cleanup_dir.split("/")
        print ("Creating folder " + last_part[1] + "...")
    return cleanup_dir

def get_necessary_dir(new_directories, file):
    necessary_dir = False
    for i in new_directories:
        if i == file:
            necessary_dir = i
    return necessary_dir

def get_dir_name (ext):
    dir_type = ""
    if ext == "bmp" or "gif" or "ico" or "jpeg" or "jpg" or "png" or "raw" or "tif" or "tiff":
        dir_type = "Images"
    elif ext == "doc" or "docx" or "odt" or "pages" or "rtf" or "txt" or "wpd" or "wps":
        dir_type = "Texts"
    elif ext == "aif" or "mp3" or "wav" or "wma":
        dir_type = "Music"
    elif ext == "mov" or "mp4" or "mpg" or "wmv":
        dir_type = "Videos"
    dir_name = desktop_dir + "/" + dir_type
    new_directories.append(dir_type)
    return dir_name



desktop_dir = r"C:\Users\wikto\OneDrive\Pulpit"

all_files = os.listdir(desktop_dir)
new_directories = []

for file in all_files:
    necessary_dir = get_necessary_dir(new_directories, file)
    if file != __file__ and file!= "standard_cleaner.bat" and file != necessary_dir:
        file_dir = desktop_dir + "/" + file
        file = file.split()
        ext = file[len(file)-1]
        cleanup_dir_name = get_dir_name (ext)
        cleanup_dir = create_dir(cleanup_dir_name)
        #shutil.move(file_dir, cleanup_dir)
        print ("Moving file " + file + "...")