

def sq(n):
    return n*n, n*n*n

def sq2(n):
    print(n*n)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(sq(num1))
print(sq(num2))
print(sq(num1)+sq(num2))
print(sq(num1)[0] +sq(num2)[0])
print(sq(num1)[1] + sq(num2)[1])
