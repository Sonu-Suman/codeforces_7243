import math

def solve(l):
    d1 = math.ceil(l[0]/l[2])
    d2 = math.ceil(l[1]/l[2])
    return d1*d2


s = [i for i in map(int, input("").split())]
print(solve(s))