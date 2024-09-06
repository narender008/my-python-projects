import os
import datetime

# create a file if it does not exist, otherwise append to the end of existing file
if os.path.exists("week6_concepts/example.txt"):
    with open("example.txt", "a") as file:
        file.write("this is new line in exist file")
else:
    with open("week6_concepts/example.txt", "w") as file:
        file.write("this is newly created file with open file.")

# read the content of the file
with open("week6_concepts/example.txt") as file:
    print(file.read())

# get the last access time of the file
timestamp = os.path.getatime("week6_concepts/example.txt")
changed_format = datetime.datetime.fromtimestamp(timestamp)
print(f"file change timestamp is {changed_format}")

# get the absolute path of the file
# file_location = os.path.abspath("example.txt")
# print(file_location)

# delete the file
# os.remove("example.txt")
