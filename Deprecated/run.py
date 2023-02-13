import os
import tkinter as tk
from tkinter import filedialog
# import pathlib
# import subprocess
# from sys import prefix
# from setuptools import extension
# from typing import List, Any

#! FUNCTIONS

# TODO: OPTIMIZE THE NEXT THREE FUNCTIONS INTO A SINGLE ONE?

#* lists all files in a given diag
def get_files_in_filelist(diag_path):
    """Read and print all the files name in the filelist.txt file"""
    #* make the path to filelist.txt in the path
    filelist_path = os.path.join(diag_path, "filelist.txt")
    #* check the file exists
    if os.path.isfile(filelist_path):
        #* open filelist.txt
        with open(filelist_path, 'rb') as file_in:
            #* read all lines
            in_lines = file_in.readlines()
            #* return all the lines
            return in_lines
    else:
        print("not found")
        return []

def get_videofiles(all_files_list):
    """Read and get all the files name from VideoFiles folder from the list"""
    #* make an empty list to hold the video files i found
    videofile_list = []
    #* go through all the files looking for video files
    for file in all_files_list:
        #* is this a video file?
        if b'objects\\VideoFile' in file:
            #* yes! add it to the list
            videofile_list.append(file)
    #* now we checked all files, return the list of found video files
    return videofile_list

def get_mov_from_videofiles(videofile_list):
    """Read and get mov files from the file list, putting them in a list"""
    #* make an empty list to hold the mov files i found
    mov_list = []
    #* go through all the files looking for mov files
    for file in videofile_list:
        #* is this a mov file?
        if b'.mov' in file:
            #* yes! add it to the list
            mov_list.append(file)
    #* now we checked all files, return the list of found video files
    return mov_list

def clean_mov(mov_list):
    """Cleans the mov files names from useless text and characters"""
    #* make a list of the mov files cleaned
    clean_list = []
    #* go through all the lines in mov_list
    for file in mov_list:
        #* it starts with internal?
        if b'internal' not in file:
            #* decode from bytes to string using a variable called field
            field = file.decode()
            #replace the objects\\videofile\\ from the line with an empty char
            #field = field.replace("objects\\VideoFile\\", "")
            #* remove whatever is after the final \
            field = field.replace(field.split("\t")[-1], "")
            field = field.replace("\t", "")
            #* add the result to the list
            clean_list.append(field)
    #* return the list
    return clean_list

def splitter(clean_list):
    """Split and list the folder paths in different list"""
    #* make a dictionary with folder path as keys (var 0) and (var 1) as filename
    folders_path = {}
    #* go through all the lines in clean_list
    for line in clean_list:
        #* split lines in folder paths
        var = os.path.split(line)
        #* create two variables for key and filenames
        var[0], var[1]
        #* look for keys in the paths
        if var[0] in folders_path:
            folders_path[var[0]]

#! APPLICATION

#* get the path to the diag we care about
root = tk.Tk()
root.withdraw()
diag_path = filedialog.askdirectory()

#* get all the files in this diag
all_files_list = get_files_in_filelist(diag_path)

#* get only the video files in the file list
videofile_list = get_videofiles(all_files_list)

#* now get only the mov videofiles
mov_list = get_mov_from_videofiles(videofile_list)

#* clean the file from the rubbish
clean_list = clean_mov(mov_list)

splitter(clean_list)
exit()

#* create the lists of the folders/subfolders/files

#! TESTING OUT WITH PRINT

# for debugging, we'll list all the files in the diag filelist.txt
file_list.file_list()

# # this will open up the project
#
# subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
#                 "D:\\d3 Projects\\python_test\\python_test.d3"])