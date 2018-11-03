

def function_without_return(somestring):
    print(somestring[::2])

def function_with_return(somestring):
    return somestring[::2]


inp = "pythonprogram"

#print(inp[::2])

#print(function_without_return(inp))

function_output = function_with_return(inp)
print(function_output)

#print("This function returns: ", function_without_return(inp))


#print("This function returns: ", function_with_return(inp))
