fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if '@uct.ac.za' in line:
        print(line)
