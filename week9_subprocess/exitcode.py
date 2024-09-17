import os
import sys


filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("this is newly created file and its content")

else:
    print(f" ERROR: file {filename} already exist")
    sys.exit(1)
