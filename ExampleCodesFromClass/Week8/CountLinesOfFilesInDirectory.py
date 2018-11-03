#Purpose: To show how to list files in a directory.

import os

def countLines(filePath):
    fhand = open(filePath)
    count = 0
    for line in fhand:
        count = count + 1
    return str(count)

def main():
    path = input("Enter a file path: ")
    if os.path.isdir(path): #What is this line doing?
        print("You entered a directory path")
        print(os.listdir(path)) #What is this doing?
        print("Here are all the .py files in this directory and"
              "their line counts:")
        for filepath in os.listdir(path): #and this?
            if filepath.endswith(".py"):
                fullPath = path + "/" + filepath
                print(fullPath)
                count = countLines(fullPath)
                print("Number of lines in: " + filepath + " is " +
                      count)
    else:
        print("Please enter a directory path")

if __name__ == "__main__":
    main()