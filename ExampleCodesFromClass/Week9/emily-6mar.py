import re

try:
    user_input = str(input("Please enter a word to make it plural: "))
    if user_input.isalpha():
        if re.search("[sxz]$", user_input):
            plural = user_input + "es"
            print(plural)
        elif re.search("[qwrtpsdfghjklzxcvbnm]y$", user_input):
            user_input.split()
            plural = user_input[0:-1] + "ies"
            print(plural)
        else:
            print(user_input + "s")
    else:
        print("Please enter a string.")
except:
    print("There was an error.")
