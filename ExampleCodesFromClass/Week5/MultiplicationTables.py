
def printtable(number):
    for i in range(1,11):
        print(str(number), "*", str(i), "=", str(i*number))

def main():
    num = input("Enter a number: ")
    if num.isnumeric():
        num = int(num)
        print("Here is the multiplication table for ", str(num))
        printtable(num)
    else:
        print("Enter a valid number!")

if __name__ == "__main__":
    main()
