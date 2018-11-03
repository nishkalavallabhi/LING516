import random
sum = 0
for i in range(10):
    randNum = random.randint(1,1000)
    sum += randNum
    print(randNum)
print("Sum of all the 10 generated numbers so far is: " + str(sum))
