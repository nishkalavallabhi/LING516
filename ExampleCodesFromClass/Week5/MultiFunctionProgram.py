import random,math

def OddEven(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

"""
Log10 of 0 is undefined. Should I be worried?
"""
def LogNum(n):
    return math.log10(n)

def RandNum(n):
    return random.randint(0,n)

def main():
    try:
        number = int(input("Enter a positive whole number: "))
        if number <= 0:
            print("Enter a positive whole number!")
        else:
            print("The number is: ", OddEven(number))
            print("Log of the number is: ", str(LogNum(number)))
            print("Random number between 0 and this number is: ", str(RandNum(number)))

    except:
        print("Something went wrong, and I don't care about giving explicit information!")

if __name__ == "__main__":
    main()

"""
Ideally, if you intend to use these functions beyond this program, by importing this into other programs,
you should have these try except blocks in all functions, not just the main function.
or, you should put those checks before the functions are called in other programs
"""
