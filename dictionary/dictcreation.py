print("Jesus is lord")

# creation of dictionary from two different and one nested 
# list and using different method 

# 1. using for loop 

keys = ['p', 'q', 'r']
values = [5, 10, 15]

d = {}
for i in range(len(keys)):       # limitation of this way is can't handle for repeated keys   
                                 
    if i < len(values):
        d[keys[i]] = values[i]
    else:
        d[keys[i]] = None

print(d)

# 2.using defaultdict from collection
from collections import defaultdict

keys = ['p', 'q', 'p']
values = [5, 10, 15]

d = defaultdict(list)

for key , value in zip(keys,values):
    d[key].append(value)

print(dict(d))

#3. using defaultdict  and zip_longest from collection and itertools respectively 

from collections import defaultdict
from itertools import zip_longest

keys = ['p', 'q', 'p']
values = [5, 10, 15,46]

d = defaultdict(list)

for key,value in zip_longest(keys,values,fillvalue=[]):
    d[key].append(value)

if len(values) > len(keys):
    d["leftover"].extend(values[len(keys):])

print(dict(d))

# 4. AS a option we can use dictionary comprehension method

keys = [1,2,3]
values = [1.2,1.3,1.4]

d={k:v for k,v in zip(keys,values)}

print(d)

# when it is one list but not nested using the enumration  is the best choice 
a = ["apple", "banana", "cherry"]

d = {ind :val for ind ,val in enumerate(a,start=1)}

print(d)

#-------------------------------------------------------------
#creating dictionary from string 
# one when it is ethier in json method or literal format

# a. using ast  from the collection 

import ast

s = "{'a': 1, 'b': 2, 'c': 3}"
d = ast.literal_eval(s)
print(d)

#b. using json 

import json

s = "{'a': 1, 'b': 2, 'c': 3}"
d = json.loads(s) # loads = string -> dict
print(d)          # dumps = dict -> string 

# 2. when it is custom dictionary

s = "a=1, b=2, c=3"

dic = [item.split("=") for item in s.split(",")]

dictionary = {key.strip():int(value.strip()) for key,value in dic}

print(dictionary)
