import math


def solve(s):
    return math.ceil((s[0]-2)/s[1])+1



n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your number: ").split())]
    print(solve(s))