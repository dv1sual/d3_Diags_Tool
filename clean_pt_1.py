def clean_pt1(file_in, file_out):
    prefix = "objects\\VideoFile\\"
    extension = ".mov"
    print('prefix', prefix)
    print('extension', extension)

    # this will clean videofile in the txt from shit

    with open(file_in, 'r+') as file_in:
        with open(file_out, 'w+') as file_out:
            for line in file_in:
                new_line = line.replace(prefix, '').split(extension)[0] + extension
                file_out.write(new_line + '\n')
                print('--> Line\n', type(line), line)
                print('--> New Line\n', type(new_line), new_line)


if __name__ == "__main__":
    clean_pt1(file_in="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\01_Only_Mov.txt",
               file_out="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\02_First_Cleaning.txt")
