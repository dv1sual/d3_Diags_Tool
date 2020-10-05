import shutil


def copy_default(src, dest):

    shutil.copytree(src, dest, dirs_exist_ok=True)


if __name__ == "__main__":
    copy_default(src="C:\\Users\\luca\\Desktop\\d3_Search_files\\01_Content_Replace_Default",
                 dest="D:\\d3 Projects\\python_test\\objects")
