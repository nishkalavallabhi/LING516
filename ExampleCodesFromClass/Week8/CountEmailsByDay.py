#Exercise 2 from Textbook chapter on dictionaries.

filecontent = open('mbox-short.txt')
requiredDict = dict()
for line in filecontent:
    if line.startswith("From "):
        strings = line.strip().split(" ")
        if len(strings) > 2:
            day = strings[2]
            if day in requiredDict.keys():
                requiredDict[day] = requiredDict[day] +1
            else:
                requiredDict[day] = 1
print(requiredDict)

#a more readable way of printing. Also shows how to loop through dictionaries
for key in requiredDict.keys():
    print(key + " " + str(requiredDict[key]))

#print in alphabetical order. Example of sorting the dictionary by key.
'''sorted(requiredDict.keys())
for key in requiredDict.keys():
    print(key + " " + str(requiredDict[key]))'''


