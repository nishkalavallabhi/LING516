import os

file_path = input("Enter the path to a file: ")
writeHandle = open(file_path, "w")
for i in range(0,10):
    writeHandle.write("line" + str(i) + " is rewritten\n")
writeHandle.close()
