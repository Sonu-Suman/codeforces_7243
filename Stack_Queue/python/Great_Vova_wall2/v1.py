import numpy as np


def solve(l):
    if len(l) == l.count(l[0]):
        return "YES"

    s = min(l)
    g = l.count(s)
    print("G: ", g)
    i = l.index(s)
    print("I: ", i)

    ma = l.copy()
    ma.sort(reverse=False)
    m = np.unique(ma)
    ne = m[1]

    va = ne - s

    # ind = l.index(m[1], i, -1)
    for k in l[i:i+s]:   # Here Something is wrong
        if ne < k:
            print("First No---------")
            return "NO"

    if g == 1:
        l[i] = va
        solve(l)
    else:
        i -= 1
        for _ in range(g):
            i += 1
            if l[i] == s:
                l[i] = va
            else:
                print("second no---------")
                return "NO"
        solve(l)



n = int(input("Enter your number of parts of wall: "))
l = [i for i in map(int, input("Enter your wall length: ").split())]
if n == len(l):
    print(solve(l))
else:
    print("This is not valid!")