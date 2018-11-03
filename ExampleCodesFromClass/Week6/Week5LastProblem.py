#Not doing any exception handling in this example.

str = input("Please enter a string which has two words seperated by a space: ")
index = str.find(" ")
str1 = str[0:index]
str2 = str[index+1:]
print(str2 + " " + str1)