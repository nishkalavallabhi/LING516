
"""
Question: Let us say I am developing a small web-application which collects data
from students. I ask students two questions - a) Enter a number, b)
Enter another number. Once the students enter two numbers, I will
show them the sum of these two numbers. Now, you all know how
students are. They don’t always read instructions properly, and even
if they read, there are those mischevious people. Write an algorithm
or draw a flowchart to explain how do you make sure you ensure they
entered only numbers, not names or something.
"""

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

#Write your logic to test whether num1 and num2 are numbers below:
is_num1_numeric = 
is_num2_numeric = 

if is_num1_numeric and is_num2_numeric:
   #write a line to print the sum of num1 and num2. Note: confirm your data types.


"""
Hints:
1. isnumeric() is a function used with strings to check if that string has numbers.
"a".isnumeric() will return false, but "1".isnumeric() will return true. You can try playing with this on Python console.

2. int(something) tries to convert that "something" into an integer, if it is possible.
int("a") will throw an error, but int("1") will convert the string 1 into an integer 1. 
"""
