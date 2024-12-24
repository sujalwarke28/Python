'''Write a python program to print the contents of a directory using the os module
 Search online for the function which does that.'''

import os

directory_path = "/usr/local/bin"

try:
    contents = os.listdir(directory_path)
    print("Contents of directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
