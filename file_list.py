import os


# this will check for the file list file in the d3 folder

def file_list():
    for f_name in os.listdir('D:\\d3 Projects\\python_test'):

        if f_name.endswith('.txt'):
            print(f_name)

            # this will read and print the filelist.txt file

            myfile = open("D:\\d3 Projects\\python_test\\filelist.txt", "r")
            contents = myfile.read()
            myfile.close()
            print(contents)


if __name__ == "__main__":
    file_list()
