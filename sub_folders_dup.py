def sub_folders_dup(file_in, file_out):

    lines_seen = []

    with open(file_in, "r+") as in_file:
        in_file = in_file.readlines()

        with open(file_out, "w+") as out_file:
            for line in in_file:
                print(line)

                if line not in lines_seen:
                    out_file.write(line)
                    lines_seen.append(line)

    for line in lines_seen:
        print(line)


if __name__ == "__main__":
    sub_folders_dup(
        file_in="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\05_Folder_Sub.txt",
        file_out="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt")
