import math

def solve(s):
    s.sort(reverse=False)
    if s[0]*2 > s[1]:
        return int(math.pow((s[0]*2), 2))
    else:
        d = s[1]
        return int(math.pow(d, 2))


n = int(input("Enter your number: "))
for _ in range(n):
    s = [i for i in map(int, input("Enter your list number: ").split())]
    if 2 != len(s):
        print("You give wrong input.")
    else:
        print(solve(s))