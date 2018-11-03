def main():
   nums = []
   stop = True
   while stop:
      inp = input("Enter a number: ")
      if inp != "done":
      	try:
            num = int(inp)
            nums.append(num)
      	except:
            print("Excluding this input, as it is not  a number")
      else:
        print("Stopping to take inputs. Here is the output:")
        stop = False
        print("Maximum: ", str(max(nums)))
        print("Minimum: ", str(min(nums)))
        #print(nums) #just to check what is in it
main()
