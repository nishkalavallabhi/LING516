import re
while True:
    try:
            word= str(input("please enter a word: "))
            if  word.isalpha():
                if re.search("\w+(s|x|z)", word):
                 word = word+"es"

                elif re.search("\w+(b|c|d|f|g|h|j|k|l|m|n|p|q|r|t|s|v|w|x|y|z)y", word):
                    word = word[0:-1] + "ies"

                elif re.search("\w+(a|e|o|u|i)y", word):
                    word = word + "s"

                else:
                     word = word +"s"
                print (word)

            else:
                print("the input is not valid")

    except:
        print( "please enter a word: ")
        continue
