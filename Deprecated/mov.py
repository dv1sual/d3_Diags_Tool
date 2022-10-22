def mov(input_file, output_file):
    # this will filter only the mov files in the Video File Folder

    with open(input_file, 'r') as file_in:
        in_lines = file_in.readlines()

        with open(output_file, "w") as file_out:

            for line in in_lines:
                if '.mov' in line:
                    file_out.write(line)


if __name__ == "__main__":
    mov(input_file="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\00_VideoFile_Folder.txt",
        output_file="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\01_Only_Mov.txt")
