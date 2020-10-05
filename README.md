# d3_Diags_Tool

 A d3 Tool for Project Diagnostics.
 
 All the script works out of the main.py - the rest are all the functions used in it.
 At the present moment, you need to manually change all your directories in order to get it work.
 
 Soon there will be the how-to guide.

01_file_list.py [function]

This will check for the filelist file in the d3 project folder and print it
on a txt file

02_video_file.py [function]

This will filter only the video file folder from that txt file
 and print the results in another txt file

03_mov.py [function]

This will filter only the mov files on that txt, and print the results on a
txt file

04_clean_pt_1.py [function]

This will clean the resulting txt from useless data and print the results on a
txt file

05_clean_pt_2.py [function]

This will clean the resulting txt from useless data and print the results on a
txt file

06_splitter.py [function]

This will split the resulting txt in folder/subfolder/files in three different
txt file

07_folder_duplicates.py [function]

This will remove the folder duplicates from the resulting txt and print it on a
txt file

08_sub_folder_dup.py [function]

This will remove the sub folder duplicates from the resulting txt and print it
on a txt file

09_copy_default.py [function]

This will copy the default content from a folder to the project folder in d3

10_create_content.py [function]

This will take the 05_clean_pt_2 file and it will create the full path with
content into the d3 project folder

11_d3_call [function]

This will open the d3 project
