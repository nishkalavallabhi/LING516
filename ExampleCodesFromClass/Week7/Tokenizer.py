#Simple tokenizer. Inserts a whitespace wherever it sees a punctuation marker.
#What this code does not cover? Handling stuff like abbreviations for example.

import re
import string

def tokenize(someString):
   pattern = '[-,;?!:.\"]' #What is this ugly looking pattern doing?
   allOccurences = re.findall(pattern, someString)
   print("These are the locations of tokenization in this sentence: ",
         allOccurences) #Just for checking.
   for i in range(0,len(allOccurences)):
       someString = someString.replace(allOccurences[i], " " +
                                       allOccurences[i] +" ")
       #What is happening here?
       someString = re.sub(r"\s+"," ",someString)
   return someString

def senSplit(someString):
    pattern = "(?<![A-Z][a-z])[.?!]\s[A-Z]"
    allOccurences = re.findall(pattern, someString)
    for i in range(0,len(allOccurences)):
       someString = someString.replace(allOccurences[i], allOccurences[i].replace(" ","\n"))
    return someString

def main():
   str = input("Enter a string to be tokenized in the next line:\n")
   #print("Your tokenized string is: " + tokenize(str))
   print(senSplit(str))

if __name__ == "__main__":
    main()

''' An alternate way of defining a pattern ..which covers all punctuation markers and is better than what I showed!
pattern = "[" + string.punctuation + "]"
print(pattern)'''
