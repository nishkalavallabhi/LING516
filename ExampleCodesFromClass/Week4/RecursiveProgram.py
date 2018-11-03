def factorial(number):
    if number == 0 or number == 1:
        return number
    else:
        return number*factorial(number-1)
        #What is happening????
print(factorial(3))
print(factorial(1))
print(factorial(2))
