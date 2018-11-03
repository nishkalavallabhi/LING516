def factorial(n):
   fact = 1
   for i in range(1,n+1): #why not start at 0??
      fact = fact*i
   return fact


n = int(input("Enter some number: "))
print(factorial(n))

if __name__ == "__main__":
    main()
