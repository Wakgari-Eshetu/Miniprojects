# sets : unordered , no duplicate , mutable ,unidexed , any datatype
# creating using curly braces  

set = {1,2,3,4}
print(max(set))

# using set() functions

#since they are mutable we add single and multiple values using add() and update() respectively 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# python set operation
# 1. union: combining sets to for other set
# using | or union() 
print(A|B)
print()
print(A.union(B))
# 2. intersection: elements found in both set 
# using & or set.intersection 
print(A&B)
print()
print(A.intersection(B))
# 3.difference: elements found inone but not in the other 
#A-B: elements found in A but not in B. How using "-" or set.difference()

print(A-B)
print()
print(B-A)
# 4.symetric difference :elements found in either of the sets 
# using "^" or set.symmetric_differnce()

print(A^B)
print()
print(A.symmetric_difference(B)) 

