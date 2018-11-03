#Taichi's solution

import re

word = input('Enter a word in its singular form: ')
plural = ""

if re.match("\w+(s|x|z)",word):
    plural = word + "es"
elif re.match("\w+(a|e|i|o|u)y", word):
    plural = word + "s"
elif re.match("\w+y", word):
    word_list = list(word)
    word_list[-1] = "i"
    word = "".join(word_list)
    plural = word + "es"
else:
    plural = word + "s"

print(plural)
