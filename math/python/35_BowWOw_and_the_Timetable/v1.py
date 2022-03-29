import math

def solve(l):
    l = int(l, 2)

    s = 0
    for i in range(51):
        if math.pow(4, i) < l:
            s += 1
    return s


print(solve(input("Enter your number in binary format: ")))