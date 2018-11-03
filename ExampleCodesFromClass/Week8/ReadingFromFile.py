def readWholeFile(path):
    content = open(path).read()
    return len(content) #This returns number of characters in the file!

def readLineByLine(path):
    handle = open(path)
    linecount = 0
    for line in handle:
        linecount = linecount +1
    handle.close()
    return linecount #This returns number of lines in the file.

def main():
    file_path = input("Enter the path to a file: ")
    print("Number of characters: " + str(readWholeFile(file_path)))
    print("Number of lines: " + str(readLineByLine(file_path)))

if __name__ == "__main__":
    main()
