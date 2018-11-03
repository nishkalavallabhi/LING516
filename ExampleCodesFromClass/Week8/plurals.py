'''
Code for getting the plural of a word, based on the rules mentioned in the class slides for today.
'''

import re

def plurals_without_regex_1(word):
  if word.endswith("s") or word.endswith("x") or word.endswith("z"):
     word = word + "es"
  elif word.endswith("y"):
     if word[-2] in "aeiou":
        word = word + "s"
     else:
        word = word[0:len(word)-1] + "ies"
  else:
     word = word + "s"
  return word

def plurals_without_regex_2(string):
  vowels = "aeiou"
  lastLetter = string[len(string)-1]
  penultimate = string[len(string)-2]
  if lastLetter == "s" or lastLetter == "x" or lastLetter == "z":
      return string + "es"
  elif lastLetter == "y":
      if penultimate in vowels:
          return string + "s"
      else:
          return string.replace(lastLetter,"ies")
  else:
      return string + "s"

def plurals_with_regex(string):
    pattern1 = "[sxz]$"
    pattern2 = "[^aeiou]y$"
    if re.search(pattern1,string):
        return string+"es"
    elif re.search(pattern2,string):
        return string[0:len(string)-1] + "ies"
    else:
        return string + "s"

def main():
   while True:
     user_input = input("Enter a word that needs to be pluralized. To exit, type the word whatever: ")
     if user_input == "whatever":
        print("bye")
        break
     if not user_input.isalpha():
        print("When I said enter a word, I meant a real word!")
     else:
       # print(pluralize(user_input.lower()))
        print(plurals_with_regex(user_input.lower()))
if __name__ == "__main__":
    main()

