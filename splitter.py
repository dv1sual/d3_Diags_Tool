def splitter(file_in, f1, f2, f3):

    with open(file_in, "r+") as g:
        lines = g.readlines()

        x = []
        y = []
        z = []

        for line in lines:
            x.append(line.split('\\')[0] + '\n')
            y.append(line.split('\\')[1] + '\n')
            z.append(line.split('\\')[-1])

        with open(f1, "w+") as f1:
            f1.writelines(x)

        with open(f2, "w+") as f2:
            f2.writelines(y)

        with open(f3, "w+") as f3:
            f3.writelines(z)


if __name__ == "__main__":
    splitter(file_in="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\03_Second_Cleaning.txt",
             f1="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\04_Folder_Main.txt",
             f2="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\05_Folder_Sub.txt",
             f3="C:\\Users\\luca\\Desktop\\d3_Search_Files\\d3_FileMaker\\00_txt_files\\06_File_Names.txt")
