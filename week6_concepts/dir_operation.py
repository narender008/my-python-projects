import os
import datetime

## making and checking directories
# listing = os.getcwd()
# list = os.listdir(listing)
# list.sort()
# for dir in list:
#     print(dir)
# os.mkdir("week7_csv_manipulation")


## listing pwd and changing it to something else

# print(os.getcwd())
# os.chdir("../../")
# print(os.getcwd())


##  checking content in the directory if they are dir or not

# print(os.getcwd())
list = os.listdir(os.getcwd())
list.sort()
for dir in list:
    if os.path.isdir(dir) == True:
        print(f"{dir} is the directory")
    else:
        print(f"{dir} is not a directory")
