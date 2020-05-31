import os
import sys

def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


image_category = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", 
                 ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic",".ind", ".indd", ".indt",
                 ".jp2", ".j2k"," .jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai",".eps",".ico"]

document_category =[".docx", ".doc", ".docm", ".dot", ".dotm", ".dotx",".xltx", ".xltm", ".xlt", 
                    ".xlsx", ".xlsm", ".xlsb", ".xls", ".xll", ".xlam", ".xla", ".pptx", ".pptm", ".ppt", ".ppsx",
                    ".ppsm", ".pps", ".ppam"," .ppa", ".potx", ".potm", ".pot" ,".accdb", ".mdb", ".vstx", ".vstm",
                    ".vst", ".vssx", ".vssm", ".vssm", ".vss", ".vsl", ".vsdx", ".vsdm", ".vsd", ".vdw",".pub", ".xsn", ".xsf",
                    ".mpp"," .odt", ".ods", ".odp",  ".htm", ".html", ".pdf", ".txt"]

video_category = [".webm", ".mkv", ".flv", ".vob"," .ogv", ".ogg" ,".drc" ,".gif" ,".gifv" ,".mng ",".avi" ,".MTS", ".M2TS", ".TS ",".mov", ".qt"
                ,".wmv" ,".yuv" ,".rm" ,".rmvb" ,".asf" ,".amv" ,".mp4", ".m4p", ".m4v ",".mpg", ".mp2", ".mpeg", ".mpe", ".mpv"
                ,".mpg", ".mpeg", ".m2v" ,".m4v ",".svi", ".3gp" ,".3g2" ,".mxf" ,".roq" ,".nsv" ,".flv", ".f4v", ".f4pz",".f4a" ,".f4b"]

audio_category = [".aa", ".aac" ,".aax", ".act", ".aiff", ".alac" ,".amr", ".ape" ,".au", ".awb", ".dct" ,".dss", ".dvf" ,".flac", ".gsm" ,
				 ".iklax", ".ivs", ".m4a", ".m4b", ".m4p"," .mmf",".mp3", ".mpc", ".msv", ".nmf", ".nsf", ".ogg", ".oga", ".mogg", ".opus",
				 ".ra", ".rm", ".raw", ".sln", ".tta" ,".voc", ".vox" ,".wav", ".wma", ".wv", ".webm" ,".8svx"]

archive_category = [".zip", ".7z", ".arj",".pkg", ".rar", ".z", ".deb", ".tar.gz",".gz", ".rpm", ".bin", ".iso", ".dmg", ".tost", ".vcd"]




dirs = []
folders = []
files  = []


images = []
documents = []
audios = []
videos = []
archives = []
others = []



def mem_status():
    total_storage = len(dirs)
    images_storage = len(images)
    documents_storage = len(documents)
    videos_storage = len(videos)
    audios_storage = len(audios)
    archives_storage = len(archives)
    others_storage = len(others)

    per_images = round((images_storage/total_storage)*100,2)
    per_documents = round((documents_storage/total_storage)*100,2)
    per_videos = round((videos_storage/total_storage)*100,2)
    per_audios = round((audios_storage/total_storage)*100,2)
    per_archives = round((archives_storage/total_storage)*100,2)
    per_others = round((others_storage/total_storage)*100,2)
    percentages = [per_images, per_documents, per_videos, per_audios, per_archives, per_others]
    actual_num = [total_storage, images_storage, documents_storage, videos_storage, audios_storage,archives_storage,others_storage]
    return [percentages, actual_num]





def classifier():
    images.clear()
    documents.clear()
    videos.clear()
    audios.clear()
    archives.clear()
    others.clear()
    image_set = set(image_category)
    audio_set = set(audio_category)
    video_set = set(video_category)
    document_set = set(document_category)
    archive_set = set(archive_category)
    import os
    for fls in files:
        ext = os.path.splitext(fls)[1]
        if ext in image_set:
            images.append(fls)
        elif ext in document_set:
            documents.append(fls)
        elif ext in video_set:
            videos.append(fls)
        elif ext in audio_set:
            audios.append(fls)
        elif ext in archive_set:
            archives.append(fls)
        else:
            others.append(fls)
        


def seperate_file_folder(paths):
    paths = os.path.normpath(paths)
    for drs in os.listdir(paths):
        dirs.append(os.path.join(paths,drs))
    for fls in dirs:
        if os.path.isfile(fls):
            files.append(fls)    
        elif os.path.isdir(fls):
            folders.append(fls)
    classifier()
    allocation_memory = mem_status()
    dirs.clear()
    folders.clear()
    files.clear()
    return allocation_memory


