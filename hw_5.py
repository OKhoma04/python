import os
import sys
import time
import datetime

file_name = sys.argv[2]     #verify file name argument from cmd
file_path = sys.argv[1]     #verify file path argument from cmd

full_name = file_path + '/' + file_name     #full path for file

#Check file metadata (created date, modification date)
def file_metadata (full_name):
    modified = os.path.getmtime(full_name)
    print("Date modified: ", time.ctime(modified))
    created = os.path.getctime(full_name)
    print("Date created: ", time.ctime(created))
    size = os.path.getsize(full_name)
    print("Size is: ", size)



#Check directory and file existance
def filelocation (file_path, file_name):
    if os.path.exists(file_path):               #check directory existance
        print('file_path', file_path)
        if file_name in os.listdir(file_path):  #check file existance in mentioned directory
            print('file_name', file_name)
            file_metadata (full_name)
        else:
            print('This file does not exist')
            new_file = open(full_name,'w')
            print('New file' ,file_name, 'has been created')
            #file_metadata (full_name)
            for all_files in os.listdir(file_path):     #Shows metadata for each file in mentioned directory
                full_name_files = file_path + '/' + all_files
                print(full_name_files)
                file_metadata (full_name_files)
    else:
        print('This directory does not exist')
        os.mkdir(file_path)                                     #create a directory if it not exists
        print('New directory' , file_path , 'has been created')
        new_file = open(full_name,'w')
        print('New file' ,file_name, 'has been created')
        file_metadata (full_name)


filelocation (file_path, file_name)
