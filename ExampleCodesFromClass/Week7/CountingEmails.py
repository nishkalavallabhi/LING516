#Program that creates a dictionary of emails and the number of times messages were sent from that email.
#Using this to demonstrate the use of dictionaries practically.

filecontent = open('mbox-short.txt')
requiredDict = dict()
for line in filecontent:
    if line.startswith("From "):
        strings = line.strip().split(" ")
        email = strings[1]
        if email in requiredDict.keys():
            requiredDict[email] = requiredDict[email] +1
        else:
            requiredDict[email] = 1
print(requiredDict)

#a more readable way of printing. Also shows how to loop through dictionaries
for key in requiredDict.keys():
    print(key + " " + str(requiredDict[key]))

#print in alphabetical order. Example of sorting the dictionary by key.
'''sorted(requiredDict.keys())
for key in requiredDict.keys():
    print(key + " " + str(requiredDict[key]))'''


