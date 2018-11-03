#Textbook example
import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
searchmatch = re.search('\S+@\S+', s)
findallmatch = re.findall('\S+@\S+', s) #This is a "LIST" object
#print(searchmatch)
print(findallmatch[1][4])
#print(findallmatch[0])
