# import os
import tkinter as tk
from tkinter import filedialog

# this will prompt the user to select the file list file.

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# this will read and print the filelist.txt file


def file_list_v2():
    with open(file_path) as f:
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    file_list_v2()
