import subprocess


def d3_call(program, project):
    subprocess.run(program, project)

    if __name__ == '__main__':
        subprocess.run(["C:\\Program Files\\d3 Production Suite\\build\\msvc\\d3.exe",
                        "D:\\d3 Projects\\python_test\\python_test.d3"])
