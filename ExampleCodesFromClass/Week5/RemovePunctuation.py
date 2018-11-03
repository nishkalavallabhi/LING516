import string
def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct = s_without_punct + letter
            #print(s_without_punct)
    return s_without_punct

print(remove_punctuation("\"Well, I never did!\", said Alice."))
#print(remove_punctuation("Are you very, very, sure?"))
