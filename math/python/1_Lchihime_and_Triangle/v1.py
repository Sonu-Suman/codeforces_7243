import math


def solve(s):
    for j in range(s[1], s[2] + 1):
        for k in range(s[0], s[1] + 1):
            i = math.sqrt(math.pow(j, 2) + math.pow(k, 2))
            if i == int(i):
                if s[2] <= i <= (s[3] + 1):
                    return int(i), j, k

    for i in range(s[2], (s[3] + 1)):
        for j in range(s[1], s[2] + 1):
            for k in range(s[0], s[1] + 1):
                if i == j == k:
                    return i, j, k


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your number: ").split())]
    print(solve(s))