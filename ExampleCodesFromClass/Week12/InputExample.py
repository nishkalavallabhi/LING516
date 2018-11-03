num_list= [int(x) for x in input("Please Enter numbers and separate "
                                 "them by comma and press Enter: ").split(",")]

inp = input("Please Enter numbers and separate them by comma and press Enter: ")
nums = inp.split()
actualnums = []
for i in nums:
    actualnums.append(int(i))
