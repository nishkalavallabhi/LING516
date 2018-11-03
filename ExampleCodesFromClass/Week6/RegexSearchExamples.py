import re
filecontent = open('mbox.txt') #This line opens a file called mbox.txt for reading.
for line in filecontent: #This loop reads a file line by line.
    line = line.rstrip() #What is this doing?

    '''#Example 1: search for a normal string. We can use normal find() method of a string too!
    if re.search('localhost', line):
        print(line) #This prints all lines which has "from nakamura" somewhere.'''

    '''#Example 2: search for a string that starts with x. We can use startsWith() instead of this!
    if re.search('^X', line):
        print(line) #This prints all lines that start with X'''

    #Example 3: Here is where regular expression search is really useful.
    if re.search('[0-9]+\sDec\s2007',line):
        print(line)