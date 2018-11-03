#Program to emulate grep. A question from textbook.
import re
hand = open('mbox.txt')
pattern = input("Enter the pattern you want to see: ") #user enters a pattern
count = 0 #variable to save the the number of times a pattern has occured

#Now reading the file line by line
for line in hand:
    if re.search(pattern,line):
        count = count +1

print("mbox.txt had " + str(count) +" lines that matched " + pattern)