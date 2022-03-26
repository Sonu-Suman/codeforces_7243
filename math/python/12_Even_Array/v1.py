import math

def solve(a, s):
    k = [0]
    m = [s[0] % 2]
    if a == 1:
        if k == m:
            return 0
        else:
            return -1

    j = 0
    for i in range(1, len(s)):
        if k[-1] != m[-1]:
            j += 1
        k.append(i % 2)
        m.append(s[i] % 2)
    return math.ceil(j / 2)


n = int(input("Enter your number: "))
for _ in range(n):
    a = int(input("Enter your number: "))
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if a != len(s):
        print("You give wrong input.")
    else:
        print(solve(a, s))