import re, string

def do_tokenize(someString):
   pattern = "[" + string.punctuation + "]"
   allOccurences = re.findall(pattern, someString)
   print("These are the locations of tokenization in this sentence: ", allOccurences) #Just for checking.
   for i in range(0,len(allOccurences)):
       someString = someString.replace(allOccurences[i], " " +
                                       allOccurences[i] +" ")
       someString = re.sub(r"\s+","\n",someString)
   return someString

print(do_tokenize("I know this, and that."))
