#Example to show how to check if a file exists in the given path.

import os #Note the new module usage

file_path = input("Enter the path to a file: ")
if os.path.isfile(file_path):
    print("This file really exists. You can read or do whatever.")
else:
    print("This file does not exist. You can create one if you want.")