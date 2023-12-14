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
    if ext == "bmp" or "gif" or "ico" or "jpeg" or "jpg" or "png" or "raw" or "tif" or "tiff" or "eps" or "psd":
        dir_type = "Images"
    elif ext == "doc" or "docx" or "odt" or "pages" or "rtf" or "txt" or "wpd" or "wps":
        dir_type = "Texts"
    elif ext == "aif" or "mp3" or "wav" or "wma":
        dir_type = "Music"
    elif ext == "mov" or "mp4" or "mpg" or "wmv":
        dir_type = "Videos"
    elif ext == "csv" or "numbers" or "ods" or "xls" or "xlsx":
        dir_type = "Spreadsheets"   
    elif ext == "asp" or "aspx" or "css" or "htm" or "html" or "jsp" or "php" or "vsdx":
        dir_type = "Web_files"   
    elif ext == "bak" or "cfg" or "conf" or "ini" or "msi" or "sys" or "tmp":
        dir_type = "System_files"
    elif ext == "7z" or "rar" or "tar" or "gz" or "zip":
        dir_type = "Compression_files"
    elif ext == "ink" or "url":
        dir_type = "Shortcuts"
    elif ext == "app" or "bat" or "bin" or "cmd" or "com" or "exe" or "vbs" or "x86":
        dir_type = "Executable_files"
    elif ext == "afpub" or "indd" or "pdfxml" or "pmd" or "pub" or "qxp":
        dir_type = "Page_layouts" 
    elif ext == "afdesign" or "ai" or "cad" or "cdr" or "drw" or "dwg" or "eps" or "odg" or "svg" or "vsdx":
        dir_type = "Draw_files" 
    elif ext == "c" or "cpp" or "cs" or "css" or "java" or "js" or "json" or "py" or "sql" or "swift" or "vb":
        dir_type = "Programming_files" 
    elif ext == "pptx" or "ppt" or "pptm" or "pptx" or "odp":
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
        #shutil.move(file_dir, cleanup_dir)
        #print ("Moving file " + file + "...")