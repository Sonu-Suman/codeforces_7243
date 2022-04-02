import math

def solve(s):
    return (s[1]+((s[0]-1)*9))



n = int(input(""))
for _ in range(n):
    s = [i for i in map(int, input("").split())]
    print(solve(s))