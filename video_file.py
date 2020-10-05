def video_file(input_file, output_file):

    # this will filter only the VideoFile Folder Content

    with open(input_file, 'rb') as file_in:
        in_lines = file_in.readlines()

        with open(output_file, "wb") as file_out:

            for line in in_lines:
                if b'VideoFile' in line:
                    file_out.write(line)


if __name__ == "__main__":
    video_file(input_file="D:\\d3 Projects\\python_test\\filelist.txt",
               output_file="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files"
                           "\\00_VideoFile_Folder.txt")
