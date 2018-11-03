import os

file_path = input("Enter the path to a file: ")
if os.path.isfile(file_path):
    print("This file already exists. You really should not be doing this. ")
else:
    writeHandle = open(file_path, "w")
    for i in range(0,10):
        writeHandle.write("line" + str(i) + " is written\n")
    writeHandle.close()