#Purpose: To show how to list files in a directory.

import os

def countLines(filePath):
    fhand = open(filePath)
    count = 0
    for line in fhand:
        count = count + 1
    return count

def main():
    path = input("Enter a file path: ")
    total = 0
    if os.path.isdir(path): #What is this line doing?
        print("You entered a directory path")
        print("Reading this file: ", os.listdir(path)) #What is this doing?
        print("Here are all the .py files in this directory and"
              "their line counts:")
        for filepath in os.listdir(path): #and this?
            if filepath.endswith(".py"):
                fullPath = path + "/" + filepath
                print(fullPath)
                count = countLines(fullPath)
                print("Number of lines in: " + filepath + " is " + str(count))
                total = total + count
            else:
                print("I am not reading this file. ", filepath)
        print("In total, I read: ", str(total), " lines from all files in this folder")
    else:
        print("Please enter a directory path")

if __name__ == "__main__":
    main()


"""
Things you can do: How do I keep reading all directories, sub-directories etc recursively?
i.e., if I get a path, I should read all files in that folder path, and check if there are any
sub-folders within this, then go that sub-folder and read all files, and so on.
"""
