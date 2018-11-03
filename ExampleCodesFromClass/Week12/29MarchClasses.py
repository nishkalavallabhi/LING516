#Reading user input as a list directly
def readList():
    inp = list(input("Enter a list of numbers: ").replace(",",""))
    #Any of the below definitions of mylist variable do the same thing.
    #mylist = list(map(int,inp[1:-1]))
    #mylist = [int(i) for i in inp[1:-1]]
    mylist = []
    for item in inp[1:-1]:
        mylist.append(int(item))

    print(mylist)
    return mylist

def readList2():
    inp = input("Enter a list of numbers: ")[1:-1].split(",")
    return([int(i) for i in inp])


#Question: What is the difference between readList() and readList2()?

#Modified version of: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def NonRecursiveBinarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = -1
    while first <= last and found < 0:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def useBinarySearch():
    mylist = sorted(readList2())
    print(mylist)
    item = int(input("Enter an number to search in this list: "))
    result = NonRecursiveBinarySearch(mylist,item)
    if(result < 0):
        print("Item not found.")
    else:
        print("Item is found at index", str(result), "in this list")

#readList()
#readList2()
#useBinarySearch()
