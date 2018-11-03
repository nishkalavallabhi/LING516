n = int(input("Enter the number of numbers you want to enter: "))
sum = 0
i = 1
while i <=n :
    current = int(input("Enter a number: "))
    sum = sum + current
    i = i+1
    print(sum,i)

print("The sum of these numbers is: ", str(sum))
print("The average of these numbers is: ", str(sum/n))
