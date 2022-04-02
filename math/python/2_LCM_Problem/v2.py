import math


def solve(s):
    for i in range(s[0], math.ceil(s[1]/2)+1):
        x = i
        for j in range(x + 1, s[1] + 1):
            y = j
            l = math.lcm(x, y)
            if s[0] <= l <= s[1]:
                return x, y

    return -1, -1


n = int(input(""))
for _ in range(n):
    s = [i for i in map(int, input("").split())]
    print(solve(s))