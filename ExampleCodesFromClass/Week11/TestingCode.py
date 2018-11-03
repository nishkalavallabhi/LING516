

import random,string,re

def gen_random_string(): #generates a random 6 character string, to be used as password
    return ''.join(random.choice(string.ascii_lowercase) for x in range(6))

def gen_random_string2():
    result = []
    for x in range(6):
        y = random.choice(string.ascii_lowercase)
        result.append(y)
    return ''.join(result)

def sorted_nicely(l):#sorts alpha-numeric strings
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

#print(sorted_nicely(["user12","userrr22sf", "irauarar"]))

print(gen_random_string2())
#print(random.choice(string.ascii_lowercase))
