string = input("Enter a paragraph of text:\n")
splitString = string.split(" ")
varN = 5
result = ""
for loopvar in range(0,len(splitString)):
    if loopvar == varN and varN < len(splitString):
        result = result + " " + "____"
        varN = varN +5
    else:
        result = result + " " + splitString[loopvar]
#Question: What does result have now?
print(result)
