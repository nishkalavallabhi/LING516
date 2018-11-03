while True:
    line = input("Enter something: ")
    if line == "pass":
        print("I am passing without printing what you entered")
        continue
    elif line == "done":
        print("I am stopping the program.")
        break
    else:
        print(line)
print("Done!")
