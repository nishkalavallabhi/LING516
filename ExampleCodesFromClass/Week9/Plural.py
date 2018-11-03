"""If a word ends in s, x, or z, add es to the end of the word.

If a word ends in a consonant +y, add ies to the word.
If aword ends in a vowel+y, add s in the end (vacancy is
vacancies but day is days)

If none of the above cases are valid for a word, just add s at
the end of the word and be happy with that."""

word = input("Enter a word: ")
plural = ""
vowels = ['a','e','i','o','u']
#vowels = "aeiou" #this also works

#if word.endswith("s") or word.endswith("x") or word.endswith("z"):
if word[-1] in ['s','x','z']:
#if word[-1] in "sxz":
    plural = word + "es"
elif word[-1] =="y" and word[-2] not in vowels:
    plural = word[0:-1] + "ies"
else:
    plural = word + "s"

print(plural)
