#Code to show how dictionaries work. Observe what different print statements do, after uncommenting
#the statement for which you want to see the output.

egDict = {'Sowmya':{'country':'India', 'education': 'PhD', 'spring courses': [314, 516]},
          'Jordan':{'country':'USA', 'education': 'MA', 'spring courses': [314]},
          'Kim':{'country':'USA', 'education': 'MA', 'spring courses': [250,110]}
          }

#print(egDict['Sowmya']['spring courses'][0])

#Adding new stuff later:
egDict['NewPerson'] = {}
egDict['NewPerson']['country'] = 'Germany'
egDict['NewPerson']['education'] = 'BS'
egDict['spring courses'] = []

#print(egDict['Sowmya'])
print(egDict['NewPerson'])
#print(len(egDict))
#print("In this semester, Sowmya teaches: ", egDict['Sowmya']['spring courses'][0])
#print("In this semester, Jordan teaches: ", egDict['Jordan']['spring courses'])
#print("In this semester, Kim teaches: ", egDict['Kim']['spring courses'])
print("In this semester, new person teaches: ", egDict['NewPerson']['spring courses'])
#Throws an error. Why?

#print(egDict.keys())
#print(egDict.keys()[0]) # this will through an error. What is the error?
#print("Evan" in egDict) #Boolean. Prints true or false

