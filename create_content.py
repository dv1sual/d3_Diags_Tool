import os
import shutil

global DEBUG
DEBUG = True


def content(txt_file, source_folder, dest_folder):
    if DEBUG:
        print("\n--> content(txt_file, source_folder, dest_folder):")
        print(f"\ttxt_file = {txt_file}")
        print(f"\tsource_folder = {source_folder}")
        print(f"\tdest_folder = {dest_folder}")

    if not source_folder.endswith("\\"):
        source_folder += "\\"

    if not dest_folder.endswith("\\"):
        dest_folder += "\\"

    mov_origin = [source_folder + file for file in os.listdir(source_folder) if file.endswith(".mov")]
    if DEBUG:
        print("\n--> mov_origin:")
        for f in mov_origin:
            print(f"\t{f}")

    with open(txt_file, "r+") as f:
        lines = f.readlines()
    if DEBUG:
        print("\n--> txt_file:")
        for l in lines:
            ret = l.replace("\n", "")
            print(f"\t{ret}")
        print("\n--> target:")

    origin_id = 0
    for line in lines:
        target = dest_folder
        path = line.split("\\")
        for i in range(len(path) - 1):
            target += path[i]
            if not os.path.exists(target):
                os.makedirs(target)
            else:
                pass
            target += "\\"
        target += path[-1].replace("\n", "")
        if DEBUG:
            print(f"\t{target}")
        if origin_id > (len(mov_origin) - 1):
            origin_id = 0
        shutil.copyfile(mov_origin[origin_id], target)
        origin_id += 1


if __name__ == '__main__':
    content(txt_file="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt",
            source_folder=r"C:\Users\luca\Desktop\d3_Search_Files\d3_FileMaker\02_Content_Replace\mov",
            dest_folder="D:\\d3 Projects\\python_test\\objects\\VideoFile")
