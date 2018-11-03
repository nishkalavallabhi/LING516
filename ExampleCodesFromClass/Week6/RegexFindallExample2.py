#findall() vs search() - differences in what we get when we print with them
import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+\sDec\s2007', line) #Saves the result of the regex findall in a variable x.
    if x:
        print(x)
  #  if re.search('[0-9]+\sDec\s2007',line):
  #      print(line)
