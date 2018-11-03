import textwrap #new module usage.

string = input("Enter a paragraph of text:\n")
splitString = string.split(" ")
varN = 5
result = ""
for i in range(0,len(splitString)):
    if i == varN and varN < len(splitString):
        result = result + " " + "____"
        varN = varN +5
    else:
        result = result + " " + splitString[i]

#Question: What does result have now?

#How should I print this neatly??
#Answer: Using textwrap module to 
wrappedResult = textwrap.wrap(result,width=80)

for string in wrappedResult:
    print(string)
