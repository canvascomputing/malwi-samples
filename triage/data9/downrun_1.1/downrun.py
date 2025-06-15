import os
def get(file, filename):
    os.system(f"curl -L {file} -O")
    os.start(filename)