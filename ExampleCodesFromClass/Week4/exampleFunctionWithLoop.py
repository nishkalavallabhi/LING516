def someFunction(number):
    result = 1
    i = 1
    while i<=number:
        result = result*i
        i = i+1
    return result
print(someFunction(5))
