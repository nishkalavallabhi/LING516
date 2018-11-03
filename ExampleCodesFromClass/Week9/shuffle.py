
import random

given_string = "This is a string I will jumble now"
string_as_list = given_string.split(" ")

#print(string_as_list)

#randomly generates a list without repetitive numbers
lst = random.sample(range(0,len(string_as_list)),len(string_as_list))
#print(lst)

#Jumbling now
string_to_user = ""
for number in lst:
    string_to_user += string_as_list[number] + " "


print("Here is a string: ", string_to_user)

user_input = input("Enter this string in correct order: ")


if user_input == given_string:
    print("You did it!")
else:
    print("Wrong answer!!")



