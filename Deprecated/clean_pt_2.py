def clean_pt2(file_in, file_out):

    # this will clean videofile in the txt from shit part 2

    with open(file_in, "r+") as f:
        lines = f.readlines()

        with open(file_out, "w+") as new_f:
            for line in lines:
                if not line.startswith("internal"):
                    new_f.write(line)


if __name__ == "__main__":
    clean_pt2(file_in="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\02_First_Cleaning.txt",
              file_out="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt")
