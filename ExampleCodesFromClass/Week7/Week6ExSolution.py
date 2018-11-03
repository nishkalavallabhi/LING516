
def main():
  mesg = "Enter a bunch of numbers separated by space: "
  try:
    inp = input(mesg)
    nums_strings = inp.split(" ")
    nums_ints = []
    for num in nums_strings:
       nums_ints.append(int(num))

    #Other way to write all the 5 lines above in 1 line: 
    #nums_ints = [int(num) for num in input(mesg).split(" ")]

    print("Maximum: ", str(max(nums_ints)))
    print("Minimum: ", str(min(nums_ints)))
    
  except:
    print("Something went wrong. You perhaps did not enter all integers")
      

if __name__ == "__main__":
   main()
