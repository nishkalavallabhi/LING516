str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
temp = int(len(str1)/2)
if str1 == str2[::-1]:
  print(str1[0:temp]+str2[temp:])
else:
  print(str2[0:temp] + str1[temp:])
