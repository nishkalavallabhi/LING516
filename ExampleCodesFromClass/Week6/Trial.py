hand = open('/home/bangaru/PycharmProjects/Week6/grepProgram.py')
#Now reading the file line by line
for line in hand:
    if line.startswith("i"):
        print(line)

