def countOccurrences(a,b):
   count = 0
   ind=a.find(b)
   while ind>=0:
    a=a[ind+1:]
    ind=a.find(b)
    count=count+1
   #write your code here.

   return count

def main():
   main_string = input("Enter a string: ")
   sub_string = input("Enter the substring: ")
   print("The number of times second string appeared in first string is: ", str(countOccurrences(main_string,sub_string)))

if __name__=="__main__":
   main()
