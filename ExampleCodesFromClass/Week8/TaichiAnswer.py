#Program that creates a dictionary of days in emails starting with 'From'

filecontent = open('mbox-short.txt') #Get a handle of the file
requiredDict = dict() #Create a dictionary which has no keys/values
for line in filecontent:
    if line.startswith("From "):
        strings = line.strip().split(" ") #If a line starts with 'From:', the line is coverted into a list on a word-by-word basis
        day = strings[2] #Assigning the word at the third position (i.e., day) to a variable called day
        if day in requiredDict.keys():
            requiredDict[day] = requiredDict[day] +1 #If the day is already in the dictionary, the frequency increases by one.
        else:
            requiredDict[day] = 1 #If the day is not already in the dictionary, this code creates another key.
print(requiredDict)

filecontent.close()
