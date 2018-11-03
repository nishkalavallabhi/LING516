
def ctof(number):
  return (number*9/5)+32

def ftoc(number):
  return (number-32)*(5/9)

#Program to convert temparature between Celsius and Fahrenheit scales, with exception handling.
scale=input("Choose a temparature scale - C for Celsius or F for Fahrenheit: ")
if scale == "C" or scale =="F":
    temparature=input("What is the temparature at your place today in " + scale + " scale? ")
    try:
        tempNumber = float(temparature)
        if scale == "C":
            result = ctof(tempNumber)
            print("The Fahrenheit equivalent of your Celsius temparature is: " + str(result))

        elif scale == "F":
            result = ctof(tempNumber)
            print("The Fahrenheit equivalent of your Celsius temparature is: " + str(result))

    except:
        print("Enter a valid number for temparature!")
else:
    print("Please choose either a C or an F")

 	
