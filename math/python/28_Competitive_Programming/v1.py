from itertools import combinations, permutations


def solve(a, l):
    if int(l) == 0:
        return 'red'
    if int(l) % 60 == 0:
        return 'red'
    else:
        for f in list(permutations(l)):
            k = 0
            for j in f:
                k = k * 10 + int(j)
            if k % 60 == 0:
                return 'red'

    return 'cyan'



n = int(input("Enter your number: "))
l = []
for _ in range(n):
    s = input("Enter number:")
    print(solve(n, s))