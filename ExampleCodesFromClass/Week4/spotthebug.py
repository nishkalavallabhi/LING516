def someFunction(number):
    result = 1
    i = 1
    while i<=number:
        result = result*i
        number = number+1
    return result
print(someFunction(5))
