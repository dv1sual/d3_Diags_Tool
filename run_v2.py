import os
import tkinter as tk
from tkinter import filedialog
# import subprocess

#! FUNCTIONS

def get_files_in_filelist(diag_path): # lists all files in a given diag
    """Read and print all the files name in the filelist.txt file"""
    filelist_path = os.path.join(diag_path, "filelist.txt") # make the path to filelist.txt in the path
    if os.path.isfile(filelist_path): # check the file exists
        with open(filelist_path, 'rb') as file_in: # open filelist.txt
            in_lines = file_in.readlines() # read all lines
            return in_lines # return all the lines
    else:
        print("not found")
        return []

def get_videofiles(all_files_list):
    """Read and get all the files name from VideoFiles folder from the list"""
    video_file_dict = {} # make an empty dict to hold path-file names
    for file in all_files_list: # go through all the files looking for video files
        if b'objects\\VideoFile' and b'.mov' in file and b'internal' not in file and b'videoin' not in file:  # is this a video file?
            decoded_path = file.decode()  # decode to a string
            decoded_path = decoded_path.replace(decoded_path.split('\t')[-1], '')  # remove size
            decoded_path = decoded_path.replace('\t', '')  # remove whitespace
            sub_dir, file_name = os.path.split(decoded_path)  # split into path-file name
            if sub_dir not in video_file_dict:
                video_file_dict[sub_dir] = [file_name]  # add new key-value pair
            else:
                video_file_dict[sub_dir].append(file_name)  # update value
    return video_file_dict

def create_videofiles(video_file_dict):
    """Create folders structures and video files in the project"""
    for 

#! APPLICATION

#* get the path to the diag we care about
root = tk.Tk()
root.withdraw()
diag_path = filedialog.askdirectory()

#* get all the files in this diag
all_files_list = get_files_in_filelist(diag_path)

#* get only the video files in the file list
videofile_list = get_videofiles(all_files_list)

for key, val in videofile_list.items():
    print(key)
    print(val)
exit()

# # this will open up the project
#
# subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
#                 "D:\\d3 Projects\\python_test\\python_test.d3"])
