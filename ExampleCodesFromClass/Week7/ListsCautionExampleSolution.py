fhand = open('mbox-short.txt')
for line in fhand:
 words = line.split()
 try:
    if(len(words) > 1):
        if words[0] != 'From':
            continue
        print(words[2])
 except Exception as err:
    print(err)