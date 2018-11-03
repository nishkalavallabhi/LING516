def funct1(lst1):
    lst1.sort()

def funct2(lst1):
    lst2 = lst1[:]
    lst2.sort(reverse=True)
    return lst2


lst1 = [9,8,7,12,1,2]
print(funct1(lst1))
print(lst1)
print(funct2(lst1))
print(lst1)
