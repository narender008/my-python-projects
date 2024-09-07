import os
import datetime

## making and checking directories
listing = os.getcwd()
list = os.listdir(listing)
list.sort()
for dir in list:
    print(dir)
os.mkdir("week7_csv_manipulation")


## listing pwd and changing it to something else

print(os.getcwd())
os.chdir("../../")
print(os.getcwd())


##  checking content in the directory if they are dir or not

print(os.getcwd())
list = os.listdir(os.getcwd())
list.sort()
for dir in list:
    if os.path.isdir(dir) == True:
        print(f"{dir} is the directory")
    else:
        print(f"{dir} is not a directory")


##coursera assignment


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return filesize


print(create_python_script("program.py"))


# The new_directory function creates a new directory inside the current working directory,
# then creates a new empty file inside the new directory, and returns the list of files in that directory.
# Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        print("creating directory")
        os.mkdir(directory)
        os.chdir(directory)
        new_path = os.path.join(os.getcwd(), filename)
        with open(new_path, "w"):
            pass
        return os.listdir(os.getcwd())
    else:
        print(f"directory is already there.")
        return os.listdir(directory)
    # Return the list of files in the new directory


# print(new_directory("PythonPrograms", "script.py"))


# The file_date function creates a new file in the current working directory,
# checks the date that the file was modified, and returns just the date portion
# of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file
# called "newfile.txt" and check the date that it was modified.


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass
    timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    # Convert the timestamp into a readable format, then into a string
    only_date = str(timestamp)
    only_date = only_date[:10]
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return f"date is {only_date}"


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


# The parent_directory function returns the name of the directory
# that's located just above the current working directory. Remember that '..'
# is a relative path alias that means "go up to the parent directory".
# Fill in the gaps to complete this function.


def parent_directory():
    cwd = os.getcwd()
    # of the current working directory
    relative_parent = os.path.join(cwd, "..")

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
