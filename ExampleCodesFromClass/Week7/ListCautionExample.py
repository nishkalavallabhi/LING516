#Identify the problem, and fix it.

fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if words[0] != 'From':
	    continue
    print(words[2])
