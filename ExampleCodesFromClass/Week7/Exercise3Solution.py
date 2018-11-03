

myfile = open('mbox-short.txt')
mydict = {}
for line in myfile:
    if line.startswith("From"):
        email = line.split(" ")[1].strip()
        if email in mydict:
            temp_count = mydict[email]
            mydict[email] = temp_count+1
        else:
            mydict[email] = 1
myfile.close()
for key in mydict.keys():
    print(key, mydict[key])
