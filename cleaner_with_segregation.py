import os
import shutil

def create_dir(cleanup_dir_name):
    if not os.path.exists(cleanup_dir_name): 
        last_part = cleanup_dir_name.split("/")
        print ("Creating folder " + last_part[1] + "...")
        #os.makedirs(cleanup_dir_name)
    return cleanup_dir_name

def get_necessary_dir(new_directories, file):
    necessary_dir = False
    for i in new_directories:
        if i == file:
            necessary_dir = i
    return necessary_dir

def get_list (text):
    lines = []
    with open(text) as file:
        for line in file: 
            line = line.strip()
            lines.append(line) 
    return lines

def get_dir_name (ext):
    dir_type = ""

    files = [r"Compression‏‏‎ files.txt", r"Draw‏‏‎ ‎files.txt", r"Executable‏‏‎ ‎files.txt", r"Images.txt", r"Music.txt", r"Page‏‏‎ ‎layouts.txt", r"Presentations.txt", r"Programming ‎files.txt", r"Shortcuts.txt", r"Spreadsheets.txt", r"System‏‏‎ files.txt", r"Texts.txt", r"Videos.txt", r"Web‏‏‎ ‎files.txt",]
    for notepad in files:
        list = get_list(notepad)
        for extension in list:
            if str(extension) == str(ext):
                notepad.split(".")
                dir_type = notepad[0]
        else:
            dir_type = "Others"
    
    dir_name = desktop_dir + "/" + dir_type
    new_directories.append(dir_type)
    return dir_name



desktop_dir = r"C:\Users\wikto\OneDrive\Pulpit"

all_files = os.listdir(desktop_dir)
new_directories = []

for file in all_files:
    necessary_dir = get_necessary_dir(new_directories, file)
    if file != __file__ and file!= "cleaner_with_segregation.bat" and file != necessary_dir:
        file_dir = desktop_dir + "/" + file
        file_splitted = file.split(".")
        ext = file_splitted[len(file_splitted)-1]        
        cleanup_dir_name = get_dir_name (ext)
        cleanup_dir = create_dir(cleanup_dir_name)
        #shutil.move(file_dir, cleanup_dir)
        print ("Moving file " + file + "...")