def create_space_download(paths):
    n_path = os.path.normpath(paths)
    main_path = os.path.join(n_path,"Download Clutter")
    images_path = os.path.join(main_path,"Images")
    docs_path = os.path.join(main_path,"Documnets")
    audio_path = os.path.join(main_path,"Audio")
    video_path = os.path.join(main_path,"Videos")
    archives_path = os.path.join(main_path,"Archives")
    others_path = os.path.join(main_path,"Others")
    try:
        error = []
        success = []
        if not os.path.exists(main_path):
            os.mkdir(main_path)
            success.append(1000)
        else:
             error.append(1000)

        os.chdir(main_path)

        if not os.path.exists(images_path):
            os.mkdir(images_path)
            success.append(1001)
        else:
            error.append(1001)

        if  not os.path.exists(docs_path):
            os.mkdir(docs_path)
            success.append(1002)
        else:
            error.append(1002)

        if not os.path.exists(audio_path):
            os.mkdir(audio_path)
            success.append(1003)
        else:
            error.append(1003)

        if not os.path.exists(video_path):
            os.mkdir(video_path)
            success.append(1004)
        else:
            error.append(1004)
        if not os.path.exists(archives_path):
            os.mkdir(archives_path)
            success.append(1005)
        else:
            error.append(1005)
        if not os.path.exists(others_path):
            os.mkdir(others_path)
            success.append(1006)
        else:
            error.append(1006)
                
        return 1,error,success
    except :
        return 0

def create_space_others(paths):
    n_path = os.path.normpath(paths)
    main_path = os.path.join(n_path,"Folder Clutter")
    images_path = os.path.join(main_path,"Images")
    docs_path = os.path.join(main_path,"Documnets")
    audio_path = os.path.join(main_path,"Audio")
    video_path = os.path.join(main_path,"Videos")
    archives_path = os.path.join(main_path,"Archives")
    others_path = os.path.join(main_path,"Others")
    try:
        error = []
        success = []
        if not os.path.exists(main_path):
            os.mkdir(main_path)
            success.append(1000)
        else:
             error.append(1000)

        os.chdir(main_path)

        if not os.path.exists(images_path):
            os.mkdir(images_path)
            success.append(1001)
        else:
            error.append(1001)

        if  not os.path.exists(docs_path):
            os.mkdir(docs_path)
            success.append(1002)
        else:
            error.append(1002)

        if not os.path.exists(audio_path):
            os.mkdir(audio_path)
            success.append(1003)
        else:
            error.append(1003)

        if not os.path.exists(video_path):
            os.mkdir(video_path)
            success.append(1004)
        else:
            error.append(1004)
        if not os.path.exists(archives_path):
            os.mkdir(archives_path)
            success.append(1005)
        else:
            error.append(1005)
        if not os.path.exists(others_path):
            os.mkdir(others_path)
            success.append(1006)
        else:
            error.append(1006)
                
        return 1,error,success
    except :
        return 0


    

def get_formatted_date():
    from datetime import date
    days = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    today = date.today()
    to_day = (today.weekday())
    format_date = today.strftime("%d %b %Y") +" "+ days[to_day]
    return format_date


def system_details():
    import platform
    import psutil
    total_disk = 0
    used_disk = 0
    os_name = platform.system()+" "+platform.release()
    platform_machine = platform.node()
    processor_info = platform.processor()
    total_ram = psutil.virtual_memory().total/(1<<30)
    used_ram = psutil.virtual_memory().used/(1<<30)
    for x in psutil.disk_partitions():
        if x[3] == 'rw,fixed':
            total_disk += psutil.disk_usage(x[1]).total/(1<<30)
            used_disk += psutil.disk_usage(x[1]).used/(1<<30)
    per_ram = (used_ram/total_ram)*100
    per_disk = (used_disk/total_disk)*100
       
    output = [ os_name, processor_info, platform_machine, total_ram, used_ram, total_disk, used_disk , per_disk, per_ram]
    return output

def download_clutter_counter():
    status = seperate_file_folder(get_download_path())
    return status


def clutter_size(paths):
    total_size = 0
    for path, dirs, files in os.walk(paths):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
        for d in dirs:
            dir = os.path.join(path,d)
            total_size += os.path.getsize(dir)

    return total_size/(1<<30)

def open_downloads():
    import subprocess
    dpath = get_download_path()
    subprocess.Popen('explorer %s'%(dpath))

def save_download_path(path1,path2):
    p1 = os.path.abspath(path1)
    p2 = os.path.abspath(path2)
    paths = {
        "Downloads path": p1,
        "Others path": p2,
    }

    import json
    with open("prefs.json","w") as pathfile:
        json.dump(paths, pathfile)
        

def load_paths():
    import json
    with open("prefs.json","r") as pathfile:
        data = json.load(pathfile)
    dpath = data["Downloads path"]
    opath = data["Others path"]
    return [dpath,opath]
    
    
    
def move_clutter(move_type):
    import time
    import shutil
    path_load = load_paths()
    if move_type == "others":
        path_request = path_load[1]
        base_folder = 'Folder Clutter'
    elif move_type == 'downloads':
        seperate_file_folder(get_download_path())
        path_request = path_load[0]
        base_folder = 'Download Clutter'
    req_path = path_request
    req_path = os.path.normpath(req_path)
    req_path = os.path.join(req_path,base_folder)
    if images:
        for files in images:
            shutil.move(files, os.path.join(req_path,'Images'))
            yield files 
    if documents:
        for files in documents:
            shutil.move(files, os.path.join(req_path,'Documnets'))
            yield files
    if audios:
        for files in audios:
            shutil.move(files, os.path.join(req_path,'Audios'))
            yield files
    if videos:
        for files in videos:
            shutil.move(files, os.path.join(req_path,'Videos'))
            yield files
    if archives:
        for files in archives:
            shutil.move(files, os.path.join(req_path,'Archives'))
            yield files
    if others:
        for files in others:
            shutil.move(files, os.path.join(req_path,'Others'))
            yield files


                
    
       
        






