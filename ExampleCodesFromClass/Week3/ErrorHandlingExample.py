try:
    number = input("Enter a number: ")
    next_number = int(number)+1
    print(int(number)/next_number)
except Exception as e:
    print(e)
