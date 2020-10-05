def bad_words(file_in, file_out):

    bad_word = ['.mov']

    with open(file_in, "r+") as in_file:
        in_file = in_file.readlines()

        with open(file_out, "w+") as out_file:
            for line in in_file:

                if not line.strip():
                    continue  # skip the empty line
                if not any(bad_word in line for bad_word in bad_word):
                    out_file.write(line)


if __name__ == "__main__":
    bad_words(
        file_in="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\08_Sub_First.txt",
        file_out="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\09_Sub_Final.txt")
