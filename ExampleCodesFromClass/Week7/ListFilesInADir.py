import os

folder = input("Enter a folder path: ")
#files_in_this_folder = os.listdir(folder)
print(os.path.isdir(folder))
print(os.path.isfile(folder))
