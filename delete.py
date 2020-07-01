import os

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if os.path.getsize(os.path.abspath(filename)) > 2**20:
            os.unlink(filename)
            print(os.path.abspath(filename))