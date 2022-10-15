import os
import tkinter as tk
from tkinter import filedialog

# import pathlib
# import subprocess
# from sys import prefix
# from setuptools import extension
# from typing import List, Any

import file_list

#* FUNCTIONS

# TODO: OPTIMIZE THE NEXT THREE FUNCTIONS INTO A SINGLE ONE

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
        if b'Object\\VideoFile' in file:
            #* yes! add it to the list
            videofile_list.append(file)
    #* now we checked all files, return the list of found video files
    return videofile_list

def get_mov_from_videofiles(all_files_list):
    """Read and get mov files from the file list, putting them in a list"""
    #* make an empty list to hold the mov files i found
    mov_list = []
    #* go through all the files looking for mov files
    for file in all_files_list:
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
            #* replace the objects\\videofile\\ from the line with an empty char
            field = field.replace("objects\\VideoFile\\", "")
            #* remove whatever is after the final \
            field = field.replace(field.split("\t")[-1], "")
            field = field.replace("\t", "")
            #* add the result to the list
            clean_list.append(field)
    #* return the list
    return clean_list

def splitter(clean_list):
    # make a list for every piece of the path
    count = {}
    x = []
    y = []
    z = []
    new_x_list = []
    new_z_list = []
    # go through all the lines in clean_list
    for line in clean_list:
        # remove videoin file from the list
        if 'videoin' not in line:
            if line in count:
                count[line]
            # add to the x list the main folder
            x.append(line.split('\\')[0] + '\n')
            # add to the y list the second
            # y.append(line.split('\\')[1] + '\n')
            # add to the z list the third or last
            z.append(line.split('\\')[-1])
        # this will clean all the duplicates in the x list
        for a in x:
            if a not in new_x_list:
                new_x_list.append(a)
        # this will clean all the duplicates in the z list
        for b in z:
            if b not in new_z_list:
                new_z_list.append(b)

    # return the lists
    return new_x_list

# APPLICATION

#* get the path to the diag we care about
root = tk.Tk()
root.withdraw()
diag_path = filedialog.askdirectory()

#* get all the files in this diag
all_files_list = get_files_in_filelist(diag_path)

#* get only the video files in the file list
videofile_list = get_videofiles(all_files_list)

#* now get only the mov videofiles
mov_list = get_mov_from_videofiles(all_files_list)

#* clean the file from the rubbish
clean_list = clean_mov(mov_list)

#* create the lists of the folders/subfolders/files
new_x_list = splitter(clean_list)
z = splitter(clean_list)

# TESTING OUT WITH PRINT

print(new_x_list)
# print(z)

quit()

# for debugging, we'll list all the files in the diag filelist.txt
file_list.file_list()

#
# # This will remove duplicates folder from sub folders
#
# in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\05_Folder_Sub.txt"
# out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt"
#
# sub_folders_dup.sub_folders_dup(file_in=in_path, file_out=out_path)
#
# # This will remove shits from the sub-folder
#
# in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt"
# out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\09_Sub_Final.txt"
#
# bad_words.bad_words(file_in=in_path, file_out=out_path)
#
# # this will copy the missing sample folder in the project
#
# in_path = "C:\\Users\\luca\\Desktop\\d3_Search_files\\01_Content_Replace_Default"
# out_path = "D:\\d3 Projects\\python_test\\objects"
#
# copy_default.copy_default(src=in_path, dest=out_path)
#
# # This will look on the cleaned txt, and it will create folder, sub folders and files in the specified directory
#
# txt_file = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt"
# source_folder = "C:\\Users\\luca\Desktop\\d3_Search_Files\\d3_FileMaker\\02_Content_Replace\\mov"
# dest_folder = "D:\\d3 Projects\\python_test\\objects\\VideoFile"
#
# create_content.content(txt_file=txt_file, source_folder=source_folder, dest_folder=dest_folder)
#
# # this will open up the project
#
# subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
#                 "D:\\d3 Projects\\python_test\\python_test.d3"])
