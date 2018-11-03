
#Get the information about n:
try:
    n = int(input("Enter the number of numbers you want to enter: "))
    sum = 0
    actual_n = 0
    if n >=2 and n <= 100:
        for i in range(0,n):
            current = input("Enter a number: ")
            if current.isnumeric() and int(current) in range(0,10001):
                sum = sum + int(current)
                actual_n = actual_n + 1
            else:
                print("You did not enter a valid input. I am skipping this input and moving on")
    else:
        print("n is not between 2 and 100. Please try again!")

    print("The sum of the numbers you entered is: ", str(sum))
    print("The average of all the valid numbers you entered is: ", str(sum/actual_n))

except:
    print("n is not an integer. Please try again")
