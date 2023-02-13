import os
import tkinter as tk
import ffmpeg
from tkinter import filedialog
from PIL import Image
import math
# from random import randrange
# import subprocess

# FUNCTIONS


def get_files_in_filelist(diag_path):  # lists all files in a given diag
    """Read and print all the files name in the filelist.txt file"""
    filelist_path = os.path.join(diag_path, "filelist.txt")  # make the path to filelist.txt in the path
    if os.path.isfile(filelist_path):  # check the file exists
        with open(filelist_path, 'rb') as file_in:  # open filelist.txt
            in_lines = file_in.readlines()  # read all lines
            return in_lines  # return all the lines
    else:
        print("not found")
        return []


def get_videofiles(all_files_list):
    """Read and get all the files name from VideoFiles folder from the list"""
    video_file_dict = {}  # make an empty dict to hold path-file names
    for file in all_files_list:  # go through all the files looking for video files
        if b'objects\\VideoFile' and b'.mov' in file and b'internal' not in file and b'videoin' not in file:
            # is this a video file?
            decoded_path = file.decode()  # decode to a string
            decoded_path = decoded_path.replace(decoded_path.split('\t')[-1], '')  # remove size
            decoded_path = decoded_path.replace('\t', '')  # remove whitespace
            sub_dir, file_name = os.path.split(decoded_path)  # split into path-file name
            if sub_dir not in video_file_dict:
                video_file_dict[sub_dir] = [file_name]  # add new key-value pair
            else:
                video_file_dict[sub_dir].append(file_name)  # update value
    return video_file_dict


def create_folders(video_file_dict):
    """Create folders structures and video files in the project"""
    for key, val in video_file_dict.items():
        path = os.path.join(diag_path, key)
        if not os.path.exists(path):
            os.mkdir(path)
        for file in val:
            file_name, file_ext = os.path.splitext(file)
            video_path = os.path.join(path, f"{file_name}.mov")
            if not os.path.isfile(video_path):
                generate_video(video_path)


def generate_video(video_path):
    # print(f"diag_path = {diag_path}") # only for debugging
    width = 1920
    height = 1080
    duration = 10  # duration of the video in seconds
    fps = 30  # frames per second
    num_frames = duration * fps
    out = (
        ffmpeg.input('pipe:', format='rawvideo', pix_fmt='rgb24', s=f"{width}x{height}", r=fps)
        .output(video_path, vcodec='hap', pix_fmt='rgba', preset='fast', format='mov')
    )
    process = out.run_async(pipe_stdin=True)
    for i in range(num_frames):
        t = i / fps  # time in seconds
        r = int(255 * math.sin(2 * math.pi * t / duration))  # red channel value
        g = int(255 * math.sin(4 * math.pi * t / duration))  # green channel value
        b = int(255 * math.sin(6 * math.pi * t / duration))  # blue channel value
        color = (r, g, b)
        img = Image.new(mode="RGB", size=(width, height), color=color)
        process.stdin.write(img.tobytes())
    process.stdin.close()
    process.wait()


# APPLICATION

# get the path to the diag we care about
root = tk.Tk()
root.withdraw()
diag_path = filedialog.askdirectory()

# get all the files in this diag
all_files_list = get_files_in_filelist(diag_path)

# get only the video files in the file list
videofile_list = get_videofiles(all_files_list)

create_folders(videofile_list)
exit()

# # this will open up the project
#
# subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
#                 "D:\\d3 Projects\\python_test\\python_test.d3"])
