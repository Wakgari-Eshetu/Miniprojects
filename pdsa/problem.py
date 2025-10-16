# Finding closest number to  n and divisible  by m 

def check(n,m):
    que = n//m
    n1 = que *m
    n2 = que*m

    return n1 if abs(n-n1) < abs(n-n2) else n2

print(check(13,4))

# dice problem 

def check(n:int)->int:
    return 7-n 

print(check(2))

# nth term of AP from first two terms

def check(a1,a2,n)->int:
    difference = a2 - a1
    return a1+(n-1)*difference

print(check(1,3,10))
