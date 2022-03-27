
from itertools import product
from collections import Counter


def solve(s):
    if s[0] == 1:
        return s[1]**2
    elif s[1] == 1:
        return s[1]
    else:
        l = []
        for i in range(s[1]+1):
            l.append(i)

        m = []
        g = []
        for i in list(product(l, repeat=s[0])):
            if s[1] == sum(i):
                min_l = int(s[0]/2)+1
                if len(Counter(i)) <= min_l:
                    g.append(i)
                    su = 0
                    for j in i:
                        su += (j**2)
                    m.append(su)

        return min(m), g[m.index(min(m))]




n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))