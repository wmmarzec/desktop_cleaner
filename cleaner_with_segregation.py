import os
import shutil

def create_dir(cleanup_dir_name):
    if not os.path.exists(cleanup_dir_name): 
        last_part = cleanup_dir_name.split("/")
        print ("Creating folder " + last_part[1] + "...")
        os.makedirs(cleanup_dir_name)
    return cleanup_dir_name

def get_necessary_dir(new_directories, file):
    necessary_dir = False
    for i in new_directories:
        if i == file:
            necessary_dir = i
    return necessary_dir

def get_dir_name (ext):
    print(ext)
    dir_type = ""
    if ext == "bmp" or ext == "gif" or ext == "ico" or ext == "jpeg" or ext == "jpg" or ext == "png" or ext == "raw" or ext == "tif" or ext == "tiff" or ext == "eps" or ext == "psd":
        dir_type = "Images"
    elif ext == "doc" or ext == "docx" or ext == "odt" or ext == "pages" or ext == "rtf" or ext ==  "txt" or ext ==  "wpd" or ext == "wps":
        dir_type = "Texts"
    elif ext == "aif" or ext == "mp3" or ext == "wav" or ext == "wma":
        dir_type = "Music"
    elif ext == "mov" or ext == "mp4" or ext == "mpg" or ext == "wmv":
        dir_type = "Videos"
    elif ext == "csv" or ext == "numbers" or ext ==  "ods" or ext == "xls" or ext == "xlsx":
        dir_type = "Spreadsheets"   
    elif ext == "asp" or ext == "aspx" or ext == "css" or ext == "htm" or ext == "html" or ext ==  "jsp" or ext ==  "php" or ext ==  "vsdx":
        dir_type = "Web_files"   
    elif ext == "bak" or ext ==  "cfg" or ext ==  "conf" or ext ==  "ini" or  ext ==  "msi" or ext ==  "sys" or ext ==  "tmp":
        dir_type = "System_files"
    elif ext == "7z" or ext == "rar" or ext ==  "tar" or ext ==  "gz" or ext == "zip":
        dir_type = "Compression_files"
    elif ext == "lnk" or ext ==  "url":
        dir_type = "Shortcuts"
    elif ext == "app" or ext ==  "bat" or ext ==  "bin" or ext == "cmd" or ext == "com" or ext == "exe" or ext == "vbs" or ext == "x86":
        dir_type = "Executable_files"
    elif ext == "afpub" or ext == "indd" or ext == "pdfxml" or ext == "pmd" or ext == "pub" or ext == "qxp":
        dir_type = "Page_layouts" 
    elif ext == "afdesign" or ext == "ai" or ext == "cad" or ext == "cdr" or ext ==  "drw" or ext ==  "dwg" or ext == "eps" or ext == "odg" or ext ==  "svg" or ext ==  "vsdx":
        dir_type = "Draw_files" 
    elif ext == "c" or ext == "cpp" or ext == "cs" or ext == "css" or ext == "java" or ext == "js" or ext == "json" or ext == "py" or ext == "sql" or ext == "swift" or ext == "vb":
        dir_type = "Programming_files" 
    elif ext == "pptx" or ext == "ppt" or ext == "pptm" or ext == "pptx" or ext == "odp":
        dir_type = "Presentations" 
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
        shutil.move(file_dir, cleanup_dir)
        print ("Moving file " + file + "...")