
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
            if tempNumber >= -58.0 and tempNumber <=58.0:
                fahren = ctof(tempNumber)
                print("The Fahrenheit equivalent of your Celsius temparature is: " + str(fahren))
            else:
                print("Please enter some realistic Celsius temparature. No one saw " + str(tempNumber)
                      + " celsius temparature anywhere before!!")
        else:
            if tempNumber >= -130.0 and tempNumber <= 130.0:
                celsius= ftoc(tempNumber)
                print("The Celsius equivalent of your Fahrenheit temparature is: " + str(celsius))
            else:
                print("Please enter some realistic Fahrenheit temparature. No one saw " + str(tempNumber)
                      + " Fahrenheit temparature anywhere before!")
    except:
        print("Enter a valid number for temparature!")
else:
    print("Please choose either a C or an F")
