import stat
import datetime
import os
import time
import shutil

def moveFiles(src = "C:\\Users\\matt\\Desktop\\Folder 1\\", dest = "C:\\Users\\matt\\Desktop\\Folder 2\\"):
    
    dirs = os.listdir(src)

    statbuf = os.stat(src)
    mod_time= statbuf.st_mtime
    print("Modification time:",statbuf.st_mtime) 

    last_time = (time.time() - mod_time) / 60
    last_time_hours = ((time.time() - mod_time)/60)/60

    print("Last modified: ", int(last_time), "minutes ago")



    for file in dirs:
        statbuf = os.stat(src + file)
        mod_file= statbuf.st_mtime
        last_time_file = (time.time() - mod_file) / 60
        last_time_file_hours = ((time.time() - mod_file)/60)/60
        
        print("Last modified: ", file, int(last_time_file), " minutes ago")
        
        print("Last modified: ", file, last_time_file_hours, "hours ago")
        
        if last_time_file_hours <= 24:
            print("Files moved: ", src +file)
            shutil.move(src + file, dest)







