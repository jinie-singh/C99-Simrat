import os
import shutil
import time

start_time = time.time()
path = input("Enter source floder name: ")
days = input("Number of days before files You want to seperate: ")
seconds = time.time() - (days * 24 * 60 * 60) #to calculate time in seconds
days = days*3600
path1 = path+"/"
destination1 = os.mkdir(path1+"Older")
list_of_files= os.listdir(path)

#function to calculate the time
def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
    #int(ctime)
	return ctime

if os.path.exists(path):
    for root_folder, folders, files in os.walk(path):
        if seconds >= get_file_or_folder_age(root_folder):
            shutil.move(path1+files,destination1)
            break
        else:
            for folder in folders:
                folder_path = os.path.join(root_folder, folder)
                if seconds >= get_file_or_folder_age(folder_path):
                   shutil.move(path1+files,destination1)
            for file in files:
                file_path = os.path.join(root_folder, file)
                if seconds >= get_file_or_folder_age(file_path):
                    shutil.move(path1+files,destination1)
                else:
                    if seconds >= get_file_or_folder_age(path):
                       shutil.move(path1+files,destination1)
else:
    print(f'"{path}" is not found')
	