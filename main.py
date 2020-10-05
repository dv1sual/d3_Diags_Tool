import subprocess
import file_list
import video_file
import mov
import clean_pt_1
import clean_pt_2
import splitter
import folder_duplicates
import sub_folders_dup
import bad_words
import copy_default
import create_content

# this will check for the file list file in the d3 folder and print the filelist.txt file

file_list.file_list()

# this will filter only the VideoFile

in_path = "D:\\d3 Projects\\python_test\\filelist.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\00_VideoFile_Folder.txt"

video_file.video_file(input_file=in_path, output_file=out_path)

# this will filter only the mov files

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\00_VideoFile_Folder.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\01_Only_Mov.txt"

mov.mov(input_file=in_path, output_file=out_path)

# this will clean videofile in the txt from shit

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\01_Only_Mov.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\02_First_Cleaning.txt"

clean_pt_1.clean_pt1(file_in=in_path, file_out=out_path)

# this will clean videofile in the txt from shit part 2

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\02_First_Cleaning.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt"

clean_pt_2.clean_pt2(file_in=in_path, file_out=out_path)

# this will isolate the folder names / sub-folders and the video files

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt"
out_path_1 = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\04_Folder_Main.txt"
out_path_2 = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\05_Folder_Sub.txt"
out_path_3 = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\06_File_Names.txt"

splitter.splitter(file_in=in_path, f1=out_path_1, f2=out_path_2, f3=out_path_3)

#  This will remove duplicates folder from the file

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\04_Folder_Main.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\07_Folder_Final.txt"

folder_duplicates.folder_duplicates(file_in=in_path, file_out=out_path)

# This will remove duplicates folder from sub folders

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\05_Folder_Sub.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt"

sub_folders_dup.sub_folders_dup(file_in=in_path, file_out=out_path)

# This will remove shits from the sub-folder

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt"
out_path = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\09_Sub_Final.txt"

bad_words.bad_words(file_in=in_path, file_out=out_path)

# this will copy the missing sample folder in the project

in_path = "C:\\Users\\luca\\Desktop\\d3_Search_files\\01_Content_Replace_Default"
out_path = "D:\\d3 Projects\\python_test\\objects"

copy_default.copy_default(src=in_path, dest=out_path)

# This will look on the cleaned txt, and it will create folder, sub folders and files in the specified directory

txt_file = "C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt"
source_folder = "C:\\Users\\luca\Desktop\\d3_Search_Files\\d3_FileMaker\\02_Content_Replace\\mov"
dest_folder = "D:\\d3 Projects\\python_test\\objects\\VideoFile"

create_content.content(txt_file=txt_file, source_folder=source_folder, dest_folder=dest_folder)

# this will open up the project

subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
                "D:\\d3 Projects\\python_test\\python_test.d3"])
