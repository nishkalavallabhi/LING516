def ctof(number):
   temp = (number*9/5) +32
   return temp

def ftoc(number):
   temp = (number-32)*5/9
   return temp

#Program to convert temparature between Celsius and Fahrenheit scales, with exception handling.
scale=input("Choose a temparature scale - C for Celsius or F for Fahrenheit: ")
if scale == "C" or scale =="F":
    temparature=input("What is the temparature at your place today in " + scale + " scale? ")
    try:
        tempNumber = float(temparature)
        if scale == "C":
           print(ctof(tempNumber))

        else:
           print(ftoc(tempNumber))

    except:
        print("Enter a valid number for temparature!")
else:
    print("Please choose either a C or an F")


