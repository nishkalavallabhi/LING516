
stringInput = input("Enter a string: ")
charInput  = input("Enter a char: ")

def countChar(someString, someChar):
   count = 0
   for anyChar in someString:
       if anyChar == someChar:
           count = count+1
           print(anyChar, str(count))

   return count


print("The number of times ", charInput, "occured in", stringInput,
    "is",countChar(stringInput,charInput))
